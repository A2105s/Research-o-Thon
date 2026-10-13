"""
Master PDF Compiler for Five-Pillar ResearchThon 2026 IEEE Paper
=============================================================================
Compiles output/final_paper.pdf complying with:
  - IEEE two-column conference layout on A4 paper
  - Central Five-Pillar Framework (IAIPF) driving the entire study
  - Supporting Six-Layer Demand Cascade as bounded engineering engine
  - All 6 master publication figures and 6 analytical tables
  - Boundary-disciplined cross-national benchmarking (India, US, China)
  - Running header: AMITY RESEARCHOTHON 2026 — IEEE FORMAT ALIGNED PROCEEDINGS
  - Balanced reference columns on the final page
"""

import os
import sys
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, 
    Table, TableStyle, Image, KeepTogether, PageBreak, FrameBreak, NextPageTemplate
)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.pdfgen import canvas

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

_ROOT = Path(r"D:\research 2.0\ResearchThon_Final")
_OUTPUT_PDF = _ROOT / "output" / "final_paper.pdf"
_FIGURES_DIR = _ROOT / "manuscript" / "figures"


class NumberedCanvas(canvas.Canvas):
    """Two-pass canvas to dynamically compute and display 'Page X of Y'."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        page_w, page_h = A4
        margin_left = 34
        margin_right = 34

        self.saveState()
        self.setFont('Times-Roman', 7.5)
        self.setFillColor(colors.HexColor('#333333'))

        # Running Header
        if self._pageNumber == 1:
            self.drawString(margin_left, page_h - 24, "AMITY RESEARCHOTHON 2026 — IEEE FORMAT ALIGNED PROCEEDINGS")
            self.drawRightString(page_w - margin_right, page_h - 24, "RESEARCH PAPER — TRACK: TECHNOLOGY & AI")
            self.setStrokeColor(colors.HexColor('#AAAAAA'))
            self.setLineWidth(0.5)
            self.line(margin_left, page_h - 28, page_w - margin_right, page_h - 28)
        else:
            self.drawString(margin_left, page_h - 24, "AMITY RESEARCHOTHON 2026 — TRACK: AI INFRASTRUCTURE & SOVEREIGNTY")
            self.drawRightString(page_w - margin_right, page_h - 24, "IEEE TWO-COLUMN PROCEEDINGS")
            self.setStrokeColor(colors.HexColor('#CCCCCC'))
            self.setLineWidth(0.5)
            self.line(margin_left, page_h - 28, page_w - margin_right, page_h - 28)

        # Running Footer
        page_str = f"Page {self._pageNumber} of {total_pages}"
        self.drawRightString(page_w - margin_right, 22, page_str)
        self.drawString(margin_left, 22, "A Five-Pillar Infrastructure Planning Framework for India's Sovereign AI")
        self.setStrokeColor(colors.HexColor('#CCCCCC'))
        self.setLineWidth(0.5)
        self.line(margin_left, 30, page_w - margin_right, 30)

        self.restoreState()


def build_ieee_pdf():
    print(f"[1/4] Preparing Five-Pillar IEEE paper compilation...")
    _OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)

    page_w, page_h = A4
    margin_top = 36
    margin_bottom = 36
    margin_left = 34
    margin_right = 34

    content_w = page_w - margin_left - margin_right # 527.27 pt
    content_h = page_h - margin_top - margin_bottom # 769.89 pt
    gutter = 14
    col_w = (content_w - gutter) / 2 # 256.63 pt

    # Page 1 Frames
    title_h = 100
    frame_title = Frame(margin_left, page_h - margin_top - title_h, content_w, title_h,
                        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='F_Title')
    col1_p1_h = content_h - title_h - 8
    frame_c1_p1 = Frame(margin_left, margin_bottom, col_w, col1_p1_h,
                        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='F_C1_P1')
    frame_c2_p1 = Frame(margin_left + col_w + gutter, margin_bottom, col_w, col1_p1_h,
                        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='F_C2_P1')

    # Standard Two-Column Frames for subsequent pages
    frame_c1_std = Frame(margin_left, margin_bottom, col_w, content_h,
                         leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='F_C1_Std')
    frame_c2_std = Frame(margin_left + col_w + gutter, margin_bottom, col_w, content_h,
                         leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='F_C2_Std')

    doc = BaseDocTemplate(str(_OUTPUT_PDF), pagesize=A4, leftMargin=margin_left, rightMargin=margin_right,
                          topMargin=margin_top, bottomMargin=margin_bottom)

    template_p1 = PageTemplate(id='Page1', frames=[frame_title, frame_c1_p1, frame_c2_p1])
    template_std = PageTemplate(id='PageStd', frames=[frame_c1_std, frame_c2_std])
    doc.addPageTemplates([template_p1, template_std])

    # ── Typography Styles ──────────────────────────────────────────
    title_style = ParagraphStyle('DocTitle', fontName='Times-Bold', fontSize=12.5, leading=15.5, alignment=TA_CENTER, textColor=colors.HexColor('#0D1B2A'))
    author_style = ParagraphStyle('DocAuthor', fontName='Times-Bold', fontSize=8.8, leading=11.2, alignment=TA_CENTER)
    affil_style = ParagraphStyle('DocAffil', fontName='Times-Roman', fontSize=7.4, leading=9.5, alignment=TA_CENTER, textColor=colors.HexColor('#333333'))

    h1_style = ParagraphStyle('SecH1', fontName='Times-Bold', fontSize=8.4, leading=10.6, spaceBefore=4.5, spaceAfter=2.0, textColor=colors.HexColor('#000000'), keepWithNext=True)
    h2_style = ParagraphStyle('SecH2', fontName='Times-Bold', fontSize=7.8, leading=9.8, spaceBefore=3.5, spaceAfter=1.5, textColor=colors.HexColor('#111111'), keepWithNext=True)
    body_style = ParagraphStyle('BodyText', fontName='Times-Roman', fontSize=7.4, leading=9.4, alignment=TA_JUSTIFY, spaceAfter=2.0)
    bullet_style = ParagraphStyle('BulletText', fontName='Times-Roman', fontSize=7.2, leading=9.0, alignment=TA_JUSTIFY, leftIndent=5, spaceAfter=1.6)
    abstract_style = ParagraphStyle('AbstractText', fontName='Times-Roman', fontSize=7.2, leading=9.0, alignment=TA_JUSTIFY, leftIndent=2, rightIndent=2, spaceAfter=2.0)
    caption_style = ParagraphStyle('Caption', fontName='Times-Italic', fontSize=6.6, leading=8.2, alignment=TA_CENTER, textColor=colors.HexColor('#222222'), spaceAfter=2.0, keepWithNext=True)
    tbl_cap_style = ParagraphStyle('TblCaption', fontName='Times-Bold', fontSize=6.6, leading=8.2, alignment=TA_CENTER, textColor=colors.HexColor('#000000'), spaceAfter=1.5, keepWithNext=True)
    ref_style = ParagraphStyle('RefEntry', fontName='Times-Roman', fontSize=6.2, leading=7.5, alignment=TA_JUSTIFY, spaceAfter=1.2, leftIndent=8, firstLineIndent=-8)

    # Table cell styles
    tc_h = ParagraphStyle('TCH', fontName='Times-Bold', fontSize=5.3, leading=6.6, alignment=TA_CENTER)
    tc_c = ParagraphStyle('TCC', fontName='Times-Roman', fontSize=5.1, leading=6.3, alignment=TA_CENTER)
    tc_l = ParagraphStyle('TCL', fontName='Times-Roman', fontSize=5.1, leading=6.3, alignment=TA_LEFT)

    def wrap_row(row, is_head=False, left_cols=None):
        out = []
        for idx, val in enumerate(row):
            if is_head:
                out.append(Paragraph(str(val), tc_h))
            elif left_cols and idx in left_cols:
                out.append(Paragraph(str(val), tc_l))
            else:
                out.append(Paragraph(str(val), tc_c))
        return out

    story = []

    # =========================================================================
    # PAGE 1 — TITLE BANNER
    # =========================================================================
    story.append(Paragraph("A Five-Pillar Infrastructure Planning Framework for India's Sovereign AI:<br/>Assessing Dependencies Across Compute, Energy, Data Centres, Connectivity, and Governance", title_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>Adarsh Singh, Sourav, and Anamidhi Shrivastava</b>", author_style))
    story.append(Paragraph("Department of Computer Science & Engineering, Amity School of Engineering and Technology<br/>Amity University Madhya Pradesh, Gwalior, India &bull; <i>{adarsh.singh, sourav, anamidhi.shrivastava}@amity.edu</i>", affil_style))
    story.append(FrameBreak())
    story.append(NextPageTemplate('PageStd'))

    # =========================================================================
    # COLUMN 1 — ABSTRACT & SECTION I (INTRODUCTION)
    # =========================================================================
    story.append(Paragraph("<b><i>Abstract</i>—National artificial intelligence (AI) strategies increasingly treat compute accelerators as primary instruments of technological sovereignty. However, genuine sovereign AI capability is not determined by silicon acquisition alone; it is bounded by an interdependent stack spanning power grids, thermal dissipation, physical water resources, international subsea connectivity, Indic data corpora, and industrial statecraft. This paper introduces the India AI Infrastructure Planning Framework (IAIPF), a structural model deconstructing national compute readiness into five non-substitutable pillars: (1) Compute and Semiconductor Sovereignty, (2) Energy and Grid Readiness, (3) Data Centres and Physical Resources, (4) Connectivity, Data and Secure Computing, and (5) Governance, Investment and Indigenous Capability. Grounded in empirical audits from the Central Electricity Authority (CEA), MeitY, JLL, CBRE, and USGS, we establish a verified India baseline and conduct boundary-disciplined comparative benchmarking against the United States and China. To inform the physical resource limits of Pillars 1–3, we deploy a supporting Six-Layer Demand-Cascade Model across 200k, 500k, and 1M GPU stress-test scenarios. For the 500k baseline, facility power reaches 891.8 MW (56.6% of India's 1,575 MW operational colocation capacity), annual energy 6.25 TWh, and cooling-water demand 11,250 ML/yr. Crucially, cross-pillar dependency analysis refutes the conventional 'foundry-first' dogma: front-end wafer starts absorb merely 1.60% of TSMC's sub-5nm output, whereas CoWoS advanced packaging consumes 7.41% (4.6x higher intensity) and substation energization queues impose 18–36 month lead times in metro clusters. Direct-to-Chip liquid cooling reduces on-site water consumption by 94.6% (to 631 ML/yr), while domestic multilingual data trusts mitigate a 3–6x Indic tokenization inference cost penalty. We synthesize these findings into an actionable, three-tier strategic roadmap prioritizing domestic packaging hubs, green grid corridors, and multilateral alliances.</b>", abstract_style))

    story.append(Paragraph("<b><i>Index Terms</i>—AI infrastructure planning, technological sovereignty, five-pillar framework, demand-cascade model, CoWoS packaging, power grid integration, tropical data centres, Indic tokenization, middle-power statecraft, IndiaAI Mission.</b>", abstract_style))
    story.append(Spacer(1, 2))

    story.append(Paragraph("I. INTRODUCTION AND RESEARCH PROBLEM", h1_style))
    story.append(Paragraph("Artificial intelligence has transitioned from an algorithmic discipline to a resource-intensive industrial apparatus governed by high-voltage electricity transmission, advanced microelectronics packaging, and global geopolitical supply chains [1]. Across leading economies, access to high-performance compute clusters is treated as an indispensable instrument of economic productivity and national security [21]. In India, this ambition is codified in the statutory authorizations of the IndiaAI Mission (Rs 10,371.92 crore; ~$1.25B USD) [2] and the India Semiconductor Mission (Semicon India 2.0; Rs 1,27,500 crore; ~$15.3B USD) [3].", body_style))
    story.append(Paragraph("However, prevailing policy discourse decouples accelerator procurement from the physical, ecological, and institutional systems required to sustain compute operations. Compute does not exist in isolation: an enterprise-scale AI cluster demands continuous megawatt-scale electricity, multi-year high-voltage substation interconnects, millions of litres of cooling water under tropical ambient heat, international submarine cable landings, and unbiased linguistic training data. Procuring silicon without concurrent infrastructure readiness creates stranded assets behind multi-year utility queues.", body_style))
    story.append(Paragraph("Furthermore, middle-power economies face what political economists term the <i>N-2 Problem</i> in technology sovereignty [17]: while superpowers (the United States and China) possess the domestic capital scale to pursue full-stack technology autarky, non-superpowers (N-2) cannot economically justify commercial sub-3nm foundries (>$30B capital expenditure per fab) without incurring catastrophic under-utilization. Attempting to replicate superpower autarky leads to severe misallocation of fiscal capital.", body_style))
    story.append(Paragraph("To address these challenges, this study investigates: <i>How can India assess and prioritise the infrastructure dependencies that shape its long-term AI capability across compute and semiconductors, energy and grid readiness, data centres and physical resources, connectivity and secure computing, and governance and indigenous capability?</i>", body_style))

    # =========================================================================
    # SECTION II — CRITICAL LITERATURE REVIEW & RESEARCH GAPS
    # =========================================================================
    story.append(Paragraph("II. CRITICAL LITERATURE REVIEW AND RESEARCH GAPS", h1_style))
    story.append(Paragraph("Existing scholarship remains bifurcated across disconnected domains: (a) <i>Microeconomic Hardware Chokepoints:</i> Akimitsu [1] maps upstream monopolistic concentration (HHI > 7,000–10,000), but omits data centres and grid interconnections. (b) <i>Data Centre Thermodynamics & Grid:</i> Shehabi et al. [6] establish server host factors (R_host = 1.82); IEA [5] forecasts 945 TWh global DC demand by 2030; Kaufmann et al. [9] highlight substation bottlenecks. Yet these assume temperate climates (PUE 1.15) and omit wafer/packaging physics. (c) <i>Middle-Power Sovereignty:</i> Portulans [17] and Stimson [21] formulate the N-2 taxonomy and Coordinated Specialization, but lack engineering quantification. (d) <i>Indian Colocation Censuses:</i> JLL [7], CBRE [8], and SBICAP [22] document 1,575 MW installed capacity (52.4% in Mumbai), but treat facilities as commercial real estate without modeling high-density AI clusters (40–100 kW/rack).", body_style))

    # TABLE I: Prior Art Comparison
    t1_raw = [
        ["Literature Source & Domain", "Primary Scope & Method", "Key Strength", "Critical Deficit Addressed in This Study"],
        ["Akimitsu (2026) [1]", "Econometric 40-stage HHI", "EUV, wafer, packaging monopolies", "Omits power grid, water, DC cooling, and policy"],
        ["LBNL / IEA (2024) [5, 6]", "Top-down macro TWh models", "Host power scaling (R_host=1.82)", "Assumes temperate PUE (1.15); omits tropical heat & fabs"],
        ["Portulans / Stimson [17, 21]", "Qualitative N-2 statecraft", "Coordinated Specialization theory", "Lacks engineering math; cannot quantify MW, TWh, or queues"],
        ["JLL / CBRE / SBICAP [7, 8, 22]", "Indian colocation censuses", "Accurate 1,575 MW stock census", "Omits chip demand, high-density racks, and subsea transit"],
        ["This Paper (IAIPF Model)", "Five-Pillar Bounded Cascade", "Integrates microelectronics to grid", "Resolves siloing, refutes wafer fallacy, models tropical PUE"],
    ]
    t1_data = [wrap_row(r, is_head=(i==0), left_cols=[0, 1, 2, 3]) for i, r in enumerate(t1_raw)]
    t1 = Table(t1_data, colWidths=[62, 60, 64, 70])
    t1.setStyle(TableStyle([
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.0),
        ('TOPPADDING', (0,0), (-1,-1), 1.0),
        ('LINEBELOW', (0,0), (-1,0), 0.8, colors.black),
        ('LINEBELOW', (0,-1), (-1,-1), 0.8, colors.black),
        ('LINEABOVE', (0,0), (-1,0), 0.8, colors.black),
    ]))
    story.append(Paragraph("TABLE I: SYSTEMATIC PRIOR ART BENCHMARK AND RESEARCH GAPS", tbl_cap_style))
    story.append(t1)
    story.append(Spacer(1, 2))

    # =========================================================================
    # SECTION III — METHODOLOGY & FIVE-PILLAR FRAMEWORK
    # =========================================================================
    story.append(Paragraph("III. RESEARCH METHODOLOGY AND THE FIVE-PILLAR FRAMEWORK", h1_style))
    story.append(Paragraph("The <b>India AI Infrastructure Planning Framework (IAIPF)</b> decomposes national compute readiness into five non-substitutable pillars (Fig. 1). Each pillar represents a necessary condition for sovereign AI capability: failure in any one pillar cascades through the entire stack. Crucially, the Six-Layer Demand Cascade is embedded not as an all-encompassing theory of sovereignty, but as an internal quantitative engineering engine calculating the physical resource requirements (MW, TWh, cooling water, wafer starts, packaging units) for Pillars 1–3.", body_style))

    # Embedded Figure 1
    f1_path = _FIGURES_DIR / "fig1_five_pillar_framework.png"
    if f1_path.exists():
        story.append(Image(str(f1_path), width=col_w, height=col_w * (6.2/10.0)))
        story.append(Paragraph("Fig. 1. The India AI Infrastructure Planning Framework (IAIPF): Five structural pillars supported by an internal Six-Layer Demand Cascade.", caption_style))

    # =========================================================================
    # SECTION IV — FIVE-PILLAR INFRASTRUCTURE ASSESSMENT
    # =========================================================================
    story.append(Paragraph("IV. FIVE-PILLAR INFRASTRUCTURE ASSESSMENT", h1_style))
    story.append(Paragraph("<b>A. Pillar 1: Compute and Semiconductor Sovereignty:</b> AI accelerators (e.g., NVIDIA GH100) are monolithic 814 mm^2 SoCs on sub-5nm nodes co-packaged with HBM3e via 2.5D CoWoS interposers delivering 3.35 TB/s bandwidth [15]. Upstream hardware tiers exhibit extreme concentration (Table II): EUV tools (ASML, HHI 10,000), sub-5nm fabs (TSMC 92%), 2.5D packaging (TSMC 89%), and refined gallium (China 98%). Under Semicon India 2.0 (Rs 1,27,500 crore) [3], India targets strategic insertion at packaging (Tata Sanand, Morigaon) and mature 28nm logic (Dholera), backed by 120,000 domestic VLSI design engineers (~20% of global talent in GCCs).", body_style))

    # TABLE II: Value Chain Chokepoints
    t2_raw = [
        ["Supply Chain Tier", "Dominant Entity", "Share", "Global HHI", "Lead Time"],
        ["EUV Lithography", "ASML (Netherlands)", "100%", "10,000", "24-36 mos"],
        ["Refined Gallium", "China (State entities)", "98%", "9,804", "Strategic"],
        ["Sub-5nm Logic Fabs", "TSMC (Taiwan)", "92%", "8,250", "14-18 wks"],
        ["2.5D CoWoS Packaging", "TSMC (Taiwan)", "89%", "8,100", "20-28 wks"],
        ["AI Accelerators (GPU)", "NVIDIA (United States)", "85%", "7,225", "26-52 wks"],
        ["HBM3e Memory Stacks", "SK Hynix / Samsung", "91%", "4,950", "16-24 wks"],
    ]
    t2_data = [wrap_row(r, is_head=(i==0), left_cols=[0, 1]) for i, r in enumerate(t2_raw)]
    t2 = Table(t2_data, colWidths=[62, 70, 28, 42, 54])
    t2.setStyle(TableStyle([
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.0),
        ('TOPPADDING', (0,0), (-1,-1), 1.0),
        ('LINEBELOW', (0,0), (-1,0), 0.8, colors.black),
        ('LINEBELOW', (0,-1), (-1,-1), 0.8, colors.black),
        ('LINEABOVE', (0,0), (-1,0), 0.8, colors.black),
    ]))
    story.append(Paragraph("TABLE II: UPSTREAM SEMICONDUCTOR VALUE CHAIN CONCENTRATION", tbl_cap_style))
    story.append(t2)
    story.append(Spacer(1, 2))

    story.append(Paragraph("<b>B. Pillar 2: Energy and Grid Readiness:</b> National compute clusters represent massive, localized baseload electrical shocks. Supplying 891.8 MW at 500k GPUs requires 18 dedicated 50 MW substations. Central Electricity Authority (CEA) transmission telemetry [4] reveals that 220kV/400kV GIS substation energization timelines extend 18–36 months, making grid civil engineering—not chip delivery—the primary temporal bottleneck. At 80% utilization and CEA grid carbon intensity of 0.716 t CO2/MWh, annual emissions reach 4.475 Mt CO2/yr, requiring 24/7 BESS-backed renewable power. In July 2026, CEA notified Cyber Security in Power Sector Regulations imposing mandatory compliance on all assets >= 50 MW [4].", body_style))

    story.append(Paragraph("<b>C. Pillar 3: Data Centres and Physical Resources:</b> India's commercial colocation capacity reached 1,575 MW in mid-2026 (projected to reach 6,500 MW by 2030) [7, 8]. However, geographic distribution is severely concentrated (Fig. 2): Mumbai commands 52.4% (825 MW) and Chennai 18.6%, placing over 71% of national capacity in two coastal metros. India's ambient summer temperatures regularly exceed 42 deg C, causing operational PUE to spike to 1.55 (vs 1.22 in US temperate zones). Wet cooling towers consume 1.80 L/kWh, dissipating 11,250 ML/yr at 500k scale and creating direct municipal drinking water conflict.", body_style))

    # Embedded Figure 4
    f4_path = _FIGURES_DIR / "fig4_metro_concentration.png"
    if f4_path.exists():
        story.append(Image(str(f4_path), width=col_w, height=col_w * (4.2/10.0)))
        story.append(Paragraph("Fig. 2. Indian Metro Infrastructure Concentration: Colocation capacity share (left) vs. subsea cables and substation lead times (right).", caption_style))

    story.append(Paragraph("<b>D. Pillar 4: Connectivity, Data and Secure Computing:</b> Physical compute is unproductive without domestic control over model weights and training corpora. Mumbai and Chennai host over 85% of India's 17+ international subsea cable systems (2Africa, Blue-Raman, SEA-ME-WE 6), explaining the severe metropolitan clustering of data centres. Furthermore, foreign LLMs impose an <i>Indic tokenization deficit</i> [2]: allocating 4–8 tokens per Hindi or Tamil word vs 1–2 per English word, inflicting a 3–6x inference cost penalty. Under the IndiaAI Mission, public capital has catalysed Sarvam AI's 105B model (22 Scheduled Languages) and the BharatGen multimodal consortium, backed by AI Kosh's 14,000 public datasets and 331 pre-trained models compliant with the DPDP Act 2023.", body_style))

    story.append(Paragraph("<b>E. Pillar 5: Governance, Investment and Indigenous Capability:</b> Under the Rs 10,372 crore IndiaAI Mission, shared GPU clusters (45,000 GPUs operational mid-2026, expanding to 100,000) are leased to domestic startups at Rs 65/GPU-hour (~$0.78 USD)—a 72.1% abatement below commercial rates of $2.80/hour [2]. By mid-2026, 9.32M GPU-hours were consumed, generating $18.8M in public surplus. India co-founded the Pax Silica coalition at the India AI Impact Summit 2026 [21] and participates in the Quad Semiconductor Supply Chain Initiative, securing capacity reservations in exchange for reciprocal critical mineral and talent access.", body_style))

    # =========================================================================
    # SECTION V — CROSS-PILLAR DEPENDENCY & BENCHMARKING
    # =========================================================================
    story.append(Paragraph("V. CROSS-PILLAR DEPENDENCY ANALYSIS AND BENCHMARKING", h1_style))
    story.append(Paragraph("<b>A. Inter-Pillar Dependency Pathways:</b> Deficits propagate across pillars (Fig. 3):<br/>"
                           "&bull; <i>Pathway A (Connectivity -> Physical -> Grid):</i> Subsea landings in Mumbai attract 52.4% of DC capacity, creating an 892 MW local power shock that triggers 18–36 month substation delays, stranding procured compute.<br/>"
                           "&bull; <i>Pathway B (Physical -> Grid -> Social License):</i> Summer heat spikes PUE to 1.55, driving evaporative water dissipation to 11,250 ML/yr and sparking municipal water conflicts in Chennai and Mumbai.<br/>"
                           "&bull; <i>Pathway C (Linguistic Data -> Compute -> Energy):</i> The Indic tokenization deficit multiplies inference token volume by 3–6x, inflating required GPU capacity and power draw.", body_style))

    # Embedded Figure 2
    f2_path = _FIGURES_DIR / "fig2_cross_pillar_dependencies.png"
    if f2_path.exists():
        story.append(Image(str(f2_path), width=col_w, height=col_w * (5.8/9.5)))
        story.append(Paragraph("Fig. 3. Cross-Pillar Constraint Interaction Pathways: Illustrating downstream constraint propagation across the infrastructure stack.", caption_style))

    story.append(Paragraph("<b>B. India–US–China Comparative Benchmarking:</b> Table III and Fig. 4 benchmark India against the US and China under disciplined comparability boundaries, confirming that India's primary structural strengths reside in chip design talent (20%) and public compute subsidization, while vulnerabilities cluster in physical packaging and metro grid queues.", body_style))

    # Embedded Figure 3
    f3_path = _FIGURES_DIR / "fig3_country_comparison.png"
    if f3_path.exists():
        story.append(Image(str(f3_path), width=col_w, height=col_w * (4.2/11.0)))
        story.append(Paragraph("Fig. 4. Multi-Pillar Quantitative Benchmarking: India vs. United States vs. China across operational colocation, microelectronics shares, and public outlays.", caption_style))

    # TABLE III: Multi-Pillar Benchmark
    t3_raw = [
        ["Pillar Domain", "Indicator", "India", "China", "United States", "Comparability Scope"],
        ["P1: Silicon", "Sub-5nm Logic Wafer Share", "0.0%", "<2.0%", "<5.0%", "Physical fab site; TSMC holds >90% [15]"],
        ["P1: Packaging", "2.5D CoWoS Advanced Pkg", "0.0%", "<3.0%", "<5.0%", "TSMC Taiwan holds ~90% [10]"],
        ["P1: Memory", "HBM3e Memory Production", "0.0%", "<1.0%", "~5.0%", "SK Hynix (57%) / Samsung (38%) [13]"],
        ["P1: Minerals", "Refined Gallium Share", "<0.5%", "98.0%", "0.0%", "USGS official mineral census [14]"],
        ["P1: Talent", "Global VLSI Design Workforce", "~20.0%", "~15.0%", "~35.0%", "India houses 120k chip designers [3]"],
        ["P2: Energy Grid", "National Peak Grid Demand", "250 GW", "1,350 GW", "745 GW", "Summer peak telemetry (CEA, State Grid)"],
        ["P3: Datacentres", "Colocation DC Capacity", "1,575 MW", "8,200 MW", "12,500 MW", "Operational colocation MW census [7]"],
        ["P3: Climate PUE", "Audited Operational PUE", "1.55", "1.38", "1.22", "Tropical baseline (>42 deg C summer) [22]"],
        ["P4: Compute", "Global Frontier AI Stock", "<3.0%", "12.0%", "75.0%", "Estimated enterprise accelerator stock [21]"],
        ["P5: Outlays", "Sovereign Public Outlays", "$16.55 B", "$47.50 B", "$52.70 B", "IndiaAI + ISM vs Big Fund vs CHIPS Act"],
    ]
    t3_data = [wrap_row(r, is_head=(i==0), left_cols=[0, 1, 5]) for i, r in enumerate(t3_raw)]
    t3 = Table(t3_data, colWidths=[42, 60, 24, 24, 28, 78])
    t3.setStyle(TableStyle([
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.8),
        ('TOPPADDING', (0,0), (-1,-1), 0.8),
        ('LINEBELOW', (0,0), (-1,0), 0.8, colors.black),
        ('LINEBELOW', (0,-1), (-1,-1), 0.8, colors.black),
        ('LINEABOVE', (0,0), (-1,0), 0.8, colors.black),
    ]))
    story.append(Paragraph("TABLE III: MULTI-PILLAR QUANTITATIVE BENCHMARK ACROSS NATIONS", tbl_cap_style))
    story.append(t3)
    story.append(Spacer(1, 2))

    # =========================================================================
    # SECTION VI — SUPPORTING DEMAND CASCADE & SCENARIO RESULTS
    # =========================================================================
    story.append(Paragraph("VI. SUPPORTING DEMAND-CASCADE METHODOLOGY AND RESULTS", h1_style))
    story.append(Paragraph("To inform the physical resource limits of Pillars 1–3, we deploy the Six-Layer Demand-Cascade Model across 200k, 500k, and 1M GPU scenarios (Table IV and Fig. 5):", body_style))
    story.append(Paragraph("<i>P<sub>IT</sub> = (N * P<sub>gpu</sub> * R<sub>host</sub>) / 10<sup>6</sup> &nbsp; [MW]</i> &nbsp;&nbsp;&nbsp;&nbsp; (1)<br/>"
                           "<i>P<sub>facility</sub> = P<sub>IT</sub> * PUE; &nbsp; E<sub>annual</sub> = (P<sub>facility</sub> * 8760 * U) / 10<sup>6</sup> &nbsp; [TWh]</i> &nbsp;&nbsp;&nbsp;&nbsp; (2)<br/>"
                           "<i>W<sub>annual</sub> = (E<sub>annual</sub> * 10<sup>6</sup> * WUE) / 10<sup>3</sup> &nbsp; [ML/yr]</i> &nbsp;&nbsp;&nbsp;&nbsp; (3)<br/>"
                           "<i>W<sub>starts</sub> = N / (N<sub>DPW</sub> * Y * Y<sub>fab</sub>); &nbsp; W<sub>CoWoS</sub> = N / (N<sub>int</sub> * Y<sub>CoWoS</sub>)</i> &nbsp;&nbsp;&nbsp;&nbsp; (4)", bullet_style))

    # TABLE IV: Scenario Cascade
    t4_raw = [
        ["Scenario", "Param", "IT (MW)", "Grid (MW)", "TWh/yr", "Water (ML)", "Wafer Starts", "TSMC %", "CoWoS %", "India DC %"],
        ["200k GPUs", "Low", "224.0", "280.0", "1.59", "318.9", "4,445", "0.57%", "2.47%", "17.8%"],
        ["", "Base", "254.8", "356.7", "2.50", "4,499.8", "5,000", "0.64%", "2.96%", "22.7%"],
        ["", "High", "420.0", "651.0", "5.13", "12,831.9", "10,527", "1.35%", "3.70%", "41.3%"],
        ["500k GPUs", "Low", "560.0", "700.0", "3.99", "797.2", "11,112", "1.42%", "6.17%", "44.4%"],
        ["(Baseline)", "Base", "637.0", "891.8", "6.25", "11,249.5", "12,500", "1.60%", "7.41%", "56.6%"],
        ["", "High", "1,050.0", "1,627.5", "12.83", "32,079.8", "26,316", "3.37%", "9.26%", "103.3%"],
        ["1M GPUs", "Low", "1,120.0", "1,400.0", "7.97", "1,594.3", "22,223", "2.85%", "12.35%", "88.9%"],
        ["", "Base", "1,274.0", "1,783.6", "12.50", "22,499.0", "25,000", "3.21%", "14.81%", "113.2%"],
        ["", "High", "2,100.0", "3,255.0", "25.66", "64,159.5", "52,632", "6.75%", "18.52%", "206.7%"],
    ]
    t4_data = [wrap_row(r, is_head=(i==0), left_cols=[0]) for i, r in enumerate(t4_raw)]
    t4 = Table(t4_data, colWidths=[38, 20, 24, 25, 22, 28, 24, 24, 25, 26])
    t4.setStyle(TableStyle([
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.8),
        ('TOPPADDING', (0,0), (-1,-1), 0.8),
        ('LINEBELOW', (0,0), (-1,0), 0.8, colors.black),
        ('LINEBELOW', (0,-1), (-1,-1), 0.8, colors.black),
        ('LINEABOVE', (0,0), (-1,0), 0.8, colors.black),
    ]))
    story.append(Paragraph("TABLE IV: SUPPORTING DEMAND-CASCADE SCENARIO RESULTS", tbl_cap_style))
    story.append(t4)
    story.append(Spacer(1, 2))

    # Embedded Figure 5
    f5_path = _FIGURES_DIR / "fig5_demand_cascade_scenarios.png"
    if f5_path.exists():
        story.append(Image(str(f5_path), width=col_w, height=col_w * (4.2/10.0)))
        story.append(Paragraph("Fig. 5. Demand-Cascade Resource Scaling (left) and the Structural Chokepoint Inversion (right).", caption_style))

    story.append(Paragraph("<b>Refuting the 'Silicon Wafer' Hypothesis:</b> A central empirical finding is that domestic front-end wafer fabrication is <i>not</i> the binding physical bottleneck:<br/>"
                           "&bull; <i>Wafer Starts:</i> 500,000 GPUs require 12,500 wafer starts—merely <b>1.60% of TSMC's sub-5nm annual output</b> (780,000 wafers).<br/>"
                           "&bull; <i>Packaging Bottleneck:</i> CoWoS packaging requires 33,334 interposer wafers—absorbing <b>7.41% of global capacity</b> (a chokepoint intensity <b>4.6x higher</b> than wafer fabrication).<br/>"
                           "&bull; <i>HBM Allocation:</i> Absorbs <b>6.67% of global HBM3e supply</b>, where India has zero domestic manufacturing.", body_style))

    story.append(Paragraph("<b>Cooling Technology Pareto Trade-offs:</b> Table V and Fig. 6 show that Direct-to-Chip (D2C) liquid cooling reduces on-site water consumption by <b>94.6%</b> (from 11,651 ML to 631 ML/yr) while lowering peak power draw by 172 MW, establishing D2C as a mandatory national standard.", body_style))

    # Embedded Figure 6
    f6_path = _FIGURES_DIR / "fig6_cooling_pareto.png"
    if f6_path.exists():
        story.append(Image(str(f6_path), width=col_w, height=col_w * (4.2/6.5)))
        story.append(Paragraph("Fig. 6. Cooling Technology Water--Energy Pareto Frontier under Tropical Ambient Heat.", caption_style))

    # TABLE V: Cooling Tradeoffs
    t5_raw = [
        ["Cooling Architecture", "Ann. PUE", "Peak PUE", "WUE (L/kWh)", "Water (ML/yr)"],
        ["Traditional Air (Evaporative)", "1.45", "1.65", "1.80", "11,651.2"],
        ["Rear-Door Heat Exchangers", "1.35", "1.45", "1.00", "6,031.5"],
        ["Direct-to-Chip (D2C) Liquid", "1.18", "1.25", "0.12", "630.9"],
        ["Single-Phase Immersion", "1.12", "1.18", "0.03", "150.8"],
    ]
    t5_data = [wrap_row(r, is_head=(i==0), left_cols=[0]) for i, r in enumerate(t5_raw)]
    t5 = Table(t5_data, colWidths=[66, 44, 46, 46, 54])
    t5.setStyle(TableStyle([
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.0),
        ('TOPPADDING', (0,0), (-1,-1), 1.0),
        ('LINEBELOW', (0,0), (-1,0), 0.8, colors.black),
        ('LINEBELOW', (0,-1), (-1,-1), 0.8, colors.black),
        ('LINEABOVE', (0,0), (-1,0), 0.8, colors.black),
    ]))
    story.append(Paragraph("TABLE V: COOLING TECHNOLOGY TRADEOFF MATRIX (500K GPUS)", tbl_cap_style))
    story.append(t5)
    story.append(Spacer(1, 2))

    # =========================================================================
    # SECTION VII — STRATEGIC ROADMAP & POLICY IMPLICATIONS
    # =========================================================================
    story.append(Paragraph("VII. DISCUSSION AND PRIORITISED PLANNING ROADMAP", h1_style))
    story.append(Paragraph("The quantitative findings direct an immediate <b>priority inversion</b>: debunking the capital-intensive 'foundry-first' doctrine (which requires >$30B capex and 7–10 year lead time) in favor of a <i>packaging-first</i> and <i>grid-first</i> sovereign posture. We operationalize this through a three-tier intervention matrix (Table VI):<br/>"
                           "<b>1) Tier 1: Domestic Build (2026–2028):</b> Spatial diversification rebates (15–20%) directing data centres away from Mumbai into power-surplus states (reducing Mumbai DC share below 35%); mandating D2C liquid cooling for clusters >= 20 kW/rack; fast-tracking 9-month CEA substation approval windows.<br/>"
                           "<b>2) Tier 2: Strategic JVs (2028–2031):</b> Expanding approved OSAT facilities (Tata, Micron) into 2.5D CoWoS interposers; extracting 50 t/yr high-purity gallium from red mud bauxite residue (CSIR-IMMT / NALCO); establishing open Indic data trusts.<br/>"
                           "<b>3) Tier 3: Managed External Dependencies (2031–2035):</b> Multi-year sovereign capacity reservations at TSMC via Pax Silica and bilateral HBM3e/HBM4 supply treaties with South Korea.", body_style))

    # TABLE VI: Roadmap
    t6_raw = [
        ["Horizon", "Target Pillar", "Key Intervention", "Lead Agency", "Target Outcome"],
        ["Tier 1 (2026-28)", "P3: Datacentres", "Mandate D2C liquid cooling", "MeitY / MoEFCC", "WUE < 0.15 L/kWh"],
        ["Tier 1 (2026-28)", "P2: Power Grid", "Spatial diversification rebates", "Min. of Power", "Mumbai DC < 35%"],
        ["Tier 1 (2026-28)", "P2: Interconnect", "Fast-track 9-mo CEA substation", "CEA / TRANSCOs", "Eliminate queue lag"],
        ["Tier 2 (2028-31)", "P1: Packaging", "2.5D CoWoS OSAT JVs", "Semi Mission", "10k interposers/mo"],
        ["Tier 2 (2028-31)", "P1: Minerals", "Red mud gallium extraction", "CSIR / Mines", "50 t/yr pure Ga"],
        ["Tier 2 (2028-31)", "P4: Indic Data", "Indic multilingual data trusts", "IndiaAI / C-DAC", "Token cost -70%"],
        ["Tier 3 (2031-35)", "P5: Diplomacy", "Pax Silica capacity treaties", "MEA / Quad", "Guaranteed TSMC share"],
        ["Tier 3 (2031-35)", "P1: Memory", "Bilateral HBM supply treaties", "Commerce", "Protected HBM quota"],
    ]
    t6_data = [wrap_row(r, is_head=(i==0), left_cols=[0, 1, 2]) for i, r in enumerate(t6_raw)]
    t6 = Table(t6_data, colWidths=[44, 48, 70, 48, 46])
    t6.setStyle(TableStyle([
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.8),
        ('TOPPADDING', (0,0), (-1,-1), 0.8),
        ('LINEBELOW', (0,0), (-1,0), 0.8, colors.black),
        ('LINEBELOW', (0,-1), (-1,-1), 0.8, colors.black),
        ('LINEABOVE', (0,0), (-1,0), 0.8, colors.black),
    ]))
    story.append(Paragraph("TABLE VI: THREE-TIER STRATEGIC INTERVENTION ROADMAP", tbl_cap_style))
    story.append(t6)
    story.append(Spacer(1, 2))

    story.append(Paragraph("<i>Limitations & Future Work:</i> The model assumes static annual utilization (80%) without dynamic diurnal inference dispatch. Future work will integrate real-time AC optimal power-flow simulations and empirical liquid-cooling testbeds under monsoon humidity regimes.", body_style))

    # =========================================================================
    # SECTION VIII — CONCLUSION & REFERENCES
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("VIII. CONCLUSION", h1_style))
    story.append(Paragraph("Sovereign artificial intelligence capability cannot be achieved by purchasing imported accelerators for deployment in power-constrained enclaves. This paper has formulated the <b>India AI Infrastructure Planning Framework (IAIPF)</b>, demonstrating that national AI scaling is bounded by an interdependent five-pillar architecture. By positioning the Demand Cascade as a supporting engineering model, we refute the belief that front-end wafer fabrication is India's binding constraint, proving that 2.5D packaging (7.41% global capacity), metropolitan substation queues (18–36 months), and Indic tokenization inefficiency represent the true structural bottlenecks. Resilient sovereignty demands disciplined, coordinated specialization in advanced packaging, green grid corridors, and domestic multilingual data trusts.", body_style))

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
    for i, r in enumerate(refs):
        if i == 12:
            story.append(FrameBreak())
        story.append(Paragraph(r, ref_style))

    print(f"[2/4] Building PDF document flow across two-column template...")
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[3/4] Successfully generated: {_OUTPUT_PDF}")


if __name__ == "__main__":
    build_ieee_pdf()
