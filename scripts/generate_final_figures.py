"""
Master Publication Figures Generator for Five-Pillar AI Infrastructure Paper
=============================================================================
Generates 6 publication-quality figures (PDF + 300 DPI PNG):
  1. fig1_five_pillar_framework: Five-Pillar Conceptual Architecture (IAIPF)
  2. fig2_cross_pillar_dependencies: Cross-Pillar Dependency & Constraint Interaction Map
  3. fig3_country_comparison: Multi-Pillar Comparable Benchmarking (India, US, China)
  4. fig4_metro_concentration: Indian Metro Infrastructure Concentration Landscape
  5. fig5_demand_cascade_scenarios: Supporting Demand Cascade Scaling & Chokepoint Inversion
  6. fig6_cooling_pareto: Tropical Cooling Water vs Energy Pareto Frontier
"""

import sys
import os
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

_ROOT = Path(r"D:\research 2.0\ResearchThon_Final")
_OUT_DIR = _ROOT / "manuscript" / "figures"
_OUT_DIR.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    'font.sans-serif': 'DejaVu Sans',
    'font.family': 'sans-serif',
    'figure.autolayout': True,
    'axes.edgecolor': '#333333',
    'axes.linewidth': 0.8,
    'grid.color': '#E0E0E0',
    'grid.linestyle': '--',
    'grid.linewidth': 0.5,
})

# =====================================================================
# FIGURE 1: Five-Pillar Conceptual Framework Architecture
# =====================================================================
def generate_fig1():
    print("Generating Figure 1: Five-Pillar Framework Architecture...")
    fig, ax = plt.subplots(figsize=(10, 6.2), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Title Banner
    ax.text(50, 96, "INDIA AI INFRASTRUCTURE PLANNING FRAMEWORK (IAIPF)", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#0F1923')
    ax.text(50, 92, "A Resource-Bounded Structural Architecture for National Sovereign AI Capability", 
            ha='center', va='center', fontsize=8.5, color='#455A64', fontstyle='italic')

    # Central Core: Supporting Demand-Cascade Quantitative Engine
    core_box = patches.FancyBboxPatch((32, 36), 36, 26, boxstyle="round,pad=1.2,rounding_size=3", 
                                      ec="#D32F2F", fc="#FFEBEE", lw=1.8)
    ax.add_patch(core_box)
    ax.text(50, 56, "SUPPORTING QUANTITATIVE ENGINE:\nSIX-LAYER DEMAND-CASCADE", ha='center', va='center', 
            fontsize=9.0, fontweight='bold', color='#B71C1C')
    ax.text(50, 48, "Scenario Modeling: 200k / 500k / 1M Accelerators\nLayer 1: IT Load -> Layer 2: Facility Power & Energy\nLayer 3: Water -> Layer 4-6: Wafers, CoWoS, HBM", 
            ha='center', va='center', fontsize=7.2, color='#37474F')
    ax.text(50, 40, "Translates Fleet Targets into Physical Resource Demands", ha='center', va='center', 
            fontsize=6.8, fontweight='bold', color='#C62828')

    # 5 Conceptual Pillars around the perimeter
    pillars = [
        {"num": "1", "title": "Compute & Semiconductor\nSovereignty", 
         "desc": "Sub-5nm Fabs (India 0% vs TSMC 92%)\nCoWoS 2.5D Packaging (8,100 HHI)\nHBM3e Triopoly & Red Mud Gallium\n120k VLSI Design Engineers (GCCs)", 
         "pos": (5, 62), "color": "#1565C0", "bg": "#E3F2FD"},
        {"num": "2", "title": "Energy & Grid\nReadiness", 
         "desc": "National Peak Demand (250 GW in 2026)\nCEA Interconnect Queues (18--36 mos)\nFeeder Substations (18x 50 MW at 500k)\nCEA Cybersecurity Rules (>=50 MW)", 
         "pos": (65, 62), "color": "#E65100", "bg": "#FFF3E0"},
        {"num": "3", "title": "Data Centres &\nPhysical Resources", 
         "desc": "Operational DC Capacity (1,575 MW)\nMumbai Metro Concentration (52.4%)\nTropical PUE Penalty (1.55 vs 1.22 US)\nD2C Liquid Cooling (94.6% Water Drop)", 
         "pos": (5, 8), "color": "#00695C", "bg": "#E0F2F1"},
        {"num": "4", "title": "Connectivity, Data &\nSecure Computing", 
         "desc": "17+ Subsea Cable Landings (BOM/MAA)\nIndic Tokenization Deficit (4--8 tok/word)\nAI Kosh (14,000 Datasets, 331 Checkpoints)\nDPDP Act 2023 & Sarvam/BharatGen", 
         "pos": (35, 4), "color": "#4A148C", "bg": "#F3E5F5"},
        {"num": "5", "title": "Governance, Investment\n& Indigenous Capability", 
         "desc": "IndiaAI (Rs 10,372 cr) & Semicon 2.0 (Rs 1.27L cr)\nSubsidized Compute (Rs 65/hr vs $2.80 cloud)\nCoordinated Specialization (N-2 Problem)\nPax Silica Coalition & Quad Supply Alliance", 
         "pos": (65, 8), "color": "#37474F", "bg": "#ECEFF1"},
    ]

    for p in pillars:
        x, y = p["pos"]
        w = 30 if p["num"] != "4" else 28
        h = 24 if p["num"] != "4" else 22
        box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=1.0,rounding_size=2", 
                                     ec=p["color"], fc=p["bg"], lw=1.4)
        ax.add_patch(box)
        ax.text(x + w/2, y + h - 5, f"PILLAR {p['num']}: {p['title']}", ha='center', va='center', 
                fontsize=7.8, fontweight='bold', color=p["color"])
        ax.text(x + w/2, y + (h/2) - 3, p["desc"], ha='center', va='center', 
                fontsize=6.4, color='#263238', multialignment='center')

    # Draw Bidirectional Coupling Arrows
    arrow_props = dict(arrowstyle="<->,head_width=0.35,head_length=0.5", color="#546E7A", lw=1.2)
    ax.annotate("", xy=(32, 68), xytext=(38, 58), arrowprops=arrow_props) # P1 <-> Core
    ax.annotate("", xy=(68, 68), xytext=(62, 58), arrowprops=arrow_props) # P2 <-> Core
    ax.annotate("", xy=(32, 30), xytext=(38, 40), arrowprops=arrow_props) # P3 <-> Core
    ax.annotate("", xy=(49, 28), xytext=(49, 36), arrowprops=arrow_props) # P4 <-> Core
    ax.annotate("", xy=(68, 30), xytext=(62, 40), arrowprops=arrow_props) # P5 <-> Core

    # Inter-pillar peripheral arrows
    dash_arrow = dict(arrowstyle="<->", color="#90A4AE", lw=1, ls="--")
    ax.annotate("", xy=(35, 74), xytext=(65, 74), arrowprops=dash_arrow) # P1 <-> P2
    ax.annotate("", xy=(20, 62), xytext=(20, 32), arrowprops=dash_arrow) # P1 <-> P3
    ax.annotate("", xy=(80, 62), xytext=(80, 32), arrowprops=dash_arrow) # P2 <-> P5
    ax.annotate("", xy=(35, 18), xytext=(45, 18), arrowprops=dash_arrow) # P3 <-> P4
    ax.annotate("", xy=(53, 18), xytext=(65, 18), arrowprops=dash_arrow) # P4 <-> P5

    for ext in ['.pdf', '.png']:
        plt.savefig(_OUT_DIR / f"fig1_five_pillar_framework{ext}", bbox_inches='tight', dpi=300)
    plt.close()
    print("  [OK] Figure 1 saved.")


# =====================================================================
# FIGURE 2: Cross-Pillar Dependency & Constraint Interaction Map
# =====================================================================
def generate_fig2():
    print("Generating Figure 2: Cross-Pillar Dependency Interaction Map...")
    fig, ax = plt.subplots(figsize=(9.5, 5.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "CROSS-PILLAR CONSTRAINT INTERACTION & DEPENDENCY PATHWAYS", 
            ha='center', va='center', fontsize=11.5, fontweight='bold', color='#0F1923')
    ax.text(50, 92, "How Structural Deficits in One Pillar Propagate Downstream to Constrain National AI Capability", 
            ha='center', va='center', fontsize=8.2, color='#455A64', fontstyle='italic')

    # Draw 4 Critical Cascade Pathways
    pathways = [
        {"title": "Pathway A: Spatial Clustering & Grid Lock-In",
         "p_from": "Pillar 4 (Subsea Cables)", "p_mid": "Pillar 3 (Data Centres)", "p_to": "Pillar 2 (Power Grid)",
         "desc": "Subsea cable landings in Mumbai (17+ systems) attract 52.4% of DC build-out -> Creates 892 MW local demand shock -> Exceeds 220kV substation capacity -> Triggers 18--36 month interconnection queues -> Strands deployed compute silicon.",
         "y": 68, "col": "#C62828"},
        {"title": "Pathway B: Tropical Thermodynamics & Water Competition",
         "p_from": "Pillar 3 (Physical Resources)", "p_mid": "Pillar 2 (Energy)", "p_to": "Pillar 5 (Social License)",
         "desc": "Monsoon ambient heat (>42 deg C) spikes PUE to 1.55 -> Conventional wet cooling consumes 11,250 ML/yr at 500k scale -> Direct competition with municipal drinking water in Mumbai & Chennai -> Forces transition to D2C liquid cooling.",
         "y": 46, "col": "#00695C"},
        {"title": "Pathway C: Semiconductor Chokepoint & Fiscal Inversion",
         "p_from": "Pillar 1 (Semiconductors)", "p_mid": "Pillar 5 (Governance)", "p_to": "Pillar 1 (Packaging Hub)",
         "desc": "Pursuing leading-edge sub-3nm fab requires >$30B capex (7--10 yr delay) -> Cascade proves wafer starts are only 1.6% of TSMC -> CoWoS packaging is 7.41% global chokepoint -> Refocuses policy toward OSAT/ATMP (Sanand/Morigaon).",
         "y": 24, "col": "#1565C0"},
        {"title": "Pathway D: Linguistic Inefficiency & Compute Multiplier",
         "p_from": "Pillar 4 (Indic Data)", "p_mid": "Pillar 1 (GPU Demand)", "p_to": "Pillar 2 (Grid Draw)",
         "desc": "Foreign LLM tokenizers allocate 4--8 tokens/word for Hindi/Tamil vs 1--2 for English -> 3--6x inference cost penalty -> Multiplies required compute stock -> Drives higher power grid demand -> Accelerates domestic model priority (Sarvam/BharatGen).",
         "y": 2, "col": "#6A1B9A"},
    ]

    for p in pathways:
        y = p["y"]
        box = patches.FancyBboxPatch((5, y), 90, 18, boxstyle="round,pad=1.0,rounding_size=1.5", 
                                     ec=p["col"], fc="#FAFAFA", lw=1.2)
        ax.add_patch(box)
        # Header strip
        ax.text(7, y + 14.5, p["title"], fontsize=8.0, fontweight='bold', color=p["col"])
        chain = f"[{p['p_from']}]  --->  [{p['p_mid']}]  --->  [{p['p_to']}]"
        ax.text(93, y + 14.5, chain, fontsize=6.8, fontweight='bold', color='#37474F', ha='right')
        ax.text(7, y + 6.5, p["desc"], fontsize=6.5, color='#263238', wrap=True)

    for ext in ['.pdf', '.png']:
        plt.savefig(_OUT_DIR / f"fig2_cross_pillar_dependencies{ext}", bbox_inches='tight', dpi=300)
    plt.close()
    print("  [OK] Figure 2 saved.")


# =====================================================================
# FIGURE 3: Multi-Pillar Country Benchmark (India vs US vs China)
# =====================================================================
def generate_fig3():
    print("Generating Figure 3: Multi-Pillar Country Comparison...")
    fig, axes = plt.subplots(1, 3, figsize=(11, 4.2), dpi=300)

    # Panel A: Data Centre Operational Capacity & Peak Grid Demand
    ax1 = axes[0]
    countries = ['India', 'China', 'United States']
    dc_capacity = [1575, 8200, 12500] # MW
    colors_dc = ['#FF9933', '#DE2910', '#0A3161']
    bars1 = ax1.bar(countries, dc_capacity, color=colors_dc, width=0.55, edgecolor='#333333', lw=0.8)
    ax1.set_ylabel("Operational Colocation DC (MW)", fontsize=8.0, fontweight='bold')
    ax1.set_title("(a) Operational Colocation Capacity\n(Comparable Operational Census)", fontsize=8.5, fontweight='bold')
    ax1.grid(axis='y', linestyle='--', alpha=0.5)
    for bar in bars1:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 250, f"{yval:,} MW", ha='center', va='bottom', fontsize=7.2, fontweight='bold')
    ax1.set_ylim(0, 15000)

    # Panel B: Semiconductor Value Chain Global Share (%)
    ax2 = axes[1]
    tiers = ['Sub-5nm Logic', '2.5D Packaging', 'HBM Memory', 'Refined Ga', 'VLSI Talent']
    india_shares = [0.0, 0.0, 0.0, 0.5, 20.0]
    us_shares = [4.0, 4.5, 5.0, 0.0, 35.0]
    china_shares = [1.5, 2.5, 0.8, 98.0, 15.0]

    x = np.arange(len(tiers))
    width = 0.25
    ax2.bar(x - width, india_shares, width, label='India', color='#FF9933', edgecolor='#333333', lw=0.6)
    ax2.bar(x, china_shares, width, label='China', color='#DE2910', edgecolor='#333333', lw=0.6)
    ax2.bar(x + width, us_shares, width, label='United States', color='#0A3161', edgecolor='#333333', lw=0.6)
    ax2.set_ylabel("Global Share (%)", fontsize=8.0, fontweight='bold')
    ax2.set_title("(b) Semiconductor Value Chain Shares\n(Frontier Fabs, OSAT & Minerals)", fontsize=8.5, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(tiers, rotation=25, ha='right', fontsize=7.0)
    ax2.legend(fontsize=7.0, loc='upper left')
    ax2.grid(axis='y', linestyle='--', alpha=0.5)
    ax2.set_ylim(0, 105)

    # Panel C: Public Capital Outlays for Semiconductor & Compute ($B USD)
    ax3 = axes[2]
    outlays = [16.55, 47.50, 52.70] # India: IndiaAI + ISM 2.0; China: Big Fund III; US: CHIPS Act
    bars3 = ax3.bar(countries, outlays, color=colors_dc, width=0.55, edgecolor='#333333', lw=0.8)
    ax3.set_ylabel("Statutory Public Outlays ($ Billion USD)", fontsize=8.0, fontweight='bold')
    ax3.set_title("(c) Sovereign Technology Outlays\n(Statutory Public Allocations)", fontsize=8.5, fontweight='bold')
    ax3.grid(axis='y', linestyle='--', alpha=0.5)
    for bar in bars3:
        yval = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2.0, yval + 1.2, f"${yval:.1f} B", ha='center', va='bottom', fontsize=7.2, fontweight='bold')
    ax3.set_ylim(0, 62)

    for ax in axes:
        ax.tick_params(labelsize=7.5)

    for ext in ['.pdf', '.png']:
        plt.savefig(_OUT_DIR / f"fig3_country_comparison{ext}", bbox_inches='tight', dpi=300)
    plt.close()
    print("  [OK] Figure 3 saved.")


# =====================================================================
# FIGURE 4: Indian Metro Infrastructure Concentration Landscape
# =====================================================================
def generate_fig4():
    print("Generating Figure 4: Indian Metro Concentration Landscape...")
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), dpi=300)

    metros = ['Mumbai', 'Chennai', 'Delhi-NCR', 'Bengaluru', 'Hyderabad', 'Pune']
    shares = [52.4, 18.6, 11.2, 8.5, 6.8, 2.5]
    colors_m = ['#D32F2F', '#E65100', '#F57C00', '#1976D2', '#388E3C', '#7B1FA2']

    # Panel A: Donut Chart of Colocation Capacity Share
    ax1 = axes[0]
    wedges, texts, autotexts = ax1.pie(shares, labels=metros, autopct='%1.1f%%', startangle=140,
                                      colors=colors_m, pctdistance=0.75,
                                      textprops={'fontsize': 7.5},
                                      wedgeprops=dict(width=0.45, edgecolor='#333333', lw=0.8))
    for at in autotexts:
        at.set_fontsize(6.8)
        at.set_weight('bold')
    ax1.set_title("(a) Operational Colocation Capacity by Metro\n(Total: 1,575 MW Mid-2026; JLL/CBRE)", fontsize=8.5, fontweight='bold')

    # Panel B: Metro Multi-Factor Constraint Index
    ax2 = axes[1]
    subsea_cables = [12, 5, 0, 0, 0, 0] # International cable landings
    substation_delay_mos = [30, 24, 18, 14, 12, 14] # Typical queue in months

    x = np.arange(len(metros))
    width = 0.38
    b1 = ax2.bar(x - width/2, subsea_cables, width, label='Subsea Cable Landings', color='#0288D1', edgecolor='#333333', lw=0.6)
    b2 = ax2.bar(x + width/2, substation_delay_mos, width, label='Substation Interconnect Queue (Mos)', color='#E64A19', edgecolor='#333333', lw=0.6)
    ax2.set_ylabel("Count / Months", fontsize=8.0, fontweight='bold')
    ax2.set_title("(b) Infrastructure Drivers & Constraints\n(Subsea Bandwidth vs Grid Substation Queue)", fontsize=8.5, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(metros, rotation=20, ha='right', fontsize=7.2)
    ax2.legend(fontsize=7.2, loc='upper right')
    ax2.grid(axis='y', linestyle='--', alpha=0.5)

    for ext in ['.pdf', '.png']:
        plt.savefig(_OUT_DIR / f"fig4_metro_concentration{ext}", bbox_inches='tight', dpi=300)
    plt.close()
    print("  [OK] Figure 4 saved.")


# =====================================================================
# FIGURE 5: Supporting Demand-Cascade Scaling & Chokepoint Inversion
# =====================================================================
def generate_fig5():
    print("Generating Figure 5: Demand-Cascade Scaling & Chokepoint Inversion...")
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), dpi=300)

    # Panel A: Physical Resources Scaling across 200k, 500k, 1M GPUs
    ax1 = axes[0]
    scenarios = ['200k GPUs', '500k GPUs\n(Baseline)', '1M GPUs']
    power_mw = [356.7, 891.8, 1783.6]
    energy_twh = [2.50, 6.25, 12.50]
    water_ml = [4499.8, 11249.5, 22499.0]

    x = np.arange(len(scenarios))
    width = 0.28
    ax1_t = ax1.twinx()

    bar1 = ax1.bar(x - width/2, power_mw, width, label='Facility Peak Power (MW)', color='#1976D2', edgecolor='#333333', lw=0.6)
    bar2 = ax1_t.bar(x + width/2, [w/1000 for w in water_ml], width, label='Water Dissipation (Billion L/yr)', color='#00796B', edgecolor='#333333', lw=0.6)

    ax1.set_ylabel("Peak Facility Power (MW)", color='#1976D2', fontsize=8.0, fontweight='bold')
    ax1_t.set_ylabel("Annual Water Dissipation (Billion Litres)", color='#00796B', fontsize=8.0, fontweight='bold')
    ax1.set_title("(a) Supporting Demand-Cascade Resource Scaling\n(Physical Demands Propagated Across Fleet Targets)", fontsize=8.5, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(scenarios, fontsize=7.5, fontweight='bold')
    ax1.grid(axis='y', linestyle='--', alpha=0.5)

    # Panel B: The Structural Chokepoint Inversion (500k GPUs)
    ax2 = axes[1]
    chokepoints = ['Colocation Grid\n(India Pipeline)', 'Colocation Grid\n(India Installed)', 'HBM3e Memory\n(Global Supply)', '2.5D CoWoS Pkg\n(Global Capacity)', 'Sub-5nm Wafers\n(TSMC Annual)']
    shares = [27.9, 56.62, 6.67, 7.41, 1.60] # %
    colors_c = ['#4CAF50', '#8BC34A', '#FF9800', '#F44336', '#2196F3']

    y_pos = np.arange(len(chokepoints))
    bars = ax2.barh(y_pos, shares, color=colors_c, edgecolor='#333333', lw=0.7)
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(chokepoints, fontsize=7.2)
    ax2.set_xlabel("Required Share of Capacity / Output (%)", fontsize=8.0, fontweight='bold')
    ax2.set_title("(b) The Structural Chokepoint Inversion\n(Packaging & Grid Far Exceed Raw Wafer Intensity)", fontsize=8.5, fontweight='bold')
    ax2.grid(axis='x', linestyle='--', alpha=0.5)

    for bar in bars:
        w = bar.get_width()
        ax2.text(w + 1.2, bar.get_y() + bar.get_height()/2.0, f"{w:.1f}%", ha='left', va='center', fontsize=7.2, fontweight='bold')
    ax2.set_xlim(0, 70)

    for ext in ['.pdf', '.png']:
        plt.savefig(_OUT_DIR / f"fig5_demand_cascade_scenarios{ext}", bbox_inches='tight', dpi=300)
    plt.close()
    print("  [OK] Figure 5 saved.")


# =====================================================================
# FIGURE 6: Cooling Water vs Energy Pareto Frontier
# =====================================================================
def generate_fig6():
    print("Generating Figure 6: Cooling Water vs Energy Pareto Frontier...")
    fig, ax = plt.subplots(figsize=(6.5, 4.2), dpi=300)

    techs = [
        {'name': 'Traditional Air (Evaporative)', 'pue': 1.45, 'wue': 1.80, 'col': '#D32F2F', 'marker': 'o'},
        {'name': 'Rear-Door Heat Exchangers', 'pue': 1.35, 'wue': 1.00, 'col': '#F57C00', 'marker': 's'},
        {'name': 'Direct-to-Chip (D2C) Liquid', 'pue': 1.18, 'wue': 0.12, 'col': '#1976D2', 'marker': '^'},
        {'name': 'Single-Phase Immersion', 'pue': 1.12, 'wue': 0.03, 'col': '#388E3C', 'marker': 'D'},
    ]

    for t in techs:
        ax.scatter(t['wue'], t['pue'], color=t['col'], s=100, marker=t['marker'], edgecolors='#333333', lw=1.0, label=t['name'], zorder=5)

    # Draw Pareto Curve
    wue_vals = [t['wue'] for t in techs]
    pue_vals = [t['pue'] for t in techs]
    ax.plot(wue_vals, pue_vals, color='#78909C', linestyle='--', lw=1.2, zorder=3)

    # Highlight National Standard (D2C)
    ax.annotate("National Optimal Standard:\nD2C Liquid with Dry Coolers\n(94.6% Water Reduction, PUE 1.18)",
                xy=(0.12, 1.18), xytext=(0.45, 1.22),
                arrowprops=dict(arrowstyle="->", color='#0D47A1', lw=1.5),
                fontsize=7.2, fontweight='bold', color='#0D47A1',
                bbox=dict(boxstyle="round,pad=0.5", fc="#E3F2FD", ec="#1565C0", lw=1))

    ax.set_xlabel("Water Usage Effectiveness - WUE (L/kWh)", fontsize=8.0, fontweight='bold')
    ax.set_ylabel("Power Usage Effectiveness - PUE (Annual)", fontsize=8.0, fontweight='bold')
    ax.set_title("Cooling Technology Water--Energy Pareto Frontier\n(Tropical Indian Climatic Context)", fontsize=8.5, fontweight='bold')
    ax.legend(fontsize=7.2, loc='upper left')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_xlim(-0.05, 2.05)
    ax.set_ylim(1.05, 1.55)

    for ext in ['.pdf', '.png']:
        plt.savefig(_OUT_DIR / f"fig6_cooling_pareto{ext}", bbox_inches='tight', dpi=300)
    plt.close()
    print("  [OK] Figure 6 saved.")


if __name__ == '__main__':
    generate_fig1()
    generate_fig2()
    generate_fig3()
    generate_fig4()
    generate_fig5()
    generate_fig6()
    print("\nAll 6 master figures generated successfully!")
