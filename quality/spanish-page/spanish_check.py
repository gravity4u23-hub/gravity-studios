#!/usr/bin/env python3
"""spanish_check.py — checks a Spanish version against the buyer's English original.

Built from the Spanish page benchmark (benchmark.md). Buyers' #1 complaint about
paid translation is machine output passed off as human work, then wrong terms,
missing pieces and broken formatting. A script can't judge how natural the Spanish
reads (a fluent person must), but it can block the mistakes that cost a small
business money or trust:

  1. Numbers: every price, size, time and phone number in the original appears
     unchanged in the Spanish (a menu with a wrong price is worse than no menu).
  2. Structure: same number of non-empty lines, so no dish or service is dropped.
  3. Leftover English: a Spanish line that is still mostly English words.
  4. Allergens: if the original names a common allergen, the Spanish names it too.
  5. Delivery note (when given): says AI-assisted drafting up front, names who
     reviewed it, and lists the terms the buyer should confirm.

Usage:
  python3 spanish_check.py ORIGINAL.txt SPANISH.txt [DELIVERY_NOTE.txt]
  python3 spanish_check.py --test
Exit 0 = pass, 1 = fail.
"""
import re, sys

NUM = re.compile(r"\d[\d,.:]*\d|\d")

# English allergen word -> accepted Spanish words (any one is enough)
ALLERGENS = {
    "peanut": ["cacahuate", "cacahuete", "maní", "mani"],
    "tree nut": ["frutos secos", "nueces"],
    "walnut": ["nuez", "nueces"],
    "almond": ["almendra"],
    "pecan": ["nuez pecana", "pecana"],
    "shellfish": ["mariscos", "marisco"],
    "shrimp": ["camarón", "camarones", "camaron", "gamba"],
    "crab": ["cangrejo", "jaiba"],
    "fish": ["pescado"],
    "egg": ["huevo"],
    "milk": ["leche", "lácteo", "lacteo"],
    "dairy": ["lácteo", "lacteo", "leche"],
    "cheese": ["queso"],
    "wheat": ["trigo"],
    "gluten": ["gluten"],
    "soy": ["soya", "soja"],
    "sesame": ["ajonjolí", "ajonjoli", "sésamo", "sesamo"],
}

EN_COMMON = set("""the and with of our your for from served topped choice add each
side sides fresh made house daily with or on in to all any one two three get free
only per extra large small call book today open closed hours we you is are
onion onions corn beans rice chicken beef pork sauce lime black green red
grilled fried tortillas cup bowl plate drink drinks appointment service""".split())

DISCLOSE = re.compile(r"\bai[- ]assisted\b|\bdrafted with ai\b|\bai\b.*\bdraft", re.I)
REVIEWER = re.compile(r"reviewed by|revisado por", re.I)
CONFIRM = re.compile(r"terms? to confirm|t[eé]rminos (para|a) confirmar|please confirm", re.I)


def lines(text):
    return [l.strip() for l in text.splitlines() if l.strip()]


def nums(text):
    return sorted(n.rstrip(".,:") for n in NUM.findall(text))


def check(original, spanish, note=None):
    errors, warnings = [], []
    src, dst = nums(original), nums(spanish)
    missing = [n for n in set(src) if dst.count(n) < src.count(n)]
    extra = [n for n in set(dst) if src.count(n) < dst.count(n)]
    if missing:
        errors.append("numbers changed or dropped: " + ", ".join(sorted(missing)))
    if extra:
        errors.append("numbers not in the original: " + ", ".join(sorted(extra)))

    lo, ls = lines(original), lines(spanish)
    if len(lo) != len(ls):
        errors.append(f"line count {len(ls)} != original {len(lo)} (dropped or merged items?)")

    for i, line in enumerate(ls, 1):
        words = re.findall(r"[a-záéíóúñü]+", line.lower())
        if len(words) >= 4:
            share = sum(w in EN_COMMON for w in words) / len(words)
            if share >= 0.34:
                errors.append(f"line {i} still reads as English: {line!r}")

    low_o, low_s = original.lower(), spanish.lower()
    for en, es in ALLERGENS.items():
        if re.search(r"\b" + en + r"(e?s)?\b", low_o) and not any(w in low_s for w in es):
            errors.append(f"allergen '{en}' in the original but not in the Spanish")

    if note is not None:
        if not DISCLOSE.search(note):
            errors.append("delivery note does not say AI-assisted drafting")
        if not REVIEWER.search(note):
            errors.append("delivery note does not say who reviewed the Spanish")
        if not CONFIRM.search(note):
            errors.append("delivery note has no 'terms to confirm' list")
    return errors, warnings


ORIG = """House Tacos - $12.50
Three corn tortillas with carne asada, onion and cilantro.
Shrimp Bowl - $14
Rice, black beans, shrimp, avocado and lime. Contains shellfish.
Peanut Brittle - $4
Open daily 11:00 to 21:00. Call (928) 555-0142."""

GOOD = """Tacos de la casa - $12.50
Tres tortillas de maíz con carne asada, cebolla y cilantro.
Bowl de camarones - $14
Arroz, frijoles negros, camarones, aguacate y limón. Contiene mariscos.
Dulce de cacahuate - $4
Abierto todos los días de 11:00 a 21:00. Llame al (928) 555-0142."""

NOTE = """Drafting was AI-assisted; every line was reviewed by [reviewer name].
Terms to confirm: "Bowl" (kept in English, common in Arizona menus), "Dulce de cacahuate"."""


def _test():
    cases = [
        ("gold passes", ORIG, GOOD, NOTE, True),
        ("wrong price", ORIG, GOOD.replace("$12.50", "$12.00"), NOTE, False),
        ("phone digit typo", ORIG, GOOD.replace("555-0142", "555-0124"), NOTE, False),
        ("dropped dish line", ORIG, GOOD.replace("Dulce de cacahuate - $4\n", ""), NOTE, False),
        ("dropped description line", ORIG, GOOD.replace(
            "Tres tortillas de maíz con carne asada, cebolla y cilantro.\n", ""), NOTE, False),
        ("allergen dropped", ORIG, GOOD.replace(" Contiene mariscos.", ""), NOTE, False),
        ("peanut not named", ORIG, GOOD.replace("Dulce de cacahuate", "Dulce crujiente").replace(
            '"Dulce de cacahuate"', '"Dulce crujiente"'), NOTE, False),
        ("line left in English", ORIG, GOOD.replace(
            "Tres tortillas de maíz con carne asada, cebolla y cilantro.",
            "Three corn tortillas with carne asada, onion and cilantro."), NOTE, False),
        ("no AI disclosure", ORIG, GOOD, NOTE.replace("Drafting was AI-assisted; e", "E"), False),
        ("no reviewer named", ORIG, GOOD, NOTE.replace("reviewed by [reviewer name]", "checked"), False),
        ("no terms to confirm", ORIG, GOOD, NOTE.split("\n")[0], False),
        ("no note given = text checks only", ORIG, GOOD, None, True),
    ]
    ok = 0
    for name, o, s, n, want in cases:
        errs, _ = check(o, s, n)
        got = not errs
        mark = "ok " if got == want else "BAD"
        ok += got == want
        print(f"{mark} {name}: {'pass' if got else 'fail'}" + ("" if got else f" ({errs[0]})"))
    print(f"self-tests {ok}/{len(cases)}")
    return ok == len(cases)


def main(argv):
    if argv[1:2] == ["--test"]:
        return 0 if _test() else 1
    if len(argv) not in (3, 4):
        print(__doc__)
        return 2
    read = lambda p: open(p, encoding="utf-8").read()
    errs, warns = check(read(argv[1]), read(argv[2]), read(argv[3]) if len(argv) == 4 else None)
    for e in errs:
        print("ERROR", e)
    for w in warns:
        print("WARN ", w)
    print("PASS" if not errs else f"FAIL ({len(errs)} errors)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
