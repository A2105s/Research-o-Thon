"""Build one self-contained, IEEE-like HTML page containing all 5 paper figures."""

from pathlib import Path
import base64

ROOT = Path(__file__).resolve().parent.parent
FIG_DIR = ROOT / "manuscript" / "figures"
OUT = ROOT / "output" / "all_figures.html"

FIGURES = [
    ("Figure 1. Six-Layer Demand-Cascade Architecture: From Policy Targets to Microelectronics and Power Grids.",
     "fig1_demand_cascade_architecture.png"),
    ("Figure 2. The Structural Chokepoint Inversion: Required Share of Constrained Global/National Capacity.",
     "fig2_structural_chokepoint_inversion.png"),
    ("Figure 3. Cross-National AI Infrastructure and Strategic Supply-Chain Benchmarking.",
     "fig3_country_comparison_benchmark.png"),
    ("Figure 4. Cooling Technology Water-Energy Pareto Frontier under Tropical Indian Ambient Profiles.",
     "fig4_cooling_water_energy_pareto.png"),
    ("Figure 5. One-at-a-Time Parameter Sensitivity and Uncertainty Tornado (500,000 GPUs).",
     "fig5_sensitivity_tornado_montecarlo.png"),
]

def data_uri(name):
    data = (FIG_DIR / name).read_bytes()
    return "data:image/png;base64," + base64.b64encode(data).decode("ascii")

blocks = []
for caption, filename in FIGURES:
    blocks.append(
        f"""
<figure>
  <img src="{data_uri(filename)}" alt="{filename}" />
  <figcaption>{caption}</figcaption>
</figure>
"""
    )

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Paper Figures — ResearchThon 2026</title>
<style>
  :root {{ --fg: #000000; --muted: #333333; --rule: #000000; }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    padding: 28px 20px;
    font-family: "Times New Roman", Times, serif;
    color: var(--fg);
    background: #ffffff;
  }}
  .page {{
    max-width: 820px;
    margin: 0 auto;
  }}
  h1 {{
    font-size: 1.25rem;
    text-align: center;
    margin: 0 0 4px;
    font-weight: 700;
  }}
  .byline {{
    text-align: center;
    margin: 0 0 16px;
    font-size: 0.95rem;
    color: var(--muted);
  }}
  hr {{
    border: none;
    border-top: 1px solid var(--rule);
    margin: 12px 0 20px;
  }}
  figure {{
    margin: 0 0 24px;
    padding: 0;
    border-top: 1px solid var(--rule);
    border-bottom: 1px solid var(--rule);
    padding-top: 10px;
    padding-bottom: 10px;
  }}
  figure img {{
    display: block;
    width: 100%;
    height: auto;
    background: #ffffff;
  }}
  figcaption {{
    margin-top: 8px;
    font-size: 0.9rem;
    text-align: center;
    color: var(--muted);
  }}
  .toc {{
    margin: 0 0 20px;
    font-size: 0.9rem;
  }}
  .toc div {{ margin: 2px 0; }}
  @media print {{
    body {{ padding: 0; }}
    .page {{ max-width: none; }}
    figure {{ break-inside: avoid; }}
  }}
</style>
</head>
<body>
<div class="page">
  <h1>A Demand-Driven Framework for India's AI Infrastructure Planning</h1>
  <p class="byline">ResearchThon 2026 — consolidated figure set (IEEE conference manuscript).</p>
  <hr />
  <div class="toc">
    {''.join(f'<div>{cap}</div>' for cap, _ in FIGURES)}
  </div>
  <hr />
  {''.join(blocks)}
</div>
</body>
</html>
"""

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(html, encoding="utf-8")
print(f"Generated {OUT} ({OUT.stat().st_size // 1024} KB)")
