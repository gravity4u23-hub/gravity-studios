#!/usr/bin/env python3
"""render_resume.py — turns a checked resume .txt into the Word + PDF files the gig promises.

The .txt is the single source of truth: it is what resume_lint and gold_check grade.
The .docx is built from it line by line (no words added), and the PDF is converted
from that .docx by LibreOffice, so all three carry the same text.

Layout is applicant-tracking-system (ATS) safe, which is the point of a resume file:
one column, no tables, no text boxes, no images, nothing in headers/footers,
a standard font (Calibri 11, fallback Carlito in the PDF), plain section headings.

Usage:
  python3 render_resume.py IN.txt OUT_DIR     -> OUT_DIR/<stem>.docx and <stem>.pdf
Needs: python-docx, LibreOffice (soffice) on PATH.
"""
import os, subprocess, sys, tempfile
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

FONT = "Calibri"


def _is_heading(line):
    s = line.strip()
    return bool(s) and s.isupper() and len(s) < 40


def build_docx(lines, path):
    doc = Document()
    sec = doc.sections[0]
    sec.top_margin = sec.bottom_margin = Inches(0.7)
    sec.left_margin = sec.right_margin = Inches(0.8)
    normal = doc.styles["Normal"]
    normal.font.name, normal.font.size = FONT, Pt(10.5)
    normal.paragraph_format.space_after = Pt(2)
    body = [l.rstrip() for l in lines]
    # optional SYNTHETIC marker line (our samples only), then the name (or contact line), then the body
    first = next(i for i, l in enumerate(body) if l.strip() and "SYNTHETIC" not in l)
    for i, line in enumerate(body):
        if not line.strip():
            continue
        if "SYNTHETIC" in line:  # the SYNTHETIC marker stays visible: no real person in our samples
            p = doc.add_paragraph()
            r = p.add_run(line)
            r.italic, r.font.size = True, Pt(8.5)
            continue
        if i == first and "|" not in line:  # the buyer's name; a contact-only line stays plain
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(line)
            r.bold, r.font.size = True, Pt(14)
            continue
        if _is_heading(line):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(8)
            r = p.add_run(line.strip())
            r.bold, r.font.size = True, Pt(11.5)
            continue
        if line.lstrip().startswith("- "):
            # plain "- " text bullet, not a Word list: survives every ATS parser and copy-paste
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.2)
            p.paragraph_format.first_line_indent = Inches(-0.15)
            p.add_run(line.strip())
            continue
        p = doc.add_paragraph()
        r = p.add_run(line.strip())
        if " | " in line and ("—" in line or "–" in line):  # job title line
            r.bold = True
    doc.save(path)


def to_pdf(docx_path, out_dir):
    with tempfile.TemporaryDirectory() as prof:
        subprocess.run(
            ["soffice", f"-env:UserInstallation=file://{prof}", "--headless",
             "--convert-to", "pdf", "--outdir", out_dir, docx_path],
            check=True, capture_output=True, timeout=120)
    return os.path.join(out_dir, os.path.splitext(os.path.basename(docx_path))[0] + ".pdf")


def main(src, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    stem = os.path.splitext(os.path.basename(src))[0]
    lines = open(src, encoding="utf-8").read().splitlines()
    docx_path = os.path.join(out_dir, stem + ".docx")
    build_docx(lines, docx_path)
    pdf_path = to_pdf(docx_path, out_dir)
    print(docx_path)
    print(pdf_path)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
