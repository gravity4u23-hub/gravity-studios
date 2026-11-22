#!/usr/bin/env python3
"""gold_check.py — standing check for the Resume + LinkedIn gold sample (gate step 2).

Checks, all code-graded:
  1. rewrite.txt and linkedin.txt pass resume_lint against original.txt + buyer-answers.txt
     (no number, year, % or $ the buyer didn't give; no stock phrase; targeted at job-post.txt).
  2. known-bad-rewrite.txt FAILS resume_lint (proves the checker isn't rubber-stamping).
  3. Every resume file says SYNTHETIC at the top (no real person's details in the repo).
  4. LinkedIn limits: headline <= 220 characters, About <= 2,600 characters.
Usage: python3 gold_check.py   (exit 0 = all pass)
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from resume_lint import lint

G = os.path.join(HERE, "gold-sample")
read = lambda n: open(os.path.join(G, n), encoding="utf-8").read()


def section(text, name):
    """Text under an ALL-CAPS heading until the next ALL-CAPS heading."""
    out, on = [], False
    for line in text.splitlines():
        if line.strip().isupper() and line.strip():
            on = line.strip() == name
            continue
        if on:
            out.append(line)
    return "\n".join(out).strip()


def main():
    source = read("original.txt") + "\n" + read("buyer-answers.txt")
    post = read("job-post.txt")
    results = []
    for f in ("rewrite.txt", "linkedin.txt"):
        errs, warns = lint(source, read(f), post)
        results.append((f"{f} passes resume_lint", not errs and not warns, errs + warns))
    errs, _ = lint(source, read("known-bad-rewrite.txt"), post)
    results.append(("known-bad-rewrite.txt is caught", bool(errs), errs))
    for f in ("original.txt", "rewrite.txt", "known-bad-rewrite.txt"):
        results.append((f"{f} marked SYNTHETIC", "SYNTHETIC" in read(f).splitlines()[0], ""))
    li = read("linkedin.txt")
    head, about = section(li, "HEADLINE"), section(li, "ABOUT")
    results.append((f"headline {len(head)} <= 220 chars", 0 < len(head) <= 220, ""))
    results.append((f"About {len(about)} <= 2600 chars", 0 < len(about) <= 2600, ""))
    ok = 0
    for name, good, detail in results:
        ok += good
        print(f"{'ok ' if good else 'BAD'} {name} {detail if detail and not good else ''}")
    print(f"{ok}/{len(results)}")
    return ok == len(results)


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
