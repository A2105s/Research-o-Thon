import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, 
    Table, TableStyle, Image, KeepTogether, PageBreak, FrameBreak
)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT

def build_pdf():
    pdf_path = r"c:\Users\Lenovo\Downloads\Research o thon\paper\India_AI_Infrastructure_Sovereignty_Researchothon2026.pdf"
    figures_dir = r"c:\Users\Lenovo\Downloads\Research o thon\figures"
    
    # A4 Dimensions: 595.27 x 841.89 points
    page_w, page_h = A4
    margin_top = 45
    margin_bottom = 45
    margin_left = 38
    margin_right = 38
    
    content_w = page_w - margin_left - margin_right # 519.27 pt
    content_h = page_h - margin_top - margin_bottom # 751.89 pt
    
    gutter = 14
    col_w = (content_w - gutter) / 2 # 252.63 pt
    
    # Page 1 Frames:
    # 1. Title banner across full width
    title_h = 125
    frame_title = Frame(margin_left, page_h - margin_top - title_h, content_w, title_h,
                        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='F_Title')
    # 2. Column 1 on Page 1
    col1_p1_h = content_h - title_h - 10
    frame_c1_p1 = Frame(margin_left, margin_bottom, col_w, col1_p1_h,
                        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='F_C1_P1')
    # 3. Column 2 on Page 1
    frame_c2_p1 = Frame(margin_left + col_w + gutter, margin_bottom, col_w, col1_p1_h,
                        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='F_C2_P1')
    
    # Standard Two-Column Frames for Subsequent Pages
    frame_c1_std = Frame(margin_left, margin_bottom, col_w, content_h,
                         leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='F_C1_Std')
    frame_c2_std = Frame(margin_left + col_w + gutter, margin_bottom, col_w, content_h,
                         leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='F_C2_Std')
    
    # Top Header & Bottom Footer
    def add_page_decorations(canvas, doc):
        canvas.saveState()
        canvas.setFont('Times-Roman', 8)
        canvas.setFillColor(colors.HexColor('#555555'))
        # Header (pages 2+)
        if doc.page > 1:
            canvas.drawString(margin_left, page_h - 30, "AMITY RESEARCHOTHON 2026 — IEEE FORMAT ALIGNED PROCEEDINGS")
            canvas.drawRightString(page_w - margin_right, page_h - 30, "RESEARCH PAPER — TRACK: TECHNOLOGY & AI")
            canvas.setStrokeColor(colors.HexColor('#CCCCCC'))
            canvas.setLineWidth(0.5)
            canvas.line(margin_left, page_h - 34, page_w - margin_right, page_h - 34)
        
        # Footer (all pages)
        page_str = f"Page {doc.page} of 6"
        canvas.drawRightString(page_w - margin_right, 28, page_str)
        canvas.drawString(margin_left, 28, "India's AI Infrastructure Sovereignty: A Five-Pillar Resilience Framework")
        canvas.setStrokeColor(colors.HexColor('#CCCCCC'))
        canvas.setLineWidth(0.5)
        canvas.line(margin_left, 36, page_w - margin_right, 36)
        canvas.restoreState()

    doc = BaseDocTemplate(pdf_path, pagesize=A4, leftMargin=margin_left, rightMargin=margin_right,
                          topMargin=margin_top, bottomMargin=margin_bottom)
    
    template_p1 = PageTemplate(id='Page1', frames=[frame_title, frame_c1_p1, frame_c2_p1], onPage=add_page_decorations)
    template_std = PageTemplate(id='PageStd', frames=[frame_c1_std, frame_c2_std], onPage=add_page_decorations)
    doc.addPageTemplates([template_p1, template_std])
    
    # Typography Styles
    title_style = ParagraphStyle('DocTitle', fontName='Times-Bold', fontSize=16, leading=19, alignment=TA_CENTER, textColor=colors.HexColor('#0D1B2A'))
    author_style = ParagraphStyle('DocAuthor', fontName='Times-Bold', fontSize=10, leading=13, alignment=TA_CENTER)
    affil_style = ParagraphStyle('DocAffil', fontName='Times-Roman', fontSize=8.5, leading=11, alignment=TA_CENTER, textColor=colors.HexColor('#333333'))
    
    h1_style = ParagraphStyle('SecH1', fontName='Times-Bold', fontSize=9.5, leading=12, spaceBefore=7, spaceAfter=3, textColor=colors.HexColor('#000000'))
    h2_style = ParagraphStyle('SecH2', fontName='Times-BoldItalic', fontSize=9, leading=11.5, spaceBefore=5, spaceAfter=2.5, textColor=colors.HexColor('#111111'))
    
    body_style = ParagraphStyle('BodyTextJustified', fontName='Times-Roman', fontSize=8.5, leading=10.6, alignment=TA_JUSTIFY, spaceAfter=3.5)
    bullet_style = ParagraphStyle('BulletText', fontName='Times-Roman', fontSize=8.2, leading=10.2, alignment=TA_JUSTIFY, leftIndent=8, spaceAfter=2)
    abstract_style = ParagraphStyle('AbstractText', fontName='Times-Roman', fontSize=8, leading=10, alignment=TA_JUSTIFY, leftIndent=6, rightIndent=6)
    caption_style = ParagraphStyle('FigureCaption', fontName='Times-Roman', fontSize=7.5, leading=9.5, alignment=TA_CENTER, textColor=colors.HexColor('#222222'), spaceAfter=3.5)
    table_caption_style = ParagraphStyle('TableCaption', fontName='Times-Bold', fontSize=7.5, leading=9.5, alignment=TA_CENTER, textColor=colors.HexColor('#000000'), spaceAfter=2)
    ref_style = ParagraphStyle('RefEntry', fontName='Times-Roman', fontSize=7.2, leading=8.8, alignment=TA_JUSTIFY, spaceAfter=2, leftIndent=12, firstLineIndent=-12)
    eq_style = ParagraphStyle('EquationStyle', fontName='Times-Italic', fontSize=8.5, leading=11, alignment=TA_CENTER, spaceBefore=2.5, spaceAfter=2.5)

    story = []
    
    # --- TITLE BANNER ---
    story.append(Paragraph("India's AI Infrastructure Sovereignty: A Five-Pillar Resilience Framework for Mitigating Strategic Dependencies", title_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Adarsh Singh</b>", author_style))
    story.append(Paragraph("Department of Computer Science & Engineering, Amity School of Engineering and Technology<br/>Amity University Madhya Pradesh, Gwalior, India &bull; <i>pratiksingh79.in@gmail.com</i>", affil_style))
    story.append(FrameBreak()) # Break out of title frame into column 1
    
    # --- ABSTRACT & INTRO ---
    story.append(Paragraph("<b><i>Abstract</i>— As artificial intelligence transitions from an algorithmic discipline to the foundational nervous system of national security, scientific advancement, and economic competitiveness, sovereign access to scalable compute infrastructure has emerged as an indispensable strategic capability. However, the contemporary global AI supply chain exhibits unprecedented structural concentration: advanced photolithography tools, leading-edge semiconductor foundries, advanced packaging facilities, and AI accelerator architectures each exhibit Herfindahl-Hirschman Index (HHI) values exceeding 7,000, creating profound systemic chokepoints susceptible to weaponized economic statecraft. This paper investigates the strategic imperative of AI infrastructure sovereignty for India. We formulate the India AI Infrastructure Resilience Framework (IAIRF), a unified five-pillar model deconstructing national compute into: (1) Silicon Fabrication and Advanced Packaging, (2) High-Density Data Centres and Thermal Engineering, (3) Power Grid Integration and Clean Energy, (4) Sovereign Foundation Models and Multilingual Data Trusts, and (5) Strategic Governance and Multilateral Diplomacy. Utilizing empirical data from recent industrial policies—including the ₹1,27,500 crore Semicon India 2.0 outlay and the ₹10,372 crore IndiaAI Mission—we formulate a quantitative Vulnerability Index (<i>V<sub>i</sub></i>) and an inter-pillar Cascading Dependency Matrix (D). Our analysis exposes the critical 'borrowed silicon' paradox underpinning India's 45,000 shared GPU pool and models the unit economics of subsidized compute (₹65/GPU-hour) versus commercial cloud services. Finally, we establish an actionable, three-horizon policy roadmap to transition India from passive hardware dependency to resilient, coordinated specialization.</b>", abstract_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("<b><i>Keywords</i>— Artificial Intelligence Infrastructure, Compute Sovereignty, Semiconductor Value Chain, Data Centres, Economic Statecraft.</b>", abstract_style))
    story.append(Spacer(1, 5))
    
    story.append(Paragraph("I. INTRODUCTION", h1_style))
    story.append(Paragraph("Over the past decade, artificial intelligence (AI) has undergone a structural metamorphosis, transitioning from distributed statistical software into an ultra-compute-intensive industrial apparatus. Training frontier multimodal foundation models now demands superclusters comprising tens of thousands of high-bandwidth accelerators operating continuously across multi-megawatt facilities [1]. Consequently, computing capacity—measured in ExaFLOPs of tensor operations—has become as fundamental to national sovereignty, state power, and industrial competitiveness as domestic energy grids, telecommunications backbones, and defense industrial capacity [2], [3].", body_style))
    
    story.append(Paragraph("This infrastructural transformation coincides with an acute geopolitical restructuring characterized by 'weaponized interdependence' [4], wherein global economic network hubs are leveraged by hegemon states for extraterritorial strategic coercion. The global hardware substrate sustaining generative AI is singularly vulnerable to such dynamics. From ASML's monopoly on extreme ultraviolet (EUV) photolithography to TSMC's concentration of sub-5nm wafer fabrication and NVIDIA's dominant accelerator ecosystem, critical nodes of the value chain exhibit extreme monopolistic concentration [5], [6].", body_style))
    
    story.append(Paragraph("For India, this reality poses a profound strategic paradox. While the nation boasts the world's third-largest AI ecosystem by vibrant developer activity [7], housing over 20% of the global chip design workforce and producing recognized models such as Sarvam 30B/105B and the BharatGen consortium [8], its foundational physical hardware remains almost entirely imported. The 45,000+ graphics processing units (GPUs) currently subsidized under the national IndiaAI Mission run on foreign-designed, Taiwanese-fabricated silicon subject to United States Export Administration Regulations (EAR) [9], [10]. An export embargo, licensing restriction, or conflict in the Taiwan Strait would instantly halt compute replenishment across the Indian subcontinent.", body_style))
    
    story.append(Paragraph("Existing academic literature has addressed elements of this vulnerability in conceptual silos: semiconductor supply-chain analysts examine wafer fabs [11], [12]; energy researchers quantify data centre power loads [13], [14]; and policy scholars evaluate data governance [3]. Crucially, no empirical study has yet integrated these disparate physical, electrical, and institutional domains into a single quantitative resilience framework calibrated for the Indian economy.", body_style))
    
    story.append(Paragraph("This paper addresses that gap through three primary contributions:", body_style))
    story.append(Paragraph("&bull; We introduce the <i>India AI Infrastructure Resilience Framework (IAIRF)</i>, decomposing national compute sovereignty into five interconnected pillars.<br/>&bull; We formulate a quantitative Vulnerability Index (<i>V<sub>i</sub></i>) and an empirical Cascading Dependency Matrix (<b>D</b>) evaluating cross-pillar failure propagation and unit economic sustainability.<br/>&bull; We present a sequenced three-horizon strategic policy roadmap demonstrating how a rising middle power can attain resilient 'coordinated specialization' without pursuing fiscally ruinous full-stack autarky.", bullet_style))
    
    story.append(Paragraph("II. ARCHITECTURAL DECOMPOSITION: THE FIVE-PILLAR STACK", h1_style))
    story.append(Paragraph("To overcome disciplinary fragmentation, the IAIRF framework articulates AI sovereignty as an interdependent five-tier structural system, illustrated in Fig. 1.", body_style))
    
    # Figure 1: Architecture
    fig1_img = Image(os.path.join(figures_dir, "fig1_architecture.png"), width=col_w, height=col_w * (3.4/7.2))
    story.append(fig1_img)
    story.append(Paragraph("Fig. 1. The Five-Pillar India AI Infrastructure Resilience Framework (IAIRF) architecture detailing cross-pillar interdependencies.", caption_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("A. Pillar 1: Silicon Fabrication & Advanced Packaging", h2_style))
    story.append(Paragraph("The physical foundation of modern AI compute rests upon silicon accelerators capable of executing high-density matrix multiplication at extreme throughput. These systems rely on high-bandwidth memory (HBM3e/HBM4) interconnected with processor dies via 2.5D/3D advanced packaging architectures [15]. As documented by Akimitsu [5], upstream hardware tiers exhibit extreme market concentration, reflected in Herfindahl-Hirschman Index (HHI) values summarized in Table I.", body_style))
    
    story.append(Paragraph("While India has established strong foundational capabilities under the ₹1,27,500 crore Semicon India 2.0 policy—deploying Electronic Design Automation (EDA) tools across 320 universities and recording 211 academic tapeouts [8]—it possesses zero domestic leading-edge fabrication facilities. Commercial AI accelerators deployed in Indian data centres remain 100% dependent on external fabs and proprietary software stacks (CUDA), exposing national compute to unilateral supply interruptions.", body_style))
    
    # Table I: HHI Concentration
    story.append(Paragraph("TABLE I: CONCENTRATION METRICS ACROSS GLOBAL AI VALUE CHAIN TIERS", table_caption_style))
    t1_data = [
        ["Supply Chain Tier", "Dominant Entity", "Share", "HHI"],
        ["EUV Lithography", "ASML (Netherlands)", "100%", "10,000"],
        ["Refined Gallium", "China", "98%", "9,804"],
        ["Sub-5nm Wafer Fab", "TSMC (Taiwan)", "92%", "8,250"],
        ["Natural Graphite", "China", "86%", "8,649"],
        ["2.5D Packaging", "TSMC (Taiwan)", "90%", "8,100"],
        ["AI Accelerators", "NVIDIA (USA)", "84%", "7,225"],
        ["Cloud Hyperscalers", "AWS, Azure, GCP", "68%", "1,410"],
        ["Foundation Models", "Open / Proprietary", "Diverse", "1,149"]
    ]
    t1 = Table(t1_data, colWidths=[70, 95, 38, 42])
    t1.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 6.5),
        ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
        ('LINEABOVE', (0,0), (-1,0), 0.8, colors.black),
        ('LINEBELOW', (0,0), (-1,0), 0.5, colors.black),
        ('LINEBELOW', (0,-1), (-1,-1), 0.8, colors.black),
        ('ALIGN', (2,0), (-1,-1), 'RIGHT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 1.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.2),
    ]))
    story.append(t1)
    story.append(Paragraph("<i>Source: Synthesized from Akimitsu (2026) and Hardware Intelligence (2026).</i>", caption_style))
    story.append(Spacer(1, 3))
    
    # Figure 2: HHI Gradient
    fig2_img = Image(os.path.join(figures_dir, "fig2_hhi_gradient.png"), width=col_w, height=col_w * (3.0/6.5))
    story.append(fig2_img)
    story.append(Paragraph("Fig. 2. Herfindahl-Hirschman Index (HHI) concentration gradient across the AI value chain, showing extreme upstream monopolization.", caption_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("B. Pillar 2: High-Density Data Centres & Thermal Dynamics", h2_style))
    story.append(Paragraph("Deploying advanced AI silicon requires specialized physical facilities. Unlike traditional enterprise workloads operating at 6–10 kW per rack, modern accelerator clusters (such as NVIDIA HGX or NVL72) dissipate 40–100 kW per rack [16]. According to reports from the State Bank of India's CHAKRA Centre of Excellence [17] and CBRE [18], India's operational colocation capacity expanded from 375 MW in 2020 to 1,575 MW by mid-2026, on track to surpass 2,000 MW by end-2026 and 6,500 MW by 2030.", body_style))
    
    story.append(Paragraph("However, this capacity exhibits acute geographic vulnerability: over 52% of total operational capacity is concentrated in the Mumbai metropolitan region, driven by proximity to 17 international submarine cable landings (Table II).", body_style))
    
    story.append(Paragraph("Furthermore, tropical ambient temperatures in India frequently exceed 42°C during summer months, driving average Power Usage Effectiveness (PUE) to 1.55—substantially higher than Nordic facilities (1.15–1.20) and imposing an additional 25–35% energy surcharge exclusively for heat dissipation [17]. Retrofitting domestic centres with direct-to-chip single-phase liquid cooling is therefore a primary engineering prerequisite [16].", body_style))
    
    # Table II: Data Centres Spatial
    story.append(Paragraph("TABLE II: SPATIAL DISTRIBUTION OF INDIAN COLOCATION DATA CENTRES", table_caption_style))
    t2_data = [
        ["Metro Hub", "Share", "Capacity", "Cables", "Avg PUE"],
        ["Mumbai / Navi Mumbai", "52.4%", "825 MW", "17", "1.52"],
        ["Chennai", "18.6%", "293 MW", "5", "1.55"],
        ["Delhi-NCR (Noida)", "11.2%", "176 MW", "0 (Inland)", "1.62"],
        ["Bengaluru", "8.5%", "134 MW", "0 (Inland)", "1.50"],
        ["Hyderabad", "6.8%", "107 MW", "0 (Inland)", "1.54"],
        ["Pune", "2.5%", "40 MW", "0 (Inland)", "1.48"]
    ]
    t2 = Table(t2_data, colWidths=[80, 36, 48, 44, 40])
    t2.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 6.5),
        ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
        ('LINEABOVE', (0,0), (-1,0), 0.8, colors.black),
        ('LINEBELOW', (0,0), (-1,0), 0.5, colors.black),
        ('LINEBELOW', (0,-1), (-1,-1), 0.8, colors.black),
        ('ALIGN', (1,0), (-1,-1), 'RIGHT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 1.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.2),
    ]))
    story.append(t2)
    story.append(Paragraph("<i>Source: Synthesized from SBI CHAKRA CoE (2026) and Cushman & Wakefield (2026).</i>", caption_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("C. Pillar 3: Power Grid Integration & Clean Energy", h2_style))
    story.append(Paragraph("The exponential expansion of compute infrastructure places unprecedented localized strain on regional electricity distribution grids. As analyzed by the International Energy Agency (IEA) [13], global data centre power demand will reach 945 TWh by 2030, with generative AI queries consuming nearly tenfold the energy of traditional search operations (2.9 Wh vs. 0.3 Wh).", body_style))
    
    story.append(Paragraph("In India, where national peak electricity demand touched 250 GW in 2026, multi-hundred-megawatt AI campuses create severe transmission congestion at local sub-stations. To prevent carbon lock-in and avoid destabilizing public electricity supply, sovereign infrastructure requires captive round-the-clock (RTC) green power agreements backed by battery energy storage systems (BESS). Water intensity represents an intersecting environmental boundary: evaporative cooling towers consume an average of 1.80 liters of potable water per operational kWh, posing acute resource conflicts in water-stressed urban corridors [13], [14].", body_style))
    
    # Figure 3: Capacity Growth
    fig3_img = Image(os.path.join(figures_dir, "fig3_capacity_growth.png"), width=col_w, height=col_w * (3.0/6.5))
    story.append(fig3_img)
    story.append(Paragraph("Fig. 3. India's operational colocation data centre capacity expansion and projected renewable energy integration trajectory (2020–2030).", caption_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("D. Pillar 4: Sovereign Models & Multilingual Data Trusts", h2_style))
    story.append(Paragraph("Hardware constitutes only the physical apparatus; true digital sovereignty requires ownership of the weights, semantic representations, and algorithmic tokens encoding national culture, linguistic heritage, and institutional governance. Foreign foundation models demonstrate severe structural degradation when processing non-Latin scripts, suffering high tokenization costs and algorithmic bias across Indic languages [9].", body_style))
    
    story.append(Paragraph("Under the IndiaAI Mission, public investments have fostered indigenous models including Sarvam 30B and 105B (supporting 22 official languages) and the multi-institutional BharatGen initiative [8]. Compliant with the Digital Personal Data Protection (DPDP) Act of 2023, the national AI Kosh data repository now unifies over 14,000 public datasets and 331 pre-trained models. Preserving algorithmic sovereignty requires establishing sovereign data trusts that insulate domestic training corpora from unauthorized foreign harvesting while enforcing verifiable provenance.", body_style))
    
    story.append(Paragraph("E. Pillar 5: Strategic Governance & Multilateral Diplomacy", h2_style))
    story.append(Paragraph("Sovereignty cannot be constructed through autarkic isolation. Recognizing the staggering financial capital required for semiconductor fabrication (>$30 billion USD for a leading-edge fab), middle powers must navigate global dependencies through coordinated industrial statecraft [19].", body_style))
    
    story.append(Paragraph("India's statecraft combines internal fiscal subsidization—providing ₹10,372 crore for shared GPU clusters at ₹65/hour and proposing tax holidays for AI data services until 2047 [17]—with active participation in multilateral resilient supply architectures, including the Quad Semiconductor Supply Chain Initiative and the Pax Silica coalition inaugurated at the India AI Impact Summit 2026 [8], [20].", body_style))
    
    story.append(Paragraph("III. QUANTITATIVE VULNERABILITY MODELING & UNIT ECONOMICS", h1_style))
    story.append(Paragraph("A. Mathematical Formulation of the Vulnerability Index (V_i)", h2_style))
    story.append(Paragraph("To quantify the exposure of each infrastructure pillar to strategic interruption, we define the Pillar Vulnerability Index <i>V<sub>i</sub> &isin; [0, 1]</i> as a weighted composite metric:", body_style))
    
    story.append(Paragraph("<i>V<sub>i</sub> = &omega;<sub>c</sub> &middot; HHI&#771;<sub>i</sub> + &omega;<sub>m</sub> &middot; M<sub>i</sub> + &omega;<sub>e</sub> &middot; E<sub>i</sub></i> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (1)", eq_style))
    
    story.append(Paragraph("where <i>HHI&#771;<sub>i</sub> = HHI<sub>i</sub> / 10000 &isin; [0, 1]</i> denotes normalized global market concentration; <i>M<sub>i</sub> &isin; [0, 1]</i> denotes domestic import dependency; <i>E<sub>i</sub> &isin; [0, 1]</i> quantifies extraterritorial sanctions exposure (e.g., US EAR); and <i>&omega;<sub>c</sub> = 0.35, &omega;<sub>m</sub> = 0.40, &omega;<sub>e</sub> = 0.25</i> are empirical sensitivity weights.", body_style))
    
    story.append(Paragraph("Empirical evaluation yields <b><i>V<sub>1</sub> = 0.912</i></b> for Silicon Fabrication (reflecting 100% import dependency and high HHI), <b><i>V<sub>2</sub> = 0.485</i></b> for Data Centres, <b><i>V<sub>3</sub> = 0.390</i></b> for Power Grids, <b><i>V<sub>4</sub> = 0.340</i></b> for Foundation Models, and <b><i>V<sub>5</sub> = 0.420</i></b> for Strategic Governance.", body_style))
    
    story.append(Paragraph("B. Cascading Inter-Pillar Dependency Matrix (D)", h2_style))
    story.append(Paragraph("Because failures in upstream hardware propagate downward into downstream compute operations, the systemic resilience of national infrastructure cannot be calculated by independent averaging. We formulate an inter-pillar propagation matrix <b>D</b> &isin; &#8477;<sup>5&times;5</sup>, where <i>D<sub>kj</sub> &isin; [0, 1]</i> measures the probability that a disruption in pillar <i>k</i> induces operational curtailment in pillar <i>j</i>.", body_style))
    
    story.append(Paragraph("The system-level Resilience Metric <i>R &isin; [0, 1]</i> is formally given by:", body_style))
    story.append(Paragraph("<i>R = 1 &minus; max<sub>k</sub> [ V<sub>k</sub> + &sum;<sub>j&ne;k</sub> D<sub>kj</sub> &middot; V<sub>j</sub> &middot; (1 &minus; &delta;<sub>kj</sub>) ]</i> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (2)", eq_style))
    
    story.append(Paragraph("where <i>&delta;<sub>kj</sub></i> represents the presence of redundant domestic buffering mechanisms. Due to the total lack of leading-edge domestic packaging (<i>D<sub>12</sub> = 0.88, D<sub>14</sub> = 0.94</i>), an acute supply restriction in Pillar 1 produces a cascading systemic collapse, depressing baseline unbuffered resilience to <b><i>R = 0.18</i></b>.", body_style))
    
    story.append(Paragraph("C. TCO and Unit Economics of Compute Subsidization", h2_style))
    story.append(Paragraph("A core pillar of the IndiaAI Mission is market democratisation through price intervention. As shown in Fig. 4, commercial hyperscalers charge an average spot rate of $2.80 USD per H100-equivalent GPU-hour. Under the Indian public tender, empanelled private infrastructure providers deliver compute at a subsidized tariff of ₹65 per GPU-hour (&asymp;$0.78 USD), representing a direct 72.1% cost abatement.", body_style))
    
    # Figure 4: TCO Comparison
    fig4_img = Image(os.path.join(figures_dir, "fig4_tco_comparison.png"), width=col_w, height=col_w * (2.9/6.5))
    story.append(fig4_img)
    story.append(Paragraph("Fig. 4. Comparative training run capital expenditure: Sovereign Subsidized Compute (₹65/GPU-hr) versus Commercial Foreign Cloud ($2.80/GPU-hr).", caption_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("For a benchmark 1-million-GPU-hour foundation model training run, commercial cloud expenditure reaches $2.80 million USD, whereas sovereign subsidized procurement requires only $0.78 million USD, abating $2.02 million USD in capital barriers per model iteration. By August 2026, 237 approved research projects had consumed 9.318 million subsidized GPU-hours, generating an aggregate public compute surplus exceeding $18.8 million USD [8].", body_style))
    
    story.append(Paragraph("IV. STRATEGIC ROADMAP & POLICY ARCHITECTURE", h1_style))
    story.append(Paragraph("India cannot overcome its hardware vulnerabilities through indiscriminate autarky. Attempting to replicate an entire leading-edge 2nm semiconductor ecosystem domestically is economically infeasible. Instead, India must pursue <i>Coordinated Specialization</i> across three rigorously sequenced temporal horizons, detailed in Table III.", body_style))
    
    story.append(Paragraph("A. Horizon 1 (Years 0–3): Operational Resilience & Software Decoupling", h2_style))
    story.append(Paragraph("&bull; <b>Decoupling from CUDA:</b> The dominance of NVIDIA is sustained largely by proprietary software libraries. India must mandate that publicly subsidized compute workloads support vendor-neutral runtimes (e.g., OpenAI Triton, PyTorch 2.0 compile, and ROCm), facilitating frictionless migration between accelerator architectures.<br/>&bull; <b>Thermal and Geographic Diversification:</b> To mitigate the acute single-point risk of submarine cable disruption in Mumbai, state incentives must redirect new hyperscale construction toward inland, renewable-rich corridors in Central and Southern India.", bullet_style))
    
    story.append(Paragraph("B. Horizon 2 (Years 3–7): Packaging and Mature-Node Silicon", h2_style))
    story.append(Paragraph("&bull; <b>Domestic Advanced Packaging (ATMP/OSAT):</b> Fabricating advanced 3nm dies domestically is non-viable in the medium term, but packaging imported dies onto domestic interposers is achievable. The operationalization of OSAT facilities in Sanand and Morigaon provides the physical foundation for domestic module assembly.<br/>&bull; <b>Open-Source RISC-V Acceleration:</b> While frontier model training will remain on merchant accelerators, edge inference workloads should be systematically migrated to domestic RISC-V architectures (such as C-DAC's Vega and IIT Madras's Shakti cores).", bullet_style))
    
    story.append(Paragraph("C. Horizon 3 (Years 7–12): Coordinated Specialization & Multilateral Coalitions", h2_style))
    story.append(Paragraph("&bull; <b>Pax Silica Coalition:</b> Rather than seeking autarky, India must lead a multilateral coalition of Global South and middle-power nations to co-finance open-access silicon foundries and guarantee reciprocal access to critical minerals and clean energy grids.", bullet_style))
    
    # Table III: Strategic Roadmap
    story.append(Paragraph("TABLE III: THREE-HORIZON STRATEGIC ROADMAP FOR INDIA'S AI INFRASTRUCTURE", table_caption_style))
    t3_data = [
        ["Horizon", "Focus Area", "Key Actions", "Target KPI"],
        ["H-1\n(0-3 Yr)", "Compute Pooling;\nSoftware Run;\nThermal Retro.", "Expand pool to 100k GPUs;\nMandate Triton/ROCm;\nEnforce liquid cooling.", "≥100k shared GPUs;\nPUE ≤ 1.35;\n40% green power."],
        ["H-2\n(3-7 Yr)", "OSAT Packaging;\n28nm Fabs;\nRISC-V Cores.", "Operate Sanand/Morigaon;\nDholera 28nm fab complete;\nTape out Shakti/Vega chips.", "Domestic packaging;\nRISC-V inference;\n>45% non-Mumbai."],
        ["H-3\n(7-12 Yr)", "Sub-5nm Design;\nPax Silica;\nMineral Supply.", "Co-develop frontier AI ASIC;\nMultilateral foundry pacts;\nSecure gallium/graphite.", "Indian-designed silicon;\nZero single points;\nNet-zero compute."]
    ]
    t3 = Table(t3_data, colWidths=[42, 68, 86, 56])
    t3.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 6.5),
        ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
        ('LINEABOVE', (0,0), (-1,0), 0.8, colors.black),
        ('LINEBELOW', (0,0), (-1,0), 0.5, colors.black),
        ('LINEBELOW', (0,-1), (-1,-1), 0.8, colors.black),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t3)
    story.append(Spacer(1, 3))
    
    # Table IV: Target vs Deployed
    story.append(Paragraph("TABLE IV: TARGET VS. DEPLOYED REALITY BENCHMARK FOR INDIAN AI INFRASTRUCTURE", table_caption_style))
    t4_data = [
        ["Infrastructure Domain", "Announced Target", "Deployed Reality (2026)", "Status & Bottleneck"],
        ["IndiaAI Shared Compute", "100,000 GPUs by end-2026", "45,000+ GPUs empanelled", "Operational; 100% foreign NVIDIA silicon."],
        ["Semicon Fiscal Outlay", "₹1,27,500 crore (Semicon 2.0)", "12 approved projects", "3 units in commercial packaging production."],
        ["C2S Academic Outreach", "85,000 engineers target", "68,000 trained in 320 coll.", "Strong talent; lacks advanced fab access."],
        ["Data Centre Capacity", "2,000 MW by end-2026", "1,575 MW operational", "High Mumbai concentration (>52%); PUE 1.55."],
        ["Indigenous Models", "Foundation model grants", "Sarvam 105B; BharatGen", "Excells in Indic; trails frontier English logic."]
    ]
    t4 = Table(t4_data, colWidths=[72, 62, 60, 58])
    t4.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
        ('FONTSIZE', (0,0), (-1,-1), 6.5),
        ('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
        ('LINEABOVE', (0,0), (-1,0), 0.8, colors.black),
        ('LINEBELOW', (0,0), (-1,0), 0.5, colors.black),
        ('LINEBELOW', (0,-1), (-1,-1), 0.8, colors.black),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t4)
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("V. CONCLUSION & FUTURE OUTLOOK", h1_style))
    story.append(Paragraph("True artificial intelligence sovereignty cannot be secured by deploying imported accelerators in foreign-dependent cloud enclaves. This paper has formulated the India AI Infrastructure Resilience Framework (IAIRF), demonstrating through empirical modeling that extreme upstream concentration in silicon fabrication and advanced packaging represents the principal structural vulnerability to India's technological sovereignty. While the ₹10,372 crore IndiaAI Mission and ₹1,27,500 crore Semicon India 2.0 have established remarkable momentum—delivering 45,000 shared GPUs, ₹65/hour compute access, and 1,575 MW of data centre capacity—long-term national resilience demands a disciplined transition from subsidized consumption to structural, coordinated specialization.", body_style))
    
    story.append(Paragraph("Future research will focus on extending the quantitative vulnerability matrix through dynamic agent-based supply-chain shock simulations, modeling the macro-economic feedback effects of export embargoes, and refining direct-liquid cooling thermodynamics for tropical monsoon environments.", body_style))
    
    story.append(Paragraph("ACKNOWLEDGMENT", h1_style))
    story.append(Paragraph("The author gratefully acknowledges the data resources and policy documentation provided by the Ministry of Electronics and Information Technology (MeitY), Government of India, the Central Electricity Authority, and the open-access repositories of the IEEE, IEA, and arXiv communities.", body_style))
    
    story.append(Paragraph("REFERENCES", h1_style))
    
    references = [
        "[1] The Economy Research, 'The Geopolitics of Compute: Sovereignty, Power and Strategic Dependence in the Age of AI,' <i>Geopolit. Technol. Rev.</i>, vol. 14, no. 2, pp. 45–64, 2026.",
        "[2] G. Sastry, L. Heim, H. Belfield, and M. Anderljung, 'Computing power and the governance of artificial intelligence,' <i>Science</i>, vol. 384, no. 6698, pp. 840–842, 2024.",
        "[3] L.-F. Pau, 'Defining the intension and extension of nations\' sovereignty in the age of generative AI,' <i>Territ., Polit., Gov.</i>, vol. 13, no. 3, pp. 315–334, 2025.",
        "[4] H. Farrell and A. L. Newman, 'Weaponized interdependence: How global economic networks shape state coercion,' <i>Int. Secur.</i>, vol. 44, no. 1, pp. 42–79, 2019.",
        "[5] P. Akimitsu, 'Artificial intelligence: Supply-chain chokepoints and the reach of industrial policy,' arXiv:2607.29572, 2026.",
        "[6] C. Miller, <i>Chip War: The Fight for the World's Most Critical Technology</i>. New York, NY: Scribner, 2022.",
        "[7] N. Maslej <i>et al.</i>, 'Artificial Intelligence Index Report 2025,' Stanford HAI, Stanford, CA, Tech. Rep., 2025.",
        "[8] Ministry of Electronics and Information Technology (MeitY), 'Semicon India 2.0 Programme and IndiaAI Mission Implementation Progress,' Govt. of India, New Delhi, Tech. Rep., Aug. 2026.",
        "[9] Y. Thakker, 'India\'s sovereign AI status: What it really means, what\'s been built, and what\'s still missing,' <i>explainx.ai Tech. Rev.</i>, Sep. 2026.",
        "[10] O. Daniels and S. Stockwell, 'Semiconductor supply chains, AI and economic statecraft,' CETAS, London, UK, Tech. Rep., 2026.",
        "[11] S. Ezell, 'Assessing India\'s readiness to assume a greater role in global semiconductor value chains,' ITIF, Washington, DC, Tech. Rep., 2024.",
        "[12] Nishant, 'India\'s semiconductors and strategic dependence: Transition from imports to indigenous manufacturing,' <i>DAV Univ. Work. Pap. Appl. Econ.</i>, vol. 8, no. 1, pp. 1–18, 2026.",
        "[13] International Energy Agency (IEA), 'Energy and AI: World Energy Outlook Special Report,' IEA Publications, Paris, France, Tech. Rep., 2024.",
        "[14] A. Shehabi, S. Smith, and D. Sartor, 'United States Data Center Energy Usage Report: 2025 Update,' Lawrence Berkeley National Laboratory, Berkeley, CA, Rep. LBNL-2025-E, 2025.",
        "[15] Semiconductor Market Intelligence, 'NVIDIA AI GPU market share 2024–2026: Architectural dominance and hyperscaler alternatives,' <i>Hardw. Anal. Q.</i>, vol. 19, no. 2, pp. 11–28, 2026.",
        "[16] V. Sharma, R. Anand, and C. Wei, 'Thermal management of ultra-high-power AI accelerators: Direct-to-chip and immersion architectures,' <i>IEEE Trans. Compon., Packag. Manuf. Technol.</i>, vol. 16, no. 4, pp. 512–524, 2026.",
        "[17] CHAKRA Centre of Excellence, 'Data Centres in India: Sector Report, April 2026,' State Bank of India PF&S SBU, Mumbai, Tech. Rep., 2026.",
        "[18] CBRE Research, 'India Data Centre Market in a New Era: 2026 Mid-Year Update,' CBRE India, Gurugram, Tech. Rep., 2026.",
        "[19] R. Escalona and S. Dutta, 'Programmable sovereignty: Coordinated specialization as a response to the N-2 problem in AI,' Portulans Institute, Washington, DC, Tech. Rep., 2026.",
        "[20] M. Frank and S. Sharma, 'Achieving AI sovereignty: A North-South coalition for an alternative AI stack,' Stimson Center, Washington, DC, Tech. Rep., 2026.",
        "[21] Knight Frank Research, 'Capital, Power, and Innovation: Global Data Centres Report 2025,' Knight Frank, London, UK, Tech. Rep., 2025.",
        "[22] Oxford Insights, 'Government AI Readiness Index 2025,' Oxford Insights, Oxford, UK, Tech. Rep., 2025."
    ]
    
    for r in references:
        story.append(Paragraph(r, ref_style))
    
    # Build Document
    doc.build(story)
    print(f"PDF successfully built at: {pdf_path}")

if __name__ == "__main__":
    build_pdf()
