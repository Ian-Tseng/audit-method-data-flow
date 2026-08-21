from __future__ import annotations

import ast
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "skills" / "audit-method-data-flow"
SKILL = (PACKAGE / "SKILL.md").read_text(encoding="utf-8")


class SkillContractTests(unittest.TestCase):
    def test_frontmatter_identity_and_license(self):
        match = re.match(r"\A---\n(.*?)\n---\n", SKILL, re.DOTALL)
        self.assertIsNotNone(match)
        frontmatter = match.group(1)
        self.assertIn("name: audit-method-data-flow", frontmatter)
        self.assertIn("license: MIT", frontmatter)
        description = next(
            line for line in frontmatter.splitlines() if line.startswith("description:")
        )
        self.assertIn("claim chains", description)
        self.assertIn("figures, tables, and slide workflows", description)

    def test_required_references_are_routed_from_skill(self):
        for name in (
            "claim-chain-clarity.md",
            "figure-table-clarity.md",
            "paper-terminology-contract.md",
        ):
            self.assertIn(f"references/{name}", SKILL)
            self.assertTrue((PACKAGE / "references" / name).is_file())

    def test_method_flow_and_claim_chain_have_complete_anchors(self):
        for anchor in (
            "Input:",
            "Dataset/source:",
            "Partition/batch:",
            "Label access:",
            "Model/component:",
            "Transformation:",
            "Output:",
            "Evaluation:",
            "Boundary:",
        ):
            self.assertIn(anchor, SKILL)
        chain = (PACKAGE / "references" / "claim-chain-clarity.md").read_text(
            encoding="utf-8"
        )
        for anchor in (
            "Problem",
            "Research question",
            "Protocol",
            "Operation and output",
            "Result and counterevidence",
            "Interpretation and boundary",
        ):
            self.assertIn(anchor, chain)

    def test_terminology_contract_required_fields_and_statuses(self):
        contract = (PACKAGE / "references" / "paper-terminology-contract.md").read_text(
            encoding="utf-8"
        )
        for field in (
            "Canonical term",
            "Definition",
            "Symbol",
            "Role",
            "Parent",
            "Input/output",
            "Changed/fixed conditions",
            "Scope",
            "Allowed aliases",
            "Forbidden aliases",
            "Source mapping",
            "Version",
        ):
            self.assertIn(f"| {field} |", contract)
        for status in (
            "planned",
            "implemented",
            "executed",
            "structurally validated",
            "artifact-validated",
            "scientifically evaluated",
            "paper-eligible",
            "historical",
        ):
            self.assertIn(status, SKILL)

    def test_figure_typography_contract_has_source_roles_and_validation(self):
        display = (PACKAGE / "references" / "figure-table-clarity.md").read_text(
            encoding="utf-8"
        )
        for anchor in (
            "## Figure typography roles",
            "Direct Nature requirement",
            "Project-specific renderer contract",
            "Arial",
            "Helvetica",
            "Symbol",
            "text-font role",
            "math-font role",
            "declared math fragments",
            "glyph coverage",
            "baseline alignment",
            "one restrained body font",
        ):
            self.assertIn(anchor, display)
        self.assertIn("Nature-specific rather than universal", display)

    def test_agent_metadata_invokes_exact_skill(self):
        agent = (PACKAGE / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn('display_name: "Audit Method Data Flow"', agent)
        self.assertIn("$audit-method-data-flow", agent)

    def test_optional_docx_helper_dependency_is_explicit(self):
        self.assertIn("separately installed `audit-venue-submission`", SKILL)
        self.assertIn("That helper is not bundled here", SKILL)

    def test_substantive_audit_code_has_no_network_or_process_transport(self):
        forbidden = {
            "http",
            "httpx",
            "requests",
            "socket",
            "subprocess",
            "urllib",
        }
        python_files = [PACKAGE / "scripts" / "package_integrity.py"]
        for path in python_files:
            tree = ast.parse(path.read_text(encoding="utf-8"))
            imports = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imports.update(alias.name.split(".", 1)[0] for alias in node.names)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imports.add(node.module.split(".", 1)[0])
            self.assertTrue(forbidden.isdisjoint(imports), f"{path}: {imports & forbidden}")

    def test_lifecycle_transport_is_isolated_and_owner_bound(self):
        updater = (PACKAGE / "scripts" / "update_policy.py").read_text(encoding="utf-8")
        emitter = (PACKAGE / "scripts" / "skill_outcome.py").read_text(encoding="utf-8")
        self.assertIn("_internal.safe_process", updater)
        self.assertIn('"Ian-Tseng"', emitter)
        self.assertNotIn("project", emitter.lower())

    def test_evidence_boundaries_are_not_overclaimed(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for phrase in (
            "scientific validity",
            "native rendering",
            "consent-gated managed updater",
            "telemetry",
        ):
            self.assertIn(phrase, readme)
        publishing = (ROOT / "PUBLISHING.md").read_text(encoding="utf-8")
        self.assertIn("Installation does not prove client discovery or invocation", publishing)
        self.assertIn("never rewrite a tag", publishing)


if __name__ == "__main__":
    unittest.main()
