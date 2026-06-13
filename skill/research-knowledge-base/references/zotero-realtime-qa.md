# Zotero Real-Time Question Workflow

## Goal

Preserve questions that arise while reading a PDF, provide immediate provisional help, and later convert only source-verified answers into the formal knowledge base.

## Recommended Zotero Note

Create one child note under each paper:

```text
阅读追问_QA
```

Keep all questions for that paper in the same child note instead of creating many fragmented notes.

Use:

```markdown
## Q001

- 日期：
- 原文位置：Page / Section / Figure / Table
- 原文摘录：
- 我的实时问题：
- AI 实时回答：
- 我自己的理解：
- 需要 Codex 核对：是
- Codex 核对结果：
- 回答依据：
- 是否修正了临时 AI 回答：
- 相关项目：
- 相关主题：
- 后续是否追原始文献：
```

The bundled `90_Templates/Zotero实时追问模板.md` can be copied into Zotero Notes.

## Input Routes

Real-time answers may come from:

- PapersGPT or another Zotero plugin
- A local model
- An MCP-enabled client
- ChatGPT, Codex, or another assistant
- The researcher's own provisional interpretation

These routes are optional. The knowledge-base workflow must not require a specific model provider or API key.

## Verification Rule

Treat all provisional AI answers as unverified annotations.

The paper is the evidence source. The AI answer is only a reading aid.

For each question:

1. Preserve the exact user question.
2. Locate the cited source position.
3. Read enough surrounding text to understand context.
4. Check figures, legends, methods, supplementary material, and cited primary work when needed.
5. Classify the provisional answer:
   - Supported
   - Partially supported
   - Overstated
   - Incorrect
   - Not answerable from this paper
6. Write a corrected explanation.
7. State the evidence basis and remaining uncertainty.

## Common Failure Modes

### Causality Inflation

The plugin may turn correlation into mechanism. Correct the answer unless perturbation, temporal evidence, or suitable functional validation supports causality.

### Evidence-Level Mixing

A review may discuss cell-line, animal, observational, and trial evidence together. Label the evidence source explicitly.

### Missing Scope

An answer may be correct only for one model, subtype, stage, sample type, or treatment setting. Restore those boundaries.

### Citation Drift

The answer may be supported by a paper cited in the review rather than by the review itself. Add the primary paper to the follow-up list.

### Method Hallucination

Do not infer software, thresholds, sample processing, or platform parameters that are not reported.

## Integration into Obsidian

Do not paste the entire chat transcript into the canonical note.

Place verified content where it belongs:

- Concept clarification → relevant background or method subsection
- Figure interpretation → corresponding result module
- Evidence-strength question → result assessment or discussion
- Project implication → `对我研究的启发` and the relevant project page
- Cross-paper question → topic or synthesis page
- Unresolved issue → verification checklist or follow-up literature list

Optionally retain a concise question record:

```markdown
### 阅读追问

- 问题：
- 核对后回答：
- 依据：
- 剩余不确定性：
```

## Privacy

Before using a remote AI model, consider whether the PDF, annotations, project hypothesis, or clinical information may be confidential.

- Prefer public papers or approved data for remote services.
- Do not send patient identifiers or unpublished sensitive results.
- Local models reduce external transmission but do not remove the need for source verification.
- MCP provides access plumbing; it does not guarantee model privacy or answer accuracy.
