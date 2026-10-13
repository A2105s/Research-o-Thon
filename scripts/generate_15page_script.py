"""
Build Script Generator for 15-Page IEEE Transactions Paper
==========================================================
Generates the comprehensive, production-ready build_15page_paper.py script.
"""

import sys
from pathlib import Path

_ROOT = Path(r"D:\research 2.0\ResearchThon_Final")
_TARGET = _ROOT / "scripts" / "build_15page_paper.py"

header_code = '''"""
Comprehensive 15-Page IEEE Transactions-Length Compiler for ResearchThon 2026
=============================================================================
Compiles output/final_paper.pdf to AT LEAST 15 pages complying with:
  - IEEE two-column format on A4 paper
  - Central Five-Pillar Framework (IAIPF) driving the entire research study
  - Supporting Six-Layer Demand Cascade as bounded engineering engine
  - Complete, exhaustive academic prose across 15 comprehensive sections
  - 6 Master Publication Figures & 20 Detailed Academic Tables
  - Running Header: AMITY RESEARCHOTHON 2026 — IEEE FORMAT ALIGNED PROCEEDINGS
  - Dynamic Two-Pass NumberedCanvas ('Page X of Y')
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
import pypdf

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

_ROOT = Path(r"D:\\research 2.0\\ResearchThon_Final")
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
            self.drawRightString(page_w - margin_right, page_h - 24, "IEEE TRANSACTIONS-LENGTH MONOGRAPH")
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
'''

print("Writing generator script...")
