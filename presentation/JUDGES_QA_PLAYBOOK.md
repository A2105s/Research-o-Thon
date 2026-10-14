# Judges' Q&A Playbook
## Sovereign by Design: A Five-Pillar Framework for India's Strategic Compute and AI Infrastructure

Companion to `PPT_IEEE_PARAKRAM.html` and `PAPER_EXPLAINED_AND_PPT_GUIDE.md`.
The Q&A slot is 5 minutes, so most answers must fit in 20 to 30 seconds. Every answer below has a **Say** line (what you speak first) and, where useful, an **If pushed** line (the deeper layer) and a **Check** line (the arithmetic or source you can point to).

---

## 0. How to answer (read this twice)

1. **Answer first, then evidence, then limit.** "No, because X. The number is Y. The caveat is Z."
2. **Concede small points fast.** If a judge finds a real weakness, say "That is a fair limitation, and here is what it changes." This is scored better than defending a weak point.
3. **Never say "will".** Say "if India deployed 500,000 H100-class GPUs, the model gives 891.8 MW". It is a scenario, not a forecast.
4. **Say "estimate" for every global capacity figure** (780,000 wafers, 450,000 CoWoS wafers, 60 million HBM stacks, 1,575 MW).
5. **Know who owns which section** (split roles) and hand over: "My teammate built that part, I will let them answer."
6. **If you do not know:** "We did not model that. Here is what we would expect and how we would test it." Never invent a number.
7. **Tag for this document:** items marked **[verify]** are outside facts from general knowledge. Check them against a current source before the event; do not quote them as exact.

---

## 1. Numbers you must be able to say without looking

| Item | Value |
|---|---|
| Baseline | 500,000 H100-class GPUs (also 200,000 and 1,000,000) |
| GPU power, server ratio | 700 W, 1.82 (DGX H100: 10.2 kW / 5.6 kW) |
| IT load | 637.0 MW |
| PUE, facility peak | 1.40, 891.8 MW |
| Annual energy, CO2 | 6.25 TWh, 4.47 Mt (0.716 t/MWh) |
| Cooling water (evaporative) | 11,249.5 ML (1.80 L/kWh) |
| Racks | 10,617 at 60 kW |
| India colocation capacity | 1,575 MW (mid-2026), so 56.62% |
| 2030 pipeline | 3,200 MW, so 27.87% |
| Dies per wafer, good dies | 63, 40 |
| Wafer starts, share of TSMC | 12,500, 1.60% of ~780,000 |
| CoWoS wafers, share | 33,334, 7.41% of ~450,000 |
| HBM stacks, share | 3.0 million, 5.00% of ~60 million |
| Packaging vs wafer pressure | 7.41 / 1.60 = 4.6 times |
| D2C cooling | minus 94.6% water, minus 172 MW, PUE 1.18 |
| Mumbai share of capacity | 52.4% |
| 1M GPUs | 113.24% of today's colocation capacity |
| 1M GPUs, high case | 3,255 MW, 2.07 times present capacity |
| Investment (proposal) | Rs 95,500 crore public + Rs 2,57,000 crore PPP |

---

## 2. Opening argument: why AI, and why the nuclear / aviation / space comparison

**Q1. Why compare AI to nuclear weapons, fighter jets and space? Is that not exaggerated?**
Say: "We compare the strategic pattern, not the weapon. In each case a handful of countries mastered the technology early, wrote the rules, and became powers. Everyone else became a buyer on someone else's terms. AI has the same structure: whoever controls compute controls what can be built."
If pushed: "The analogy is about dependence and bargaining power. We are not proposing an arms race. AI is dual-use and mostly commercial, which makes the dependence broader, not smaller."

**Q2. In what way is AI different from nuclear technology?**
Say: "Three ways. AI is diffuse and mostly commercial, there is no treaty regime like the NPT, and it can be rented from abroad. That last point is exactly why sovereignty is hard: you can buy access, but access can be priced, throttled or cut."
Check: the five original nuclear-weapon states are also the five permanent members of the UN Security Council. This is the cleanest 'powers' example.

**Q3. India is already a nuclear and space power. Why does AI need separate attention?**
Say: "Nuclear and space were state programmes with limited physical footprints. AI needs national-scale electricity, cooling water and a global chip supply chain. The risk is that India has the algorithms and talent but not the physical base."

**Q4. You say India built nuclear and space capability 'against restrictions'. Evidence?**
Say: "India's 1974 and 1998 nuclear tests were followed by technology denial and sanctions, and India developed launch vehicles and satellites largely indigenously. The Aryabhata satellite in 1975 was built in India but launched on a Soviet rocket; India's own launch vehicle, SLV-3, flew in 1980. We say that openly."
Check [verify]: sanctions after 1998 and the technology-denial regimes of that period.

**Q5. Why mention fighters and engines? Is India behind there?**
Say: "Because engines are the clearest example of a hidden chokepoint. Few countries can build a modern fighter engine. India's own Kaveri engine programme has run for decades and India still imports engines for its fighters. It shows what it costs to depend on a component you cannot make."
If pushed [verify]: the indigenous 5th-generation programme (AMCA) is in development and no indigenous 5th-generation fighter is in service. We say 'closing the gap', not 'ahead'.

**Q6. What do '5th generation' and '6th generation' mean on your slide?**
Say: "5th-generation fighters combine stealth, sensor fusion and networking, in service from 2005 with the F-22. 6th-generation fighters are programmes in development in the 2030s (US, UK-Japan-Italy, France-Germany-Spain programmes) [verify current status]. We use them as the aviation examples of a technology that only a few countries master."

**Q7. Why is the timeline drawn to scale?**
Say: "So the real spacing is visible. Jet fighters, nuclear weapons and the space age arrived within 13 years of each other (1944 to 1957), stealth fighters in 2005, and generative AI in 2022. Waves keep arriving, and each one rewarded the countries that were early. India's own record sits on the lower line: nuclear and space milestones in the 1970s to 2020s."

**Q8. Does 'be ahead or equal in AI' mean India must build every layer?**
Say: "No. Our definition of sovereign is to control what India can control (power, cooling, location, packaging partnerships) and to manage the dependencies it cannot (foundry, memory, export rules). Equal does not mean self-sufficient."

---

## 3. Problem, gap and novelty

**Q9. What is the research gap, in one sentence?**
Say: "Studies cover semiconductors, power grids or policy separately; none of the ones we reviewed starts from a GPU target and follows it through power, cooling, silicon, packaging and memory in one reproducible model."

**Q10. Is it really the first such model? Did you search enough?**
Say: "We do not claim first in the world. We say none of the studies we reviewed combines all of those layers. Our closest comparisons are IEA/LBNL (power and cooling, no chip supply) and Akimitsu 2026 (chip dependency graph, no power or GPU scenarios)."

**Q11. What is new compared with IEA, LBNL or Akimitsu?**
Say: "They each solve half. We connect both halves and add a demand-driven scenario so the output is a bill of physical requirements for a stated GPU target."

**Q12. What are the five gaps RG-01 to RG-05?**
Say: "Siloing, no cascade from GPU target to physical need, the silicon-wafer fallacy, under-estimated tropical cooling, and the operationalisation deficit: frameworks that never become numbers."

**Q13. What is the 'silicon wafer fallacy'?**
Say: "The belief that front-end wafer fabrication is India's binding physical bottleneck for AI compute. For 500,000 GPUs it is 1.60% of TSMC's yearly sub-5 nm output."

**Q14. Why 500,000 GPUs? Who said India will buy that many?**
Say: "Nobody. It is an illustrative planning scenario, 11 to 15 times today's shared pool (34,000 to 45,000 GPUs). We also run 200,000 and 1,000,000. Everything scales linearly, so any target can be read off."

---

## 4. Framework (five pillars, four loops)

**Q15. Why five pillars? Is that arbitrary?**
Say: "They come from the dependency chain: compute, energy, physical resources, connectivity and security, and governance with capital and talent. It is a conceptual framework, not empirically validated. The validated part is the Demand-Cascade Model."
If pushed: future work is expert validation (for example a Delphi round).

**Q16. How were the four feedback loops identified?**
Say: "From the literature and policy documents, as structural couplings. They are conceptual, not estimated. Loop A, the power-compute deadlock, is the clearest: you cannot get power without proof of use, and you cannot install GPUs without power."

**Q17. Where is the model in the framework?**
Say: "The pillars are the map. The Demand-Cascade Model is the calculator that quantifies pillars 1 to 3 (compute, energy, physical resources). Pillars 4 and 5 are treated qualitatively and through the roadmap."

**Q18. Why is cybersecurity or data localisation not in the numbers?**
Say: "Because they change cost and risk, not the physical requirements the model computes. They are in Pillar 4 and Loop C."

---

## 5. The model, layer by layer

**Q19. Walk me through the model in 20 seconds.**
Say: "Start with N GPUs. Layer 1: N times 700 W times 1.82 gives 637 MW of IT load. Layer 2: times PUE 1.40 gives 891.8 MW, and 6.25 TWh a year. Layer 3: water from the energy, and racks from the load. Layers 4 to 6: wafers, CoWoS packaging and HBM from N directly."

**Q20. Why is it called 'deterministic'?**
Say: "Same inputs always give the same outputs, so anyone can re-run it. The only randomness is the Monte Carlo, which uses a fixed seed (42)."

**Q21. Where does 1.82 come from?**
Say: "An NVIDIA DGX H100 draws about 10.2 kW for 8 GPUs of 700 W, which is 5.6 kW of GPU power. 10.2 / 5.6 = 1.82. It captures CPUs, networking, fans and power conversion."

**Q22. 700 W is the maximum rating. Real draw is lower.**
Say: "Correct, and we say 'peak'. The facility peak figure is a provisioning number, which is what substations must be sized for. Annual energy applies a separate utilisation factor of 0.80."

**Q23. Why PUE 1.40 when India's average is 1.55?**
Say: "1.55 reflects older sites. 1.40 is a modern new-build value. We show 1.25 and 1.55 as low and high, and the sensitivity chart shows plus or minus 10.7% on power."
Check: at PUE 1.55 the facility draw is 987.4 MW (62.7% of 1,575 MW). At 1.25 it is 796.3 MW (50.6%).

**Q24. Why 80% utilisation?**
Say: "A planning value for an average training and inference fleet. It only affects energy, water and CO2, not the peak MW. Range tested: 0.65 to 0.90."
Check: at 0.90, energy is 7.03 TWh; at 0.65 it is 5.07 TWh.

**Q25. Is the 8,760 factor right?**
Say: "Hours in a year. Energy = facility MW x 8,760 x utilisation / 1,000,000 gives TWh. 891.8 x 8,760 x 0.80 / 10^6 = 6.25."

**Q26. How is the CO2 figure computed?**
Say: "6.25 TWh x 0.716 t per MWh (the CEA grid average) = 4.47 Mt a year. It uses today's grid mix, so it falls if supply is cleaner."

**Q27. How do you get the water number?**
Say: "Annual energy times a water intensity of 1.80 L per kWh from the IEA for evaporative cooling: 6.25 x 10^9 kWh x 1.80 = 11.25 billion litres, or 11,249.5 ML."
If pushed: the range is 0.20 (closed-loop or dry) to 2.50 L/kWh. At 0.20 it is 1,250 ML; at 2.50 it is 15,624 ML.

**Q28. Is evaporative cooling actually common in Indian data centres?**
Say: "Many large sites use chillers or air-side cooling with some evaporative assist. We use 1.80 as the evaporative baseline to show the penalty in hot, water-stressed regions, and we show the alternatives in the cooling table."

**Q29. How many dies fit on a wafer?**
Say: "The standard gross-die formula for a 300 mm wafer and an 814 mm2 die: pi r2 / A minus 2 pi r / sqrt(2A) = 86.84 - 23.36 = 63.5, so 63."

**Q30. Explain the Murphy yield model.**
Say: "It assumes defects land randomly, so a bigger die has a higher chance of being hit. With D0 = 0.08 per cm2 and an 8.14 cm2 die, D0 x A = 0.651. Yield = ((1 - e^-0.651) / 0.651)^2 = 0.540."

**Q31. Why multiply the yield by 1.2? Is that double counting?**
Say: "No. It represents binning: dies with a few defective sections are sold as slightly lower-spec parts, so the usable fraction is higher than the strict defect-free yield. It is capped at 0.85. 0.540 x 1.2 = 0.648. Without binning the wafer count rises by 20%, which would take the TSMC share from 1.60% to about 1.9%, and the conclusion is unchanged."

**Q32. Why round down to 40 good dies?**
Say: "63 x 0.648 = 40.8, and you cannot use a fraction of a die, so we round down. It is the conservative direction (more wafers)."

**Q33. Why is the number of good dies per wafer so low?**
Say: "The H100 die is very large, 814 mm2, so few fit on a wafer and the yield is hurt. That is also why wafer demand is not trivial, but it is still small against TSMC's output."

**Q34. How do you get the CoWoS number?**
Say: "Each GPU needs one silicon interposer. We assume 15 packages per 300 mm interposer wafer: 500,000 / 15 = 33,334 wafers, which is 7.41% of ~450,000 global CoWoS wafers a year."

**Q35. Is 15 packages per wafer accurate?**
Say: "It is an industry-estimate assumption, listed in the parameter register, and it is the single most debatable packaging input. We vary it from 12 to 18."
If pushed: "The conclusion does not depend on it. For CoWoS pressure to fall below the 1.60% wafer pressure, you would need about 69 packages per interposer wafer (500,000 / (0.016 x 450,000) = 69.4). A 300 mm wafer has 70,686 mm2 of area, and an interposer is several times the die area, so that is physically impossible."

**Q36. How do you get HBM?**
Say: "Stacks = N x stacks per GPU. 500,000 x 6 = 3.0 million, against ~60 million per year globally, which is 5.00%."

**Q37. An H100 has five active HBM stacks, not six.**
Say: "That is a good catch [verify against the datasheet]. The H100 SXM carries five active HBM3 stacks on a six-site package, while the H200 carries six HBM3e stacks. We use 6 as an H100/H200-class value (register item PAR-011) and 8 for B200-class in the high case. With 5 stacks the share is 4.17%; with 8 it is 6.67%. All are above the 1.60% wafer share."
Check: 2.5M / 60M = 4.17%; 4.0M / 60M = 6.67%.

**Q38. Why does every layer scale linearly? Real systems do not.**
Say: "Because each requirement is per GPU. That is by design for a first-order planning model. Non-linearity enters through infrastructure lumpiness (substations, grid queues), which we address in the policy sections, not the arithmetic."

**Q39. How do you handle rounding?**
Say: "Wafer counts and rack counts are rounded up, good dies per wafer are rounded down, so every rounding goes in the conservative direction."

**Q40. What is the grid-frequency equation doing in the paper?**
Say: "It is motivation, not one of the six layers. It shows why a sudden AI load swing matters: a 250 MW step on a 50 GW grid with 4.2 s inertia gives df/dt of about minus 0.03 Hz per second, so without response the frequency would reach the lower limit in a few seconds. That is why fast storage is recommended."
Check: 50 x (250 / 50,000) / (2 x 4.2) = 0.0298 Hz/s. The 'few seconds' illustration (about 3.4 s from 50.00 to 49.90 Hz) is our own arithmetic, not a cited result.

---

## 6. Parameters and data sources

**Q41. Where do the denominators (780k, 450k, 60M, 1,575 MW) come from?**
Say: "Industry reports and census data (for example TrendForce, TSMC reports, and JLL/CBRE-type data-centre census figures), logged in our denominator audit. They are estimates and they move every year."
Prep: open the PDFs in `sources/` once yourself so you can name the exact document for each.

**Q42. What if the denominators are wrong by 20% or 2x?**
Say: "The percentages scale proportionally, but the order does not change. The CoWoS-to-wafer pressure ratio is 4.6 times. To flip the ordering, CoWoS capacity would need to be about 4.6 times larger relative to wafer capacity than we assume."

**Q43. Why compare against TSMC only?**
Say: "Over 90% of leading-edge logic is made in Taiwan. We state it as a limitation: Samsung and Intel add capacity. Including them would lower the wafer share further, which strengthens, not weakens, our conclusion."

**Q44. Why is the colocation figure the right denominator?**
Say: "It is the best-measured operational capacity (a census), so the comparison can be verified. It excludes captive or hyperscaler-owned capacity, which would enlarge the denominator and lower the percentage. The absolute 891.8 MW does not change. We state it as a scale comparison."

**Q45. Why use H100 and not newer GPUs?**
Say: "H100 has public datasheet values for power and die size, so every input is traceable. Blackwell-class values enter in the high case (1,000 W, 8 HBM stacks)."

**Q46. Why is the baseline the same across the three scenarios?**
Say: "To isolate scale. Only N changes between the columns."

**Q47. What are the 'Low' and 'High' cases?**
Say: "Low is optimistic, High is pessimistic, on all eight parameters together: for example PUE 1.25 / 1.55, GPU power 700 / 1,000 W, server ratio 1.60 / 2.10, water 0.20 / 2.50 L/kWh."
Check: 500,000 GPUs, High: 500,000 x 1,000 x 2.10 = 1,050 MW IT x 1.55 = 1,627.5 MW, which is 103% of 1,575 MW. Low: 560 MW x 1.25 = 700 MW, which is 44.4%.

**Q48. Where is the parameter register?**
Say: "`model/parameter_register.csv`: each parameter has a low, base and high value, a unit and a source."

---

## 7. Results: the power wall

**Q49. Is 56.62% realistic? Nobody builds that in one go.**
Say: "Correct. It is a scale comparison: one programme is equivalent to more than half of today's whole colocation industry, which is why it needs planning years ahead. Against the 3,200 MW pipeline to 2030 it is 27.87%."

**Q50. India's total electricity is huge. Is 6.25 TWh not trivial?**
Say: "Nationally it is small, roughly 0.3 to 0.4% of generation [verify: India generates roughly 1,800 to 2,000 TWh a year]. The constraint is local and instantaneous: 891.8 MW delivered to a few grid nodes, with 36 to 48 month equipment lead times. Energy in TWh is not the bottleneck; megawatts at specific substations are."

**Q51. Why does Mumbai matter?**
Say: "52.4% of capacity (about 825 MW) sits there because of cable landings and the financial hub. Adding 891.8 MW there would roughly double the city's data-centre load. The roadmap targets a Mumbai share below 35% by 2028."
Check: 0.524 x 1,575 = 825 MW.

**Q52. How many substations?**
Say: "About 18 of 50 MW each: 891.8 / 50 = 17.8."

**Q53. Could the load be shifted or flexible?**
Say: "Partly. Training loads can be time-shifted, and storage can smooth swings, but the connection must still be sized for peak. That is why the grid-connection process, not the energy total, is the bottleneck."

**Q54. Why not just use solar or captive power?**
Say: "The model counts demand, not supply. Round-the-clock renewables are in Tier 2 of the roadmap. A 24x7 AI load needs firm power or storage, which is why we also list nuclear baseload and batteries."

**Q55. Is nuclear or small modular reactors (SMR) realistic by 2031?**
Say: "We treat it as a longer-horizon option, not a base assumption, and the investment line is an envelope. India has announced a nuclear mission for small reactors [verify details], but commercial deployment timelines are uncertain."

---

## 8. Results: the chokepoint inversion (semiconductors)

**Q56. Are you saying India should not build fabs?**
Say: "No. We say the wafer volume for this programme is only 1.60% of TSMC's yearly output, so a leading-edge fab built only for that volume is poor value. Fabs can matter for other strategic, economic and defence reasons."

**Q57. India has the Tata fab and Micron plant. Do you ignore Semicon India?**
Say: "No. The packaging side (OSAT/ATMP) and design talent are where Semicon India fits our result: packaging, not wafers, is where India can add value. Tier 2 of the roadmap is packaging joint ventures. [verify project status before quoting]."

**Q58. What exactly is CoWoS?**
Say: "Chip-on-Wafer-on-Substrate, TSMC's advanced packaging that mounts the GPU and its memory side by side on a silicon interposer. Without it, the GPU and the HBM cannot work together."

**Q59. What is HHI?**
Say: "Herfindahl-Hirschman Index: the sum of squared market shares. 10,000 is a monopoly. CoWoS is 90 squared = 8,100; HBM is 57 squared + 38 squared + 5 squared = 4,718. Above 2,500 is highly concentrated."

**Q60. Why does the 'inversion' matter for policy?**
Say: "Because money follows the famous problem. If the real constraints are packaging, memory and power, then billions spent on a leading-edge fab for this purpose would leave the binding constraints untouched."

**Q61. HBM share 5% looks small. Why call it a chokepoint?**
Say: "Share of demand is one measure. Concentration is the other: three suppliers, zero in India, and Loop B means one export rule can cut packaging and memory together. Also 5% is 3.1 times the wafer share."

**Q62. What if TSMC expands CoWoS several times over?**
Say: "Then the packaging pressure falls, and we say so: a several-fold capacity expansion or guaranteed allocation would reduce it. Our conclusion is about today's structure and is stress-tested over a wide parameter range."

**Q63. What if wafer yields collapse?**
Say: "Even at the high defect density of 0.12 per cm2, wafer starts rise by 33.3% to about 16,667, which is 2.14% of TSMC output; still below packaging at 7.41%."

**Q64. Does the model include export controls?**
Say: "No. Export rules (US EAR, iCET) are a limitation and outside the numerical model. They are the reason Loop B and Tier 3 (reservations, contingency playbook) exist."

**Q65. Why is lithography (ASML) in the table with no demand number?**
Say: "It is an upstream monopoly (HHI 10,000). Its demand depends on fab build-out rather than GPU count, so we show it for context and mark it 'upstream'."

---

## 9. Results: cooling and water

**Q66. Where does '94.6% less water' come from?**
Say: "Direct-to-chip (D2C) uses 632.1 ML against 11,651.3 ML for evaporative air cooling: 632.1 / 11,651.3 = 5.4%, so a 94.6% cut."

**Q67. And 172 MW?**
Say: "PUE falls from 1.45 to 1.18, a difference of 0.27 on a 637 MW IT load: 637 x 0.27 = 172 MW less facility load."

**Q68. Why not recommend immersion cooling?**
Say: "It is better on paper (PUE 1.12, 150 ML), but harder to deploy at scale, with a less mature supply chain. D2C is the practical balance."

**Q69. What does '236,000 residents' mean?**
Say: "11,651 ML a year divided by an assumed 135 litres per person per day is about 236,000 people's domestic water. The 135 L figure is an illustrative assumption, not a measured value for any city."

**Q70. Why make cooling the 'biggest lever'?**
Say: "In the sensitivity analysis cooling water use swings the output from minus 88.9% to plus 38.9%, larger than any other single input. For power itself, the biggest lever is the GPU's own wattage, plus 42.9% at 1,000 W."

---

## 10. Sensitivity and Monte Carlo

**Q71. What does the tornado chart show?**
Say: "We move one input at a time from its low to its high bound with all others at base, and show the percentage change in the affected output. Do not compare bars of different colours as if they were the same quantity."

**Q72. What does the Monte Carlo add?**
Say: "It varies seven inputs together, 1,000 random draws with seed 42. In the middle 80% of outcomes wafers stay at 1.4 to 1.9% of TSMC, CoWoS at 6.9 to 7.9% of global, and facility power at 51 to 71% of colocation capacity. The ordering never flips."

**Q73. Why is the Monte Carlo median power (963 MW) higher than the base (891.8 MW)?**
Say: "Because the random GPU power range is 650 to 850 W, which averages 750 W, above the 700 W base."

**Q74. Which distributions did you use?**
Say: "Bounded ranges from the parameter register, sampled independently. We state that correlations (for example hotter climate leading to higher PUE and water) are not modelled."
Honest note: confirm in `model/demand_cascade.py` whether sampling is uniform or triangular before you answer in detail.

**Q75. Are 1,000 draws enough?**
Say: "For percentile estimates at P10 and P90 to the precision we report, yes. The conclusion is an ordering that holds across the whole range, not a fine estimate."

---

## 11. Policy, roadmap and investment

**Q76. Why three tiers?**
Say: "Order of control: first do what India controls (power, cooling, location), then build with partners (packaging), then manage what it cannot control (foundry, memory, export rules)."

**Q77. Are the rupee figures official?**
Say: "No. They are our proposed planning envelopes: Rs 95,500 crore public plus Rs 2,57,000 crore PPP, about Rs 3.5 lakh crore over 2026 to 2035. They are not bottom-up costings."

**Q78. Does Rs 1 lakh crore for GPU clusters cover 500,000 GPUs?**
Say: "As an order of magnitude, yes for the accelerators. Rs 1 lakh crore is about USD 12 billion, or roughly USD 24,000 per GPU, against a market price for H100-class cards of the order of USD 25,000 to 30,000 [verify]. Facilities, power and cooling sit on other lines, and the paper does not claim a full cost model."
Check: 1,00,000 crore = Rs 1 trillion; at about Rs 83 per USD that is about USD 12 billion.

**Q79. Why cap Mumbai at 35%?**
Say: "It is a policy target to reduce single-city risk (52.4% today). The 15 to 20% capital rebate is a proposed lever for relocation. The number is a proposal to be tuned, not an estimate."

**Q80. What is the IndiaAI subsidy comparison?**
Say: "Rs 65 per GPU-hour is about USD 0.78, against USD 2.00 to 2.80 on the market, which is a 61 to 72% subsidy. We use it to show the policy is already price-subsidising compute while the physical base is unbudgeted."
Check: 1 - 0.78/2.00 = 61%; 1 - 0.78/2.80 = 72%.

**Q81. Why condition subsidies on PUE of 1.25 or lower?**
Say: "It uses public money to pull the market toward efficient, low-water designs. At PUE 1.25 instead of 1.40, the baseline falls from 891.8 MW to about 796 MW."

**Q82. Is the 9-month approval window feasible?**
Say: "It is a proposal. The reference is the 36 to 48 month equipment lead time for high-voltage gear; the approval window addresses the part that is purely administrative."

**Q83. Why gallium?**
Say: "It is a critical mineral for power and RF semiconductors with concentrated supply. Extraction from bauxite residue (red mud) is an aspirational idea in the roadmap (50 tonnes a year), not a claim of current capacity."

**Q84. What should India do first, with the least regret?**
Say: "Power connection process and location diversification, plus direct-to-chip cooling as a condition. They are cheap relative to fabs, fast to implement and useful regardless of which scenario happens."

---

## 12. Validity, limitations and methodology

**Q85. How do you validate the model?**
Say: "Three ways. Inputs trace to datasheets and cited sources. The arithmetic is unit-tested (10 of 10 tests pass) and outputs reproduce with one command. And sensitivity and Monte Carlo show the conclusion does not hinge on any single input. We have not validated against a measured national deployment, because none exists at this scale."

**Q86. What are your biggest limitations?**
Say: "(1) Fixed 80% utilisation. (2) Typical, not proprietary, defect density. (3) Export controls are outside the model. (4) Capacity denominators are market estimates. (5) The model counts GPUs, not performance, so more efficient chips mean fewer GPUs for the same work. (6) The baseline uses H100-class numbers."

**Q87. If chips get more efficient, does your conclusion collapse?**
Say: "It shifts the numbers, not the structure. Efficiency gains often increase total demand (the rebound effect), and the new chips are larger and use more packaging and memory, which strengthens the packaging and HBM points."

**Q88. Your model has no cost or economics.**
Say: "Correct, deliberately. We estimate physical requirements and give an investment envelope. A full techno-economic model is future work."

**Q89. No GDP, jobs or startup impact?**
Say: "Correct. We avoided unsupported macro forecasts. The paper makes only physical and cost-envelope claims."

**Q90. What would change your conclusion?**
Say: "Several-fold more CoWoS capacity or guaranteed allocation for India (lower packaging pressure), a much cheaper power-connection process, or a step change in chip efficiency."

**Q91. What is the next step?**
Say: "Couple the model to a power-flow (ACOPF) simulation of specific state grids using public telemetry, add performance-per-watt trends, and test other Global South countries."

---

## 13. Integrity, reproducibility and AI tools

**Q92. How can we reproduce your results?**
Say: "`pip install -r model/requirements.txt`, then `python model/demand_cascade.py`; tests with `python model/tests/test_demand_cascade.py`. The Monte Carlo seed is 42. Figures are generated from the same code."

**Q93. Did you use AI tools?**
Say the truth that matches your team's actual practice. A safe pattern: "We used AI tools as assistants for drafting and checking, and we verified every number, data choice and equation ourselves; we take full responsibility for the content." Do not deny use if it happened.

**Q94. Which parts did each of you do?**
Prepare your own one-line answer per person before the event; judges often ask this.

**Q95. How were the 500 source files handled?**
Say: "They were hashed (SHA-256) in a manifest and checked for duplicates. Only curated primary sources feed the evidence register."

---

## 14. Curveballs and hostile questions

**Q96. 'This is just a spreadsheet.'**
Say: "A transparent spreadsheet-level model is the point: every equation is a few lines, every input is sourced, and a policymaker can check it. The contribution is connecting layers that other studies keep apart, and the finding that follows."

**Q97. 'Why should India not simply rent GPUs from abroad?'**
Say: "Renting is part of the answer today. But access can be repriced or restricted, and data-sovereignty, latency and security rules push sensitive workloads onto domestic compute. Our model says what it takes to host that compute at home."

**Q98. 'Is 56.62% not misleading since hyperscalers are excluded?'**
Say: "That is why we call it a scale comparison to the colocation census. The absolute number, 891.8 MW, is unaffected, and so is the point that it needs dozens of new substations."

**Q99. 'Your wafer share is small because you assumed a huge TSMC capacity.'**
Say: "Suppose TSMC's capacity were half our estimate. The wafer share would double to 3.2%, but CoWoS and HBM are separate denominators and stay at 7.41% and 5.00%. The ordering only flips if the packaging capacity is about 4.6 times larger relative to wafer capacity than we assume, and a 2x error does not do that."

**Q100. 'You have no India-specific data on defect rates.'**
Say: "Correct and unavoidable: defect rates are proprietary to the foundry. We use a published typical value and show the range of 0.06 to 0.12."

**Q101. 'Why trust industry numbers (TrendForce, JLL, TSMC reports)?'**
Say: "They are the best available public estimates, and we flag them as estimates. Their uncertainty is covered by the sensitivity analysis and the Monte Carlo."

**Q102. 'Is India's grid failing under this? That is alarmist.'**
Say: "We are not predicting failure. We are showing the size of the connection and planning task, so it can be started early."

**Q103. 'What about China's approach?'**
Say: "China is the example of heavy domestic investment in the full chain, and it still faces equipment and packaging limits. We do not model it, but it supports our point that no country controls every layer."

**Q104. 'Why not focus on algorithms or data instead of hardware?'**
Say: "They matter, and India has strengths there. But algorithms need compute to train and run, and compute needs the physical base. Hardware is the layer that can be cut off from outside."

**Q105. 'One sentence: what should the government do on Monday?'**
Say: "Fix the power-connection pipeline and location mix for 50 MW and larger sites, require efficient cooling for subsidised compute, and negotiate packaging and memory capacity as seriously as GPU purchases."

---

## 15. Say these limitations yourself, before they are asked

1. "This is a what-if model, not a forecast."
2. "The capacity denominators are market estimates."
3. "Export controls are outside the model."
4. "The investment table is our proposal, not a government budget."
5. "The baseline uses H100-class values; the HBM stack count (6) is a class-level value."
6. "The 1,575 MW denominator covers colocation capacity only."

---

## 16. Mental arithmetic you can do on the spot

| Question | Calculation |
|---|---|
| IT load | 500,000 x 700 W x 1.82 = 637.0 MW |
| Facility | 637.0 x 1.40 = 891.8 MW |
| Share of colocation | 891.8 / 1,575 = 56.6% |
| Share of pipeline | 891.8 / 3,200 = 27.9% |
| Energy | 891.8 x 8,760 x 0.80 / 10^6 = 6.25 TWh |
| CO2 | 6.25 x 0.716 = 4.47 Mt |
| Water | 6.25 x 10^9 kWh x 1.80 L = 11.25 x 10^9 L |
| Racks | 637,000 kW / 60 = 10,617 |
| Wafers | 500,000 / 40 = 12,500; / 780,000 = 1.60% |
| CoWoS | 500,000 / 15 = 33,334; / 450,000 = 7.41% |
| HBM | 500,000 x 6 = 3.0 M; / 60 M = 5.00% |
| Ratio | 7.41 / 1.60 = 4.6 |
| D2C power saving | 637 x (1.45 - 1.18) = 172 MW |
| Substations | 891.8 / 50 = 18 |
| Subsidy | 1 - 0.78/2.00 = 61%; 1 - 0.78/2.80 = 72% |
| Investment | 95,500 + 2,57,000 = 3,52,500 crore |

---

## 17. Phrases to use and avoid

| Avoid | Use |
|---|---|
| "India will need 891.8 MW" | "If India deployed 500,000 H100-class GPUs, the model gives 891.8 MW" |
| "The first framework ever" | "To our knowledge, none of the studies we reviewed links all of these layers" |
| "India does not need a fab" | "Wafer volume for this programme is only 1.60% of TSMC output" |
| "56.62% of India's power" | "Equivalent to 56.62% of today's operational colocation capacity (1,575 MW)" |
| "Immersion is best" | "Direct-to-chip is the practical balance; immersion is better on paper" |
| "The government plan" | "Our proposed planning envelope" |
| "AI is just like nuclear weapons" | "AI shares the strategic pattern: early movers set the rules" |

**Closing line if you get a final word:** "The question is not whether India should be in the AI race, but whether it plans the power, cooling and chip supply the race physically requires. Our model puts numbers on that, and shows the hard part is not where most people are looking."
