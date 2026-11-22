#!/usr/bin/env python3
"""check_resumes.py — Resume + LinkedIn eval set runner (code-graded rules).

Runs every case in cases.json:
  * the GOLD delivery must pass every rule (warnings count as failures), and
  * the BAD delivery must fail, on the rule named in 'bad_breaks'
    (proves the checker isn't rubber-stamping).
It also runs the new rules over the real gold sample (../gold-sample/).

Rules (all code, no judgment):
  invented_numbers      any number, year, % or $ not in the buyer's own text (resume_lint)
  stock_phrases         template phrases like "results-driven" (resume_lint)
  untargeted            fewer than 3 job-post keywords used (resume_lint warning)
  invented_credentials  a degree, diploma, certificate or license the buyer never listed
  title_inflation       a seniority word (Manager, Supervisor, Senior...) in a job title
                        that isn't in any of the buyer's own job titles
  private_data          birth date, street address, SSN or marital status on the resume
  ai_note               the delivery note lacks the "AI-assisted" line
  linkedin_limits       headline over 220 characters or About over 2,600

Usage:
  python3 check_resumes.py            run the eval set (exit 0 = all as expected)
  python3 check_resumes.py --test     self-tests for the helper rules
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from resume_lint import lint  # noqa: E402

YEAR_RANGE = re.compile(r"\b(?:19|20)\d{2}\s*[-–—]\s*(?:(?:19|20)\d{2}|present)\b", re.I)
SENIORITY = ["manager", "director", "supervisor", "senior", "head", "chief", "vp",
             "president", "executive", "lead", "principal", "owner"]
CREDENTIALS = [r"\bdegree\b", r"\bbachelor", r"\bmaster'?s\b", r"\bmba\b", r"\bph\.?d\b",
               r"\bdiploma\b", r"\bged\b", r"\bcertified\b", r"\bcertification\b",
               r"\bcertificate\b", r"\blicen[sc]ed?\b"]
PRIVATE = {
    "birth date": re.compile(r"\b(?:dob|date of birth|born)\b", re.I),
    "street address": re.compile(r"\b\d{2,6}\s+(?:[NSEW]\.?\s+)?[A-Za-z]+\s+"
                                 r"(?:st|street|ave|avenue|rd|road|blvd|dr|drive|ln|lane|way|ct|court|pl)\b", re.I),
    "SSN": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    "marital status": re.compile(r"\b(?:married|single|divorced|widowed)\b", re.I),
}


def titles(text):
    """Job-title part of every line that carries a year range."""
    out = []
    for line in text.splitlines():
        if YEAR_RANGE.search(line):
            out.append(re.split(r"\s[-–—]\s|,|\|", line, maxsplit=1)[0].strip().lower())
    return out


def words(s):
    return set(re.findall(r"[a-z]+", s.lower()))


def check(source, job_post, delivery):
    """Return the set of rules this delivery breaks, with details."""
    broken = {}
    resume = "\n".join(delivery["resume"])
    linked = "\n".join(delivery.get(k, "") for k in ("headline", "about"))
    errs, warns = lint(source, resume + "\n" + linked, job_post)
    for e in errs:
        broken["invented_numbers" if e.startswith("invented") else "stock_phrases"] = e
    if warns:
        broken["untargeted"] = "; ".join(warns)
    low_src, low_out = source.lower(), (resume + "\n" + linked).lower()
    creds = [p for p in CREDENTIALS if re.search(p, low_out) and not re.search(p, low_src)]
    if creds:
        broken["invented_credentials"] = ", ".join(creds)
    src_title_words = set().union(*[words(t) for t in titles(source)] or [set()])
    inflated = sorted({w for t in titles(resume) for w in words(t)
                       if w in SENIORITY and w not in src_title_words})
    if inflated:
        broken["title_inflation"] = ", ".join(inflated)
    found = [name for name, rx in PRIVATE.items() if rx.search(resume + "\n" + linked)]
    if found:
        broken["private_data"] = ", ".join(found)
    if "ai-assisted" not in delivery.get("note", "").lower():
        broken["ai_note"] = "delivery note has no AI-assisted line"
    if len(delivery.get("headline", "")) > 220 or len(delivery.get("about", "")) > 2600:
        broken["linkedin_limits"] = f"headline {len(delivery.get('headline', ''))} chars"
    return broken


def run():
    data = json.load(open(os.path.join(HERE, "cases.json"), encoding="utf-8"))
    ok = total = 0
    for c in data["cases"]:
        src, post = "\n".join(c["source"]), data["job_posts"][c["job_post"]]
        g = check(src, post, c["gold"])
        good = not g
        print(f"{'ok ' if good else 'BAD'} {c['id']}: gold {'passes' if good else 'FAILS ' + str(g)}")
        ok += good; total += 1
        b = check(src, post, c["bad"])
        good = c["bad_breaks"] in b
        extra = sorted(set(b) - {c["bad_breaks"]})
        print(f"{'ok ' if good else 'BAD'} {c['id']}: bad caught on {c['bad_breaks']}"
              f"{' (also ' + ', '.join(extra) + ')' if extra else ''}" if good else
              f"BAD {c['id']}: bad NOT caught on {c['bad_breaks']} (got {sorted(b)})")
        ok += good; total += 1
    # the real gold sample must pass the new rules too
    gs = os.path.join(os.path.dirname(HERE), "gold-sample")
    rd = lambda n: open(os.path.join(gs, n), encoding="utf-8").read()
    src = rd("original.txt") + "\n" + rd("buyer-answers.txt")
    li = rd("linkedin.txt")
    head = li.split("ABOUT")[0].replace("HEADLINE", "").strip()
    about = li.split("ABOUT", 1)[1].strip() if "ABOUT" in li else ""
    delivery = {"resume": rd("rewrite.txt").splitlines(), "headline": head, "about": about,
                "note": "AI-assisted drafting, every line edited and checked by a person."}
    g = check(src, rd("job-post.txt"), delivery)
    good = not g
    print(f"{'ok ' if good else 'BAD'} gold-sample (Guess ASM): {'passes all rules' if good else g}")
    ok += good; total += 1
    print(f"{ok}/{total}")
    return ok == total


def _test():
    cases = [
        ("titles() reads year lines only", titles("Shift Lead - X | 2020 - Present\nRan the store"), ["shift lead"]),
        ("en dash range", titles("Store Manager — Y | 2019 – 2021"), ["store manager"]),
        ("comma title", titles("Server, Copper Grill, 2019 - Present"), ["server"]),
        ("address caught", bool(PRIVATE["street address"].search("4127 W Palm Lane")), True),
        ("city/state not an address", bool(PRIVATE["street address"].search("Phoenix, AZ 85009")), False),
        ("dob caught", bool(PRIVATE["birth date"].search("DOB 03/14/1991")), True),
        ("'single' as adjective is still flagged (known limit, safe side)",
         bool(PRIVATE["marital status"].search("single location")), True),
    ]
    ok = 0
    for name, got, want in cases:
        good = got == want
        ok += good
        print(f"{'ok ' if good else 'BAD'} {name}: {got!r}")
    # summary line mentioning 'manager' must not count as a title
    b = check("Shift Lead, A, 2020 - Present", "manager store cash schedule train",
              {"resume": ["Shift Lead - A | 2020 - Present", "- Ran the store when the manager was out; cash, schedule, train."],
               "note": "AI-assisted"})
    good = "title_inflation" not in b
    ok += good
    print(f"{'ok ' if good else 'BAD'} 'manager' outside a title line is fine: {sorted(b)}")
    total = len(cases) + 1
    print(f"{ok}/{total}")
    return ok == total


if __name__ == "__main__":
    sys.exit(0 if (_test() if sys.argv[1:] == ["--test"] else run()) else 1)
