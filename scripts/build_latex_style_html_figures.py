"""
Master LaTeX-Styled HTML Figures Generator
=========================================
Generates output/all_figures.html with an authentic LaTeX / IEEE publication feel:
- Times New Roman & STIX Two Text typography
- Real KaTeX mathematical typesetting
- Pure academic vector styling (TikZ and pgfplots aesthetics)
- Crisp black-and-white / grayscale line art with academic hatches
- LaTeX table styling (toprule, midrule, bottomrule)
- Authentic IEEE figure floats with horizontal rules and italicized captions
"""

import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIG_DIR = ROOT / "manuscript" / "figures"
OUT = ROOT / "output" / "all_figures.html"

def get_base64_img(filename):
    p = FIG_DIR / filename
    if p.exists():
        data = p.read_bytes()
        return "data:image/png;base64," + base64.b64encode(data).decode("ascii")
    return ""

img_fig1 = get_base64_img("fig1_demand_cascade_architecture.png")
img_fig2 = get_base64_img("fig2_structural_chokepoint_inversion.png")
img_fig3 = get_base64_img("fig3_country_comparison_benchmark.png")
img_fig4 = get_base64_img("fig4_cooling_water_energy_pareto.png")
img_fig5 = get_base64_img("fig5_sensitivity_tornado_montecarlo.png")

template = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>IEEE Format Figures &amp; Demand-Cascade Model Architecture</title>

<!-- Authentic LaTeX & Academic Typography from Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=STIX+Two+Text:ital,wght@0,400;0,600;0,700;1,400;1,600;1,700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">

<!-- KaTeX for exact LaTeX math equations -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
        onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>

<style>
  :root {
    --font-roman: "STIX Two Text", "Nimbus Roman No9 L", "Times New Roman", Times, serif;
    --font-mono: "JetBrains Mono", "Courier New", Courier, monospace;
    --ink: #000000;
    --charcoal: #222222;
    --dark-grey: #444444;
    --mid-grey: #777777;
    --light-grey: #dddddd;
    --paper-bg: #ffffff;
    --page-bg: #ecefe6;
    --rule-heavy: 1.5px solid #000000;
    --rule-mid: 0.75px solid #000000;
    --rule-thin: 0.5px solid #333333;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background-color: var(--page-bg);
    color: var(--ink);
    font-family: var(--font-roman);
    font-size: 10pt;
    line-height: 1.45;
    padding: 30px 15px;
    -webkit-font-smoothing: antialiased;
  }

  /* Toolbar */
  .toolbar {
    max-width: 900px;
    margin: 0 auto 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #ffffff;
    padding: 8px 16px;
    border: 1px solid #b8bec5;
    border-radius: 4px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    font-family: var(--font-roman);
  }
  .toolbar-title {
    font-size: 0.95rem;
    font-weight: 700;
    letter-spacing: 0.02em;
  }
  .toolbar-links {
    display: flex;
    gap: 8px;
  }
  .toolbar-btn {
    background: #f4f4f4;
    border: 1px solid #999;
    padding: 3px 10px;
    font-family: var(--font-roman);
    font-size: 0.85rem;
    color: #000;
    cursor: pointer;
    text-decoration: none;
    border-radius: 3px;
  }
  .toolbar-btn:hover {
    background: #e5e5e5;
  }

  /* Authentic LaTeX A4 / Letter Paper Sheet */
  .latex-sheet {
    max-width: 900px;
    margin: 0 auto;
    background: var(--paper-bg);
    padding: 45px 55px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.12);
    border: 1px solid #d0d0d0;
  }

  /* LaTeX Header */
  .ieee-journal-header {
    text-align: center;
    font-size: 7.5pt;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #333;
    margin-bottom: 24px;
    border-bottom: 0.5px solid #555;
    padding-bottom: 6px;
  }

  .paper-title {
    text-align: center;
    font-size: 18pt;
    font-weight: 700;
    line-height: 1.25;
    margin-bottom: 18px;
    color: #000;
  }

  .paper-authors-block {
    display: flex;
    justify-content: space-around;
    text-align: center;
    margin-bottom: 22px;
  }
  .author-col {
    flex: 1;
    max-width: 48%;
  }
  .author-name {
    font-size: 11pt;
    font-weight: 400;
    color: #000;
  }
  .author-dept {
    font-size: 10pt;
    font-style: italic;
  }
  .author-inst {
    font-size: 10pt;
  }
  .author-email {
    font-size: 9.5pt;
    font-family: var(--font-roman);
    margin-top: 2px;
  }

  /* Abstract Box */
  .abstract-box {
    margin: 0 auto 28px;
    padding: 10px 0 14px;
    border-top: var(--rule-thin);
    border-bottom: var(--rule-thin);
    text-align: justify;
    font-size: 9pt;
    line-height: 1.38;
  }
  .abstract-heading {
    font-weight: 700;
    font-style: italic;
  }
  .index-terms {
    margin-top: 6px;
  }
  .index-terms-heading {
    font-weight: 700;
    font-style: italic;
  }

  /* Figure Float Container */
  .latex-figure-float {
    margin: 36px 0;
    page-break-inside: avoid;
  }
  .figure-rule-top {
    border: none;
    border-top: var(--rule-mid);
    margin-bottom: 12px;
  }
  .figure-rule-bottom {
    border: none;
    border-top: var(--rule-mid);
    margin-top: 10px;
    margin-bottom: 14px;
  }

  .figure-header-tag {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 8pt;
    font-family: var(--font-mono);
    color: #555;
    margin-bottom: 8px;
  }
  .view-toggle-link {
    color: #0056b3;
    cursor: pointer;
    text-decoration: underline;
    font-family: var(--font-roman);
    font-size: 8.5pt;
  }

  /* The Pure LaTeX / TikZ Visual Canvas */
  .tikz-canvas {
    width: 100%;
    background: #ffffff;
    padding: 10px 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  /* LaTeX TikZ Node Box */
  .tikz-node {
    border: 1px solid #000000;
    background: #ffffff;
    border-radius: 2px;
    padding: 10px 14px;
    font-family: var(--font-roman);
  }
  .tikz-node-title {
    font-size: 9pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    border-bottom: 0.5px solid #000;
    padding-bottom: 3px;
    margin-bottom: 6px;
    display: flex;
    justify-content: space-between;
  }
  .tikz-node-body {
    font-size: 8.5pt;
    line-height: 1.35;
  }

  /* Caption */
  .latex-caption {
    font-size: 8.5pt;
    text-align: justify;
    line-height: 1.35;
    padding: 0 4px;
  }
  .latex-caption strong {
    font-weight: 700;
  }

  /* LaTeX Tables (Booktabs style) */
  .booktabs-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 8.5pt;
    margin: 12px 0 6px;
    text-align: left;
  }
  .booktabs-table thead tr:first-child {
    border-top: var(--rule-heavy);
  }
  .booktabs-table thead tr:last-child {
    border-bottom: var(--rule-mid);
  }
  .booktabs-table tbody tr:last-child {
    border-bottom: var(--rule-heavy);
  }
  .booktabs-table th, .booktabs-table td {
    padding: 5px 8px;
  }
  .booktabs-table th {
    font-weight: 700;
    font-size: 8pt;
    text-transform: uppercase;
  }

  /* SVG Graphics Styling */
  svg text {
    font-family: var(--font-roman) !important;
  }

  @media print {
    body { background: #fff; padding: 0; }
    .toolbar { display: none; }
    .latex-sheet { box-shadow: none; border: none; padding: 0; max-width: 100%; }
  }
</style>
</head>
<body>

<div class="toolbar">
  <div class="toolbar-title">ResearchThon 2026 &bull; LaTeX Paper Figures Appendix</div>
  <div class="toolbar-links">
    <a href="#fig1" class="toolbar-btn">Fig. 1</a>
    <a href="#fig2" class="toolbar-btn">Fig. 2</a>
    <a href="#fig3" class="toolbar-btn">Fig. 3</a>
    <a href="#fig4" class="toolbar-btn">Fig. 4</a>
    <a href="#fig5" class="toolbar-btn">Fig. 5</a>
    <button onclick="window.print()" class="toolbar-btn">Print / Export PDF</button>
  </div>
</div>

<div class="latex-sheet">

  <div class="ieee-journal-header">
    AMITY RESEARCH-O-THON 2026 &mdash; IEEE TRANSACTIONS &amp; CONFERENCE PROCEEDINGS FORMAT
  </div>

  <h1 class="paper-title">Sovereign by Design: An Integrated Five-Pillar Framework for India's Strategic Compute and Artificial Intelligence Infrastructure</h1>

  <div class="paper-authors-block">
    <div class="author-col">
      <div class="author-name">Parikshit Singh Bais, Adarsh Singh</div>
      <div class="author-dept">dept. of Computer Science and Engineering</div>
      <div class="author-inst">Amity School of Engineering and Technology</div>
      <div class="author-inst">Amity University Madhya Pradesh, Gwalior, India</div>
      <div class="author-email">e-mail: {parikshit.bais, adarsh.singh}@amity.edu</div>
    </div>
    <div class="author-col">
      <div class="author-name">Sourav, Anamidhi Shrivastava</div>
      <div class="author-dept">dept. of Computer Science and Engineering</div>
      <div class="author-inst">Amity School of Engineering and Technology</div>
      <div class="author-inst">Amity University Madhya Pradesh, Gwalior, India</div>
      <div class="author-email">e-mail: {sourav, anamidhi.shrivastava}@amity.edu</div>
    </div>
  </div>

  <div class="abstract-box">
    <span class="abstract-heading">Abstract&mdash;</span>National artificial intelligence sovereignty requires co-optimizing physical, microelectronic, and institutional infrastructure. Prevailing policy treats compute, power grids, data centres, connectivity, and governance in isolation, creating capital misallocations and grid vulnerabilities. This paper introduces the India AI Infrastructure Readiness Framework (IAIRF 2.0) and an auditable six-layer Demand-Cascade Model (DCM) parameterised using verified 2026 regulatory telemetry and foundry audits. Propagating national deployment targets bottom-up, our empirical analysis reveals four core findings. First, deploying 500,000 accelerators demands 891.8 MW of peak facility power, absorbing over half of India's operational colocation capacity. Second, the assumption that domestic sub-5 nm wafer fabrication is the binding constraint is refuted: required logic wafer starts consume merely 1.60% of global foundry capacity, whereas CoWoS advanced packaging consumes 7.41%&mdash;a 4.6-fold higher constraint intensity. Third, direct-to-chip liquid cooling slashes evaporative water withdrawal by 94.6% (saving 11 billion litres annually) and reduces facility power by 172 MW in tropical climates. Fourth, Mumbai's 52.4% capacity concentration and 20&ndash;40% dynamic AI load swings threaten transmission stability. We present a sequenced three-tier roadmap prioritising transmission corridors, packaging partnerships, and regional dispersion over premature leading-edge foundries.
    <div class="index-terms">
      <span class="index-terms-heading">Index Terms&mdash;</span>Advanced packaging, Artificial intelligence, Compute sovereignty, Data centre cooling, High-bandwidth memory, Power grid infrastructure.
    </div>
  </div>


  <!-- ==================== FIGURE 1 ==================== -->
  <div class="latex-figure-float" id="fig1">
    <hr class="figure-rule-top" />
    <div class="figure-header-tag">
      <span>TIKZ MODEL: DCM-6-TIER-FLOW</span>
      <span class="view-toggle-link" onclick="toggleView('f1')">Toggle Camera-Ready Vector View</span>
    </div>

    <!-- TikZ Native HTML/SVG Figure -->
    <div class="tikz-canvas" id="f1-tikz">
      <div style="width: 100%; max-width: 780px; display: flex; flex-direction: column; gap: 8px;">
        
        <!-- Tier 1 -->
        <div class="tikz-node">
          <div class="tikz-node-title">
            <span>Tier 1: Sovereign Policy Targets</span>
            <span style="font-family: var(--font-mono); font-weight: 400;">[$\mathcal{T}_1$]</span>
          </div>
          <div class="tikz-node-body">
            Target Deployment: $N_{\mathrm{acc}} = 500{,}000$ high-bandwidth accelerators (2030 Sovereign AI Plan) &bull; 
            Fiscal Outlays: Semicon India 2.0 (&#8377;1,27,500 cr) $\cdot$ IndiaAI (&#8377;10,372 cr / $1.25B) &bull; 
            Empaneled Compute: $45{,}000+$ GPUs live at &#8377;65/hr (~$0.72/hr, 60&ndash;72% subsidy)
          </div>
        </div>

        <div style="text-align: center; font-size: 8pt; color: #444; line-height: 1;">
          $\boldsymbol{\downarrow}$ <em>Algorithmic FLOP &amp; Parameter Sizing ($C = 6PD$)</em>
        </div>

        <!-- Tier 2 -->
        <div class="tikz-node">
          <div class="tikz-node-title">
            <span>Tier 2: Algorithmic Compute Sizing</span>
            <span style="font-family: var(--font-mono); font-weight: 400;">[$\mathcal{T}_2$]</span>
          </div>
          <div class="tikz-node-body">
            Target Stock: $245.0\text{ ExaFLOPS}$ FP16/BF16 tensor performance &bull; 
            Indigenous Foundation Models: Param-1 (2.9B parameters, 7.5T tokens, DST NM-ICPS) $\cdot$ Sarvam 30B/105B &bull; 
            Memory Subsystem: KV-cache footprint &amp; tensor parallel interconnects
          </div>
        </div>

        <div style="text-align: center; font-size: 8pt; color: #444; line-height: 1;">
          $\boldsymbol{\downarrow}$ <em>Server Chassis Architecture &amp; Silicon Aggregation</em>
        </div>

        <!-- Tier 3 -->
        <div class="tikz-node">
          <div class="tikz-node-title">
            <span>Tier 3: Server Physics &amp; Aggregation</span>
            <span style="font-family: var(--font-mono); font-weight: 400;">[$\mathcal{T}_3$]</span>
          </div>
          <div class="tikz-node-body">
            Node Geometry: $62{,}500$ 8-way SXM/NVLink server chassis &bull; 
            Unit Power: $10.20\text{ kW}$ per chassis ($8\times 700\text{ W}$ accelerator TDP + CPUs &amp; optics) &bull; 
            Peak Cluster IT Load: $P_{\mathrm{IT}} = 637.50\text{ MW}$
          </div>
        </div>

        <div style="text-align: center; font-size: 8pt; color: #444; line-height: 1;">
          $\boldsymbol{\downarrow}$ <em>Facility Thermodynamics &amp; Tropical Heat Rejection</em>
        </div>

        <!-- Tier 4 -->
        <div class="tikz-node">
          <div class="tikz-node-title">
            <span>Tier 4: Thermal Engineering &amp; Cooling</span>
            <span style="font-family: var(--font-mono); font-weight: 400;">[$\mathcal{T}_4$]</span>
          </div>
          <div class="tikz-node-body">
            Cooling Standard: Direct-to-Chip (D2C) liquid cooling with dry coolers (rated $\mathrm{PUE} = 1.25$) &bull; 
            Peak Facility Power: $P_{\mathrm{facility}} = 891.80\text{ MW}$ ($172.0\text{ MW}$ savings vs. evaporative air $\mathrm{PUE} = 1.45$) &bull; 
            Water Withdrawal: $630.9\text{ ML/yr}$ ($94.6\%$ reduction saving $11.02\text{ billion litres/yr}$)
          </div>
        </div>

        <div style="text-align: center; font-size: 8pt; color: #444; line-height: 1;">
          $\boldsymbol{\swarrow}$ <em>Microelectronic Value Chain</em> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\boldsymbol{\searrow}$ <em>Grid Transmission Interconnection</em>
        </div>

        <!-- Tiers 5 & 6 -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
          <div class="tikz-node">
            <div class="tikz-node-title">
              <span>Tier 5: Supply Chain</span>
              <span style="font-family: var(--font-mono); font-weight: 400;">[$\mathcal{T}_5$]</span>
            </div>
            <div class="tikz-node-body">
              Logic Wafers: $12{,}500$ starts ($1.60\%$ TSMC sub-5nm capacity) via Murphy yield &bull; 
              Packaging: $33{,}334$ CoWoS wafers ($7.41\%$ TSMC output, $\mathrm{HHI} = 8{,}100$) &bull; 
              Memory: $4{,}000{,}000$ HBM3e stacks ($6.67\%$ global triopoly)
            </div>
          </div>

          <div class="tikz-node">
            <div class="tikz-node-title">
              <span>Tier 6: Grid &amp; Transmission</span>
              <span style="font-family: var(--font-mono); font-weight: 400;">[$\mathcal{T}_6$]</span>
            </div>
            <div class="tikz-node-body">
              Colocation Share: $56.62\%$ of mid-2026 domestic operational capacity ($891.8\text{ MW} / 1{,}575\text{ MW}$) &bull; 
              Metropolitan Risk: Mumbai $52.4\%$ ($467.3\text{ MW}$) &bull; 
              Interconnection: $18\times 50\text{ MW}$ substations @ $400/220\text{ kV}$
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- Camera-Ready Image View (hidden by default) -->
    <div id="f1-camera" style="display: none; text-align: center;">
      <img src="{{IMG_FIG1}}" style="max-width: 100%; height: auto;" alt="Fig. 1" />
    </div>

    <hr class="figure-rule-bottom" />
    <div class="latex-caption">
      <strong>Fig. 1.</strong> The six-layer Demand-Cascade Model (DCM) architecture: tracing policy targets through algorithmic sizing, hardware aggregation, thermal engineering, semiconductor supply-chain allocation, and power grid constraints. The framework establishes continuous analytical causality between national policy ambitions and physical microelectronic/thermodynamic realities.
    </div>
  </div>


  <!-- ==================== FIGURE 2 ==================== -->
  <div class="latex-figure-float" id="fig2">
    <hr class="figure-rule-top" />
    <div class="figure-header-tag">
      <span>PGFPLOTS: STRUCTURAL-CHOKEPOINT-INVERSION</span>
      <span class="view-toggle-link" onclick="toggleView('f2')">Toggle Camera-Ready Vector View</span>
    </div>

    <!-- Pgfplots Native SVG Bar Chart -->
    <div class="tikz-canvas" id="f2-tikz">
      <svg viewBox="0 0 760 210" style="width: 100%; max-width: 760px; height: auto;">
        <!-- Axes -->
        <line x1="280" y1="20" x2="280" y2="175" stroke="#000" stroke-width="1" />
        <line x1="280" y1="175" x2="720" y2="175" stroke="#000" stroke-width="1" />
        
        <!-- Gridlines -->
        <line x1="353" y1="20" x2="353" y2="175" stroke="#ccc" stroke-dasharray="2,2" stroke-width="0.5" />
        <line x1="426" y1="20" x2="426" y2="175" stroke="#ccc" stroke-dasharray="2,2" stroke-width="0.5" />
        <line x1="500" y1="20" x2="500" y2="175" stroke="#ccc" stroke-dasharray="2,2" stroke-width="0.5" />
        <line x1="573" y1="20" x2="573" y2="175" stroke="#ccc" stroke-dasharray="2,2" stroke-width="0.5" />
        <line x1="646" y1="20" x2="646" y2="175" stroke="#ccc" stroke-dasharray="2,2" stroke-width="0.5" />
        <line x1="720" y1="20" x2="720" y2="175" stroke="#ccc" stroke-dasharray="2,2" stroke-width="0.5" />

        <!-- X ticks -->
        <text x="280" y="190" font-size="9" text-anchor="middle">0%</text>
        <text x="353" y="190" font-size="9" text-anchor="middle">10%</text>
        <text x="426" y="190" font-size="9" text-anchor="middle">20%</text>
        <text x="500" y="190" font-size="9" text-anchor="middle">30%</text>
        <text x="573" y="190" font-size="9" text-anchor="middle">40%</text>
        <text x="646" y="190" font-size="9" text-anchor="middle">50%</text>
        <text x="720" y="190" font-size="9" text-anchor="middle">60%</text>
        <text x="500" y="205" font-size="9.5" text-anchor="middle" font-style="italic">Required share of constrained capacity (%)</text>

        <!-- Bar 1: Wafer Starts (1.60%) -->
        <text x="270" y="44" font-size="9.5" text-anchor="end">Wafer starts: TSMC sub-5nm share</text>
        <rect x="280" y="32" width="12" height="18" fill="#dddddd" stroke="#000" stroke-width="0.75" />
        <text x="300" y="45" font-size="9" font-weight="700">1.60%</text>

        <!-- Bar 2: HBM3e (6.67%) -->
        <text x="270" y="74" font-size="9.5" text-anchor="end">HBM3e: Global output share</text>
        <rect x="280" y="62" width="49" height="18" fill="#aaaaaa" stroke="#000" stroke-width="0.75" />
        <text x="337" y="75" font-size="9" font-weight="700">6.67%</text>

        <!-- Bar 3: CoWoS (7.41%) -->
        <text x="270" y="104" font-size="9.5" text-anchor="end" font-weight="700">CoWoS: Global capacity share (4.6x chokepoint)</text>
        <rect x="280" y="92" width="54" height="18" fill="#555555" stroke="#000" stroke-width="1" />
        <text x="342" y="105" font-size="9" font-weight="700">7.41%</text>

        <!-- Bar 4: Colocation Power 2030 (27.9%) -->
        <text x="270" y="134" font-size="9.5" text-anchor="end">Colocation power: 2030 pipeline</text>
        <rect x="280" y="122" width="205" height="18" fill="#888888" stroke="#000" stroke-width="0.75" />
        <text x="493" y="135" font-size="9" font-weight="700">27.90%</text>

        <!-- Bar 5: Colocation Power mid-2026 (56.62%) -->
        <text x="270" y="164" font-size="9.5" text-anchor="end" font-weight="700">Colocation power: mid-2026 operational</text>
        <rect x="280" y="152" width="415" height="18" fill="#222222" stroke="#000" stroke-width="1" />
        <text x="702" y="165" font-size="9" font-weight="700" fill="#fff" text-anchor="end">56.62%</text>
      </svg>
    </div>

    <div id="f2-camera" style="display: none; text-align: center;">
      <img src="{{IMG_FIG2}}" style="max-width: 100%; height: auto;" alt="Fig. 2" />
    </div>

    <hr class="figure-rule-bottom" />
    <div class="latex-caption">
      <strong>Fig. 2.</strong> The structural chokepoint inversion (500,000-GPU baseline): required share of global advanced packaging (7.41%) and domestic colocation power (56.62%) far outstrips raw logic wafer requirements (1.60%). This refutes the prevailing policy premise that domestic sub-3nm wafer fabrication is India's primary bottleneck.
    </div>

    <!-- LaTeX Booktabs Telemetry Table -->
    <table class="booktabs-table">
      <thead>
        <tr>
          <th>Constrained Strategic Subsystem</th>
          <th>National 500k Requirement</th>
          <th>Global / Domestic Denominator</th>
          <th>Required Absorption Share</th>
          <th>HHI Concentration</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>TSMC Sub-5nm Wafer Starts</td>
          <td>12,500 logic wafers/yr</td>
          <td>780,000 wafers/yr (global)</td>
          <td><strong>1.60%</strong></td>
          <td>5,600 (Duopoly)</td>
        </tr>
        <tr>
          <td>CoWoS Advanced Packaging</td>
          <td>33,334 interposer wafers/yr</td>
          <td>450,000 wafers/yr (global)</td>
          <td><strong>7.41%</strong> (4.6x inversion)</td>
          <td>8,100 (Monopoly)</td>
        </tr>
        <tr>
          <td>HBM3e High-Bandwidth Memory</td>
          <td>4,000,000 8-Hi stacks</td>
          <td>60,000,000 stacks/yr (global)</td>
          <td><strong>6.67%</strong></td>
          <td>4,200 (Triopoly)</td>
        </tr>
        <tr>
          <td>Operational Colocation Power</td>
          <td>891.80 MW facility draw</td>
          <td>1,575 MW (mid-2026 operational)</td>
          <td><strong>56.62%</strong></td>
          <td>Regional: Mumbai 52.4%</td>
        </tr>
      </tbody>
    </table>
  </div>


  <!-- ==================== FIGURE 3 ==================== -->
  <div class="latex-figure-float" id="fig3">
    <hr class="figure-rule-top" />
    <div class="figure-header-tag">
      <span>PGFPLOTS: COUNTRY-BENCHMARK-DUAL-PANEL</span>
      <span class="view-toggle-link" onclick="toggleView('f3')">Toggle Camera-Ready Vector View</span>
    </div>

    <!-- Pgfplots Dual Panel SVG -->
    <div class="tikz-canvas" id="f3-tikz">
      <svg viewBox="0 0 760 210" style="width: 100%; max-width: 760px; height: auto;">
        <!-- Panel A: Compute Stock -->
        <text x="180" y="16" font-size="9.5" font-weight="700" text-anchor="middle">(a) Accelerated compute stock (EFLOPS FP16 eq.)</text>
        <line x1="50" y1="30" x2="50" y2="170" stroke="#000" stroke-width="0.8" />
        <line x1="50" y1="170" x2="350" y2="170" stroke="#000" stroke-width="0.8" />
        
        <!-- Y grid -->
        <text x="42" y="173" font-size="8" text-anchor="end">0</text>
        <text x="42" y="128" font-size="8" text-anchor="end">400</text>
        <line x1="50" y1="125" x2="350" y2="125" stroke="#eee" stroke-width="0.5" />
        <text x="42" y="83" font-size="8" text-anchor="end">800</text>
        <line x1="50" y1="80" x2="350" y2="80" stroke="#eee" stroke-width="0.5" />
        <text x="42" y="38" font-size="8" text-anchor="end">1200</text>
        <line x1="50" y1="35" x2="350" y2="35" stroke="#eee" stroke-width="0.5" />

        <!-- Bars -->
        <!-- US: 1200 -->
        <rect x="75" y="35" width="45" height="135" fill="#111111" stroke="#000" stroke-width="0.75" />
        <text x="97" y="28" font-size="8.5" text-anchor="middle" font-weight="700">1,200</text>
        <text x="97" y="184" font-size="8.5" text-anchor="middle">US</text>

        <!-- China: 450 -->
        <rect x="145" y="119" width="45" height="51" fill="#555555" stroke="#000" stroke-width="0.75" />
        <text x="167" y="112" font-size="8.5" text-anchor="middle" font-weight="700">450</text>
        <text x="167" y="184" font-size="8.5" text-anchor="middle">China</text>

        <!-- India Plan: 245 -->
        <rect x="215" y="142" width="45" height="28" fill="#aaaaaa" stroke="#000" stroke-width="0.75" />
        <text x="237" y="136" font-size="8.5" text-anchor="middle" font-weight="700">245</text>
        <text x="237" y="184" font-size="8" text-anchor="middle">India 500k</text>

        <!-- India Now: 35 -->
        <rect x="285" y="166" width="45" height="4" fill="#ffffff" stroke="#000" stroke-width="0.75" />
        <text x="307" y="160" font-size="8.5" text-anchor="middle" font-weight="700">35</text>
        <text x="307" y="184" font-size="8" text-anchor="middle">India Now</text>


        <!-- Panel B: Self-Sufficiency Tiers -->
        <text x="560" y="16" font-size="9.5" font-weight="700" text-anchor="middle">(b) Microelectronic self-sufficiency (%)</text>
        <line x1="420" y1="30" x2="420" y2="170" stroke="#000" stroke-width="0.8" />
        <line x1="420" y1="170" x2="740" y2="170" stroke="#000" stroke-width="0.8" />

        <text x="412" y="173" font-size="8" text-anchor="end">0%</text>
        <text x="412" y="103" font-size="8" text-anchor="end">50%</text>
        <line x1="420" y1="100" x2="740" y2="100" stroke="#eee" stroke-width="0.5" />
        <text x="412" y="33" font-size="8" text-anchor="end">100%</text>
        <line x1="420" y1="30" x2="740" y2="30" stroke="#eee" stroke-width="0.5" />

        <!-- Legend -->
        <rect x="620" y="34" width="10" height="8" fill="#111" />
        <text x="634" y="41" font-size="7.5">US</text>
        <rect x="660" y="34" width="10" height="8" fill="#666" />
        <text x="674" y="41" font-size="7.5">China</text>
        <rect x="705" y="34" width="10" height="8" fill="#ccc" stroke="#000" stroke-width="0.5" />
        <text x="719" y="41" font-size="7.5">India</text>

        <!-- Sub-5nm -->
        <rect x="440" y="163" width="14" height="7" fill="#111" />
        <rect x="456" y="167" width="14" height="3" fill="#666" />
        <rect x="472" y="169.5" width="14" height="0.5" fill="#ccc" stroke="#000" stroke-width="0.5" />
        <text x="463" y="184" font-size="7.5" text-anchor="middle">Sub-5nm</text>

        <!-- Packaging -->
        <rect x="515" y="163" width="14" height="7" fill="#111" />
        <rect x="531" y="166" width="14" height="4" fill="#666" />
        <rect x="547" y="169.5" width="14" height="0.5" fill="#ccc" stroke="#000" stroke-width="0.5" />
        <text x="538" y="184" font-size="7.5" text-anchor="middle">CoWoS Pkg</text>

        <!-- Design -->
        <rect x="590" y="51" width="14" height="119" fill="#111" />
        <rect x="606" y="142" width="14" height="28" fill="#666" />
        <rect x="622" y="142" width="14" height="28" fill="#ccc" stroke="#000" stroke-width="0.5" />
        <text x="613" y="184" font-size="7.5" text-anchor="middle">Design</text>

        <!-- Gallium -->
        <rect x="665" y="169.5" width="14" height="0.5" fill="#111" />
        <rect x="681" y="31" width="14" height="139" fill="#666" />
        <rect x="697" y="169" width="14" height="1" fill="#ccc" stroke="#000" stroke-width="0.5" />
        <text x="688" y="184" font-size="7.5" text-anchor="middle">Gallium</text>
      </svg>
    </div>

    <div id="f3-camera" style="display: none; text-align: center;">
      <img src="{{IMG_FIG3}}" style="max-width: 100%; height: auto;" alt="Fig. 3" />
    </div>

    <hr class="figure-rule-bottom" />
    <div class="latex-caption">
      <strong>Fig. 3.</strong> Cross-national comparative benchmark between the United States, China, and India across accelerated compute stock in ExaFLOPS (Panel A) and microelectronic supply chain self-sufficiency across four strategic tiers (Panel B). Illustrates the structural "N-2 asymmetry" confronting non-superpower states in attempting autarkic replication.
    </div>
  </div>


  <!-- ==================== FIGURE 4 ==================== -->
  <div class="latex-figure-float" id="fig4">
    <hr class="figure-rule-top" />
    <div class="figure-header-tag">
      <span>PGFPLOTS: COOLING-PARETO-FRONTIER</span>
      <span class="view-toggle-link" onclick="toggleView('f4')">Toggle Camera-Ready Vector View</span>
    </div>

    <!-- Pgfplots Pareto Scatter & Curve SVG -->
    <div class="tikz-canvas" id="f4-tikz">
      <svg viewBox="0 0 760 220" style="width: 100%; max-width: 760px; height: auto;">
        <!-- Axes -->
        <line x1="160" y1="20" x2="160" y2="180" stroke="#000" stroke-width="1" />
        <line x1="160" y1="180" x2="700" y2="180" stroke="#000" stroke-width="1" />

        <!-- Gridlines -->
        <line x1="160" y1="151" x2="700" y2="151" stroke="#e0e0e0" stroke-dasharray="2,2" stroke-width="0.5" />
        <line x1="160" y1="122" x2="700" y2="122" stroke="#e0e0e0" stroke-dasharray="2,2" stroke-width="0.5" />
        <line x1="160" y1="93" x2="700" y2="93" stroke="#e0e0e0" stroke-dasharray="2,2" stroke-width="0.5" />
        <line x1="160" y1="64" x2="700" y2="64" stroke="#e0e0e0" stroke-dasharray="2,2" stroke-width="0.5" />
        <line x1="160" y1="35" x2="700" y2="35" stroke="#e0e0e0" stroke-dasharray="2,2" stroke-width="0.5" />

        <!-- Y labels -->
        <text x="150" y="184" font-size="9" text-anchor="end">1.10</text>
        <text x="150" y="155" font-size="9" text-anchor="end">1.20</text>
        <text x="150" y="126" font-size="9" text-anchor="end">1.30</text>
        <text x="150" y="97" font-size="9" text-anchor="end">1.40</text>
        <text x="150" y="68" font-size="9" text-anchor="end">1.50</text>
        <text x="150" y="39" font-size="9" text-anchor="end">1.60</text>
        <text x="100" y="105" font-size="9.5" text-anchor="middle" font-style="italic" transform="rotate(-90 100 105)">Annual Facility PUE</text>

        <!-- X ticks -->
        <text x="160" y="196" font-size="9" text-anchor="middle">0.0</text>
        <text x="295" y="196" font-size="9" text-anchor="middle">0.5</text>
        <text x="430" y="196" font-size="9" text-anchor="middle">1.0</text>
        <text x="565" y="196" font-size="9" text-anchor="middle">1.5</text>
        <text x="700" y="196" font-size="9" text-anchor="middle">2.0</text>
        <text x="430" y="212" font-size="9.5" text-anchor="middle" font-style="italic">Cooling Water Intensity (WUE, L/kWh)</text>

        <!-- Pareto curve -->
        <path d="M 168 174.2 L 192.4 156.8 L 430 107.5 L 646 78.5" fill="none" stroke="#555" stroke-width="1.2" stroke-dasharray="4,3" />

        <!-- Shaded Pareto Area -->
        <polygon points="168,174.2 192.4,156.8 430,107.5 646,78.5 646,180 168,180" fill="#f0f0f0" opacity="0.6" />

        <!-- Markers -->
        <!-- Immersion: (168, 174) Diamond -->
        <polygon points="168,169 173,174 168,179 163,174" fill="#ffffff" stroke="#000" stroke-width="1.2" />
        <text x="180" y="174" font-size="8.5">Immersion (0.03, 1.12)</text>

        <!-- D2C Liquid: (192.4, 156.8) Triangle -->
        <polygon points="192.4,151 197.4,160 187.4,160" fill="#222" stroke="#000" stroke-width="1.2" />
        <text x="206" y="152" font-size="9" font-weight="700">D2C Liquid (0.12, 1.18) &mdash; Optimal</text>

        <!-- RDHx: (430, 107.5) Square -->
        <rect x="425" y="102.5" width="10" height="10" fill="#777" stroke="#000" stroke-width="1" />
        <text x="444" y="110" font-size="8.5">Rear-Door HEX (1.00, 1.35)</text>

        <!-- Air: (646, 78.5) Circle -->
        <circle cx="646" cy="78.5" r="5" fill="#ffffff" stroke="#000" stroke-width="1.5" />
        <text x="635" y="66" font-size="8.5" text-anchor="end">Traditional Evaporative Air (1.80, 1.45)</text>

        <!-- Annotations -->
        <line x1="620" y1="70" x2="570" y2="45" stroke="#000" stroke-width="0.6" />
        <text x="565" y="42" font-size="8" text-anchor="end">Summer humidity spike (+0.12 PUE)</text>

        <line x1="260" y1="140" x2="310" y2="135" stroke="#000" stroke-width="0.6" />
        <text x="316" y="138" font-size="8" font-weight="700">Saves 11 Billion Litres / Year (94.6%)</text>
      </svg>
    </div>

    <div id="f4-camera" style="display: none; text-align: center;">
      <img src="{{IMG_FIG4}}" style="max-width: 100%; height: auto;" alt="Fig. 4" />
    </div>

    <hr class="figure-rule-bottom" />
    <div class="latex-caption">
      <strong>Fig. 4.</strong> Cooling technology water-energy Pareto frontier across Indian tropical ambient profiles: Direct-to-Chip (D2C) liquid cooling achieves the optimal trade-off between power efficiency and water conservation, eliminating 11.02 billion litres/year of evaporative losses and cutting facility power by 172 MW compared to conventional evaporative air systems.
    </div>

    <!-- LaTeX Booktabs Table -->
    <table class="booktabs-table">
      <thead>
        <tr>
          <th>Cooling Architecture</th>
          <th>Annual Facility PUE</th>
          <th>Cooling WUE (L/kWh)</th>
          <th>Peak Facility Power (MW)</th>
          <th>Annual Water Loss (ML/yr)</th>
          <th>Summer Penalty</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Traditional Evaporative Air</td>
          <td>1.45</td>
          <td>1.80 L/kWh</td>
          <td>988.10 MW</td>
          <td>11,651.0 ML</td>
          <td>+0.12 PUE</td>
        </tr>
        <tr>
          <td>Rear-Door HEX (RDHx)</td>
          <td>1.35</td>
          <td>1.00 L/kWh</td>
          <td>920.00 MW</td>
          <td>6,447.0 ML</td>
          <td>+0.08 PUE</td>
        </tr>
        <tr>
          <td><strong>Direct-to-Chip Liquid (Optimal)</strong></td>
          <td><strong>1.25 Rated (1.18 base)</strong></td>
          <td><strong>0.12 L/kWh</strong></td>
          <td><strong>891.80 MW (-172 MW)</strong></td>
          <td><strong>630.9 ML (-94.6%)</strong></td>
          <td><strong>Minimal</strong></td>
        </tr>
        <tr>
          <td>Two-Phase Immersion</td>
          <td>1.12</td>
          <td>0.03 L/kWh</td>
          <td>761.60 MW</td>
          <td>150.0 ML</td>
          <td>Zero wet-bulb loss</td>
        </tr>
      </tbody>
    </table>
  </div>


  <!-- ==================== FIGURE 5 ==================== -->
  <div class="latex-figure-float" id="fig5">
    <hr class="figure-rule-top" />
    <div class="figure-header-tag">
      <span>PGFPLOTS: SENSITIVITY-TORNADO-OAT</span>
      <span class="view-toggle-link" onclick="toggleView('f5')">Toggle Camera-Ready Vector View</span>
    </div>

    <!-- Pgfplots Tornado SVG -->
    <div class="tikz-canvas" id="f5-tikz">
      <svg viewBox="0 0 760 210" style="width: 100%; max-width: 760px; height: auto;">
        <!-- Axes -->
        <line x1="430" y1="20" x2="430" y2="180" stroke="#000" stroke-width="1.2" />
        <line x1="170" y1="180" x2="700" y2="180" stroke="#000" stroke-width="1" />

        <!-- Grid ticks -->
        <line x1="170" y1="20" x2="170" y2="180" stroke="#eee" stroke-width="0.5" />
        <text x="170" y="194" font-size="8.5" text-anchor="middle">-100%</text>
        <line x1="235" y1="20" x2="235" y2="180" stroke="#eee" stroke-width="0.5" />
        <text x="235" y="194" font-size="8.5" text-anchor="middle">-75%</text>
        <line x1="300" y1="20" x2="300" y2="180" stroke="#eee" stroke-width="0.5" />
        <text x="300" y="194" font-size="8.5" text-anchor="middle">-50%</text>
        <line x1="365" y1="20" x2="365" y2="180" stroke="#eee" stroke-width="0.5" />
        <text x="365" y="194" font-size="8.5" text-anchor="middle">-25%</text>
        <text x="430" y="194" font-size="9" text-anchor="middle" font-weight="700">0%</text>
        <line x1="521" y1="20" x2="521" y2="180" stroke="#eee" stroke-width="0.5" />
        <text x="521" y="194" font-size="8.5" text-anchor="middle">+35%</text>
        <line x1="612" y1="20" x2="612" y2="180" stroke="#eee" stroke-width="0.5" />
        <text x="612" y="194" font-size="8.5" text-anchor="middle">+70%</text>
        <text x="430" y="208" font-size="9" text-anchor="middle" font-style="italic">Relative swing on peak facility power / resource consumption (%)</text>

        <!-- Legend -->
        <rect x="530" y="24" width="10" height="8" fill="#dddddd" stroke="#000" stroke-width="0.5" />
        <text x="544" y="31" font-size="7.5">Lower input bound ($-\Delta\%$)</text>
        <rect x="635" y="24" width="10" height="8" fill="#333333" />
        <text x="649" y="31" font-size="7.5">Upper input bound ($+\Delta\%$)</text>

        <!-- Row 1: PUE (1.25 to 1.55) -->
        <text x="160" y="48" font-size="8.5" text-anchor="end">Cooling PUE ($1.25 \rightarrow 1.55$)</text>
        <rect x="402" y="38" width="28" height="14" fill="#dddddd" stroke="#000" stroke-width="0.5" />
        <text x="396" y="49" font-size="7.5" text-anchor="end">-10.7%</text>
        <rect x="430" y="38" width="28" height="14" fill="#333333" />
        <text x="464" y="49" font-size="7.5" text-anchor="start">+10.7%</text>

        <!-- Row 2: Utilization (0.65 to 0.90) -->
        <text x="160" y="70" font-size="8.5" text-anchor="end">Compute utilization ($0.65 \rightarrow 0.90$)</text>
        <rect x="381" y="60" width="49" height="14" fill="#dddddd" stroke="#000" stroke-width="0.5" />
        <text x="375" y="71" font-size="7.5" text-anchor="end">-18.7%</text>
        <rect x="430" y="60" width="33" height="14" fill="#333333" />
        <text x="469" y="71" font-size="7.5" text-anchor="start">+12.5%</text>

        <!-- Row 3: Server overhead (1.6 to 2.1) -->
        <text x="160" y="92" font-size="8.5" text-anchor="end">Server overhead factor ($1.6 \rightarrow 2.1$)</text>
        <rect x="398" y="82" width="32" height="14" fill="#dddddd" stroke="#000" stroke-width="0.5" />
        <text x="392" y="93" font-size="7.5" text-anchor="end">-12.1%</text>
        <rect x="430" y="82" width="40" height="14" fill="#333333" />
        <text x="476" y="93" font-size="7.5" text-anchor="start">+15.4%</text>

        <!-- Row 4: Accelerator TDP (700W to 1,000W) -->
        <text x="160" y="114" font-size="8.5" text-anchor="end" font-weight="700">Accelerator TDP ($700\text{W} \rightarrow 1{,}000\text{W}$)</text>
        <rect x="391" y="104" width="39" height="14" fill="#dddddd" stroke="#000" stroke-width="0.5" />
        <text x="385" y="115" font-size="7.5" text-anchor="end">-15.0%</text>
        <rect x="430" y="104" width="111" height="14" fill="#111111" />
        <text x="547" y="115" font-size="7.5" text-anchor="start" font-weight="700">+42.8%</text>

        <!-- Row 5: Defect density D0 (0.06 to 0.12) -->
        <text x="160" y="136" font-size="8.5" text-anchor="end">Defect density $D_0$ ($0.06 \rightarrow 0.12\text{ cm}^{-2}$)</text>
        <rect x="401" y="126" width="29" height="14" fill="#dddddd" stroke="#000" stroke-width="0.5" />
        <text x="395" y="137" font-size="7.5" text-anchor="end">-11.1%</text>
        <rect x="430" y="126" width="100" height="14" fill="#333333" />
        <text x="536" y="137" font-size="7.5" text-anchor="start">+38.4%</text>

        <!-- Row 6: Cooling WUE (0.2 to 2.5 L/kWh) -->
        <text x="160" y="158" font-size="8.5" text-anchor="end" font-weight="700">Cooling WUE ($0.2 \rightarrow 2.5\text{ L/kWh}$)</text>
        <rect x="199" y="148" width="231" height="14" fill="#bbbbbb" stroke="#000" stroke-width="0.5" />
        <text x="193" y="159" font-size="7.5" text-anchor="end" font-weight="700">-88.9%</text>
        <rect x="430" y="148" width="101" height="14" fill="#111111" />
        <text x="537" y="159" font-size="7.5" text-anchor="start">+38.9%</text>
      </svg>
    </div>

    <div id="f5-camera" style="display: none; text-align: center;">
      <img src="{{IMG_FIG5}}" style="max-width: 100%; height: auto;" alt="Fig. 5" />
    </div>

    <hr class="figure-rule-bottom" />
    <div class="latex-caption">
      <strong>Fig. 5.</strong> One-at-a-time (OAT) parameter sensitivity tornado diagram (500,000-GPU deployment): relative percentage swing in peak facility power and resource consumption across empirical uncertainty bounds. Highlights that next-generation accelerator TDP (+42.8%) and cooling WUE variations (&minus;88.9% to +38.9%) exert dominant operational variance.
    </div>
  </div>

  <div style="text-align: center; font-size: 8pt; color: #555; margin-top: 36px; border-top: 0.5px solid #bbb; padding-top: 10px;">
    ResearchThon 2026 Proceedings &bull; IEEEtran Format Aligned &bull; Compiled from Authoritative LaTeX Model Pipeline
  </div>

</div>

<script>
  function toggleView(prefix) {
    const tikzEl = document.getElementById(prefix + '-tikz');
    const camEl = document.getElementById(prefix + '-camera');
    if (!tikzEl || !camEl) return;

    if (tikzEl.style.display === 'none') {
      tikzEl.style.display = 'flex';
      camEl.style.display = 'none';
    } else {
      tikzEl.style.display = 'none';
      camEl.style.display = 'block';
    }
  }
</script>

</body>
</html>
"""

# Replace image placeholders
html_doc = (
    template.replace("{{IMG_FIG1}}", img_fig1)
    .replace("{{IMG_FIG2}}", img_fig2)
    .replace("{{IMG_FIG3}}", img_fig3)
    .replace("{{IMG_FIG4}}", img_fig4)
    .replace("{{IMG_FIG5}}", img_fig5)
)

OUT.write_text(html_doc, encoding="utf-8")
print(f"Generated LaTeX-styled HTML figures: {OUT} ({OUT.stat().st_size // 1024} KB)")
