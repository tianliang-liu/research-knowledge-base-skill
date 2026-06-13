from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    REPO_ROOT
    / "skill"
    / "research-knowledge-base"
    / "scripts"
    / "init_knowledge_base.py"
)

CORE_DIRECTORIES = (
    "01_Literature",
    "02_Projects",
    "03_Topics",
    "04_Methods_Concepts",
    "05_Synthesis",
    "90_Templates",
)

TEMPLATE_FILES = (
    "文献笔记模板.md",
    "综述文献笔记模板.md",
    "Project模板.md",
    "Topic_MOC模板.md",
    "Method_Concept模板.md",
    "Synthesis模板.md",
    "Zotero实时追问模板.md",
)


def run_initializer(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


class InitializeKnowledgeBaseTests(unittest.TestCase):
    def test_creates_named_knowledge_base_from_bundled_template(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            destination = Path(temp_dir)
            result = run_initializer(
                "--destination",
                str(destination),
                "--name",
                "Demo Research Knowledge Base",
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            target = destination / "Demo Research Knowledge Base"
            self.assertTrue(target.is_dir())
            for directory in CORE_DIRECTORIES:
                self.assertTrue((target / directory).is_dir(), directory)
            for filename in TEMPLATE_FILES:
                self.assertTrue((target / "90_Templates" / filename).is_file(), filename)
            self.assertIn("CREATED", result.stdout)

    def test_refuses_existing_non_empty_target_without_merge(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir) / "Existing Knowledge Base"
            target.mkdir()
            existing = target / "personal-note.md"
            existing.write_text("keep me", encoding="utf-8")

            result = run_initializer(
                "--destination",
                temp_dir,
                "--name",
                target.name,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(existing.read_text(encoding="utf-8"), "keep me")
            self.assertIn("--merge", result.stderr)

    def test_merge_copies_missing_files_without_overwriting_existing_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir) / "Existing Knowledge Base"
            target.mkdir()
            readme = target / "README.md"
            readme.write_text("custom content", encoding="utf-8")

            result = run_initializer(
                "--destination",
                temp_dir,
                "--name",
                target.name,
                "--merge",
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(readme.read_text(encoding="utf-8"), "custom content")
            self.assertTrue((target / "01_Literature").is_dir())
            self.assertTrue(
                (target / "90_Templates" / "文献笔记模板.md").is_file()
            )
            self.assertIn("SKIPPED", result.stdout)

    def test_rejects_blank_name(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            result = run_initializer(
                "--destination",
                temp_dir,
                "--name",
                "   ",
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("name", result.stderr.lower())


if __name__ == "__main__":
    unittest.main()
