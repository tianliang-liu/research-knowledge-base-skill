# Literature Reading Workflow

## Source Acquisition

Accept any of:

- Zotero title or item key
- Zotero PDF attachment
- Local PDF
- DOI
- PMID or PMCID
- Publisher, PubMed, or repository URL

Prefer this source order:

1. Zotero metadata and attached PDF
2. Publisher or repository full text
3. PubMed/PMC metadata and full text
4. Abstract-only record

State clearly when the full text is unavailable. Do not label an abstract-only analysis as a complete deep reading.

## Common Metadata

Capture when available:

```yaml
type: literature
article_type:
status:
title:
authors:
year:
journal:
doi:
pmid:
pmcid:
url:
zotero_key:
zotero_attachment_key:
zotero_collection:
citation_key:
research_area: []
disease_or_model: []
topics: []
data_type: []
methods: []
sample_type: []
related_projects: []
```

Never guess missing identifiers.

## Article-Type Routing

Use the original-research template when the paper reports a newly conducted experiment, cohort, trial, model, dataset analysis, or method evaluation.

Use the review template when the paper primarily organizes existing literature, including:

- Narrative review
- Systematic review
- Meta-analysis
- Perspective
- Primer
- Clinical review

For guidelines, protocols, methods reviews, or dataset descriptors, adapt the closest template and explicitly name the article type.

## Original Research Standard

### 1. Research Background

Record:

- Established knowledge
- Precise unresolved problem
- Author's research question
- Hypothesis
- Why the problem matters to the researcher's projects

Keep this section focused. Do not turn it into a general review.

### 2. Methods

This is a priority section. Record enough detail to evaluate or reuse the work:

- Cohort source and recruitment
- Sample size and exclusions
- Disease, phenotype, stage, or model
- Sample type and collection time
- Controls and grouping
- Experimental design
- Platforms and assays
- Sample processing
- Quality control
- Data preprocessing
- Statistical tests and multiple-testing correction
- Bioinformatics software, databases, and important parameters
- External validation
- Functional validation
- Sensitivity analyses
- Method strengths, limitations, and reproducibility gaps

Separate reported methods from inferred methods. If an important parameter is absent, say so.

### 3. Research Content

Prefer figure- or result-level decomposition:

```text
Question
→ Method used for this result
→ Key observation
→ Author interpretation
→ Evidence-quality assessment
→ Researcher-specific relevance
```

For each major figure or result:

- Explain what question it addresses.
- Connect the method to the result.
- Include direction and context, not only significance.
- Distinguish association from causality.
- Note whether validation supports the claim.
- Mention important supplementary findings.

### 4. Discussion

Record:

- Main contribution
- Genuine innovation
- Relationship to prior work
- Limitations acknowledged by authors
- Additional limitations identified during reading
- Generalizability
- Clinical or mechanistic significance
- Reusable methods, datasets, markers, or figure designs
- Implications for current projects
- Follow-up papers and unresolved questions

## Review Standard

Do not force a review into a methods/results structure.

### 1. Review Position

Determine:

- Review type
- Scope and time range
- Systematic search or inclusion criteria
- Meta-analysis status
- Author perspective and possible bias
- Whether it is suitable as a field-entry paper

### 2. Field Framework

Reconstruct how the authors divide the field. Capture modules, transitions, and the main explanatory line.

### 3. Evidence Map

Separate:

- Basic experiments
- Cell lines, organoids, or patient-derived models
- Animal models
- Single-cell, spatial, or multi-omics cohorts
- Retrospective clinical cohorts
- Prospective cohorts
- Randomized trials
- Systematic reviews and meta-analyses
- Guidelines and consensus

State which conclusions are strong, which are preliminary, and which require checking the cited primary paper.

### 4. Thematic Reading

For every major theme:

- Question addressed
- Author's core claim
- Supporting evidence type
- Key primary references
- Important mechanisms, markers, drugs, datasets, or methods
- Controversy or uncertainty
- Relevance to current research

### 5. Structured Extraction

Create tables when relevant for:

- Mechanistic axes
- Cell types or states
- Methods
- Datasets, cohorts, or trials
- Drugs, targets, or interventions
- Markers or feature sets

### 6. Trends and Follow-Up

Capture:

- Direction of the field
- Major unresolved disputes
- Issues underemphasized by the authors
- Implications for sampling, platform choice, analysis, interpretation, and validation
- Primary papers that deserve full reading

## Evidence Language

Use language proportional to evidence:

- `shows` only for directly supported results
- `is associated with` for observational associations
- `supports` when evidence is convergent but incomplete
- `suggests` for preliminary findings
- `hypothesizes` for proposed mechanisms without direct validation

Do not convert a review author's statement into primary evidence.

## Higher-Level Integration

After the canonical note is complete, perform at least one justified action:

- Add project-specific evidence to `02_Projects`.
- Add a cross-paper conclusion to `03_Topics`.
- Add a reusable procedure or concept to `04_Methods_Concepts`.
- Add a multi-paper inference to `05_Synthesis`.

Do not create empty higher-level pages merely to satisfy this step.

## Final Checks

- Metadata traceability is present.
- Article type and template match.
- Full text versus abstract-only scope is declared.
- Methods and findings are sufficiently detailed for the article type.
- Evidence strength is not overstated.
- User questions are answered or marked unresolved.
- New wikilinks point to existing or intentionally created pages.
