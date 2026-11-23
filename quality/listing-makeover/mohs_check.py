#!/usr/bin/env python3
"""Listing Makeover gold sample: every hardness number must match an opened source.

Scorecard row 1 (Accuracy) says "every fact true and sourced". The Davias Helix listings
print a Mohs hardness for each stone under *Proven*, so a wrong number there is a false
"proven" fact on a live shop. This check reads every "**Stone** — ... Mohs X" line and
compares X with SOURCES below (each value copied from a page opened on 2026-11-22).

  python3 mohs_check.py gold-sample-listings.md   # exit 1 on any mismatch or unsourced stone
  python3 mohs_check.py --test

Rules:
  - the stone must be in SOURCES, else FAIL "unsourced"
  - the listing's range must sit inside the sourced range (a "~" value counts as that number)
  - stones marked open=True print OPEN (sources disagree; Atlas re-checks in a browser) but don't fail
Offline, standard library only.
"""
import re
import sys

GEO_AV = "geology.com/gemstones/aventurine ('6.5 to 7'); minerals.net/gemstone/aventurine ('6.5–7')"
IGS = "gemsociety.org/article/select-gems-ordered-mohs-hardness"
USGS = "pubs.usgs.gov/gip/gemstones/mineral.html"

# stone: (low, high, source, open)
SOURCES = {
    "amethyst": (7, 7, f"{IGS} ('Amethyst | 7'); {USGS} (quartz 7)", False),
    "clear quartz": (7, 7, f"{IGS} ('Quartz | 7'); {USGS} ('Quartz (hardness: 7 Mohs)')", False),
    "rose quartz": (7, 7, f"{USGS} (quartz 7, 'Rose quartz' listed as a variety)", False),
    "citrine": (7, 7, f"{IGS} ('Citrine | 7')", False),
    "smoky quartz": (7, 7, f"{IGS} ('Smoky Quartz | 7')", False),
    "tiger's eye": (6.5, 7, "en.wikipedia.org/wiki/Tiger's_eye (infobox: Mohs 6.5-7, opened 2026-11-22); geology.com classes tiger's eye as a quartz gemstone, hardness 7", False),
    "onyx": (6.5, 7, f"{IGS} ('Chalcedony | 6½ - 7'); onyx is a chalcedony/agate type ({USGS})", False),
    "carnelian": (6.5, 7, f"{IGS} ('Chalcedony | 6½ - 7'); carnelian listed under agate ({USGS})", False),
    "pink tourmaline": (7, 7.5, f"{USGS} ('Tourmaline (hardness: 7-7.5 Mohs)')", False),
    "black tourmaline": (7, 7.5, f"{USGS} ('Tourmaline (hardness: 7-7.5 Mohs)')", False),
    "amazonite": (6, 6.5, f"{IGS} ('Amazonite | 6 - 6½'); {USGS} (feldspar 6-6.5)", False),
    "labradorite": (6, 6.5, f"{IGS} ('Labradorite | 6 - 6½'); {USGS} (feldspar 6-6.5)", False),
    "moonstone": (6, 6.5, f"{USGS} ('Feldspar (hardness: 6-6.5 Mohs)', Moonstone listed under it)", False),
    "aquamarine": (7.5, 8, f"{IGS} ('Aquamarine | 7½ - 8'); {USGS} ('Beryl (hardness: 7.5-8 Mohs)')", False),
    "green aventurine": (6.5, 7, GEO_AV, False),
    "amber": (2, 2.5, "gia.edu/amber ('Mohs Hardness: 2.0 to 2.5'); pubs.usgs.gov/gip/gemstones/organic.html ('2-2.5')", False),
    "lapis lazuli": (5, 6, f"{USGS} ('5-5.5'); {IGS} ('Lapis Lazuli | 5 - 6')", False),
    "fluorite": (4, 4, "britannica.com/science/Mohs-hardness (table: 'fluorite | 4'), opened by Atlas 2026-11-23 (PR #47); the scale's own reference mineral for 4", False),
    "obsidian": (5, 5.5, "igi.org/all-about-colored-stones-obsidian ('obsidian sits at around 5-5.5', Mark Reyes G.G., IGI, opened 2026-11-22); firemountaingems.com golden sheen obsidian ('Hardness: 5 to 5-1/2')", False),
}

LINE = re.compile(r"^- \*\*(?P<stone>[^*]+)\*\*.*?Mohs (?P<val>~?\d+(?:\.\d+)?(?:\s*[–-]\s*\d+(?:\.\d+)?)?)", re.M)


def parse_range(val):
    nums = [float(x) for x in re.findall(r"\d+(?:\.\d+)?", val)]
    return nums[0], nums[-1]


def check_text(text):
    """Return (fails, opens, checked) lists of strings."""
    fails, opens, seen = [], [], {}
    for m in LINE.finditer(text):
        stone, val = m.group("stone").strip(), m.group("val")
        key = stone.lower()
        if key in seen:
            if seen[key] != val:
                fails.append(f"{stone}: two different values in one file ({seen[key]} vs {val})")
            continue
        seen[key] = val
        if key not in SOURCES:
            fails.append(f"{stone}: Mohs {val} has no opened source in SOURCES")
            continue
        lo, hi, src, is_open = SOURCES[key]
        a, b = parse_range(val)
        if not (lo <= a <= b <= hi):
            fails.append(f"{stone}: listing says Mohs {val}, source says {lo:g}–{hi:g} — {src}")
        elif is_open:
            opens.append(f"{stone}: Mohs {val} fits {lo:g}–{hi:g} but sources are thin — {src}")
    return fails, opens, sorted(seen)


def report(path):
    with open(path, encoding="utf-8") as f:
        fails, opens, seen = check_text(f.read())
    for s in fails:
        print("FAIL " + s)
    for s in opens:
        print("OPEN " + s)
    print(f"\n{len(seen) - len(fails)}/{len(seen)} stones match an opened source"
          + (f", {len(opens)} open for Atlas" if opens else ""))
    return 1 if fails or not seen else 0


def self_test():
    good = "- **Green Aventurine** — *Proven:* quartz, Mohs 6.5–7.\n- **Amber** — *Proven:* resin (Mohs 2–2.5)\n"
    cases = [
        ("sourced ranges pass", check_text(good)[0] == []),
        ("old '~6.5' aventurine passes as 6.5 (inside 6.5–7)",
         check_text("- **Green Aventurine** — Mohs ~6.5.")[0] == []),
        ("aventurine 6–6.5 fails (6 is below the source)",
         len(check_text("- **Green Aventurine** — Mohs 6–6.5.")[0]) == 1),
        ("unsourced stone fails", "no opened source" in " ".join(check_text("- **Jade** — Mohs 6.")[0])),
        ("quartz 8 fails", len(check_text("- **Citrine** — yellow quartz, Mohs 8.")[0]) == 1),
        ("same stone, two values fails",
         len(check_text("- **Amethyst** — Mohs 7.\n- **Amethyst** — Mohs 7.5.\n")[0]) == 1),
        ("obsidian 5–5.5 passes, no longer OPEN (IGI, Atlas 2026-11-22)", check_text("- **Obsidian** — glass; Mohs 5–5.5.") == ([], [], ["obsidian"])),
        ("hyphen and en dash both parse", parse_range("6-6.5") == parse_range("6–6.5") == (6.0, 6.5)),
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
    if len(args) != 1:
        print(__doc__)
        sys.exit(2)
    sys.exit(report(args[0]))
