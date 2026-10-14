"""
Master HTML Builder for ResearchThon 2026 Academic Figures
=========================================================
Generates an ultra-aesthetic, publication-grade interactive explorer for all
5 figures used in the IEEE paper. Features:
  - Native HTML/CSS/SVG interactive figures with animated metrics
  - Real LaTeX Math typesetting via KaTeX
  - Dual Theme: Classic LaTeX Paper (Light) vs Midnight Quantum (Dark)
  - Toggle between Interactive Web View and Camera-Ready Matplotlib View
  - Deep-dive empirical breakdown cards, formulas, and policy takeaways
  - 100% self-contained standalone HTML (output/all_figures.html)
"""

from pathlib import Path
import base64

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

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Scientific Figures &amp; DCM Architecture — Sovereign by Design (ResearchThon 2026)</title>

<!-- Modern Academic Typography -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&family=STIX+Two+Text:ital,wght@0,400;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">

<!-- KaTeX for authentic LaTeX Math typesetting -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
        onload="renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}]}});"></script>

<style>
  :root {{
    --font-serif: "STIX Two Text", "Times New Roman", Times, Georgia, serif;
    --font-sans: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    --font-mono: "JetBrains Mono", Consolas, monospace;
    
    /* Light (LaTeX Academic Paper) Theme */
    --bg-page: #f8fafc;
    --bg-paper: #ffffff;
    --bg-card: #ffffff;
    --bg-subtle: #f1f5f9;
    --border-paper: #e2e8f0;
    --border-subtle: #cbd5e1;
    --border-accent: #2563eb;
    
    --text-primary: #0f172a;
    --text-secondary: #334155;
    --text-muted: #64748b;
    
    --accent-blue: #1d4ed8;
    --accent-blue-light: #eff6ff;
    --accent-teal: #0d9488;
    --accent-amber: #d97706;
    --accent-rose: #e11d48;
    --accent-purple: #7c3aed;
    
    --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
    --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.07), 0 2px 4px -2px rgba(0,0,0,0.04);
    --shadow-paper: 0 2px 4px rgba(0,0,0,0.04), 0 12px 24px -4px rgba(0,0,0,0.06);
    
    --radius-sm: 6px;
    --radius-md: 10px;
    --radius-lg: 14px;
  }}

  [data-theme="dark"] {{
    --bg-page: #0a0d14;
    --bg-paper: #111827;
    --bg-card: #151f32;
    --bg-subtle: #1e293b;
    --border-paper: #1e293b;
    --border-subtle: #334155;
    --border-accent: #3b82f6;
    
    --text-primary: #f8fafc;
    --text-secondary: #cbd5e1;
    --text-muted: #94a3b8;
    
    --accent-blue: #3b82f6;
    --accent-blue-light: #172554;
    --accent-teal: #14b8a6;
    --accent-amber: #f59e0b;
    --accent-rose: #f43f5e;
    --accent-purple: #a855f7;
    
    --shadow-sm: 0 1px 2px rgba(0,0,0,0.4);
    --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.5);
    --shadow-paper: 0 4px 20px rgba(0,0,0,0.6);
  }}

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}

  body {{
    background-color: var(--bg-page);
    color: var(--text-primary);
    font-family: var(--font-sans);
    line-height: 1.6;
    transition: background-color 0.25s ease, color 0.25s ease;
  }}

  /* Top Sticky Bar */
  .top-navbar {{
    position: sticky;
    top: 0;
    z-index: 100;
    background: var(--bg-paper);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--border-paper);
    padding: 12px 28px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: var(--shadow-sm);
  }}

  .nav-brand {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  .nav-badge {{
    background: var(--accent-blue-light);
    color: var(--accent-blue);
    font-size: 0.75rem;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 9999px;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    border: 1px solid rgba(37,99,235,0.25);
  }}
  .nav-title {{
    font-family: var(--font-serif);
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--text-primary);
  }}

  .nav-actions {{
    display: flex;
    align-items: center;
    gap: 14px;
  }}

  .nav-tabs {{
    display: flex;
    align-items: center;
    gap: 4px;
    background: var(--bg-subtle);
    padding: 4px;
    border-radius: var(--radius-md);
    border: 1px solid var(--border-subtle);
  }}
  .nav-tab-btn {{
    background: transparent;
    border: none;
    padding: 6px 14px;
    font-size: 0.82rem;
    font-weight: 600;
    color: var(--text-secondary);
    border-radius: var(--radius-sm);
    cursor: pointer;
    transition: all 0.15s ease;
    text-decoration: none;
  }}
  .nav-tab-btn:hover {{
    color: var(--text-primary);
  }}
  .nav-tab-btn.active {{
    background: var(--bg-paper);
    color: var(--accent-blue);
    box-shadow: var(--shadow-sm);
  }}

  .btn-action {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 7px 16px;
    font-size: 0.84rem;
    font-weight: 600;
    border-radius: var(--radius-md);
    border: 1px solid var(--border-subtle);
    background: var(--bg-card);
    color: var(--text-primary);
    cursor: pointer;
    transition: all 0.2s ease;
  }}
  .btn-action:hover {{
    border-color: var(--border-accent);
    color: var(--accent-blue);
  }}

  /* Main Container */
  .container {{
    max-width: 1060px;
    margin: 36px auto 100px;
    padding: 0 24px;
  }}

  /* Paper Header Card */
  .paper-header {{
    background: var(--bg-paper);
    border: 1px solid var(--border-paper);
    border-radius: var(--radius-lg);
    padding: 40px 48px;
    margin-bottom: 42px;
    box-shadow: var(--shadow-paper);
    position: relative;
    overflow: hidden;
  }}
  .paper-header::before {{
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 5px;
    background: linear-gradient(90deg, #1d4ed8, #0d9488, #7c3aed);
  }}
  .paper-conference-tag {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-family: var(--font-mono);
    font-size: 0.8rem;
    color: var(--accent-blue);
    margin-bottom: 16px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-weight: 700;
  }}
  .paper-title {{
    font-family: var(--font-serif);
    font-size: 2.1rem;
    font-weight: 700;
    line-height: 1.28;
    color: var(--text-primary);
    margin-bottom: 16px;
  }}
  .paper-subtitle {{
    font-family: var(--font-serif);
    font-size: 1.2rem;
    font-style: italic;
    color: var(--text-secondary);
    margin-bottom: 26px;
  }}
  
  .paper-authors {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 24px;
    padding-top: 22px;
    border-top: 1px solid var(--border-subtle);
    font-size: 0.9rem;
  }}
  .author-col {{
    line-height: 1.48;
  }}
  .author-names {{
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 4px;
  }}
  .author-dept {{
    font-style: italic;
    color: var(--text-secondary);
  }}
  .author-inst {{
    color: var(--text-muted);
  }}
  .author-email {{
    font-family: var(--font-mono);
    font-size: 0.82rem;
    color: var(--accent-blue);
    margin-top: 4px;
  }}

  .paper-meta-pills {{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 26px;
    padding-top: 20px;
    border-top: 1px dashed var(--border-subtle);
  }}
  .meta-pill {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 0.78rem;
    font-weight: 600;
    color: var(--text-secondary);
    background: var(--bg-subtle);
    padding: 5px 12px;
    border-radius: var(--radius-sm);
    border: 1px solid var(--border-subtle);
  }}

  /* Figure Card */
  .figure-card {{
    background: var(--bg-paper);
    border: 1px solid var(--border-paper);
    border-radius: var(--radius-lg);
    margin-bottom: 48px;
    box-shadow: var(--shadow-paper);
    overflow: hidden;
    scroll-margin-top: 80px;
  }}

  .figure-card-header {{
    padding: 18px 28px;
    background: var(--bg-subtle);
    border-bottom: 1px solid var(--border-paper);
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 12px;
  }}
  .figure-number-badge {{
    display: inline-flex;
    align-items: center;
    gap: 10px;
    font-weight: 700;
    font-size: 0.95rem;
    color: var(--accent-blue);
    font-family: var(--font-sans);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }}
  .figure-tags {{
    display: flex;
    gap: 8px;
  }}
  .figure-tag {{
    font-size: 0.74rem;
    font-weight: 600;
    padding: 3px 10px;
    border-radius: 9999px;
    background: var(--bg-paper);
    color: var(--text-muted);
    border: 1px solid var(--border-subtle);
  }}

  .view-mode-toggle {{
    display: inline-flex;
    align-items: center;
    background: var(--bg-paper);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-sm);
    padding: 2px;
  }}
  .view-mode-btn {{
    border: none;
    background: transparent;
    padding: 4px 10px;
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--text-muted);
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.15s ease;
  }}
  .view-mode-btn.active {{
    background: var(--accent-blue-light);
    color: var(--accent-blue);
  }}

  .figure-visual-stage {{
    padding: 32px 28px;
    background: var(--bg-paper);
    display: flex;
    justify-content: center;
    align-items: center;
    border-bottom: 1px solid var(--border-subtle);
    min-height: 280px;
  }}

  /* Mode Containers */
  .mode-interactive {{
    width: 100%;
    display: block;
  }}
  .mode-camera {{
    width: 100%;
    display: none;
    text-align: center;
  }}
  .mode-camera img {{
    max-width: 100%;
    height: auto;
    border-radius: var(--radius-sm);
    box-shadow: var(--shadow-sm);
    background: #ffffff;
  }}

  /* FIG 1: Demand Cascade Visual Flow */
  .dcm-architecture-canvas {{
    width: 100%;
    max-width: 960px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 14px;
  }}
  .dcm-tier-row {{
    display: grid;
    grid-template-columns: 160px 1fr;
    gap: 20px;
    align-items: stretch;
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-md);
    padding: 16px 20px;
    box-shadow: var(--shadow-sm);
    transition: all 0.2s ease;
  }}
  .dcm-tier-row:hover {{
    border-color: var(--border-accent);
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
  }}
  .tier-badge-col {{
    display: flex;
    flex-direction: column;
    justify-content: center;
    border-right: 1px solid var(--border-subtle);
    padding-right: 16px;
  }}
  .tier-code {{
    font-family: var(--font-mono);
    font-size: 0.78rem;
    font-weight: 700;
    color: var(--accent-blue);
    letter-spacing: 0.05em;
  }}
  .tier-name {{
    font-family: var(--font-serif);
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--text-primary);
    line-height: 1.3;
    margin-top: 2px;
  }}
  .tier-content-col {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 14px;
    align-items: center;
  }}
  .metric-box {{
    background: var(--bg-subtle);
    padding: 10px 14px;
    border-radius: var(--radius-sm);
    border: 1px solid var(--border-subtle);
  }}
  .metric-label {{
    font-size: 0.74rem;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }}
  .metric-value {{
    font-family: var(--font-mono);
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-top: 3px;
  }}
  .metric-sub {{
    font-size: 0.78rem;
    color: var(--text-secondary);
    margin-top: 2px;
  }}

  .tier-connector {{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8px;
    height: 20px;
    color: var(--text-muted);
    font-size: 0.85rem;
    font-weight: 600;
    font-family: var(--font-mono);
    user-select: none;
  }}

  /* FIG 2: Bar Chart Styles */
  .chart-container {{
    width: 100%;
    max-width: 900px;
    margin: 0 auto;
  }}
  .bar-chart-row {{
    margin-bottom: 18px;
  }}
  .bar-meta {{
    display: flex;
    justify-content: space-between;
    font-size: 0.88rem;
    font-weight: 600;
    margin-bottom: 6px;
    color: var(--text-primary);
  }}
  .bar-track {{
    height: 30px;
    background: var(--bg-subtle);
    border-radius: var(--radius-sm);
    border: 1px solid var(--border-subtle);
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
  }}
  .bar-fill {{
    height: 100%;
    border-radius: var(--radius-sm);
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding-right: 12px;
    color: #ffffff;
    font-family: var(--font-mono);
    font-size: 0.82rem;
    font-weight: 700;
    transition: width 1.2s cubic-bezier(0.16, 1, 0.3, 1);
  }}

  /* FIG 4: Pareto Grid */
  .pareto-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 20px;
    width: 100%;
    max-width: 940px;
    margin: 0 auto;
  }}
  .pareto-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-md);
    padding: 20px;
    position: relative;
    box-shadow: var(--shadow-sm);
    transition: all 0.2s ease;
  }}
  .pareto-card:hover {{
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
  }}
  .pareto-card.optimal {{
    border: 2px solid var(--accent-teal);
    background: rgba(13,148,136,0.04);
  }}
  .pareto-badge {{
    position: absolute;
    top: 14px;
    right: 14px;
    font-size: 0.7rem;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }}
  .pareto-badge.sweet {{
    background: #ccfbf1;
    color: #0f766e;
    border: 1px solid #99f6e4;
  }}
  .pareto-title {{
    font-family: var(--font-serif);
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 14px;
  }}
  .pareto-stat {{
    display: flex;
    justify-content: space-between;
    font-size: 0.85rem;
    padding: 6px 0;
    border-bottom: 1px dashed var(--border-subtle);
  }}
  .pareto-stat:last-child {{ border-bottom: none; }}
  .pareto-stat .k {{ color: var(--text-muted); }}
  .pareto-stat .v {{ font-family: var(--font-mono); font-weight: 700; color: var(--text-primary); }}

  /* FIG 5: Tornado Diagram */
  .tornado-wrapper {{
    width: 100%;
    max-width: 920px;
    margin: 0 auto;
  }}
  .tornado-header-row {{
    display: grid;
    grid-template-columns: 220px 1fr 1fr;
    margin-bottom: 10px;
    font-size: 0.78rem;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }}
  .tornado-row {{
    display: grid;
    grid-template-columns: 220px 1fr 1fr;
    gap: 8px;
    align-items: center;
    margin-bottom: 10px;
    font-size: 0.86rem;
  }}
  .tornado-label {{
    text-align: right;
    font-weight: 600;
    color: var(--text-primary);
    padding-right: 12px;
  }}
  .tornado-neg-side {{
    display: flex;
    justify-content: flex-end;
    align-items: center;
    background: var(--bg-subtle);
    height: 28px;
    border-radius: 4px 0 0 4px;
    position: relative;
    border-right: 2px solid var(--text-primary);
  }}
  .tornado-pos-side {{
    display: flex;
    justify-content: flex-start;
    align-items: center;
    background: var(--bg-subtle);
    height: 28px;
    border-radius: 0 4px 4px 0;
    position: relative;
    border-left: 2px solid var(--text-primary);
  }}
  .tornado-bar-neg {{
    height: 100%;
    background: #64748b;
    border-radius: 4px 0 0 4px;
    display: flex;
    align-items: center;
    padding-left: 8px;
    font-family: var(--font-mono);
    font-size: 0.78rem;
    font-weight: 700;
    color: #ffffff;
  }}
  .tornado-bar-pos {{
    height: 100%;
    background: #1e293b;
    border-radius: 0 4px 4px 0;
    display: flex;
    align-items: center;
    padding-right: 8px;
    font-family: var(--font-mono);
    font-size: 0.78rem;
    font-weight: 700;
    color: #ffffff;
  }}

  /* LaTeX Caption Box */
  .figure-caption-box {{
    padding: 22px 28px 24px;
    font-family: var(--font-serif);
    font-size: 1.05rem;
    line-height: 1.65;
    color: var(--text-primary);
    text-align: justify;
    background: var(--bg-paper);
  }}
  .fig-label {{
    font-weight: 700;
    color: var(--text-primary);
  }}

  /* Insights Accordion */
  .figure-insights {{
    padding: 18px 28px;
    background: var(--bg-subtle);
    border-top: 1px solid var(--border-paper);
  }}
  .insights-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 0.88rem;
    font-weight: 700;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }}
  .insights-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 16px;
    margin-top: 16px;
  }}
  .insight-card {{
    background: var(--bg-paper);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-sm);
    padding: 14px 18px;
  }}
  .insight-card h4 {{
    font-size: 0.84rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: var(--accent-blue);
    margin-bottom: 6px;
  }}
  .insight-card p {{
    font-size: 0.86rem;
    color: var(--text-secondary);
    line-height: 1.5;
  }}

  /* Page Footer */
  .page-footer {{
    text-align: center;
    padding: 48px 20px;
    font-size: 0.88rem;
    color: var(--text-muted);
    border-top: 1px solid var(--border-paper);
  }}

  @media (max-width: 768px) {{
    .paper-header {{ padding: 24px 20px; }}
    .paper-title {{ font-size: 1.5rem; }}
    .dcm-tier-row {{ grid-template-columns: 1fr; }}
    .tier-badge-col {{ border-right: none; border-bottom: 1px solid var(--border-subtle); padding-bottom: 10px; margin-bottom: 10px; }}
    .tornado-header-row, .tornado-row {{ grid-template-columns: 140px 1fr 1fr; font-size: 0.75rem; }}
  }}
</style>
</head>
<body data-theme="light">

<!-- Top Navigation -->
<header class="top-navbar">
  <div class="nav-brand">
    <span class="nav-badge">IEEEtran 10pt</span>
    <span class="nav-title">Sovereign by Design &bull; Scientific Figures Showcase</span>
  </div>
  
  <div class="nav-actions">
    <nav class="nav-tabs">
      <a href="#fig1" class="nav-tab-btn active">Fig 1</a>
      <a href="#fig2" class="nav-tab-btn">Fig 2</a>
      <a href="#fig3" class="nav-tab-btn">Fig 3</a>
      <a href="#fig4" class="nav-tab-btn">Fig 4</a>
      <a href="#fig5" class="nav-tab-btn">Fig 5</a>
    </nav>

    <button class="btn-action" id="themeToggleBtn" onclick="toggleTheme()" title="Toggle Dark/Light Mode">
      <span id="themeIcon">🌙</span> <span id="themeLabel">Dark Mode</span>
    </button>
  </div>
</header>

<div class="container">

  <!-- Scholarly Paper Header -->
  <section class="paper-header">
    <div class="paper-conference-tag">
      <span>Amity Research-o-Thon 2026</span> &bull; <span>IEEE Format Aligned Proceedings</span>
    </div>
    <h1 class="paper-title">Sovereign by Design: An Integrated Five-Pillar Framework for India's Strategic Compute and Artificial Intelligence Infrastructure</h1>
    <div class="paper-subtitle">Auditable Demand-Cascade Model (DCM), Empirical Supply-Chain Telemetry &amp; Microelectronic Chokepoint Inversion</div>
    
    <div class="paper-authors">
      <div class="author-col">
        <div class="author-names">Parikshit Singh Bais, Adarsh Singh</div>
        <div class="author-dept">dept. of Computer Science and Engineering</div>
        <div class="author-inst">Amity School of Engineering and Technology<br>Amity University Madhya Pradesh, Gwalior, India</div>
        <div class="author-email">e-mail: {{parikshit.bais, adarsh.singh}}@amity.edu</div>
      </div>
      <div class="author-col">
        <div class="author-names">Sourav, Anamidhi Shrivastava</div>
        <div class="author-dept">dept. of Computer Science and Engineering</div>
        <div class="author-inst">Amity School of Engineering and Technology<br>Amity University Madhya Pradesh, Gwalior, India</div>
        <div class="author-email">e-mail: {{sourav, anamidhi.shrivastava}}@amity.edu</div>
      </div>
    </div>

    <div class="paper-meta-pills">
      <span class="meta-pill"><strong>Layout:</strong> 2-Column IEEEtran (10 pt)</span>
      <span class="meta-pill"><strong>Pages:</strong> Exactly 11 Pages</span>
      <span class="meta-pill"><strong>Citations:</strong> 36 Primary Literature Sources</span>
      <span class="meta-pill"><strong>Compute Target:</strong> 500,000 Accelerators (2030)</span>
      <span class="meta-pill"><strong>Operational Baseline:</strong> 45,000+ Shared GPUs (₹65/hr)</span>
      <span class="meta-pill"><strong>National Outlay:</strong> ₹10,372 Cr (IndiaAI) &bull; ₹1,27,500 Cr (Semicon India 2.0)</span>
    </div>
  </section>


  <!-- ==================== FIGURE 1 ==================== -->
  <article class="figure-card" id="fig1">
    <div class="figure-card-header">
      <div class="figure-number-badge">
        <span>Figure 1</span> &bull; <span>Demand-Cascade Architecture (DCM)</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <div class="view-mode-toggle">
          <button class="view-mode-btn active" onclick="setViewMode('fig1', 'interactive')">Interactive UI</button>
          <button class="view-mode-btn" onclick="setViewMode('fig1', 'camera')">Camera-Ready Vector</button>
        </div>
        <div class="figure-tags">
          <span class="figure-tag">6-Tier Pipeline</span>
          <span class="figure-tag">Policy &rarr; Grid</span>
        </div>
      </div>
    </div>

    <div class="figure-visual-stage">
      <div class="mode-interactive" id="fig1-interactive">
        <div class="dcm-architecture-canvas">
          
          <div class="dcm-tier-row">
            <div class="tier-badge-col">
              <span class="tier-code">TIER 1</span>
              <span class="tier-name">Sovereign Policy Targets</span>
            </div>
            <div class="tier-content-col">
              <div class="metric-box">
                <div class="metric-label">Deployment Horizon</div>
                <div class="metric-value">500,000 Accelerators</div>
                <div class="metric-sub">2030 Sovereign AI Roadmap</div>
              </div>
              <div class="metric-box">
                <div class="metric-label">National Outlays</div>
                <div class="metric-value">₹10,372 Cr / ₹1,27,500 Cr</div>
                <div class="metric-sub">IndiaAI Mission &bull; Semicon India 2.0</div>
              </div>
              <div class="metric-box">
                <div class="metric-label">Active GPU Pool</div>
                <div class="metric-value">45,000+ Empaneled</div>
                <div class="metric-sub">Subsidized at ₹65/hr (~$0.72/hr)</div>
              </div>
            </div>
          </div>

          <div class="tier-connector">&darr; Algorithmic FLOP &amp; Memory Bounds ($C = 6PD$)</div>

          <div class="dcm-tier-row">
            <div class="tier-badge-col">
              <span class="tier-code">TIER 2</span>
              <span class="tier-name">Algorithmic Compute Sizing</span>
            </div>
            <div class="tier-content-col">
              <div class="metric-box">
                <div class="metric-label">Target Compute Stock</div>
                <div class="metric-value">245.0 ExaFLOPS</div>
                <div class="metric-sub">FP16 / BF16 Tensor Operations</div>
              </div>
              <div class="metric-box">
                <div class="metric-label">Scaling Law Formulation</div>
                <div class="metric-value">$C = 6PD$</div>
                <div class="metric-sub">Parameters $P = 70\text{{B}} \dots 1\text{{T}}$</div>
              </div>
              <div class="metric-box">
                <div class="metric-label">Indigenous Models</div>
                <div class="metric-value">Param-1 &bull; Sarvam</div>
                <div class="metric-sub">7.5T Multilingual Tokens Trained</div>
              </div>
            </div>
          </div>

          <div class="tier-connector">&darr; Server Chassis &amp; High-Speed Interconnect Aggregation</div>

          <div class="dcm-tier-row">
            <div class="tier-badge-col">
              <span class="tier-code">TIER 3</span>
              <span class="tier-name">Server Physics &amp; Aggregation</span>
            </div>
            <div class="tier-content-col">
              <div class="metric-box">
                <div class="metric-label">Server Chassis Nodes</div>
                <div class="metric-value">62,500 Nodes</div>
                <div class="metric-sub">8-Way GPU HGX / NVL Architecture</div>
              </div>
              <div class="metric-box">
                <div class="metric-label">Server Unit Power</div>
                <div class="metric-value">10.20 kW / Node</div>
                <div class="metric-sub">8x 700W TDP + Host CPUs &amp; Optics</div>
              </div>
              <div class="metric-box">
                <div class="metric-label">Aggregate Peak IT Load</div>
                <div class="metric-value">637.50 MW</div>
                <div class="metric-sub">Direct Silicon Accelerator Draw</div>
              </div>
            </div>
          </div>

          <div class="tier-connector">&darr; Facility Thermodynamics &amp; Tropical Heat Rejection</div>

          <div class="dcm-tier-row">
            <div class="tier-badge-col">
              <span class="tier-code">TIER 4</span>
              <span class="tier-name">Thermodynamics &amp; Cooling</span>
            </div>
            <div class="tier-content-col">
              <div class="metric-box">
                <div class="metric-label">D2C Liquid Cooling PUE</div>
                <div class="metric-value">1.25 Rated PUE</div>
                <div class="metric-sub">vs. 1.45 Conventional Evaporative Air</div>
              </div>
              <div class="metric-box">
                <div class="metric-label">Peak Facility Power</div>
                <div class="metric-value">891.80 MW Load</div>
                <div class="metric-sub">Saves 172.0 MW vs Traditional Air</div>
              </div>
              <div class="metric-box">
                <div class="metric-label">Cooling Water Withdrawal</div>
                <div class="metric-value">630.9 ML/yr D2C</div>
                <div class="metric-sub">94.6% Slashed (11B Litres Conserved)</div>
              </div>
            </div>
          </div>

          <div class="tier-connector">&darr; Dual Supply-Chain &amp; Power Grid Interconnections</div>

          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
            <div class="dcm-tier-row" style="grid-template-columns: 1fr;">
              <div style="border-bottom: 1px solid var(--border-subtle); padding-bottom: 8px; margin-bottom: 8px;">
                <span class="tier-code">TIER 5</span> &bull; <span class="tier-name">Semiconductor Value Chain</span>
              </div>
              <div style="display: flex; flex-direction: column; gap: 8px;">
                <div class="metric-box">
                  <div class="metric-label">TSMC Sub-5nm Wafer Starts</div>
                  <div class="metric-value">12,500 Wafers (1.60%)</div>
                  <div class="metric-sub">Murphy Yield Model ($D_0 = 0.08\text{{ cm}}^{{-2}}$)</div>
                </div>
                <div class="metric-box">
                  <div class="metric-label">CoWoS Advanced Packaging</div>
                  <div class="metric-value">33,334 Wafers (7.41%)</div>
                  <div class="metric-sub">Binding Chokepoint (4.6x Higher Intensity)</div>
                </div>
                <div class="metric-box">
                  <div class="metric-label">HBM3e Memory Output</div>
                  <div class="metric-value">4,000,000 Stacks (6.67%)</div>
                  <div class="metric-sub">Triopoly (SK Hynix, Samsung, Micron)</div>
                </div>
              </div>
            </div>

            <div class="dcm-tier-row" style="grid-template-columns: 1fr;">
              <div style="border-bottom: 1px solid var(--border-subtle); padding-bottom: 8px; margin-bottom: 8px;">
                <span class="tier-code">TIER 6</span> &bull; <span class="tier-name">Grid Integration &amp; Substations</span>
              </div>
              <div style="display: flex; flex-direction: column; gap: 8px;">
                <div class="metric-box">
                  <div class="metric-label">Colocation Power Absorption</div>
                  <div class="metric-value">56.62% of mid-2026</div>
                  <div class="metric-sub">891.8 MW of 1,575 MW Total Capacity</div>
                </div>
                <div class="metric-box">
                  <div class="metric-label">Mumbai Concentration Risk</div>
                  <div class="metric-value">52.4% Concentration</div>
                  <div class="metric-sub">467.3 MW Load in Single Transmission Zone</div>
                </div>
                <div class="metric-box">
                  <div class="metric-label">Substation Requirements</div>
                  <div class="metric-value">18x 50 MW Substations</div>
                  <div class="metric-sub">CEA 400/220 kV Interconnection Queue</div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
      <div class="mode-camera" id="fig1-camera">
        <img src="{img_fig1}" alt="Fig 1 Camera-Ready" />
      </div>
    </div>

    <div class="figure-caption-box">
      <span class="fig-label">Fig. 1.</span> <strong>The six-layer Demand-Cascade Model (DCM) architecture:</strong> tracing policy targets through algorithmic sizing, hardware aggregation, thermal engineering, semiconductor supply-chain allocation, and power grid constraints. The framework establishes continuous analytical causality between national policy ambitions and physical microelectronic/thermodynamic realities.
    </div>

    <div class="figure-insights">
      <div class="insights-header">
        <span>Empirical Mechanics &amp; Cross-Pillar Takeaways</span>
      </div>
      <div class="insights-grid">
        <div class="insight-card">
          <h4>Policy Decoupling</h4>
          <p>Prevailing policy treats compute and electrical grids as separate silos. DCM proves that deploying 500k GPUs absorbs 56.62% of India's current colocation capacity.</p>
        </div>
        <div class="insight-card">
          <h4>Subsidized Compute Track</h4>
          <p>IndiaAI's ₹65/hr compute rate (60–72% commercial discount) has enabled 237 research projects to consume 93.18 lakh GPU-hours across 45,000 live units.</p>
        </div>
        <div class="insight-card">
          <h4>Transmission Saturation</h4>
          <p>Feeding 891.8 MW into metropolitan clusters requires dedicated CEA 400/220 kV corridors with fast-tracked 9-month approval windows to avoid catastrophic queue delays.</p>
        </div>
      </div>
    </div>
  </article>


  <!-- ==================== FIGURE 2 ==================== -->
  <article class="figure-card" id="fig2">
    <div class="figure-card-header">
      <div class="figure-number-badge">
        <span>Figure 2</span> &bull; <span>Structural Chokepoint Inversion</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <div class="view-mode-toggle">
          <button class="view-mode-btn active" onclick="setViewMode('fig2', 'interactive')">Interactive UI</button>
          <button class="view-mode-btn" onclick="setViewMode('fig2', 'camera')">Camera-Ready Vector</button>
        </div>
        <div class="figure-tags">
          <span class="figure-tag">Core Empirical Discovery</span>
          <span class="figure-tag">Packaging vs Fabs</span>
        </div>
      </div>
    </div>

    <div class="figure-visual-stage">
      <div class="mode-interactive" id="fig2-interactive">
        <div class="chart-container">
          
          <div class="bar-chart-row">
            <div class="bar-meta">
              <span>Wafer Starts: TSMC Sub-5nm Share (Front-End Lithography)</span>
              <span><strong>1.60%</strong> (12,500 of 780,000 wafers/yr)</span>
            </div>
            <div class="bar-track">
              <div class="bar-fill" style="width: 16%; background: #64748b;">1.60%</div>
            </div>
          </div>

          <div class="bar-chart-row">
            <div class="bar-meta">
              <span>HBM3e Memory: Global Output Share (Triopoly Supply)</span>
              <span><strong>6.67%</strong> (4,000,000 of 60,000,000 stacks)</span>
            </div>
            <div class="bar-track">
              <div class="bar-fill" style="width: 32%; background: #475569;">6.67%</div>
            </div>
          </div>

          <div class="bar-chart-row">
            <div class="bar-meta">
              <span>CoWoS Advanced Packaging: TSMC Global Capacity <span style="color:#ef4444; font-weight:700;">(4.6-fold Inversion Chokepoint)</span></span>
              <span><strong style="color:#ef4444;">7.41%</strong> (33,334 of 450,000 wafers/yr)</span>
            </div>
            <div class="bar-track">
              <div class="bar-fill" style="width: 38%; background: #1e293b; border-right: 4px solid #ef4444;">7.41%</div>
            </div>
          </div>

          <div class="bar-chart-row">
            <div class="bar-meta">
              <span>Domestic Colocation Power: 2030 Pipeline Absorption</span>
              <span><strong>27.90%</strong> (891.8 MW of 3,200 MW Pipeline)</span>
            </div>
            <div class="bar-track">
              <div class="bar-fill" style="width: 62%; background: #334155;">27.90%</div>
            </div>
          </div>

          <div class="bar-chart-row">
            <div class="bar-meta">
              <span>Domestic Colocation Power: mid-2026 Operational Capacity <span style="color:#f97316; font-weight:700;">(Severe Constraint)</span></span>
              <span><strong style="color:#f97316;">56.62%</strong> (891.8 MW of 1,575 MW Operational)</span>
            </div>
            <div class="bar-track">
              <div class="bar-fill" style="width: 88%; background: #0f172a; border-right: 4px solid #f97316;">56.62%</div>
            </div>
          </div>

        </div>
      </div>
      <div class="mode-camera" id="fig2-camera">
        <img src="{img_fig2}" alt="Fig 2 Camera-Ready" />
      </div>
    </div>

    <div class="figure-caption-box">
      <span class="fig-label">Fig. 2.</span> <strong>The structural chokepoint inversion (500,000-GPU baseline):</strong> required share of global advanced packaging (7.41%) and domestic colocation power (56.62%) far outstrips raw logic wafer requirements (1.60%). This refutes the prevailing policy premise that domestic sub-3nm wafer fabrication is India's primary bottleneck.
    </div>

    <div class="figure-insights">
      <div class="insights-header">
        <span>Strategic Value-Chain Analysis</span>
      </div>
      <div class="insights-grid">
        <div class="insight-card">
          <h4>The Logic Fallacy</h4>
          <p>Sub-3nm gigafabs cost $15–20B. Yet 500k GPUs require only 1.60% of TSMC's sub-5nm output—a commercially manageable allocation via sovereign purchase treaties.</p>
        </div>
        <div class="insight-card">
          <h4>The True Chokepoint: CoWoS</h4>
          <p>Advanced packaging requires 7.41% of global CoWoS capacity (HHI = 8,100)—exhibiting a constraint intensity 4.6-fold higher than front-end lithography.</p>
        </div>
        <div class="insight-card">
          <h4>Near-Term Priority</h4>
          <p>Semicon India 2.0 must prioritize 2.5D interposer packaging joint-ventures (Tata Morigaon, Micron Sanand) to capture packaging sovereignty before funding front-end fabs.</p>
        </div>
      </div>
    </div>
  </article>


  <!-- ==================== FIGURE 3 ==================== -->
  <article class="figure-card" id="fig3">
    <div class="figure-card-header">
      <div class="figure-number-badge">
        <span>Figure 3</span> &bull; <span>Cross-National Comparative Benchmark</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <div class="view-mode-toggle">
          <button class="view-mode-btn active" onclick="setViewMode('fig3', 'interactive')">Interactive UI</button>
          <button class="view-mode-btn" onclick="setViewMode('fig3', 'camera')">Camera-Ready Vector</button>
        </div>
        <div class="figure-tags">
          <span class="figure-tag">N-2 Asymmetry</span>
          <span class="figure-tag">US &bull; China &bull; India</span>
        </div>
      </div>
    </div>

    <div class="figure-visual-stage">
      <div class="mode-interactive" id="fig3-interactive">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; width: 100%; max-width: 920px; margin: 0 auto;">
          
          <!-- Panel A -->
          <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 22px;">
            <h4 style="font-family: var(--font-serif); font-size: 1.15rem; margin-bottom: 16px;">(a) Accelerated Compute Stock (EFLOPS FP16 eq.)</h4>
            
            <div style="display: flex; flex-direction: column; gap: 12px;">
              <div>
                <div class="bar-meta"><span>United States</span><span><strong>1,200 EFLOPS</strong></span></div>
                <div class="bar-track"><div class="bar-fill" style="width: 100%; background: #0f172a;">1,200</div></div>
              </div>
              <div>
                <div class="bar-meta"><span>China</span><span><strong>450 EFLOPS</strong></span></div>
                <div class="bar-track"><div class="bar-fill" style="width: 37.5%; background: #334155;">450</div></div>
              </div>
              <div>
                <div class="bar-meta"><span>India (2030 500k Plan)</span><span><strong>245 EFLOPS</strong></span></div>
                <div class="bar-track"><div class="bar-fill" style="width: 20.4%; background: #64748b;">245</div></div>
              </div>
              <div>
                <div class="bar-meta"><span>India (mid-2026 Operational)</span><span><strong>35 EFLOPS</strong></span></div>
                <div class="bar-track"><div class="bar-fill" style="width: 5%; background: #94a3b8; color: #000;">35</div></div>
              </div>
            </div>
          </div>

          <!-- Panel B -->
          <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 22px;">
            <h4 style="font-family: var(--font-serif); font-size: 1.15rem; margin-bottom: 16px;">(b) Domestic Value-Chain Self-Sufficiency (%)</h4>
            
            <table style="width: 100%; border-collapse: collapse; font-size: 0.85rem; text-align: center;">
              <thead>
                <tr style="border-bottom: 2px solid var(--border-paper); color: var(--text-muted);">
                  <th style="text-align: left; padding: 8px 4px;">Strategic Tier</th>
                  <th style="padding: 8px 4px;">US</th>
                  <th style="padding: 8px 4px;">China</th>
                  <th style="padding: 8px 4px; color: var(--accent-blue);">India</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom: 1px dashed var(--border-subtle);">
                  <td style="text-align: left; padding: 9px 4px; font-weight: 600;">Sub-5nm Wafer Fab</td>
                  <td>5%</td>
                  <td>2%</td>
                  <td style="font-weight: 700; color: #ef4444;">0%</td>
                </tr>
                <tr style="border-bottom: 1px dashed var(--border-subtle);">
                  <td style="text-align: left; padding: 9px 4px; font-weight: 600;">Advanced Packaging</td>
                  <td>5%</td>
                  <td>3%</td>
                  <td style="font-weight: 700; color: #ef4444;">0%</td>
                </tr>
                <tr style="border-bottom: 1px dashed var(--border-subtle);">
                  <td style="text-align: left; padding: 9px 4px; font-weight: 600;">Silicon Design (EDA/RTL)</td>
                  <td>85%</td>
                  <td>20%</td>
                  <td style="font-weight: 700; color: var(--accent-teal);">20%</td>
                </tr>
                <tr>
                  <td style="text-align: left; padding: 9px 4px; font-weight: 600;">Gallium Refining</td>
                  <td>0%</td>
                  <td>99%</td>
                  <td style="font-weight: 700; color: var(--accent-amber);">0.5%</td>
                </tr>
              </tbody>
            </table>
            <div style="font-size: 0.76rem; color: var(--text-muted); margin-top: 12px; line-height: 1.4;">
              *Gallium: USGS 2025; CSIR-IMMT pilot targets 50 MT/yr (6N purity) from red mud at NALCO/Hindalco.
            </div>
          </div>

        </div>
      </div>
      <div class="mode-camera" id="fig3-camera">
        <img src="{img_fig3}" alt="Fig 3 Camera-Ready" />
      </div>
    </div>

    <div class="figure-caption-box">
      <span class="fig-label">Fig. 3.</span> <strong>Cross-national comparative benchmark between the United States, China, and India across accelerated compute stock in ExaFLOPS (Panel A) and microelectronic supply chain self-sufficiency across four strategic tiers (Panel B).</strong> Illustrates the structural "N-2 asymmetry" confronting non-superpower states in attempting autarkic replication.
    </div>

    <div class="figure-insights">
      <div class="insights-header">
        <span>Strategic Geopolitics &amp; Frugal AI Doctrine</span>
      </div>
      <div class="insights-grid">
        <div class="insight-card">
          <h4>The "N-2" Reality</h4>
          <p>Full-stack hardware independence is available only to the US and China. India's optimal strategy is "Coordinated Specialization" rather than capital-dilutive autarky.</p>
        </div>
        <div class="insight-card">
          <h4>Leveraging Silicon Design</h4>
          <p>With 20% of the world's VLSI design engineers, India can lead open RISC-V matrix acceleration chiplets on 28nm nodes (Tata Dholera) over premature leading-edge fabs.</p>
        </div>
        <div class="insight-card">
          <h4>Critical Minerals Defense</h4>
          <p>China's 99% gallium dominance can be countered by commercializing CSIR-IMMT's extraction tech from domestic bauxite red mud at NALCO and Hindalco.</p>
        </div>
      </div>
    </div>
  </article>


  <!-- ==================== FIGURE 4 ==================== -->
  <article class="figure-card" id="fig4">
    <div class="figure-card-header">
      <div class="figure-number-badge">
        <span>Figure 4</span> &bull; <span>Cooling Technology Pareto Frontier</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <div class="view-mode-toggle">
          <button class="view-mode-btn active" onclick="setViewMode('fig4', 'interactive')">Interactive UI</button>
          <button class="view-mode-btn" onclick="setViewMode('fig4', 'camera')">Camera-Ready Vector</button>
        </div>
        <div class="figure-tags">
          <span class="figure-tag">Thermodynamics</span>
          <span class="figure-tag">Water &bull; Energy Tradeoff</span>
        </div>
      </div>
    </div>

    <div class="figure-visual-stage">
      <div class="mode-interactive" id="fig4-interactive">
        <div class="pareto-grid">
          
          <div class="pareto-card">
            <div class="pareto-title">Traditional Evaporative Air</div>
            <div class="pareto-stat"><span class="k">Annual PUE</span><span class="v">1.45</span></div>
            <div class="pareto-stat"><span class="k">Cooling WUE</span><span class="v">1.80 L/kWh</span></div>
            <div class="pareto-stat"><span class="k">Facility Power</span><span class="v">988.1 MW</span></div>
            <div class="pareto-stat"><span class="k">Water Loss</span><span class="v" style="color:#ef4444;">11,651 ML/yr</span></div>
            <div class="pareto-stat"><span class="k">Summer Penalty</span><span class="v">+0.12 PUE</span></div>
          </div>

          <div class="pareto-card">
            <div class="pareto-title">Rear-Door HEX (RDHx)</div>
            <div class="pareto-stat"><span class="k">Annual PUE</span><span class="v">1.35</span></div>
            <div class="pareto-stat"><span class="k">Cooling WUE</span><span class="v">1.00 L/kWh</span></div>
            <div class="pareto-stat"><span class="k">Facility Power</span><span class="v">920.0 MW</span></div>
            <div class="pareto-stat"><span class="k">Water Loss</span><span class="v">6,447 ML/yr</span></div>
            <div class="pareto-stat"><span class="k">Summer Penalty</span><span class="v">+0.08 PUE</span></div>
          </div>

          <div class="pareto-card optimal">
            <span class="pareto-badge sweet">Optimal Frontier</span>
            <div class="pareto-title" style="color: var(--accent-teal);">Direct-to-Chip (D2C) Liquid</div>
            <div class="pareto-stat"><span class="k">Annual PUE</span><span class="v" style="color:var(--accent-teal); font-weight:700;">1.25 Rated</span></div>
            <div class="pareto-stat"><span class="k">Cooling WUE</span><span class="v" style="color:var(--accent-teal); font-weight:700;">0.12 L/kWh</span></div>
            <div class="pareto-stat"><span class="k">Facility Power</span><span class="v">891.8 MW</span></div>
            <div class="pareto-stat"><span class="k">Water Loss</span><span class="v" style="color:var(--accent-teal); font-weight:700;">630.9 ML/yr</span></div>
            <div class="pareto-stat"><span class="k">Water Savings</span><span class="v" style="color:var(--accent-teal); font-weight:700;">94.6% Slashed</span></div>
          </div>

          <div class="pareto-card">
            <div class="pareto-title">Two-Phase Immersion</div>
            <div class="pareto-stat"><span class="k">Annual PUE</span><span class="v">1.12</span></div>
            <div class="pareto-stat"><span class="k">Cooling WUE</span><span class="v">0.03 L/kWh</span></div>
            <div class="pareto-stat"><span class="k">Facility Power</span><span class="v">761.6 MW</span></div>
            <div class="pareto-stat"><span class="k">Water Loss</span><span class="v">150.0 ML/yr</span></div>
            <div class="pareto-stat"><span class="k">Capex Cost</span><span class="v">High Premium</span></div>
          </div>

        </div>
      </div>
      <div class="mode-camera" id="fig4-camera">
        <img src="{img_fig4}" alt="Fig 4 Camera-Ready" />
      </div>
    </div>

    <div class="figure-caption-box">
      <span class="fig-label">Fig. 4.</span> <strong>Cooling technology water-energy Pareto frontier across Indian tropical ambient profiles:</strong> Direct-to-Chip (D2C) liquid cooling achieves the optimal trade-off between power efficiency and water conservation, eliminating 11.02 billion litres/year of evaporative losses and cutting facility power by 172 MW compared to conventional evaporative air systems.
    </div>

    <div class="figure-insights">
      <div class="insights-header">
        <span>Resource Sustainability &amp; Grid Safeguards</span>
      </div>
      <div class="insights-grid">
        <div class="insight-card">
          <h4>11 Billion Litre Conservation</h4>
          <p>Indian tropical ambient temperatures exceed wet-bulb limits in summer, causing evaporative cooling towers to consume 11,651 ML/yr at 500k scale. D2C slashes this by 94.6%.</p>
        </div>
        <div class="insight-card">
          <h4>172 MW Facility Power Saving</h4>
          <p>Operating at a PUE of 1.25 instead of 1.45 reclaims 172 MW of critical substation power—equivalent to three dedicated 50 MW transmission substations.</p>
        </div>
        <div class="insight-card">
          <h4>Mandatory Empanelment Standard</h4>
          <p>We propose that IndiaAI subsidies require a maximum facility PUE of 1.25 and mandatory closed-loop dry heat rejection for all subsidized colocation providers.</p>
        </div>
      </div>
    </div>
  </article>


  <!-- ==================== FIGURE 5 ==================== -->
  <article class="figure-card" id="fig5">
    <div class="figure-card-header">
      <div class="figure-number-badge">
        <span>Figure 5</span> &bull; <span>Sensitivity &amp; Uncertainty Tornado</span>
      </div>
      <div style="display:flex; align-items:center; gap:10px;">
        <div class="view-mode-toggle">
          <button class="view-mode-btn active" onclick="setViewMode('fig5', 'interactive')">Interactive UI</button>
          <button class="view-mode-btn" onclick="setViewMode('fig5', 'camera')">Camera-Ready Vector</button>
        </div>
        <div class="figure-tags">
          <span class="figure-tag">OAT Perturbation</span>
          <span class="figure-tag">Elasticity Bounds</span>
        </div>
      </div>
    </div>

    <div class="figure-visual-stage">
      <div class="mode-interactive" id="fig5-interactive">
        <div class="tornado-wrapper">
          <div class="tornado-header-row">
            <div style="text-align: right; padding-right: 12px;">Model Parameter</div>
            <div style="text-align: right; padding-right: 12px;">Lower Bound Swing (&minus;&Delta;%)</div>
            <div style="text-align: left; padding-left: 12px;">Upper Bound Swing (+&Delta;%)</div>
          </div>

          <div class="tornado-row">
            <div class="tornado-label">Cooling PUE (1.25 &rarr; 1.55)</div>
            <div class="tornado-neg-side"><div class="tornado-bar-neg" style="width: 25%;">&minus;10.7%</div></div>
            <div class="tornado-pos-side"><div class="tornado-bar-pos" style="width: 25%;">+10.7%</div></div>
          </div>

          <div class="tornado-row">
            <div class="tornado-label">Utilization (0.65 &rarr; 0.90)</div>
            <div class="tornado-neg-side"><div class="tornado-bar-neg" style="width: 44%;">&minus;18.7%</div></div>
            <div class="tornado-pos-side"><div class="tornado-bar-pos" style="width: 30%;">+12.5%</div></div>
          </div>

          <div class="tornado-row">
            <div class="tornado-label">Server Overhead (1.6 &rarr; 2.1)</div>
            <div class="tornado-neg-side"><div class="tornado-bar-neg" style="width: 28%;">&minus;12.1%</div></div>
            <div class="tornado-pos-side"><div class="tornado-bar-pos" style="width: 36%;">+15.4%</div></div>
          </div>

          <div class="tornado-row">
            <div class="tornado-label">GPU TDP (700 W &rarr; 1,000 W)</div>
            <div class="tornado-neg-side"><div class="tornado-bar-neg" style="width: 35%;">&minus;15.0%</div></div>
            <div class="tornado-pos-side"><div class="tornado-bar-pos" style="width: 85%;">+42.8%</div></div>
          </div>

          <div class="tornado-row">
            <div class="tornado-label">Defect Density D₀ (0.06 &rarr; 0.12)</div>
            <div class="tornado-neg-side"><div class="tornado-bar-neg" style="width: 26%;">&minus;11.1%</div></div>
            <div class="tornado-pos-side"><div class="tornado-bar-pos" style="width: 76%;">+38.4%</div></div>
          </div>

          <div class="tornado-row">
            <div class="tornado-label">Cooling WUE (0.2 &rarr; 2.5 L/kWh)</div>
            <div class="tornado-neg-side"><div class="tornado-bar-neg" style="width: 95%;">&minus;88.9%</div></div>
            <div class="tornado-pos-side"><div class="tornado-bar-pos" style="width: 77%;">+38.9%</div></div>
          </div>

        </div>
      </div>
      <div class="mode-camera" id="fig5-camera">
        <img src="{img_fig5}" alt="Fig 5 Camera-Ready" />
      </div>
    </div>

    <div class="figure-caption-box">
      <span class="fig-label">Fig. 5.</span> <strong>One-at-a-time (OAT) parameter sensitivity tornado diagram (500,000-GPU deployment):</strong> relative percentage swing in peak facility power and resource consumption across empirical uncertainty bounds. Highlights that next-generation accelerator TDP (+42.8%) and cooling WUE variations (&minus;88.9% to +38.9%) exert dominant operational variance.
    </div>

    <div class="figure-insights">
      <div class="insights-header">
        <span>Elasticity Bounds &amp; Robust Architecture Design</span>
      </div>
      <div class="insights-grid">
        <div class="insight-card">
          <h4>TDP Dominance (+42.8%)</h4>
          <p>Upgrading from 700W to 1,000W accelerators increases national peak power by 382 MW, proving that hardware silicon choices dictate grid capacity requirements.</p>
        </div>
        <div class="insight-card">
          <h4>Cooling Asymmetry (&minus;88.9%)</h4>
          <p>WUE variation causes an 88.9% swing in water consumption, underscoring that closed-loop liquid systems protect against regional drought vulnerabilities.</p>
        </div>
        <div class="insight-card">
          <h4>Yield Sensitivity (+38.4%)</h4>
          <p>Defect density variations in sub-5nm lithography can inflate wafer starts by 38.4%, validating the necessity of mature packaging partnerships over unproven domestic fabs.</p>
        </div>
      </div>
    </div>
  </article>

</div>

<footer class="page-footer">
  <div>Sovereign by Design &bull; Research-o-Thon 2026 Proceedings &bull; IEEE Conference Aligned Figures</div>
  <div style="margin-top: 6px; font-family: var(--font-mono); font-size: 0.8rem;">Generated directly from manuscript telemetry &bull; Authoritative LaTeX Model Pipeline</div>
</footer>

<script>
  function toggleTheme() {{
    const body = document.body;
    const currentTheme = body.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    body.setAttribute('data-theme', newTheme);
    
    document.getElementById('themeIcon').textContent = newTheme === 'dark' ? '☀️' : '🌙';
    document.getElementById('themeLabel').textContent = newTheme === 'dark' ? 'Light Mode' : 'Dark Mode';
  }}

  function setViewMode(figId, mode) {{
    const card = document.getElementById(figId);
    if (!card) return;
    
    const interactiveContainer = card.querySelector('#' + figId + '-interactive');
    const cameraContainer = card.querySelector('#' + figId + '-camera');
    const buttons = card.querySelectorAll('.view-mode-btn');

    if (mode === 'interactive') {{
      interactiveContainer.style.display = 'block';
      cameraContainer.style.display = 'none';
      buttons[0].classList.add('active');
      buttons[1].classList.remove('active');
    }} else {{
      interactiveContainer.style.display = 'none';
      cameraContainer.style.display = 'block';
      buttons[0].classList.remove('active');
      buttons[1].classList.add('active');
    }}
  }}

  // Active navigation tab on scroll
  const tabs = document.querySelectorAll('.nav-tab-btn');
  window.addEventListener('scroll', () => {{
    let current = '';
    const articles = document.querySelectorAll('article.figure-card');
    articles.forEach(article => {{
      const top = article.offsetTop - 120;
      if (window.pageYOffset >= top) {{
        current = article.getAttribute('id');
      }}
    }});

    tabs.forEach(tab => {{
      tab.classList.remove('active');
      if (tab.getAttribute('href') === `#${{current}}`) {{
        tab.classList.add('active');
      }}
    }});
  }});
</script>

</body>
</html>
"""

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(html_content, encoding="utf-8")
print(f"Generated {OUT} ({OUT.stat().st_size // 1024} KB)")
