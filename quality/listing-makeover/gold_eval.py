#!/usr/bin/env python3
"""Listing Makeover gate step 3 prep: run the eval set's code rules on the REAL gold sample.

The eval set (Gravity-Studio PR #52, portfolio/listing-makeover/evals/check_listings.py) was
proven on 8 synthetic cases. This runs the same check() on the 12 real Davias Helix listings,
with the seller's own intake as the source of truth:

  intake  = davias HELIX_COLLECTION.md @ 005b877 (stones, construction, matching, notes) and
            README.md (maker names), copied verbatim into helix-intake.json
  facts   = each listing's Mohs values, allowed only because mohs_check.py SOURCES sourced them

So "no invented numbers" here means: every number in a listing is either the seller's or a
sourced Mohs value. It adds one rule the synthetic set did not have:

  TREATMENT: a listing that says "Every stone is natural" while naming a stone that is usually
  treated (citrine: heated; onyx: dyed; carnelian: heated) must carry a note or [question] about THAT stone. Source for citrine:
  GIA, gia.edu/citrine-description ("Since natural citrine is rare, most of the citrine on the
  market is the result of heat treatment"), opened 2026-11-22. FTC: sellers should disclose a
  treatment "if it significantly affects the value of the gemstone" (ftc.gov "Loupe" guidance
  on the Jewelry Guides, opened 2026-11-22).

  python3 gold_eval.py gold-sample-listings.md [--gs ../../../gravity-studio]   # exit 1 on any FAIL
  python3 gold_eval.py --test
Offline, standard library only. Never posts anything.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mohs_check  # noqa: E402

# Stones a seller must answer for before "natural" stands alone. Only stones with an opened
# source are listed. Each entry: (what is usually done to it, source).
TREATED = {
    "citrine": ("heat-treated", "GIA citrine-description: 'most of the citrine on the market is the result of heat treatment'"),
    "onyx": ("dyed", "gemsociety.org black-onyx article (opened 2026-11-22): 'Most solid black pieces sold today is actually "
                     "dyed black chalcedony'; GIA (Atlas, browser, PR #33): 'What many call \u2018black onyx\u2019 is actually dyed black chalcedony'"),
    "carnelian": ("heat-treated", "gemsociety.org carnelian article (opened 2026-11-23): 'You should assume, unless informed otherwise, "
                                  "that any piece of carnelian has been enhanced in this way' (heating); property table 'Typical Treatments: Heat Treatment'"),
}
NATURAL_LINE = re.compile(r"every stone is natural", re.I)
TREAT_WORD = r"(treat|heat|dye|natural|untreated)"


def has_note(block, stone):
    """The answer must be about THIS stone: a line naming it with a treatment word, or a [question] naming it."""
    st = re.escape(stone)
    bracket = re.compile(r"\[[^\]]*" + st + r"[^\]]*" + TREAT_WORD + r"[^\]]*\]|\[[^\]]*" + TREAT_WORD + r"[^\]]*" + st + r"[^\]]*\]", re.I)
    if bracket.search(block):
        return True
    for line in block.splitlines():
        if re.search(st, line, re.I) and re.search(r"(heat[- ]?treated|dyed|treated|untreated)", line, re.I):
            return True
    return False


def load_check_listings(gs_root):
    evals = os.path.join(gs_root, "portfolio", "listing-makeover", "evals")
    if not os.path.exists(os.path.join(evals, "check_listings.py")):
        sys.exit(f"check_listings.py not found under {evals} - check out Gravity-Studio PR #52 "
                 "(branch claude/listing-makeover-evals) beside this repo, or pass --gs")
    sys.path.insert(0, evals)
    import check_listings  # noqa: E402
    return check_listings


def mohs_facts(stones):
    out = []
    for s in stones:
        lo, hi, src, _open = mohs_check.SOURCES[s.lower()]
        # the sourced range ends, plus any value quoted from an opened page (USGS lapis '5-5.5')
        quoted = [x for x in re.findall(r"\d+(?:\.\d+)?", src) if lo <= float(x) <= hi]
        out += [f"{lo:g}", f"{hi:g}"] + quoted
    return out


def treatment_errors(block, stones):
    errs = []
    if not NATURAL_LINE.search(block):
        return errs
    for s in stones:
        hit = TREATED.get(s.lower())
        if hit and not has_note(block, s):
            how, why = hit
            errs.append(f"says 'Every stone is natural' but {s} is usually {how} ({why}); "
                        f"needs the seller's answer or a [{s}: natural or {how}?] question")
    return errs


def case_for(entry, notes):
    return {
        "id": entry["name"], "platform": "etsy", "lore": True,
        "intake": entry["text"] + " " + notes,
        "facts": mohs_facts(entry["stones"]),
        "must_mention_any": entry["stones"],
        "must_not_mention": ["sterling", "925", "gold-filled", "14k", "hypoallergenic", "heals",
                             "cures", "anxiety", "only 1 left", "limited stock", "certified"],
        "expect_placeholder": "size",
    }


def run(listing_path, gs_root, intake_path=os.path.join(HERE, "helix-intake.json")):
    cl = load_check_listings(gs_root)
    with open(intake_path, encoding="utf-8") as f:
        intake = json.load(f)
    with open(listing_path, encoding="utf-8") as f:
        text = f.read()
    norm = lambda n: n.replace("\u2019", "'")
    blocks = {norm(n): b for n, b in cl.listing_lint.parse(text)}
    fails = 0
    for entry in intake["designs"]:
        block = blocks.get(norm(entry["name"]))
        if block is None:
            print(f"FAIL {entry['name']}: no listing in {listing_path}")
            fails += 1
            continue
        errs = cl.check(case_for(entry, intake["notes"]), block) + treatment_errors(block, entry["stones"])
        fails += bool(errs)
        print(("FAIL " if errs else "PASS ") + entry["name"] + ("" if not errs else ": " + "; ".join(errs)))
    n = len(intake["designs"])
    print(f"\n{n - fails}/{n} real listings pass the eval set's code rules + treatment rule")
    return 1 if fails else 0


def self_test():
    ok_block = "Citrine & Aventurine.\nEvery stone is natural. [Citrine: natural or heat-treated? ask the maker]\n"
    bad_block = "Citrine & Aventurine.\nEvery stone is natural, so color varies.\n"
    both_bad = "Tiger's Eye & Onyx.\nEvery stone is natural.\n"
    cases = [
        ("citrine + 'every stone is natural' with no note fails", len(treatment_errors(bad_block, ["Citrine"])) == 1),
        ("citrine with a [placeholder] question passes", treatment_errors(ok_block, ["Citrine"]) == []),
        ("citrine with 'heat-treated' stated passes",
         treatment_errors("Every stone is natural. Citrine (heat-treated amethyst).", ["Citrine"]) == []),
        ("amethyst alone passes (not on the treated list)", treatment_errors(bad_block, ["Amethyst"]) == []),
        ("no 'natural' line, no rule", treatment_errors("Citrine bead.", ["Citrine"]) == []),
        ("onyx + 'every stone is natural' fails (Atlas, PR #33)", len(treatment_errors(both_bad, ["Tiger's Eye", "Onyx"])) == 1),
        ("onyx stated as dyed passes", treatment_errors("Every stone is natural.\n- Onyx: dyed black chalcedony.", ["Onyx"]) == []),
        ("a citrine note does not clear onyx", len(treatment_errors(
            "Every stone is natural.\n- Citrine: heat-treated amethyst.\n- Onyx: black.", ["Citrine", "Onyx"])) == 1),
        ("carnelian + 'every stone is natural' fails (gemsociety, Nov 23)",
         len(treatment_errors("Every stone is natural.", ["Carnelian", "Clear Quartz"])) == 1),
        ("carnelian with a [question] passes",
         treatment_errors("Every stone is natural. [Carnelian: natural color or heat-treated? ask the maker]", ["Carnelian"]) == []),
        ("Mohs facts come from mohs_check SOURCES", {"5", "5.5"} <= set(mohs_facts(["Obsidian"]))),
        ("a value quoted from an opened page counts (USGS lapis 5-5.5)", "5.5" in mohs_facts(["Lapis Lazuli"])),
        ("a value outside the sourced range never counts", "8" not in mohs_facts(["Amethyst"])),
    ]
    bad = sum(not ok for _, ok in cases)
    for label, ok in cases:
        print(("PASS " if ok else "FAIL ") + label)
    print(f"\nself-test {len(cases) - bad}/{len(cases)}")
    return 1 if bad else 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["--test"]:
        sys.exit(self_test())
    gs = os.path.join(HERE, "..", "..", "..", "gravity-studio")
    if "--gs" in args:
        i = args.index("--gs")
        gs = args[i + 1]
        del args[i:i + 2]
    if len(args) != 1:
        print(__doc__)
        sys.exit(2)
    sys.exit(run(args[0], gs))
