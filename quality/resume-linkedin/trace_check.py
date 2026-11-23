#!/usr/bin/env python3
"""trace_check.py — every word of substance in a resume rewrite must trace to the buyer.

resume_lint.py catches invented NUMBERS and stock phrases. It cannot catch an
invented WORD fact ("managed a team", "drove sales", "led audits"). This check
closes that hole for gate step 3, row 1 (Accuracy / "True to the buyer"):

  For each line of the delivery (rewrite.txt + linkedin.txt), every content word
  (stopwords dropped, light stemming) must be one of:
    SOURCE  in the buyer's own resume or intake answers           -> fine
    POST    in the target job post (keyword aim)                  -> listed for Atlas
    REWORD  in reword_allowlist.json with a one-line reason        -> listed for Atlas
  Anything else is NEW and fails the check.

The allowlist is the point: every word we add that the buyer never said has a
written reason a reviewer can disagree with.

Usage:
  python3 trace_check.py            check the gold sample, print the trace table
  python3 trace_check.py --md       same, as a Markdown table (for gold-sample.md)
  python3 trace_check.py --test     self-tests: planted invented facts must fail
Exit 0 = no NEW words.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
GOLD = os.path.join(HERE, "gold-sample")

STOP = set("""a an the and or but of to in on at for from by with as is are was were be been
being it its this that these those i i'm i've my me we our you your he she they them their
who what when where which while than then so if not no nor do does did done have has had
can could will would should may might must shall up down out over under into onto off
about after before since until each every all any some one two own same other such only
just also very more most per via vs etc s t ve m re ll d""".split())

# Section labels and layout words a resume always carries; not facts about the buyer.
FRAME = set("""summary experience education skills headline about target role present
sample candidate synthetic real person made gold email phone""".split())


def stem(w):
    w = w.lower().strip("'")
    if w.endswith("'s"):
        w = w[:-2]
    for suf in ("ings", "ing", "ies", "ied", "es", "ed", "ly", "s"):
        if len(w) > len(suf) + 2 and w.endswith(suf):
            w = w[: -len(suf)]
            if suf in ("ies", "ied"):
                w += "y"
            elif len(w) > 2 and w[-1] == w[-2] and w[-1] not in "ls":
                w = w[:-1]          # running -> run, setting -> set
            break
    if len(w) > 3 and w.endswith("e"):
        w = w[:-1]                  # schedule / scheduling -> schedul
    return w


def content_words(text):
    out = []
    for w in re.findall(r"[A-Za-z][A-Za-z'\-]*", text):
        for part in w.split("-"):
            lw = part.lower()
            if lw.endswith("'s"):
                lw = lw[:-2]
            if lw and lw not in STOP and lw not in FRAME and len(lw) > 1:
                out.append((lw, stem(lw)))
    return out


def vocab(text):
    return {s for _, s in content_words(text)}


def load_allow(path):
    with open(path) as f:
        data = json.load(f)
    allow = {}
    for word, reason in data.items():
        if not reason or len(reason.strip()) < 8:
            raise SystemExit(f"allowlist word '{word}' needs a real one-line reason")
        allow[stem(word)] = (word, reason)
    return allow


def delivery_lines(rewrite, linkedin):
    lines = []
    for name, text in (("resume", rewrite), ("linkedin", linkedin)):
        for raw in text.splitlines():
            line = raw.strip().lstrip("-").strip()
            if not line or line.isupper() or line.startswith("SAMPLE CANDIDATE"):
                continue
            # LinkedIn About is prose: one row per sentence.
            parts = re.split(r"(?<=[.!?])\s+", line) if name == "linkedin" else [line]
            lines += [(name, p) for p in parts if p]
    return lines


def trace(source, post, rewrite, linkedin, allow):
    src, pst = vocab(source), vocab(post)
    rows, new_total = [], 0
    for where, line in delivery_lines(rewrite, linkedin):
        post_w, reword_w, new_w = [], [], []
        for word, st in content_words(line):
            if st in src:
                continue
            if st in pst:
                post_w.append(word)
            elif st in allow:
                reword_w.append(word)
            else:
                new_w.append(word)
        new_total += len(new_w)
        rows.append((where, line, sorted(set(post_w)), sorted(set(reword_w)), sorted(set(new_w))))
    return rows, new_total


def read(name):
    with open(os.path.join(GOLD, name)) as f:
        return f.read()


def run(md=False):
    source = read("original.txt") + "\n" + read("buyer-answers.txt")
    post = read("job-post.txt")
    allow = load_allow(os.path.join(HERE, "reword_allowlist.json"))
    rows, new_total = trace(source, post, read("rewrite.txt"), read("linkedin.txt"), allow)
    used = {stem(w) for r in rows for w in r[3]}
    unused = [w for st, (w, _) in allow.items() if st not in used]
    if md:
        print("| # | Where | Line (start) | From the post | Reworded (reason in allowlist) | NEW |")
        print("|---|---|---|---|---|---|")
    for i, (where, line, p, r, n) in enumerate(rows, 1):
        if md:
            short = line if len(line) <= 60 else line[:57] + "..."
            short = short.replace("|", "\\|")
            print(f"| {i} | {where} | {short} | {', '.join(p) or '—'} | {', '.join(r) or '—'} | {', '.join(n) or '—'} |")
        else:
            flag = "NEW " if n else "ok  "
            extra = []
            if p: extra.append("post: " + ", ".join(p))
            if r: extra.append("reword: " + ", ".join(r))
            if n: extra.append("NEW: " + ", ".join(n))
            print(f"{flag}{where:8} {line[:70]}" + (f"  [{'; '.join(extra)}]" if extra else ""))
    if unused:
        print(f"\nnote: allowlist words not used by this sample: {', '.join(sorted(unused))}")
    print(f"\n{len(rows)} lines traced, {new_total} NEW words")
    return 0 if new_total == 0 else 1


def selftest():
    source = read("original.txt") + "\n" + read("buyer-answers.txt")
    post = read("job-post.txt")
    allow = load_allow(os.path.join(HERE, "reword_allowlist.json"))
    rw, li = read("rewrite.txt"), read("linkedin.txt")
    cases = [
        ("gold passes", rw, li, True),
        ("'managed a team' fails", rw + "\n- Managed a team of associates.\n", li, False),
        ("'drove sales' fails", rw.replace("Helped customers on the sales floor",
                                           "Drove sales on the floor"), li, False),
        ("new employer fails", rw + "\nCashier — Example Pharmacy, Mesa, AZ | 2017 – 2018\n", li, False),
        ("new skill fails", rw.replace("Excel (basic)", "Excel (pivot tables, VLOOKUP)"), li, False),
        ("invented duty in LinkedIn fails", rw, li + "\nI also led our quarterly audits.\n", False),
        ("new credential fails", rw.replace("High school diploma, 2018",
                                           "High school diploma, 2018; ServSafe Manager"), li, False),
    ]
    ok = 0
    for name, r, l, expect_pass in cases:
        _, new_total = trace(source, post, r, l, allow)
        passed = new_total == 0
        good = passed == expect_pass
        ok += good
        print(("ok  " if good else "FAIL") + f" {name} (NEW words: {new_total})")
    # allowlist without a reason must be refused
    tmp = os.path.join(HERE, ".tmp_allow.json")
    with open(tmp, "w") as f:
        json.dump({"spearheaded": ""}, f)
    try:
        load_allow(tmp)
        print("FAIL allowlist entry without a reason is refused")
    except SystemExit:
        ok += 1
        print("ok   allowlist entry without a reason is refused")
    finally:
        os.remove(tmp)
    total = len(cases) + 1
    print(f"{ok}/{total}")
    return 0 if ok == total else 1


if __name__ == "__main__":
    if "--test" in sys.argv:
        sys.exit(selftest())
    sys.exit(run(md="--md" in sys.argv))
