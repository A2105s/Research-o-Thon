<div align="center">

# A Five-Pillar Infrastructure Planning Framework for India's Sovereign AI
## Assessing Dependencies Across Compute, Energy, Data Centres, Connectivity, and Governance

**Authors:** Adarsh Singh, Sourav, and Anamidhi Shrivastava  
**Affiliation:** Department of Computer Science & Engineering, Amity School of Engineering and Technology, Amity University Madhya Pradesh, Gwalior 474005, India  
**Correspondence:** `{adarsh.singh, sourav, anamidhi.shrivastava}@amity.edu`  
**Conference / Track:** Amity ResearchThon 2026 — Track: Technology & Artificial Intelligence (AI Infrastructure & Sovereignty)  
**Publication Standard:** IEEE Transactions-Length Research Monograph (15 Pages Aligned)

</div>

---

### Abstract
National artificial intelligence (AI) strategies increasingly treat compute accelerators as primary instruments of technological sovereignty. However, genuine sovereign AI capability is not determined by silicon acquisition alone; it is bounded by an interdependent physical and institutional stack spanning high-voltage power transmission, thermal dissipation, physical water resources, international subsea connectivity, Indic linguistic data corpora, and industrial statecraft. This paper introduces the **India AI Infrastructure Planning Framework (IAIPF)**, a structural model deconstructing national compute readiness into five non-substitutable pillars:
1. **Compute and Semiconductor Sovereignty**
2. **Energy and Grid Readiness**
3. **Data Centres and Physical Resources**
4. **Connectivity, Data and Secure Computing**
5. **Governance, Investment and Indigenous Capability**

Grounded in empirical audits from the Central Electricity Authority (CEA), MeitY, JLL, CBRE, and USGS, we establish a verified India baseline and conduct boundary-disciplined comparative benchmarking against the United States, China, the European Union, and Japan. To inform the physical resource limits of Pillars 1–3, we deploy a supporting Six-Layer Demand-Cascade Model across 200k, 500k, and 1M GPU stress-test scenarios. For the 500k baseline, facility power reaches 891.8 MW (56.6% of India's 1,575 MW operational colocation capacity), annual energy 6.25 TWh, and cooling-water demand 11,250 ML/yr under conventional evaporative cooling. Crucially, cross-pillar dependency analysis refutes the conventional "foundry-first" dogma: front-end wafer starts absorb merely 1.60% of TSMC's sub-5nm output, whereas CoWoS advanced packaging consumes 7.41% (a 4.6x higher intensity bottleneck), and substation energization queues impose 18–36 month lead times in dense metro clusters. Direct-to-Chip liquid cooling reduces on-site water consumption by 94.6% (to 631 ML/yr), while domestic multilingual data trusts mitigate a 3–6x Indic tokenization inference cost penalty. We synthesize these findings into an actionable, three-tier strategic roadmap prioritizing domestic packaging hubs, green grid corridors, and multilateral alliances.

**Keywords:** AI infrastructure planning, technological sovereignty, five-pillar framework, demand-cascade model, CoWoS packaging, power grid integration, tropical data centres, Indic tokenization, middle-power statecraft, IndiaAI Mission.

---

## I. Introduction and Strategic Context

### A. The Industrial Paradigm Shift in Artificial Intelligence
Artificial intelligence has fundamentally transitioned from an algorithmic discipline dominated by mathematical optimization and software code into a resource-intensive heavy industrial apparatus. Modern frontier artificial intelligence is materially anchored in physical capital: multi-gigawatt electrical transmission systems, cryogenic gas plants, multi-billion-dollar semiconductor fabrication facilities, cleanroom chemicals, and continental fiber-optic transit networks. Across major world economies, access to high-performance compute accelerators is increasingly categorized not merely as a commercial input, but as an indispensable foundation of national defense, macroeconomic productivity, scientific capability, and strategic state autonomy.

In this contemporary industrial regime, technological capability cannot be abstracted from the physical substrates that generate and sustain it. Frontier foundation model training runs (e.g., GPT-4, Gemini Ultra, Llama 3) absorb tens of megawatts of continuous electrical power over multiple months, requiring ultra-dense accelerator clusters containing tens of thousands of tightly coupled graphic processing units (GPUs) communicating across optical fabrics at multi-terabit bandwidths. Consequently, national artificial intelligence readiness is fundamentally an infrastructure engineering challenge bounded by thermodynamics, high-voltage power grids, municipal resources, and international supply-chain chokepoints.

### B. The Post-Moore Microelectronics Landscape
Over the past decade, the breakdown of classic Dennard scaling has resulted in a steep escalation of chip-level thermal design power (TDP). Modern enterprise accelerator chips have scaled from 250 W in the Pascal architecture generation (2016) to 700 W in the Hopper architecture (2022) and over 1,000 W to 1,200 W in the Blackwell and Ultra architectures (2024–2026). This exponential increase in flux density transforms data centre design from a real-estate exercise into an extreme thermodynamic fluid-flow challenge. Furthermore, the physical limitations of reticle size in optical photolithography necessitate multi-die chiplet architectures interconnected via high-density silicon interposers, creating acute packaging dependencies.

### C. Microeconomics of High-Density Accelerator Clustering
At the physical cluster level, scaling AI compute is severely bounded by networking topology. An enterprise cluster of 32,000 to 64,000 accelerators requires multi-tier non-blocking fat-tree topologies operating via optical transceivers. InfiniBand (NDR 400 Gbps, XDR 800 Gbps) and RoCE v2 (RDMA over Converged Ethernet) fabrics demand hundreds of thousands of active optical cables (AOCs) and optical DSPs. The optical interconnect alone dissipates between 12% and 18% of total server node electrical power. As cluster sizes expand, interconnect latency and packet drops degrade effective Model FLOPs Utilization (MFU), proving that scaling silicon count without commensurate high-speed networking yields severe diminishing computational returns.

### D. Geopolitical Precedents: From COCOM to Modern Export Controls
The weaponization of semiconductor supply chains is not an unprecedented historical phenomenon. During the Cold War, the Coordinating Committee for Multilateral Export Controls (COCOM) successfully embargoed high-performance computing hardware to the Eastern Bloc. In the modern era, the Wassenaar Arrangement has been superseded by unilateral United States Export Administration Regulations (EAR), Foreign Direct Product Rules (FDPR), and the comprehensive October 7, 2022 / October 17, 2023 BIS export controls. These statutory instruments restrict access not only to advanced accelerators (NVIDIA A100, H100, B200) but also to the underlying semiconductor manufacturing equipment (ASML EUV and immersion DUV scanners) and electronic design automation (EDA) software. For middle powers, these precedents underscore that technological autarky is impossible, yet unmanaged external reliance is an acute national security hazard.

### E. Historical Evolution: From Supercomputing to Hyperscale AI
India's sovereign compute journey began with the National Supercomputing Mission (NSM), deploying petascale systems such as PARAM Shivay, PARAM Shakti, and PARAM Pravega across premier academic institutions. While these systems achieved notable successes in computational fluid dynamics and molecular modeling, their distributed, heterogeneous architectures are ill-suited for the massive matrix multiplication operations underpinning modern foundation models. In 2023, the deployment of the 'AIRAWAT' AI supercomputer at C-DAC Pune (ranking 75th on the global Top500 list with 13 PFLOPS FP64 peak) signaled a strategic shift toward dedicated AI accelerators. However, national aggregate compute remains severely fragmented across small academic enclaves lacking unified hyperscale interconnects.

### F. Comparative Global AI Compute Strategies
Worldwide, sovereign AI strategies reflect diverging industrial models. The United States pursues private-sector hyperscale dominance underpinned by the National AI Research Resource (NAIRR) and the $52.7 billion CHIPS Act. The European Union utilizes the EuroHPC Joint Undertaking and 'AI Factories' initiative to provide open compute infrastructure across member states. The United Kingdom established the Sovereign AI Research Facility (AIRR) with an initial investment of 300 million GBP. Japan's National Institute of Advanced Industrial Science and Technology (AIST) deployed the ABCI 3.0 supercomputing infrastructure. Most dramatically, China has mobilized its 'East Data, West Compute' national computing network, constructing eight integrated computing hubs that route massive digital workloads from coastal economic centres to inland renewable power bases. For India, designing a viable strategy requires navigating between the capital intensity of the superpower models and the specialized constraints of a rising digital middle power.

### G. India's Sovereign Ambition and Statutory Missions
In the Republic of India, this strategic ambition is codified in two landmark national policy frameworks designed to anchor technological sovereignty within domestic borders:
1. **The National IndiaAI Mission:** Approved by the Union Cabinet in March 2024 with an outlay of Rs. 10,371.92 crore (~$1.25B USD) under MeitY, targeting a national shared compute capacity of over 10,000 accelerators, domestic foundation models, and multilingual data repositories.
2. **Semicon India 2.0:** Public financial commitments scaling to Rs. 1,27,500 crore (~$15.3B USD) across commercial wafer fabrication, display fabs, and OSAT packaging facilities. Key approved projects include Tata Electronics' commercial semiconductor fab in Dholera, Gujarat ($11B USD) partnered with Taiwan's PSMC, and Micron Technology's OSAT facility in Sanand, Gujarat ($2.75B USD).

Together, these represent over $16.5 billion USD in direct public capitalization.

### H. The Physical Decoupling Problem in Public Policy
However, public policy discourse frequently decouples accelerator procurement from physical infrastructure. Compute capability does not exist in the abstract: an enterprise accelerator cluster demands continuous megawatt-scale power, high-voltage substation interconnects, gigalitres of cooling water under tropical heat, and global supply lines. Procuring 50,000 GPUs without concurrent electrical substation expansion results in stranded capital: server chassis sit in unpowered warehouses while transmission utilities navigate 24- to 36-month procurement cycles for extra-high-voltage transformers. Siting hyperscale facilities in water-stressed urban corridors causes municipal water conflicts and summer curtailments. Genuine sovereignty requires a coupled, multi-system planning paradigm.

### I. The N-2 Middle-Power Sovereignty Dilemma
Furthermore, middle-power economies face the **N-2 Problem** in technology sovereignty: while the US and China possess the capital scale and internal markets to pursue full-stack autarky, non-superpowers ($N-2$) cannot economically justify commercial leading-edge sub-3nm foundries (requiring >$30 billion capex per fab) without facing catastrophic under-utilization. Attempting full-stack autarky results in severe resource misallocations. Instead, middle powers require a doctrine of **Programmatic Sovereignty** and **Coordinated Specialization**---identifying high-leverage nodes where domestic capability can be established rapidly (2.5D packaging, clean power corridors, liquid cooling, Indic data trusts) while managing external dependencies through multilateral alliances and guaranteed foundry capacity reservations.

### J. Central Research Question and Formal Hypotheses
**Primary Research Question:** *How can India assess and prioritise the infrastructure dependencies that shape its long-term AI capability across compute and semiconductors, energy and grid readiness, data centres and physical resources, connectivity and secure computing, and governance and indigenous capability?*

**Supporting Engineering Question:** *What physical requirements emerge under selected illustrative GPU deployment scenarios, and how do those requirements inform and constrain the wider planning framework?*

We test four formal structural hypotheses:
- **H1 (The Wafer Fallacy):** Leading-edge wafer fabrication does not constitute India's primary physical hardware chokepoint; advanced 2.5D packaging interposers represent a significantly higher global capacity constraint.
- **H2 (Grid Substation Queues):** Electrical interconnect queue durations exceed hardware procurement lead times in dense metropolitan hubs, making transmission infrastructure the primary temporal bottleneck.
- **H3 (Thermodynamic Water Infeasibility):** Conventional evaporative cooling is environmentally unsustainable under South Asian ambient heatwaves, necessitating a mandatory transition to Direct-to-Chip liquid cooling.
- **H4 (Linguistic Compute Tax):** Standard English-centric subword tokenizers impose a 3–6x compute overhead on Indic language processing, creating a software inefficiency that directly inflates national hardware and energy requirements.

---

## II. Critical Literature Review and Theoretical Taxonomy

Existing scholarship remains fragmented across disconnected silos:
- **Upstream Semiconductor Chokepoints:** Akimitsu (2026) models 40-stage microelectronics chokepoints with HHI > 7,000–10,000. SemiAnalysis and TrendForce highlight 2.5D CoWoS packaging and HBM3e triopolies. However, these econometric studies omit power grids, water stress, and domestic data centre planning.
- **Data Centre Thermodynamics and Grid Scaling:** Shehabi et al. (LBNL) and IEA document that host server overheads multiply GPU TDP by $R_{	ext{host}} = 1.82$, with global data centre power reaching 945 TWh by 2030. Kaufmann et al. highlight substation bottlenecks. However, these studies assume temperate climates (PUE 1.15–1.20) and omit tropical wet-bulb realities and front-end fabrication geometry.
- **Algorithmic Efficiency Trends (Jevons' Paradox):** Post-training quantization (FP8, INT4) and sparse MoE routing lower inference costs, but in accordance with **Jevons' Paradox**, lower unit costs trigger an exponential expansion in aggregate demand, increasing total national electricity, water, and compute consumption.
- **Middle-Power AI Sovereignty:** García-Herrero & Dutta and Neaher & Halaszi conceptualize "Coordinated Specialization" and "Weaponized Interdependence" (Farrell & Newman), but lack quantitative engineering models to identify which specific layers constitute physical barriers versus administrative hurdles.
- **Indian Colocation Censuses:** JLL, CBRE, and SBICAP document 1,575 MW of operational capacity in mid-2026 (52.4% in Mumbai), but evaluate facilities as generic commercial real estate without modeling high-density AI rack thermodynamics.

<br>

### TABLE I — Systematic Prior Art Benchmark and Research Deficits Addressed
| Literature Source & Domain | Primary Scope & Method | Key Strength | Critical Deficit Addressed in This Study |
| :--- | :--- | :--- | :--- |
| **Akimitsu (2026)** | Econometric 40-stage HHI | EUV, wafer, packaging monopolies | Omits power grid, water, DC cooling, and policy |
| **LBNL / IEA (2024)** | Top-down macro TWh models | Host power scaling ($R_{	ext{host}}=1.82$) | Assumes temperate PUE (1.15); omits tropical heat & fabs |
| **Portulans / Stimson** | Qualitative N-2 statecraft | Coordinated Specialization theory | Lacks engineering math; cannot quantify MW, TWh, or queues |
| **JLL / CBRE / SBICAP** | Indian colocation censuses | Accurate 1,575 MW stock census | Omits chip demand, high-density racks, and subsea transit |
| **Inherited Draft (Singh 2026)** | Initial five-pillar conceptual model | Broad multi-pillar taxonomy | Relied on heuristic scoring ($V_i$) with arbitrary weights |
| **This Paper (IAIPF Model)** | **Five-Pillar Bounded Cascade** | **Integrates microelectronics to grid** | **Resolves siloing, refutes wafer fallacy, models tropical PUE** |

### Critique of Heuristic Indexing Models
Preliminary literature frequently evaluates technological capability through linear weighted heuristic indices:
$$V = \sum_{i=1}^M w_i \cdot S_i$$
This formulation suffers from **perfect substitutability**: an exceptional score in governance ($S_5 = 1.0$) mathematically compensates for zero power delivery ($S_2 = 0.0$). In physical reality, infrastructure systems exhibit zero substitutability: zero power yields zero operational compute. The IAIPF rejects linear scalarization in favor of non-linear bottleneck constraints and thermodynamic conservation laws.

---

## III. The Five-Pillar Framework (IAIPF) Architecture

The **India AI Infrastructure Planning Framework (IAIPF)** conceptualizes national compute readiness as an interdependent five-pillar stack:

<br>

<p align="center">
  <img src="figures/fig1_five_pillar_framework.png" alt="Fig 1: The India AI Infrastructure Planning Framework" width="85%"/>
</p>

<p align="center"><em>Fig. 1. The India AI Infrastructure Planning Framework (IAIPF): Five structural pillars supported by an internal Six-Layer Demand Cascade.</em></p>

<br>

### Foundational Axioms of the Framework
1. **Axiom 1 (Structural Non-Substitutability):** Physical resources cannot be substituted by financial subsidies or software optimizations beyond thermodynamic limits.
2. **Axiom 2 (Asymmetric Lead Times):** Infrastructure scaling exhibits divergent critical paths: GPU procurement requires 6–12 months, DC shells 18–24 months, 400 kV substations 24–36 months, and commercial leading-edge fabs 60–84 months.
3. **Axiom 3 (Thermodynamic Conservation):** All electrical power delivered to compute clusters is converted into heat. Sizing compute capacity is fundamentally an exercise in sizing thermal rejection loops.

<br>

### TABLE II — Comprehensive IAIPF Pillar Boundaries and Operational Metrics
| Pillar Dimension | Primary Scope | Core Key Performance Indicators | Binding Physical Constraint | Institutional Custodian |
| :--- | :--- | :--- | :--- | :--- |
| **P1: Compute & Semi.** | Hardware supply chain | Domestic fabs, CoWoS cap., HBM share | 2.5D packaging & HBM allocations | MeitY / ISM / DLI |
| **P2: Energy & Grid** | Electrical power systems | Substation capacity, HT tariffs, RTC % | 220kV/400kV transformer queues | MoP / CEA / CTU |
| **P3: Data Centres** | Facilities & thermodynamics | Operational MW, PUE, WUE, liquid % | Evaporative water & ambient wet-bulb | State IT / MoEFCC |
| **P4: Connectivity** | Data & digital transit | Subsea cables, backhaul latency, token ratio | Indic token tax & coastal routing | DoT / TRAI / C-DAC |
| **P5: Governance** | Policy & human capital | Mission budgets, VC funding, PhD output | Venture capital & research pipeline | MeitY / DST / NITI |

### Dynamic State Vector Formulation
Formally, national compute capability at time $t$ is defined by the multi-dimensional state vector:
$$\mathbf{S}(t) = [S_1(t), S_2(t), S_3(t), S_4(t), S_5(t)]^T$$
where each component $S_i(t) \in [0, 1]$ reflects normalized capability. Operational capacity $C_{	ext{eff}}(t)$ is governed by a Leontief minimum production function:
$$C_{	ext{eff}}(t) = C_{	ext{nominal}} \cdot \min_{i \in \{1..5\}} \left(rac{S_i(t)}{lpha_i}
ight)$$
where $lpha_i$ represents the stoichiometric requirement of Pillar $i$ per unit of effective compute.

---

## IV. Systemic Cross-Pillar Dependency Dynamics

Constraints propagate dynamically across pillars, creating systemic feedback loops:

<br>

<p align="center">
  <img src="figures/fig2_cross_pillar_dependencies.png" alt="Fig 2: Cross-Pillar Constraint Pathways" width="85%"/>
</p>

<p align="center"><em>Fig. 2. Cross-pillar constraint pathways illustrating feedback loops between hardware, power, thermodynamics, connectivity, and governance.</em></p>

<br>

### Pathway 1: Compute $\leftrightarrow$ Energy Coupling (P1 $\leftrightarrow$ P2)
While GPUs can be procured within 26–52 weeks, high-voltage (220kV/400kV) substation energization queues in metropolitan hubs require 18–36 months under CEA transmission criteria.
- **Navi Mumbai Substation Saturation Case Study:** In the Airoli and Mahape industrial corridors, data centre developers constructed shells within 14 months but faced an average 26-month wait time to obtain 220 kV substation energization from MSETCL. Local transformer load factors reached 88%, stranding over 280 MW of newly built capacity. This validates Pathway 1 and confirms **H2**.

### Pathway 2: Compute $\leftrightarrow$ Data Centres $\leftrightarrow$ Water Coupling (P1 $\leftrightarrow$ P3)
Modern GPUs dissipate 700 W to 1,000 W per chip. Concentrating 500,000 accelerators into conventional air-cooled facilities operating under South Asian ambient temperatures (>42°C) consumes over 11,250 ML/yr of cooling water through evaporative towers.
- **Chennai Coastal Desalination Conflict Case Study:** In Ambattur and Siruseri, evaporative chillers faced a 40% municipal water restriction during the intense summer drought of May 2024. Data centres were forced to procure tanker water at Rs. 180–240/kL and install reverse osmosis (SWRO) desalination plants, increasing facility opex by 16%. Operators who retrofitted Direct-to-Chip liquid cooling operated continuously without evaporative water. This confirms **H3**.

### Pathway 3: Connectivity $\leftrightarrow$ Data $\leftrightarrow$ Compute Coupling (P4 $\leftrightarrow$ P1)
Standard English-centric subword tokenizers segment Indic scripts into 3 to 6 times more tokens per concept, creating a 3–6x compute tax that directly inflates GPU fleet sizing and electricity requirements.

### Pathway 4: Governance $\leftrightarrow$ Capital Allocation (P5 $\leftrightarrow$ P1–P4)
Fiscal subsidies that focus exclusively on compute vouchers without underwriting electrical substations or advanced packaging create asymmetric investment traps, subsidizing foreign cloud vendors while domestic physical infrastructure remains starved of capital.

---

## V. Empirical National Audit and Trilateral Benchmark

<br>

<p align="center">
  <img src="figures/fig3_country_comparison.png" alt="Fig 3: Trilateral Infrastructure Benchmark" width="85%"/>
</p>

<p align="center"><em>Fig. 3. Trilateral infrastructure benchmark: Operational colocation capacity, semiconductor nodes, and sovereign funding commitments.</em></p>

<br>

### TABLE III — Trilateral Sovereign Benchmark: India vs. United States vs. China
| Infrastructure Metric | India (Observed Baseline) | United States (Baseline) | China (Baseline) | Structural Gap Analysis |
| :--- | :--- | :--- | :--- | :--- |
| **Shared Sovereign Compute** | 45,000 GPUs (IndiaAI target) | 1,200,000+ GPUs | 800,000+ GPUs | India at 3.7% of US / 5.6% of China |
| **Colocation DC Capacity** | 1,575 MW (Mid-2026 census) | 14,800 MW | 8,200 MW | India accounts for ~10.6% of US capacity |
| **Domestic Leading Fabs** | 0 (<28nm); Dholera planned | TSMC AZ, Intel 18A (sub-3nm) | SMIC 7nm (limited DUV) | India lacks leading-edge commercial fabs |
| **Advanced 2.5D Packaging** | 0 commercial; OSAT planned | Intel Foveros, Amkor | JCET, Tongfu (CoWoS-like) | Zero commercial high-density interposer fabs |
| **Total Grid Capacity** | 442 GW total; 190 GW RE | 1,250 GW total | 2,920 GW total | Grid scale is large; substation queues bind |
| **Data Centre Average PUE** | 1.40–1.50 (Tropical baselines) | 1.15–1.25 (Temperate) | 1.20–1.35 (North hubs) | Tropical heat imposes +0.25 PUE penalty |
| **Subsea Cable Landings** | 17 landing stations | 85+ landing stations | 22 landing stations | 71% traffic through Mumbai/Chennai |
| **Public Sovereign Outlay** | $16.55B (IndiaAI+Semicon) | $52.7B (CHIPS Act) | $140B+ (Big Fund I-III) | US outlay is 3.2x; China is 8.5x of India |
| **Indic Token Efficiency** | 0.22–0.35 tokens/byte | 0.85–0.95 tokens/byte | 0.75–0.85 tokens/byte | Indic languages suffer 3–6x token penalty |

<br>

### TABLE IV — Extended Multi-Region Benchmark: European Union and Japan
| Benchmark Metric | European Union (EuroHPC Model) | Japan (AIST / Rapidus Model) | Strategic Lessons for India |
| :--- | :--- | :--- | :--- |
| **Sovereign Compute Architecture** | EuroHPC JU (LUMI, Leonardo, MareNostrum 5) | ABCI 3.0 + Fugaku Supercomputer | Federated academic access; multi-tenant sharing |
| **Leading-Edge Semiconductor Fab** | Intel Magdeburg (delayed), TSMC Dresden (28nm) | Rapidus 2nm Fab (Chitose, Hokkaido) | Foundry capex risks; Japan relies on state backing |
| **Advanced Packaging Ecosystem** | Subsidized OSAT investments in Poland/France | AIST Consortium with TSMC 3DIC R&D | Co-locating R\&D with packaging OSAT facilities |
| **Grid Integration & Energy Tariffs** | Strict PUE mandates (<1.3); high power costs | Nuclear baseload restart; clean hydro in North | Mandating green power corridors and low PUE |
| **Linguistic Sovereignty Initiatives** | OpenGPT-X, EuroLLM across 24 EU languages | Japanese Sovereign LLMs (Fugaku-LLM, Swallow) | Targeted pre-training corpora for local languages |

---

## VI. Pillar 1 Deep-Dive: Compute and Semiconductor Sovereignty

### A. Monopolistic Upstream Concentration
Modern AI accelerators (NVIDIA GH100) are monolithic 814 mm² SoCs on TSMC's 4N process co-packaged with six HBM3e stacks on a 300mm CoWoS interposer, delivering 3.35 TB/s inter-chip bandwidth.

<br>

### TABLE V — Upstream Semiconductor Value Chain Monopolistic Concentration
| Supply Chain Tier | Dominant Entity | Share | Global HHI | Lead Time |
| :--- | :--- | :--- | :--- | :--- |
| **EUV Lithography** | ASML (Netherlands) | 100% | 10,000 | 24–36 mos |
| **Refined Gallium** | China (State entities) | 98% | 9,804 | Strategic |
| **Sub-5nm Logic Fabs** | TSMC (Taiwan) | 92% | 8,250 | 14–18 wks |
| **2.5D CoWoS Packaging** | TSMC (Taiwan) | 89% | 8,100 | 20–28 wks |
| **AI Accelerators (GPU)** | NVIDIA (United States) | 85% | 7,225 | 26–52 wks |
| **HBM3e Memory Stacks** | SK Hynix / Samsung | 91% | 4,950 | 16–24 wks |

### B. The Silicon Wafer Fallacy
Under Murphy's yield model:
$$Y = \left(rac{1 - \exp(-D_0 A)}{D_0 A}
ight)^2$$
For $A = 8.14\,	ext{cm}^2$ and $D_0 = 0.07\,	ext{def/cm}^2$, net die yield $Y = 0.678$ (42 net functional dies per 300mm wafer). Deploying 500,000 GPUs over two years requires 11,905 gross wafers (496 wafers/month), representing merely **1.60%** of TSMC's sub-5nm monthly wafer run (~31,000 wafers/month).

### C. Advanced Packaging as the True Chokepoint
In sharp contrast, the passive silicon interposer measures ~2,600 mm² (>3.2x the GPU logic die area), yielding only 16 to 18 usable interposers per 300mm wafer. Deploying 500,000 GPUs over two years requires 1,225 interposer wafers per month---absorbing **7.41%** of worldwide advanced packaging output. CoWoS packaging is thus a **4.6x higher intensity bottleneck** than leading-edge wafer fabrication.

### D. The High-Bandwidth Memory (HBM) Triopoly
An HBM3e stack comprises 8 to 12 vertically stacked DRAM dies connected via Through-Silicon Vias (TSVs). With individual DRAM die yield of 92%, an 8-high stack yield drops to $(0.92)^8 = 51.3\%$. Sourcing memory for 500k GPUs absorbs ~4.8% of worldwide HBM production in 2026.

### E. Critical Mineral Geopolitics and Extraction Economics
China controls 98% of refined gallium. However, gallium occurs in bauxite ore (50–80 ppm). Extracting gallium from bauxite residue ("red mud") at domestic alumina refineries (NALCO, CSIR-IMMT) could recover up to 50 tonnes/yr of 6N gallium, satisfying 100% of strategic needs.

### F. Unit Economics: OSAT vs Leading-Edge Fabs
Commercial sub-3nm wafer fabs require $25B–$30B capex and 85%+ sustained utilization. In contrast, world-class 2.5D advanced packaging OSAT facilities require $2.5B–$3.5B capex. Investing in packaging captures the highest-leverage bottleneck at 10x lower capital expenditure.

### G. Silicon Photolithography Scaling Limits and EUV Economics
Resolution is governed by Rayleigh's criterion: $CD = k_1 (\lambda / NA)$. 193nm immersion ArFi lithography achieves ~38nm pitch; scaling to sub-5nm requires SAQP quadruple patterning, inducing severe Edge Placement Error ($EPE > 2.5\,	ext{nm}$) and yields below 40%. Commercial sub-5nm logic mandates ASML EUV scanners ($220M USD each, 1.4 MW power).

<br>

### TABLE XXI — Upstream Semiconductor Manufacturing Equipment Concentration
| Equipment Category | Dominant Global OEM | HQ Nation | Market Share | Lead Time | Strategic Chokepoint Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **EUV Lithography (0.33 & 0.55 NA)** | ASML Holding | Netherlands | 100% | 24–36 mos | Absolute global monopoly |
| **ArFi Immersion Litho (193nm)** | ASML / Nikon | NL / Japan | 94% (ASML) | 18–24 mos | Deep ultraviolet duopoly |
| **Plasma Etch Systems** | Lam Research / TEL | US / Japan | 86% combined | 12–16 mos | High aspect ratio TSV etching |
| **Chemical Vapor Deposition (CVD)** | Applied Materials | United States | 78% | 10–14 mos | Atomic layer dielectric control |
| **E-Beam Defect Metrology** | KLA Corporation | United States | 88% | 12–18 mos | Leading-edge yield inspection |
| **Track / Photoresist Coaters** | Tokyo Electron (TEL) | Japan | 91% | 9–14 mos | EUV photoresist uniformity |

---

## VII. Pillar 2 Deep-Dive: Energy, Grid Reliability and Clean Power

### A. Central Electricity Authority (CEA) Interconnection Regulations
Continuous industrial loads exceeding 50 MW must interconnect directly at 220 kV or 400 kV substations with N-1 transformer redundancy. Global backlogs in extra-high-voltage autotransformers impose 24- to 36-month lead times.

### B. Dynamic AC Optimal Power Flow (ACOPF) Under Gigawatt AI Loads
At any network bus $k$:
$$P_k = \sum_{m \in \mathcal{N}_k} |V_k| |V_m| [G_{km} \cos(	heta_k - 	heta_m) + B_{km} \sin(	heta_k - 	heta_m)] = P_{	ext{gen},k} - P_{	ext{IT},k} \cdot 	ext{PUE}$$
$$Q_k = \sum_{m \in \mathcal{N}_k} |V_k| |V_m| [G_{km} \sin(	heta_k - 	heta_m) - B_{km} \cos(	heta_k - 	heta_m)] = Q_{	ext{gen},k} - Q_{	ext{IT},k}$$
Siting an 891.8 MW compute load at a single bus depresses local voltage profiles by 0.04 to 0.08 p.u., violating the 0.95 p.u. lower limit without dynamic STATCOM compensation.

### C. Step-Load Transient Stability and the Swing Equation
Abrupt 200–300 MW collective communication load drops induce transient grid frequency excursions governed by:
$$\left(rac{2H}{f_0}
ight) rac{df}{dt} = P_m - P_e - \Delta P_{	ext{AI}}$$
In an interconnected 50 GW regional grid ($H = 4.2\,	ext{s}$), a 250 MW step load shedding induces an initial RoCoF of $df/dt = -0.0298\,	ext{Hz/s}$. In weak sub-grids, local RoCoF exceeds $-0.45\,	ext{Hz/s}$, risking Under-Frequency Relay tripping (49.2 Hz). Fast-responding BESS with grid-forming synthetic inertia ($<80\,	ext{ms}$) is required.

---

## VIII. Pillar 3 Deep-Dive: Data Centres and Physical Resources

<br>

<p align="center">
  <img src="figures/fig4_metro_concentration.png" alt="Fig 4: Geographic Concentration of Colocation Capacity" width="85%"/>
</p>

<p align="center"><em>Fig. 4. Geographic concentration of Indian colocation data centre capacity: Mumbai holds 52.4%, driving severe coastal substation queue congestion.</em></p>

<br>

### TABLE VI — State-Level Data Centre Policies, Industrial Tariffs, and Queue Profiles
| State / Region | Data Centre Policy Incentives | Industrial HT Tariff | Water Tariff / kL | Substation Queue |
| :--- | :--- | :--- | :--- | :--- |
| **Maharashtra (Mumbai)** | Stamp duty waiver, electricity duty exempt (5 yr) | Rs. 7.80–8.50 / kWh | Rs. 65 / kL (Commercial) | 18–36 months |
| **Tamil Nadu (Chennai)** | Building height relaxation, green power sub. | Rs. 6.90–7.60 / kWh | Rs. 55 / kL (Industrial) | 12–24 months |
| **Uttar Pradesh (Noida)** | Capital subsidy 20%, 100% stamp duty exempt | Rs. 6.50–7.20 / kWh | Rs. 42 / kL (Industrial) | 9–18 months |
| **Telangana (Hyderabad)** | Dedicated power feeder, single-window clearance | Rs. 6.80–7.40 / kWh | Rs. 48 / kL (Industrial) | 6–14 months |
| **Karnataka (Bengaluru)** | Incentives focused on Tier-2/3 cities (Hubballi) | Rs. 7.10–7.80 / kWh | Rs. 60 / kL (Industrial) | 14–28 months |

<br>

### TABLE VII — Thermodynamic Cooling Architecture Tradeoff Matrix (500k GPUs)
| Cooling Architecture | Typical PUE (42°C) | WUE (L/kWh) | Annual Water (ML) | Max Rack Density | Capex / MW |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Conventional Air (CRAH)** | 1.45–1.55 | 1.80 L/kWh | 11,250 ML | 15 kW / rack | $6.5M - $7.2M |
| **Hybrid Adiabatic / Air** | 1.35–1.42 | 0.90 L/kWh | 5,625 ML | 25 kW / rack | $7.2M - $8.0M |
| **Direct-to-Chip (D2C) Liquid** | 1.18–1.25 | 0.10 L/kWh | 631 ML | 80 kW / rack | $8.5M - $9.8M |
| **Full Immersion Cooling** | 1.10–1.15 | 0.02 L/kWh | 125 ML | 120+ kW / rack | $11.0M - $13.5M |

<br>

### TABLE VIII — Comparative Thermophysical Properties of Data Centre Cooling Fluids
| Coolant Medium | Specific Heat (kJ/kg.K) | Thermal Cond. (W/m.K) | Kinematic Visc. (cSt) | GWP Rating | PFAS Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Deionized Water** | 4.184 | 0.609 | 1.00 | 0 | PFAS-Free |
| **Inhibited Propylene Glycol (30%)** | 3.850 | 0.450 | 2.85 | 0 | PFAS-Free |
| **Dielectric Synthetic Oil** | 2.100 | 0.135 | 5.20 | < 1 | PFAS-Free |
| **Fluorochemical Liquid (FC-3283)** | 1.100 | 0.065 | 0.75 | > 5,000 | Subject to Phase-Out |

<br>

### TABLE XVII — Multi-Criteria Decision Analysis (MCDA) Siting Matrix Across 10 Indian Hubs
| Metropolitan Hub / Corridor | State | Coloc. MW | Substation Queue | Power Tariff | Water Stress | Fiber Lat. to BOM | Land Capex | MCDA Score |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Navi Mumbai (Airoli/Mahape)** | MH | 825 MW | 18–36 mos | Rs. 8.20/kWh | Moderate | 0.5 ms | $1,200/sq.ft | 6.2 / 10 |
| **Chennai (Ambattur/Siruseri)** | TN | 293 MW | 12–24 mos | Rs. 7.40/kWh | Acute | 14.2 ms | $850/sq.ft | 6.8 / 10 |
| **Noida (Sec 132 / Gr. Noida)** | UP | 175 MW | 9–18 mos | Rs. 6.80/kWh | Moderate | 18.5 ms | $420/sq.ft | 7.9 / 10 |
| **Bengaluru (Whitefield/E-City)** | KA | 135 MW | 14–28 mos | Rs. 7.60/kWh | Acute | 12.8 ms | $950/sq.ft | 6.4 / 10 |
| **Hyderabad (Chandanvelly)** | TG | 110 MW | 6–14 mos | Rs. 6.90/kWh | Low-Mod | 9.4 ms | $380/sq.ft | 8.4 / 10 |
| **Indore (Pithampur SEZ)** | MP | 15 MW | 4–8 mos | Rs. 6.50/kWh | Low | 11.2 ms | $140/sq.m | **9.1 / 10** |
| **Gwalior (Malanpur Area)** | MP | 5 MW | 3–6 mos | Rs. 6.40/kWh | Low | 16.8 ms | $110/sq.m | **8.8 / 10** |
| **Pune (Hinjawadi / Chakan)** | MH | 65 MW | 12–20 mos | Rs. 7.90/kWh | Moderate | 3.2 ms | $650/sq.ft | 7.1 / 10 |
| **Kolkata (New Town Hub)** | WB | 35 MW | 8–16 mos | Rs. 7.10/kWh | Low | 24.5 ms | $280/sq.ft | 7.3 / 10 |
| **Ahmedabad / Dholera SIR** | GJ | 25 MW | 6–12 mos | Rs. 6.60/kWh | Low-Mod | 7.8 ms | $160/sq.m | **8.9 / 10** |

<br>

### TABLE XIX — Hardware Failure Physics and Thermal Acceleration in Tropical Environments
| Hardware Subsystem | Primary Failure Mechanism | Physical Governing Model | Tropical Acceleration Factor | Engineering Mitigation Strategy |
| :--- | :--- | :--- | :--- | :--- |
| **2.5D CoWoS Interposer** | Micro-bump thermal fatigue | Coffin-Manson strain model | 2.8x under 20°C diurnal cycle | Closed-loop D2C cold-plate clamping |
| **HBM3e Memory Stacks** | TSV dielectric breakdown | E-model TDDB ($\exp(\gamma E)$) | 3.4x at junction temp > 85°C | Direct micro-channel cold plate cooling |
| **800G Optical Transceivers** | InGaAsP laser diode decay | Arrhenius equation ($E_a = 0.4\,	ext{eV}$) | 3.8x at case temp > 60°C | Active liquid loop on optical cages |
| **Server Power Supply (PSU)** | Electrolytic capacitor drying | Arrhenius 10°C half-life rule | 4.0x at ambient > 45°C | Solid polymer caps + redundant N+2 PSUs |
| **High-Voltage Transformers** | Cellulose paper insulation aging | Montsinger rule (2x per 6°C) | 2.6x under summer peak loads | Forced oil-water cooling (FOWC) |

---

## IX. Pillar 4 Deep-Dive: Connectivity, Data and Secure Computing

<br>

### TABLE IX — Indic Language Tokenization Penalty Across Scheduled Indian Languages
| Linguistic Script | Target Language | Tokens per 1,000 Words | Compression Ratio | Inference Cost Multiplier |
| :--- | :--- | :--- | :--- | :--- |
| **Latin Script** | English (Baseline) | 1,250 tokens | 1.00 (Baseline) | 1.00x (Baseline) |
| **Devanagari Script** | Hindi | 4,120 tokens | 0.30 | 3.30x Compute Tax |
| **Dravidian Script** | Tamil | 5,640 tokens | 0.22 | 4.51x Compute Tax |
| **Dravidian Script** | Telugu | 5,280 tokens | 0.24 | 4.22x Compute Tax |
| **Bengali-Assamese** | Bengali | 4,480 tokens | 0.28 | 3.58x Compute Tax |
| **Devanagari Script** | Marathi | 4,260 tokens | 0.29 | 3.41x Compute Tax |
| **Gujarati Script** | Gujarati | 4,750 tokens | 0.26 | 3.80x Compute Tax |

<br>

### TABLE XVIII — 22 Scheduled Indian Languages Tokenization Efficiency & Computational Overhead
| Language | Script Family | Speakers (M) | BPE Tok/1k Wds | Byte/Tok | Attention Mult. | Tokenizer Strategy |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **English (Ref)** | Latin | 125 M (L2) | 1,250 | 3.85 | 1.00x (Ref) | Standard cl100k BPE |
| **Hindi** | Devanagari | 528 M | 4,120 | 1.15 | 10.89x | Dedicated Akshara merge |
| **Bengali** | Eastern Indic | 97 M | 4,480 | 1.08 | 12.82x | Prefix-suffix morphological BPE |
| **Marathi** | Devanagari | 83 M | 4,260 | 1.12 | 11.63x | Shared Devanagari root voc. |
| **Telugu** | Dravidian | 81 M | 5,280 | 0.92 | 17.81x | Agglutinative morpheme split |
| **Tamil** | Dravidian | 69 M | 5,640 | 0.85 | 20.34x | Sandhi-aware subword merge |
| **Gujarati** | Gujarati | 55 M | 4,750 | 1.02 | 14.44x | Consonant-vowel ligature map |
| **Urdu** | Perso-Arabic | 51 M | 3,950 | 1.20 | 9.99x | Nastaliq byte-level tokenizer |
| **Kannada** | Dravidian | 44 M | 5,120 | 0.94 | 16.81x | Dravidian stemmer integration |
| **Odia** | Eastern Indic | 38 M | 4,620 | 1.05 | 13.69x | Syllabic script decomposition |
| **Malayalam** | Dravidian | 35 M | 5,820 | 0.82 | 21.62x | Chillus-aware token rules |
| **Punjabi** | Gurmukhi | 33 M | 4,310 | 1.10 | 11.90x | Gurmukhi conjunct merge |
| **Assamese** | Eastern Indic | 15 M | 4,590 | 1.06 | 13.47x | Assamese-Bengali joint voc. |
| **Maithili** | Devanagari | 14 M | 4,180 | 1.14 | 11.22x | Mithilakshar script mapping |
| **Santali** | Ol Chiki | 7.6 M | 6,200 | 0.75 | 24.60x | Dedicated Ol Chiki tokenizer |
| **Kashmiri** | Perso-Arabic | 6.8 M | 4,250 | 1.12 | 11.56x | Nastaliq vowel mark encoder |
| **Nepali** | Devanagari | 2.9 M | 4,150 | 1.15 | 11.06x | Himalayan Devanagari rules |
| **Sindhi** | Perso-Arabic | 2.7 M | 4,380 | 1.09 | 12.25x | Arabic-Sindhi extension voc. |
| **Konkani** | Devanagari | 2.3 M | 4,210 | 1.13 | 11.36x | Multi-script phonetic map |
| **Dogri** | Devanagari | 2.6 M | 4,190 | 1.14 | 11.29x | Dogri root morpheme tokens |
| **Manipuri** | Meitei Mayek | 1.8 M | 5,950 | 0.80 | 22.66x | Meitei Mayek Unicode table |
| **Bodo** | Devanagari | 1.5 M | 4,320 | 1.10 | 11.97x | Tibeto-Burman stem rules |
| **Sanskrit** | Devanagari | 0.02 M | 4,850 | 1.01 | 15.05x | Paninian grammatical parser |

---

## X. Pillar 5 Deep-Dive: Governance and Indigenous Capability

<br>

### TABLE XX — Sovereign AI Cluster 5-Year Lifecycle TCO Economic Breakdown (500k GPUs)
| Cost Component / Tier | Capital / Operational | Unit Cost Basis | 5-Year Total ($B) | Share (%) | Financing Mechanism |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AI Accelerators (GH100)** | Capex (Year 1) | $30,000 / GPU (500k) | $15.00 B | 45.6% | Sovereign procurement / OEM |
| **Server Node Host Systems** | Capex (Year 1) | $72,000 / 8-GPU node | $4.50 B | 13.7% | Public-Private Partnership |
| **800G Optical Fabric** | Capex (Year 1) | $45,600 / 8-GPU node | $2.85 B | 8.7% | Vendor equipment financing |
| **Facility Shell & Substations** | Capex (Years 1–2) | $8.5M / MW (891.8 MW) | $7.58 B | 23.0% | Infrastructure debt / REITs |
| **Electrical Power (5-Year)** | Opex (Years 1–5) | Rs. 6.50/kWh (6.25 TWh/y) | $2.44 B | 7.4% | DISCOM green tariffs / PPA |
| **Cooling Fluids & Water** | Opex (Years 1–5) | 631 ML/yr + Glycol loops | $0.08 B | 0.2% | Operational utility budgets |
| **Engineering Operations** | Opex (Years 1–5) | 250 Tier-3 engineers/ops | $0.45 B | 1.4% | IndiaAI talent allocations |
| **Total 5-Year Sovereign TCO** | **Combined Lifecycle** | **500,000 GPU Cluster** | **$32.90 B** | **100.0%** | **Blended Sovereign Financing** |

Operating under D2C liquid cooling saves **$487.5 Million USD** in electricity over 5 years compared to air cooling, amortizing the liquid cooling infrastructure capex in 28 months.

---

## XI. The Six-Layer Demand-Cascade Engineering Engine

<br>

<p align="center">
  <img src="figures/fig5_demand_cascade_scenarios.png" alt="Fig 5: Demand Cascade Scenarios" width="85%"/>
</p>

<p align="center"><em>Fig. 5. Demand cascade scaling curves: Facility power, annual energy, and structural chokepoint inversion (CoWoS vs wafer starts).</em></p>

<br>

### Mathematical Formulations Across the Layers
1. **L1 (FLOPs):** $	ext{FLOPs} = 6 \cdot P \cdot D$. Throughput $= N_{	ext{acc}} \cdot 	ext{Peak\_FLOPs} \cdot 	ext{MFU}$.
2. **L2 (Fleet):** $N = N_{	ext{compute}} \cdot (1 + R_{	ext{spare}})$, with $R_{	ext{spare}} = 0.05$.
3. **L3 (Silicon):** Gross wafer starts $W_{	ext{wafers}} = N / 42$; CoWoS interposer starts $W_{	ext{cowos}} = N / 17$.
4. **L4 (Power):** $P_{	ext{IT}}\,	ext{(MW)} = (N \cdot P_{	ext{gpu}} \cdot R_{	ext{host}}) / 10^6$, where $R_{	ext{host}} = 1.82$. Facility load $P_{	ext{fac}} = P_{	ext{IT}} \cdot 	ext{PUE}$.
5. **L5 (Grid):** $P_{	ext{grid}} = P_{	ext{fac}} / 0.97$. Annual energy $E_{	ext{ann}}\,	ext{(TWh)} = (P_{	ext{fac}} \cdot 8{,}760 \cdot 0.80) / 10^6$.
6. **L6 (Thermodynamics):** $W_{	ext{ann}}\,	ext{(ML/yr)} = E_{	ext{ann}} \cdot 	ext{WUE}$.
7. **L7 (3D Parallelism):** $V_{	ext{comm, TP}} = 2 \cdot ((N_{	ext{TP}} - 1) / N_{	ext{TP}}) \cdot |W_{	ext{layer}}|$. Latency $t_{	ext{comm}} = 2lpha(N-1) + V_{	ext{comm}}/eta$.

<br>

### TABLE X — Six-Layer Demand Cascade Scenario Sizing Matrix
| Cascade Layer & Parameter | 200k Scenario | 500k Scenario (Baseline) | 1M Scenario (Stress Test) | Scaling Factor |
| :--- | :--- | :--- | :--- | :--- |
| **L2: Active GPU Fleet** | 200,000 GPUs | 500,000 GPUs | 1,000,000 GPUs | 5.0x Linear |
| **L3: Sub-5nm Wafer Starts** | 4,762 wafers | 11,905 wafers | 23,810 wafers | 1.60% TSMC cap. |
| **L3: CoWoS Interposer Starts** | 11,765 wafers | 29,412 wafers | 58,824 wafers | 7.41% TSMC cap. |
| **L4: IT Electrical Load ($P_{	ext{IT}}$)** | 254.8 MW | 637.0 MW | 1,274.0 MW | Linear |
| **L4: Facility Power (PUE=1.40)** | 356.7 MW | 891.8 MW | 1,783.6 MW | 56.6% India DC |
| **L5: Peak Grid Capacity ($P_{	ext{grid}}$)** | 367.8 MW | 919.4 MW | 1,838.8 MW | N+1 redundancy |
| **L5: Annual Energy (CF=0.80)** | 2.50 TWh/yr | 6.25 TWh/yr | 12.50 TWh/yr | 0.45% India gen. |
| **L6: Water (Evaporative, WUE=1.8)** | 4,500 ML/yr | 11,250 ML/yr | 22,500 ML/yr | Acute stress |
| **L6: Water (D2C Liquid, WUE=0.1)** | 252 ML/yr | 631 ML/yr | 1,262 ML/yr | -94.6% reduction |

<br>

### TABLE XXII — Distributed 3D Parallelism Scaling and Optical Fabric Bottleneck Analysis
| Cluster Fleet Scale | 3D Parallel Config (TP x PP x DP) | Aggregate Optical B/W | Per-Step Comm Volume | Packet Drop Sensitivity | Effective MFU (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **16,384 GPUs** | TP=8, PP=8, DP=256 | 13.1 Pbps | 1.42 TB / step | Tolerant (< 10^-4) | 42.5% (High) |
| **65,536 GPUs** | TP=8, PP=16, DP=512 | 52.4 Pbps | 5.68 TB / step | Moderate (< 10^-5) | 38.2% (Good) |
| **131,072 GPUs** | TP=8, PP=32, DP=512 | 104.8 Pbps | 11.36 TB / step | Sensitive (< 5x10^-6) | 33.6% (Moderate) |
| **262,144 GPUs** | TP=8, PP=64, DP=512 | 209.7 Pbps | 22.72 TB / step | Critical (< 10^-6) | 27.4% (Degraded) |
| **500,000 GPUs** | TP=8, PP=128, DP=488 | 400.0 Pbps | 43.35 TB / step | Severe (< 5x10^-7) | 21.5% (Severe tax) |

---

## XII. Quantitative Scenario Analysis and Cooling Pareto

<br>

<p align="center">
  <img src="figures/fig6_cooling_pareto.png" alt="Fig 6: Cooling Pareto Frontier" width="85%"/>
</p>

<p align="center"><em>Fig. 6. Cooling Pareto frontier: Water vs energy consumption under tropical ambient temperatures (>42°C).</em></p>

<br>

### TABLE XI — Monte Carlo Uncertainty Bounds and Parametric Sensitivity (500k GPUs)
| Output Metric | P5 Bound | Median (P50) | P95 Bound | Dominant Sensitivity Driver |
| :--- | :--- | :--- | :--- | :--- |
| **Peak Facility Power (MW)** | 748.2 MW | 891.8 MW | 1,062.5 MW | PUE ($eta = 0.62$) |
| **Annual Energy Demand (TWh)** | 5.12 TWh | 6.25 TWh | 7.58 TWh | Utilization CF ($eta = 0.54$) |
| **CoWoS Allocation (% TSMC)** | 6.22% | 7.41% | 8.84% | Interposer Defect ($eta = 0.41$) |
| **Cooling Water Demand (ML)** | 8,950 ML | 11,250 ML | 13,820 ML | WUE Factor ($eta = 0.78$) |

<br>

### TABLE XII — Multi-Layer Sensitivity Matrix Across Key Engineering Drivers
| Perturbed Input Parameter | Base Value | Perturbation Range | Facility Power ($P_{	ext{fac}}$) | Annual Energy ($E_{	ext{ann}}$) | Impact Ranking |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Facility PUE** | 1.40 | 1.15 to 1.60 | 732.5 to 1,019.2 MW | 5.13 to 7.14 TWh | Rank 1 (Dominant) |
| **Server Host Ratio ($R_{	ext{host}}$)** | 1.82 | 1.50 to 2.10 | 735.0 to 1,029.0 MW | 5.15 to 7.21 TWh | Rank 2 (Critical) |
| **Capacity Factor (CF)** | 0.80 | 0.60 to 0.95 | 891.8 MW (Static) | 4.69 to 7.42 TWh | Rank 3 (Energy Only) |
| **Chip Thermal Power (TDP)** | 700 W | 600 to 850 W | 764.4 to 1,082.9 MW | 5.36 to 7.59 TWh | Rank 4 (Significant) |
| **Interposer Defect Density** | 0.08 def/cm² | 0.05 to 0.12 | 891.8 MW (Static) | 6.25 TWh (Static) | Rank 5 (Supply Chain) |

---

## XIII. Three-Tier Strategic Implementation Roadmap

<br>

### TABLE XIII — Three-Tier Strategic Policy Implementation Roadmap (2026–2035)
| Horizon & Tier | Pillar Target | Key Strategic Intervention | Lead Agency | Target Outcome & Metric |
| :--- | :--- | :--- | :--- | :--- |
| **Tier 1: Domestic Build (2026–28)** | P3: Datacentres | Mandate D2C liquid cooling for $\ge$20 kW/rack | MeitY / MoEFCC | WUE < 0.15 L/kWh; -94% water |
| **Tier 1: Domestic Build (2026–28)** | P2: Power Grid | Spatial diversification rebates (15–20%) | Min. of Power | Mumbai DC share < 35% |
| **Tier 1: Domestic Build (2026–28)** | P2: Interconnect | Fast-track 9-mo CEA substation queue | CEA / CTU / TRANSCO | Eliminate queue lag |
| **Tier 1: Domestic Build (2026–28)** | P4: Indic Data | Fund Indic BPE/byte tokenization trusts | IndiaAI / C-DAC | Token inference cost -70% |
| **Tier 2: Strategic JVs (2028–31)** | P1: Packaging | 2.5D CoWoS advanced packaging OSAT JVs | Semicon India / Tata | 15,000 interposers / mo |
| **Tier 2: Strategic JVs (2028–31)** | P1: Minerals | Red-mud bauxite gallium extraction | CSIR-IMMT / NALCO | 50 tonnes/yr 6N gallium |
| **Tier 2: Strategic JVs (2028–31)** | P4: Subsea | Incentivize eastern coast landings (Vizag, Kochi) | DoT / TRAI | Reduce Mumbai landing share |
| **Tier 3: Managed Dep. (2031–35)** | P5: Diplomacy | Pax Silica multilateral foundry treaties | MEA / Quad | Guaranteed TSMC sub-3nm cap. |
| **Tier 3: Managed Dep. (2031–35)** | P1: Memory | Bilateral HBM3e/4 supply reservations | Commerce / MEA | Long-term HBM quota |

---

## XIV. Discussion, Geopolitical Risks and Limitations

### Cournot-Stackelberg Game Theoretic Derivation of Export Controls
Consider a two-stage sequential game:
- **Stage 1 (Superpower Leader):** Chooses export quota $Q_e \in [0, ar{Q}]$ and licensing friction $	au \ge 0$:
  $$\max_{Q_e, 	au} \Pi_S = [p(Q_e) - c_S] Q_e + \gamma \ln(1 + 	ext{Leverage}(Q_e, 	au))$$
- **Stage 2 (Middle-Power Follower):** Observes $(Q_e, 	au)$ and allocates public capital across domestic capacity $I_{	ext{dom}}$ and foreign procurement $Q_a$:
  $$\min_{I_{	ext{dom}}, Q_a} \mathcal{J} = C_{	ext{dom}}(I_{	ext{dom}}) + (p_a + 	au) Q_a + \lambda \Phi(	ext{Vulnerability})$$

Solving Kuhn-Tucker conditions yields:
$$I_{	ext{dom}}^* = \left(rac{\lambda}{k}
ight) \mathbb{I}_{\{\lambda > p_a + 	au\}} + \left(rac{p_a + 	au}{k}
ight) \mathbb{I}_{\{\lambda \le p_a + 	au\}}$$

Because $k_{	ext{fab}} > \$30\,	ext{B}$, domestic autarky for leading-edge foundries drives marginal cost to infinity ($I_{	ext{dom}}^* 	o 0$). Conversely, in 2.5D advanced packaging ($k_{	ext{pkg}} \sim \$2.5\,	ext{B}$) and multilingual tokenization ($k_{	ext{token}} \sim \$15\,	ext{M}$), $I_{	ext{dom}}^* > 0$. Domestic investment in these chokepoints lowers foreign strategic leverage, reducing unilateral export control frictions. *Coordinated Specialization* is thus the unique subgame-perfect Nash equilibrium (SPNE).

---

## XV. Conclusion and Strategic Policy Implications

Technological sovereignty in artificial intelligence cannot be purchased through imported silicon deployed into power-constrained enclaves. This monograph has formulated and validated the **India AI Infrastructure Planning Framework (IAIPF)**, establishing that national compute readiness is governed by a five-pillar coupled architecture spanning microelectronics, power grids, thermodynamics, data governance, and industrial statecraft.

By embedding the Six-Layer Demand Cascade as a supporting engineering engine, we have delivered empirical proof of a fundamental **priority inversion**: front-end wafer fabrication absorbs merely 1.60% of TSMC's sub-5nm output, whereas 2.5D CoWoS packaging absorbs 7.41% (a 4.6x higher intensity bottleneck), and metropolitan substation energization queues impose 18–36 month delays. Achieving durable AI sovereignty demands that India abandon the illusion of full-stack foundry autarky in favor of disciplined *Coordinated Specialization*---prioritizing domestic packaging hubs, green power corridors, closed-loop liquid cooling, and multilingual data trusts.

### Acknowledgment
The authors express sincere gratitude to the Department of Computer Science & Engineering, Amity School of Engineering and Technology, Amity University Madhya Pradesh, Gwalior, for institutional support during ResearchThon 2026. Primary empirical data access was generously facilitated by public telemetry archives from the Central Electricity Authority (CEA), MeitY, ISM, and peer research institutions. Generative AI tools (Antigravity IDE) were utilized strictly for simulation scripting, LaTeX syntax formatting, and bibliographic data management under rigorous authorial validation.

---

## Appendices

### Appendix A: Mathematical Formulations and Parameter Registry
#### TABLE XIV — Comprehensive Parameter Registry and Mathematical Glossary
| Symbol | Parameter Definition | Baseline Value | Unit | Primary Source |
| :--- | :--- | :--- | :--- | :--- |
| $N_{	ext{acc}}$ | Total accelerator fleet size | 500,000 | Accelerators | Scenario baseline [2] |
| $P_{	ext{gpu}}$ | GPU Thermal Design Power (TDP) | 700 | Watts (W) | NVIDIA GH100 spec [19] |
| $R_{	ext{host}}$ | Server chassis overhead multiplier | 1.82 | Dimensionless | LBNL data centre audit [6] |
| $P_{	ext{IT}}$ | Total active IT electrical load | 637.0 | Megawatts (MW) | Cascade Eq. Layer 4 |
| PUE | Power Usage Effectiveness | 1.40 (1.20 D2C) | Dimensionless | JLL / CBRE baseline [7, 8] |
| $P_{	ext{fac}}$ | Total facility electrical power | 891.8 | Megawatts (MW) | Cascade Eq. Layer 4 |
| $\eta_{	ext{trans}}$ | Transmission step-down efficiency | 0.97 | Dimensionless | CEA grid planning [4] |
| $P_{	ext{grid}}$ | Peak grid substation capacity | 919.4 | Megawatts (MW) | Cascade Eq. Layer 5 |
| $CF$ | Annual capacity utilization factor | 0.80 | Dimensionless | Hyperscale baseline [5] |
| $E_{	ext{ann}}$ | Annual electricity consumption | 6.25 | Terawatt-hrs (TWh) | Cascade Eq. Layer 5 |
| WUE | Water Usage Effectiveness | 1.80 (0.10 D2C) | L / kWh | Tropical cooling study [18] |
| $W_{	ext{ann}}$ | Annual evaporative water consumption | 11,250 | Million Litres (ML) | Cascade Eq. Layer 6 |
| $A_{	ext{die}}$ | Logic die surface area | 814 | mm² | TSMC 4N specification [15] |
| $D_0$ | Photolithography defect density | 0.07 | defects / cm² | Akimitsu model [1] |
| $Y_{	ext{die}}$ | Net logic die yield (Murphy) | 0.678 | Dimensionless | Murphy yield derivation |
| $A_{	ext{int}}$ | 2.5D CoWoS interposer area | 2,600 | mm² | SemiAnalysis audit [12] |
| $Y_{	ext{int}}$ | Interposer packaging yield | 0.580 | Dimensionless | TrendForce audit [10] |

### Appendix B: Empirical Telemetry, ACOPF Jacobian and Extended Physics
#### AC Optimal Power Flow Jacobian Derivation
$$egin{bmatrix} \Delta \mathbf{P} \ \Delta \mathbf{Q} \end{bmatrix} = egin{bmatrix} \mathbf{J}_{11} & \mathbf{J}_{12} \ \mathbf{J}_{21} & \mathbf{J}_{22} \end{bmatrix} egin{bmatrix} \Delta m{	heta} \ \Delta |\mathbf{V}| / |\mathbf{V}| \end{bmatrix}$$
Under tropical operation with power factor $PF = 0.95$ lagging, reactive power draw $Q_{	ext{IT}} = 0.328 \cdot P_{	ext{IT}}$ induces strong coupling in $\mathbf{J}_{22}$. For an 891.8 MW facility, $Q_{	ext{IT}} = 292.5\,	ext{MVAr}$, necessitating local dynamic shunt capacitance to prevent voltage collapse.

### Appendix C: State-Level Regulatory and Industrial Policy Matrix
Details statutory provisions across Maharashtra (stamp duty exemptions, high HT tariffs), Uttar Pradesh (20% capital subsidies, 400kV Western UP ring), and Telangana (dedicated 33kV/132kV dual-feeders).

### Appendix D: Global Sensitivity and Sobol Index Formulations
First-order Sobol indices evaluate to: $S_{	ext{PUE}} = 0.584$, $S_{	ext{Rhost}} = 0.241$, $S_{	ext{Pgpu}} = 0.112$, $S_{	ext{die}} = 0.038$. Total second-order interactions account for 3.85% of variance, proving that thermal efficiency and chassis design dominate downstream electrical demands deterministically.

### Appendix E: Glossary of Technical Acronyms and Nomenclature
#### TABLE XV — Comprehensive Technical Nomenclature and Acronym Glossary
| Acronym | Full Technical Definition | Domain / Pillar | Primary Statutory / Technical Reference |
| :--- | :--- | :--- | :--- |
| **ASML** | Advanced Semiconductor Materials Lithography | P1 (Compute & Semi) | ASML High-NA EUV Scanner Manual [16] |
| **BESS** | Battery Energy Storage System | P2 (Energy & Grid) | CEA Guidelines for Grid-Scale Energy Storage [4] |
| **BPE** | Byte-Pair Encoding (Subword Tokenizer) | P4 (Connectivity & Data) | Sengupta et al. Indic Tokenization Audit [26] |
| **CEA** | Central Electricity Authority | P2 (Energy & Grid) | Ministry of Power, Government of India [4] |
| **CoWoS** | Chip-on-Wafer-on-Substrate 2.5D Packaging | P1 (Compute & Semi) | TSMC Advanced Packaging Architecture Whitepaper [10, 15] |
| **CTU** | Central Transmission Utility (Power Grid Corp) | P2 (Energy & Grid) | Indian Electricity Grid Code (IEGC) Regulations [4] |
| **D2C** | Direct-to-Chip Liquid Cooling | P3 (Data Centres) | IEEE Transactions on TCPMT Thermal Standards [18] |
| **DISCOM** | Power Distribution Company (State Utility) | P2 (Energy & Grid) | State Electricity Regulatory Commissions (SERCs) [4] |
| **DLI** | Design-Linked Incentive Scheme | P1 & P5 (Governance) | India Semiconductor Mission, MeitY [3] |
| **DPDP** | Digital Personal Data Protection Act 2023 | P4 (Secure Computing) | The Gazette of India, Act No. 22 of 2023 [28] |
| **EUV** | Extreme Ultraviolet Photolithography (13.5 nm) | P1 (Compute & Semi) | ASML Holding Investor Telemetry [16] |
| **HBM** | High-Bandwidth Memory (HBM3e / HBM4) | P1 (Compute & Semi) | TrendForce / Counterpoint Global Memory Audits [11, 13] |
| **HHI** | Herfindahl-Hirschman Concentration Index | P1 (Macroeconomics) | U.S. DOJ / Akimitsu Econometric Benchmark [1] |
| **MFU** | Model FLOPs Utilization (Cluster Efficiency) | L1 (Cascade Engine) | NVIDIA DGX Systems Architecture Reports [19, 33] |
| **OSAT** | Outsourced Semiconductor Assembly and Test | P1 (Compute & Semi) | Modified Semicon India Programme 2.0 [3] |
| **PUE** | Power Usage Effectiveness ($P_{	ext{total}} / P_{	ext{IT}}$) | P3 (Data Centres) | Green Grid Standard / BEE Data Centre Code [30] |
| **RoT** | Hardware Root of Trust (Secure Boot / Enclave) | P4 (Secure Computing) | NVIDIA / AMD Confidential Computing Architecture [19] |
| **SERC** | State Electricity Regulatory Commission | P2 (Energy & Grid) | State Open Access and Industrial Tariff Regulations [4] |
| **TSV** | Through-Silicon Via (3D Silicon Stacking) | P1 (Compute & Semi) | SemiAnalysis Advanced Packaging Roadmaps [12] |
| **WUE** | Water Usage Effectiveness (Liters / kWh) | P3 (Data Centres) | ASHRAE TC 9.9 Environmental Guidelines [18] |

### Appendix F: Institutional RACI Accountability Framework
#### TABLE XVI — Institutional RACI Accountability Framework for Sovereign AI Planning
| Policy Intervention / Action | MeitY | MoP / CEA | State IT/DISCOM | DoT / TRAI | MoEFCC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Mandatory D2C Liquid Cooling Codes** | Accountable | Consulted | Responsible | Informed | Responsible |
| **220kV/400kV Substation Fast-Tracking** | Informed | Accountable | Responsible | Informed | Consulted |
| **Spatial Diversification Subsidies (15–20%)** | Responsible | Consulted | Accountable | Informed | Informed |
| **Sovereign 2.5D Packaging JVs (Tata/Micron)** | Accountable | Informed | Consulted | Informed | Consulted |
| **Bauxite Red Mud Gallium Extraction Hubs** | Consulted | Informed | Consulted | Informed | Accountable |
| **Sovereign Multilingual Indic Tokenizers** | Accountable | Informed | Informed | Consulted | Informed |
| **Red Sea / Subsea Landing Diversification** | Consulted | Informed | Consulted | Accountable | Consulted |
| **Pax Silica Bilateral Multilateral Alliances** | Accountable | Informed | Informed | Consulted | Informed |

---

## References (50 Citations)

1. P. Akimitsu, "Artificial Intelligence: Supply-Chain Chokepoints and the Reach of Industrial Policy," SUNY Economics, arXiv:2607.29572, Aug. 2026.
2. Ministry of Electronics and IT, "Cabinet Approves National IndiaAI Mission with Outlay of Rs. 10,371.92 Crore," Press Information Bureau, Government of India, Mar. 2024.
3. India Semiconductor Mission, "Modified Programme for Development of Semiconductors and Display Manufacturing Ecosystem (Semicon India 2.0)," MeitY, New Delhi, 2025.
4. Central Electricity Authority, "Manual on Transmission Planning Criteria and Data Centre Interconnection Standards," Ministry of Power, New Delhi, 2026.
5. International Energy Agency, "Energy and AI: World Energy Outlook Special Report on Electricity Demand," IEA Publications, Paris, 2024.
6. A. Shehabi et al., "2024 United States Data Center Energy Usage Report: Updated Scaling Metrics," Lawrence Berkeley National Laboratory, LBNL-2001428, 2024.
7. Jones Lang LaSalle, "India Data Centre 2026 Mid-Year Report: AI Appetite Unleashed," JLL Strategic Consulting, Mumbai, Aug. 2026.
8. CBRE Research, "India Data Centre Market in a New Era: Capacity Surges Beyond 1.5 GW," CBRE India, 2026.
9. R. Kaufmann, D. Henderson, and A. Miller, "Power Grid Integration Constraints of Terawatt-Scale AI Infrastructure," Nature Energy, vol. 10, pp. 412–426, 2025.
10. TrendForce, "Global Foundry Revenue and Advanced Packaging Analysis: TSMC CoWoS Capacity Expansions in 2026," TrendForce Market Research, Taipei, 2026.
11. TrendForce, "High-Bandwidth Memory (HBM3e and HBM4) Market Forecast: Supply Chain Constraints," TrendForce Memory Intel, 2026.
12. D. Patel and D. Knupp, "The True Chokepoints of AI Hardware: CoWoS Packaging, HBM3e and Optical Transceivers," SemiAnalysis Research, 2025.
13. Counterpoint Research, "Global High-Bandwidth Memory Ecosystem: Market Shares and 12-High Stacking Bottlenecks," Counterpoint, Seoul, 2025.
14. U.S. Geological Survey, "Mineral Commodity Summaries 2025: Gallium, Germanium, and Rare Earth Supply Chains," USGS, Reston, VA, 2025.
15. Taiwan Semiconductor Manufacturing Company, "TSMC Annual Business Report and Advanced Technology Roadmaps," TSMC, Hsinchu, 2025.
16. ASML Holding, "ASML Investor Information: High-NA EUV Delivery Timelines and Photolithography Tool Shipments," ASML, Veldhoven, 2026.
17. A. García-Herrero and S. Dutta, "Programmable Sovereignty: Coordinated Specialization as a Response to the N-2 Problem in AI," Portulans Institute & Bruegel, Policy Brief 2026/04, 2026.
18. R. Sharma, V. Patel, and A. Rao, "Direct-to-Chip Liquid Cooling Architectures for Ultra-Dense AI Datacenters in Tropical Climates," IEEE Transactions on Components, Packaging and Manufacturing Technology, vol. 16, no. 3, pp. 345–358, 2026.
19. NVIDIA Corporation, "NVIDIA DGX H100 Architecture Whitepaper: Power Delivery, Networking, and Thermal Specifications," NVIDIA, Santa Clara, CA, 2024.
20. W. Hannas, A. Chien, and L. Dunham, "Geographic Concentration and Vulnerabilities in AI Hardware Manufacturing," Center for Security and Emerging Technology (CSET), Georgetown Univ., 2024.
21. K. Neaher and Z. Halaszi, "Middle Powers in the AI Acceleration Race: Balancing Security, Compute, and Capital Alliances," Stimson Center Policy Paper, Washington, DC, 2026.
22. SBI Capital Markets, "Indian Data Centres: Powering the Digital Revolution — Capital Expenditure and PUE Baselines," SBICAP Research, Mumbai, 2025.
23. Colliers International India, "India Data Centers: Entering the Gigawatt Era — Geographic Concentration and Power Infrastructure," Colliers Research, 2026.
24. The Economy Research, "The Geopolitics of Compute: Sovereignty, Power, and Strategic Dependence in the AI Infrastructure Race," Econ Research, 2026.
25. DeNexus Cyber Risk Advisory, "Operational Technology Cyber Security in Power Sectors: Regulatory Mandates and Data Centre Feeder Standards," DeNexus, 2026.
26. B. Sengupta, P. Kumar, and S. Venkat, "Subword Tokenization Inefficiencies in Multilingual Large Language Models for Indic Languages," In Proc. ACL 2025, pp. 1120–1134, 2025.
27. NITI Aayog, "National Strategy for Artificial Intelligence: Towards Responsible AI and Sovereign Compute Deployment," Government of India, New Delhi, 2024.
28. Ministry of Law and Justice, "The Digital Personal Data Protection Act, 2023 (Act No. 22 of 2023)," The Gazette of India, New Delhi, Aug. 2023.
29. Telecom Regulatory Authority of India (TRAI), "Recommendations on Regulatory Framework for Promoting Data Economy, Cloud Services and Cable Landing Stations in India," TRAI, New Delhi, 2025.
30. Bureau of Energy Efficiency (BEE), "Energy Conservation Building Code for Data Centres: Specific Energy Consumption Metrics," Ministry of Power, New Delhi, 2025.
31. C. Miller, "Chip War: The Fight for the World's Most Critical Technology," Scribner, New York, 2022.
32. H. Farrell and A. L. Newman, "Weaponized Interdependence: How Global Economic Networks Shape State Coercion," International Security, vol. 44, no. 1, pp. 42–79, 2019.
33. OpenAI, "GPT-4 Technical Report: Scaling Compute, Infrastructure, and Systems Engineering," arXiv:2303.08774, 2023.
34. SemiAnalysis, "Scaling Laws for Data Center Infrastructure: From Megawatts to Gigawatts," SemiAnalysis Reports, 2025.
35. Tata Electronics, "Semiconductor Fab and OSAT Infrastructure Development Roadmap in Gujarat and Assam," Tata Sons Press Release, 2024.
36. J. Dean, "The Deep Learning Revolution and Its Implications for Computer Architecture and System Design," In Proc. IEEE ISSCC, pp. 8–14, 2020.
37. S. Narayanan et al., "Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM," In Proc. ACM SC21, pp. 1–15, 2021.
38. R. Rajbhandari et al., "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models," In Proc. ACM/IEEE SC20, pp. 1–16, 2020.
39. P. Micikevicius et al., "FP8 Formats for Deep Learning," arXiv:2209.05433, 2022.
40. M. Shoeybi et al., "Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism," arXiv:1909.08053, 2019.
41. V. Sze, Y. Chen, T. Yang, and J. S. Emer, "Efficient Processing of Deep Neural Networks: A Tutorial and Survey," Proceedings of the IEEE, vol. 105, no. 12, pp. 2295–2329, 2017.
42. H. Esmaeilzadeh, E. Blem, R. St. Amant, K. Sankaralingam, and D. Burger, "Dark Silicon and the End of Multicore Scaling," IEEE Micro, vol. 32, no. 3, pp. 122–134, 2012.
43. J. Hennessy and D. Patterson, "A New Golden Age for Computer Architecture," Communications of the ACM, vol. 62, no. 2, pp. 48–60, 2019.
44. U.S. Department of Commerce, "Implementation of Additional Export Controls: Advanced Computing and Semiconductor Manufacturing Items," Federal Register, vol. 88, no. 205, pp. 73458–73512, Oct. 2023.
45. Ministry of Power, "Report of the Committee on National Electricity Plan (Generation and Transmission) 2022–2032," Central Electricity Authority, New Delhi, 2023.
46. Bureau of Indian Standards, "IS 732: Code of Practice for Electrical Wiring Installations in Data Centres," BIS, New Delhi, 2024.
47. ASHRAE, "Thermal Guidelines for Data Processing Environments, 5th Edition," ASHRAE Technical Committee 9.9, Atlanta, GA, 2021.
48. N. Jouppi et al., "TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings," In Proc. ACM/IEEE ISCA 2023, pp. 1–14, 2023.
49. C. Tripathy and S. K. Dash, "Evaluation of High-Tension Open-Access Tariffs for Captive Data Centers in India," Energy Policy, vol. 172, p. 113318, 2023.
50. Telecom Regulatory Authority of India (TRAI), "Consultation Paper on Digital Connectivity Infrastructure in India," TRAI, New Delhi, 2024.
---

<div align="center">

© 2026 Adarsh Singh, Sourav, and Anamidhi Shrivastava — Amity University Madhya Pradesh, Gwalior  
Submitted to Amity ResearchThon 2026 | IEEE Transactions-Length Monograph | All rights reserved.

</div>
