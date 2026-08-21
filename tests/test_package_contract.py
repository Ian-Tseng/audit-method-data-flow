from __future__ import annotations

import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "skills" / "audit-method-data-flow"
MANIFEST = PACKAGE / "references" / "package-manifest.json"
INTEGRITY = PACKAGE / "scripts" / "package_integrity.py"


def load_integrity_module():
    spec = importlib.util.spec_from_file_location("package_integrity", INTEGRITY)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load package integrity helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def text_files(root: Path):
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in {
            ".cff",
            ".json",
            ".md",
            ".py",
            ".yaml",
            ".yml",
        }:
            yield path
    yield root / "LICENSE"


class PackageContractTests(unittest.TestCase):
    def test_release_identity_is_synchronized(self):
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        self.assertEqual(version, "0.1.2")
        package_version = json.loads(
            (PACKAGE / "references" / "package-version.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(package_version["skill_name"], "audit-method-data-flow")
        self.assertEqual(package_version["version"], version)
        for citation in (ROOT / "CITATION.cff", PACKAGE / "CITATION.cff"):
            content = citation.read_text(encoding="utf-8")
            self.assertIn(f'version: "{version}"', content)
            self.assertIn('date-released: "2026-08-21"', content)
            self.assertIn('license: "MIT"', content)
        self.assertEqual(
            (ROOT / "CITATION.cff").read_bytes(),
            (PACKAGE / "CITATION.cff").read_bytes(),
        )
        self.assertIn(f"## [{version}] - 2026-08-21", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"))

    def test_root_and_package_license_are_identical(self):
        self.assertEqual((ROOT / "LICENSE").read_bytes(), (PACKAGE / "LICENSE").read_bytes())
        self.assertIn("MIT License", (PACKAGE / "LICENSE").read_text(encoding="utf-8"))

    def test_manifest_verifies_and_detects_ordinary_file_drift(self):
        module = load_integrity_module()
        digest = module.verify_manifest(PACKAGE)
        self.assertRegex(digest, r"^[0-9a-f]{64}$")
        with tempfile.TemporaryDirectory() as temporary:
            copy = Path(temporary) / PACKAGE.name
            shutil.copytree(PACKAGE, copy)
            (copy / "LICENSE").write_text("changed\n", encoding="utf-8")
            with self.assertRaises(module.IntegrityError):
                module.verify_manifest(copy)

    def test_github_install_metadata_does_not_change_package_identity(self):
        module = load_integrity_module()
        for github_ref in ("refs/heads/main", "refs/tags/v0.1.2"):
            with self.subTest(github_ref=github_ref), tempfile.TemporaryDirectory() as temporary:
                copy = Path(temporary) / PACKAGE.name
                shutil.copytree(PACKAGE, copy)
                skill_path = copy / "SKILL.md"
                content = skill_path.read_text(encoding="utf-8")
                content = content.replace(
                    "license: MIT\n---",
                    "license: MIT\n"
                    "metadata:\n"
                    "  github-path: skills/audit-method-data-flow\n"
                    f"  github-ref: {github_ref}\n"
                    "  github-repo: https://github.com/Ian-Tseng/audit-method-data-flow\n"
                    "  github-tree-sha: 0123456789abcdef0123456789abcdef01234567\n"
                    "---",
                    1,
                )
                skill_path.write_text(content, encoding="utf-8")
                self.assertRegex(module.verify_manifest(copy), r"^[0-9a-f]{64}$")

    def test_wrong_or_unknown_github_update_origin_is_rejected(self):
        module = load_integrity_module()
        cases = {
            "wrong-repo": "  github-repo: https://github.com/example/audit-method-data-flow\n",
            "wrong-path": "  github-path: skills/other-skill\n",
            "wrong-ref": "  github-ref: refs/heads/untrusted\n",
            "bad-tree": "  github-tree-sha: not-a-commit\n",
            "unknown-key": "  github-owner: Ian-Tseng\n",
        }
        for name, replacement in cases.items():
            with self.subTest(name=name), tempfile.TemporaryDirectory() as temporary:
                copy = Path(temporary) / PACKAGE.name
                shutil.copytree(PACKAGE, copy)
                skill_path = copy / "SKILL.md"
                metadata = (
                    "metadata:\n"
                    "  github-path: skills/audit-method-data-flow\n"
                    "  github-ref: refs/heads/main\n"
                    "  github-repo: https://github.com/Ian-Tseng/audit-method-data-flow\n"
                    "  github-tree-sha: 0123456789abcdef0123456789abcdef01234567\n"
                )
                key = replacement.split(":", 1)[0].strip()
                if key in {"github-path", "github-ref", "github-repo", "github-tree-sha"}:
                    metadata = re.sub(rf"^  {key}:.*$", replacement.rstrip(), metadata, flags=re.MULTILINE)
                else:
                    metadata += replacement
                content = skill_path.read_text(encoding="utf-8").replace(
                    "license: MIT\n---", f"license: MIT\n{metadata}---", 1
                )
                skill_path.write_text(content, encoding="utf-8")
                with self.assertRaises(module.IntegrityError):
                    module.verify_manifest(copy)

    def test_top_level_github_metadata_is_rejected(self):
        module = load_integrity_module()
        with tempfile.TemporaryDirectory() as temporary:
            copy = Path(temporary) / PACKAGE.name
            shutil.copytree(PACKAGE, copy)
            skill_path = copy / "SKILL.md"
            content = skill_path.read_text(encoding="utf-8").replace(
                "license: MIT\n---",
                "license: MIT\ngithub-repo: https://github.com/Ian-Tseng/audit-method-data-flow\n---",
                1,
            )
            skill_path.write_text(content, encoding="utf-8")
            with self.assertRaises(module.IntegrityError):
                module.verify_manifest(copy)

    def test_package_root_link_is_rejected(self):
        module = load_integrity_module()
        with tempfile.TemporaryDirectory() as temporary:
            real = Path(temporary) / "real"
            link = Path(temporary) / "linked"
            shutil.copytree(PACKAGE, real)
            try:
                os.symlink(real, link, target_is_directory=True)
            except OSError as exc:
                self.skipTest(f"directory symlink unavailable: {exc}")
            with self.assertRaises(module.IntegrityError):
                module.verify_manifest(link)

    def test_package_root_reparse_check_runs_before_resolution(self):
        module = load_integrity_module()
        with mock.patch.object(module, "_is_link_like", wraps=module._is_link_like) as check:
            module.verify_manifest(PACKAGE)
        checked = [call.args[0] for call in check.call_args_list]
        self.assertIn(PACKAGE, checked)

    def test_text_is_valid_portable_utf8(self):
        private_path_patterns = (
            re.compile(r"(?i)[a-z]:\\users\\[^\\\r\n]+"),
            re.compile(r"/Users/[^/\r\n]+"),
        )
        seen = set()
        for path in text_files(PACKAGE):
            if path in seen or not path.exists():
                continue
            seen.add(path)
            content = path.read_text(encoding="utf-8")
            self.assertNotIn("\ufffd", content, path.as_posix())
            self.assertFalse(
                any("\ue000" <= character <= "\uf8ff" for character in content),
                path.as_posix(),
            )
            for pattern in private_path_patterns:
                self.assertIsNone(pattern.search(content), path.as_posix())

    def test_relative_markdown_links_resolve(self):
        link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
        for markdown in ROOT.rglob("*.md"):
            content = markdown.read_text(encoding="utf-8")
            for target in link_pattern.findall(content):
                target = target.strip().strip("<>").split("#", 1)[0]
                if not target or "://" in target or target.startswith("mailto:"):
                    continue
                destination = (markdown.parent / target).resolve()
                self.assertTrue(destination.exists(), f"{markdown}: {target}")

    def test_source_ledger_and_live_source_status_are_explicit(self):
        source = (ROOT / "SOURCE.md").read_text(encoding="utf-8")
        self.assertIn("owner explicitly authorized publication", source)
        self.assertIn("exactly these semantic source files", source)
        ledger = (PACKAGE / "references" / "figure-table-clarity.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Access date: **2026-08-21**", ledger)
        for url in (
            "https://research-figure-guide.nature.com/",
            "https://www.nature.com/nature-portfolio/for-authors/write",
            "https://neurips.cc/public/guides/PaperChecklist",
            "https://www.elsevier.support/publishing/answer/how-do-i-prepare-my-files-for-submission-in-editorial-manager",
        ):
            self.assertIn(url, ledger)
        self.assertIn("HTTP 403 to automated retrieval", ledger)
        self.assertIn("HTTP 502 to automated retrieval", ledger)
        self.assertIn("No new rule inferred", ledger)

    def test_integrity_cli_help_runs(self):
        result = subprocess.run(
            [sys.executable, "-X", "utf8", str(INTEGRITY), "--help"],
            cwd=ROOT,
            text=True,
            encoding="utf-8",
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("verify", result.stdout)

    def test_ci_is_cross_platform_pinned_and_utf8_explicit(self):
        workflow = (ROOT / ".github" / "workflows" / "validate.yml").read_text(
            encoding="utf-8"
        )
        for os_name in ("ubuntu-latest", "macos-latest", "windows-latest"):
            self.assertIn(os_name, workflow)
        self.assertRegex(workflow, r"actions/checkout@[0-9a-f]{40}")
        self.assertRegex(workflow, r"actions/setup-python@[0-9a-f]{40}")
        self.assertIn("python -X utf8", workflow)


if __name__ == "__main__":
    unittest.main()
