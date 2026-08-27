#!/usr/bin/env python3
"""Validate a local, machine-readable method/claim/evidence contract."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import stat
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


MAX_BYTES = 256 * 1024
IDENTIFIER = re.compile(r"^[a-z][a-z0-9-]{0,63}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
ROOT_KEYS = {"schema_version", "authorization", "branches", "claims", "evidence"}
AUTH_KEYS = {
    "authorized_to_process",
    "confidentiality_policy_checked",
    "external_services_allowed",
    "retention_decision",
    "human_verifier",
}
BRANCH_FIELDS = (
    "input",
    "dataset_source",
    "partition_or_batch",
    "label_access",
    "model_component",
    "transformation",
    "output",
    "evaluation",
    "boundary",
)
BRANCH_KEYS = {"id", *BRANCH_FIELDS}
CLAIM_FIELDS = (
    "problem",
    "research_question",
    "protocol",
    "operation_output",
    "result",
    "counterevidence",
    "interpretation_boundary",
)
CLAIM_KEYS = {"id", "branch_id", "section_locators", *CLAIM_FIELDS}
EVIDENCE_KEYS = {
    "id",
    "claim_id",
    "kind",
    "sha256",
    "locator_id",
    "locator_verified",
    "verified_by",
    "verified_at",
}


class ContractError(ValueError):
    pass


def _exact_keys(value: dict[str, Any], expected: set[str], scope: str) -> None:
    actual = set(value)
    if actual != expected:
        missing = sorted(expected - actual)
        unknown = sorted(actual - expected)
        raise ContractError(f"{scope} keys differ; missing={missing}; unknown={unknown}")


def _string(value: Any, scope: str) -> str:
    if not isinstance(value, str) or not value.strip() or len(value) > 500:
        raise ContractError(f"{scope} must be a non-empty string of at most 500 characters")
    return value.strip()


def _identifier(value: Any, scope: str) -> str:
    text = _string(value, scope)
    if not IDENTIFIER.fullmatch(text):
        raise ContractError(f"{scope} must be a lowercase stable identifier")
    return text


def _verification_time(value: Any, scope: str) -> str | None:
    text = _string(value, scope)
    if text.casefold() == "unresolved":
        return None
    try:
        parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ContractError(f"{scope} must be an ISO 8601 timestamp") from exc
    if parsed.tzinfo is None:
        raise ContractError(f"{scope} must include a timezone")
    return text


def _list(value: Any, scope: str, maximum: int) -> list[Any]:
    if not isinstance(value, list) or not value or len(value) > maximum:
        raise ContractError(f"{scope} must contain 1..{maximum} items")
    return value


def _canonical_digest(contract: dict[str, Any]) -> str:
    payload = json.dumps(contract, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def validate_contract(contract: Any) -> dict[str, Any]:
    if not isinstance(contract, dict):
        raise ContractError("contract must be an object")
    _exact_keys(contract, ROOT_KEYS, "contract")
    if contract["schema_version"] != 1:
        raise ContractError("schema_version must equal 1")

    authorization = contract["authorization"]
    if not isinstance(authorization, dict):
        raise ContractError("authorization must be an object")
    _exact_keys(authorization, AUTH_KEYS, "authorization")
    for field in ("authorized_to_process", "confidentiality_policy_checked", "external_services_allowed"):
        if type(authorization[field]) is not bool:
            raise ContractError(f"authorization.{field} must be boolean")
    if not isinstance(authorization["retention_decision"], str) or authorization["retention_decision"] not in {"ephemeral", "project_controlled", "owner_defined"}:
        raise ContractError("authorization.retention_decision is unsupported")
    human_verifier = _string(authorization["human_verifier"], "authorization.human_verifier")

    findings: list[dict[str, str]] = []
    if not authorization["authorized_to_process"]:
        findings.append({"code": "PROCESSING_NOT_AUTHORIZED", "scope": "authorization", "item_id": "authorization"})
    if not authorization["confidentiality_policy_checked"]:
        findings.append({"code": "CONFIDENTIALITY_POLICY_UNCHECKED", "scope": "authorization", "item_id": "authorization"})
    if authorization["external_services_allowed"]:
        findings.append({"code": "EXTERNAL_PROCESSING_NOT_ALLOWED", "scope": "authorization", "item_id": "authorization"})
    if human_verifier.casefold() == "unresolved":
        findings.append({"code": "HUMAN_VERIFIER_UNRESOLVED", "scope": "authorization", "item_id": "authorization"})

    branches = _list(contract["branches"], "branches", 128)
    branch_ids: set[str] = set()
    for item in branches:
        if not isinstance(item, dict):
            raise ContractError("each branch must be an object")
        _exact_keys(item, BRANCH_KEYS, "branch")
        item_id = _identifier(item["id"], "branch.id")
        if item_id in branch_ids:
            raise ContractError(f"duplicate branch id: {item_id}")
        branch_ids.add(item_id)
        for field in BRANCH_FIELDS:
            value = _string(item[field], f"branch.{field}")
            if value.casefold() == "unresolved":
                findings.append({"code": "UNRESOLVED_FIELD", "scope": "branch", "item_id": item_id, "field": field})

    claims = _list(contract["claims"], "claims", 256)
    claim_ids: set[str] = set()
    for item in claims:
        if not isinstance(item, dict):
            raise ContractError("each claim must be an object")
        _exact_keys(item, CLAIM_KEYS, "claim")
        item_id = _identifier(item["id"], "claim.id")
        if item_id in claim_ids:
            raise ContractError(f"duplicate claim id: {item_id}")
        claim_ids.add(item_id)
        branch_id = _identifier(item["branch_id"], "claim.branch_id")
        if branch_id not in branch_ids:
            raise ContractError(f"claim {item_id} names an unknown branch")
        for field in CLAIM_FIELDS:
            value = _string(item[field], f"claim.{field}")
            if value.casefold() == "unresolved":
                findings.append({"code": "UNRESOLVED_FIELD", "scope": "claim", "item_id": item_id, "field": field})
        locators = _list(item["section_locators"], "claim.section_locators", 20)
        for locator in locators:
            if _string(locator, "claim.section_locator").casefold() == "unresolved":
                findings.append({"code": "UNRESOLVED_FIELD", "scope": "claim", "item_id": item_id, "field": "section_locators"})

    evidence = _list(contract["evidence"], "evidence", 512)
    evidence_ids: set[str] = set()
    evidenced_claims: set[str] = set()
    for item in evidence:
        if not isinstance(item, dict):
            raise ContractError("each evidence item must be an object")
        _exact_keys(item, EVIDENCE_KEYS, "evidence")
        item_id = _identifier(item["id"], "evidence.id")
        if item_id in evidence_ids:
            raise ContractError(f"duplicate evidence id: {item_id}")
        evidence_ids.add(item_id)
        claim_id = _identifier(item["claim_id"], "evidence.claim_id")
        if claim_id not in claim_ids:
            raise ContractError(f"evidence {item_id} names an unknown claim")
        if not isinstance(item["kind"], str) or item["kind"] not in {"artifact_hash", "table_row", "figure_panel", "source_locator", "execution_receipt"}:
            raise ContractError(f"evidence {item_id} has unsupported kind")
        if not isinstance(item["sha256"], str) or not SHA256.fullmatch(item["sha256"]):
            raise ContractError(f"evidence {item_id} has invalid sha256")
        locator_id = _identifier(item["locator_id"], f"evidence {item_id}.locator_id")
        if type(item["locator_verified"]) is not bool:
            raise ContractError(f"evidence {item_id}.locator_verified must be boolean")
        verifier = _string(item["verified_by"], f"evidence {item_id}.verified_by")
        verified_at = _verification_time(item["verified_at"], f"evidence {item_id}.verified_at")
        locator_complete = locator_id.casefold() != "unresolved"
        digest_complete = item["sha256"] != "0" * 64
        verification_complete = verifier.casefold() != "unresolved" and verified_at is not None
        if not locator_complete:
            findings.append({"code": "EVIDENCE_LOCATOR_UNRESOLVED", "scope": "evidence", "item_id": item_id})
        if not digest_complete:
            findings.append({"code": "EVIDENCE_DIGEST_UNRESOLVED", "scope": "evidence", "item_id": item_id})
        if verifier.casefold() == "unresolved":
            findings.append({"code": "EVIDENCE_VERIFIER_UNRESOLVED", "scope": "evidence", "item_id": item_id})
        if verified_at is None:
            findings.append({"code": "EVIDENCE_TIME_UNRESOLVED", "scope": "evidence", "item_id": item_id})
        if item["locator_verified"] and locator_complete and digest_complete and verification_complete:
            evidenced_claims.add(claim_id)
        if not item["locator_verified"]:
            findings.append({"code": "LOCATOR_UNVERIFIED", "scope": "evidence", "item_id": item_id})
    for claim_id in sorted(claim_ids - evidenced_claims):
        findings.append({"code": "CLAIM_WITHOUT_VERIFIED_EVIDENCE", "scope": "claim", "item_id": claim_id})

    blocked = any(item["scope"] == "authorization" for item in findings)
    return {
        "schema_version": 1,
        "status": "BLOCKED" if blocked else ("PARTIAL" if findings else "PASS"),
        "contract_digest_sha256": _canonical_digest(contract),
        "counts": {"branches": len(branches), "claims": len(claims), "evidence": len(evidence)},
        "findings": findings,
        "content_echoed": False,
        "external_processing": "not_performed",
    }


def _is_link_like(path: Path) -> bool:
    attributes = getattr(path.lstat(), "st_file_attributes", 0)
    reparse = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    return path.is_symlink() or bool(reparse and attributes & reparse)


def load_contract(path: Path) -> dict[str, Any]:
    if _is_link_like(path):
        raise ContractError("contract path must not be a symlink or reparse point")
    info = path.stat()
    if not stat.S_ISREG(info.st_mode) or info.st_size > MAX_BYTES:
        raise ContractError("contract must be a regular file no larger than 256 KiB")
    try:
        value = json.loads(path.read_bytes().decode("utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ContractError("contract is not readable UTF-8 JSON") from exc
    if not isinstance(value, dict):
        raise ContractError("contract must be an object")
    return value


def template() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "authorization": {
            "authorized_to_process": False,
            "confidentiality_policy_checked": False,
            "external_services_allowed": False,
            "retention_decision": "owner_defined",
            "human_verifier": "unresolved",
        },
        "branches": [{**{"id": "branch-main"}, **{field: "unresolved" for field in BRANCH_FIELDS}}],
        "claims": [{
            "id": "claim-1",
            "branch_id": "branch-main",
            **{field: "unresolved" for field in CLAIM_FIELDS},
            "section_locators": ["unresolved"],
        }],
        "evidence": [{
            "id": "evidence-1",
            "claim_id": "claim-1",
            "kind": "artifact_hash",
            "sha256": "0" * 64,
            "locator_id": "unresolved",
            "locator_verified": False,
            "verified_by": "unresolved",
            "verified_at": "unresolved",
        }],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("template")
    validate = commands.add_parser("validate")
    validate.add_argument("--contract", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        output = template() if args.command == "template" else validate_contract(load_contract(args.contract))
    except (ContractError, OSError) as exc:
        print(json.dumps({"status": "INVALID", "message": str(exc)}, sort_keys=True), file=sys.stderr)
        return 2
    print(json.dumps(output, ensure_ascii=False, sort_keys=True))
    return 0 if output.get("status") in {None, "PASS", "PARTIAL"} else 3


if __name__ == "__main__":
    raise SystemExit(main())
