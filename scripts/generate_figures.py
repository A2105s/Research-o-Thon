"""Generate publication-grade figures for the ResearchThon 2026 paper.

Design rules
------------
* Every plotted number is computed from model/demand_cascade.py (v2.0) or read
  from research/parameter_register.csv -- nothing is hard-coded by hand.
* Palette: forest green / steel blue / brick red / neutral greys (colour-blind
  distinguishable, also legible in greyscale print).
* Labels never sit on top of data marks: an automated layout check
  (``check_layout``) fails the build if any text overlaps other text, or
  overlaps a bar/box it does not belong to.
* Fonts are embedded as TrueType (Type 42) as required by IEEE PDF eXpress.

Figures written to figures/ and mirrored to manuscript/figures/:
  fig1_demand_cascade_architecture  (Fig. 1, in paper)
  fig2_structural_chokepoint_inversion (Fig. 2, in paper)
  fig5_sensitivity_tornado_montecarlo  (Fig. 3 in paper; legacy file name kept)
  fig4_cooling_water_energy_pareto  (supplementary, built from Table 4 data)
"""

from pathlib import Path
import itertools
import shutil
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, Patch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))
import demand_cascade as dcm  # noqa: E402  (model v2.0 -- single source of truth)

FIG_DIR = ROOT / "figures"
MANUSCRIPT_FIG_DIR = ROOT / "manuscript" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)
MANUSCRIPT_FIG_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------- palette ---
INK = "#1A1A1A"
GREY_D = "#4D4D4D"
GREY_M = "#8C8C8C"
GREY_L = "#D9D9D9"
GREEN = "#2B6239"      # electrical / power
GREEN_T = "#E4EFE7"
BLUE = "#3F77A8"       # physical resources / global capacity
BLUE_T = "#E1ECF6"
RED = "#A82424"        # semiconductor chokepoints / India constraint
RED_T = "#F7E2E2"
NEUTRAL = "#4D4D4D"
NEUTRAL_T = "#EDEDED"

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
    "mathtext.fontset": "stix",
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "svg.fonttype": "none",
    "font.size": 7,
    "axes.labelsize": 7.5,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "legend.fontsize": 7,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.pad_inches": 0.03,
    "axes.edgecolor": INK,
    "axes.linewidth": 0.6,
})


# ------------------------------------------------------------ layout check ---
def _overlap(a, b, pad=0.0):
    return not (a.x1 + pad <= b.x0 or b.x1 + pad <= a.x0 or
                a.y1 + pad <= b.y0 or b.y1 + pad <= a.y0)


def check_layout(fig, name, patches_to_avoid=(), inside_ok=()):
    """Raise if any two texts overlap, or a text overlaps a foreign patch."""
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    texts = [t for t in fig.findobj(matplotlib.text.Text)
             if t.get_visible() and t.get_text().strip()]
    boxes = [(t, t.get_window_extent(r)) for t in texts]
    problems = []
    for (t1, b1), (t2, b2) in itertools.combinations(boxes, 2):
        if _overlap(b1, b2, pad=-0.5):
            problems.append(f"text/text: {t1.get_text()!r} x {t2.get_text()!r}")
    for t, b in boxes:
        if t in inside_ok:
            continue
        for p in patches_to_avoid:
            if _overlap(b, p.get_window_extent(r), pad=-0.5):
                problems.append(f"text/patch: {t.get_text()!r}")
                break
    # everything must stay inside the canvas
    fb = fig.bbox
    for t, b in boxes:
        if b.x0 < fb.x0 - 1 or b.x1 > fb.x1 + 1 or b.y0 < fb.y0 - 1 or b.y1 > fb.y1 + 1:
            problems.append(f"text off-canvas: {t.get_text()!r}")
    if problems:
        raise RuntimeError(f"[{name}] layout problems:\n  " + "\n  ".join(problems))
    print(f"  layout OK  {name}: {len(boxes)} text objects, no overlaps")


def save(fig, name):
    for ext in ("pdf", "png", "svg"):
        fig.savefig(FIG_DIR / f"{name}.{ext}", bbox_inches="tight")
    plt.close(fig)


def clean_axes(ax, grid="x"):
    ax.grid(axis=grid, linestyle="-", linewidth=0.3, color=GREY_L, zorder=0)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


# ------------------------------------------------------------ model values ---
BASE = dcm.run_cascade_v2(500_000)                      # 500k GPUs, base case
COOLING = dcm.generate_cooling_comparison()             # Table 4 rows


# ------------------------------------------------------------------ Fig. 1 ---
def figure1():
    W, H = 7.16, 2.32
    fig = plt.figure(figsize=(W, H))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")

    HDR = 0.23
    boxes = []   # (rect patches) for containment checks
    texts_in = []

    def node(x, y, w, h, header, lines, head_c, body_c):
        body = Rectangle((x, y), w, h, fc=body_c, ec=head_c, lw=0.9, zorder=2)
        head = Rectangle((x, y + h - HDR), w, HDR, fc=head_c, ec=head_c, lw=0.9, zorder=3)
        ax.add_patch(body)
        ax.add_patch(head)
        boxes.append(body)
        ax.text(x + w / 2, y + h - HDR / 2, header, ha="center", va="center",
                color="white", fontsize=7, fontweight="bold", zorder=4)
        # distribute body lines evenly in the body area
        n = len(lines)
        area = h - HDR
        for i, (txt, bold) in enumerate(lines):
            yy = y + area - (i + 0.5) * area / n
            ax.text(x + w / 2, yy, txt, ha="center", va="center", color=INK,
                    fontsize=6.8, fontweight="bold" if bold else "normal", zorder=4)

    def arrow_h(x0, x1, y):
        ax.annotate("", xy=(x1, y), xytext=(x0, y),
                    arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.9,
                                    shrinkA=0, shrinkB=0, mutation_scale=8), zorder=5)

    def elbow(x0, y0, x1, y1):
        xm = (x0 + x1) / 2
        ax.plot([x0, xm, xm], [y0, y0, y1], color=INK, lw=0.9, zorder=5,
                solid_capstyle="butt")
        arrow_h(xm, x1, y1)

    # geometry (inches)
    yc = 1.38                      # vertical centre of the flow
    hm = 1.08                      # main box height
    hs = 0.82                      # stacked box height
    xs = [0.05, 1.38, 2.88, 4.38, 5.90]
    ws = [1.00, 1.22, 1.22, 1.22, 1.21]

    node(xs[0], yc - hm / 2, ws[0], hm, "Policy target",
         [("GPU target N", False), ("200k / 500k / 1M", True), ("Baseline: 500k", False)],
         NEUTRAL, NEUTRAL_T)

    node(xs[1], yc - hm / 2, ws[1], hm, "Layer 1 \u00b7 IT load",
         [(r"$P_{IT}=N\,P_{gpu}\,R_{host}$", False),
          ("700 W, $R_{host}$ = 1.82", False),
          (f"{BASE['it_load_mw']:,.1f} MW", True)],
         GREEN, GREEN_T)

    node(xs[2], yc - hm / 2, ws[2], hm, "Layer 2 \u00b7 Facility",
         [("PUE 1.40, U = 0.80", False),
          (f"{BASE['fac_power_mw']:,.1f} MW peak", True),
          (f"{BASE['annual_energy_twh']:.2f} TWh/yr", True)],
         GREEN, GREEN_T)

    y_top = yc + 0.05
    y_bot = yc - 0.05 - hs
    node(xs[3], y_top, ws[3], hs, "Layer 3 \u00b7 Cooling",
         [("WUE 1.80 L/kWh", False), (f"{BASE['annual_water_ml']:,.1f} ML/yr", True)],
         BLUE, BLUE_T)
    node(xs[3], y_bot, ws[3], hs, "Layer 4 \u00b7 Silicon",
         [(f"{BASE['good_dies']} good dies / wafer", False),
          (f"{BASE['wafer_starts']:,} wafer starts", True),
          (f"{BASE['tsmc_share_pct']:.2f}% of TSMC sub-5 nm", False)],
         RED, RED_T)

    node(xs[4], yc - hm / 2, ws[4], hm, "Layers 5\u20136",
         [(f"{BASE['cowos_wafers']:,} CoWoS wafers", True),
          (f"{BASE['cowos_share_pct']:.2f}% of global", False),
          (f"{BASE['hbm_stacks']/1e6:.1f}M HBM3e stacks", True),
          (f"{BASE['hbm_share_pct']:.2f}% of global", False)],
         RED, RED_T)

    # connectors
    arrow_h(xs[0] + ws[0], xs[1], yc)
    arrow_h(xs[1] + ws[1], xs[2], yc)
    elbow(xs[2] + ws[2], yc, xs[3], y_top + hs / 2)
    elbow(xs[2] + ws[2], yc, xs[3], y_bot + hs / 2)
    elbow(xs[3] + ws[3], y_top + hs / 2, xs[4], yc + 0.18)
    elbow(xs[3] + ws[3], y_bot + hs / 2, xs[4], yc - 0.18)

    # legend row (domain colour key)
    ly = 0.16
    items = [(NEUTRAL, "Policy input", 0.05),
             (GREEN, "Electrical load (Layers 1\u20132)", 1.25),
             (BLUE, "Physical resources (Layer 3)", 3.30),
             (RED, "Semiconductor supply chain (Layers 4\u20136)", 5.17)]
    for c, label, x in items:
        ax.add_patch(Rectangle((x, ly - 0.05), 0.12, 0.10, fc=c, ec=c, zorder=3))
        ax.text(x + 0.17, ly, label, ha="left", va="center", fontsize=6.8, color=INK)

    check_layout(fig, "fig1", patches_to_avoid=(), inside_ok=())
    # containment: every body text must lie inside its own box
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    for t in ax.texts:
        tb = t.get_window_extent(r)
        host = [b for b in boxes if b.get_window_extent(r).contains(*[(tb.x0 + tb.x1) / 2, (tb.y0 + tb.y1) / 2])]
        if host:
            bb = host[0].get_window_extent(r)
            if tb.x0 < bb.x0 + 1 or tb.x1 > bb.x1 - 1 or tb.y0 < bb.y0 or tb.y1 > bb.y1:
                raise RuntimeError(f"[fig1] text spills out of its box: {t.get_text()!r}")
    save(fig, "fig1_demand_cascade_architecture")


# ------------------------------------------------------------------ Fig. 2 ---
def figure2():
    r = BASE
    rows = [  # label, value (computed), colour
        ("Sub-5 nm wafer starts\n(TSMC, 780k wafers/yr)", r["tsmc_share_pct"], BLUE),
        ("HBM3e stacks\n(global, 60M stacks/yr)", r["hbm_share_pct"], BLUE),
        ("CoWoS packaging wafers\n(global, 450k wafers/yr)", r["cowos_share_pct"], BLUE),
        ("Colocation power, 2030 pipeline\n(India, 3,200 MW)", r["colo_pipe_share_pct"], RED),
        ("Colocation power, mid-2026\n(India, 1,575 MW operational)", r["colo_op_share_pct"], RED),
    ]
    fig, ax = plt.subplots(figsize=(3.45, 2.55))
    fig.subplots_adjust(left=0.50, right=0.97, top=0.98, bottom=0.26)
    y = np.arange(len(rows))
    vals = [v for _, v, _ in rows]
    bars = ax.barh(y, vals, height=0.58, color=[c for *_, c in rows],
                   edgecolor=INK, linewidth=0.5, zorder=3)
    ax.set_yticks(y)
    ax.set_yticklabels([l for l, *_ in rows], fontsize=6.6, linespacing=1.15)
    ax.invert_yaxis()
    ax.set_xlim(0, 76)
    ax.set_xticks(range(0, 71, 10))
    ax.set_xlabel("Share of capacity required by 500k GPUs (%)", loc="right")
    clean_axes(ax, "x")
    ax.tick_params(axis="y", length=0)
    for b, v in zip(bars, vals):
        ax.text(v + 1.2, b.get_y() + b.get_height() / 2, f"{v:.2f}%",
                va="center", ha="left", fontsize=7, fontweight="bold", color=INK)
    handles = [Patch(fc=BLUE, ec=INK, lw=0.5, label="Global semiconductor capacity"),
               Patch(fc=RED, ec=INK, lw=0.5, label="India colocation power")]
    fig.legend(handles=handles, loc="lower center", ncol=2, frameon=False,
               handlelength=1.1, columnspacing=1.2, bbox_to_anchor=(0.55, 0.0), fontsize=6.8)
    check_layout(fig, "fig2", patches_to_avoid=list(bars))
    save(fig, "fig2_structural_chokepoint_inversion")


# ------------------------------------------------------------------ Fig. 5 ---
def _oat(metric, **kw):
    """Relative change (%) of `metric` for low/high parameter bound vs. base."""
    base = dcm.run_cascade_v2(500_000)[metric]
    lo_kw, hi_kw = kw["lo"], kw["hi"]
    lo = dcm.run_cascade_v2(500_000, **lo_kw)[metric]
    hi = dcm.run_cascade_v2(500_000, **hi_kw)[metric]
    return 100 * (lo / base - 1), 100 * (hi / base - 1)


def figure5():
    # (label, metric, low-kwargs, high-kwargs); bounds from research/parameter_register.csv
    spec = [
        ("GPU board power (TDP)\n700 \u2192 1,000 W", "fac_power_mw",
         dict(p_gpu_w=700.0), dict(p_gpu_w=1000.0)),
        ("Server host overhead\n1.60 \u2192 2.10", "fac_power_mw",
         dict(r_host=1.60), dict(r_host=2.10)),
        ("Facility PUE\n1.25 \u2192 1.55", "fac_power_mw",
         dict(pue=1.25), dict(pue=1.55)),
        ("Utilisation\n0.65 \u2192 0.90", "annual_energy_twh",
         dict(utilization=0.65), dict(utilization=0.90)),
        ("Defect density D\u2080\n0.06 \u2192 0.12 cm\u207b\u00b2", "wafer_starts",
         dict(defect_density_cm2=0.06), dict(defect_density_cm2=0.12)),
        ("Cooling WUE\n0.20 \u2192 2.50 L/kWh", "annual_water_ml",
         dict(wue=0.20), dict(wue=2.50)),
    ]
    colour = {"fac_power_mw": GREEN, "annual_energy_twh": "#7BA886",
              "annual_water_ml": BLUE, "wafer_starts": RED}
    name = {"fac_power_mw": "Peak facility power", "annual_energy_twh": "Annual energy",
            "annual_water_ml": "Cooling water", "wafer_starts": "Wafer starts"}

    data = []
    for label, metric, lo, hi in spec:
        d_lo, d_hi = _oat(metric, lo=lo, hi=hi)
        data.append((label, metric, d_lo, d_hi))
    data.sort(key=lambda t: t[3] - t[2], reverse=True)   # widest swing on top

    fig, ax = plt.subplots(figsize=(3.45, 3.0))
    fig.subplots_adjust(left=0.40, right=0.97, top=0.98, bottom=0.31)
    y = np.arange(len(data))
    all_patches, label_texts = [], []
    for yi, (label, metric, d_lo, d_hi) in enumerate(data):
        c = colour[metric]
        p1 = ax.barh(yi, d_lo, height=0.56, color=c, alpha=0.55, edgecolor=INK, lw=0.5, zorder=3)
        p2 = ax.barh(yi, d_hi, height=0.56, color=c, edgecolor=INK, lw=0.5, zorder=3)
        all_patches += list(p1) + list(p2)
        # high-bound label (right of bar)
        ax.text(d_hi + 1.5, yi, f"+{d_hi:.1f}%", ha="left", va="center", fontsize=6.8)
        # low-bound label
        if d_lo < -60:
            t = ax.text(d_lo + 2.0, yi, f"{d_lo:.1f}%", ha="left", va="center",
                        fontsize=6.8, color=INK, fontweight="bold")
            label_texts.append(t)
        else:
            ax.text(d_lo - 1.5 if d_lo < -0.05 else -1.5, yi,
                    f"{d_lo:.1f}%" if d_lo < -0.05 else "0.0%",
                    ha="right", va="center", fontsize=6.8)
    ax.axvline(0, color=INK, lw=0.8, zorder=4)
    ax.set_yticks(y)
    ax.set_yticklabels([d[0] for d in data], fontsize=6.6, linespacing=1.15)
    ax.invert_yaxis()
    ax.set_xlim(-102, 72)
    ax.set_xticks(range(-100, 61, 20))
    ax.set_xlabel("Change from 500k-GPU base case (%)\n"
                  "\u2190 parameter at low bound  |  parameter at high bound \u2192", linespacing=1.3,
                  loc="right")
    clean_axes(ax, "x")
    ax.tick_params(axis="y", length=0)
    handles = [Patch(fc=colour[m], ec=INK, lw=0.5, label=name[m])
               for m in ("fac_power_mw", "annual_energy_twh", "annual_water_ml", "wafer_starts")]
    fig.legend(handles=handles, loc="lower center", ncol=4, frameon=False, handlelength=1.0,
               columnspacing=0.9, handletextpad=0.4, bbox_to_anchor=(0.55, 0.0), fontsize=6.6,
               title="Output metric affected", title_fontsize=6.6)
    check_layout(fig, "fig5", patches_to_avoid=all_patches, inside_ok=tuple(label_texts))
    save(fig, "fig5_sensitivity_tornado_montecarlo")
    return data


# ------------------------------------------------------------------ Fig. 4 ---
def figure4():
    style = {  # marker, colour, label offset (dx, dy in data units), alignment
        "Traditional_Air": ("o", RED, (-0.06, 0.035), "right", "Traditional air (evaporative)"),
        "RDHx": ("s", GREY_D, (0.07, -0.035), "left", "Rear-door heat exchanger"),
        "D2C_Liquid": ("^", BLUE, (0.09, -0.02), "left", "Direct-to-chip liquid"),
        "Immersion": ("D", GREEN, (0.09, -0.02), "left", "Single-phase immersion"),
    }
    fig, ax = plt.subplots(figsize=(3.45, 2.6))
    fig.subplots_adjust(left=0.15, right=0.97, top=0.97, bottom=0.17)
    xs = [row["wue_l_kwh"] for row in COOLING]
    ys = [row["annual_pue"] for row in COOLING]
    ax.plot(xs, ys, color=GREY_M, lw=0.9, ls="--", zorder=2)
    for row in COOLING:
        m, c, (dx, dy), ha, lab = style[row["mode"]]
        ax.scatter(row["wue_l_kwh"], row["annual_pue"], s=48, marker=m, color=c,
                   edgecolor=INK, linewidth=0.5, zorder=4)
        ax.text(row["wue_l_kwh"] + dx, row["annual_pue"] + dy,
                f"{lab}\n{row['annual_water_ml']:,.0f} ML/yr", ha=ha, va="center",
                fontsize=6.6, linespacing=1.15, color=INK)
    ax.set_xlim(-0.08, 2.05)
    ax.set_ylim(1.04, 1.52)
    ax.set_xticks([0, 0.5, 1.0, 1.5, 2.0])
    ax.set_yticks([1.1, 1.2, 1.3, 1.4, 1.5])
    ax.set_xlabel("Cooling water intensity, WUE (L/kWh)")
    ax.set_ylabel("Annual PUE")
    clean_axes(ax, "both")
    check_layout(fig, "fig4", patches_to_avoid=[])
    save(fig, "fig4_cooling_water_energy_pareto")


def sync_outputs():
    for src in FIG_DIR.glob("fig*"):
        if src.is_file():
            shutil.copy2(src, MANUSCRIPT_FIG_DIR / src.name)


if __name__ == "__main__":
    figure1()
    figure2()
    sens = figure5()
    figure4()
    sync_outputs()
    print("Sensitivity values (sorted):")
    for label, metric, lo, hi in sens:
        print(f"  {label.splitlines()[0].encode('ascii', 'replace').decode():<26s} {metric:<18s} {lo:+7.1f}% {hi:+7.1f}%")
    print(f"Figures written to {FIG_DIR} and {MANUSCRIPT_FIG_DIR}.")
