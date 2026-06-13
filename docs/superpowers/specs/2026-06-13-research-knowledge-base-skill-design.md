# Research Knowledge Base Skill Design

## 1. Objective

Create and publicly release a reusable Codex Skill that helps researchers build and maintain an Obsidian + Zotero + Codex knowledge base.

The Skill will preserve the proven workflow from the existing personal knowledge base while removing personal paths, breast-cancer-specific projects, and private literature content. It will be designed primarily for Chinese-speaking researchers, with English Skill metadata and a concise bilingual GitHub presentation.

Repository:

```text
research-knowledge-base-skill
```

Distribution:

- Public GitHub repository
- MIT License
- Installable Codex Skill
- Reusable Obsidian vault template
- Deterministic initialization script

## 2. Supported Workflows

The Skill will support five related workflows.

### 2.1 Initialize a Research Knowledge Base

Create a domain-neutral knowledge base with:

```text
01_Literature
02_Projects
03_Topics
04_Methods_Concepts
05_Synthesis
90_Templates
```

The initialization process will accept a destination and knowledge-base name, copy the bundled vault template, and avoid overwriting existing files unless explicitly requested.

### 2.2 Deep-Read Literature

Process literature supplied through:

- Zotero title or item key
- Local PDF
- DOI or PMID
- Article URL

The Skill will distinguish:

- Original research
- Review, perspective, primer, and clinical review

Original research notes emphasize methods and figure/result-level findings. Review notes emphasize field structure, evidence mapping, major themes, controversies, and follow-up primary literature.

### 2.3 Organize Higher-Level Knowledge

After a literature note is complete, the Skill will identify valuable material for:

- Project evidence maps
- Topic/MOC pages
- Method and concept pages
- Multi-paper synthesis pages

One paper will have only one canonical detailed note in `01_Literature`. Project pages will link and reinterpret existing notes instead of duplicating them.

### 2.4 Integrate Real-Time Zotero Questions

The Skill will support a Zotero child note named:

```text
阅读追问_QA
```

The note may contain:

- User question
- Source page, section, figure, or table
- Selected source text
- Real-time AI answer
- User interpretation
- Verification status

When later creating the formal Obsidian literature note, Codex will treat the real-time AI answer as unverified, check it against the paper, correct or expand it, and integrate only supported conclusions.

### 2.5 Maintain the Knowledge Base

The Skill will:

- Find literature notes still marked `reading` or `summarized`
- Identify notes not linked to higher-level pages
- Update project evidence gaps
- Recommend the next high-priority papers
- Change a note to `synthesized` only after a real higher-level integration action

## 3. Repository Architecture

```text
research-knowledge-base-skill/
├── README.md
├── LICENSE
├── skill/
│   └── research-knowledge-base/
│       ├── SKILL.md
│       ├── agents/
│       │   └── openai.yaml
│       ├── scripts/
│       │   └── init_knowledge_base.py
│       ├── references/
│       │   ├── architecture.md
│       │   ├── literature-workflow.md
│       │   ├── zotero-realtime-qa.md
│       │   └── maintenance.md
│       └── assets/
│           └── vault-template/
│               ├── README.md
│               ├── 01_Literature/
│               ├── 02_Projects/
│               ├── 03_Topics/
│               ├── 04_Methods_Concepts/
│               ├── 05_Synthesis/
│               └── 90_Templates/
└── examples/
    └── initialization-profile.example.md
```

## 4. Component Responsibilities

### 4.1 `SKILL.md`

Contains only the essential execution workflow:

- Trigger conditions
- Initial environment inspection
- Workflow selection
- Rules for article-type selection
- Requirements for Zotero question-note verification
- Knowledge-synthesis rules
- Validation requirements
- Pointers to the appropriate reference files

It will remain concise and under 500 lines.

### 4.2 Reference Files

`architecture.md`:

- Folder responsibilities
- Status model
- Canonical-note rule
- Project reuse model

`literature-workflow.md`:

- Original research workflow
- Review workflow
- Metadata expectations
- Evidence-strength handling
- Higher-level integration

`zotero-realtime-qa.md`:

- Recommended child-note schema
- How to distinguish user questions from AI answers
- Verification and correction workflow
- Privacy and external-model considerations

`maintenance.md`:

- Weekly review
- Status transitions
- Evidence-gap updates
- Link and placeholder checks

### 4.3 Initialization Script

`init_knowledge_base.py` will:

- Use only the Python standard library
- Accept `--destination` and `--name`
- Locate the bundled vault template relative to the script
- Copy the template into the requested destination
- Refuse to overwrite an existing non-empty target by default
- Support an explicit `--merge` mode that copies only missing files
- Print all created and skipped paths
- Return a non-zero exit code for invalid arguments or unsafe conflicts

It will not:

- Modify Obsidian global configuration automatically
- Install Zotero or Obsidian plugins
- Upload files or contact model APIs
- Depend on a specific disease, project, or local filesystem path

### 4.4 Vault Assets

The bundled vault template will include:

- Domain-neutral index pages
- Original-research literature template
- Review literature template
- Project template
- Topic/MOC template
- Method/concept template
- Synthesis template
- Zotero real-time Q&A child-note template

All fixed references to breast cancer, CTC, CSF, or personal projects will be removed.

### 4.5 GitHub Documentation

The root `README.md` will include:

- Chinese introduction and quick start
- Short English overview
- What the Skill does
- Installation options
- Example trigger prompts
- Expected knowledge-base structure
- Zotero/Obsidian/Codex responsibility split
- Real-time Q&A integration
- Limitations and privacy notes
- MIT license statement

The README is repository documentation, not part of the installed Skill context.

## 5. Data Flow

### 5.1 Knowledge-Base Initialization

```text
Research profile
→ Skill inspects destination
→ Initialization script copies vault assets
→ Codex customizes project/topic/method starting pages
→ User configures Obsidian template folder
```

### 5.2 Literature Processing

```text
Zotero item/PDF/DOI/URL
→ Retrieve metadata and full text
→ Detect article type
→ Read optional 阅读追问_QA child note
→ Verify real-time answers against source
→ Generate canonical literature note
→ Update project/topic/method/synthesis pages
→ Validate links and status
```

### 5.3 New Project

```text
New research question
→ Search existing 01_Literature notes
→ Classify reusable evidence
→ Create project evidence map
→ Identify gaps
→ Read only papers that materially affect the new project
```

## 6. Error Handling and Safety

- Never overwrite an existing knowledge base without explicit authorization.
- Never treat AI-generated Zotero answers as source evidence.
- Never fabricate metadata, figures, page locations, or paper findings.
- Mark inaccessible full text and unresolved claims explicitly.
- Preserve unrelated user files and custom Obsidian structures.
- Avoid embedding local absolute paths, credentials, API keys, or private library data.
- Do not require a paid model API for the Skill itself.
- Treat optional Zotero and MCP integrations as capabilities, not mandatory dependencies.

## 7. Validation

Validation will include:

1. Official Skill structure validation with `quick_validate.py`.
2. `agents/openai.yaml` generation and consistency check.
3. Initialization-script tests in temporary directories:
   - Fresh creation
   - Existing target refusal
   - Merge without overwrite
   - Invalid destination handling
4. Scan for private paths and breast-cancer-specific content.
5. Markdown fence and YAML frontmatter checks.
6. Verify required vault folders and templates.
7. Install the Skill into a temporary Codex skills directory and inspect the result.
8. Review the final Git diff before commit and publication.

## 8. GitHub Publication

Publication steps:

1. Initialize the repository on branch `main`.
2. Add the completed Skill, documentation, license, and examples.
3. Commit with a clear initial-release message.
4. Create public GitHub repository `research-knowledge-base-skill`.
5. Push `main`.
6. Verify the remote repository URL and visible files.

No release archive or package registry publication is required for version 1.0. The GitHub repository itself is the distribution source.

## 9. Acceptance Criteria

The task is complete when:

- The repository has a valid installable Skill.
- A researcher can initialize a fresh vault using the bundled script.
- The Skill handles original research and review articles differently.
- Zotero real-time Q&A notes have a defined verification and integration workflow.
- Project pages reuse existing literature notes instead of duplicating them.
- All assets are domain-neutral and contain no private paths.
- Validation passes.
- The repository is public on GitHub under the MIT License.
