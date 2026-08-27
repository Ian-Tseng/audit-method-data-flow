from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "audit-method-data-flow" / "scripts" / "method_evidence_contract.py"


def load_module():
    spec = importlib.util.spec_from_file_location("method_evidence_contract", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def valid_contract() -> dict:
    return {
        "schema_version": 1,
        "authorization": {
            "authorized_to_process": True,
            "confidentiality_policy_checked": True,
            "external_services_allowed": False,
            "retention_decision": "project_controlled",
            "human_verifier": "owner",
        },
        "branches": [{
            "id": "branch-main",
            "input": "dataset-a",
            "dataset_source": "source-a",
            "partition_or_batch": "test-fold",
            "label_access": "held-out labels",
            "model_component": "encoder",
            "transformation": "embedding",
            "output": "scores",
            "evaluation": "metric-a",
            "boundary": "population-a",
        }],
        "claims": [{
            "id": "claim-1",
            "branch_id": "branch-main",
            "problem": "problem-anchor",
            "research_question": "question-anchor",
            "protocol": "protocol-anchor",
            "operation_output": "output-anchor",
            "result": "result-anchor",
            "counterevidence": "counter-anchor",
            "interpretation_boundary": "boundary-anchor",
            "section_locators": ["methods:branch-main", "results:claim-1"],
        }],
        "evidence": [{
            "id": "evidence-1",
            "claim_id": "claim-1",
            "kind": "artifact_hash",
            "sha256": "a" * 64,
            "locator_id": "artifact-main",
            "locator_verified": True,
            "verified_by": "owner",
            "verified_at": "2026-08-27T12:00:00Z",
        }],
    }


class MethodEvidenceContractTests(unittest.TestCase):
    def test_contract_passes_without_echoing_claim_text(self) -> None:
        module = load_module()
        contract = valid_contract()
        report = module.validate_contract(contract)
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(report["counts"], {"branches": 1, "claims": 1, "evidence": 1})
        self.assertEqual(report["findings"], [])
        rendered = json.dumps(report)
        self.assertNotIn("problem-anchor", rendered)
        self.assertNotIn("result-anchor", rendered)
        self.assertEqual(len(report["contract_digest_sha256"]), 64)

    def test_contract_blocks_unapproved_external_processing(self) -> None:
        module = load_module()
        contract = valid_contract()
        contract["authorization"]["external_services_allowed"] = True
        report = module.validate_contract(contract)
        self.assertEqual(report["status"], "BLOCKED")
        self.assertEqual(report["findings"], [{
            "code": "EXTERNAL_PROCESSING_NOT_ALLOWED",
            "scope": "authorization",
            "item_id": "authorization",
        }])

    def test_unresolved_chain_is_partial_and_reported_by_id(self) -> None:
        module = load_module()
        contract = valid_contract()
        contract["claims"][0]["counterevidence"] = "unresolved"
        report = module.validate_contract(contract)
        self.assertEqual(report["status"], "PARTIAL")
        self.assertEqual(report["findings"], [{
            "code": "UNRESOLVED_FIELD",
            "scope": "claim",
            "item_id": "claim-1",
            "field": "counterevidence",
        }])

    def test_all_authorization_gates_and_malformed_retention_fail_closed(self) -> None:
        module = load_module()
        for field, value, code in (
            ("authorized_to_process", False, "PROCESSING_NOT_AUTHORIZED"),
            ("confidentiality_policy_checked", False, "CONFIDENTIALITY_POLICY_UNCHECKED"),
            ("external_services_allowed", True, "EXTERNAL_PROCESSING_NOT_ALLOWED"),
        ):
            with self.subTest(field=field):
                contract = valid_contract()
                contract["authorization"][field] = value
                report = module.validate_contract(contract)
                self.assertEqual(report["status"], "BLOCKED")
                self.assertIn(code, [item["code"] for item in report["findings"]])
        contract = valid_contract()
        contract["authorization"]["retention_decision"] = []
        with self.assertRaises(module.ContractError):
            module.validate_contract(contract)

    def test_placeholder_digest_and_locator_never_count_as_verified_evidence(self) -> None:
        module = load_module()
        contract = valid_contract()
        contract["evidence"][0].update({
            "sha256": "0" * 64,
            "locator_id": "unresolved",
            "locator_verified": True,
        })
        report = module.validate_contract(contract)
        self.assertEqual(report["status"], "PARTIAL")
        codes = [item["code"] for item in report["findings"]]
        self.assertIn("EVIDENCE_LOCATOR_UNRESOLVED", codes)
        self.assertIn("EVIDENCE_DIGEST_UNRESOLVED", codes)
        self.assertIn("CLAIM_WITHOUT_VERIFIED_EVIDENCE", codes)

    def test_stable_locator_is_required_but_not_echoed(self) -> None:
        module = load_module()
        contract = valid_contract()
        contract["evidence"][0]["locator_id"] = "artifact-secret-row-7"
        report = module.validate_contract(contract)
        self.assertEqual(report["status"], "PASS")
        self.assertNotIn("artifact-secret-row-7", json.dumps(report))
        contract["evidence"][0]["locator_id"] = "Not stable"
        with self.assertRaises(module.ContractError):
            module.validate_contract(contract)

    def test_cli_validates_local_bounded_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "contract.json"
            path.write_text(json.dumps(valid_contract()), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "-X", "utf8", str(SCRIPT), "validate", "--contract", str(path)],
                cwd=ROOT,
                text=True,
                encoding="utf-8",
                capture_output=True,
                check=False,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["status"], "PASS")

    def test_unresolved_verification_metadata_cannot_pass(self) -> None:
        module = load_module()
        cases = (
            ("human_verifier", lambda value: value["authorization"].update({"human_verifier": "unresolved"}), "BLOCKED"),
            ("section_locator", lambda value: value["claims"][0].update({"section_locators": ["unresolved"]}), "PARTIAL"),
            ("verified_by", lambda value: value["evidence"][0].update({"verified_by": "unresolved"}), "PARTIAL"),
            ("verified_at", lambda value: value["evidence"][0].update({"verified_at": "unresolved"}), "PARTIAL"),
        )
        for name, mutate, expected in cases:
            with self.subTest(name=name):
                contract = valid_contract()
                mutate(contract)
                self.assertEqual(module.validate_contract(contract)["status"], expected)

    def test_invalid_evidence_kind_and_timestamp_are_structured_errors(self) -> None:
        module = load_module()
        for field, value in (("kind", []), ("verified_at", "2026-08-27")):
            with self.subTest(field=field):
                contract = valid_contract()
                contract["evidence"][0][field] = value
                with self.assertRaises(module.ContractError):
                    module.validate_contract(contract)

    def test_duplicate_and_dangling_relations_fail_closed(self) -> None:
        module = load_module()
        cases = (
            lambda value: value["branches"].append(dict(value["branches"][0])),
            lambda value: value["claims"][0].update({"branch_id": "missing-branch"}),
            lambda value: value["evidence"][0].update({"claim_id": "missing-claim"}),
            lambda value: value["evidence"].append(dict(value["evidence"][0])),
        )
        for mutate in cases:
            with self.subTest(case=repr(mutate)):
                contract = valid_contract()
                mutate(contract)
                with self.assertRaises(module.ContractError):
                    module.validate_contract(contract)

    def test_each_claim_requires_its_own_verified_evidence(self) -> None:
        module = load_module()
        contract = valid_contract()
        second = dict(contract["claims"][0])
        second["id"] = "claim-2"
        contract["claims"].append(second)
        report = module.validate_contract(contract)
        self.assertEqual(report["status"], "PARTIAL")
        self.assertIn(
            {"code": "CLAIM_WITHOUT_VERIFIED_EVIDENCE", "scope": "claim", "item_id": "claim-2"},
            report["findings"],
        )

    def test_cli_template_partial_blocked_and_invalid_outcomes(self) -> None:
        template = subprocess.run(
            [sys.executable, "-X", "utf8", str(SCRIPT), "template"],
            cwd=ROOT,
            text=True,
            encoding="utf-8",
            capture_output=True,
            check=False,
        )
        self.assertEqual(template.returncode, 0, template.stderr)
        self.assertEqual(json.loads(template.stdout)["schema_version"], 1)

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            cases = []
            partial = valid_contract()
            partial["claims"][0]["result"] = "unresolved"
            cases.append(("partial", partial, 0, "PARTIAL"))
            blocked = valid_contract()
            blocked["authorization"]["authorized_to_process"] = False
            cases.append(("blocked", blocked, 3, "BLOCKED"))
            invalid = valid_contract()
            invalid["evidence"][0]["kind"] = []
            cases.append(("invalid", invalid, 2, "INVALID"))
            for name, contract, returncode, status in cases:
                with self.subTest(name=name):
                    path = root / f"{name}.json"
                    path.write_text(json.dumps(contract), encoding="utf-8")
                    result = subprocess.run(
                        [sys.executable, "-X", "utf8", str(SCRIPT), "validate", "--contract", str(path)],
                        cwd=ROOT,
                        text=True,
                        encoding="utf-8",
                        capture_output=True,
                        check=False,
                    )
                    self.assertEqual(result.returncode, returncode, result.stderr)
                    stream = result.stdout if returncode in {0, 3} else result.stderr
                    self.assertEqual(json.loads(stream)["status"], status)

    def test_file_boundary_rejects_malformed_and_oversized_inputs(self) -> None:
        module = load_module()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            malformed = root / "malformed.json"
            malformed.write_bytes(b"{")
            oversized = root / "oversized.json"
            oversized.write_bytes(b"x" * (module.MAX_BYTES + 1))
            for path in (malformed, oversized, root):
                with self.subTest(path=path.name):
                    with self.assertRaises(module.ContractError):
                        module.load_contract(path)

    def test_file_boundary_rejects_actual_symlink_and_reparse_attribute(self) -> None:
        module = load_module()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "target.json"
            target.write_text(json.dumps(valid_contract()), encoding="utf-8")
            linked = root / "linked.json"
            try:
                linked.symlink_to(target)
            except OSError as exc:
                self.skipTest(f"symlink creation unavailable: {exc}")
            self.assertTrue(module._is_link_like(linked))
            with self.assertRaises(module.ContractError):
                module.load_contract(linked)

        reparse = getattr(module.stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
        candidate = Path("reparse-contract.json")
        with mock.patch.object(Path, "lstat", return_value=SimpleNamespace(st_file_attributes=reparse)), mock.patch.object(Path, "is_symlink", return_value=False):
            self.assertTrue(module._is_link_like(candidate))


if __name__ == "__main__":
    unittest.main()
