# ResearchThon AI Infrastructure Master Kit

## Purpose

This kit organises the project into a single evidence-first workflow for a conceptual research paper proposing a five-pillar framework for India's AI infrastructure planning, supported by a quantitative GPU demand-cascade model.

This is not a generic essay-writing workflow. Antigravity should inspect the research materials, verify claims, build traceable datasets, implement and test the model, create comparison tables and figures, and only then generate LaTeX.

## Working research title

**A Demand-Driven Framework for India's AI Infrastructure Planning: Linking Compute, Energy, Physical Resources, and Semiconductor Dependencies**

The title is provisional. Revise only if the verified research gap or results justify it.

## Core research question

How can India assess and prioritise the infrastructure dependencies that shape its long-term AI capability, and what requirements emerge when different levels of AI compute demand are propagated through the underlying infrastructure and semiconductor supply chain?

## Research design: two connected components

1. **Five-pillar planning framework** — the conceptual contribution expected by the faculty coordinator.
2. **Demand-cascade model** — a quantitative demonstration that starts with hypothetical GPU scenarios and estimates requirements across infrastructure layers.

The five pillars structure the paper. The demand cascade provides the technical demonstration. Do not treat them as competing approaches.

## Five pillars

1. Compute and semiconductor sovereignty.
2. Energy and grid readiness.
3. Data centres and physical resources.
4. Connectivity, data and secure computing.
5. Governance, investment and indigenous capability.

## GPU scenarios

Use 200,000, 500,000, and 1,000,000 GPUs as illustrative scenarios only, unless a reliable source establishes a specific scenario as an official target. Do not call them government targets.

## Essential research rules

- Facts, assumptions, calculations, projections and recommendations must be labelled separately.
- Every quantitative claim must be traceable to a source or a reproducible calculation.
- GPU access is not equivalent to GPU ownership or sovereign control.
- Installed generation capacity is not the same as firm electricity available at a particular data-centre site.
- Announced data-centre capacity is not operational capacity.
- Semiconductor design, fabrication, packaging, memory and manufacturing equipment are different capabilities.
- Never manufacture missing values to complete a table or chart.
- If data are unavailable or definitions are incompatible, mark them as missing/non-comparable and explain why.
- Do not claim a research gap before a documented literature search.
- Do not state that a paper is plagiarism-free based on AI review. Use an actual institutional similarity-checking tool if available, interpret its report responsibly, and manually review all matched passages.
- AI-generated content and analysis must be checked by the authors and disclosed according to event rules.
- Do not claim acceptance or guaranteed publication.

## How to use the kit

1. Extract this ZIP.
2. Open the extracted folder as the Antigravity workspace.
3. Put downloaded reports, academic papers, datasets, official documents, and the event template into `sources/`. Keep originals unchanged.
4. Start with `prompts/00_SCOPE_AND_WORKSPACE_AUDIT.md`.
5. Run one prompt at a time in numerical order. Review its deliverables before proceeding.
6. Antigravity must use local files first, then search/download additional public sources only where evidence gaps remain.
7. Keep a log of downloaded sources, source URLs, download dates, source versions, and failed retrievals.
8. Generate the paper in LaTeX only after the evidence, framework, calculations, and figures have been reviewed.

## Suggested project folders

Antigravity should create these inside the active project workspace:
- `sources/raw/` — unmodified downloaded originals
- `sources/metadata/` — source inventory and bibliographic metadata
- `data/raw/` — downloaded raw datasets, unmodified
- `data/processed/` — cleaned datasets with scripts and provenance
- `research/` — literature review, claims, research gap, methodology
- `model/` — parameters, equations, code, tests
- `figures/` — reproducible figures
- `tables/` — reproducible paper tables
- `manuscript/` — LaTeX source, BibTeX, section files
- `output/` — compiled review PDF and final exports
- `logs/` — run logs, source retrieval log, corrections
- `presentation/` — slides, notes, jury questions

## Recommended division of labour

- **Antigravity:** workspace inspection, research retrieval where possible, data extraction, code, reproducible figures/tables, LaTeX source, automated checks.
- **You and teammates:** judge source credibility, approve assumptions, verify findings, confirm claims, own the research decisions.
- **Claude:** critical review and similarity-report interpretation; not a substitute for a real plagiarism database or citation verification.
- **ChatGPT:** research design, source verification, methodology critique, equation review, manuscript critique, and presentation defence.
- **LaTeX/Overleaf or local TeX:** compile and refine the manuscript after scientific content is stable.

## Stop rule

At each prompt, Antigravity should report: files created/changed, checks performed, unresolved issues, and the next action. It must stop at review gates rather than autonomously invent missing evidence or continue into a later stage.
