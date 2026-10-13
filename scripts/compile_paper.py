"""
Master PDF Compiler for ResearchThon 2026 IEEE Conference Paper
=============================================================
Compiles the authoritative LaTeX manuscript using pdflatex and bibtex,
ensuring strict compliance with IEEE format guidelines, balanced columns,
and accurate vector figures.

Outputs:
  - manuscript/main.pdf
  - output/final_paper.pdf
  - output/researchthon_paper.pdf
  - output/main.pdf
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
_MANUSCRIPT_DIR = _ROOT / "manuscript"
_OUTPUT_DIR = _ROOT / "output"
_MAIN_TEX = _MANUSCRIPT_DIR / "main.tex"
_COMPILED_PDF = _MANUSCRIPT_DIR / "main.pdf"

def compile_latex():
    print(f"=== Compiling LaTeX Paper: {_MAIN_TEX} ===")
    _OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Step 1: pdflatex
    print("[1/4] Running pdflatex (pass 1)...")
    res1 = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "main.tex"],
        cwd=str(_MANUSCRIPT_DIR),
        capture_output=True,
        text=True
    )
    if res1.returncode != 0:
        print("Warning: pdflatex pass 1 returned non-zero exit code.")

    # Step 2: bibtex
    print("[2/4] Running bibtex...")
    res_bib = subprocess.run(
        ["bibtex", "main"],
        cwd=str(_MANUSCRIPT_DIR),
        capture_output=True,
        text=True
    )
    if res_bib.returncode != 0:
        print("Warning: bibtex returned non-zero exit code.")

    # Step 3: pdflatex pass 2
    print("[3/4] Running pdflatex (pass 2)...")
    subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "main.tex"],
        cwd=str(_MANUSCRIPT_DIR),
        capture_output=True,
        text=True
    )

    # Step 4: pdflatex pass 3 (resolve all cross-refs and balances)
    print("[4/4] Running pdflatex (final pass)...")
    res_final = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "main.tex"],
        cwd=str(_MANUSCRIPT_DIR),
        capture_output=True,
        text=True
    )

    if not _COMPILED_PDF.exists():
        print("ERROR: Compilation failed, main.pdf not found.")
        sys.exit(1)

    print(f"Successfully generated: {_COMPILED_PDF} ({_COMPILED_PDF.stat().st_size:,} bytes)")

    # Copy to output destinations
    targets = [
        _OUTPUT_DIR / "final_paper.pdf",
        _OUTPUT_DIR / "main.pdf",
        _OUTPUT_DIR / "researchthon_paper.pdf",
    ]
    for dest in targets:
        shutil.copy2(_COMPILED_PDF, dest)
        print(f"  -> Synced to: {dest}")

    print("=== Paper Render Complete! ===")

if __name__ == "__main__":
    compile_latex()
