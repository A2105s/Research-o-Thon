"""
build_pdf_reportlab.py
======================
Generates a near-IEEE-style PDF for the ResearchThon 2026 paper using ReportLab.
All figures are embedded from manuscript/figures/. All tables are typeset inline.
Run from: D:\research 2.0\ResearchThon_Final\
"""

import os, sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer,
    Image, Table, TableStyle, HRFlowable, KeepTogether
)

# ── Paths ──────────────────────────────────────────────────────────────────
BASE = r"D:\research 2.0\ResearchThon_Final"
FIG_DIR = os.path.join(BASE, "manuscript", "figures")
OUT_DIR = os.path.join(BASE, "output")
os.makedirs(OUT_DIR, exist_ok=True)
OUT_PDF = os.path.join(OUT_DIR, "final_paper.pdf")

# ── Page Setup ─────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = letter
MARGIN_TOP    = 0.75 * inch
MARGIN_BOTTOM = 0.75 * inch
MARGIN_OUTER  = 0.65 * inch
MARGIN_INNER  = 0.65 * inch
COL_GAP       = 0.25 * inch
COL_W         = (PAGE_W - MARGIN_OUTER - MARGIN_INNER - COL_GAP) / 2

# ── Colours ────────────────────────────────────────────────────────────────
IEEE_BLUE   = colors.HexColor("#00629B")
HEADER_GREY = colors.HexColor("#F5F5F5")
ROW_EVEN    = colors.HexColor("#EAF3FB")
ROW_ODD     = colors.white
RULE_COLOR  = colors.HexColor("#CCCCCC")

# ── Styles ─────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def S(name, parent="Normal", **kw):
    return ParagraphStyle(name, parent=styles[parent], **kw)

title_style    = S("Title2", fontSize=14, leading=17, alignment=TA_CENTER,
                   textColor=IEEE_BLUE, spaceAfter=4, fontName="Helvetica-Bold")
author_style   = S("Author2", fontSize=10, leading=13, alignment=TA_CENTER,
                   spaceAfter=2, fontName="Helvetica")
affil_style    = S("Affil2", fontSize=8.5, leading=11, alignment=TA_CENTER,
                   textColor=colors.HexColor("#444444"), spaceAfter=6)
abstract_head  = S("AbsHead2", fontSize=9, leading=11, fontName="Helvetica-BoldOblique",
                   leftIndent=6, rightIndent=6, spaceAfter=2)
abstract_body  = S("AbsBody2", fontSize=8.5, leading=11, alignment=TA_JUSTIFY,
                   leftIndent=6, rightIndent=6, spaceAfter=4)
kw_style       = S("KW2", fontSize=8.5, leading=11, leftIndent=6, rightIndent=6,
                   spaceAfter=8)
sec_head       = S("SecHead2", fontSize=9.5, leading=12, fontName="Helvetica-Bold",
                   textColor=IEEE_BLUE, spaceBefore=8, spaceAfter=3)
subsec_head    = S("SubSecHead2", fontSize=9, leading=11.5, fontName="Helvetica-Bold",
                   spaceBefore=5, spaceAfter=2)
body_style     = S("Body2", fontSize=8.5, leading=11.5, alignment=TA_JUSTIFY,
                   spaceAfter=4)
bullet_style   = S("Bullet2", fontSize=8.5, leading=11.5, alignment=TA_JUSTIFY,
                   leftIndent=12, spaceAfter=2, bulletIndent=4)
enum_style     = S("Enum2", fontSize=8.5, leading=11.5, alignment=TA_JUSTIFY,
                   leftIndent=14, spaceAfter=2)
caption_style  = S("Caption2", fontSize=8, leading=10, alignment=TA_CENTER,
                   fontName="Helvetica-Oblique", spaceAfter=4, spaceBefore=2)
table_cap_style = S("TCap2", fontSize=8.5, leading=10, fontName="Helvetica-Bold",
                    alignment=TA_CENTER, spaceAfter=2, spaceBefore=6)
footnote_style = S("Footnote2", fontSize=7.5, leading=10, alignment=TA_JUSTIFY,
                   textColor=colors.HexColor("#555555"), spaceAfter=4)
ref_head_style = S("RefHead2", fontSize=9.5, leading=12, fontName="Helvetica-Bold",
                   textColor=IEEE_BLUE, spaceBefore=8, spaceAfter=3)
ref_style      = S("Ref2", fontSize=7.8, leading=10.5, alignment=TA_JUSTIFY,
                   leftIndent=14, firstLineIndent=-14, spaceAfter=2)
ack_style      = S("AckHead2", fontSize=8.5, leading=11, fontName="Helvetica-BoldOblique",
                   spaceAfter=2)

# ── Header / Footer ────────────────────────────────────────────────────────
def on_page(canvas_obj, doc):
    canvas_obj.saveState()
    canvas_obj.setStrokeColor(IEEE_BLUE)
    canvas_obj.setLineWidth(1.2)
    canvas_obj.line(MARGIN_OUTER, PAGE_H - MARGIN_TOP + 6,
                    PAGE_W - MARGIN_OUTER, PAGE_H - MARGIN_TOP + 6)
    canvas_obj.setFont("Helvetica", 7.5)
    canvas_obj.setFillColor(colors.HexColor("#666666"))
    canvas_obj.drawString(MARGIN_OUTER, 0.45 * inch,
                          "ResearchThon 2026 · Amity University MP · Draft for Review")
    canvas_obj.drawRightString(PAGE_W - MARGIN_OUTER, 0.45 * inch, f"Page {doc.page}")
    canvas_obj.setLineWidth(0.5)
    canvas_obj.setStrokeColor(RULE_COLOR)
    canvas_obj.line(MARGIN_OUTER, 0.60 * inch, PAGE_W - MARGIN_OUTER, 0.60 * inch)
    canvas_obj.restoreState()

# ── Helpers ────────────────────────────────────────────────────────────────
def fig(fname, caption, label_num, width=None):
    path = os.path.join(FIG_DIR, fname)
    w = width or (COL_W * 2 + COL_GAP)
    if not os.path.exists(path):
        return [Paragraph(f"[Figure {label_num} missing: {fname}]", caption_style)]
    return [
        Image(path, width=w, height=w * 0.55, kind="proportional"),
        Paragraph(f"<b>Fig. {label_num}.</b> {caption}", caption_style),
    ]

def rule(color=RULE_COLOR, thickness=0.5):
    return HRFlowable(width="100%", thickness=thickness, color=color,
                      spaceAfter=3, spaceBefore=3)

def sec(num, title):
    return [Paragraph(f"{num}. {title.upper()}", sec_head), rule(IEEE_BLUE, 0.8)]

def subsec(num, title):
    return [Paragraph(f"{num}  {title}", subsec_head)]

def P(text, style=None):
    return Paragraph(text, style or body_style)

def B(text):
    return Paragraph(f"• {text}", bullet_style)

def E(n, text):
    return Paragraph(f"({n}) {text}", enum_style)

def SP(h=4):
    return Spacer(1, h)

# ── Tables ─────────────────────────────────────────────────────────────────
def tbl_style_base():
    return [
        ("FONTSIZE",      (0, 0), (-1, -1), 7),
        ("LEADING",       (0, 0), (-1, -1), 9),
        ("BACKGROUND",    (0, 0), (-1, 0), IEEE_BLUE),
        ("TEXTCOLOR",     (0, 0), (-1, 0), colors.white),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("GRID",          (0, 0), (-1, -1), 0.4, colors.HexColor("#AAAAAA")),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]

def make_table_prior_art():
    data = [
        ["Source", "Methodology", "Scenarios", "Phys. Infra", "Micro-HW", "Repro."],
        ["Akimitsu 2026", "Econometric HHI", "None", "None", "HHI 40 stages", "Code"],
        ["Portulans 2026", "Qualitative policy", "Conceptual", "None", "Taxonomy", "Memo"],
        ["IEA / LBNL 2024", "Macro energy", "Global TWh", "PUE 1.15-1.25", "None", "Projections"],
        ["Inherited Draft", "Heuristic Vuln.", "10k/45k", "Qual. PUE 1.55", "Cites HHI", "Static PDF"],
        ["This Paper v2.0", "Demand Cascade", "200k/500k/1M", "MW,TWh,Water", "CoWoS,HBM", "Python"],
    ]
    full_w = COL_W * 2 + COL_GAP
    cw = [full_w*0.17, full_w*0.18, full_w*0.14, full_w*0.16, full_w*0.18, full_w*0.15]
    ts = tbl_style_base() + [
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [ROW_ODD, ROW_EVEN]*4),
        ("BACKGROUND",     (0, -1), (-1, -1), colors.HexColor("#D0E8F5")),
        ("FONTNAME",       (0, -1), (-1, -1), "Helvetica-Bold"),
        ("ALIGN",          (0, 0), (-1, -1), "CENTER"),
    ]
    tbl = Table(data, colWidths=cw, repeatRows=1)
    tbl.setStyle(TableStyle(ts))
    return tbl

def make_table_scenarios():
    data = [
        ["Scen.", "Var.", "IT MW", "Fac MW", "TWh/yr", "Water ML", "Wafers", "TSMC%", "CoWoS W", "CoWoS%", "Colo%"],
        ["200k", "Low",  "224",   "280",   "1.59",  "319",    "4,445",  "0.57%", "11,112", "2.47%", "17.78%"],
        ["",     "Base", "255",   "357",   "2.50",  "4,500",  "5,000",  "0.64%", "13,334", "2.96%", "22.65%"],
        ["",     "High", "420",   "651",   "5.13",  "12,832", "10,527", "1.35%", "16,667", "3.70%", "41.33%"],
        ["500k", "Low",  "560",   "700",   "3.99",  "797",    "11,112", "1.42%", "27,778", "6.17%", "44.44%"],
        ["",     "Base", "637",   "892",   "6.25",  "11,250", "12,500", "1.60%", "33,334", "7.41%", "56.62%"],
        ["",     "High", "1,050", "1,628", "12.83", "32,080", "26,316", "3.37%", "41,667", "9.26%","103.33%"],
        ["1M",   "Low",  "1,120", "1,400", "7.97",  "1,594",  "22,223", "2.85%", "55,556","12.35%","88.89%"],
        ["",     "Base", "1,274", "1,784", "12.50", "22,499", "25,000", "3.21%", "66,667","14.81%","113.24%"],
        ["",     "High", "2,100", "3,255", "25.66", "64,160", "52,632", "6.75%", "83,334","18.52%","206.67%"],
    ]
    full_w = COL_W * 2 + COL_GAP
    cw = [full_w*0.07]*2 + [full_w*0.09]*9
    ts = tbl_style_base() + [
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("ROWBACKGROUNDS",(0, 1), (-1, 3),  [ROW_ODD, ROW_ODD, ROW_ODD]),
        ("ROWBACKGROUNDS",(0, 4), (-1, 6),  [ROW_EVEN, ROW_EVEN, ROW_EVEN]),
        # Highlight 500k base row
        ("BACKGROUND",   (0, 6), (-1, 6),  colors.HexColor("#FFE4B5")),
        ("FONTNAME",     (0, 6), (-1, 6),  "Helvetica-Bold"),
        ("SPAN",         (0, 1), (0, 3)),
        ("SPAN",         (0, 4), (0, 6)),
        ("SPAN",         (0, 7), (0, 9)),
    ]
    tbl = Table(data, colWidths=cw, repeatRows=1)
    tbl.setStyle(TableStyle(ts))
    return tbl

def make_table_chokepoints():
    data = [
        ["Infrastructure Layer",          "HHI",   "India", "500k Share", "Lead Time"],
        ["EUV Lithography (ASML)",         "10,000","0%",   "Upstream",   "24-36 mos"],
        ["Sub-5nm Logic (TSMC)",           "5,400", "0%",   "1.60%",      "14-18 wks"],
        ["2.5D CoWoS Pkg (TSMC)",          "8,100", "0%",   "7.41%",      "20-28 wks"],
        ["HBM3e Memory (SK/Samsung)",      "4,950", "0%",   "6.67%",      "16-24 wks"],
        ["400kV Substations",             "2,200", "75%",  "56.62%",     "36-48 mos"],
        ["Colo. Water Rights",            "N/A",  "100%", "11,250 ML",  "Seasonal"],
    ]
    cw = [COL_W*0.95, COL_W*0.45, COL_W*0.45, COL_W*0.55, COL_W*0.60]
    ts = tbl_style_base() + [
        ("ALIGN",          (1, 0), (-1, -1), "CENTER"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [ROW_ODD, ROW_EVEN]*5),
        ("BACKGROUND",     (3, 3), (3, 4),   colors.HexColor("#FFD0D0")),
        ("BACKGROUND",     (3, 5), (3, 5),   colors.HexColor("#FFD0D0")),
        ("FONTNAME",       (0, 5), (-1, 5),  "Helvetica-Bold"),
    ]
    tbl = Table(data, colWidths=cw, repeatRows=1)
    tbl.setStyle(TableStyle(ts))
    return tbl

def make_table_cooling():
    data = [
        ["Cooling Technology",           "Ann. PUE","Sum. PUE","WUE L/kWh","Water ML"],
        ["Air Cooling (Evaporative)",    "1.45",    "1.65",    "1.80",     "11,651"],
        ["Rear-Door Heat Exchangers",    "1.35",    "1.45",    "1.00",     "6,032"],
        ["Direct-to-Chip (D2C) Liquid", "1.18",    "1.25",    "0.12",     "631"],
        ["Single-Phase Immersion",       "1.12",    "1.18",    "0.03",     "151"],
    ]
    cw = [COL_W*1.0, COL_W*0.52, COL_W*0.56, COL_W*0.58, COL_W*0.54]
    ts = tbl_style_base() + [
        ("FONTSIZE",       (0, 0), (-1, -1), 7.5),
        ("LEADING",        (0, 0), (-1, -1), 9.5),
        ("ALIGN",          (1, 0), (-1, -1), "CENTER"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [ROW_ODD, ROW_EVEN, ROW_ODD, ROW_EVEN]),
        ("BACKGROUND",     (0, 3), (-1, 3),  colors.HexColor("#C8F5C8")),
        ("FONTNAME",       (0, 3), (-1, 3),  "Helvetica-Bold"),
    ]
    tbl = Table(data, colWidths=cw, repeatRows=1)
    tbl.setStyle(TableStyle(ts))
    return tbl

# ── Story ──────────────────────────────────────────────────────────────────
story = []

story += [
    SP(6),
    Paragraph("A Demand-Driven Framework for India's AI Infrastructure Planning:<br/>"
              "Linking Compute, Energy, Physical Resources, and Semiconductor Dependencies",
              title_style),
    Paragraph("Adarsh Singh &nbsp;·&nbsp; Sourav &nbsp;·&nbsp; Anamidhi Shrivastava", author_style),
    Paragraph("Amity School of Engineering and Technology, Amity University Madhya Pradesh, Gwalior, India",
              affil_style),
    rule(IEEE_BLUE, 1.2),
    Paragraph("Abstract", abstract_head),
    Paragraph(
        "National AI strategies increasingly treat high-performance compute accelerators as primary "
        "instruments of technological sovereignty. However, compute scaling is physically bounded by "
        "electricity transmission, cooling water, semiconductor lithography, advanced packaging, and "
        "geopolitically concentrated supply chains. This paper develops an evidence-backed "
        "<b>Five-Pillar Conceptual Framework</b> integrated with an auditable six-layer "
        "<b>Demand-Cascade Model</b> to evaluate India's AI infrastructure trajectory across 200k, "
        "500k, and 1M GPU deployment scenarios. For the baseline 500k-GPU case, the model projects "
        "peak facility power of <b>891.8 MW</b> (56.62% of India's operational colocation capacity), "
        "annual energy of 6.25 TWh (4.475 Mt CO2), and water withdrawal of 11,249 ML/year. "
        "Crucially, empirical results <b>refute</b> the conventional hypothesis that front-end fab "
        "capacity is the binding chokepoint: wafer starts represent only 1.60% of TSMC's sub-5nm "
        "output, whereas CoWoS packaging absorbs 7.41% (4.6x higher intensity) and HBM3e consumes "
        "6.67% of global supply. Policy planning must invert standard priorities.",
        abstract_body),
    Paragraph("<b>Keywords:</b> AI infrastructure, semiconductor sovereignty, demand-cascade modeling, "
              "power grid constraints, CoWoS packaging, HBM.", kw_style),
    rule(RULE_COLOR),
    SP(4),
]

story += sec("I", "Introduction")
story += [
    P("AI has transitioned from an algorithmic discipline to an ultra-compute-intensive industrial "
      "apparatus governed by capital expenditure, high-voltage power grids, and physical "
      "microelectronic supply lines. India's IndiaAI Mission (Rs. 10,371.92 crore, ~$1.25B) and "
      "Semicon India 2.0 (Rs. 1,27,500 crore) codify this ambition."),
    P("Prevailing policy discourse decouples accelerator procurement from the physical systems "
      "required to sustain compute operations. A 500k-GPU cluster demands continuous megawatt-scale "
      "power, high-voltage substations, gigalitres of cooling water under tropical ambient "
      "temperatures, and supply chains spanning EUV lithography, CoWoS packaging, and HBM. Without "
      "rigorous co-planning, fiscal subsidies risk procuring silicon that sits idle behind "
      "multi-year transmission queues or creates municipal water conflicts."),
    P("Middle-power economies face the <i>N-2 Problem</i>: non-superpower nations cannot "
      "realistically build commercial sub-3nm foundries (>$20B capex/fab) without crippling "
      "under-utilization. This paper introduces an integrated Five-Pillar Framework and an "
      "auditable six-layer Demand-Cascade Model to identify true structural chokepoints."),
]

story += sec("II", "Literature Review and Research Gap")
story += subsec("A.", "Data Centre Thermodynamics and Grid Scaling")
story += [
    P("Shehabi et al. [LBNL 2024] document server-level host overheads multiplying GPU TDP by "
      "1.6-2.1x. IEA [2024] projects global data centre electricity demand exceeding 1,000 TWh by "
      "2026. JLL and CBRE confirm India's operational colocation capacity at 1,575 MW (mid-2026), "
      "with 52.4% concentrated in Mumbai and substation interconnection queues of 18-36 months."),
]
story += subsec("B.", "Semiconductor Geopolitics and Foundry Chokepoints")
story += [
    P("Akimitsu [2026] demonstrates extreme market concentration (HHI: EUV 10,000; refined gallium "
      "9,804; CoWoS packaging 8,100). SemiAnalysis and TrendForce identify CoWoS 2.5D packaging "
      "as the primary AI hardware bottleneck, with HBM3e concentrated in a tight triopoly "
      "(SK Hynix, Samsung, Micron)."),
    SP(4),
    Paragraph("TABLE I. Prior Art Benchmark and Analytical Comparison Matrix", table_cap_style),
    make_table_prior_art(),
    SP(6),
]
story += subsec("C.", "Five Core Research Gaps")
story += [
    P("Five critical research deficits remain unaddressed:"),
    E(1, "<b>RG-01 Disciplinary Siloing:</b> Microelectronics, energy, and governance research are disconnected."),
    E(2, "<b>RG-02 Absent Demand Cascade:</b> No study propagates GPU targets (200k-1M) bottom-up through chip TDP, PUE, wafer geometry, and packaging."),
    E(3, "<b>RG-03 Silicon Wafer Fallacy:</b> Policy assumes domestic sub-5nm fab is the binding constraint without testing whether packaging limits deployment first."),
    E(4, "<b>RG-04 Tropical Climate Blind Spot:</b> Global models assume temperate PUE baselines (1.15-1.20), ignoring Indian summer heatwave spikes (>42C, PUE up to 1.65)."),
    E(5, "<b>RG-05 Policy Operationalization Gap:</b> No quantitative intervention matrix distinguishing build vs. partner vs. manage."),
]

story += sec("III", "Demand-Cascade Model Formulation")
story += [
    P("The model maps an exogenous accelerator target N through six deterministic physical layers, "
      "fully parameterized from empirical data centre audits, foundry specifications, and CEA telemetry."),
]
story += subsec("A.", "Layer 1: IT Electrical Load")
story += [
    P("GPU TDP P_gpu = 700 W (H100 SXM5); chassis overhead R_host = 1.82 (CPUs, DDR5, InfiniBand, PCIe):"),
    P("<i>P_IT = N x P_gpu x R_host / 10^6  [MW]</i>", abstract_body),
]
story += subsec("B.", "Facility Power and Annual Energy")
story += [
    P("P_facility = P_IT x PUE (tropical baseline PUE = 1.40)"),
    P("E_annual = P_facility x 8760 x 0.80 / 10^6  [TWh]  (80% utilization)"),
    P("Emissions: E_annual x 0.716 tCO2/MWh  [Mt CO2]  (CEA grid factor)"),
]
story += subsec("C.", "Layers 3-6: Water, Racks, Wafers, Packaging, HBM")
story += [
    P("Water: I_water x E_annual x 10^9 / 10^6  [ML]. Racks: P_IT x 10^3 / 60 kW."),
    P("Wafer starts: Gross dies = 63 (GH100, 814 mm2 die, 300mm wafer, edge-loss eq.). "
      "Murphy yield Y_M ~ 0.540 (D0=0.08/cm2); industrial net yield Y=0.65 => 40 good dies/wafer. "
      "W_starts = ceil(N/40)."),
    P("CoWoS interposers: W_CoWoS = ceil(N/15). HBM3e stacks: N_HBM = N x 8."),
    SP(6),
    Paragraph("TABLE II. Demand-Cascade Simulation Results — All Scenarios (Model v2.0)", table_cap_style),
    make_table_scenarios(),
    SP(4),
    P("Note: 500k Base row highlighted. CoWoS% of global ~450k wafers/year; TSMC% of "
      "~780k sub-5nm wafers/year; Colo% of India 1,575 MW operational capacity.", footnote_style),
    SP(6),
]

story += fig("fig1_demand_cascade_architecture.png",
             "Six-Layer Demand-Cascade Architecture: From Policy Targets to Microelectronics and Power Grids.", "1")
story += [SP(4)]

story += sec("IV", "Empirical Results and Discussion")
story += subsec("A.", "Scenario Scaling Analysis")
story += [
    P("In the baseline 500k-GPU scenario, IT load reaches 637.0 MW. Under tropical PUE = 1.40, "
      "peak facility power escalates to <b>891.8 MW</b> — <b>56.62% of India's entire operational "
      "colocation capacity</b>. Annual electricity totals 6.25 TWh/year (4.475 Mt CO2); evaporative "
      "water dissipation reaches 11,249.5 ML/year (11.25 billion litres)."),
]

story += fig("fig2_structural_chokepoint_inversion.png",
             "The Structural Chokepoint Inversion: CoWoS packaging (7.41%) and grid capacity (56.62%) "
             "are binding constraints — not front-end wafers (1.60%). Red bars denote binding chokepoints.", "2")
story += [SP(4)]

story += subsec("B.", "Refuting the Silicon Wafer Hypothesis")
story += [
    P("Deploying 500k GPUs requires 12,500 wafer starts. TSMC sub-5nm capacity is ~780,000 "
      "wafers/year. India's requirement is only <b>1.60% of annual global sub-5nm output</b>. "
      "Domestically building a sub-5nm gigafab ($15-20B capex, 7-10 year lead) to serve 1.60% "
      "of demand constitutes a severe capital misallocation."),
]
story += subsec("C.", "True Structural Chokepoints")
story += [
    E(1, "<b>CoWoS Advanced Packaging:</b> 33,334 interposer wafers = <b>7.41% of global capacity</b> "
         "(4.6x higher bottleneck intensity than front-end wafers)."),
    E(2, "<b>HBM3e Memory:</b> 4,000,000 HBM stacks = <b>6.67% of global supply</b>. India has "
         "zero domestic fabrication capability."),
    E(3, "<b>Grid Congestion:</b> 891.8 MW into Mumbai requires 18 dedicated 50 MW substations, "
         "triggering 24-36 month interconnection delays (CEA guidelines)."),
    E(4, "<b>Water Stress:</b> 11.25 billion litres/year conflicts with urban water supply."),
    SP(4),
    Paragraph("TABLE III. Semiconductor vs. Physical Infrastructure Chokepoint Hierarchy", table_cap_style),
    make_table_chokepoints(),
    SP(4),
]

story += fig("fig3_country_comparison_benchmark.png",
             "Cross-National AI Infrastructure Benchmarking: Compute stocks and asymmetric supply-chain "
             "dependencies across US, China, and India.", "3")
story += [SP(4)]

story += subsec("D.", "Cross-National Benchmarking")
story += [
    P("India hosts ~20% of global chip design engineers in foreign GCCs but possesses 0% domestic "
      "sub-5nm logic, 0% CoWoS packaging, and 0% HBM fabrication. Deploying 500k GPUs elevates "
      "India's active compute from 35 to 245 EFLOPS, approaching China's 450 EFLOPS, but requires "
      "managing deep foreign dependencies across all supply layers."),
]
story += subsec("E.", "Cooling Technology Pareto Trade-Offs")
story += [
    P("In summer heatwaves (>42C), traditional air cooling degrades to PUE = 1.65 and water "
      "consumption exceeds 11,600 ML/year. Direct-to-Chip (D2C) liquid cooling reduces water "
      "consumption by <b>94.6%</b> (11,651 to 631 ML) and lowers peak power by 172 MW."),
    SP(4),
    Paragraph("TABLE IV. Cooling Technology Trade-Off Matrix — Tropical Indian Ambient (500k GPUs)",
              table_cap_style),
    make_table_cooling(),
    SP(4),
]

story += fig("fig4_cooling_water_energy_pareto.png",
             "Cooling Technology Water-Energy Pareto Frontier across Indian Climatic Profiles. "
             "D2C liquid cooling dominates on both PUE and water metrics.", "4")
story += [SP(4)]

story += fig("fig5_sensitivity_tornado_montecarlo.png",
             "One-at-a-Time Parameter Sensitivity (Tornado) and Monte Carlo Uncertainty Analysis "
             "(1,000 runs). 90% CI for facility power: [834 MW, 1,130 MW].", "5")
story += [SP(4)]

story += subsec("F.", "Sensitivity and Monte Carlo Analysis")
story += [
    P("Tornado analysis (Fig. 5) confirms facility power is most sensitive to PUE and GPU TDP. "
      "Switching from air cooling (PUE=1.55) to D2C (PUE=1.18) saves <b>235.7 MW</b> of peak "
      "grid demand at 500k scale. Monte Carlo 90% CI: facility power [834-1,130 MW], "
      "wafer starts [11,112-14,706]."),
]

story += sec("V", "Strategic Roadmap and Policy Implications")
story += subsec("A.", "Priority Inversion: Debunking Foundry-First")
story += [
    P("Standard policy advocates $15-20B for a domestic sub-5nm foundry. The cascade model proves "
      "this is a strategic misallocation: 12,500 wafers/year (< 2% of a gigafab's break-even volume) "
      "produce zero operational accelerators without CoWoS, HBM, and 891.8 MW of substation power."),
    P("<b>Old priority:</b> Sub-5nm logic fab ($15B+ capex, 7-10yr lead). "
      "<b>New priority:</b> High-voltage Green AI transmission corridors, spatial decentralization, "
      "and bilateral packaging/memory JVs."),
]
story += subsec("B.", "Three-Tier Strategic Intervention Matrix")
story += [
    P("<b>Tier 1 — Build Domestically (2026-2028):</b>"),
    B("Mandate 15-20% capital rebates directing greenfield AI clusters to Gujarat, Rajasthan, Odisha, "
      "MP — reducing Mumbai concentration below 35%."),
    B("Condition IndiaAI subsidies on PUE <= 1.25 and closed-loop dry heat rejection, eliminating "
      "11 billion litres/year of municipal water loss."),
    B("Fast-track 9-month CEA approval window for 400/220 kV substations serving clusters >= 50 MW."),
    P("<b>Tier 2 — Partner Strategically (2028-2031):</b>"),
    B("Expand ATMP/OSAT facilities (Tata Electronics, Micron) toward 2.5D silicon/glass interposers "
      "via JVs with Taiwanese/Japanese OSATs under Semicon 2.0."),
    B("Scale CSIR-IMMT gallium extraction from NALCO/Hindalco bauxite residue to 50 MT/year."),
    B("Mobilize 120,000 VLSI engineers into an open-standard (UCIe) chiplet consortium for "
      "domain-specific RISC-V matrix accelerators on mature nodes."),
    P("<b>Tier 3 — Manage External Dependencies (2031-2035):</b>"),
    B("Secure multi-year sovereign foundry agreements at TSMC and bilateral HBM supply treaties "
      "with South Korea, leveraging India's consumer market as strategic trade offsets."),
]

story += sec("VI", "Conclusion and Limitations")
story += [
    P("This paper presents the first reproducible, multi-layer demand-cascade framework linking "
      "national AI accelerator targets to electric transmission, cooling thermodynamics, and "
      "semiconductor supply chains. The empirical findings prove that India's sovereign compute "
      "bottleneck is <b>2.5D CoWoS packaging</b>, <b>HBM allocation</b>, and "
      "<b>metropolitan grid congestion</b> — not front-end lithography. By prioritizing "
      "transmission corridors, spatial dispersion, and packaging alliances, India can deploy "
      "resilient sovereign AI infrastructure without capital misallocation."),
    P("<i>Limitations:</i> Model assumes static 80% utilization without dynamic nodal power "
      "dispatch, and relies on public foundry defect density disclosures. Future work will "
      "integrate real-time AC power-flow simulations and dynamic diurnal inference scaling."),
    SP(4),
    Paragraph("Acknowledgment", ack_style),
    P("The authors acknowledge Amity University MP, CEA, MeitY, and academic repositories. "
      "Generative AI tools (Antigravity IDE) were used strictly for simulation scripting, "
      "LaTeX code formatting, and bibliographic indexing under full author verification.",
      footnote_style),
]

story += [rule(IEEE_BLUE, 0.8), Paragraph("References", ref_head_style)]
for ref in [
    "[1] K. Akimitsu, Chokepoints and Concentrations in the AI Hardware Stack, CSIS, 2026.",
    "[2] Ministry of Electronics & IT, IndiaAI Mission Gazette Notification, MeitY, 2024.",
    "[3] India Semiconductor Mission, Semicon India 2.0 Policy Framework, ISM, 2025.",
    "[4] A. Shehabi et al., US Data Center Energy Usage Report, LBNL, 2024.",
    "[5] International Energy Agency, AI and Energy: Global Data Centre Demand, IEA, 2024.",
    "[6] M. Kaufmann et al., Transmission Grid Congestion from HPC Clusters, IEEE PES, 2025.",
    "[7] JLL, India Data Centre Market Census H1 2026, JLL, 2026.",
    "[8] CBRE, Asia Pacific Data Centre Report 2026, CBRE, 2026.",
    "[9] Central Electricity Authority, Grid Interconnection Guidelines 2026, CEA, 2026.",
    "[10] TSMC, 2025 Annual Report: Technology and Capacity Roadmap, TSMC, 2025.",
    "[11] SemiAnalysis, CoWoS Supply Analysis: AI Packaging Bottleneck, SemiAnalysis, 2025.",
    "[12] TrendForce, Foundry Market Dynamics H1 2026, TrendForce, 2026.",
    "[13] TrendForce, HBM3e Supply Chain Report 2026, TrendForce, 2026.",
    "[14] Counterpoint Research, HBM Market Share Analysis Q4 2025, Counterpoint, 2025.",
    "[15] USGS, Mineral Commodity Summaries: Gallium, U.S. Geological Survey, 2025.",
    "[16] Portulans Institute / Bruegel, AI Sovereignty: The N-2 Problem, Portulans, 2026.",
    "[17] NVIDIA Corporation, H100 SXM5 Technical Specifications, NVIDIA, 2024.",
    "[18] Colliers, APAC Data Centre Outlook Report 2026, Colliers, 2026.",
    "[19] NITI Aayog, India's Strategy for AI: Indispensable Not Imitative, NITI, 2025.",
    "[20] B. T. Murphy, Cost-size optima of monolithic ICs, Proc. IEEE, 1964.",
    "[21] G. E. Moore, Cramming More Components onto ICs, Electronics, 1965.",
    "[22] IEA, Water-Energy Nexus in Data Centres, IEA, 2024.",
    "[23] NALCO/CSIR-IMMT, Gallium Recovery from Bayer Process Red Mud, CSIR, 2024.",
]:
    story.append(Paragraph(ref, ref_style))

# ── Build ──────────────────────────────────────────────────────────────────
frame_left  = Frame(MARGIN_OUTER, MARGIN_BOTTOM,
                    COL_W, PAGE_H - MARGIN_TOP - MARGIN_BOTTOM,
                    id="left", leftPadding=0, rightPadding=COL_GAP/2,
                    topPadding=0, bottomPadding=0)
frame_right = Frame(MARGIN_OUTER + COL_W + COL_GAP, MARGIN_BOTTOM,
                    COL_W, PAGE_H - MARGIN_TOP - MARGIN_BOTTOM,
                    id="right", leftPadding=COL_GAP/2, rightPadding=0,
                    topPadding=0, bottomPadding=0)

doc = BaseDocTemplate(
    OUT_PDF,
    pagesize=letter,
    pageTemplates=[PageTemplate(id="TwoCol", frames=[frame_left, frame_right], onPage=on_page)],
    title="A Demand-Driven Framework for India's AI Infrastructure Planning",
    author="Adarsh Singh, Sourav, Anamidhi Shrivastava",
    subject="ResearchThon 2026",
    creator="Antigravity IDE | ReportLab 5"
)

doc.build(story)
print(f"\nOK PDF generated: {OUT_PDF}")
print(f"  Size: {os.path.getsize(OUT_PDF)/1024:.1f} KB")