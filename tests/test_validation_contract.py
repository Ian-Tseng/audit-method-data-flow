from __future__ import annotations

import copy
import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATION = ROOT / "validation"
ACCEPTED_MAP = VALIDATION / "component-map" / "accepted-map.json"


def canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def directory_digest(path: Path) -> str:
    entries = []
    for child in sorted(candidate for candidate in path.rglob("*") if candidate.is_file()):
        relative = child.relative_to(path)
        if "__pycache__" in relative.parts or child.suffix.lower() in {".pyc", ".pyo"}:
            continue
        entries.append({"path": relative.as_posix(), "sha256": sha256_file(child)})
    return sha256_bytes(canonical_bytes(entries))


def current_evidence_paths() -> tuple[Path, Path]:
    index = (VALIDATION / "README.md").read_text(encoding="utf-8")
    record_match = re.search(r"\(history/([^)]+\.json)\)", index)
    report_match = re.search(r"\(reports/([^)]+\.md)\)", index)
    if record_match is None or report_match is None:
        raise AssertionError("validation index does not identify current record/report")
    return (
        VALIDATION / "history" / record_match.group(1),
        VALIDATION / "reports" / report_match.group(1),
    )


class ValidationContractTests(unittest.TestCase):
    def test_receipt_count_matches_discovered_suite(self):
        receipt = json.loads(
            (VALIDATION / "release-candidate-test-receipt.json").read_text(
                encoding="utf-8"
            )
        )
        discovered = unittest.defaultTestLoader.discover(str(ROOT / "tests"))
        self.assertEqual(receipt["tests"]["tests_run"], discovered.countTestCases())
        self.assertEqual(receipt["tests"]["status"], "PASS")
        for field in ("failures", "errors", "skipped"):
            self.assertEqual(receipt["tests"][field], 0)

    def test_current_record_and_report_are_discoverable(self):
        record_path, report_path = current_evidence_paths()
        self.assertTrue(record_path.is_file())
        self.assertTrue(report_path.is_file())
        self.assertEqual(record_path.stem, report_path.stem)

    def test_accepted_map_integrity_and_sources_match_exact_bytes(self):
        accepted = json.loads(ACCEPTED_MAP.read_text(encoding="utf-8"))
        payload = copy.deepcopy(accepted)
        expected = payload.pop("integrity")["canonical_payload_sha256"]
        self.assertEqual(sha256_bytes(canonical_bytes(payload)), expected)
        for item in accepted["source_snapshot"]:
            source = ROOT / item["source"]
            self.assertTrue(item["exists"], item["source"])
            if item["kind"] == "file":
                actual = sha256_file(source)
            elif item["kind"] == "directory":
                actual = directory_digest(source)
            else:
                self.fail(f"unsupported current source kind: {item}")
            self.assertEqual(actual, item["sha256"], item["source"])

    def test_package_evidence_uses_cross_platform_file_granularity(self):
        accepted = json.loads(ACCEPTED_MAP.read_text(encoding="utf-8"))
        package_sources = [
            item
            for item in accepted["source_snapshot"]
            if item["source"].startswith("skills/audit-method-data-flow")
        ]
        self.assertTrue(package_sources)
        self.assertTrue(
            all(item["kind"] == "file" for item in package_sources),
            "package evidence must not depend on platform-specific Path ordering",
        )

    def test_current_record_integrity_map_binding_and_evidence_match(self):
        record_path, _ = current_evidence_paths()
        record = json.loads(record_path.read_text(encoding="utf-8"))
        payload = copy.deepcopy(record)
        expected = payload["integrity"].pop("canonical_payload_sha256")
        self.assertEqual(sha256_bytes(canonical_bytes(payload)), expected)
        accepted = json.loads(ACCEPTED_MAP.read_text(encoding="utf-8"))
        self.assertEqual(record["scan"]["accepted_map"]["map_id"], accepted["map_id"])
        self.assertEqual(
            record["scan"]["accepted_map"]["sha256"], sha256_file(ACCEPTED_MAP)
        )
        for item in record["evidence_items"]:
            source = item["source"]
            if source["kind"] != "file":
                continue
            self.assertEqual(item["freshness"], "current")
            self.assertEqual(sha256_file(ROOT / source["path"]), source["sha256"])

    def test_current_report_preserves_record_scope(self):
        record_path, report_path = current_evidence_paths()
        record = json.loads(record_path.read_text(encoding="utf-8"))
        report = report_path.read_text(encoding="utf-8")
        self.assertIn(record["scan"]["scan_id"], report)
        self.assertIn(record["integrity"]["canonical_payload_sha256"], report)
        self.assertIn("Scan status: **PARTIAL**", report)
        self.assertIn("have not yet been observed", report)


if __name__ == "__main__":
    unittest.main()
