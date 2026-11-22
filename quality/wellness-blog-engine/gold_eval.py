#!/usr/bin/env python3
"""Wellness Blog Engine gate step 3 prep: run the eval set's code rules on the REAL gold sample,
and check every quotation in it against the words on the source page.

Two parts:

  1. EVAL   Gravity-Studio PR #55 `portfolio/wellness-blog-engine/evals/check_posts.check()` (post_lint
            --presale + headline, disease, safety, lineage and testimonial checks). Its gold set only
            holds sample 001 (Black Seed, our own sample). This runs it on sample 002 (Winter Sun,
            the real-business sample), the one the gate scores.
  2. QUOTES Scorecard row 1 (Accuracy) and rubric row 1 (Faithful to sources) both turn on whether
            the post says no more than its sources. Every quotation in the post body must be in
            QUOTES below: words found verbatim on the source page, opened 2026-11-22. A quotation that
            is not in the table fails. The only exception is a sentence labelled [FRINGE] that
            reports what posts online claim (those quotes are the claims we refuse, not sources).

  The QUOTES table belongs to sample 002. A new sample adds its own rows after its pages are opened.
  A quote inside a [FRINGE] line is skipped, so a [FRINGE] line must only report online claims.

  Needs Gravity-Studio branch claude/wellness-negation-scope (stacked on PR #55). On PR #55's own
  branch the "disease claim in the body" plant is MISSED: a "not" later in the sentence hid it.

  python3 gold_eval.py gold-sample-002-winter-sun.md [--gs ../../../gravity-studio]   # exit 1 on any FAIL
  python3 gold_eval.py --test [--gs ...]   # plants errors in the REAL sample; each must be caught
Offline, standard library only. Never posts anything.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# Source pages, opened 2026-11-22 (Claude run 22:25 UTC, read in full or past every quoted line).
SOURCES = {
    "A": "Singh et al. 2011, AJTCAM 8(5 Suppl):208-213 - pmc.ncbi.nlm.nih.gov/articles/PMC3252722 (published 2011 Jul 3)",
    "B": "NIH ODS Ashwagandha Health Professional Fact Sheet - ods.od.nih.gov/factsheets/ashwagandha-HealthProfessional/ (Updated: May 2, 2025)",
    "C": "Memorial Sloan Kettering, About Herbs: Ashwagandha - mskcc.org/cancer-care/integrative-medicine/herbs/ashwagandha (Last Updated: July 28, 2026)",
}
# Each quote as it stands on the page (curly quotes normalised). Note = where the page goes on,
# so a reader can see the quote was not cut to change its meaning.
QUOTES = [
    ("The root smells like horse ('ashwa'), that is why it is called Ashwagandha", "A",
     "page continues '(on consuming it gives the power of a horse)'; the post paraphrases that next"),
    ("that promotes a youthful state of physical and mental health", "A", ""),
    ("commonly available as a churna, a fine sieved powder that can be mixed with water, ghee (clarified butter) or honey", "A", ""),
    ("when given with milk, it is the best tonic for children", "A", "in parentheses on the page; post adds 'not advice to copy for a child today'"),
    ("has been used in the traditional Ayurvedic and Unani medicine systems of India as an adaptogen", "B", ""),
    ("appeared to be greater with doses of 500 to 600 mg/day", "B", ""),
    ("more prominent when the dose was 600 mg/day and when the treatment duration was at least 8 weeks", "B", ""),
    ("may help reduce anxiety and stress and improve sleep", "B", ""),
    ("it is challenging to develop recommendations", "B", ""),
    ("Large scale clinical studies are needed to prove the clinical efficacy of this herb", "A",
     "page continues ', specially in stress related diseases, neuronal disorders and cancers.' - the cut narrows nothing the post claims"),
    ("appears to be well tolerated for up to about 3 months of use, but its long-term safety is not known", "B", ""),
    ("Don't use ashwagandha if you're pregnant because it may increase your risk of miscarriage", "C", ""),
    ("a few reports of more serious side effects, including adverse effects on liver function", "B", ""),
    ("might also affect thyroid function", "B", "page: 'Ashwagandha might also affect thyroid function and interact with some medications.'"),
    ("may also trigger or exacerbate autoimmune diseases", "C", "page: 'It may also trigger or exacerbate autoimmune diseases (79).'"),
    ("this effect has not been observed in humans", "C", ""),
]
QUOTE = re.compile(r'"([^"\n]+)"')


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip(" .,;:").lower()


KNOWN = {norm(q): src for q, src, _ in QUOTES}


def body_of(text):
    """Post body = from the H2 headline to Sources. Headline option titles are not quotations."""
    m = re.search(r"(?m)^## (?!Headline options)", text)
    start = m.start() if m else 0
    end = text.find("## Sources")
    return text[start:end if end > 0 else len(text)]


def quote_errors(text):
    errs, n = [], 0
    for line in body_of(text).splitlines():
        if line.startswith("## "):  # a heading's own phrase ("Smell of the Horse") is a title, not a source quote
            continue
        for q in QUOTE.findall(line):
            if "[FRINGE]" in line:
                continue
            n += 1
            if norm(q) not in KNOWN:
                errs.append(f"quote: not found on any opened source page: \"{q[:80]}\"")
    return errs, n


def load_check(gs):
    path = os.path.join(gs, "portfolio", "wellness-blog-engine", "evals")
    if not os.path.isfile(os.path.join(path, "check_posts.py")):
        sys.exit(f"check_posts.py not found under {path} (check out Gravity-Studio PR #55, branch claude/wellness-evals)")
    sys.path.insert(0, path)
    import check_posts  # noqa: E402
    return check_posts


def evaluate(text, cp):
    errs = cp.check(text)
    qerrs, n = quote_errors(text)
    return errs + qerrs, n


# Plants on the REAL sample. Each must be caught by the named check (proves the run isn't a rubber stamp).
PLANTS = [
    ("cure in a headline option", "headline",
     "2. **Ashwagandha in Your Pantry:", "2. **Ashwagandha Cures Anxiety:"),
    ("buyer's disease claim in the body", "disease",
     "So in its home tradition, ashwagandha is a slow, daily tonic, not a quick fix.",
     "So in its home tradition, ashwagandha reverses diabetes and is not a quick fix."),
    ("whole 'who should skip it' block cut", "safety",
     None, None),  # special-cased in self_test: everything from that heading to the bottom line goes
    ("unsourced age claim", "lineage",
     "a root that Indian medicine has kept in its pantry for a very long time.",
     "a root that Indian medicine has kept in its pantry for 3,000 years."),
    ("invented customer story", "testimonial",
     "So in its home tradition, ashwagandha is a slow, daily tonic, not a quick fix.",
     "One of our customers told us it changed her sleep. So in its home tradition, ashwagandha is a slow, daily tonic, not a quick fix."),
    ("quote stretched past its source", "quote",
     "\"may help reduce anxiety and stress and improve sleep,\"",
     "\"reliably reduces anxiety and stress and improves sleep,\""),
    ("quote invented and pinned on NIH", "quote",
     "So in its home tradition, ashwagandha is a slow, daily tonic, not a quick fix.",
     "NIH calls it \"one of the safest herbs in the world.\" So in its home tradition, ashwagandha is a slow, daily tonic, not a quick fix."),
]


def plant(text, old, new):
    if old is None:
        a, b = text.index("## Who should skip it"), text.index("## The bottom line")
        return text[:a] + text[b:]
    if text.count(old) != 1:
        raise ValueError(f"plant anchor must occur exactly once: {old[:60]!r}")
    return text.replace(old, new)


def self_test(sample, cp):
    text = open(sample, encoding="utf-8").read()
    wrong = 0
    errs, n = evaluate(text, cp)
    print(("PASS " if not errs else "FAIL ") + f"real sample as written ({n} quotations checked)")
    wrong += bool(errs)
    for label, kind, old, new in PLANTS:
        got = {e.split(":")[0] for e in evaluate(plant(text, old, new), cp)[0]}
        ok = kind in got
        wrong += not ok
        print(("CAUGHT " if ok else "MISSED ") + f"{label} [{kind}]" + ("" if ok else f" - got {sorted(got) or 'nothing'}"))
    unit = [
        ("[FRINGE] line's quoted online claim is not checked as a source quote",
         not quote_errors('## X\n**[FRINGE]** Posts claim it "cures anxiety".\n## Sources')[0]),
        ("curly quotes and a trailing comma still match", norm("“might also affect thyroid function,”".strip("“”")) in KNOWN),
        ("every table quote names a source page", all(src in SOURCES for _, src, _ in QUOTES)),
    ]
    for label, ok in unit:
        wrong += not ok
        print(("PASS " if ok else "FAIL ") + label)
    print(f"\nself-test: {len(PLANTS)} plants, {len(unit)} unit" + (" - OK" if not wrong else f" - {wrong} problem(s)"))
    return 1 if wrong else 0


def main(argv):
    gs = os.path.normpath(os.path.join(HERE, "..", "..", "..", "gravity-studio"))
    if "--gs" in argv:
        i = argv.index("--gs")
        gs = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    cp = load_check(gs)
    if "--test" in argv:
        return self_test(os.path.join(HERE, "gold-sample-002-winter-sun.md"), cp)
    if not argv:
        print(__doc__)
        return 2
    bad = 0
    for path in argv:
        errs, n = evaluate(open(path, encoding="utf-8").read(), cp)
        print(f"{path}: {'OK' if not errs else 'FAIL'} ({n} quotations, {n - sum(e.startswith('quote') for e in errs)} on a source page)")
        for e in errs:
            print("  -", e)
        bad += bool(errs)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
