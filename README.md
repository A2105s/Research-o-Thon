# A Demand-Driven Framework for India's AI Infrastructure Planning
## Linking Compute, Energy, Physical Resources, and Semiconductor Dependencies

[![ResearchThon 2026](https://img.shields.io/badge/Event-ResearchThon%202026-blue.svg)](https://amity.edu)
[![Format](https://img.shields.io/badge/Format-IEEE%20Conference-success.svg)](output/final_paper.pdf)
[![License: MIT](https://img.shields.io/badge/Code%20License-MIT-yellow.svg)](LICENSE_AND_ATTRIBUTION.md)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](model/requirements.txt)
[![Tests: Passing](https://img.shields.io/badge/Tests-10%2F10%20Passing-brightgreen.svg)](model/tests/)

**Institution:** Department of Computer Science & Engineering, Amity School of Engineering and Technology, Amity University Madhya Pradesh, Gwalior, India  
**Authors:** Adarsh Singh, Sourav, Anamidhi Shrivastava  
**Track:** AI Infrastructure, Semiconductor Sovereignty & Strategic Computing  

---

## 1. Executive Summary

National artificial intelligence (AI) strategies increasingly treat high-performance compute accelerators as primary instruments of technological sovereignty. However, compute scaling is physically bounded by electricity transmission, cooling water, semiconductor lithography, advanced packaging, and geopolitically concentrated supply chains.

This repository provides the complete, reproducible research codebase, evidence register, simulation models, and LaTeX manuscript for our **Five-Pillar Conceptual Framework** and six-layer **Demand-Cascade Model**. Evaluating three illustrative deployment scenarios (**200,000, 500,000, and 1,000,000 GPUs**), our model translates accelerator targets into:
- **IT Electrical Load & Substation Capacity:** 637.0 MW IT load and 891.8 MW peak facility draw (500k GPUs @ PUE 1.40).
- **National Grid Absorption:** Absorbs **56.62% of India's current operational colocation data centre capacity** (1,575 MW in mid-2026).
- **The Structural Chokepoint Inversion:** Refutes the widespread belief that front-end semiconductor fabrication capacity is India's binding physical bottleneck: required wafer starts represent merely **1.60%** of TSMC's annual sub-5nm output (12,500 wafers), whereas 2.5D advanced packaging (CoWoS) consumes **7.41%** of global capacity ($4.6\times$ higher intensity) and HBM3e absorbs **6.67%** of global production.

---

## 2. Repository Architecture

```text
ResearchThon_Final/
├── README.md                      # Complete project overview & reproduction guide
├── LICENSE_AND_ATTRIBUTION.md     # MIT (code) & CC BY 4.0 (manuscript) licensing
├── .gitignore                     # Repository hygiene exclusions
├── docs/
│   ├── event_guidelines/          # Official ResearchThon rules and rubrics
│   ├── project_brief/             # Master project brief and workflow roadmap
│   ├── audit_reports/             # Technical red-team verification reports
│   └── previous_versions/         # Preserved prior drafts and friend's repo paper
├── sources/
│   ├── source_manifest.csv        # SHA-256 audited manifest of all 500 scanned files
│   ├── duplicate_report.csv       # Exact hash duplicate registry
│   ├── research_papers/           # Curated primary research PDFs
│   └── official_reports/          # Government & industry censuses (MeitY, CEA, JLL)
├── research/
│   ├── research_gap.md            # Rigorous 5-point literature deficit assessment
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
├── figures/
│   ├── architecture/              # Fig 1: Six-layer cascade flowchart
│   ├── comparisons/               # Figs 2, 3, 4: Chokepoints, country benchmark, Pareto
│   └── sensitivity/               # Fig 5: Multi-parameter sensitivity tornado
├── tables/                        # Machine-readable CSV tables matching manuscript
├── manuscript/
│   ├── main.tex                   # IEEE conference LaTeX source code
│   ├── references.bib             # 23 verified BibTeX citations (2024–2026)
│   └── figures/                   # Vector PDFs and PNGs embedded in paper
├── presentation/
│   ├── speaker_notes.md           # 5-minute timed presentation script
│   └── jury_questions.md          # Defense Q&A register for jury evaluation
├── output/
│   ├── final_paper.pdf            # 5-page compiled submission PDF (IEEE format)
│   └── review_report.md           # Red-team compliance checklist
└── scripts/
    ├── compile_paper.py           # Automated PDF compiler
    └── generate_figures.py        # Matplotlib vector figure generator
```

---

## 3. Quick Start & Reproduction

### Prerequisites
- Python 3.10 or higher
- Optional: TeX Live / MikTeX (or use the built-in ReportLab compiler)

### Step 1: Install Dependencies
```bash
pip install -r model/requirements.txt
```

### Step 2: Run Unit Tests
```bash
python model/tests/test_demand_cascade.py
```

### Step 3: Run Model Simulation
```bash
python model/demand_cascade.py
```
Outputs are written to `data/scenario_outputs/` and `tables/`.

### Step 4: Regenerate Figures
```bash
python scripts/generate_figures.py
```
Vector PDFs and high-DPI PNGs are generated in `figures/` and copied to `manuscript/figures/`.

### Step 5: Compile Final PDF
```bash
python scripts/compile_paper.py
```
Compiles the publication-ready 5-page IEEE PDF to `output/final_paper.pdf`.

---

## 4. Key Findings

| Metric Layer | 200,000 GPUs | 500,000 GPUs (Baseline) | 1,000,000 GPUs | Constraint Source |
|:---|:---:|:---:|:---:|:---|
| **IT Electrical Load** | 254.8 MW | **637.0 MW** | 1,274.0 MW | Board TDP 700W, Server Ratio 1.82 |
| **Facility Peak Power** | 356.7 MW | **891.8 MW** | 1,783.6 MW | Tropical PUE 1.40 |
| **National Colocation Share** | 22.65% | **56.62%** | 113.24% | Mid-2026 Colocation Capacity (1,575 MW) |
| **Annual Electricity** | 2.50 TWh | **6.25 TWh** | 12.50 TWh | 80% Utilization Factor |
| **Annual Cooling Water** | 4,500 ML | **11,250 ML** | 22,499 ML | Baseline Evaporative (1.80 L/kWh) |
| **Logic Wafer Starts** | 5,000 | **12,500** | 25,000 | Murphy Defect Yield (65% functional) |
| **TSMC Sub-5nm Allocation** | 0.64% | **1.60%** | 3.21% | TSMC Advanced Capacity (~780k wpy) |
| **CoWoS Interposer Wafers** | 13,334 | **33,334** | 66,667 | 15 packages / 300mm interposer wafer |
| **Global CoWoS Allocation** | 2.96% | **7.41%** | 14.81% | Global CoWoS Capacity (~450k wpy) |
| **HBM3e Memory Stacks** | 1,600,000 | **4,000,000** | 8,000,000 | 8 stacks / accelerator card |
| **Global HBM Allocation** | 2.67% | **6.67%** | 13.33% | Global HBM Output (~60M stacks/yr) |

---

## 5. Academic Citation

```bibtex
@inproceedings{singh2026demanddriven,
  author    = {Singh, Adarsh and Sourav and Shrivastava, Anamidhi},
  title     = {A Demand-Driven Framework for India's AI Infrastructure Planning: Linking Compute, Energy, Physical Resources, and Semiconductor Dependencies},
  booktitle = {Proceedings of ResearchThon 2026},
  organization = {Amity University Madhya Pradesh},
  year      = {2026},
  address   = {Gwalior, India}
}
```
