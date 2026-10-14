# Your Paper Explained from Zero — and How to Turn It into a PPT

**Paper:** *Sovereign by Design: A Five-Pillar Framework for India's Strategic Compute and AI Infrastructure*
**Final PDF:** `output/final_paper.pdf` (6 pages) | **Source:** `manuscript/main.tex` | **Model code:** `model/demand_cascade.py`

> **How to use this file.** Read Parts 1-6 once, slowly, with the PDF open next to you. Part 7 lists what the paper does *not* claim, so you do not get trapped by the jury. Part 8 is a practice Q&A. Part 9 is the PPT plan. Part 10 is a one-page cheat sheet of numbers to memorise.
> Every number below was re-checked against the model output in the final version of the paper (Table II, Table V, Fig. 3 etc.).

---

## PART 0 — The whole paper in 30 seconds

> **India wants to buy hundreds of thousands of AI chips (GPUs). But a GPU is useless without electricity, cooling water, and a long chain of foreign factories that make it. We built a calculator that starts from "how many GPUs?" and works out, step by step, how much power, water, silicon wafers, chip-packaging and memory that needs. The surprise: the thing everyone worries about (building a chip factory in India) is the *smallest* problem. The real bottlenecks are advanced chip packaging, memory chips, and electricity supply to cities like Mumbai.**

If you remember only one sentence for the jury, remember the bold one.

### The three-line "so what"
1. **Wrong worry:** Making the silicon wafers for 500,000 GPUs needs only **1.60 %** of what TSMC (Taiwan) produces per year. That is easy to *buy*, so spending huge money on a leading-edge chip fab in India for this purpose is a poor use of money.
2. **Real worry #1 (chips):** Chip *packaging* (CoWoS) needs **7.41 %** of the world's capacity — **4.6 times** more pressure than the wafers — and nearly all of it is done by one company, TSMC.
3. **Real worry #2 (power):** 500,000 GPUs need **891.8 MW** at peak. India's total operational colocation (rented data-centre) capacity is only **1,575 MW**, so this one project equals **56.62 %** of everything India has today, and over half of it already sits in Mumbai.

---

## PART 1 — Plain-English story of the paper

### 1.1 The problem (use a simple analogy)
Imagine a country announces: *"We will buy 500 Ferraris for every city."* Before buying, someone must ask: Are there roads? Petrol pumps? Mechanics? Who makes the tyres, and do we depend on one foreign tyre factory?

India's AI plan is the same. The government (IndiaAI Mission, Rs 10,371 crore) wants lots of GPUs. But most people only count GPUs. They do not ask:
- Is there **electricity** (and the high-voltage lines/substations to carry it)?
- Is there **water** to cool them?
- Who makes the **chips, packages and memory**, and can they be cut off by another country?

### 1.2 The gap (why the paper is needed)
Different experts each look at only one piece:
- **Semiconductor analysts** study who makes chips, but ignore how much power the data centre needs.
- **Power-grid researchers** study electricity, but ignore chip packaging limits.
- **Policy writers** list goals, but never count physical resources.

The paper calls this **"disciplinary siloing"** (experts working in separate boxes). The paper lists five specific gaps (RG-01 to RG-05, see Table I in the paper):
| Code | Gap in plain words |
|---|---|
| RG-01 | Nobody links compute + power + chips + policy together |
| RG-02 | No "cascade": nobody starts from a GPU target and follows it all the way down |
| RG-03 | "Silicon wafer fallacy": wrongly assuming wafer fabs are the main problem |
| RG-04 | Tropical cooling is underestimated (India is hot, so cooling costs more) |
| RG-05 | Frameworks are not turned into numbers or action ("operationalisation deficit") |

### 1.3 What the paper contributes (two things)
- **C1 — IAIRF 2.0** (India AI Infrastructure Readiness Framework): a *conceptual map* with **5 pillars**.
- **C2 — DCM** (Demand-Cascade Model): a *calculator* with **6 layers** that turns a GPU number into physical requirements.

Think of C1 as the **map** and C2 as the **calculator**.

### 1.4 The Five Pillars (the map)
| Pillar | Name in the paper | In plain words |
|---|---|---|
| **P1** | Compute & Semiconductor Sovereignty | The GPUs themselves, chip packaging, minerals like gallium. The IndiaAI shared pool: 45,000+ GPUs at Rs 65 per GPU-hour |
| **P2** | Energy & Grid Readiness | Electricity supply, transmission lines, waiting time for a grid connection, frequency stability |
| **P3** | Physical Resources & Data Centres | Buildings, cooling, water, where data centres are located (52.4 % in Mumbai) |
| **P4** | Connectivity, Data & Security | Undersea internet cables (17+), data-protection law (DPDPA), cybersecurity rules for power assets (CEA 2026) |
| **P5** | Governance, Investment & Indigenous Capability | Government missions (IndiaAI, Semicon India 2.0), money, talent, home-grown AI models |

> **Warning:** the old `presentation/speaker_notes.md` describes the pillars differently (e.g. "Pillar IV: Semiconductor Supply Chains"). **Use this table — it matches the final paper.**

### 1.5 The Four Feedback Loops (why the pillars cannot be fixed one at a time)
A "loop" is a trap where fixing one thing is blocked by another.
- **Loop A — Power-Compute Deadlock:** You cannot install GPUs without power; you cannot get power (grid queue, land) without proving you will use it. Each waits for the other.
- **Loop B — Packaging-Memory Co-Constraint:** A single US export-rule change can cut off *both* CoWoS packaging and HBM memory at the same time.
- **Loop C — Data-Connectivity Governance Tension:** Data-localisation law (keep data in India) raises costs and makes foreign investors nervous.
- **Loop D — Talent-Sovereignty Paradox:** India has 4.3 million engineers, but many work for foreign companies' India centres (GCCs); AI/ML talent gap about 720,000 now, 1.6 million by 2030.

---

## PART 2 — Jargon decoder (keep this open while reading)

| Term | Meaning in plain English | Why it matters here |
|---|---|---|
| **GPU / accelerator** | The special chip that does AI maths (e.g. NVIDIA H100) | The thing India wants to buy |
| **TDP (board power)** | Electricity a GPU draws at full load. H100 = **700 W** (like 7 bright bulbs) | Starting point of the whole calculation |
| **MW, GW, TWh** | MW = megawatt (a million watts). 1 GW = 1,000 MW. TWh = terawatt-hour = energy over time (a billion kWh) | MW is "how hard", TWh is "how much in a year" |
| **PUE** | Power Usage Effectiveness = total building electricity ÷ computer electricity. PUE 1.40 means for every 1 unit used by computers, 0.4 extra goes to cooling etc. Lower is better; 1.0 is perfect | Hot India has high PUE (avg 1.55) |
| **WUE** | Water Usage Effectiveness = litres of water used per kWh. Evaporative cooling = 1.80 L/kWh | Water stress |
| **ML (megalitre)** | 1 million litres | 11,250 ML = 11.25 *billion* litres |
| **Colocation data centre** | A "rented" data centre where firms put their servers | India's capacity = 1,575 MW (mid-2026) |
| **Substation** | Big electrical hub that steps high voltage down for a site | 18 substations of 50 MW needed for 891.8 MW |
| **Wafer** | A 300 mm (12-inch) silicon disc on which chips are printed. Like a pizza | Wafer count = "how much silicon" |
| **Die** | One chip cut from the wafer. GPU die is huge (814 mm²) so only 63 fit | Few dies per wafer = many wafers |
| **Yield** | Fraction of dies that work (defects ruin some) | Lower yield = more wafers |
| **TSMC** | Taiwan company that makes nearly all advanced AI chips | The "denominator": ~780,000 sub-5 nm wafers/yr |
| **Sub-5 nm / EUV** | Most advanced chip-making; EUV machines are made only by ASML (Netherlands) | 100 % monopoly |
| **CoWoS** | "Chip-on-Wafer-on-Substrate": TSMC's packaging that mounts the GPU and its memory side by side on a silicon base ("interposer") | The hidden bottleneck; ~450,000 wafers/yr globally |
| **HBM / HBM3e** | High-Bandwidth Memory: memory chips stacked like a tower right next to the GPU | Made only by SK Hynix, Samsung, Micron; ~60 million stacks/yr |
| **HHI** | Herfindahl-Hirschman Index: market concentration. Square each company's % share and add up. One firm with 100 % = 10,000 (total monopoly). Above ~2,500 is "highly concentrated" | Shows how few suppliers control a step |
| **D2C cooling** | Direct-to-Chip liquid cooling: coolant pipes touch the chip | Saves 94.6 % of water |
| **Rear-door HEX / Immersion** | Other cooling methods: fan-door radiator; dipping servers in special liquid | Compared in Table V |
| **IEGC, RoCoF, BESS** | Grid code; Rate of Change of Frequency; Battery Energy Storage System | Grid stability (Eq. 1) |
| **Crore / lakh crore** | 1 crore = 10 million rupees; 1 lakh crore = 1 trillion rupees | Money tables |
| **EAR, iCET** | US Export Administration Regulations (chip export rules); India-US tech partnership | Outside-control risk |
| **PPP** | Public-Private Partnership | Investment table |

---

## PART 3 — The Demand-Cascade Model, layer by layer

### 3.0 The idea in one picture (this is Figure 1 of the paper)
```
GPU target N  -->  Layer 1: IT load  -->  Layer 2: Facility power & energy
                                                |                 |
                                         Layer 3: Cooling water   Layer 4: Silicon wafers
                                                       \         /
                                                  Layers 5-6: CoWoS packaging + HBM memory
```
"Cascade" = a waterfall. One number (N, how many GPUs) falls through six steps and each step produces a requirement. The model is **deterministic**: same inputs always give same outputs, so anyone can re-run it (`python model/demand_cascade.py`).

We run it for **N = 200,000, 500,000, 1,000,000** GPUs. **500,000 is the "baseline"** — all headline numbers refer to it.

**Baseline inputs** (each comes from a cited source or the project's parameter register):
| Input | Symbol | Value | Where it comes from |
|---|---|---|---|
| GPU power | P_gpu | 700 W | NVIDIA H100 datasheet |
| Server overhead ratio | R_host | 1.82 | DGX H100 uses 10.2 kW for 8 GPUs (5.6 kW GPU power): 10.2/5.6 = 1.82 |
| PUE | PUE | 1.40 | Indian average is 1.55; 1.40 = modern new build |
| Utilisation | U | 0.80 | GPUs busy 80 % of the year |
| Water intensity | I_water | 1.80 L/kWh | IEA report (evaporative cooling) |
| Rack power | D_rack | 60 kW/rack | AI racks are 40-100 kW |
| Die area | A_die | 814 mm² | H100 chip size |
| Defect density | D0 | 0.08 per cm² | Published typical value |
| CoWoS packages per wafer | C | 15 | Industry estimate |
| HBM stacks per GPU | N_stacks | 6 | H100/H200 class |

---

### 3.1 Layer 1 — IT electrical load (Equation 2)

**Question:** How much electricity do the computers themselves need?

$$P_{IT} = \frac{N \cdot P_{gpu} \cdot R_{host}}{10^{6}} \quad [\text{MW}]$$

- N = number of GPUs; P_gpu = watts per GPU; R_host = multiplier because each GPU sits inside a server that also has CPUs, fans, network cards (1.82 means the whole server uses 1.82 times the GPU's power).
- Dividing by 1,000,000 converts watts to megawatts.

**Worked example (500,000 GPUs):**
500,000 × 700 W × 1.82 = 637,000,000 W = **637.0 MW**.

**Crux:** *"A GPU's 700 W is only about half the story; the whole server draws 1.82× that."*

---

### 3.2 Layer 2 — Facility power and annual energy (Equations 3, 4, 5)

**Question:** The building also needs cooling, lights, power conversion. How much power does the grid actually have to deliver, and how much energy per year?

$$P_{facility} = P_{IT} \cdot PUE \quad [\text{MW}] \qquad (3)$$
$$E_{annual} = \frac{P_{facility} \cdot 8760 \cdot U}{10^{6}} \quad [\text{TWh}] \qquad (4)$$
$$GHG = E_{annual} \cdot EF_{grid} \quad [\text{Mt CO}_2/\text{yr}] \qquad (5)$$

- 8,760 = hours in a year. U = fraction of time busy. EF_grid = 0.716 tonnes of CO₂ per MWh (India's grid average, CEA).

**Worked example:**
- Facility power = 637.0 × 1.40 = **891.8 MW** (this is the "peak draw").
- Energy = 891.8 × 8,760 × 0.80 ÷ 1,000,000 = **6.25 TWh per year**.
- CO₂ = 6.25 × 0.716 = **4.47 million tonnes per year**.

**Then the key comparison:** 891.8 ÷ 1,575 MW (India's operational colocation capacity, mid-2026) = **56.62 %**.
Against the 3,200 MW *pipeline* (under construction till 2030): 891.8 ÷ 3,200 = **27.87 %**.

> **Careful phrasing:** Say *"equivalent to 56.62 % of today's operational capacity"*. Do **not** say "India will use 56 % of its data-centre power" — it is a **scale comparison**, not a forecast.

**Crux:** *"One 500k-GPU programme is the size of more than half of India's entire present data-centre industry."*

---

### 3.3 Layer 3 — Cooling water and racks (Equations 6, 7)

**Question:** How much water evaporates, and how many cabinets (racks) are needed?

$$W_{annual} = \frac{E_{annual} \cdot 10^{9} \cdot I_{water}}{10^{6}} \quad [\text{ML}] \qquad (6)$$
$$N_{rack} = \left\lceil \frac{P_{IT} \times 10^{3}}{D_{rack}} \right\rceil \qquad (7)$$

- Energy (TWh) × 10⁹ converts to kWh. × 1.80 litres per kWh gives litres. ÷ 10⁶ converts litres to megalitres.
- ⌈ ⌉ means "round up".

**Worked example:**
- Water: 6.2497 × 10⁹ kWh × 1.80 L = 11.25 × 10⁹ L = **11,249.5 ML** (11.25 billion litres).
- Racks: 637,000 kW ÷ 60 kW = 10,616.7 → **10,617 racks**.

**Crux:** *"Evaporative cooling is like the data centre sweating; in a hot, water-stressed country that sweat is billions of litres."*

---

### 3.4 Layer 4 — Silicon wafers (Equations 8, 9, 10)

**Question:** How many 300 mm silicon wafers must TSMC process to make 500,000 GPU chips?

**Step A — how many chips fit on one wafer (Eq. 8):**
$$N_{gross} = \left\lfloor \frac{\pi r^{2}}{A_{die}} - \frac{2\pi r}{\sqrt{2A_{die}}} \right\rfloor$$
- First term = wafer area ÷ chip area (how many would fit if the wafer were a perfect rectangle sheet). Second term subtracts chips lost at the curved edge.
- r = 150 mm, A_die = 814 mm².
- π × 150² = 70,686 mm². ÷ 814 = 86.84. Edge loss = 942.5 ÷ 40.35 = 23.36. 86.84 − 23.36 = 63.48 → **63 chips per wafer**.

**Step B — how many of those work (Eq. 9, the Murphy yield model):**
$$Y_{Murphy} = \left( \frac{1 - e^{-D_0 A_{die}}}{D_0 A_{die}} \right)^2$$
- Idea: defects land randomly on the wafer. A bigger chip has a higher chance of being hit. D₀ = defects per cm²; A in cm² (814 mm² = 8.14 cm²).
- D₀ × A = 0.08 × 8.14 = 0.651. Plug in: ((1 − e^−0.651) ÷ 0.651)² = **0.540** (54 % work).
- **"Binning" boost:** Makers sell chips with a few broken sections by switching those sections off (so a slightly flawed chip is still a good, slightly lower-spec chip). The model multiplies by 1.2 (capped at 0.85): 0.540 × 1.2 = **0.648 ≈ 0.65**.
- Good chips per wafer: 63 × 0.648 = 40.8 → rounded down = **40**.

**Step C — wafers needed (Eq. 10):**
$$W_{starts} = \lceil N / N_{good} \rceil = 500{,}000 / 40 = \mathbf{12{,}500\ wafers}$$

**Compare to the world:** TSMC makes about 780,000 sub-5 nm wafers a year → 12,500 ÷ 780,000 = **1.60 %**.

**Crux:** *"The silicon needs of a half-million-GPU programme are small — 1.6 % of one company's yearly output."*

---

### 3.5 Layers 5-6 — Packaging (CoWoS) and memory (HBM) (Equations 11, 12)

**Question:** A GPU chip alone is not a product. It must be *packaged* with memory. What does that consume?

$$W_{CoWoS} = \lceil N / C_{CoWoS} \rceil \qquad (11) \qquad\qquad N_{HBM} = N \cdot N_{stacks} \qquad (12)$$

- **CoWoS:** each GPU needs one silicon "interposer" (a base plate that connects the GPU and memory). About 15 finished packages come from one 300 mm interposer wafer (the interposer is large, so few fit).
  500,000 ÷ 15 = 33,333.3 → **33,334 interposer wafers**. Global capacity ≈ 450,000 per year → **7.41 %**.
- **HBM:** each H100/H200-class GPU carries 6 memory stacks → 500,000 × 6 = **3,000,000 stacks**. World output ≈ 60 million stacks/yr → **5.00 %**. (B200-class cards carry 8 → used in the "High" case.)

**Why 7.41 % is "worse" than 1.60 %:** the ratio is 7.41 ÷ 1.60 = **4.6×**. Packaging takes 4.6 times more of the world's capacity than the wafers do — and TSMC does ~90 % of CoWoS (HHI 8,100).

**Crux:** *"The wafer is easy to find; the bridge that connects the chip to its memory is the scarce part."*

---

### 3.6 The grid-stability equation (Equation 1, the odd one out)

$$\frac{2H}{f_0}\frac{df}{dt} = P_m - P_e - \Delta P_{AI}$$

**Plain meaning:** The power grid is like a spinning flywheel at 50 Hz. If demand suddenly jumps (an AI cluster ramps up), the flywheel slows down: frequency falls. The equation says *how fast* it falls.
- H = grid "inertia" (how heavy the flywheel is) = 4.2 seconds. f₀ = 50 Hz. P_m = generation, P_e = normal demand, ΔP_AI = the sudden AI load change. df/dt = rate of change of frequency (RoCoF).

**Worked example:** a sudden **250 MW** AI load on a **50 GW** grid: (250 ÷ 50,000) = 0.005 of the grid. df/dt = 50 × 0.005 ÷ (2 × 4.2) = **−0.0298 Hz per second**.
*Illustration (our arithmetic, not from the paper):* India's grid code allows 49.90-50.05 Hz. Frequency would reach 49.90 Hz in about 0.10 ÷ 0.0298 ≈ **3.4 seconds** if nothing responded — which is why fast battery storage (BESS) is recommended.

**Where it fits:** Eq. 1 is *background motivation* for why power is a risk (AI loads can swing 20-40 % within a minute). It is **not** one of the six cascade layers.

**Crux:** *"Big AI loads switching on and off can shake the grid frequency within seconds."*



---

## PART 4 — The results: what the model says

### 4.1 Scenario table (Table II in the paper) — how to read it
Columns: **IT MW** (Layer 1), **Fac. MW** (Layer 2 peak), **TWh/yr**, **Water ML** (Layer 3), **Wafers** and **TSMC %** (Layer 4), **CoWoS** and **CoWoS %** (Layer 5), **Colo %** (share of India's 1,575 MW colocation capacity).
Each GPU target has **Low / Base / High** rows — three "what if" versions:

| Setting | Low (optimistic) | **Base** | High (pessimistic) |
|---|---|---|---|
| GPU power | 700 W | **700 W** | 1,000 W (Blackwell-class) |
| Server overhead | 1.60 | **1.82** | 2.10 |
| PUE | 1.25 | **1.40** | 1.55 |
| Utilisation | 0.65 | **0.80** | 0.90 |
| Water (L/kWh) | 0.20 | **1.80** | 2.50 |
| Defect density | 0.06 | **0.08** | 0.12 |
| CoWoS packages / wafer | 18 | **15** | 12 |
| HBM stacks / GPU | 6 | **6** | 8 |

> The paper's text names only GPU power and PUE for the variants; the code changes all of the above. If asked "what do Low and High mean?", use this table.

**The three Base rows to memorise:**
| | 200k GPUs | **500k GPUs** | 1M GPUs |
|---|---|---|---|
| IT load (MW) | 254.8 | **637.0** | 1,274.0 |
| Facility peak (MW) | 356.7 | **891.8** | 1,783.6 |
| Energy (TWh/yr) | 2.50 | **6.25** | 12.50 |
| Water (ML/yr) | 4,499.8 | **11,249.5** | 22,499.0 |
| Wafer starts | 5,000 | **12,500** | 25,000 |
| % of TSMC output | 0.64 % | **1.60 %** | 3.21 % |
| CoWoS wafers | 13,334 | **33,334** | 66,667 |
| % of global CoWoS | 2.96 % | **7.41 %** | 14.81 % |
| % of India colocation | 22.65 % | **56.62 %** | 113.24 % |

**Patterns a beginner can spot:**
- Everything scales **linearly** with N. Double the GPUs → double the power, water, wafers (that is why 200k → 500k → 1M columns look like ×2.5 and ×2).
- At **1 million GPUs the facility needs more power than India's entire colocation industry today (113 %)**.
- In the worst case (1M, High) the draw is **3,255 MW = 2.07 × India's present capacity** (3,255 ÷ 1,575).
- Wafer % stays in single digits even in the worst case (4.27 %); packaging % is always bigger than wafer % — in every row.

### 4.2 Monte Carlo (Table III) — "what if all the inputs wiggle together?"
- **What it is:** the computer picks random values for 7 inputs at once, 1,000 times, and records the results.
- Ranges used: GPU power 650-850 W; host ratio 1.65-2.05; PUE 1.25-1.55; utilisation 0.70-0.90; WUE 0.30-2.20; D₀ 0.06-0.11; 14/15/16 packages per wafer. Seed 42 (so results can be repeated).
- **P10 / P50 / P90** = the 10th, 50th (median) and 90th percentile. "80 % of outcomes fall between P10 and P90."

| Output | P10 | P50 | P90 |
|---|---|---|---|
| Facility power (MW) | 809.2 | 963.1 | 1,114.4 |
| Energy (TWh) | 5.69 | 6.79 | 8.24 |
| Water (ML) | 3,515.5 | 8,186.0 | 13,570.9 |
| Wafer starts | 11,112 | 12,821 | 14,706 |
| CoWoS wafers | 31,250 | 33,334 | 35,715 |

- **Why is the median power (963 MW) higher than the base case (891.8 MW)?** Because the random GPU-power range is 650-850 W (average 750 W), while the base case uses 700 W. Say this *before* the jury asks.
- **Take-away:** in the middle 80 % of draws, facility power = 51-71 % of India's colocation capacity; CoWoS = 6.9-7.9 % of global; wafers = only 1.4-1.9 % of TSMC. **The ordering "packaging > wafers" never flips.**

### 4.3 The four findings

**Finding 1 — Refuting the "silicon wafer hypothesis".** Common belief: "India needs its own chip fab to be AI-sovereign." Result: 12,500 wafers/yr = 1.60 % of TSMC — buyable through capacity-reservation contracts. A leading-edge fab takes years to qualify and only pays off at huge volume; building one for 1.60 % of demand is a misuse of capital. *(Careful: this says the **wafer volume** is not the bottleneck. It does not say fabs are useless for other purposes.)*

**Finding 2 — Structural chokepoint inversion.** "Inversion" = the real order of difficulty is upside-down from what people think.
- CoWoS: 7.41 % (4.6× the wafer pressure).
- HBM: 5.00 % of world output; only 3 suppliers; **zero** Indian production.
- Power: 891.8 MW into Mumbai (which already holds 52.4 % of national capacity) ≈ 18 substations of 50 MW each; high-voltage equipment lead time 36-48 months.

**Finding 3 — Tropical cooling penalty.** Evaporative cooling in 42 °C+ heat pushes PUE up to 1.65 and consumes 11,651 ML/yr (≈ 236,000 residents' domestic water at an assumed 135 L/person/day). Heat also shortens hardware life. **D2C liquid cooling** cuts water by **94.6 %** (to 632 ML) and facility load by **172 MW** (PUE 1.45 → 1.18; 637 × 0.27 = 172).

**Finding 4 — Scale and tariffs.** India's shared pool is ~34,000-45,000 GPUs (policy target 100,000 by end-2026). The 500k baseline is **11-15 times** today's pool. IndiaAI charges Rs 65/GPU-hour (≈ $0.78) vs. $2.00-2.80 market → a **61-72 % subsidy**. Advanced chips still depend on US export rules.

---

## PART 5 — The three figures in the paper (how to read and what to say)

### Figure 1 — The six-layer cascade (flow diagram)
- **What you see:** boxes left → right. Grey = policy input; **green** = electrical (Layers 1-2); **blue** = physical resources (Layer 3); **red** = semiconductor supply chain (Layers 4-6). Each box shows the equation result for 500k GPUs.
- **Read it as:** *"Start with N GPUs → 637 MW of servers → 891.8 MW and 6.25 TWh for the building → 11,249.5 ML of water; and in parallel 12,500 wafers → 33,334 CoWoS wafers and 3.0M memory stacks."*
- **Say:** "This is the whole model on one slide. Every number is computed by code, not typed by hand."

### Figure 2 — Structural chokepoint inversion (horizontal bars)
- **Axis:** each bar = share (%) of a limited resource that 500k GPUs would need.
- **Bars (top to bottom):** wafers 1.60 % → HBM 5.00 % → CoWoS 7.41 % (all **blue** = global semiconductor capacity) → colocation power vs 2030 pipeline 27.87 % → colocation power vs today 56.62 % (both **red** = India power).
- **Message:** the bars get *longer* as you go down: the "famous" problem (wafers) is the shortest bar. That is the "inversion".
- **Say:** "The shortest bar is the one everyone argues about. The longest bar is the one nobody budgets for."
- **Careful:** blue and red bars use **different denominators** (global chip capacity vs India's power capacity). The figure shows *relative pressure*, not a single scale of "difficulty".

### Figure 3 — Sensitivity "tornado" (butterfly bars)
- **What it does:** moves **one input at a time** from its lowest to its highest value, keeping everything else at base, and shows how much the output changes (%).
- **Left part of a bar** = input at its low bound (lighter colour); **right part** = input at its high bound (darker colour). Colour = which output is affected: dark green = peak power; light green = annual energy; blue = water; red = wafer starts.
- **Rows (largest swing at top):**
| Input | Output affected | Low → | High → | Why |
|---|---|---|---|---|
| Cooling WUE 0.20→2.50 | Water | −88.9 % | +38.9 % | Water use is directly proportional to WUE (0.2/1.8) |
| Defect density 0.06→0.12 | Wafers | −14.9 % | +33.3 % | More defects → fewer good chips → more wafers |
| GPU power 700→1,000 W | Peak power | 0.0 % | +42.9 % | 1,000/700 = 1.43. Low = 0 because 700 W *is* the base |
| Utilisation 0.65→0.90 | Energy | −18.7 % | +12.5 % | 0.65/0.80, 0.90/0.80 |
| Host overhead 1.60→2.10 | Peak power | −12.1 % | +15.4 % | 1.60/1.82, 2.10/1.82 |
| PUE 1.25→1.55 | Peak power | −10.7 % | +10.7 % | 1.25/1.40, 1.55/1.40 |
- **Message:** For **power**, the biggest lever is the GPU's own wattage (+42.9 %); for **water**, it is the cooling technology (−88.9 %). Cooling choice is the biggest single policy lever.
- **Warning:** do not compare bar lengths across different colours as if they were the same quantity (power vs water vs wafers).

> **Figure 4 (cooling trade-off, PUE vs WUE)** exists in `figures/` but is **not** in the paper. You may use it as a *bonus slide*: x = water per kWh, y = PUE; the four cooling types run from "high water, high PUE" (air) to "almost no water, low PUE" (immersion).

---

## PART 6 — The other tables, the roadmap, the money

### Table I — Prior art matrix
Compares existing studies with this paper on method, whether they handle GPU scenarios, and which gaps they close.
| Source | Method | GPU scenarios? | Gaps closed |
|---|---|---|---|
| Akimitsu 2026 | HHI dependency graph | None | RG-03 partial |
| IEA/LBNL 2024 | Energy model | Global | RG-04 partial |
| Kaufmann 2025 | Grid power-flow | None | RG-01 partial |
| SBI CHAKRA 2025 | Market census | None | RG-04 partial |
| **This paper** | 5-Pillar + DCM | **200k-1M** | **RG-01 to 05** |
**Safe claim:** "None of the studies we reviewed combines GPU targets, power, cooling and chip supply in one model." **Avoid "first ever in the world"** (you cannot prove it).

### Table IV — Structural chokepoint hierarchy
| Layer | HHI | India's share | Demand from 500k GPUs | Lead time |
|---|---|---|---|---|
| EUV lithography (ASML) | 10,000 | 0 % | upstream | 24-36 months |
| Sub-5 nm logic (TSMC) | N/A | 0 % | **1.60 %** | 14-18 weeks |
| CoWoS packaging (TSMC) | 8,100 | 0 % | **7.41 %** | 20-28 weeks |
| HBM3e (SK/Samsung/Micron) | 4,718 | 0 % | **5.00 %** | 16-24 weeks |
| Colocation power (India) | N/A | 100 % | **56.62 %** | 36-48 months |
| Municipal water rights | N/A | 100 % | 11,250 ML | Seasonal |
- **HHI example:** HBM = 57² + 38² + 5² = 3,249 + 1,444 + 25 = **4,718**. CoWoS 90² = 8,100. ASML 100² = 10,000.
- **How to read:** the bigger the HHI, the fewer firms control it. India's share of those global chip steps is 0 %, so India is a pure *buyer*.
- *(The lead-time column is indicative; do not quote it as a precise sourced number.)*

### Table V — Cooling technologies at 500k GPUs
| System | Annual PUE | Peak (summer) PUE | WUE (L/kWh) | Water (ML/yr) |
|---|---|---|---|---|
| Traditional air (evaporative) | 1.45 | 1.65 | 1.80 | 11,651.3 |
| Rear-door heat exchanger | 1.35 | 1.45 | 1.00 | 6,026.5 |
| **Direct-to-chip (D2C)** | **1.18** | **1.25** | **0.12** | **632.1** |
| Single-phase immersion | 1.12 | 1.18 | 0.03 | 150.0 |
- **Read:** moving down the table, both PUE (power waste) and water fall. D2C is the practical sweet spot; immersion is best on paper but harder to deploy.
- **Policy link:** "Condition IndiaAI subsidies on PUE ≤ 1.25 and closed-loop dry heat rejection".

### Table VI — Investment architecture (2026-2035)
| Area | Public (Rs crore) | PPP (Rs crore) | Lead agencies |
|---|---|---|---|
| AI Infrastructure Zones & AICA (P3/P5) | 2,500 | 5,000 | DPIIT, MeitY |
| Power corridors + BESS (P2) | 15,000 | 65,000 | MoP, SECI |
| GPU cluster expansion (P1) | 20,000 | 80,000 | MeitY, IndiaAI |
| Packaging JVs / gallium (P1) | 10,000 | 40,000 | ISM, CSIR |
| SMR / nuclear baseload (P2) | 25,000 | 50,000 | DAE, NPCIL |
| Talent & R&D (P5) | 15,000 | 5,000 | MoE, DST |
| Connectivity / security (P4) | 8,000 | 12,000 | DoT, NCIIPC |
| **Total** | **95,500** | **2,57,000** | |
- Total = Rs 3,52,500 crore ≈ Rs 3.5 lakh crore.
- **Be honest:** these are the **authors' proposed planning envelopes**, not government budgets. The paper says so explicitly.

### The 3-tier roadmap (what to actually do)
| Tier | Period | Examples |
|---|---|---|
| **Tier 1 — Build domestically** | 2026-28 | Move data centres out of Mumbai (target < 35 % share by 2028; 15-20 % capital rebate); require D2C cooling for IndiaAI subsidy; 9-month CEA approval window for ≥50 MW substations; AI Power Corridors (5 GW); 20 pre-cleared AI Infrastructure Zones in 10 states |
| **Tier 2 — Develop via partnerships** | 2028-31 | Advanced-packaging joint ventures (ASE, Ibiden with Tata/Micron) to reduce CoWoS dependency < 1 % by 2032; gallium from bauxite "red mud" (aspirational 50 t/yr); chiplet consortium using 120,000 VLSI engineers; renewable round-the-clock power + small modular reactors |
| **Tier 3 — Manage external dependence** | 2031-35 | Multi-year wafer reservations at TSMC/Samsung (manageable at ~1.6 %); HBM4 advance-purchase deals; an export-control "contingency playbook" |
**Logic of the tiers:** do what you control first (power, cooling, location), then build with partners (packaging), and *manage* what you can't control (foundry, memory).

### KPIs (how to measure success, one line per pillar)
P1: sovereign GPU fleet size, domestic packaging throughput. P2: grid-connection lead time for ≥50 MW, share of round-the-clock renewables. P3: Mumbai share (<35 %), D2C share, PUE. P4: backbone capacity, DPDPA rules, OT-security compliance. P5: AICA 90-day clearance rate, IndiaAI fund disbursement.


---

## PART 7 — What the paper does NOT claim (know your limits before the jury does)

| Do **not** say | Say instead |
|---|---|
| "India **will** need 891.8 MW" | "**If** India deployed 500,000 H100-class GPUs, the model gives 891.8 MW" — it is a **what-if scenario**, not a forecast |
| "This is the first framework ever" | "To our knowledge, none of the studies we reviewed links all of these layers" |
| "India doesn't need any fab" | "Wafer **volume** for this programme is only 1.60 % of TSMC's output; a fab built just for that is poor value. Fabs may still matter for other strategic reasons" |
| "56.62 % of India's power" | "equivalent to 56.62 % of today's operational **colocation** capacity (1,575 MW)" |
| "Immersion cooling is best, so adopt it" | "D2C is the practical balance; immersion is better on paper" |
| "The investment table is the government's plan" | "These are **our proposed** planning envelopes" |
| GDP gains, startups or jobs numbers | The paper deliberately makes **no** GDP forecast — only the physical requirements and cost envelope |

**Honest limitations (the paper states them; say them first and you look confident):**
1. **Fixed utilisation 80 %.** Real loads vary through the day (peaks of +20-40 %).
2. **Defect density is a published typical value (0.08/cm²)**; TSMC's real data is secret. Moving it to 0.06-0.12 changes wafer needs by −14.9 % to +33.3 %.
3. **Export rules and diplomacy (EAR, iCET) are outside the model.**
4. **Capacity denominators (780k wafers, 450k CoWoS, 60M HBM stacks) are market estimates** and change every year — they are the single weakest point; say "estimates".
5. **The model counts GPUs, not performance.** Newer chips do more work per watt, so the same compute may need fewer GPUs.
6. **Baseline uses H100-class numbers (700 W, 6 HBM stacks).** Blackwell-class cases appear only in the "High" variant.

**Numbers that have the weakest backing — do not stress them in the talk:** the lead-time column of Table IV; the "135 L/person/day" water-per-person assumption; the 120,000 VLSI-engineer figure; the specific Rs amounts in Table VI (they are proposals). Also, the original external reports (JLL, CBRE, TrendForce etc.) were not re-opened during checking — **open the PDFs in `sources/` once yourself** so you can answer "where does 780,000 come from?".

---

## PART 8 — Practice Q&A (rehearse these out loud)

**Q1. In one sentence, what is your contribution?**
A model that starts from "how many GPUs" and converts it into power, water, wafers, packaging and memory demand — and shows the bottleneck is packaging and power, not wafers.

**Q2. Why is 891.8 MW the number?** 500,000 × 700 W × 1.82 = 637 MW of servers; × PUE 1.40 = 891.8 MW at the building.

**Q3. Where does 1.82 come from?** An NVIDIA DGX H100 server draws 10.2 kW for 8 GPUs of 700 W each (5.6 kW). 10.2 ÷ 5.6 = 1.82. (Source in the project's parameter register.)

**Q4. Why PUE 1.40 when India averages 1.55?** 1.55 is today's average of mostly older sites; 1.40 is a modern new-build target. We also show 1.25 and 1.55 in Low/High and in the sensitivity chart (±10.7 %).

**Q5. Is 56.62 % realistic? Nobody builds it all at once.** Correct. It is a scale comparison — it shows the programme is the size of more than half of today's industry, so it must be planned years ahead. Against the 2030 pipeline (3,200 MW) it is 27.87 %.

**Q6. Why compare against TSMC only?** Over 90 % of sub-5 nm logic is made in Taiwan (CSET). We state this as a limitation: other foundries (Samsung, Intel) add some capacity.

**Q7. If wafers aren't the problem, why does Semicon India matter?** Wafer *volume* for this programme is small and purchasable, but India's packaging (ATMP/OSAT), design talent and mineral supply chain are the parts it can actually build — that is Tiers 1-2 of the roadmap.

**Q8. Why is CoWoS harder than wafers?** Each GPU needs one large interposer; only ~15 packages fit on a wafer, global capacity is ~450,000 wafers/yr, and TSMC controls ~90 % (HHI 8,100). Result: 7.41 % vs 1.60 % — 4.6×.

**Q9. How accurate are 780,000 / 450,000 / 60 million?** They are industry estimates (TrendForce, TSMC reports) recorded in our denominator audit; they shift every year. If a denominator is 20 % different, the percentages change by about 20 % but the *order* stays the same. (Check: even the Monte Carlo never flipped the order.)

**Q10. What is the Monte Carlo for?** To test whether the conclusion survives if all inputs vary together: 1,000 random draws. In the middle 80 %, wafers stay at 1.4-1.9 % of TSMC and CoWoS at 6.9-7.9 % of global.

**Q11. Why is the Monte Carlo median above your base case?** The random GPU-power range (650-850 W) averages 750 W, above the 700 W base.

**Q12. What is the single biggest policy lever?** Cooling technology: switching to D2C cuts water use by 94.6 % and about 172 MW of facility load. For the power draw itself, GPU wattage matters most (+42.9 % at 1,000 W).

**Q13. Why are you worried about Mumbai?** 52.4 % of India's data-centre capacity is there (near the undersea cable landings). One city's grid failure or cable fault hits half the industry; adding 891.8 MW more would need ~18 substations of 50 MW and 36-48 months equipment lead time.

**Q14. What does "sovereign" mean in your paper?** Not owning every step — that is unrealistic. It means controlling what India can control (power, cooling, location, packaging partnerships) and managing the dependencies it cannot (foundry, memory, export rules).

**Q15. Why 6 HBM stacks and not 8?** H100/H200-class cards use 6 (our register, PAR-011); B200-class use 8, which we use in the High case. With 8, HBM demand would be 6.67 % instead of 5.00 %. Either way it is above the 1.60 % wafer figure.

**Q16. What would change your conclusion?** If TSMC's packaging capacity grew several-fold, or if India won guaranteed priority allocation, the CoWoS pressure would fall. If wafer yield collapsed (D₀ much higher), wafer demand would rise — but even at 0.12 defects/cm² it is only 2.14 % of TSMC.

**Q17. Is your investment table official?** No — it is our proposed planning envelope (Rs 95,500 crore public + Rs 2,57,000 crore PPP).

**Q18. What is new compared with IEA / LBNL?** They model power and cooling for data centres but don't connect to chip supply; Akimitsu maps chip chokepoints but without power or GPU scenarios. We connect both in one reproducible model with 200k-1M GPU scenarios.

**Q19. How can we reproduce your results?** `python model/demand_cascade.py` (deterministic, seed 42 for Monte Carlo); 10 unit tests pass (`python model/tests/test_demand_cascade.py`); figures are generated from the same code (`python scripts/generate_figures.py`).

**Q20. Did you use AI tools?** Answer **truthfully** per your team's actual use (the project notes mention AI assistants for drafting/critique/code checks). A safe pattern: "We used AI tools as assistants for drafting and checking; the model, the data choices and every number were verified by us, and we take responsibility." Do not deny use if it happened.

**Q21. What would you do with more time?** Plug the model into a power-flow (ACOPF) simulator of western and southern state grids using IndiaAI-portal telemetry, add chip-efficiency (performance-per-watt) trends, and test other Global South countries.

---

## PART 9 — Building the PPT

### 9.1 Design rules (read before opening PowerPoint)
1. **One message per slide.** The title is the message ("Wafers are the *smallest* problem"), not a topic ("Results").
2. **Max ~6 lines / 30 words per slide;** font ≥ 24 pt body, ≥ 32 pt titles. The jury is 5-10 metres away.
3. **Use the same colour code as the figures:** green = electricity, blue = physical resources/global capacity, red = chip supply chain/India constraint, grey = neutral. Judges will learn the code by slide 3.
4. **Big-number slides** work best: one huge number + one line (e.g. "891.8 MW" / "= 56.62 % of India's data-centre capacity").
5. **Show at most ONE equation** (Layer 1) on a main slide, written in words next to it. Put the rest in backup slides.
6. **Use the PNG files, not screenshots of the PDF:** `figures/fig1_demand_cascade_architecture.png`, `figures/fig2_structural_chokepoint_inversion.png`, `figures/fig5_sensitivity_tornado_montecarlo.png` (this is Fig. 3 in the paper), bonus `figures/fig4_cooling_water_energy_pareto.png`. They are 300 dpi, so they stay sharp when enlarged. Vector `.pdf`/`.svg` versions are in the same folder.
7. **Animate Fig 1 in steps** (Appear on click: Layer 1 → Layer 2 → Layers 3/4 → Layers 5-6) so you can explain one box at a time.
8. **Reduce Fig 2 / Fig 3 labels:** crop or enlarge so axis text is readable; consider re-colouring only the bar you are talking about (highlight the 1.60 % bar, then the 7.41 % bar).
9. **Title slide:** paper title, authors (Dr. Madhavi Dhingra + 4 students), Amity University Madhya Pradesh, track "AI Infrastructure, Semiconductor Sovereignty & Strategic Computing", ResearchThon 2026.
10. **Don't read the slide.** Slides = pictures and numbers; the words come from you.

### 9.2 Recommended slide plan — 10 main slides (~8 minutes) + backups
*(If you only get 5 minutes, use the "5-minute cut" below. Confirm the time limit with the organisers.)*

| # | Slide title (the message) | What is on the slide | What you say (core idea) | Time |
|---|---|---|---|---|
| 1 | **Title** | Title, team, institute, track | One sentence: "We asked what India's AI chip plans physically require." | 0:20 |
| 2 | **"Buying GPUs is the easy part"** | Photo/icon: GPU → plug → water drop → chip factory; the Ferrari analogy | The problem: GPUs need power, water and a foreign supply chain; India plans 100,000 → 500,000 GPUs; nobody has linked it all | 0:50 |
| 3 | **The gap: experts work in silos** | 3 boxes (Chips / Power / Policy) with a "?" gap between them | Existing studies cover one piece each; our contribution = 5-pillar map + 6-layer calculator | 0:45 |
| 4 | **Five pillars, four traps** | Pentagon of 5 pillars (P1-P5) + tiny icons for Loops A-D | One line per pillar; give one loop example (Power-Compute deadlock) | 0:50 |
| 5 | **The calculator: Figure 1 (animated)** | Fig 1, revealed step by step; Layer 1 equation in words beside it: "GPUs × watts × server overhead" | Walk the cascade; stress that every number is computed by code you can re-run | 1:15 |
| 6 | **Result 1: the power wall** | HUGE: "891.8 MW" → "56.62 % of India's data-centre capacity". Mini-bar: 200k/500k/1M = 22.65 / 56.62 / 113.24 % | Scale comparison, not a forecast; 1M GPUs would exceed today's entire industry | 1:00 |
| 7 | **Result 2: the inversion (Figure 2)** | Fig 2 with the 1.60 % bar highlighted first, then 7.41 % and 56.62 % | "The problem everyone debates is the smallest bar." 4.6× | 1:15 |
| 8 | **Result 3: cooling is the biggest lever (Table V + Fig 3 highlight)** | 2-column mini table: Air 11,651 ML vs D2C 632 ML; "−94.6 %, −172 MW" | Hot climate → evaporative cooling is costly; D2C is the policy fix. Show WUE bar of tornado (−88.9 %) | 0:50 |
| 9 | **How sure are we? (Monte Carlo + sensitivity)** | Fig 3 tornado + one line "1,000 random runs: wafers 1.4-1.9 %, CoWoS 6.9-7.9 % — order never flips" | Robustness: the conclusion survives uncertainty | 0:50 |
| 10 | **What India should do: 3 tiers** | Timeline with 3 coloured blocks (Build 2026-28 / Partner 2028-31 / Manage 2031-35) + "Rs 95,500 cr public + Rs 2.57 lakh cr PPP (our proposal)" | Do the controllable first; partner on packaging; manage the rest | 1:00 |
| 11 | **Take-aways & limits** | 3 bullets (wafers small, packaging + power binding, cooling lever) + "Limits: what-if model; estimates" | End strongly; mention limitations yourself | 0:40 |
| — | **Thank you / Q&A** | Contact + QR to repo (optional) | Invite questions | — |

(That is 11 content slides + thank-you; at ~45 s each ≈ 9 min. Merge slides 2-3 if you need a tighter 8 minutes.)

### 9.3 The 5-minute cut (if the limit is tighter)
Slides: **1** Title (10 s) → **2** Problem + gap, merged (40 s) → **3** Fig 1 cascade (60 s) → **4** The power wall (45 s) → **5** Fig 2 inversion (60 s) → **6** Cooling + robustness merged (45 s) → **7** Roadmap + take-aways (40 s). Move pillars/loops to a backup slide.

### 9.4 Suggested script lines for the key slides (adapt in your own words)
- **Slide 2:** "AI is not just software. A chip needs electricity, water, and a supply chain that starts in the Netherlands, runs through Taiwan, and ends in a data centre. India's plan counts GPUs; we asked what those GPUs physically require."
- **Slide 5:** "Start with a number — how many GPUs. Each GPU draws 700 watts, but the server around it makes it 1.82 times that. Multiply, and 500,000 GPUs need 637 megawatts. The building's cooling overhead lifts that to 891.8 megawatts."
- **Slide 6:** "891.8 megawatts is more than half of everything India's data-centre industry has today. At a million GPUs, it is more than all of it."
- **Slide 7:** "Everyone argues India needs its own chip factory. The wafers for 500,000 GPUs are 1.6 percent of what one company makes in a year. The scarce thing is the packaging — 7.4 percent — and the memory. The easy problem is the famous one; the hard problem is the invisible one."
- **Slide 8:** "India is hot and water-stressed. Direct-to-chip liquid cooling cuts the water by 94.6 percent and saves 172 megawatts. This is the cheapest policy lever in our study."
- **Slide 11:** "This is a what-if model, not a forecast. The denominators are market estimates, and the order of the bottlenecks holds even when we randomise everything."

### 9.5 Backup slides (hidden after "Thank you" — open only if asked)
B1 Equations 2-7 (power, energy, water, racks) with the worked 500k example. B2 Wafer maths (Eq. 8-10: 63 dies → 40 good → 12,500 wafers). B3 CoWoS and HBM maths (Eq. 11-12). B4 Table II full scenario results. B5 Monte Carlo table. B6 Chokepoint table with HHI. B7 Investment table. B8 Parameter register (where each input comes from). B9 Grid-stability equation and the 3.4-second illustration. B10 Fig 4 cooling trade-off. B11 Limitations list.

### 9.6 Delivery tips
- **Split roles** (5 authors): e.g. A = problem + gap + pillars (slides 2-4); B = model/Fig 1 (slide 5); C = results (6-8); D = robustness + roadmap (9-10); faculty or lead = take-aways + Q&A coordination. Each speaker owns the Q&A on their section.
- **Rehearse with a timer** at least 3 times; trim words, not slides, if you overrun.
- **Memorise the 8 numbers** in Part 10. Everything else you can read off the backup slides.
- **Use analogies out loud:** pizza (wafer), "sweating" (evaporative cooling), flywheel (grid frequency), "bridge" (CoWoS), "Ferrari without roads" (opening).
- **Say "if" and "scenario"** instead of "will". Say "estimate" for the denominators.
- **Look at the jury, not the screen.** Point at the figure with a laser/pointer only on the bar you discuss.
- **Prepare for a "why not X?" question** (why TSMC only, why 700 W, why not nuclear): the honest answer is in Part 7-8.
- **Bring** the PDF, the PPT in two formats (.pptx and .pdf), and the repo folder offline on a USB drive.

---

## PART 10 — Cheat sheet: the numbers to memorise

| What | Number |
|---|---|
| Baseline GPUs | **500,000** (also 200k and 1M) |
| GPU power / server factor | **700 W** / **1.82** |
| IT load | **637.0 MW** |
| PUE / facility peak | **1.40** / **891.8 MW** |
| Energy / CO₂ | **6.25 TWh/yr** / **4.47 Mt/yr** |
| Water (baseline, evaporative) | **11,249.5 ML** (≈ 11.25 billion litres) |
| India colocation capacity (mid-2026) | **1,575 MW** → project = **56.62 %** |
| 2030 pipeline | 3,200 MW → **27.87 %** |
| Chips per wafer / good chips | **63 / 40** (yield 0.54 → 0.65 with binning) |
| Wafer starts / share of TSMC | **12,500 / 1.60 %** |
| CoWoS wafers / share of global | **33,334 / 7.41 %** (4.6× the wafer pressure) |
| HBM stacks / share of global | **3.0 million / 5.00 %** |
| D2C cooling | **−94.6 % water, −172 MW**, PUE 1.18 |
| Mumbai share of India's capacity | **52.4 %** |
| 1M GPUs, High case | 3,255 MW = **2.07 ×** India's present capacity |
| Today's shared GPU pool / target | 34,000-45,000 / 100,000 by end-2026 |
| Subsidy | Rs 65/GPU-hr (≈ $0.78) vs $2.00-2.80 → **61-72 %** |
| Public + PPP outlay (our proposal) | Rs 95,500 cr + Rs 2,57,000 cr = ~**Rs 3.5 lakh crore** |
| Bottleneck order | **Packaging (7.41 %) > HBM (5.00 %) > Wafers (1.60 %)**, and **power (56.62 %)** is the biggest |

---

## PART 11 — Housekeeping warnings before you build the PPT

1. **`presentation/speaker_notes.md` is out of date.** It uses the *old* title ("A Demand-Driven Framework..."), a different pillar list, an "84 papers" claim and old numbers. **Do not copy from it.** Use this file instead.
2. **Use `output/final_paper.pdf`** as the reference (6 pages; the same file is also in `manuscript/main.pdf`).
3. **Numbers changed during the final audit.** If you have older slides or notes, update: HBM is now **3.0 M stacks / 5.00 %** (was 4.0 M / 6.67 %); Table II Low/High wafer columns were corrected; the "280,000 households", "26-month wait", "Chennai", "GDP $120 B" and "Stargate" statements were removed.
4. **Before presenting, open the source PDFs in `sources/`** for the denominators (TSMC wafers, CoWoS, HBM, India colocation) so that you can quote where they came from.
5. **Check the event's presentation rules** (time limit, slide count, template) with the organisers — the files in `docs/event_guidelines/` only cover the *paper* rules.

*End of guide.*
