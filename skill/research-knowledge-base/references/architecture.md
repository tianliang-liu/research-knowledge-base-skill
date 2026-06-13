# Knowledge-Base Architecture

## Purpose

Use this architecture for long-term research knowledge, not for laboratory administration, meeting notes, daily experiment logs, or temporary task management.

## Folder Model

```text
Research Knowledge Base
├── 01_Literature
├── 02_Projects
├── 03_Topics
├── 04_Methods_Concepts
├── 05_Synthesis
└── 90_Templates
```

### `01_Literature`

Store one canonical detailed note per deeply read paper.

Include:

- Original studies
- Important reviews
- Methods and dataset papers
- Clinical trials
- Guidelines or consensus documents worth repeated use

Do not create separate `Unread`, `Reading`, or `Done` folders. Use frontmatter status.

### `02_Projects`

Organize evidence around a concrete research problem.

A project page should answer:

- What problem does the project address?
- What hypotheses are currently plausible?
- Which existing papers support or challenge the project?
- How strong is each evidence line?
- Which evidence, experiment, dataset, or method is still missing?

Do not copy full literature summaries into a project page. Link the canonical literature note and add only the project-specific interpretation.

### `03_Topics`

Store topic pages and Maps of Content (MOCs) that span papers and projects.

Examples:

- Disease or biological-system overview
- Mechanism
- Cell type or state
- Treatment class
- Sample type
- Technical platform
- Clinical question

### `04_Methods_Concepts`

Store reusable methodological and conceptual knowledge:

- Experimental protocols
- Analysis workflows
- Statistical approaches
- Public datasets and cohorts
- Markers and feature sets
- Mechanistic axes and pathways
- Model systems
- Quality-control rules

### `05_Synthesis`

Store conclusions that require more than one paper:

- Evidence chains
- Research hypotheses
- Contradictions and controversies
- Study-design decisions
- Figure and table concepts
- Presentation or manuscript arguments

Do not use this folder for single-paper summaries.

### `90_Templates`

Keep the templates for:

- Original research
- Reviews
- Projects
- Topics/MOCs
- Methods/concepts
- Syntheses
- Zotero real-time questions

## Canonical-Note Rule

Each paper has one detailed note in `01_Literature`.

The same paper may support multiple projects and topics. Reuse it through wikilinks:

```markdown
- [[2026 - Author - Short title]]: supports the sampling strategy but does not validate clinical utility.
```

This prevents contradictory duplicate summaries and makes corrections propagate through the knowledge base.

## Status Model

```text
unread       Collected but not read
reading      Full reading is in progress
summarized   Canonical literature note is complete
synthesized  At least one higher-level integration is complete
archived     Retained but not currently useful
```

Do not use `synthesized` merely because a literature note is long. It requires a real update to a project, topic, method, or synthesis page.

## Starting a New Project

1. Create the project position and core questions.
2. Search existing literature notes by disease, mechanism, method, sample, and outcome.
3. Classify reusable papers:
   - Core evidence
   - Background
   - Methods
   - Peripheral relevance
4. Write one project-specific relevance statement per paper.
5. Create an evidence map:

| Project question | Existing evidence | Strength | Gap | Next action |
|---|---|---|---|---|
|  |  |  |  |  |

6. Re-open full papers only when the project depends on methodological detail, exact evidence, or a disputed interpretation.

## Initialization Profile

Before customization, identify:

- Knowledge-base name
- Main research area
- Three to five long-term questions
- Current projects
- Diseases, organisms, or model systems
- Sample types
- Technical platforms
- Mechanisms, pathways, or cell types
- Zotero collections
- Topics that should become initial MOCs

Avoid pre-populating many empty pages. Create only pages that reflect current research activity.
