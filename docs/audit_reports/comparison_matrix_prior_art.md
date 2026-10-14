# Stage B: Deep Review of Closest Prior Studies & Comprehensive Comparison Matrix

**Project:** ResearchThon 2026 — Amity University Madhya Pradesh  
**Document:** `revision_v2/comparison_matrix_prior_art.md`  
**Purpose:** Exhaustive comparative evaluation between the proposed Demand-Cascade Paper (v2) and the closest prior literature in the 91-document research corpus.

---

## 1. Synthesis of the Closest Prior Studies

### Study 1: Inherited Research Project (`friends repo`)
- **Title:** *India's AI Infrastructure Sovereignty: A Five-Pillar Resilience Framework for Mitigating Strategic Dependencies* (IAIRF)
- **Methodology:** Conceptual five-pillar decomposition + Heuristic Vulnerability Index ($V_i = \sum w_j c_{ij}$) + Qualitative Dependency Matrix $\mathbf{D}$.
- **Core Findings:** High concentration in photolithography and foundries (HHI > 7,000); computes composite resilience index $R = 0.18$; proposes 3-horizon policy roadmap.
- **Critical Limitations & Vulnerabilities:**
  1. *Heuristic Vulnerability Score ($R=0.18$):* The mathematical formulation assigns subjective weights without empirical calibration or unit consistency.
  2. *No Demand-Driven Physical Cascade:* Lacks bottom-up translation from GPU counts to MW, TWh, litres of water, and silicon wafers.
  3. *Static Baseline:* Discusses only the 10,000 subsidized GPU target under IndiaAI without analyzing 200k, 500k, or 1M scale trajectories.
  4. *Conflation of Fiscal Allocations:* Conflated IndiaAI (₹10,372 cr) with Semicon 2.0 (₹1,27,500 cr).

### Study 2: Akimitsu (August 2026, SUNY / arXiv:2607.29572)
- **Title:** *Artificial Intelligence: Supply-Chain Chokepoints and the Reach of Industrial Policy*
- **Methodology:** Microeconomic supply-chain graph modeling and empirical Herfindahl-Hirschman Index (HHI) quantification across 40+ production stages.
- **Core Findings:** Hardware stack exhibits extreme upstream asymmetry (ASML EUV HHI=10,000, Gallium HHI=9,804, CoWoS packaging HHI=8,100), while downstream model hosting is competitive (HHI=1,410). Concludes that standard industrial policy subsidies fail if upstream chokepoints are legally or physically concentrated.
- **Critical Limitations for India:**
  1. Does not model physical infrastructure demands (MW power, grid bottlenecks, cooling water).
  2. Does not model middle-power economies like India attempting to build national sovereign compute capacity.
  3. Static global equilibrium without scenario-based GPU deployment cascades.

### Study 3: Portulans Institute / Bruegel (García-Herrero & Dutta, 2026)
- **Title:** *Programmable Sovereignty: Coordinated Specialization as a Response to the N-2 Problem in AI*
- **Methodology:** Geopolitical and economic policy framework analyzing non-superpower nations ($N-2$).
- **Core Findings:** Full-stack semiconductor and AI autarky is impossible for non-US/China nations due to the $>\$30	ext{B}$ capital barrier of sub-3nm fabs. Proposes "Coordinated Specialization" (focusing on design, packaging, domain data, and open runtimes).
- **Critical Limitations:**
  1. Entirely qualitative policy treatise.
  2. Provides no quantitative resource-allocation thresholds or empirical capacity calculators.

### Study 4: International Energy Agency (IEA, 2024/2026)
- **Title:** *Energy and AI: World Energy Outlook Special Report* (304 pages)
- **Methodology:** Global macroeconomic energy system modeling, top-down data centre electricity tracking, and grid capacity forecasting to 2030/2035.
- **Core Findings:** Global DC electricity consumption to double from ~415 TWh to ~945 TWh by 2030. AI server power density increasing from 10–15 kW/rack to 40–100 kW/rack.
- **Critical Limitations for India:**
  1. Top-down regional aggregates (India grouped into broader Asia-Pacific or high-level totals).
  2. Ignores microelectronics supply-chain feedbacks (wafer starts, CoWoS, HBM).
  3. Uses temperate climate assumptions (PUE 1.15–1.20) rather than tropical Indian realities (PUE 1.40–1.55).

### Study 5: Lawrence Berkeley National Laboratory (Shehabi et al., 2024/2025)
- **Title:** *2024 United States Data Center Energy Usage Report* (79 pages)
- **Methodology:** Bottom-up server inventory modeling, hyperscale facility audits, and PUE/WUE efficiency curve regressions.
- **Core Findings:** Validates server overhead multipliers ($\mu_{	ext{server}} pprox 1.75 - 1.90$) and hyperscale PUE distributions.
- **Critical Limitations:** Geographically restricted to the United States grid; does not consider non-US export controls or sovereign supply-chain vulnerabilities.

### Study 6: JLL & CBRE India Reports (2026 Mid-Year)
- **Title:** *India Data Centre 2026 Mid-Year Report: AI Appetite Unleashed*
- **Methodology:** Census of all operational and under-construction colocation facilities across India's top 7 metros.
- **Core Findings:** Operational capacity reached 1,575 MW in mid-2026; 3,200 MW in pipeline; 52.4% concentrated in Navi Mumbai. Substation allocation lead times span 36–48 months.
- **Critical Limitations:** Pure real-estate market census with no microelectronic hardware or semiconductor modeling.

---

## 2. Multi-Dimensional Comparison Matrix

| Evaluation Dimension | Inherited Draft (`friends repo`) | Akimitsu (2026, SUNY) | Portulans Institute (2026) | IEA / LBNL (2024-2026) | **Our Proposed Paper (v2)** |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Primary Method** | Conceptual 5-Pillar + Heuristic Index ($V_i$) | Econometric HHI chokepoint graph | Qualitative policy statecraft | Top-down macroeconomic energy modeling | **First-principles Demand-Cascade Model + 5-Pillar Systems Engineering** |
| **Model Reproducibility** | Static script (ReportLab) | Analytical math formulas | Descriptive qualitative | Macro scenario models | **Fully reproducible Python engine (deterministic CSV outputs, unit tests)** |
| **GPU Deployment Scenarios** | Static 10k/45k policy mentions | None | None | Regional TWh aggregates | **Explicit 200k, 500k, and 1,000,000 GPU scenarios** |
| **Server-to-Facility Electrical Cascade** | Qualitative PUE mention | None | None | Sector-level PUE averages | **Disaggregated: Chip TDP $\to$ Server Overhead (1.82) $\to$ IT MW $\to$ Facility Peak MW $\to$ Annual TWh** |
| **Tropical Climate & Cooling Disaggregation** | None | None | None | Temperate baselines (1.15-1.25) | **Tropical PUE penalty (1.40-1.55), evaporative WUE (1.80 L/kWh) vs Closed-loop D2C (<0.15 L/kWh)** |
| **Semiconductor Front-End Wafer Starts** | Mentions TSMC share qualitatively | Wafer stage HHI (5,400) | Policy fab discussion | None | **Murphy defect yield equation ($A=814\text{ mm}^2, D_0=0.08$) $\implies$ 12,500 wafers (1.60-1.74% TSMC)** |
| **Advanced Packaging & HBM Bottlenecks** | Mentions packaging as general risk | Packaging HHI (8,100) | Mentions OSAT | None | **Calculates 33,334 CoWoS interposers (7.41% global cap) & 4M HBM3e stacks (6.67% global cap)** |
| **National Grid & Infrastructure Absorption** | Mentions 1,575 MW colocation | None | None | National grid totals | **Quantifies operational colocation absorption (56.6%) vs 2030 planned pipeline absorption (27.9%)** |
| **Spatial Regional Grid Risk** | Mumbai mentioned qualitatively | None | None | Regional aggregates | **Mumbai grid share (26% city load) vs Delhi/Noida water stress vs RE captive RTC power** |
| **Policy Operationalization** | Generic 3-horizon timeline | Tax/subsidy limits | Coordinated Specialization taxonomy | Efficiency standards | **Actionable 3-tier matrix: Build Domestically, Partner Strategically, Manage Foreign Dependency** |

---
