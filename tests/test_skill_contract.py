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

    def test_first_reader_inference_gate_is_explicit(self):
        contract = (PACKAGE / "references" / "paper-terminology-contract.md").read_text(
            encoding="utf-8"
        )
        skill_folded = SKILL.casefold()
        contract_folded = contract.casefold()
        for anchor in (
            "Eliminate first-reader inference",
            "first substantive use",
            "plain-language definition",
            "definition inventory",
            "semantic relation",
            "unresolved inference",
        ):
            self.assertIn(anchor.casefold(), skill_folded)
        for anchor in (
            "## First-reader inference gate",
            "first abstract use",
            "first body use",
            "local definition locator",
            "required relation",
            "unresolved inference",
        ):
            self.assertIn(anchor.casefold(), contract_folded)

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

        display_folded = " ".join(display.split())
        for anchor in (
            "absolute comparator and method values",
            "define the subtraction order",
            "same evaluation rows",
            "nonmatched descriptive quantities",
            "do not imply an intervention effect",
            "target-batch size",
            "higher-precision run summaries",
            "row-matching status",
        ):
            self.assertIn(anchor, display_folded)

    def test_validate_contract_requires_bounded_convergent_rechecks(self):
        skill_folded = " ".join(SKILL.casefold().split())
        for anchor in (
            "convergent repair loop",
            "rebuild and reload every affected reader-facing artifact",
            "invalidating the preceding pass",
            "restart every applicable source",
            "limit one audit run to three repair-and-recheck cycles",
            "one complete pass makes no further repair",
            "pending, with its reason, required evidence, and resumption condition",
        ):
            self.assertIn(anchor, skill_folded)

    def test_semantic_universality_gate_distinguishes_standard_and_project_terms(self):
        contract = (PACKAGE / "references" / "paper-terminology-contract.md").read_text(
            encoding="utf-8"
        )
        skill_folded = SKILL.casefold()
        contract_folded = contract.casefold()
        for anchor in (
            "semantic universality gate",
            "field-standard",
            "project-specific",
            "plain protocol description",
            "not located in the checked sources",
        ):
            self.assertIn(anchor, skill_folded)
            self.assertIn(anchor, contract_folded)

    def test_citation_closure_and_counted_groups_are_explicit(self):
        contract = (PACKAGE / 'references' / 'paper-terminology-contract.md').read_text(
            encoding='utf-8'
        )
        skill_folded = ' '.join(SKILL.casefold().split())
        contract_folded = ' '.join(contract.casefold().split())
        for anchor in (
            'citation closure',
            'citation class',
            'reader-facing citation',
            'first substantive use',
            'matching citation key or reference-list entry',
            'counted or collective component labels',
            'name every stable member',
        ):
            self.assertIn(anchor, skill_folded)
        for anchor in (
            'citation closure',
            'citation class',
            'reader-facing citation',
            'first substantive use',
            'matching citation key or reference-list entry',
            'counted and collective labels',
            'name every stable member',
        ):
            self.assertIn(anchor, contract_folded)
        for anchor in (
            'active artifact inventory',
            'independently readable',
            'technical appendices',
            'release guides',
            'generated archives',
        ):
            self.assertIn(anchor, skill_folded)
            self.assertIn(anchor, contract_folded)

    def test_recommended_updates_default_to_owner_bound_local_preview(self):
        skill_folded = ' '.join(SKILL.casefold().split())
        for anchor in (
            'recommended update',
            'Ian-Tseng/audit-method-data-flow',
            'local contribution preview',
            'public submission',
            'exact approval',
            'do not manufacture',
        ):
            self.assertIn(anchor.casefold(), skill_folded)

    def test_default_paper_quality_gate_is_recursive_and_auditable(self):
        skill_folded = ' '.join(SKILL.casefold().split())
        for anchor in (
            'default paper-quality gate',
            'first-reader clarity and define-before-use',
            'smooth, lean prose without redundant wording',
            'claim, protocol, evidence, counterevidence, and boundary consistency',
            'semantic universality classifications and canonical terminology',
            'figure and table callouts, captions, column labels, metric directions, and final-size readability',
            'run-aware docx checks and rendered pdf inspection',
            'm1-m18',
            's1-s31',
            'independent fresh-reader review',
            'pass, n/a, or pending',
            'every applicable item is pass or n/a',
            'any pending item keeps the gate open',
            'zero critical or major findings',
            'keep the gate open',
            'cycle count does not establish closure',
            'reason, required evidence, and resumption condition',
            'what exact output does the component produce?',
            'the auditor visually inspects',
            'when a terminology contract is in scope',
        ):
            self.assertIn(anchor, skill_folded)

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
