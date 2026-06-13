# Research Knowledge Base Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build, validate, and publish a domain-neutral Codex Skill for creating and maintaining an Obsidian + Zotero + Codex research knowledge base.

**Architecture:** Keep the installed Skill concise and move detailed workflows into four reference files. Bundle an Obsidian vault skeleton as assets and provide one standard-library Python script for deterministic initialization. Keep GitHub-facing bilingual documentation outside the installed Skill.

**Tech Stack:** Markdown, YAML, Python 3 standard library, `unittest`, Codex Skill validation scripts, Git, GitHub.

---

## File Map

```text
README.md
LICENSE
examples/initialization-profile.example.md
skill/research-knowledge-base/SKILL.md
skill/research-knowledge-base/agents/openai.yaml
skill/research-knowledge-base/scripts/init_knowledge_base.py
skill/research-knowledge-base/references/architecture.md
skill/research-knowledge-base/references/literature-workflow.md
skill/research-knowledge-base/references/zotero-realtime-qa.md
skill/research-knowledge-base/references/maintenance.md
skill/research-knowledge-base/assets/vault-template/README.md
skill/research-knowledge-base/assets/vault-template/01_Literature/文献索引.md
skill/research-knowledge-base/assets/vault-template/02_Projects/项目索引.md
skill/research-knowledge-base/assets/vault-template/03_Topics/主题索引.md
skill/research-knowledge-base/assets/vault-template/04_Methods_Concepts/方法概念索引.md
skill/research-knowledge-base/assets/vault-template/05_Synthesis/综合输出索引.md
skill/research-knowledge-base/assets/vault-template/90_Templates/文献笔记模板.md
skill/research-knowledge-base/assets/vault-template/90_Templates/综述文献笔记模板.md
skill/research-knowledge-base/assets/vault-template/90_Templates/Project模板.md
skill/research-knowledge-base/assets/vault-template/90_Templates/Topic_MOC模板.md
skill/research-knowledge-base/assets/vault-template/90_Templates/Method_Concept模板.md
skill/research-knowledge-base/assets/vault-template/90_Templates/Synthesis模板.md
skill/research-knowledge-base/assets/vault-template/90_Templates/Zotero实时追问模板.md
tests/test_init_knowledge_base.py
tests/test_skill_package.py
```

### Task 1: Scaffold the Skill and Write Script Tests

**Files:**
- Create: `skill/research-knowledge-base/`
- Create: `tests/test_init_knowledge_base.py`

- [ ] **Step 1: Initialize the Skill skeleton**

Run:

```bash
python3 /Users/liutianliang_1/.codex/skills/.system/skill-creator/scripts/init_skill.py \
  research-knowledge-base \
  --path skill \
  --resources scripts,references,assets \
  --interface display_name="Research Knowledge Base" \
  --interface short_description="构建并维护 Zotero、Obsidian 与 Codex 科研知识库" \
  --interface default_prompt="Use $research-knowledge-base to initialize and maintain my research literature knowledge base."
```

Expected: `skill/research-knowledge-base` and `agents/openai.yaml` are created.

- [ ] **Step 2: Write failing initialization tests**

Create `tests/test_init_knowledge_base.py` with tests that:

```python
def test_creates_named_knowledge_base_from_bundled_template():
    # Runs the CLI in a temporary directory.
    # Expects all six core directories and seven template files.

def test_refuses_existing_non_empty_target_without_merge():
    # Creates a target with an existing file.
    # Expects a non-zero return code and preserves that file.

def test_merge_copies_missing_files_without_overwriting_existing_files():
    # Creates a customized README in the target.
    # Runs --merge and verifies README is unchanged while missing files appear.

def test_rejects_blank_name():
    # Passes a whitespace-only name and expects a non-zero return code.
```

- [ ] **Step 3: Run tests to verify RED**

Run:

```bash
python3 -m unittest tests/test_init_knowledge_base.py -v
```

Expected: FAIL because `init_knowledge_base.py` and the completed vault assets do not exist.

- [ ] **Step 4: Commit the test scaffold**

```bash
git add skill/research-knowledge-base tests/test_init_knowledge_base.py
git commit -m "test: define knowledge base initialization behavior"
```

### Task 2: Implement and Verify the Initialization Script

**Files:**
- Create: `skill/research-knowledge-base/scripts/init_knowledge_base.py`

- [ ] **Step 1: Implement the CLI**

Implement:

```python
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--destination", required=True, type=Path)
    parser.add_argument("--name", required=True)
    parser.add_argument("--merge", action="store_true")
    return parser.parse_args()


def copy_template(template_root: Path, target: Path, merge: bool) -> tuple[list[Path], list[Path]]:
    # Refuse a non-empty target unless merge is true.
    # In merge mode, copy only paths that do not already exist.
    # Return created and skipped paths.


def main() -> int:
    # Validate the name, locate ../assets/vault-template,
    # create destination/name, print CREATED/SKIPPED entries,
    # and return 0 only on success.
```

- [ ] **Step 2: Run initialization tests**

Run:

```bash
python3 -m unittest tests/test_init_knowledge_base.py -v
```

Expected: Script tests progress to failures caused only by missing vault assets.

- [ ] **Step 3: Add a minimal temporary vault asset set**

Create the six core directories and all expected template file names under `assets/vault-template`, with valid minimal Markdown content.

- [ ] **Step 4: Run tests to verify GREEN**

Run:

```bash
python3 -m unittest tests/test_init_knowledge_base.py -v
```

Expected: all four tests pass.

- [ ] **Step 5: Commit**

```bash
git add skill/research-knowledge-base/scripts skill/research-knowledge-base/assets tests/test_init_knowledge_base.py
git commit -m "feat: add deterministic knowledge base initializer"
```

### Task 3: Build the Domain-Neutral Vault Assets

**Files:**
- Modify: `skill/research-knowledge-base/assets/vault-template/README.md`
- Modify: all index and template files listed in the File Map
- Create: `skill/research-knowledge-base/assets/vault-template/90_Templates/Zotero实时追问模板.md`

- [ ] **Step 1: Replace minimal assets with full templates**

Use domain-neutral fields such as:

```yaml
research_area: []
disease_or_model: []
topics: []
sample_type: []
related_projects: []
```

Do not include personal paths or fixed references to breast cancer, CTC, CSF, or personal projects.

- [ ] **Step 2: Add the Zotero real-time question template**

The template must represent repeated entries with:

```markdown
## Q001

- 日期：
- 原文位置：
- 原文摘录：
- 我的实时问题：
- AI 实时回答：
- 我自己的理解：
- 需要 Codex 核对：是
- Codex 核对结果：
- 相关项目：
- 相关主题：
- 后续是否追原始文献：
```

- [ ] **Step 3: Re-run initialization tests**

Run:

```bash
python3 -m unittest tests/test_init_knowledge_base.py -v
```

Expected: all tests pass with the complete asset set.

- [ ] **Step 4: Commit**

```bash
git add skill/research-knowledge-base/assets
git commit -m "feat: add reusable Obsidian research vault templates"
```

### Task 4: Write Skill References and Core Instructions

**Files:**
- Create: `skill/research-knowledge-base/references/architecture.md`
- Create: `skill/research-knowledge-base/references/literature-workflow.md`
- Create: `skill/research-knowledge-base/references/zotero-realtime-qa.md`
- Create: `skill/research-knowledge-base/references/maintenance.md`
- Replace: `skill/research-knowledge-base/SKILL.md`

- [ ] **Step 1: Write the four focused references**

Each reference has one responsibility:

- `architecture.md`: folder model, canonical literature notes, statuses, project reuse.
- `literature-workflow.md`: metadata/full-text retrieval, article-type routing, deep-reading standards, synthesis.
- `zotero-realtime-qa.md`: child-note schema, source verification, answer correction, privacy boundaries.
- `maintenance.md`: weekly audit, status transitions, evidence gaps, link checks.

- [ ] **Step 2: Write concise `SKILL.md`**

Use this trigger metadata:

```yaml
---
name: research-knowledge-base
description: Use when researchers want to initialize, structure, populate, or maintain an Obsidian literature knowledge base; deeply read original studies or reviews from Zotero, PDFs, DOI, PMID, or URLs; organize project evidence maps, topic MOCs, methods, and syntheses; or integrate real-time Zotero reading questions.
---
```

The body must:

- Inspect the current vault before editing.
- Route initialization, literature reading, new-project, real-time Q&A, and maintenance requests.
- Read only the relevant reference file.
- Prefer Zotero metadata/PDF when available.
- Treat AI answers in Zotero notes as unverified.
- Avoid duplicating canonical literature notes.
- Validate links, placeholders, metadata, and status before completion.

- [ ] **Step 3: Regenerate `agents/openai.yaml`**

Run:

```bash
python3 /Users/liutianliang_1/.codex/skills/.system/skill-creator/scripts/generate_openai_yaml.py \
  skill/research-knowledge-base \
  --interface display_name="Research Knowledge Base" \
  --interface short_description="构建并维护 Zotero、Obsidian 与 Codex 科研知识库" \
  --interface default_prompt="Use $research-knowledge-base to initialize and maintain my research literature knowledge base."
```

Expected: valid quoted YAML strings and a default prompt containing `$research-knowledge-base`.

- [ ] **Step 4: Commit**

```bash
git add skill/research-knowledge-base/SKILL.md skill/research-knowledge-base/references skill/research-knowledge-base/agents
git commit -m "feat: define research knowledge base workflow"
```

### Task 5: Add Package Validation Tests

**Files:**
- Create: `tests/test_skill_package.py`

- [ ] **Step 1: Write failing package tests**

Test:

```python
def test_required_skill_files_exist():
    # Checks SKILL.md, openai.yaml, script, four references, and seven templates.

def test_skill_contains_no_private_paths_or_domain_specific_projects():
    # Scans distributable files for /Users/, /Volumes/, and private project names.

def test_markdown_fences_are_balanced():
    # Ensures every Markdown file has balanced triple-backtick fences.

def test_frontmatter_is_present_in_note_templates():
    # Checks original, review, project, topic, method, and synthesis templates.

def test_skill_md_stays_under_500_lines():
    # Protects progressive disclosure.
```

- [ ] **Step 2: Run tests to verify RED or expose defects**

Run:

```bash
python3 -m unittest tests/test_skill_package.py -v
```

Expected: any package defects are reported before fixes.

- [ ] **Step 3: Fix only reported defects**

Update the relevant Skill, reference, or asset files without weakening tests.

- [ ] **Step 4: Run all tests**

Run:

```bash
python3 -m unittest discover -s tests -v
```

Expected: all tests pass.

- [ ] **Step 5: Run official Skill validation**

Run:

```bash
python3 /Users/liutianliang_1/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skill/research-knowledge-base
```

Expected: validation succeeds.

- [ ] **Step 6: Commit**

```bash
git add tests skill/research-knowledge-base
git commit -m "test: validate skill package integrity"
```

### Task 6: Add Bilingual Repository Documentation

**Files:**
- Create: `README.md`
- Create: `LICENSE`
- Create: `examples/initialization-profile.example.md`

- [ ] **Step 1: Add MIT License**

Use the standard MIT license text with:

```text
Copyright (c) 2026 Tianliang Liu
```

- [ ] **Step 2: Write bilingual README**

Include:

- Chinese introduction and quick start
- English overview
- Installation from the GitHub repository
- Example prompts
- Vault architecture
- Zotero/Obsidian/Codex responsibilities
- Real-time Zotero question workflow
- No-API and privacy clarification
- Limitations

- [ ] **Step 3: Add an initialization profile example**

Provide a fictional, non-breast-cancer example containing:

- Knowledge-base name
- Research area
- Core questions
- Projects
- Keywords
- Zotero collections

- [ ] **Step 4: Commit**

```bash
git add README.md LICENSE examples
git commit -m "docs: add bilingual usage and installation guide"
```

### Task 7: Final Verification and GitHub Publication

**Files:**
- Review all repository files

- [ ] **Step 1: Run the complete verification suite**

Run:

```bash
python3 -m unittest discover -s tests -v
python3 /Users/liutianliang_1/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill/research-knowledge-base
python3 skill/research-knowledge-base/scripts/init_knowledge_base.py \
  --destination /tmp/research-kb-release-check \
  --name "Demo Research Knowledge Base"
git diff --check
git status --short
```

Expected:

- All tests pass.
- Official Skill validation succeeds.
- Demo vault is created with all expected folders and templates.
- No whitespace errors.
- Only intentional files are staged or untracked.

- [ ] **Step 2: Scan for private information**

Run:

```bash
rg -n '/Users/|/Volumes/|乳腺癌脑转移|CTC 多组学|tianliang_liu@qq.com' \
  README.md LICENSE examples skill tests
```

Expected: no private path or personal-project matches. The license holder name is allowed.

- [ ] **Step 3: Commit release-ready state**

```bash
git add README.md LICENSE examples skill tests docs
git commit -m "chore: prepare initial public release"
```

- [ ] **Step 4: Create the public GitHub repository**

Create:

```text
tianliang-liu/research-knowledge-base-skill
```

Settings:

- Visibility: Public
- Initialize with files: No
- License selection in UI: None, because `LICENSE` is already committed

- [ ] **Step 5: Push `main`**

Add the remote and push:

```bash
git remote add origin https://github.com/tianliang-liu/research-knowledge-base-skill.git
git push -u origin main
```

- [ ] **Step 6: Verify the remote repository**

Verify:

- Repository is public.
- Default branch is `main`.
- README renders.
- `LICENSE` is recognized as MIT.
- `skill/research-knowledge-base/SKILL.md` is accessible.
- Clone URL works.
