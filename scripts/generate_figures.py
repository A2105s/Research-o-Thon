"""Generate monochrome, publication-grade figures for the ResearchThon 2026 paper."""

from pathlib import Path
import shutil

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parent.parent
FIG_DIR = ROOT / "figures"
MANUSCRIPT_FIG_DIR = ROOT / "manuscript" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)
MANUSCRIPT_FIG_DIR.mkdir(parents=True, exist_ok=True)

BLACK = "#141414"
CHARCOAL = "#333333"
DARK_GREY = "#595959"
MID_GREY = "#8C8C8C"
LIGHT_GREY = "#C9C9C9"
PALE_GREY = "#F2F2F2"
NAVY = "#4472C4"
DARK_RED = "#C00000"
FOREST = "#70AD47"
AMBER = "#BF8F00"
HATCHES = ("///", "xxx", "\\\\", "+++", "...", "OOO")

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
    "font.size": 8.5,
    "axes.labelsize": 8.5,
    "axes.titlesize": 9,
    "axes.titleweight": "bold",
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 7.4,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.04,
    "axes.edgecolor": BLACK,
    "axes.linewidth": 0.65,
    "grid.color": "#A8A8A8",
    "grid.linewidth": 0.35,
    "grid.alpha": 0.35,
})


def save(name):
    fig = plt.gcf()
    fig.savefig(FIG_DIR / f"{name}.pdf")
    fig.savefig(FIG_DIR / f"{name}.png")
    fig.savefig(FIG_DIR / f"{name}.svg")
    plt.close(fig)


def base_axes(ax, grid="y"):
    ax.grid(axis=grid, linestyle=":", linewidth=0.35, alpha=0.35, zorder=0)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(BLACK)
    ax.spines["bottom"].set_color(BLACK)


def box(ax, text, centre, width, height, fill, fontsize=6.4):
    x, y = centre
    patch = FancyBboxPatch(
        (x - width / 2, y - height / 2), width, height,
        boxstyle="round,pad=0.008,rounding_size=0.012",
        facecolor=fill, edgecolor=BLACK, linewidth=0.7, hatch=None,
        transform=ax.transAxes, zorder=2, alpha=0.98)
    ax.add_patch(patch)
    ax.text(x, y - height / 2 - 0.035, text, color=BLACK, ha="center", va="top",
            fontsize=6.1, weight="bold", transform=ax.transAxes, zorder=4,
            linespacing=1.08, bbox=dict(boxstyle="round,pad=0.16", fc="white",
            ec="none", alpha=0.92))


def arrow(ax, start, end):
    patch = FancyArrowPatch(start, end, connectionstyle="arc3,rad=0.0",
                            transform=ax.transAxes, arrowstyle="-|>",
                            mutation_scale=12, lw=1.15, color=BLACK, zorder=4,
                            capstyle="round", joinstyle="round")
    ax.add_patch(patch)


def figure1():
    fig, ax = plt.subplots(figsize=(7.0, 2.85))
    ax.axis("off")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    rows = [
        ("Policy targets\n200k / 500k / 1M GPUs", (0.09, 0.5), NAVY, 0.15, 0.52),
        ("Layer 1: IT load\n700-1,000 W/GPU\nhost factor 1.82", (0.265, 0.5), CHARCOAL, 0.13, 0.50),
        ("Layer 2: Facility\nPUE 1.40 base\n891.8 MW peak", (0.445, 0.5), CHARCOAL, 0.13, 0.50),
        ("Layer 3: Cooling\nWUE 0.12-1.80", (0.635, 0.755), DARK_GREY, 0.125, 0.26),
        ("Layer 4: Silicon\n12,500 wafer starts", (0.635, 0.245), DARK_GREY, 0.125, 0.26),
        ("Layers 5-6\n33,334 CoWoS\n4.0M HBM", (0.835, 0.5), DARK_RED, 0.13, 0.50),
    ]
    for text, centre, fill, width, height in rows:
        box(ax, text, centre, width, height, fill)

    for start, end in [((0.165, 0.5), (0.20, 0.5)), ((0.33, 0.5), (0.38, 0.5)),
                      ((0.51, 0.62), (0.572, 0.755)), ((0.51, 0.38), (0.572, 0.245)),
                      ((0.697, 0.755), (0.77, 0.62)), ((0.697, 0.245), (0.77, 0.38))]:
        arrow(ax, start, end)

    ax.text(0.9, 0.02, "Baseline values are for 500,000 GPUs.", transform=ax.transAxes,
            ha="right", va="bottom", fontsize=7, color=DARK_GREY)
    save("fig1_demand_cascade_architecture")


def figure2():
    categories = ["Wafer starts: TSMC share", "HBM3e: global output", "CoWoS: global capacity",
                  "Colocation power: 2030 pipeline", "Colocation power: mid-2026"]
    shares = [1.60, 6.67, 7.41, 27.9, 56.62]
    fills = [LIGHT_GREY, MID_GREY, NAVY, DARK_GREY, DARK_RED]

    fig, ax = plt.subplots(figsize=(3.45, 2.8))
    y = np.arange(len(categories))
    bars = ax.barh(y, shares, height=0.54, color=fills, edgecolor=BLACK, linewidth=0.5,
                   zorder=3)
    ax.set_yticks(y)
    ax.set_yticklabels(categories)
    ax.set_xlabel("Required share of constrained capacity (%)")
    ax.set_xlim(0, 74)
    ax.invert_yaxis()
    base_axes(ax, grid="x")

    for bar, val in zip(bars, shares):
        ax.text(val + 0.9, bar.get_y() + bar.get_height() / 2, f"{val:.1f}%",
               va="center", ha="left", fontsize=7.6, color=BLACK)

    ax.text(0.98, 0.98, "Values are required shares at the 500,000-GPU baseline",
           transform=ax.transAxes, ha="right", va="top", fontsize=6.6, color=DARK_GREY)
    save("fig2_structural_chokepoint_inversion")


def figure3():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 2.95), gridspec_kw={"wspace": 0.42})
    fig.subplots_adjust(bottom=0.16)

    countries = ["US", "China", "India\nnow", "India\n500k plan"]
    compute = [1200, 450, 35, 245]
    bar_colors = [NAVY, DARK_RED, MID_GREY, LIGHT_GREY]
    bars = ax1.bar(countries, compute, color=bar_colors, width=0.62, edgecolor=BLACK,
                   linewidth=0.5, zorder=3)
    ax1.set_ylabel("AI compute (EFLOPS FP16 eq.)")
    ax1.set_title("(a) Accelerated compute stock")
    ax1.set_xticks(np.arange(len(countries)))
    ax1.set_xticklabels(countries, rotation=18, ha="right")
    base_axes(ax1)
    for bar, val in zip(bars, compute):
        ax1.text(bar.get_x() + bar.get_width() / 2, val + 22, f"{val:,}", ha="center", fontsize=7.2)

    stages = ["Sub-5 nm", "Packaging", "Design", "Gallium"]
    scores = ( (5, 5, 85, 0), (2, 3, 20, 99), (0, 0, 20, 0.5) )
    labels = ("US", "China", "India")
    fills = (NAVY, DARK_RED, LIGHT_GREY)
    x = np.arange(len(stages))
    w = 0.23
    for idx, (score, fill) in enumerate(zip(scores, fills)):
        ax2.bar(x + (idx - 1) * w, score, w, color=fill, edgecolor=BLACK,
                linewidth=0.4, zorder=3, label=labels[idx])
    ax2.set_xticks(x)
    ax2.set_xticklabels(stages)
    ax2.set_ylabel("Domestic self-sufficiency (%)")
    ax2.set_title("(b) Microelectronic dependencies")
    ax2.set_ylim(0, 108)
    base_axes(ax2)
    ax2.legend(loc="upper left", frameon=True, handlelength=1.0, fontsize=7.0)
    save("fig3_country_comparison_benchmark")


def figure4():
    tech = {
        "Traditional air": (1.80, 1.45, DARK_RED, "o"),
        "Rear-door HEX": (1.00, 1.35, AMBER, "s"),
        "D2C liquid": (0.12, 1.18, NAVY, "^"),
        "Immersion": (0.03, 1.12, FOREST, "D"),
    }
    fig, ax = plt.subplots(figsize=(3.45, 2.8))
    wue_values = []
    pue_values = []
    for name, (wue, pue, colour, marker) in tech.items():
        ax.scatter(wue, pue, s=74, color=PALE_GREY, marker=marker, edgecolors=colour,
                   linewidth=1.0, zorder=4, label=name)
        pass
        wue_values.append(wue)
        pue_values.append(pue)

    order = np.argsort(wue_values)
    curve_x = np.array(wue_values)[order]
    curve_y = np.array(pue_values)[order]
    ax.plot(curve_x, curve_y, color=DARK_GREY, linestyle="--", lw=0.95, zorder=3)
    ax.fill_between(curve_x, curve_y, color=PALE_GREY, alpha=0.35, zorder=2)

    ax.annotate("High summer humidity raises PUE and water use", xy=(1.80, 1.45),
               xytext=(0.82, 1.56), fontsize=7.0, color=BLACK, weight="bold",
               arrowprops=dict(arrowstyle="-", color=BLACK, lw=0.6))
    ax.annotate("D2C cooling cuts water use by 94.6%", xy=(0.12, 1.18), xytext=(0.34, 1.30),
               fontsize=7.0, color=BLACK, weight="bold",
               arrowprops=dict(arrowstyle="-", color=BLACK, lw=0.6))

    ax.set_xlabel("Cooling water intensity (WUE, L/kWh)")
    ax.set_ylabel("Annual PUE")
    ax.set_xlim(-0.08, 2.05)
    ax.set_ylim(1.05, 1.65)
    base_axes(ax, grid="both")
    ax.legend(loc="upper right", frameon=False, handlelength=1.1)
    save("fig4_cooling_water_energy_pareto")


def figure5():
    parameters = ["Cooling PUE (1.25 to 1.55)", "Utilization (0.65 to 0.90)", "Server overhead (1.60 to 2.10)",
                  "GPU TDP (700 to 1,000 W)", "Defect density (0.06 to 0.12)", "Cooling WUE (0.20 to 2.50 L/kWh)"]
    neg = [-10.7, -18.7, -12.1, -15.0, -11.1, -88.9]
    pos = [10.7, 12.5, 15.4, 42.8, 38.4, 38.9]

    fig, ax = plt.subplots(figsize=(3.45, 2.9))
    y = np.arange(len(parameters))
    ax.barh(y, neg, height=0.5, color=LIGHT_GREY, edgecolor=BLACK, zorder=3,
            label="Lower input bound")
    ax.barh(y, pos, height=0.5, color=NAVY, edgecolor=BLACK, zorder=3,
            label="Upper input bound")
    ax.axvline(0, color=BLACK, lw=0.8, zorder=4)
    ax.set_yticks(y)
    ax.set_yticklabels(parameters, fontsize=7.1)
    ax.set_xlabel("Relative change from base case (%)")
    ax.set_xlim(-96, 52)
    ax.invert_yaxis()
    base_axes(ax, grid="x")

    for yi, val in enumerate(pos):
        ax.text(val + 1.0, yi, f"+{val:.1f}%", ha="left", va="center", fontsize=6.7, color=BLACK)
    for yi, val in enumerate(neg):
        if val < -50:
            ax.text(val + 2.0, yi, f"{val:.1f}%", ha="left", va="center", fontsize=6.7, color=BLACK, weight="bold")
        else:
            ax.text(val - 1.0, yi, f"{val:.1f}%", ha="right", va="center", fontsize=6.7, color=BLACK)
    ax.legend(loc="upper left", frameon=False, handlelength=1.1)
    save("fig5_sensitivity_tornado_montecarlo")


def sync_outputs():
    for src in FIG_DIR.glob("fig*"):
        if src.is_file():
            shutil.copy2(src, MANUSCRIPT_FIG_DIR / src.name)


if __name__ == "__main__":
    figure1()
    figure2()
    figure3()
    figure4()
    figure5()
    sync_outputs()
    print(f"Updated monochrome publication-grade figures in {FIG_DIR} and {MANUSCRIPT_FIG_DIR}.")
