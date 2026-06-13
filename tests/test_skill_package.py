from __future__ import annotations

import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skill" / "research-knowledge-base"
VAULT_ROOT = SKILL_ROOT / "assets" / "vault-template"

REQUIRED_FILES = (
    SKILL_ROOT / "SKILL.md",
    SKILL_ROOT / "agents" / "openai.yaml",
    SKILL_ROOT / "scripts" / "init_knowledge_base.py",
    SKILL_ROOT / "references" / "architecture.md",
    SKILL_ROOT / "references" / "literature-workflow.md",
    SKILL_ROOT / "references" / "zotero-realtime-qa.md",
    SKILL_ROOT / "references" / "maintenance.md",
    VAULT_ROOT / "90_Templates" / "文献笔记模板.md",
    VAULT_ROOT / "90_Templates" / "综述文献笔记模板.md",
    VAULT_ROOT / "90_Templates" / "Project模板.md",
    VAULT_ROOT / "90_Templates" / "Topic_MOC模板.md",
    VAULT_ROOT / "90_Templates" / "Method_Concept模板.md",
    VAULT_ROOT / "90_Templates" / "Synthesis模板.md",
    VAULT_ROOT / "90_Templates" / "Zotero实时追问模板.md",
)

FRONTMATTER_TEMPLATES = (
    "文献笔记模板.md",
    "综述文献笔记模板.md",
    "Project模板.md",
    "Topic_MOC模板.md",
    "Method_Concept模板.md",
    "Synthesis模板.md",
)

PRIVATE_PATTERNS = (
    "/" + r"Users/",
    "/" + r"Volumes/",
    "乳腺癌" + "脑转移" + "脑脊液多组学项目",
    "CTC" + " 多组学测序项目",
    r"tianliang_liu" + r"@qq\.com",
)


def distributable_files() -> list[Path]:
    return sorted(path for path in SKILL_ROOT.rglob("*") if path.is_file())


class SkillPackageTests(unittest.TestCase):
    def test_required_skill_files_exist(self) -> None:
        for path in REQUIRED_FILES:
            self.assertTrue(path.is_file(), str(path.relative_to(REPO_ROOT)))

    def test_skill_contains_no_private_paths_or_domain_specific_projects(self) -> None:
        combined = "\n".join(
            path.read_text(encoding="utf-8") for path in distributable_files()
        )
        for pattern in PRIVATE_PATTERNS:
            self.assertIsNone(re.search(pattern, combined), pattern)

    def test_markdown_fences_are_balanced(self) -> None:
        for path in distributable_files():
            if path.suffix != ".md":
                continue
            fence_count = sum(
                1
                for line in path.read_text(encoding="utf-8").splitlines()
                if line.startswith("```")
            )
            self.assertEqual(
                fence_count % 2,
                0,
                f"Unbalanced Markdown fence in {path.relative_to(REPO_ROOT)}",
            )

    def test_frontmatter_is_present_in_note_templates(self) -> None:
        template_root = VAULT_ROOT / "90_Templates"
        for filename in FRONTMATTER_TEMPLATES:
            text = (template_root / filename).read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\n"), filename)
            self.assertIn("\n---\n", text[4:], filename)
            self.assertRegex(text, r"(?m)^type:\s*\S+")

    def test_real_time_question_template_requires_source_verification(self) -> None:
        text = (
            VAULT_ROOT / "90_Templates" / "Zotero实时追问模板.md"
        ).read_text(encoding="utf-8")
        for field in (
            "原文位置",
            "原文摘录",
            "我的实时问题",
            "AI 实时回答",
            "需要 Codex 核对",
            "Codex 核对结果",
            "回答依据",
        ):
            self.assertIn(field, text)

    def test_skill_md_stays_under_500_lines(self) -> None:
        lines = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8").splitlines()
        self.assertLess(len(lines), 500)

    def test_openai_default_prompt_names_the_skill(self) -> None:
        text = (SKILL_ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn("$research-knowledge-base", text)


if __name__ == "__main__":
    unittest.main()
