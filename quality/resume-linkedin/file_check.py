#!/usr/bin/env python3
"""file_check.py — standing check on the Word + PDF resume files we deliver.

A resume file can go wrong in ways the .txt check never sees: a word dropped or
added while formatting, a table or text box that applicant-tracking systems (ATS)
skip, contact details hidden in a header, a PDF whose text can't be selected,
or a resume that spills onto a second page. Each is checked by code here.

Checks for a .txt + .docx + .pdf trio:
  1. The .docx text equals the .txt word for word (same words, same order).
  2. The .pdf text (pdftotext) equals the .txt word for word, i.e. it is selectable text, not an image.
  3. The .docx has no tables, no images/text boxes, and empty headers and footers.
  4. The PDF is 1 page (entry-level resume).
  5. The text pulled from the PDF passes resume_lint against the buyer's own inputs
     (so the file the buyer receives is graded, not just our .txt).
  6. The SYNTHETIC marker is the first line of both files (no real person in our samples).

Usage:
  python3 file_check.py            # checks gold-sample/rewrite.{txt,docx,pdf}
  python3 file_check.py --test     # self-tests: a drifted .docx and a 2-page PDF must fail
Needs: python-docx, pdftotext, pdfinfo (poppler), and LibreOffice for --test.
"""
import os, re, subprocess, sys, tempfile
from docx import Document

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from resume_lint import lint

G = os.path.join(HERE, "gold-sample")
read = lambda p: open(p, encoding="utf-8").read()


def words(text):
    # "–" and "—" are kept as words; bullets and spacing differences are ignored
    return re.findall(r"[^\s·•]+", text.replace(" ", " "))


def docx_text(path):
    return "\n".join(p.text for p in Document(path).paragraphs)


def pdf_text(path):
    return subprocess.run(["pdftotext", "-layout", path, "-"], check=True,
                          capture_output=True, text=True).stdout


def pdf_pages(path):
    out = subprocess.run(["pdfinfo", path], check=True, capture_output=True, text=True).stdout
    return int(re.search(r"^Pages:\s+(\d+)", out, re.M).group(1))


def docx_structure(path):
    d = Document(path)
    problems = []
    if d.tables:
        problems.append(f"{len(d.tables)} table(s)")
    xml = d.element.xml
    for tag, name in (("<w:drawing", "image/drawing"), ("<w:pict", "picture"), ("<w:txbxContent", "text box")):
        if tag in xml:
            problems.append(name)
    for s in d.sections:
        for part in (s.header, s.footer):
            if any(p.text.strip() for p in part.paragraphs):
                problems.append("text in header/footer")
    return problems


def first_diff(a, b):
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return f"word {i}: expected {x!r}, got {y!r}"
    return f"length {len(a)} vs {len(b)}"


def check(txt_path, docx_path, pdf_path, source, post, max_pages=1):
    src = words(read(txt_path))
    dtx, ptx = docx_text(docx_path), pdf_text(pdf_path)
    res = []
    dw, pw = words(dtx), words(ptx)
    res.append(("docx text == txt", dw == src, "" if dw == src else first_diff(src, dw)))
    res.append(("pdf text == txt (selectable)", pw == src, "" if pw == src else first_diff(src, pw)))
    probs = docx_structure(docx_path)
    res.append(("docx is ATS-safe (no tables/images/text boxes/header text)", not probs, ", ".join(probs)))
    n = pdf_pages(pdf_path)
    res.append((f"pdf is {n} page(s) <= {max_pages}", n <= max_pages, ""))
    errs, warns = lint(source, ptx, post)
    res.append(("pdf text passes resume_lint", not errs and not warns, "; ".join(errs + warns)))
    marked = all("SYNTHETIC" in t.strip().splitlines()[0] for t in (dtx, ptx))
    res.append(("SYNTHETIC marker on line 1 of both files", marked, ""))
    return res


def report(res):
    ok = 0
    for name, good, detail in res:
        ok += good
        print(f"{'ok ' if good else 'BAD'} {name} {detail if detail and not good else ''}")
    print(f"{ok}/{len(res)}")
    return ok == len(res)


def inputs():
    return read(os.path.join(G, "original.txt")) + "\n" + read(os.path.join(G, "buyer-answers.txt")), \
        read(os.path.join(G, "job-post.txt"))


def selftest():
    from render_resume import build_docx, to_pdf
    source, post = inputs()
    base = read(os.path.join(G, "rewrite.txt"))
    cases = []
    with tempfile.TemporaryDirectory() as tmp:
        # A: an invented result slipped in while formatting -> docx/pdf drift + lint must fail
        t = os.path.join(tmp, "a.txt"); open(t, "w").write(base)
        d = os.path.join(tmp, "a.docx")
        build_docx((base.replace("Bilingual in English and Spanish.",
                                 "Bilingual in English and Spanish. Grew sales 20%.")).splitlines(), d)
        p = to_pdf(d, tmp)
        r = check(t, d, p, source, post)
        cases.append(("drifted file (added 'Grew sales 20%') fails text match + lint",
                      not r[0][1] and not r[1][1] and not r[4][1]))
        # B: the same resume padded to 2 pages must fail the page check
        t2 = os.path.join(tmp, "b.txt")
        long = base + "\n" + "\n".join(f"- Filler line {i} for a page test." for i in range(80))
        open(t2, "w").write(long)
        d2 = os.path.join(tmp, "b.docx"); build_docx(long.splitlines(), d2)
        p2 = to_pdf(d2, tmp)
        r2 = check(t2, d2, p2, source + " " + " ".join(str(i) for i in range(80)), post)
        cases.append(("2-page file fails the page check", not r2[3][1]))
        # C: a table in the docx must fail the ATS check
        d3 = os.path.join(tmp, "c.docx"); build_docx(base.splitlines(), d3)
        doc = Document(d3); doc.add_table(rows=1, cols=2); doc.save(d3)
        cases.append(("docx with a table fails the ATS check", bool(docx_structure(d3))))
        # D: the real files pass
        cases.append(("gold files pass", all(g for _, g, _ in run_gold(quiet=True))))
    ok = sum(g for _, g in cases)
    for n, g in cases:
        print(f"{'ok ' if g else 'BAD'} {n}")
    print(f"self-tests {ok}/{len(cases)}")
    return ok == len(cases)


def run_gold(quiet=False):
    source, post = inputs()
    j = lambda n: os.path.join(G, n)
    return check(j("rewrite.txt"), j("rewrite.docx"), j("rewrite.pdf"), source, post)


if __name__ == "__main__":
    if "--test" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(0 if report(run_gold()) else 1)
