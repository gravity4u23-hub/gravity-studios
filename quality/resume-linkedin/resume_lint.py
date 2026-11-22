#!/usr/bin/env python3
"""resume_lint.py — checks a rewritten resume against the buyer's original.

Blocks the two things resume buyers complain about most (benchmark.md):
  1. Invented facts: any number, year, % or $ amount in the rewrite that is not
     in the original resume / buyer's answers.
  2. Template language: stock phrases that make a resume read generic or AI-made.
Also warns when no keyword from the target job post appears in the rewrite.

Usage:
  python3 resume_lint.py ORIGINAL.txt REWRITE.txt [JOB_POST.txt]
  python3 resume_lint.py --test
Exit 0 = pass, 1 = fail.
"""
import re, sys

STOCK = [
    "results-driven", "results driven", "dynamic", "proven track record",
    "detail-oriented", "detail oriented", "go-getter", "synergy", "team player",
    "hard-working", "hardworking", "self-starter", "think outside the box",
    "passionate about", "seasoned professional", "highly motivated",
    "best-in-class", "rockstar", "ninja", "spearheaded", "leveraged",
]
STOP = set("""a an the and or of to in on for with at by from as is are be was were
this that your you our we will can able job role team work working experience years
skills required preferred plus must including other new more""".split())

NUM = re.compile(r"\$?\d[\d,]*(?:\.\d+)?%?")


def numbers(text):
    """Normalized numbers: '$1,200' -> '1200', '35%' -> '35'."""
    return {n.replace("$", "").replace(",", "").rstrip("%").rstrip(".") for n in NUM.findall(text)}


def keywords(text):
    words = re.findall(r"[a-zA-Z][a-zA-Z+#.-]{2,}", text.lower())
    return {w.strip(".-") for w in words if w not in STOP}


def lint(original, rewrite, job_post=None):
    errors, warnings = [], []
    invented = sorted(numbers(rewrite) - numbers(original), key=lambda x: (len(x), x))
    if invented:
        errors.append("invented numbers (not in the original): " + ", ".join(invented))
    low = rewrite.lower()
    stock = [p for p in STOCK if p in low and p not in original.lower()]
    if stock:
        errors.append("stock phrases: " + ", ".join(stock))
    if job_post:
        overlap = keywords(job_post) & keywords(rewrite)
        if len(overlap) < 3:
            warnings.append(f"only {len(overlap)} job-post keywords used — not targeted")
    return errors, warnings


def _test():
    orig = "Cashier, Fry's Food, 2019-2023. Handled about 300 customers a day. Trained 4 new hires."
    post = "Retail supervisor. Train new cashiers, handle customer complaints, cash office, scheduling."
    cases = [
        ("clean rewrite", "Cashier, Fry's Food, 2019-2023. Served about 300 customers a day; trained 4 new cashiers and handled customer complaints.", True),
        ("invented percent", "Cashier, Fry's Food, 2019-2023. Cut wait times 25% serving 300 customers a day.", False),
        ("invented money", "Cashier, Fry's Food, 2019-2023. Balanced $12,000 in daily cash.", False),
        ("inflated count", "Cashier, Fry's Food, 2019-2023. Trained 12 new hires.", False),
        ("changed year", "Cashier, Fry's Food, 2018-2023. Trained 4 new hires.", False),
        ("stock phrase", "Results-driven cashier, Fry's Food, 2019-2023, trained 4 new hires.", False),
        ("phrase the buyer used is allowed", None, True),
        ("comma number same value", "Handled about 300 customers a day across 2019-2023; trained 4.", True),
    ]
    ok = 0
    for name, rewrite, should_pass in cases:
        o = orig
        if rewrite is None:  # buyer's own words are theirs to keep
            o = orig + " Team player."
            rewrite = "Team player. Cashier, Fry's Food, 2019-2023, trained 4 new hires."
        errs, _ = lint(o, rewrite, post)
        passed = not errs
        good = passed == should_pass
        ok += good
        print(f"{'ok ' if good else 'BAD'} {name}: {'pass' if passed else 'fail'} {errs if errs else ''}")
    # targeting warning
    _, warns = lint(orig, "Cashier 2019-2023, 300 a day, 4 hires.", post)
    good = bool(warns)
    ok += good
    print(f"{'ok ' if good else 'BAD'} untargeted rewrite warns: {warns}")
    total = len(cases) + 1
    print(f"{ok}/{total}")
    return ok == total


if __name__ == "__main__":
    if sys.argv[1:] == ["--test"]:
        sys.exit(0 if _test() else 1)
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    read = lambda p: open(p, encoding="utf-8").read()
    errs, warns = lint(read(sys.argv[1]), read(sys.argv[2]), read(sys.argv[3]) if len(sys.argv) > 3 else None)
    for w in warns:
        print("WARN", w)
    for e in errs:
        print("FAIL", e)
    print("OK" if not errs else "FAIL")
    sys.exit(1 if errs else 0)
