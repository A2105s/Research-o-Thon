"""
Generate Five Publication-Grade Figures for ResearchThon 2026 Paper Revision v2
================================================================================
Generates high-resolution PNG and PDF vector figures in revision_v2/figures/
Authors: Adarsh Singh, Sourav, Anamidhi Shrivastava
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

FIG_DIR = Path(__file__).resolve().parent.parent / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# Set publication style
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 8,
    "axes.labelsize": 8.5,
    "axes.titlesize": 9,
    "xtick.labelsize": 7.5,
    "ytick.labelsize": 7.5,
    "legend.fontsize": 7.5,
    "figure.titlesize": 9.5,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})


def generate_fig1_architecture():
    """Fig 1: Systems Architecture & Six-Layer Cascade Flowchart."""
    fig, ax = plt.subplots(figsize=(6.8, 3.2))
    ax.axis("off")

    boxes = [
        {"text": "Policy Targets\n(200k / 500k / 1M GPUs)\nIndiaAI & Semicon 2.0", "xy": (0.08, 0.5), "color": "#1A365D", "w": 0.16, "h": 0.55},
        {"text": "Layer 1: IT Load\nBoard TDP: 700-1000W\nServer Overhead R_host: 1.82\n(637.0 MW @ 500k)", "xy": (0.28, 0.5), "color": "#2B6CB0", "w": 0.16, "h": 0.55},
        {"text": "Layer 2: Facility & Grid\nPUE: 1.25-1.55 (Base 1.40)\n891.8 MW Peak Power\n6.25 TWh Annual (0.80 U)", "xy": (0.48, 0.5), "color": "#2C7A7B", "w": 0.16, "h": 0.55},
        {"text": "Layer 3: Thermal & Water\nWUE: 0.12 - 1.80 L/kWh\n11,250 ML/yr Evaporative\n10,617 Racks (@ 60 kW)", "xy": (0.68, 0.75), "color": "#D69E2E", "w": 0.16, "h": 0.38},
        {"text": "Layer 4: Silicon Logic\nMurphy Yield (D0=0.08, A=814)\n12,500 Wafer Starts\n1.60% of TSMC Sub-5nm", "xy": (0.68, 0.28), "color": "#C53030", "w": 0.16, "h": 0.38},
        {"text": "Layers 5 & 6: Chokepoints\nCoWoS: 33,334 Wafers (7.41%)\nHBM3e: 4.0M Stacks (6.67%)\nTrue Binding Bottlenecks", "xy": (0.90, 0.5), "color": "#742A2A", "w": 0.15, "h": 0.55},
    ]

    for b in boxes:
        x, y = b["xy"]
        w, h = b["w"], b["h"]
        rect = plt.Rectangle((x - w/2, y - h/2), w, h, facecolor=b["color"], edgecolor="black", linewidth=1.0, alpha=0.9, transform=ax.transAxes, zorder=2)
        ax.add_patch(rect)
        ax.text(x, y, b["text"], color="white", weight="bold", ha="center", va="center", fontsize=6.8, transform=ax.transAxes, zorder=3)

    # Connecting arrows
    arrows = [
        ((0.16, 0.5), (0.20, 0.5)),
        ((0.36, 0.5), (0.40, 0.5)),
        ((0.56, 0.6), (0.60, 0.75)),
        ((0.56, 0.4), (0.60, 0.28)),
        ((0.76, 0.75), (0.825, 0.6)),
        ((0.76, 0.28), (0.825, 0.4)),
    ]
    for start, end in arrows:
        ax.annotate("", xy=end, xytext=start, xycoords="axes fraction", textcoords="axes fraction",
                    arrowprops=dict(arrowstyle="->", lw=1.5, color="#2D3748"))

    ax.set_title("Fig. 1. Six-Layer Demand-Cascade Architecture: From Policy Targets to Microelectronics and Power Grids", pad=10, weight="bold")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "fig1_demand_cascade_architecture.png")
    plt.savefig(FIG_DIR / "fig1_demand_cascade_architecture.pdf")
    plt.close()
    print("  [OK] Fig 1 generated.")


def generate_fig2_chokepoint_inversion():
    """Fig 2: The Structural Chokepoint Inversion (Bottleneck Comparison Bar Chart)."""
    fig, ax = plt.subplots(figsize=(5.5, 3.2))

    categories = [
        "Front-End Wafer Starts\n(TSMC Sub-5nm Share)",
        "2.5D CoWoS Packaging\n(Global Capacity Share)",
        "HBM3e Memory Stacks\n(Global Output Share)",
        "Colocation Facility Power\n(India Operational Capacity)",
        "Colocation Facility Power\n(India 2030 Pipeline)",
    ]
    shares = [1.60, 7.41, 6.67, 56.62, 27.87]
    colors = ["#3182CE", "#E53E3E", "#DD6B20", "#805AD5", "#38A169"]

    bars = ax.barh(categories, shares, color=colors, edgecolor="black", height=0.55, zorder=3)
    ax.set_xlim(0, 65)
    ax.set_xlabel("Required Share of Global / National Capacity (%)", weight="bold")
    ax.grid(axis="x", linestyle="--", alpha=0.6, zorder=0)

    for bar, val in zip(bars, shares):
        ax.text(val + 1.2, bar.get_y() + bar.get_height()/2, f"{val:.1f}%", va="center", weight="bold", fontsize=7.5)

    # Annotate the inversion
    ax.annotate("Silicon Wafer Fallacy:\nOnly 1.6% of TSMC\n(Easily absorbed)",
                xy=(1.60, 0), xytext=(12, 0.2),
                arrowprops=dict(arrowstyle="->", color="#2B6CB0", lw=1.2),
                fontsize=6.8, weight="bold", color="#2B6CB0")

    ax.annotate("True Hardware Chokepoint:\nCoWoS packaging is 4.6x more\nconstrained than raw wafers!",
                xy=(7.41, 1), xytext=(20, 1.25),
                arrowprops=dict(arrowstyle="->", color="#C53030", lw=1.2),
                fontsize=6.8, weight="bold", color="#C53030")

    ax.annotate("Immediate Physical Bottleneck:\n891.8 MW absorbs >56% of national\ncolocation datacenter capacity!",
                xy=(56.62, 3), xytext=(32, 2.7),
                arrowprops=dict(arrowstyle="->", color="#6B46C1", lw=1.2),
                fontsize=6.8, weight="bold", color="#6B46C1")

    ax.set_title("Fig. 2. The Structural Chokepoint Inversion (500,000-GPU Baseline Deployment)", weight="bold", pad=8)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "fig2_structural_chokepoint_inversion.png")
    plt.savefig(FIG_DIR / "fig2_structural_chokepoint_inversion.pdf")
    plt.close()
    print("  [OK] Fig 2 generated.")


def generate_fig3_country_comparison():
    """Fig 3: Cross-Country Comparative Infrastructure Benchmark (US vs. China vs. India)."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.8, 3.0))

    countries = ["United States", "China", "India (Current)", "India (500k Goal)"]
    compute_eflops = [1200, 450, 35, 245]  # EFLOPS FP16 equivalent
    dc_power_gw = [12.5, 8.2, 1.58, 2.47]  # Data center operational power GW

    # Panel A: Compute stock
    bars1 = ax1.bar(countries, compute_eflops, color=["#1A365D", "#C53030", "#CBD5E0", "#DD6B20"], edgecolor="black", width=0.55, zorder=3)
    ax1.set_ylabel("AI Compute Capacity (EFLOPS FP16 Equiv.)", weight="bold")
    ax1.set_title("A. Estimated Accelerated Compute Fleet", weight="bold")
    ax1.grid(axis="y", linestyle="--", alpha=0.6, zorder=0)
    ax1.set_xticklabels(["US", "China", "India\nCurrent", "India\n500k Plan"], rotation=0)
    for b in bars1:
        ax1.text(b.get_x() + b.get_width()/2, b.get_height() + 25, f"{int(b.get_height())}", ha="center", weight="bold", fontsize=7.2)

    # Panel B: Semiconductor Self-Sufficiency Radar/Bars
    stages = ["Sub-5nm Logic", "Advanced Pkg", "Chip Design/EDA", "Refined Gallium"]
    x = np.arange(len(stages))
    width = 0.25

    us_scores = [5, 5, 85, 0]      # Percent domestic or controlled
    cn_scores = [2, 3, 20, 98]
    in_scores = [0, 0, 20, 0.5]

    ax2.bar(x - width, us_scores, width, label="US", color="#1A365D", edgecolor="black", zorder=3)
    ax2.bar(x, cn_scores, width, label="China", color="#C53030", edgecolor="black", zorder=3)
    ax2.bar(x + width, in_scores, width, label="India", color="#DD6B20", edgecolor="black", zorder=3)

    ax2.set_ylabel("Domestic Self-Sufficiency (%)", weight="bold")
    ax2.set_title("B. Asymmetric Microelectronic Dependencies", weight="bold")
    ax2.set_xticks(x)
    ax2.set_xticklabels(["Sub-5nm\nLogic", "Advanced\nPackaging", "Design/\nWorkforce", "Refined\nGallium"])
    ax2.legend(loc="upper right", framealpha=0.9)
    ax2.grid(axis="y", linestyle="--", alpha=0.6, zorder=0)

    fig.suptitle("Fig. 3. Cross-National AI Infrastructure & Strategic Supply Chain Benchmarking", weight="bold", y=0.99)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "fig3_country_comparison_benchmark.png")
    plt.savefig(FIG_DIR / "fig3_country_comparison_benchmark.pdf")
    plt.close()
    print("  [OK] Fig 3 generated.")


def generate_fig4_cooling_pareto():
    """Fig 4: Cooling Technology Water-Energy Pareto Frontier across Indian Climatic Zones."""
    fig, ax = plt.subplots(figsize=(5.5, 3.2))

    technologies = {
        "Traditional Air (Evaporative)": {"pue": 1.45, "wue": 1.80, "marker": "o", "color": "#E53E3E"},
        "Rear-Door Heat Exchangers":     {"pue": 1.35, "wue": 1.00, "marker": "s", "color": "#DD6B20"},
        "Direct-to-Chip (D2C) Liquid":   {"pue": 1.18, "wue": 0.12, "marker": "^", "color": "#3182CE"},
        "Single-Phase Immersion":        {"pue": 1.12, "wue": 0.03, "marker": "D", "color": "#38A169"},
    }

    # Plot base points
    for name, d in technologies.items():
        ax.scatter(d["wue"], d["pue"], color=d["color"], s=75, marker=d["marker"], edgecolors="black", label=name, zorder=4)

    # Pareto curve
    wues = [1.80, 1.00, 0.12, 0.03]
    pues = [1.45, 1.35, 1.18, 1.12]
    sorted_pairs = sorted(zip(wues, pues))
    ax.plot([p[0] for p in sorted_pairs], [p[1] for p in sorted_pairs], color="#4A5568", linestyle="--", lw=1.2, zorder=3)

    # Regional Summer Penalty Zones
    ax.annotate("Navi Mumbai Summer:\nHigh Humidity Limits Evaporation\nPUE spikes to 1.62 under Air Cooling",
                xy=(1.80, 1.45), xytext=(1.25, 1.55),
                arrowprops=dict(arrowstyle="->", color="#C53030", lw=1.0),
                fontsize=6.5, weight="bold")

    ax.annotate("National Optimal Standard:\nD2C Liquid Cooling with Dry Coolers\nSlashes water by 93% and PUE to 1.18",
                xy=(0.12, 1.18), xytext=(0.40, 1.22),
                arrowprops=dict(arrowstyle="->", color="#2B6CB0", lw=1.0),
                fontsize=6.5, weight="bold")

    ax.set_xlabel("On-Site Cooling Water Intensity (WUE in Litres / kWh)", weight="bold")
    ax.set_ylabel("Power Usage Effectiveness (Annual PUE)", weight="bold")
    ax.set_ylim(1.05, 1.65)
    ax.set_xlim(-0.08, 2.10)
    ax.grid(True, linestyle="--", alpha=0.6, zorder=0)
    ax.legend(loc="upper left", framealpha=0.9, fontsize=7.0)

    ax.set_title("Fig. 4. Cooling Technology Water-Energy Pareto Frontier under Tropical Indian Ambient Profiles", weight="bold", pad=8)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "fig4_cooling_water_energy_pareto.png")
    plt.savefig(FIG_DIR / "fig4_cooling_water_energy_pareto.pdf")
    plt.close()
    print("  [OK] Fig 4 generated.")


def generate_fig5_sensitivity_tornado():
    """Fig 5: Multi-Parameter Global Sensitivity & Monte Carlo Uncertainty Tornado Plot."""
    fig, ax = plt.subplots(figsize=(5.5, 3.2))

    parameters = [
        "Cooling PUE (1.25 -> 1.55)",
        "Server Overhead R_host (1.60 -> 2.10)",
        "GPU TDP (700W -> 1000W)",
        "Murphy Defect D0 (0.06 -> 0.12 cm^-2)",
        "Capacity Utilization U (0.65 -> 0.90)",
        "Cooling WUE (0.20 -> 2.50 L/kWh)",
    ]

    # Percentage swing on primary metric (Facility Power MW or Wafer Starts)
    neg_swings = [-10.7, -12.1, -15.0, -11.1, -18.7, -88.9]  # Percentage decrease from base
    pos_swings = [10.7, 15.4, 42.8, 38.4, 12.5, 38.9]       # Percentage increase from base

    y_pos = np.arange(len(parameters))

    ax.barh(y_pos, neg_swings, color="#3182CE", edgecolor="black", height=0.5, label="Low Parameter Bound (-Δ%)", zorder=3)
    ax.barh(y_pos, pos_swings, color="#E53E3E", edgecolor="black", height=0.5, label="High Parameter Bound (+Δ%)", zorder=3)

    ax.axvline(0, color="black", lw=1.0, zorder=4)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(parameters, fontsize=7.2)
    ax.set_xlabel("Impact on Peak Facility Power / Resource Consumption (%)", weight="bold")
    ax.set_xlim(-100, 60)
    ax.grid(axis="x", linestyle="--", alpha=0.6, zorder=0)
    ax.legend(loc="lower right", framealpha=0.9, fontsize=7.0)

    ax.set_title("Fig. 5. One-at-a-Time Parameter Sensitivity & Uncertainty Tornado (500k GPUs)", weight="bold", pad=8)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "fig5_sensitivity_tornado_montecarlo.png")
    plt.savefig(FIG_DIR / "fig5_sensitivity_tornado_montecarlo.pdf")
    plt.close()
    print("  [OK] Fig 5 generated.")


if __name__ == "__main__":
    print("Generating 5 Publication-Grade Vector Figures for Revision v2...")
    generate_fig1_architecture()
    generate_fig2_chokepoint_inversion()
    generate_fig3_country_comparison()
    generate_fig4_cooling_pareto()
    generate_fig5_sensitivity_tornado()
    print("All 5 figures generated successfully in revision_v2/figures/.")
