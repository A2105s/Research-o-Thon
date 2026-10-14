# Presentation Speaker Notes and Delivery Guide

**Project:** ResearchThon 2026 — Amity University Madhya Pradesh  
**Presentation:** *A Demand-Driven Framework for India's AI Infrastructure Planning*  
**Document:** `presentation/speaker_notes.md`  
**Target Duration:** 8 to 10 Minutes Total (~45 to 60 seconds per slide)  

---

### Slide 1: Title and Research Question (Time: 0:00 – 0:45)
> "Respected judges, faculty members, and fellow researchers. Today, my colleague and I present our research on *A Demand-Driven Framework for India's AI Infrastructure Planning: Linking Compute, Energy, Physical Resources, and Semiconductor Dependencies*.
>
> In contemporary policy discourse, artificial intelligence is often treated as an ethereal software race. However, AI model capability is fundamentally anchored in physical reality: electricity transmission lines, cooling water, silicon wafers, advanced packaging, and global supply chains.
>
> Our central research question is straightforward: *What are the end-to-end physical resource and microelectronic boundary conditions required to support large-scale sovereign AI compute in India, and where do the true structural bottlenecks reside?* Today, we demonstrate the answers using an auditable, reproducible mathematical model."

---

### Slide 2: The Physical Embodiment of AI Compute (Time: 0:45 – 1:30)
> "To understand the motivation for this work, we must examine the 'Borrowed Silicon' paradox. India currently houses the world's third-largest AI developer base and recognized model initiatives like Sarvam and BharatGen. Furthermore, the Union Cabinet has authorized ₹10,371.92 crore under the IndiaAI Mission to subsidize compute access.
>
> However, virtually every GPU powering these workloads is designed in the United States and manufactured in Taiwan under US export jurisdiction. 
>
> More critically, compute cannot simply be dropped into existing server rooms. An enterprise accelerator cluster demands continuous megawatt-scale power, dedicated high-voltage substations, and millions of litres of cooling water. If a nation procures 100,000 GPUs without co-planning its grid and cooling corridors, those chips will sit unpowered in warehouse crates behind multi-year transmission queues."

---

### Slide 3: Literature Review & The Research Gap (Time: 1:30 – 2:20)
> "When we audited existing literature across 84 foundational papers and institutional reports, we discovered a deep academic divide.
>
> On one side, geopolitical scholars like Akimitsu and CSET analyze TSMC's foundry dominance and semiconductor export controls, but they treat compute as an abstract commodity without modeling data centre thermodynamics or grid stress.
>
> On the other side, mechanical and electrical engineering scholars at LBNL and the IEA model server power and cooling PUE, but they evaluate facilities in isolation without connecting to upstream microelectronics or national deployment targets.
>
> Our work bridges this divide. We provide the first reproducible, unified framework that connects high-level national GPU procurement targets directly to macro-grid capacity, water stress, and upstream semiconductor supply lines."

---

### Slide 4: The Five-Pillar Conceptual Framework (Time: 2:20 – 3:15)
> "As illustrated in Figure 1, we conceptualize AI infrastructure sovereignty not as a standalone GPU count, but as a closed-loop system of five interdependent pillars:
>
> - **Pillar I:** Compute Stock and High-Speed Interconnect Fabrics.
> - **Pillar II:** Energy Generation, Grid Interconnection, and Transmission Substations.
> - **Pillar III:** Physical Resources, Tropical PUE Cooling Overheads, and Spatial Location.
> - **Pillar IV:** Semiconductor Supply Chains, spanning Logic Wafers, 2.5D CoWoS Packaging, and High-Bandwidth Memory.
> - **Pillar V:** Human Capital and Strategic Governance, encompassing India's 120,000 VLSI chip design engineers and public procurement policy.
>
> Unlike superficial vulnerability indices that assign arbitrary decimal scores, our framework models the physical and institutional dependencies transmitting failure across these pillars."

---

### Slide 5: The Six-Layer Demand-Cascade Model (Time: 3:15 – 4:10)
> "To make this framework operationally rigorous, we developed a six-layer mathematical demand cascade. 
>
> Given an exogenous accelerator deployment target $N$—we evaluate 200,000, 500,000, and 1,000,000 GPUs—the model deterministically calculates:
> - Layer 1: IT Electrical Load in megawatts, incorporating server host chassis overheads ($R_{\text{host}} = 1.82$).
> - Layer 2: Facility Peak Power using empirical PUE baselines, and annual electrical energy at 80% utilization.
> - Layer 3: Evaporative cooling water withdrawal in megalitres and physical rack footprints.
> - Layer 4: Semiconductor wafer starts using the Murphy defect yield model on 300 mm wafers.
> - Layer 5: 2.5D CoWoS advanced packaging interposer wafers.
> - Layer 6: High-Bandwidth Memory HBM3e stack allocations.
>
> Every equation is mathematically verified. Our codebase includes 51 automated unit tests that enforce conservation laws, verify linearity, and prevent rounding errors."

---

### Slide 6: Cross-National Benchmarking (Time: 4:10 – 5:00)
> "Before running the model, we established an empirical baseline comparing India, the United States, and China across strictly comparable metrics.
>
> In operational commercial colocation data centre capacity, India stands at 1,575 MW, compared to 8,200 MW in China and 12,500 MW in the US.
>
> In semiconductor manufacturing, India currently possesses 0% domestic sub-5nm logic fabrication, 0% commercial 2.5D CoWoS advanced packaging, and 0% HBM memory production. 
>
> However, India possesses a tremendous asymmetric strength: over 20% of the world's leading chip design talent resides in Indian engineering centres. The challenge is that this talent currently designs proprietary IP for foreign fabless multinationals rather than sovereign architectures."

---

### Slide 7: Quantitative Scenario Results (Time: 5:00 – 6:00)
> "Now let us examine the core model results, focusing on our baseline scenario of 500,000 GPUs—the scale required for serious national AI independence.
>
> Operating 500,000 GPUs requires **637.0 MW of IT load**. Under Indian tropical conditions at a base PUE of 1.40, this demands **891.8 MW of continuous peak grid interconnect**.
>
> Let that number sink in: **891.8 MW is equivalent to 56.62% of India's entire currently operational commercial colocation data centre footprint.**
>
> Annually, this cluster consumes **6.25 TWh of electricity** and **11.25 billion litres of cooling water** under conventional wet cooling. On the semiconductor side, it requires **12,500 logic wafer starts**, **33,334 CoWoS packaging wafers**, and **3,000,000 HBM3e stacks**."

---

### Slide 8: Refuting the Wafer Hypothesis & True Chokepoints (Time: 6:00 – 7:00)
> "This brings us to the central scientific discovery of our research: **the empirical refutation of the 'Silicon Fab' hypothesis.**
>
> Popular commentary frequently assumes that the primary physical barrier to AI sovereignty is the inability to manufacture leading-edge silicon wafers domestically. But when we compare our model output against TSMC's actual production telemetry, the data refutes this claim:
>
> TSMC produces over 720,000 sub-5nm wafers annually. India's 500,000-GPU requirement consumes **merely 1.74% of annual global sub-5nm wafer output**. Front-end lithography capacity is not the binding bottleneck.
>
> Where do the real bottlenecks reside?
> 1. **2.5D CoWoS Advanced Packaging:** 33,334 interposer wafers consume **7.41% of total worldwide packaging capacity**, where lead times exceed a year.
> 2. **HBM3e Memory:** 3 million stacks consume **6.67% of global production**, controlled by a Korean duopoly.
> 3. **Domestic Power Grids:** 891.8 MW requires 18 dedicated 50 MW substations in an ecosystem where Mumbai—housing 52.4% of current data centres—already faces 24-month interconnection backlogs."

---

### Slide 9: Strategic Roadmap & The Priority Inversion (Time: 7:00 – 8:00)
> "Because the physical bottlenecks reside in packaging and power rather than raw lithography, our framework directs an **immediate inversion of national planning priorities**:
>
> The conventional doctrine advocates spending $15 to $20 billion on a domestic sub-5nm logic fab. But our model proves that a 500k cluster cannot absorb a gigafab's minimum economic scale, and domestic 3nm dies produce zero usable GPUs without packaging and power.
>
> Instead, our framework dictates a **Transmission-and-Packaging-First** roadmap:
> - **Phase 1 (Build Now, 2026–2028):** Establish 400/220 kV Green AI Transmission Corridors; institute spatial subsidies to diversify away from Mumbai into Gujarat, Rajasthan, and Odisha; and mandate Direct Liquid Cooling ($\text{PUE} \le 1.25$) to eliminate water loss.
> - **Phase 2 (Build through Partnership, 2028–2031):** Upgrade domestic ATMP plants (Tata, Micron) into 2.5D packaging joint ventures with Taiwan and Japan, and mobilize GCC talent to tape out sovereign RISC-V chiplets.
> - **Phase 3 (Depend & Ally, 2031–2035):** Deploy 1.8 GW of captive clean microgrids and secure bilateral wafer reservation treaties."

---

### Slide 10: Conclusion and Summary (Time: 8:00 – 8:45)
> "In conclusion:
> 1. AI infrastructure sovereignty is a multi-dimensional physical engineering challenge governed by transmission lines, cooling physics, and advanced packaging.
> 2. Our Demand-Cascade Model provides an open, auditable, and reproducible planning tool for national decision-makers.
> 3. True strategic sovereignty is achieved not through capital-ruinous autarky, but through **coordinated specialization, grid debottlenecking, and advanced packaging alliances**.
>
> Our manuscript has been fully verified, passes all 51 test suites, and adheres strictly to the 6-page IEEE format. We welcome your questions. Thank you."
