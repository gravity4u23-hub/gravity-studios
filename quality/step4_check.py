"""Checks quality/STEP4_READS.md, the owner's one-page step-4 reads.

Each "## Read N" card must have: a "Would ..." question with a $ price, an
"**Issue:** #N" line, at least one "**Source:**" file that exists, a
"**Recommendation:**" line, and at least one quoted ("> ") line. Every quoted
line must appear word for word in one of that card's source files, so the
owner never reads a line the sample doesn't contain.

Run:  python3 step4_check.py            (checks STEP4_READS.md)
      python3 step4_check.py --self-test
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def cards(text):
    parts = re.split(r"^## (Read \d+[^\n]*)$", text, flags=re.M)
    return [(parts[i].strip(), parts[i + 1]) for i in range(1, len(parts), 2)]


def check(text, root=ROOT):
    errors = []
    found = cards(text)
    if not found:
        return ["no '## Read N' cards found"]
    for name, body in found:
        q = re.search(r"^\*\*Question:\*\* (.+)$", body, re.M)
        if not q or "Would" not in q.group(1) or "$" not in q.group(1):
            errors.append(f"{name}: needs a '**Question:** Would ... $price' line")
        if not re.search(r"^\*\*Issue:\*\* #\d+", body, re.M):
            errors.append(f"{name}: needs an '**Issue:** #N' line")
        if not re.search(r"^\*\*Recommendation:\*\* \S", body, re.M):
            errors.append(f"{name}: needs a '**Recommendation:**' line")
        srcs = re.findall(r"^\*\*Source:\*\* (\S+)$", body, re.M)
        texts = []
        for s in srcs:
            p = os.path.join(root, s)
            if os.path.isfile(p):
                texts.append(open(p, encoding="utf-8").read())
            else:
                errors.append(f"{name}: source file not found: {s}")
        if not srcs:
            errors.append(f"{name}: needs at least one '**Source:**' file")
        quotes = [l[2:] for l in body.splitlines() if l.startswith("> ")]
        if not quotes:
            errors.append(f"{name}: no quoted lines from the sample")
        for line in quotes:
            if texts and not any(line in t for t in texts):
                errors.append(f"{name}: quoted line not found word for word in its source: {line[:70]}")
    return errors


def self_test():
    import tempfile
    d = tempfile.mkdtemp()
    open(os.path.join(d, "s.md"), "w").write("> **Reply:** Thank you, Dana! Enjoy every bar.\n- **Liver.** Some text here.\n")
    good = ("## Read 1 — X\n**Question:** Would I pay **$79 a month**?\n**Issue:** #13\n"
            "**Source:** s.md\n\n> **Reply:** Thank you, Dana! Enjoy every bar.\n> - **Liver.** Some text here.\n"
            "**Recommendation:** Yes.\n")
    cases = [
        ("gold passes", good, True),
        ("changed word in quote", good.replace("Enjoy every bar", "Enjoy each bar"), False),
        ("invented quote line", good + "> Customers love us.\n", False),
        ("missing source file", good.replace("s.md", "nope.md"), False),
        ("no price in question", good.replace("**$79 a month**", "it"), False),
        ("no issue", good.replace("**Issue:** #13\n", ""), False),
        ("no recommendation", good.replace("**Recommendation:** Yes.\n", ""), False),
        ("no quotes", "\n".join(l for l in good.splitlines() if not l.startswith("> ")), False),
        ("no cards", "# nothing", False),
    ]
    ok = 0
    for label, text, want in cases:
        got = not check(text, d)
        mark = "OK " if got == want else "BAD"
        ok += got == want
        print(f"{mark} {label}")
    print(f"self-tests {ok}/{len(cases)}")
    return ok == len(cases)


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(0 if self_test() else 1)
    text = open(os.path.join(HERE, "STEP4_READS.md"), encoding="utf-8").read()
    errs = check(text)
    n = len(cards(text))
    q = sum(1 for _, b in cards(text) for l in b.splitlines() if l.startswith("> "))
    for e in errs:
        print("FAIL", e)
    print(f"{n} reads, {q} quoted lines, {len(errs)} errors")
    sys.exit(1 if errs else 0)
