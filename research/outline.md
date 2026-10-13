# Paper Outline — India's AI Infrastructure Sovereignty

**Paper Title:** India's AI Infrastructure Sovereignty: A Five-Pillar Resilience Framework for Mitigating Strategic Dependencies  
**Format:** IEEE Double-Column A4 Format (CPS Template)  
**Strict Limit:** Exactly 6 Pages (Dense, comprehensive, fully cited)  
**Target Submission:** Amity Researchothon 2026 (IEEE Format Aligned)  

---

## Page-by-Page Architectural Budget

| Page | Section | Target Word Count | Key Figures / Tables | Content Description |
|:---:|:---|:---:|:---|:---|
| **Page 1** | **Title, Authors, Abstract, Keywords**<br>**Section I: Introduction** | ~850 words | None | Title, affiliation, abstract (210 words), 5 keywords. The geopolitics of compute, weaponized interdependence, India's paradox: software leadership vs. hardware import dependence, research question & paper organization. |
| **Page 2** | **Section II: Architectural Decomposition: The Five-Pillar Stack**<br>• II-A: Silicon & Accelerator Fab<br>• II-B: High-Density Data Centres | ~850 words | **Figure 1:** Five-Pillar IAIRF Architecture Stack<br>**Table I:** Comparative Global Concentration (HHI) across Supply Tiers | Decomposition of Pillar 1 (Silicon, EDA, CoWoS packaging, the "borrowed silicon" vulnerability) and Pillar 2 (Data centre density, 40-100 kW racks, liquid cooling, PUE challenges in tropical climates). |
| **Page 3** | **Section II (Cont.): Pillars 3, 4, 5**<br>• II-C: Energy & Grid Integration<br>• II-D: Sovereign Models & Data Trusts<br>• II-E: Strategic Governance | ~850 words | **Table II:** India Data Centre Metrics by Metro Hub (MW, PUE, Subsea Cables)<br>**Figure 2:** India Data Centre Capacity vs Green Power (2020-2030) | Decomposition of Pillar 3 (peak demand 250 GW, captive renewable PPAs), Pillar 4 (Sarvam 30B/105B, BharatGen, AI Kosh 14k datasets), and Pillar 5 (Semicon 2.0 ₹1,27,500 cr, IndiaAI ₹10,372 cr, Pax Silica coalition). |
| **Page 4** | **Section III: Quantitative Vulnerability Modeling & Unit Economics**<br>• III-A: Mathematical Formulation of IAIRF<br>• III-B: Cascading Dependency Matrix<br>• III-C: TCO & Subsidy Sustainability | ~800 words | **Equation (1):** Vulnerability Score $V_i$<br>**Equation (2):** Systemic Resilience Index $R$<br>**Figure 3:** HHI Concentration Gradient across AI Value Chain | Mathematical formulation of Vulnerability Index and Systemic Resilience. Empirical scoring of each pillar. Cascading failure dynamics. Unit economics: ₹65/hr vs $2.80/hr commercial hyperscaler pricing. |
| **Page 5** | **Section IV: Strategic Roadmap & Policy Architecture**<br>• IV-A: Horizon 1 (0–3 Yrs): Compute Pooling & Open Runtimes<br>• IV-B: Horizon 2 (3–7 Yrs): Packaging, Mature Fabs & RISC-V<br>• IV-C: Horizon 3 (7–12 Yrs): Sub-7nm Partnerships & Pax Silica | ~850 words | **Table III:** Three-Horizon Strategic Roadmap Matrix (Actions, Budgets, Milestones, KPIs) | Concrete policy interventions: Chips to Startup (C2S), DLI expansion, domestic OSAT (Tata Sanand, Micron), RISC-V accelerator cores (Shakti, Vega), tax holidays to 2047, Quad/Pax Silica semiconductor pacts. |
| **Page 6** | **Section V: Conclusion & Future Outlook**<br>**Acknowledgment**<br>**References (1–20+)** | ~450 words text + ~400 words references | **Table IV:** Target vs Deployed Reality Benchmark | Summary of core findings, policy implications, limitations, future research trajectories. Minimum 18 IEEE-formatted citations (all strictly aligned, >12 from 2021–2026). |

---

## Detailed Mathematical Formulation (Section III)

### 1. Pillar Vulnerability Index ($V_i$)
For each pillar $i \in \{1, 2, 3, 4, 5\}$, the vulnerability score is defined as:
$$V_i = \omega_c \cdot \widetilde{\text{HHI}}_i + \omega_m \cdot M_i + \omega_e \cdot E_i$$
where:
- $\widetilde{\text{HHI}}_i = \frac{\text{HHI}_i}{10000} \in [0, 1]$ represents normalized global market concentration.
- $M_i \in [0, 1]$ represents the domestic import dependency ratio (share of domestic demand met by foreign imports).
- $E_i \in [0, 1]$ represents exposure to extraterritorial jurisdiction and export control sanctions (e.g. US EAR / BIS rules).
- $\omega_c + \omega_m + \omega_e = 1$ are calibrated sensitivity weights ($\omega_c = 0.35, \omega_m = 0.40, \omega_e = 0.25$).

### 2. Cascading Systemic Resilience Index ($R$)
Because a severe failure in upstream silicon or power immediately throttles downstream compute clusters, systemic resilience is modeled via an inter-pillar dependency matrix $\mathbf{D} \in \mathbb{R}^{5 \times 5}$:
$$R = 1 - \max_{k} \left[ V_k + \sum_{j \neq k} D_{kj} \cdot V_j \right]$$
where $D_{kj}$ quantifies the propagation coefficient of a disruption from pillar $k$ to pillar $j$.

---

## Target Visual Assets (to be generated in `/figures`)
1. **`fig1_architecture.png` / `.pdf`**: Architectural block diagram of the Five-Pillar IAIRF Stack.
2. **`fig2_hhi_gradient.png` / `.pdf`**: High-resolution bar chart of Herfindahl-Hirschman Index (HHI) across supply tiers (Gallium, EUV, CoWoS, Accelerators, Cloud, Models).
3. **`fig3_capacity_growth.png` / `.pdf`**: Dual-axis trajectory chart of India Data Centre Capacity (MW, 2020–2030) and Green Energy Penetration (%).
4. **`fig4_tco_comparison.png` / `.pdf`**: Comparative cost analysis of Sovereign Subsidized Compute (₹65/hr) vs. Foreign Commercial Clouds ($2.80/hr).
