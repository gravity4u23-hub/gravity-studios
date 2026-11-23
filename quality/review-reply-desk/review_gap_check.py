#!/usr/bin/env python3
"""Standing check for Review Reply Desk trial prospects (Quality Gate step 5, trials 2-3).

A trial needs a real gap: a review under 5 stars, from the last 12 months, with no owner
response. This check reads the prospect table in trial-prospects.md and fails any row whose
STATUS claims more than its evidence shows. It exists because the cloud can read Birdeye's
copies of Google reviews but not always the stars or the owner replies, and "not in the
extracted text" is not the same as "no reply".

Columns (markdown table, in this order):
  ID | Business | Health | Source URL | Page name, city | Read (UTC) | Reviews / avg |
  Under-5 stars | Under-5 age (months) | Owner response | Status

The file also states the prospects' city on one line: **Prospect city:** Flagstaff, AZ

Values:
  Health          yes / no   (yes = clinic: no review text may be quoted in the row, and
                              replies must never confirm the reviewer was a patient)
  Under-5 stars   1-4 (seen on the page) / unknown / none
  Owner response  none-rendered (looked at the rendered page, no reply) / not-in-text /
                  yes / -
  Page name, city the name and city the source page shows, as "Name, City ST";
                  "unrecorded" only on rows read before Nov 23 14:25 UTC; "-" when not read
  Status          ELIGIBLE / NEEDS-BROWSER / NO-GAP / WRONG-PAGE / NOT-READ

Rules:
  1. ELIGIBLE needs stars 1-4, age <= 12, Owner response = none-rendered, a source URL and
     a read time. Anything weaker is NEEDS-BROWSER at best.
  2. NO-GAP needs evidence that agrees with itself (Atlas, PR #55):
       - a shown average below 5.0 proves an under-5 review exists, so it is never NO-GAP;
       - Under-5 stars = none is enough on its own;
       - an average of 5.0 alone is enough only under 20 reviews (at 21+, one 4-star
         review still displays as 5.0: 20x5 + 1x4 = 104/21 = 4.95).
  3. NOT-READ rows carry no source URL, read time or findings.
  4. A row read from a source has an http(s) URL and a read time (YYYY-MM-DD HH:MM).
  5. Health = yes rows quote no review text (no double, curly or paired single quotes).
  6. A site search can return a different business with a similar name (Nov 23: "Cedar
     Health" in Tucson for Cedar Health Center, Flagstaff). So the page must be the
     prospect: its city must be the prospect city, and its name must hold every key word
     of the business name or the other way round, with at least one shared word that
     isn't a generic practice word (health, center, clinic, ...). ELIGIBLE needs that
     match recorded.
     NEEDS-BROWSER and NO-GAP need it too, except legacy "unrecorded" rows read before
     2026-11-23 14:25 UTC. A page that
     fails the match is WRONG-PAGE, and WRONG-PAGE must actually fail it.

Usage:  python3 review_gap_check.py [trial-prospects.md]
        python3 review_gap_check.py --self-test
Exit 0 = every row's status is supported; 1 = at least one ERROR.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
STATUSES = {"ELIGIBLE", "NEEDS-BROWSER", "NO-GAP", "WRONG-PAGE", "NOT-READ"}
RESPONSES = {"none-rendered", "not-in-text", "yes", "-"}
TIME = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$")
NCOLS = 11
# Words that don't identify a business: legal forms, titles, filler.
SOFT = {"the", "of", "and", "pllc", "llc", "inc", "pc", "dr", "nmd", "lac", "md", "dc", "do"}
# Practice words many businesses share. A match needs at least one word outside this set
# (Atlas, PR #56: "Health Center, Flagstaff AZ" must not pass as Cedar Health Center).
GENERIC = {"health", "healthcare", "center", "centre", "clinic", "medical", "medicine",
           "care", "wellness", "family", "practice"}
# "unrecorded" is only for rows read before the page column existed (Atlas, PR #56).
LEGACY_CUTOFF = "2026-11-23 14:25"


def keywords(name):
    return {w for w in re.findall(r"[a-z0-9]+", name.lower()) if w not in SOFT}


def city_key(city):
    return re.sub(r"[^a-z]", "", city.lower())


def page_match(biz, page, prospect_city):
    """Return (True, '') if the page is the prospect, else (False, reason)."""
    if "," not in page:
        return False, "page cell must be 'Name, City ST'"
    name, city = page.rsplit(",", 1)
    if not prospect_city:
        return False, "file has no '**Prospect city:**' line"
    if city_key(city) != city_key(prospect_city):
        return False, f"page city '{city.strip()}' is not the prospect city '{prospect_city}'"
    a, b = keywords(re.sub(r"\(.*?\)", " ", biz)) or keywords(biz), keywords(name)
    full = keywords(biz)
    if not b or not ((b <= full and len(b) >= min(2, len(a))) or a <= b):
        return False, f"page name '{name.strip()}' does not match '{biz}'"
    if not (b & full) - GENERIC:
        return False, f"page name '{name.strip()}' shares only generic practice words with '{biz}'"
    return True, ""


def rows(text):
    out = []
    for line in text.splitlines():
        if not re.match(r"^\|\s*P\d{3}\s*\|", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        out.append((line, cells))
    return out


def check_row(line, c, prospect_city="Flagstaff, AZ"):
    errs = []
    if len(c) != NCOLS:
        return [f"{c[0]}: expected {NCOLS} columns, got {len(c)}"]
    pid, biz, health, url, page, read, cnt, stars, age, resp, status = c
    tag = f"{pid} {biz}"
    if status not in STATUSES:
        errs.append(f"{tag}: unknown status '{status}'")
    if resp not in RESPONSES:
        errs.append(f"{tag}: Owner response must be one of {sorted(RESPONSES)}")
    if health not in ("yes", "no"):
        errs.append(f"{tag}: Health must be yes or no")
    if status == "NOT-READ":
        if any(v not in ("-", "") for v in (url, page, read, cnt, stars, age)) or resp != "-":
            errs.append(f"{tag}: NOT-READ row carries findings; give it a status that matches")
        return errs
    if not re.match(r"^https?://\S+$", url):
        errs.append(f"{tag}: read rows need the source URL")
    if not TIME.match(read):
        errs.append(f"{tag}: read rows need a read time 'YYYY-MM-DD HH:MM'")
    if health == "yes" and re.search(r"[\"“”‘’]|'[^'|]{3,}'", line):
        errs.append(f"{tag}: health business row quotes review text; keep patient words out of the public repo")
    if page == "unrecorded":
        if status not in ("NEEDS-BROWSER", "NO-GAP"):
            errs.append(f"{tag}: {status} needs the page's name and city recorded, not 'unrecorded'")
        if TIME.match(read) and read > LEGACY_CUTOFF:
            errs.append(f"{tag}: 'unrecorded' is only for rows read before {LEGACY_CUTOFF} UTC; record the page's name and city")
    else:
        ok, why = page_match(biz, page, prospect_city)
        if status == "WRONG-PAGE" and ok:
            errs.append(f"{tag}: WRONG-PAGE but the page matches the prospect; give it a real status")
        if status != "WRONG-PAGE" and not ok:
            errs.append(f"{tag}: {why}; mark it WRONG-PAGE")
    if status == "ELIGIBLE":
        if stars not in ("1", "2", "3", "4"):
            errs.append(f"{tag}: ELIGIBLE needs the under-5 star count seen on the page (got '{stars}')")
        if not age.isdigit() or int(age) > 12:
            errs.append(f"{tag}: ELIGIBLE needs an under-5 review from the last 12 months (got '{age}')")
        if resp != "none-rendered":
            errs.append(f"{tag}: ELIGIBLE needs 'none-rendered' (a rendered look); '{resp}' is not proof of no reply")
    if status == "NO-GAP":
        m = re.match(r"^\s*(\d+)\s*/\s*(\d(?:\.\d+)?)\s*$", cnt)
        n, avg = (int(m.group(1)), float(m.group(2))) if m else (None, None)
        if avg is not None and avg < 5.0:
            errs.append(f"{tag}: NO-GAP contradicts a {avg} average, which proves an under-5 review exists")
        elif stars != "none" and not (avg == 5.0 and n < 20):
            errs.append(f"{tag}: NO-GAP needs Under-5 stars = none, or a 5.0 average on under 20 reviews (one 4-star hides in a 5.0 at 21+)")
    return errs


def run(path):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"\*\*Prospect city:\*\*\s*(.+)", text)
    city = m.group(1).strip() if m else ""
    rs = rows(text)
    errs = [e for line, c in rs for e in check_row(line, c, city)]
    counts = {s: sum(1 for _, c in rs if len(c) == NCOLS and c[-1] == s) for s in sorted(STATUSES)}
    for e in errs:
        print("ERROR", e)
    print(f"SUMMARY rows={len(rs)} errors={len(errs)} " + " ".join(f"{k}={v}" for k, v in counts.items()))
    return 1 if errs or not rs else 0


def self_test():
    U = "https://reviews.birdeye.com/x"
    T = "2026-11-23 13:40"
    PG = "A, Flagstaff AZ"
    cases = [
        ("good eligible", ["P001", "A", "no", U, PG, T, "20 / 4.5", "3", "2", "none-rendered", "ELIGIBLE"], 0),
        ("eligible on unknown stars", ["P001", "A", "no", U, PG, T, "20 / 4.5", "unknown", "2", "none-rendered", "ELIGIBLE"], 1),
        ("eligible on not-in-text", ["P001", "A", "no", U, PG, T, "20 / 4.5", "3", "2", "not-in-text", "ELIGIBLE"], 1),
        ("eligible but old review", ["P001", "A", "no", U, PG, T, "20 / 4.5", "3", "30", "none-rendered", "ELIGIBLE"], 1),
        ("needs-browser is fine", ["P001", "A", "yes", U, PG, T, "23 / 4.5", "unknown", "-", "not-in-text", "NEEDS-BROWSER"], 0),
        ("no-gap by 5.0 avg", ["P001", "A", "yes", U, PG, T, "5 / 5.0", "none", "-", "not-in-text", "NO-GAP"], 0),
        ("no-gap without evidence", ["P001", "A", "no", U, PG, T, "55 / 4.6", "unknown", "-", "not-in-text", "NO-GAP"], 1),
        ("health row quotes a patient", ["P001", "A \"loved my treatment\"", "yes", U, PG, T, "5 / 5.0", "none", "-", "-", "NO-GAP"], 1),
        ("read row with no URL", ["P001", "A", "no", "-", PG, T, "20 / 4.5", "unknown", "-", "not-in-text", "NEEDS-BROWSER"], 1),
        ("read row with no time", ["P001", "A", "no", U, PG, "today", "20 / 4.5", "unknown", "-", "not-in-text", "NEEDS-BROWSER"], 1),
        ("not-read is fine", ["P001", "A", "yes", "-", "-", "-", "-", "-", "-", "-", "NOT-READ"], 0),
        ("not-read with findings", ["P001", "A", "yes", U, "-", "-", "-", "3", "-", "-", "NOT-READ"], 1),
        ("not-read with a count and read time", ["P001", "A", "yes", "-", "-", T, "16 / 4.9", "-", "-", "-", "NOT-READ"], 1),
        ("no-gap: stars none vs 4.6 avg (Atlas)", ["P001", "A", "no", U, PG, T, "55 / 4.6", "none", "-", "not-in-text", "NO-GAP"], 1),
        ("no-gap: 5.0 avg alone at 25 reviews (Atlas)", ["P001", "A", "no", U, PG, T, "25 / 5.0", "unknown", "-", "not-in-text", "NO-GAP"], 1),
        ("no-gap: 5.0 avg alone at 16 reviews", ["P001", "A", "no", U, PG, T, "16 / 5.0", "unknown", "-", "not-in-text", "NO-GAP"], 0),
        ("no-gap: stars none at 25 / 5.0", ["P001", "A", "no", U, PG, T, "25 / 5.0", "none", "-", "not-in-text", "NO-GAP"], 0),
        ("health row single-quotes a patient", ["P001", "A 'loved my treatment'", "yes", U, PG, T, "5 / 5.0", "none", "-", "-", "NO-GAP"], 1),
        ("health row with an apostrophe in the name", ["P001", "Kovalik's Clinic", "yes", U, "Kovalik's Clinic, Flagstaff AZ", T, "5 / 5.0", "none", "-", "-", "NO-GAP"], 0),
        ("unrecorded on a fresh read (Atlas)", ["P001", "A", "yes", U, "unrecorded", "2026-11-23 15:35", "23 / 4.5", "unknown", "-", "not-in-text", "NEEDS-BROWSER"], 1),
        ("only generic words shared (Atlas)", ["P006", "Cedar Health Center", "yes", U, "Health Center, Flagstaff AZ", T, "7 / 4.4", "unknown", "-", "not-in-text", "NEEDS-BROWSER"], 1),
        ("generic-only page marked wrong-page", ["P006", "Cedar Health Center", "yes", U, "Health Center, Flagstaff AZ", T, "7 / 4.4", "unknown", "-", "not-in-text", "WRONG-PAGE"], 0),
        ("distinctive word shared", ["P009", "The Vitality Doctor (Dr Christina Kovalik NMD, LAc)", "yes", U, "The Vitality Doctor Dr Christina Kovalik NMD LAc, Flagstaff AZ", T, "23 / 4.5", "unknown", "-", "not-in-text", "NEEDS-BROWSER"], 0),
        ("bad status word", ["P001", "A", "no", U, PG, T, "20 / 4.5", "3", "2", "none-rendered", "READY"], 1),
        ("legacy unrecorded needs-browser", ["P001", "A", "yes", U, "unrecorded", T, "23 / 4.5", "unknown", "-", "not-in-text", "NEEDS-BROWSER"], 0),
        ("legacy unrecorded cannot be eligible", ["P001", "A", "no", U, "unrecorded", T, "20 / 4.5", "3", "2", "none-rendered", "ELIGIBLE"], 1),
        ("same name, other city", ["P006", "Cedar Health Center", "yes", U, "Cedar Health, Tucson AZ", T, "7 / 4.4", "unknown", "-", "not-in-text", "NEEDS-BROWSER"], 1),
        ("other city marked wrong-page", ["P006", "Cedar Health Center", "yes", U, "Cedar Health, Tucson AZ", T, "7 / 4.4", "unknown", "-", "not-in-text", "WRONG-PAGE"], 0),
        ("other practice, same surname", ["P007", "Munderloh Integrated Medical", "yes", U, "Munderloh Chiropractic, Flagstaff AZ", T, "197 / 4.8", "unknown", "-", "not-in-text", "NEEDS-BROWSER"], 1),
        ("wrong-page that matches", ["P008", "Synergistic Healthcare PLLC", "yes", U, "Synergistic Healthcare, Flagstaff AZ", T, "16 / 5.0", "none", "-", "not-in-text", "WRONG-PAGE"], 1),
        ("reordered name with person", ["P010", "Acupuncture Wellness Center (Cynthia Hull)", "yes", U, "Hull Cynthia-Acupuncture Wellness Center, Flagstaff AZ", T, "5 / 5.0", "none", "-", "not-in-text", "NO-GAP"], 0),
        ("one generic word is no match", ["P008", "Synergistic Healthcare PLLC", "yes", U, "Healthcare, Flagstaff AZ", T, "16 / 5.0", "none", "-", "not-in-text", "NO-GAP"], 1),
        ("page cell without a city", ["P008", "Synergistic Healthcare PLLC", "yes", U, "Synergistic Healthcare", T, "16 / 5.0", "none", "-", "not-in-text", "NO-GAP"], 1),
    ]
    ok = 0
    for name, c, bad in cases:
        line = "| " + " | ".join(c) + " |"
        got = 1 if check_row(line, c) else 0
        ok += got == bad
        print(("PASS" if got == bad else "FAIL"), name)
    print(f"self-test {ok}/{len(cases)}")
    return 0 if ok == len(cases) else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    sys.exit(run(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "trial-prospects.md")))
