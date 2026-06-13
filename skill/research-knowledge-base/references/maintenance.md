# Knowledge-Base Maintenance

## Recommended Frequency

- Weekly when reading several papers
- Every two weeks during slower periods
- Before launching a new project
- Before writing a presentation, proposal, or manuscript section

## Audit Order

### 1. Literature Status

Find notes with:

```yaml
status: reading
```

Check whether they are genuinely in progress or abandoned.

Find notes with:

```yaml
status: summarized
```

Check whether a higher-level integration is still missing.

### 2. Metadata and Source Access

Check:

- Title, authors, year, and journal
- DOI, PMID, PMCID
- Zotero item and attachment keys
- PDF or source link
- Declared full-text versus abstract-only scope

Do not fill missing identifiers by guessing.

### 3. Unresolved Questions

Search for:

- `需要 Codex 核对：是`
- Unchecked verification tasks
- Empty evidence-strength fields
- Follow-up papers not yet read
- Claims marked as uncertain

Prioritize questions that affect experimental design, analysis, or interpretation.

### 4. Higher-Level Integration

For each summarized paper, ask:

- Does it change a project evidence map?
- Does it add or challenge a topic-level conclusion?
- Does it provide a reusable method, dataset, marker, or concept?
- Does it contribute to a multi-paper synthesis?

Update only pages where the paper adds real value.

### 5. Project Evidence Gaps

For each active project, update:

| Project question | Existing evidence | Strength | Gap | Next action |
|---|---|---|---|---|
|  |  |  |  |  |

Identify:

- Missing comparator or control evidence
- Missing validation cohort
- Conflicting findings
- Sample or platform mismatch
- Unresolved mechanism
- Missing clinical relevance

### 6. Link Integrity

Check:

- Literature links in projects
- Topic and method links in literature notes
- Links to renamed files
- Placeholder wikilinks
- Duplicate notes for the same paper

Prefer repairing links over creating duplicate target pages.

## Status Transitions

Use:

```text
unread → reading
reading → summarized
summarized → synthesized
any state → archived
```

Only mark `summarized` when the canonical note is complete enough for later reuse.

Only mark `synthesized` after updating at least one project, topic, method, or synthesis page with verified content.

## Maintenance Report

At the end, report:

- Files updated
- Papers moved between statuses
- Questions resolved
- Project evidence gaps found
- Broken or placeholder links remaining
- One to three highest-priority papers for the next reading cycle

Do not silently restructure the vault during routine maintenance. Propose structural changes separately when needed.
