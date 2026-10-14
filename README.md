# Sovereign by Design: An Integrated Five-Pillar Framework for India's Strategic Compute and AI Infrastructure

[![ResearchThon 2026](https://img.shields.io/badge/Event-ResearchThon%202026-blue.svg)](https://amity.edu)
[![Branch: adarshv2](https://img.shields.io/badge/Branch-adarshv2-orange.svg)](https://github.com/A2105s/Research-o-Thon/tree/adarshv2)
[![Format: IEEE Conference](https://img.shields.io/badge/Format-IEEE%20Conference-success.svg)](manuscript/main.tex)
[![License: MIT](https://img.shields.io/badge/Code%20License-MIT-yellow.svg)](LICENSE_AND_ATTRIBUTION.md)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](model/requirements.txt)
[![Tests: Passing](https://img.shields.io/badge/Tests-10%2F10%20Passing-brightgreen.svg)](model/tests/)

**Institution:** Department of Computer Science and Engineering, Amity School of Engineering and Technology, Amity University Madhya Pradesh, Gwalior, India

**Authors (in order):**

| # | Name | Role | Email |
|:-:|------|------|-------|
| 1 | **Dr. Madhavi Dhingra** | Faculty Coordinator, Associate Professor | madhavi.dhingra@gmail.com |
| 2 | **Adarsh Singh** | Student Author | officialadarsh.in@gmail.com |
| 3 | **Parikshit Singh Bais** | Student Author | sillypari@gmail.com |
| 4 | **Anamidi Shrivastava** | Student Author | anamidishrivastava@gmail.com |
| 5 | **Sourav** | Student Author | Souravsingh1024@gmail.com |

**Track:** AI Infrastructure, Semiconductor Sovereignty & Strategic Computing

---

## 1. Executive Summary

National artificial intelligence (AI) strategies increasingly treat high-performance compute accelerators as primary instruments of technological sovereignty. However, compute scaling is physically bounded by electricity transmission, cooling water, semiconductor lithography, advanced packaging (CoWoS), high-bandwidth memory (HBM), and geopolitically concentrated supply chains.

This repository provides the complete, reproducible research codebase, evidence register, simulation models, figures, and LaTeX manuscript for our **Five-Pillar Conceptual Framework** and six-layer **Demand-Cascade Model (DCM)**. Evaluating three deployment scenarios (**200,000, 500,000, and 1,000,000 GPUs**), the model translates national accelerator targets into concrete infrastructure requirements:

- **IT Electrical Load & Substation Capacity:** 637.0 MW IT load and 891.8 MW peak facility draw (500k GPUs @ PUE 1.40).
- **National Grid Absorption:** Absorbs **56.62% of India's current operational colocation data centre capacity** (1,575 MW in mid-2026).
- **Structural Chokepoint Inversion:** Refutes the belief that front-end wafer fabrication is India's binding constraint — required sub-5 nm wafer starts represent merely **1.60%** of TSMC's annual output (12,500 wafers), whereas 2.5D CoWoS advanced packaging consumes **7.41%** of global capacity (**4.6×** higher intensity) and HBM3e absorbs **6.67%** of global production.
- **Cooling-Water Mitigation:** Direct-to-chip liquid cooling cuts evaporative water withdrawal by **94.6%** (11,250 ML → 631 ML/yr) and reduces facility power by 172 MW in tropical climates.
- **Grid Stability Risk:** Mumbai's 52.4% capacity concentration and 20–40% dynamic AI load swings threaten transmission stability.

The paper closes with a sequenced **three-tier strategic roadmap** prioritising transmission corridors, packaging partnerships, and regional dispersion over premature leading-edge foundries.

---

## 2. Repository Architecture

```text
Research-o-Thon-Mixture/
├── README.md                      # This file — project overview & reproduction guide
├── LICENSE_AND_ATTRIBUTION.md     # MIT (code) & CC BY 4.0 (manuscript) licensing
├── IDEAAA.md                      # Ideation and concept notes
├── final_paper.md                 # Full-length (15-page aligned) Markdown draft
├── template (2).pdf               # Official IEEE event template (PDF)
├── .gitignore                     # Repository hygiene exclusions
├── docs/
│   ├── event_guidelines/          # Official ResearchThon rules, rubrics, paper template
│   ├── project_brief/             # Master project brief and workflow roadmap
│   ├── audit_reports/             # Technical red-team verification reports
│   └── previous_versions/         # Preserved prior drafts
├── sources/
│   ├── source_manifest.csv        # SHA-256 audited manifest of all scanned files
│   ├── duplicate_report.csv       # Exact hash duplicate registry
│   ├── research_papers/           # Curated primary research PDFs
│   └── official_reports/          # Government & industry sources (MeitY, CEA, JLL, CBRE)
├── research/
│   ├── research_gap.md            # Literature deficit assessment
│   ├── literature_matrix.csv      # Cross-study comparative synthesis
│   ├── evidence_register.csv      # Empirical facts traced to primary sources
│   ├── parameter_register.csv     # Engineering parameters with low/base/high bounds
│   └── claim_register.md          # Audited verification of all numerical claims
├── data/
│   └── scenario_outputs/          # Deterministic CSV outputs (200k, 500k, 1M GPUs)
├── model/
│   ├── demand_cascade.py          # Primary Python simulation engine (v2.0)
│   ├── parameter_register.csv     # Authoritative parameter dictionary
│   ├── requirements.txt           # Python dependencies
│   └── tests/
│       └── test_demand_cascade.py # Automated unit test suite (10/10 passing)
├── figures/                       # Architecture, comparison, and sensitivity figures
├── figures_review/                # Figure QA / review exports
├── tables/                        # Machine-readable CSV tables matching manuscript
├── Data_Tables/                   # Authoritative source tables (Sheets PDF exports)
├── manuscript/
│   ├── main.tex                   # IEEEtran conference LaTeX source
│   ├── IEEEtran.cls               # IEEE conference class file
│   ├── references.bib             # Verified BibTeX citations (2024–2026)
│   ├── main.pdf                   # Compiled manuscript PDF
│   └── figures/                   # Vector PDFs and PNGs embedded in paper
├── presentation/                  # Speaker notes and jury Q&A
├── sample_images/                 # Sample reference imagery
├── output/                        # Template crops, test renders, final PDF exports
├── model/                         # Simulation engine (see above)
└── scripts/
    ├── compile_paper.py           # Automated PDF compiler (ReportLab fallback)
    └── generate_figures.py        # Matplotlib vector figure generator
```

---

## 3. Quick Start & Reproduction

### Prerequisites
- **Python 3.10+**
- Optional: TeX distribution (TeX Live / MiKTeX / Tectonic) for native LaTeX compilation of `manuscript/main.tex`
- Optional: `uv` (if you use the `latex-paper-en` skill's compile workflow)

### Step 1 — Install Dependencies

```bash
pip install -r model/requirements.txt
```

### Step 2 — Run Unit Tests

```bash
python model/tests/test_demand_cascade.py
```

Expected: **10/10 tests passing**.

### Step 3 — Run Model Simulation

```bash
python model/demand_cascade.py
```

Deterministic CSV outputs are written to `data/scenario_outputs/` and `tables/`.

### Step 4 — Regenerate Figures

```bash
python scripts/generate_figures.py
```

Vector PDFs and high-DPI PNGs are generated in `figures/` and copied into `manuscript/figures/`.

### Step 5 — Compile the Manuscript (LaTeX)

With a TeX distribution installed:

```bash
cd manuscript
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Or via the Python compiler (ReportLab fallback):

```bash
python scripts/compile_paper.py
```

---

## 4. Key Findings (Scenario Matrix)

| Metric Layer | 200,000 GPUs | 500,000 GPUs (Baseline) | 1,000,000 GPUs | Constraint Source |
|:---|:---:|:---:|:---:|:---|
| **IT Electrical Load** | 254.8 MW | **637.0 MW** | 1,274.0 MW | Board TDP 700 W, server ratio 1.82 |
| **Facility Peak Power** | 356.7 MW | **891.8 MW** | 1,783.6 MW | Tropical PUE 1.40 |
| **National Colocation Share** | 22.65% | **56.62%** | 113.24% | Mid-2026 colocation capacity (1,575 MW) |
| **Annual Electricity** | 2.50 TWh | **6.25 TWh** | 12.50 TWh | 80% utilisation factor |
| **Annual Cooling Water** | 4,500 ML | **11,250 ML** | 22,499 ML | Baseline evaporative (1.80 L/kWh) |
| **Logic Wafer Starts** | 5,000 | **12,500** | 25,000 | Murphy defect yield (65% functional) |
| **TSMC Sub-5 nm Allocation** | 0.64% | **1.60%** | 3.21% | TSMC advanced capacity (~780k wpy) |
| **CoWoS Interposer Wafers** | 13,334 | **33,334** | 66,667 | 15 packages per 300 mm interposer wafer |
| **Global CoWoS Allocation** | 2.96% | **7.41%** | 14.81% | Global CoWoS capacity (~450k wpy) |
| **HBM3e Memory Stacks** | 1,600,000 | **4,000,000** | 8,000,000 | 8 stacks / accelerator card |
| **Global HBM Allocation** | 2.67% | **6.67%** | 13.33% | Global HBM output (~60M stacks/yr) |

---

## 5. Five-Pillar Framework

1. **Compute and Semiconductor Sovereignty** — logic wafer starts, advanced packaging (CoWoS), HBM supply.
2. **Energy and Grid Readiness** — substation capacity, transmission corridors, renewable integration.
3. **Data Centres and Physical Resources** — tropical PUE, cooling-water budgets, land and water constraints.
4. **Connectivity, Data and Secure Computing** — subsea cables, Indic multilingual corpora, secure enclaves.
5. **Governance, Investment and Indigenous Capability** — IndiaAI Mission, multilateral alliances, industrial policy.

The six-layer **Demand-Cascade Model** operationalises these pillars by propagating national GPU deployment targets bottom-up through board TDP → rack density → hall load → PUE → grid absorption → physical-resource demand.

---

## 6. Branching & Collaboration

| Branch | Purpose |
|--------|---------|
| `main` | Primary integration branch |
| `adarshv2` | **Current working branch** — Adarsh Singh's active revision line (author-block update, README overhaul) |

Remote: [`github.com/A2105s/Research-o-Thon`](https://github.com/A2105s/Research-o-Thon)

```bash
git fetch origin
git checkout adarshv2
```

---

## 7. Academic Citation

```bibtex
@inproceedings{singh2026sovereign,
  author    = {Dhingra, Madhavi and Singh, Adarsh and Bais, Parikshit Singh and Shrivastava, Anamidi and Sourav},
  title     = {Sovereign by Design: An Integrated Five-Pillar Framework for India's Strategic Compute and Artificial Intelligence Infrastructure},
  booktitle = {Proceedings of ResearchThon 2026},
  organization = {Amity University Madhya Pradesh},
  year      = {2026},
  address   = {Gwalior, India}
}
```

---

## 8. License

- **Code** (`model/`, `scripts/`): MIT License — see [`LICENSE_AND_ATTRIBUTION.md`](LICENSE_AND_ATTRIBUTION.md).
- **Manuscript & figures** (`manuscript/`, `figures/`): CC BY 4.0.
- **Third-party source PDFs** (`sources/`): © their respective publishers; included for academic citation only.

---

## 9. Contact

Questions and collaboration requests: **Parikshit Singh Bais** ([sillypari@gmail.com](mailto:sillypari@gmail.com)) or **Adarsh Singh** ([officialadarsh.in@gmail.com](mailto:officialadarsh.in@gmail.com)).
