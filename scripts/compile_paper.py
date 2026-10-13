"""
Master PDF Compiler for ResearchThon 2026 IEEE Conference Paper (Revision v2)
=============================================================================
Generates revision_v2/output/researchthon_v2_review.pdf complying with:
  - IEEE two-column format on A4 paper
  - Exactly <= 6 pages
  - Header: AMITY RESEARCHOTHON 2026 — IEEE FORMAT ALIGNED PROCEEDINGS
  - Authors: Adarsh Singh, Sourav, Anamidhi Shrivastava
  - Incorporates all 5 comparative figures and all tables
  - Full text of Sections I through VI with 23 IEEE references
"""

import os
import sys
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, 
    Table, TableStyle, Image, KeepTogether, PageBreak, FrameBreak
)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

_ROOT = Path(__file__).resolve().parent.parent
_OUTPUT_PDF = _ROOT / "output" / "final_paper.pdf"
_FIGURES_DIR = _ROOT / "manuscript" / "figures"


def build_pdf_v2():
    print(f"Compiling IEEE Revision v2 Review PDF to: {_OUTPUT_PDF}")
    _OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)

    page_w, page_h = A4
    margin_top = 38
    margin_bottom = 38
    margin_left = 36
    margin_right = 36

    content_w = page_w - margin_left - margin_right # 523.27 pt
    content_h = page_h - margin_top - margin_bottom # 765.89 pt
    gutter = 14
    col_w = (content_w - gutter) / 2 # 254.63 pt

    # Page 1 Frames
    title_h = 105
    frame_title = Frame(margin_left, page_h - margin_top - title_h, content_w, title_h,
                        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='F_Title')
    col1_p1_h = content_h - title_h - 6
    frame_c1_p1 = Frame(margin_left, margin_bottom, col_w, col1_p1_h,
                        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='F_C1_P1')
    frame_c2_p1 = Frame(margin_left + col_w + gutter, margin_bottom, col_w, col1_p1_h,
                        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='F_C2_P1')

    # Standard Two-Column Frames for Pages 2 to 6
    frame_c1_std = Frame(margin_left, margin_bottom, col_w, content_h,
                         leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='F_C1_Std')
    frame_c2_std = Frame(margin_left + col_w + gutter, margin_bottom, col_w, content_h,
                         leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='F_C2_Std')

    def add_decorations(canvas, doc):
        canvas.saveState()
        canvas.setFont('Times-Roman', 7.5)
        canvas.setFillColor(colors.HexColor('#444444'))
        if doc.page > 1:
            canvas.drawString(margin_left, page_h - 26, "AMITY RESEARCHOTHON 2026 — IEEE FORMAT ALIGNED PROCEEDINGS")
            canvas.drawRightString(page_w - margin_right, page_h - 26, "RESEARCH PAPER — TRACK: AI INFRASTRUCTURE & SOVEREIGNTY")
            canvas.setStrokeColor(colors.HexColor('#CCCCCC'))
            canvas.setLineWidth(0.5)
            canvas.line(margin_left, page_h - 30, page_w - margin_right, page_h - 30)

        page_str = f"Page {doc.page} of 6"
        canvas.drawRightString(page_w - margin_right, 24, page_str)
        canvas.drawString(margin_left, 24, "A Demand-Driven Framework for India's AI Infrastructure Planning")
        canvas.setStrokeColor(colors.HexColor('#CCCCCC'))
        canvas.setLineWidth(0.5)
        canvas.line(margin_left, 32, page_w - margin_right, 32)
        canvas.restoreState()

    doc = BaseDocTemplate(str(_OUTPUT_PDF), pagesize=A4, leftMargin=margin_left, rightMargin=margin_right,
                          topMargin=margin_top, bottomMargin=margin_bottom)

    template_p1 = PageTemplate(id='Page1', frames=[frame_title, frame_c1_p1, frame_c2_p1], onPage=add_decorations)
    template_std = PageTemplate(id='PageStd', frames=[frame_c1_std, frame_c2_std], onPage=add_decorations)
    doc.addPageTemplates([template_p1, template_std])

    title_style = ParagraphStyle('DocTitle', fontName='Times-Bold', fontSize=13.5, leading=16.5, alignment=TA_CENTER, textColor=colors.HexColor('#0D1B2A'))
    author_style = ParagraphStyle('DocAuthor', fontName='Times-Bold', fontSize=9.0, leading=11.5, alignment=TA_CENTER)
    affil_style = ParagraphStyle('DocAffil', fontName='Times-Roman', fontSize=7.8, leading=10.0, alignment=TA_CENTER, textColor=colors.HexColor('#333333'))

    h1_style = ParagraphStyle('SecH1', fontName='Times-Bold', fontSize=8.8, leading=11.0, spaceBefore=5, spaceAfter=2.0, textColor=colors.HexColor('#000000'))
    body_style = ParagraphStyle('BodyText', fontName='Times-Roman', fontSize=7.8, leading=9.8, alignment=TA_JUSTIFY, spaceAfter=2.0)
    bullet_style = ParagraphStyle('BulletText', fontName='Times-Roman', fontSize=7.6, leading=9.5, alignment=TA_JUSTIFY, leftIndent=5, spaceAfter=1.8)
    abstract_style = ParagraphStyle('AbstractText', fontName='Times-Roman', fontSize=7.4, leading=9.2, alignment=TA_JUSTIFY, leftIndent=3, rightIndent=3)
    caption_style = ParagraphStyle('Caption', fontName='Times-Italic', fontSize=7.0, leading=8.5, alignment=TA_CENTER, textColor=colors.HexColor('#222222'), spaceAfter=2.0)
    tbl_cap_style = ParagraphStyle('TblCaption', fontName='Times-Bold', fontSize=7.0, leading=8.5, alignment=TA_CENTER, textColor=colors.HexColor('#000000'), spaceAfter=1.5)
    ref_style = ParagraphStyle('RefEntry', fontName='Times-Roman', fontSize=6.5, leading=7.8, alignment=TA_JUSTIFY, spaceAfter=1.2, leftIndent=9, firstLineIndent=-9)

    story = []

    # ================= PAGE 1 =================
    story.append(Paragraph("A Demand-Driven Framework for India's AI Infrastructure Planning: Linking Compute, Energy, Physical Resources, and Semiconductor Dependencies", title_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>Adarsh Singh, Sourav, and Anamidhi Shrivastava</b>", author_style))
    story.append(Paragraph("Department of Computer Science & Engineering, Amity School of Engineering and Technology<br/>Amity University Madhya Pradesh, Gwalior, India &bull; <i>contact@amity.edu</i>", affil_style))
    story.append(FrameBreak())

    # Column 1
    story.append(Paragraph("<b><i>Abstract</i>— National artificial intelligence (AI) strategies increasingly treat high-performance compute accelerators as primary instruments of technological sovereignty. However, compute scaling is physically bounded by electricity transmission, cooling water, semiconductor lithography, advanced packaging, and geopolitically concentrated supply chains. This paper develops an evidence-backed Five-Pillar Conceptual Framework integrated with an auditable, six-layer Demand-Cascade Model to evaluate India's AI infrastructure trajectory across 200,000, 500,000, and 1,000,000 graphics processing unit (GPU) deployment scenarios. Parameterized from empirical data centre audits, foundry specifications, and Central Electricity Authority telemetry, the model translates accelerator targets into peak electrical power, annual energy, cooling water withdrawal, front-end silicon wafer starts, 2.5D interposer packaging allocations, and High-Bandwidth Memory (HBM) stacks. For a baseline 500,000-GPU deployment, the model projects a peak facility power demand of 891.8 MW—equivalent to 56.62% of India's current operational colocation data centre capacity—and an annual consumption of 6.25 TWh (4.475 Mt CO<sub>2</sub>). Crucially, the empirical results refute the conventional hypothesis that front-end semiconductor fabrication capacity is the binding physical chokepoint: required wafer starts represent merely 1.60% of TSMC's annual sub-5nm output, whereas 2.5D advanced packaging (CoWoS) consumes 7.41% of total worldwide capacity (4.6× higher intensity) and HBM3e absorbs 6.67% of global supply. Consequently, policy planning must invert standard priorities, subordinating premature domestic leading-edge fab construction to high-voltage power transmission corridors, geographical spatial diversification, and bilateral advanced packaging and memory partnerships.</b>", abstract_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("<b><i>Keywords</i>— Artificial intelligence infrastructure, semiconductor sovereignty, demand-cascade modeling, power grid constraints, advanced packaging (CoWoS), high-bandwidth memory.</b>", abstract_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("I. INTRODUCTION", h1_style))
    story.append(Paragraph("Artificial intelligence (AI) has transitioned from an algorithmic discipline to an ultra-compute-intensive industrial apparatus governed by capital expenditure, high-voltage power grids, and physical microelectronic supply lines. Across leading economies, access to high-density compute clusters is viewed as indispensable for national security, economic productivity, and strategic autonomy [1]. In India, this ambition is codified in the statutory authorization of the IndiaAI Mission with an outlay of ₹10,371.92 crore (~$1.25B USD) [2], complemented by the India Semiconductor Mission (Semicon India 2.0) with an expanded budgetary horizon of ₹1,27,500 crore [3]. Policy pronouncements frequently articulate deployment goals scaling from an initial subsidized tender of 10,000 graphics processing units (GPUs) toward national fleets exceeding 100,000 to 500,000 accelerators by 2030.", body_style))
    story.append(Paragraph("However, prevailing policy discourse frequently decouples accelerator procurement from the physical and industrial systems required to sustain compute operations. Compute does not exist in the ether: an enterprise accelerator cluster demands continuous megawatt-scale electrical power, high-voltage substation interconnects, gigalitres of cooling water under tropical ambient temperatures, and complex supply chains spanning lithography, advanced packaging, and high-bandwidth memory (HBM). Without rigorous physical co-planning, fiscal subsidies risk procuring silicon that sits idle behind multi-year transmission queues or causes severe municipal resource conflicts.", body_style))
    story.append(Paragraph("Furthermore, middle-power economies face what scholars term the 'N-2 Problem' in AI sovereignty [17]: while the United States and China possess the domestic capital and market scale to pursue full-stack technology autonomy, non-superpower nations (N-2) cannot realistically build commercial leading-edge sub-3nm foundries (>$20 billion capex per fab) without facing crippling under-utilization. Attempting to copy superpower autarky policies results in severe resource misallocations.", body_style))

    # Column 2
    story.append(FrameBreak())
    f1_path = _FIGURES_DIR / "fig1_demand_cascade_architecture.png"
    if f1_path.exists():
        story.append(Image(str(f1_path), width=col_w, height=col_w * (3.2/6.8)))
        story.append(Paragraph("Fig. 1. Six-Layer Demand-Cascade Architecture: From Policy Targets to Microelectronics and Power Grids.", caption_style))

    story.append(Paragraph("To address these vulnerabilities, this paper introduces an integrated Five-Pillar Conceptual Framework (Fig. 1) and formulates an auditable, reproducible six-layer Demand-Cascade Model. By mapping exogenous accelerator targets (200k, 500k, 1M GPUs) through empirical physical equations, we quantify the boundary constraints governing India's AI infrastructure trajectory and identify where the true structural chokepoints reside.", body_style))

    story.append(Paragraph("II. LITERATURE REVIEW AND RESEARCH GAP", h1_style))
    story.append(Paragraph("Existing scholarship remains fundamentally bifurcated across disconnected technical domains:", body_style))
    story.append(Paragraph("<b>A. Data Centre Thermodynamics and Grid Scaling:</b> Shehabi et al. [6] establish empirical power profiles for hyperscale accelerator architectures, documenting that server host overheads (CPUs, NICs, fans) multiply raw chip thermal design power (TDP) by a factor of 1.6 to 2.1. The International Energy Agency (IEA) [5] estimates that global data centre electricity demand could exceed 1,000 TWh by 2026. Kaufmann et al. [9] highlight that multi-hundred-megawatt compute clusters create local substation bottlenecks that cannot be resolved through generic generation capacity alone. In India, industry censuses by JLL [7] and CBRE [8] reveal an operational colocation capacity of 1,575 MW in mid-2026, with 52.4% concentrated in Mumbai, where grid interconnection queues extend to 18–36 months under CEA guidelines [4].", body_style))
    story.append(Paragraph("<b>B. Semiconductor Geopolitics and Foundry Chokepoints:</b> Econometric modeling by Akimitsu [1] demonstrates that upstream AI hardware inputs exhibit extreme market concentration with Herfindahl-Hirschman Index (HHI) values exceeding 7,000 to 10,000. Over 90% of commercial sub-5nm logic fabrication resides in Taiwan under TSMC [15]. Telemetry from SemiAnalysis [12] and TrendForce [10] highlights that the primary hardware bottleneck for modern AI accelerators is not raw wafer lithography, but Chip-on-Wafer-on-Substrate (CoWoS) 2.5D advanced packaging. Similarly, Counterpoint Research [13] and TrendForce [11] demonstrate that global HBM3e supply is concentrated in a tight triopoly between SK Hynix, Samsung, and Micron. In critical minerals, the USGS [14] notes that China controls 98% of refined gallium.", body_style))

    # ================= PAGE 2 =================
    story.append(PageBreak())

    # Column 1
    story.append(Paragraph("<b>C. The Five Core Research Gaps:</b> Despite these valuable domain studies, five critical research deficits remain unaddressed (Table I):<br/>"
                           "1) <i>Disciplinary Siloing (RG-01):</i> Microelectronics analysts study fabs in isolation, energy researchers study grid loads without chip yields, and governance scholars omit physical resource accounting.<br/>"
                           "2) <i>Absence of a Bottom-Up Demand Cascade (RG-02):</i> No published study propagates scaled GPU deployments (200k, 500k, 1M GPUs) bottom-up from chip TDP through server nodes, facility PUE, wafer geometry, and packaging interposers.<br/>"
                           "3) <i>The Silicon Wafer Fallacy (RG-03):</i> Mainstream policy discourse assumes that domestic sub-5nm fab capacity is India's binding constraint, without testing whether wafer volume or advanced packaging actually limits deployment.<br/>"
                           "4) <i>Tropical Climate Cooling Penalty (RG-04):</i> Global models assume temperate datacenter baselines (PUE 1.15–1.20) and ignore extreme South Asian summer heatwaves (>42°C), which spike PUE and evaporative water loss.<br/>"
                           "5) <i>Operationalizing Coordinated Specialization (RG-05):</i> NITI Aayog's doctrine of 'Indispensable, Not Imitative' lacks a quantitative intervention matrix distinguishing domestic build, strategic alliances, and managed external dependency.", body_style))

    # Table 1: Prior Art
    t1_data = [
        ["Literature Source", "Primary Method", "GPU Scenarios", "Power / Water", "Hardware Cascade"],
        ["Akimitsu (2026) [1]", "Econometric HHI", "None (Sector)", "None", "40 Stage HHIs"],
        ["Portulans (2026) [17]", "Qualitative Statecraft", "None (Conceptual)", "None", "N-2 Taxonomy"],
        ["IEA / LBNL [5, 6]", "Macro Energy Models", "Top-down TWh", "PUE 1.15-1.25", "Omits Wafers/Pkg"],
        ["Inherited Draft", "Heuristic Score (Vi)", "Static 10k/45k", "PUE 1.55 (Qual)", "Cites Akimitsu"],
        ["This Paper (v2.0)", "First-principles Cascade", "200k, 500k, 1M", "MW, TWh, Water", "Murphy, CoWoS, HBM"],
    ]
    t1 = Table(t1_data, colWidths=[52, 54, 48, 48, 52])
    t1.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 5.8),
        ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
        ('FONTNAME', (0,-1), (-1,-1), 'Times-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('LINEBELOW', (0,0), (-1,0), 0.8, colors.black),
        ('LINEBELOW', (0,-1), (-1,-1), 0.8, colors.black),
        ('LINEABOVE', (0,0), (-1,0), 0.8, colors.black),
    ]))
    story.append(Paragraph("TABLE I: PRIOR ART BENCHMARK AND LITERATURE COMPARISON MATRIX", tbl_cap_style))
    story.append(t1)
    story.append(Spacer(1, 2))

    story.append(Paragraph("III. DEMAND-CASCADE MODEL FORMULATION", h1_style))
    story.append(Paragraph("The Demand-Cascade Model maps an exogenous target of <i>N</i> accelerators through six deterministic layers:", body_style))
    story.append(Paragraph("<b>Layer 1: IT Electrical Load (P<sub>IT</sub>):</b> Active IT power accounts for accelerator board TDP (P<sub>gpu</sub>) and server chassis overhead (R<sub>host</sub> = 1.82) [19]:", body_style))
    story.append(Paragraph("<i>P<sub>IT</sub> = (N &middot; P<sub>gpu</sub> &middot; R<sub>host</sub>) / 10<sup>6</sup> &nbsp; [MW]</i> &nbsp;&nbsp;&nbsp;&nbsp; (1)", bullet_style))

    # Column 2
    story.append(FrameBreak())
    story.append(Paragraph("<b>Layer 2: Facility Peak Power and Annual Energy:</b> Facility grid capacity incorporates Power Usage Effectiveness (PUE = 1.40 tropical baseline):", body_style))
    story.append(Paragraph("<i>P<sub>facility</sub> = P<sub>IT</sub> &middot; PUE &nbsp; [MW]</i> &nbsp;&nbsp;&nbsp;&nbsp; (2)", bullet_style))
    story.append(Paragraph("Annual electrical energy consumption (E<sub>annual</sub> in TWh) is a function of cluster capacity utilization factor <i>U = 0.80</i> across 8,760 hours:", body_style))
    story.append(Paragraph("<i>E<sub>annual</sub> = (P<sub>facility</sub> &middot; 8760 &middot; U) / 10<sup>6</sup> &nbsp; [TWh]</i> &nbsp;&nbsp;&nbsp;&nbsp; (3)", bullet_style))
    story.append(Paragraph("Operational greenhouse gas emissions reflect Central Electricity Authority (CEA) emission factor EF<sub>grid</sub> = 0.716 tCO<sub>2</sub>/MWh [4]:", body_style))
    story.append(Paragraph("<i>Emissions<sub>annual</sub> = E<sub>annual</sub> &middot; EF<sub>grid</sub> &nbsp; [Mt CO<sub>2</sub>]</i> &nbsp;&nbsp;&nbsp;&nbsp; (4)", bullet_style))

    story.append(Paragraph("<b>Layer 3: Thermal Water Withdrawal and Equipment Racks:</b> Annual evaporative cooling water consumption reflects water intensity I<sub>water</sub> (L/kWh) [5]:", body_style))
    story.append(Paragraph("<i>W<sub>annual</sub> = (E<sub>annual</sub> &middot; 10<sup>9</sup> &middot; I<sub>water</sub>) / 10<sup>6</sup> &nbsp; [ML]</i> &nbsp;&nbsp;&nbsp;&nbsp; (5)", bullet_style))
    story.append(Paragraph("Physical rack footprint (N<sub>rack</sub>) is determined by power density (D<sub>rack</sub> = 60 kW/rack):", body_style))
    story.append(Paragraph("<i>N<sub>rack</sub> = &lceil; P<sub>IT</sub> &middot; 10<sup>3</sup> / D<sub>rack</sub> &rceil;</i> &nbsp;&nbsp;&nbsp;&nbsp; (6)", bullet_style))

    story.append(Paragraph("<b>Layer 4: Semiconductor Wafer Starts:</b> Gross dies per 300mm wafer (N<sub>gross</sub>) are calculated from radius r=150mm and die area A<sub>die</sub>=814 mm<sup>2</sup> via edge-loss geometry:", body_style))
    story.append(Paragraph("<i>N<sub>gross</sub> = &lfloor; &pi;r<sup>2</sup> / A<sub>die</sub> - 2&pi;r / &radic;(2A<sub>die</sub>) &rfloor; = 63</i> &nbsp;&nbsp;&nbsp;&nbsp; (7)", bullet_style))
    story.append(Paragraph("Analytical defect yield is formulated via the Murphy model with defect density D<sub>0</sub> = 0.08 cm<sup>-2</sup>: <i>Y<sub>Murphy</sub> = ((1 - e<sup>-D<sub>0</sub>A</sup>)/(D<sub>0</sub>A))<sup>2</sup> &approx; 0.540</i>. Accounting for industrial binning, net functional yield reaches Y = 0.65, giving N<sub>good</sub> = &lfloor; 63 &middot; 0.65 &rfloor; = 40 good dies. Required 300mm wafer starts are:", body_style))
    story.append(Paragraph("<i>W<sub>starts</sub> = &lceil; N / N<sub>good</sub> &rceil;</i> &nbsp;&nbsp;&nbsp;&nbsp; (8)", bullet_style))

    story.append(Paragraph("<b>Layers 5 and 6: 2.5D Packaging and HBM Memory:</b> Silicon interposer wafers required for CoWoS packaging (W<sub>CoWoS</sub>) reflect C<sub>CoWoS</sub> = 15 packages/wafer:", body_style))
    story.append(Paragraph("<i>W<sub>CoWoS</sub> = &lceil; N / C<sub>CoWoS</sub> &rceil;</i> &nbsp;&nbsp;&nbsp;&nbsp; (9)", bullet_style))
    story.append(Paragraph("Total HBM3e memory stacks scale linearly (N<sub>stacks</sub> = 8 per GPU):", body_style))
    story.append(Paragraph("<i>N<sub>HBM</sub> = N &middot; N<sub>stacks</sub></i> &nbsp;&nbsp;&nbsp;&nbsp; (10)", bullet_style))

    # ================= PAGE 3 =================
    story.append(PageBreak())

    # Column 1
    t2_data = [
        ["Scenario", "Variant", "IT (MW)", "Fac (MW)", "TWh/yr", "Water (ML)", "Wafers", "TSMC %", "CoWoS %", "Colo Op %"],
        ["200k GPUs", "Low", "224.0", "280.0", "1.59", "318.9", "4,445", "0.57%", "2.47%", "17.8%"],
        ["", "Base", "254.8", "356.7", "2.50", "4,499.8", "5,000", "0.64%", "2.96%", "22.7%"],
        ["", "High", "420.0", "651.0", "5.13", "12,831.9", "10,527", "1.35%", "3.70%", "41.3%"],
        ["500k GPUs", "Low", "560.0", "700.0", "3.99", "797.2", "11,112", "1.42%", "6.17%", "44.4%"],
        ["", "Base", "637.0", "891.8", "6.25", "11,249.5", "12,500", "1.60%", "7.41%", "56.6%"],
        ["", "High", "1,050.0", "1,627.5", "12.83", "32,079.8", "26,316", "3.37%", "9.26%", "103.3%"],
        ["1M GPUs", "Low", "1,120.0", "1,400.0", "7.97", "1,594.3", "22,223", "2.85%", "12.35%", "88.9%"],
        ["", "Base", "1,274.0", "1,783.6", "12.50", "22,499.0", "25,000", "3.21%", "14.81%", "113.2%"],
        ["", "High", "2,100.0", "3,255.0", "25.66", "64,159.5", "52,632", "6.75%", "18.52%", "206.7%"],
    ]
    t2 = Table(t2_data, colWidths=[38, 20, 24, 25, 22, 28, 24, 24, 25, 25])
    t2.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 5.6),
        ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('LINEBELOW', (0,0), (-1,0), 0.8, colors.black),
        ('LINEBELOW', (0,-1), (-1,-1), 0.8, colors.black),
        ('LINEABOVE', (0,0), (-1,0), 0.8, colors.black),
    ]))
    story.append(Paragraph("TABLE II: DEMAND-CASCADE SIMULATION RESULTS ACROSS GPU DEPLOYMENT SCENARIOS (MODEL V2.0)", tbl_cap_style))
    story.append(t2)
    story.append(Spacer(1, 2))

    story.append(Paragraph("IV. EMPIRICAL RESULTS AND DISCUSSION", h1_style))
    story.append(Paragraph("<b>A. Scenario Scaling Analysis:</b> Table II summarizes model outputs. In the baseline 500,000-GPU scenario, active IT load reaches 637.0 MW. Under tropical climatic conditions (PUE = 1.40), peak facility power escalates to <b>891.8 MW</b>. This represents <b>56.62% of India's entire operational colocation data centre capacity</b> (1,575 MW in mid-2026 [7]). At 80% utilization, annual electricity consumption totals <b>6.25 TWh/year</b> (generating 4.475 Mt CO<sub>2</sub>), while evaporative water dissipation reaches <b>11,249.5 ML/year</b> (11.25 million cubic meters).", body_style))

    # Column 2
    story.append(FrameBreak())
    f2_path = _FIGURES_DIR / "fig2_structural_chokepoint_inversion.png"
    if f2_path.exists():
        story.append(Image(str(f2_path), width=col_w, height=col_w * (3.2/5.5)))
        story.append(Paragraph("Fig. 2. The Structural Chokepoint Inversion: Proving that packaging and substation grid capacity are the binding constraints rather than front-end wafers.", caption_style))

    story.append(Paragraph("<b>B. Refuting the 'Silicon Wafer' Hypothesis:</b> A foundational finding is the empirical refutation of the widespread belief that domestic front-end semiconductor fabrication is the binding physical chokepoint (Fig. 2):<br/>"
                           "&bull; <i>Sub-5nm Wafer Demand:</i> Deploying 500,000 GPUs requires exactly <b>12,500 300mm wafer starts</b>.<br/>"
                           "&bull; <i>Global Foundry Context:</i> TSMC's sub-5nm capacity exceeds 65,000 wpm (~<b>780,000 wafers annually</b> [15]).<br/>"
                           "&bull; <i>Relative Scarcity:</i> India's 500k requirement consumes <b>merely 1.60% of annual global sub-5nm wafer output</b>.<br/>"
                           "Thus, raw silicon lithography is easily absorbable by commercial foundry supply lines provided procurement capital is allocated.", body_style))

    story.append(Paragraph("<b>C. Identification of the True Structural Chokepoints:</b> The binding constraints reside in packaging, memory, and domestic infrastructure (Table III):<br/>"
                           "1) <i>2.5D Advanced Packaging (CoWoS):</i> Packaging 500,000 GPUs requires <b>33,334 CoWoS interposer wafers</b>. With global capacity bounded at ~450,000 wpy [10], India absorbs <b>7.41% of total worldwide packaging output</b> (a bottleneck intensity <b>4.6 times higher</b> than front-end wafer fabrication).<br/>"
                           "2) <i>High-Bandwidth Memory (HBM3e):</i> Requires <b>4,000,000 HBM stacks</b> (<b>6.67%</b> of global output), where India possesses zero domestic fabrication or packaging.<br/>"
                           "3) <i>Spatial Transmission Congestion:</i> Supplying 891.8 MW into Mumbai (which holds 52.4% of existing capacity) requires 18 dedicated 50 MW CEA substations [4], triggering grid saturation and multi-year interconnection delays.<br/>"
                           "4) <i>Municipal Hydrological Strain:</i> Consuming 11.25 billion litres/year under conventional wet cooling creates direct conflict with urban drinking water.", body_style))

    # Table 3: Chokepoints
    t3_data = [
        ["Infrastructure Layer", "Global HHI", "India Share", "500k Share", "Lead Time"],
        ["EUV Lithography (ASML)", "10,000", "0.0%", "Upstream", "24-36 mos"],
        ["Sub-5nm Logic Fabs (TSMC)", "5,400", "0.0%", "1.60%", "14-18 wks"],
        ["2.5D CoWoS Packaging", "8,100", "0.0%", "7.41%", "20-28 wks"],
        ["HBM3e Memory Stacks", "4,950", "0.0%", "6.67%", "16-24 wks"],
        ["Substation GIS (400kV)", "2,200", "75.0%", "56.62%", "36-48 mos"],
        ["Colocation Water Rights", "N/A", "100.0%", "11,250 ML", "Seasonal"],
    ]
    t3 = Table(t3_data, colWidths=[58, 44, 46, 46, 56])
    t3.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 5.8),
        ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('LINEBELOW', (0,0), (-1,0), 0.8, colors.black),
        ('LINEBELOW', (0,-1), (-1,-1), 0.8, colors.black),
        ('LINEABOVE', (0,0), (-1,0), 0.8, colors.black),
    ]))
    story.append(Paragraph("TABLE III: STRUCTURAL CHOKEPOINT HIERARCHY (500K GPUS)", tbl_cap_style))
    story.append(t3)

    # ================= PAGE 4 =================
    story.append(PageBreak())

    # Column 1
    f3_path = _FIGURES_DIR / "fig3_country_comparison_benchmark.png"
    if f3_path.exists():
        story.append(Image(str(f3_path), width=col_w, height=col_w * (3.0/6.8)))
        story.append(Paragraph("Fig. 3. Cross-National AI Infrastructure & Strategic Supply Chain Benchmarking.", caption_style))

    story.append(Paragraph("<b>D. Cross-National Comparative Benchmarking:</b> Fig. 3 compares India against the US and China. While India houses ~20% of global chip design engineers in foreign GCCs, it possesses 0% domestic sub-5nm logic fabrication, 0% CoWoS advanced packaging, and 0% HBM manufacturing. Deploying 500,000 GPUs would elevate India's active compute fleet from 35 EFLOPS to 245 EFLOPS, closing the gap with China (450 EFLOPS), but requires managing deep foreign dependencies.", body_style))

    story.append(Paragraph("<b>E. Cooling Technology Pareto Trade-Offs:</b> Table IV and Fig. 4 present cooling trade-offs under South Asian ambient profiles. In summer heatwaves (>42°C), traditional air cooling experiences severe efficiency degradation, with peak PUE escalating to 1.65 and water consumption exceeding 11,600 ML/year. Transitioning to Direct-to-Chip (D2C) liquid cooling with dry coolers slashes on-site water consumption by <b>94.6%</b> (from 11,651 ML to 630.9 ML) while lowering peak power by 172 MW, establishing D2C liquid cooling as an indispensable national infrastructure standard.", body_style))

    # Table 4: Cooling
    t4_data = [
        ["Cooling Technology", "Ann. PUE", "Summer PUE", "WUE (L/kWh)", "Water (ML)"],
        ["Traditional Air (Evap.)", "1.45", "1.65", "1.80", "11,651.2"],
        ["Rear-Door Heat Exch.", "1.35", "1.45", "1.00", "6,031.5"],
        ["Direct-to-Chip (D2C)", "1.18", "1.25", "0.12", "630.9"],
        ["Immersion Cooling", "1.12", "1.18", "0.03", "150.8"],
    ]
    t4 = Table(t4_data, colWidths=[65, 42, 45, 48, 50])
    t4.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 5.8),
        ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('LINEBELOW', (0,0), (-1,0), 0.8, colors.black),
        ('LINEBELOW', (0,-1), (-1,-1), 0.8, colors.black),
        ('LINEABOVE', (0,0), (-1,0), 0.8, colors.black),
    ]))
    story.append(Paragraph("TABLE IV: EMPIRICAL COOLING TECHNOLOGY TRADE-OFF MATRIX (500K GPUS)", tbl_cap_style))
    story.append(t4)
    story.append(Spacer(1, 2))

    # Column 2
    story.append(FrameBreak())
    f4_path = _FIGURES_DIR / "fig4_cooling_water_energy_pareto.png"
    if f4_path.exists():
        story.append(Image(str(f4_path), width=col_w, height=col_w * (3.2/5.5)))
        story.append(Paragraph("Fig. 4. Cooling Technology Water-Energy Pareto Frontier across Indian Climatic Profiles.", caption_style))

    f5_path = _FIGURES_DIR / "fig5_sensitivity_tornado_montecarlo.png"
    if f5_path.exists():
        story.append(Image(str(f5_path), width=col_w, height=col_w * (3.2/5.5)))
        story.append(Paragraph("Fig. 5. One-at-a-Time Sensitivity & Monte Carlo Uncertainty Tornado (500k GPUs).", caption_style))

    story.append(Paragraph("<b>F. Sensitivity and Monte Carlo Uncertainty Analysis:</b> Tornado analysis (Fig. 5) and Monte Carlo simulations (1,000 runs) demonstrate that facility power is exceptionally sensitive to PUE and GPU TDP: transitioning from tropical air cooling (PUE = 1.55) to D2C liquid cooling (PUE = 1.18) <b>saves 235.7 MW of peak grid demand</b> at 500k scale. Monte Carlo 90% confidence intervals establish that facility power spans [834.4 MW, 1,129.8 MW], while wafer starts range between 11,112 and 14,706 wafers.", body_style))

    # ================= PAGE 5 =================
    story.append(PageBreak())

    # Column 1
    story.append(Paragraph("V. STRATEGIC ROADMAP AND POLICY IMPLICATIONS", h1_style))
    story.append(Paragraph("<b>A. Documented Priority Inversion: Debunking 'Foundry-First':</b> Standard policy discourse advocates spending $15–$20 billion to build a domestic sub-5nm logic foundry. Our cascade model proves this is a strategic misallocation. A 500k-GPU sovereign cluster consumes only 12,500 wafers/year—less than 2% of the annual volume needed to economically sustain a modern gigafab. Furthermore, domestic logic dies produce zero operational accelerators without 2.5D packaging, HBM, and 891.8 MW of substation power.<br/>"
                           "The framework directs an <b>immediate priority inversion</b>:<br/>"
                           "&bull; <i>Old Priority:</i> Sub-5nm logic fabrication megaprojects ($15B+ capital risk, 7–10 year lead time).<br/>"
                           "&bull; <i>Inverted New Priority:</i> High-voltage Green AI transmission corridors, spatial decentralization to power-surplus states, and bilateral packaging/memory joint ventures.", body_style))

    story.append(Paragraph("<b>B. Three-Tier Strategic Intervention Matrix:</b> Interventions are categorized into three operational tiers based on multi-criteria feasibility and sovereignty leverage:<br/>"
                           "<b>1) Tier 1: Build Domestically (2026–2028):</b><br/>"
                           "&bull; <i>Spatial Diversification:</i> Mandate 15–20% capital rebates directing greenfield AI clusters away from Mumbai into Gujarat, Rajasthan, Odisha, and Madhya Pradesh, reducing Mumbai's concentration below 35%.<br/>"
                           "&bull; <i>Liquid Cooling Mandate:</i> Condition IndiaAI compute subsidies on PUE &le; 1.25 and closed-loop dry heat rejection, eliminating 11 billion litres/year of municipal water loss.<br/>"
                           "&bull; <i>Fast-Track Grid Substations:</i> Amend Central Electricity Authority regulations to create a dedicated 9-month approval window for 400/220 kV substations serving compute clusters &ge; 50 MW.<br/>"
                           "<b>2) Tier 2: Partner Strategically (2028–2031):</b><br/>"
                           "&bull; <i>Advanced Packaging JVs:</i> Expand approved domestic ATMP/OSAT facilities (Tata Electronics, Micron) toward 2.5D silicon and glass interposers via joint ventures with Taiwanese and Japanese OSATs under Semicon 2.0.<br/>"
                           "&bull; <i>Critical Mineral Refining:</i> Scale CSIR-IMMT technology to extract refined gallium from domestic bauxite refinery residue (red mud) at NALCO and Hindalco, producing 50 metric tons/year of high-purity gallium.<br/>"
                           "&bull; <i>Sovereign Chiplet Consortium:</i> Mobilize India's 120,000 VLSI design engineers into an open-standard (UCIe) consortium to tape out domain-specific RISC-V matrix acceleration chiplets on mature foundry nodes.<br/>"
                           "<b>3) Tier 3: Manage External Dependencies (2031–2035):</b><br/>"
                           "&bull; Secure multi-year sovereign foundry capacity reservation agreements at TSMC and bilateral memory supply treaties with South Korea, leveraging India's large consumer market as strategic trade offsets.", body_style))

    # Column 2
    story.append(FrameBreak())
    story.append(Paragraph("VI. CONCLUSION AND LIMITATIONS", h1_style))
    story.append(Paragraph("This paper presents the first reproducible, multi-layer demand-cascade framework linking national AI accelerator targets directly to electric transmission, cooling thermodynamics, and semiconductor supply chains. The empirical findings prove that India's sovereign compute bottleneck is not front-end lithography volume, but 2.5D CoWoS packaging, HBM allocation, and metropolitan grid congestion. By prioritizing transmission corridors, spatial dispersion, and packaging alliances, India can deploy resilient sovereign AI infrastructure without falling victim to capital misallocations.<br/>"
                           "<i>Limitations:</i> The model assumes static annual cluster utilization (80%) without dynamic nodal power dispatch, and relies on public foundry defect density disclosures. Future research will integrate real-time AC power-flow simulations and dynamic diurnal inference scaling.", body_style))

    story.append(Paragraph("ACKNOWLEDGMENT", h1_style))
    story.append(Paragraph("The authors acknowledge the research facilities at Amity University Madhya Pradesh and primary data access provided by the Central Electricity Authority, MeitY, and academic repositories. Generative AI tools (Antigravity IDE) were utilized strictly for simulation scripting, LaTeX code formatting, and bibliographic indexing under full author verification.", body_style))

    story.append(Paragraph("REFERENCES", h1_style))
    refs = [
        "[1] P. Akimitsu, \"Artificial Intelligence: Supply-Chain Chokepoints and the Reach of Industrial Policy,\" SUNY Economics, arXiv:2607.29572, Aug. 2026.",
        "[2] Ministry of Electronics and IT, \"Cabinet Approves National IndiaAI Mission with Outlay of Rs. 10,371.92 Crore,\" PIB, GoI, Mar. 2024.",
        "[3] India Semiconductor Mission, \"Modified Programme for Development of Semiconductors (Semicon India 2.0),\" MeitY, New Delhi, 2025.",
        "[4] Central Electricity Authority, \"Manual on Transmission Planning Criteria and Data Centre Interconnection Standards,\" Ministry of Power, 2026.",
        "[5] International Energy Agency, \"Energy and AI: World Energy Outlook Special Report on Electricity Demand,\" IEA Publications, Paris, 2024.",
        "[6] A. Shehabi et al., \"2024 United States Data Center Energy Usage Report: Updated Scaling Metrics,\" LBNL-2001428, 2024.",
        "[7] Jones Lang LaSalle, \"India Data Centre 2026 Mid-Year Report: AI Appetite Unleashed,\" JLL Strategic Consulting, Mumbai, Aug. 2026.",
        "[8] CBRE Research, \"India Data Centre Market in a New Era: Capacity Surges Beyond 1.5 GW,\" CBRE India, 2026.",
        "[9] R. Kaufmann, D. Henderson, and A. Miller, \"Power Grid Integration Constraints of Terawatt-Scale AI Infrastructure,\" Nature Energy, vol. 10, 2025.",
        "[10] TrendForce, \"Global Foundry Revenue and Advanced Packaging Analysis: TSMC CoWoS Capacity Expansions in 2026,\" TrendForce, 2026.",
        "[11] TrendForce, \"High-Bandwidth Memory (HBM3e and HBM4) Market Forecast: Supply Chain Constraints,\" TrendForce Memory Intel, 2026.",
        "[12] D. Patel and D. Knupp, \"The True Chokepoints of AI Hardware: CoWoS Packaging, HBM3e and Optical Transceivers,\" SemiAnalysis, 2025.",
        "[13] Counterpoint Research, \"Global High-Bandwidth Memory Ecosystem: Market Shares and 12-High Stacking Bottlenecks,\" Counterpoint, 2025.",
        "[14] U.S. Geological Survey, \"Mineral Commodity Summaries 2025: Gallium, Germanium, and Rare Earth Supply Chains,\" USGS, Reston, VA, 2025.",
        "[15] Taiwan Semiconductor Manufacturing Company, \"TSMC Annual Business Report and Advanced Technology Roadmaps,\" TSMC, 2025.",
        "[16] ASML Holding, \"ASML Investor Information: High-NA EUV Delivery Timelines and Photolithography Tool Shipments,\" ASML, 2026.",
        "[17] A. García-Herrero and S. Dutta, \"Programmable Sovereignty: Coordinated Specialization as a Response to the N-2 Problem in AI,\" Portulans & Bruegel, 2026.",
        "[18] R. Sharma, V. Patel, and A. Rao, \"Direct-to-Chip Liquid Cooling Architectures for Ultra-Dense AI Datacenters in Tropical Climates,\" IEEE TCPMT, 2026.",
        "[19] NVIDIA Corporation, \"NVIDIA DGX H100 Architecture Whitepaper: Power Delivery and Thermal Specifications,\" NVIDIA, Santa Clara, 2024.",
        "[20] W. Hannas, A. Chien, and L. Dunham, \"Geographic Concentration and Vulnerabilities in AI Hardware Manufacturing,\" CSET, Georgetown Univ., 2024.",
        "[21] K. Neaher and Z. Halaszi, \"Middle Powers in the AI Acceleration Race: Balancing Security, Compute, and Capital Alliances,\" Stimson Center, 2026.",
        "[22] SBI Capital Markets, \"Indian Data Centres: Powering the Digital Revolution — Capital Expenditure and PUE Baselines,\" SBICAP, 2025.",
        "[23] Colliers International India, \"India Data Centers: Entering the Gigawatt Era — Geographic Concentration,\" Colliers Research, 2026.",
    ]
    for r in refs:
        story.append(Paragraph(r, ref_style))

    doc.build(story)
    print(f"  [OK] Successfully compiled Revision v2 Review PDF to: {_OUTPUT_PDF}")


if __name__ == "__main__":
    build_pdf_v2()
