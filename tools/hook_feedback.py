#!/usr/bin/env python3
"""hook_feedback.py — turn real post results into "do more of / avoid" lists for the next batch.

Source (X-batch 2026-11-23, dipanshu_ai Claude course, transcript 00:23:33-00:24:20):
  "We actually plug in the top 10% performing hooks ... To do more of / And we have a list of
   the bottom 90% hooks / To avoid ... what I can do each day is update / The hooks that are
   working and not working ... Which is self-iterating / Feedback loop"

What this does: reads a CSV export of posts (Metricool or any tool) with the post text and
its numbers, ranks by engagement rate, and prints a block to paste into the social-batch
instructions. Honest limits, added on top of the source:
  * posts with fewer than --min-impressions (default 200) are left out: a rate on a tiny
    sample is noise, not a lesson;
  * with fewer than 10 usable posts it says "not enough data" and prints nothing to paste;
  * the hook is the post's first line, quoted exactly (no rewriting).
The source's split is top 10% / bottom 90%; --avoid-pct changes the avoid share.

CSV columns (header names, case-insensitive): text, impressions, engagements
Usage:  python3 tools/hook_feedback.py posts.csv [--min-impressions 200] [--avoid-pct 90]
        python3 tools/hook_feedback.py --self-test
No data yet (Nov 23, 2026): Metricool has no network connected, so nothing has been posted.
"""
import csv
import io
import math
import sys


def load(fh):
    rows = []
    for r in csv.DictReader(fh):
        r = {k.strip().lower(): (v or "").strip() for k, v in r.items() if k}
        try:
            imp, eng = float(r["impressions"]), float(r["engagements"])
        except (KeyError, ValueError):
            continue
        hook = r.get("text", "").splitlines()[0].strip() if r.get("text") else ""
        if hook:
            rows.append((hook, imp, eng))
    return rows


def feedback(rows, min_imp=200, avoid_pct=90):
    usable = [(h, i, e, e / i) for h, i, e in rows if i >= min_imp]
    if len(usable) < 10:
        return None, f"not enough data: {len(usable)} posts with {min_imp}+ impressions (need 10)"
    usable.sort(key=lambda r: r[3], reverse=True)
    n = len(usable)
    top_n = max(1, math.ceil(n * 0.10))
    avoid_n = min(n - top_n, max(1, math.floor(n * avoid_pct / 100)))
    top, avoid = usable[:top_n], usable[n - avoid_n:]
    out = [f"Based on {n} real posts with {min_imp}+ impressions (engagement rate = engagements / impressions).",
           "", f"Hooks to do more of (top {top_n}):"]
    out += [f'- "{h}" ({r:.1%})' for h, _, _, r in top]
    out += ["", f"Hooks to avoid (bottom {avoid_n}):"]
    out += [f'- "{h}" ({r:.1%})' for h, _, _, r in avoid]
    return "\n".join(out), None


def selftest():
    ok = total = 0
    # SYNTHETIC fixture: 12 made-up posts, not real results.
    lines = ["text,impressions,engagements"] + [f"Hook {i},1000,{i * 5}" for i in range(1, 13)]
    lines.append("Tiny sample hook,50,40")
    rows = load(io.StringIO("\n".join(lines)))
    text, err = feedback(rows)
    checks = [
        ("12 usable posts give a block", err is None and text is not None),
        ("best hook is on top", text and text.index('"Hook 12"') < text.index("Hooks to avoid")),
        ("tiny sample (50 impressions) left out", text and "Tiny sample" not in text),
        ("top share is 10% (2 of 12, rounded up)", text and "top 2" in text),
        ("avoid share defaults to 90% of the rest", text and "bottom 10" in text),
        ("fewer than 10 usable posts -> no block", feedback(rows[:5])[0] is None),
        ("--avoid-pct 10 avoids only 1", "bottom 1)" in feedback(rows, avoid_pct=10)[0]),
        ("hook is the first line, verbatim", load(io.StringIO('text,impressions,engagements\n"Line one\nline two",500,5'))[0][0] == "Line one"),
    ]
    for name, good in checks:
        total += 1
        ok += bool(good)
        print(("ok  " if good else "FAIL") + " " + name)
    print(f"{ok}/{total}")
    return 0 if ok == total else 1


def main(argv):
    if "--self-test" in argv:
        return selftest()
    if not argv:
        print(__doc__)
        return 2
    min_imp = int(argv[argv.index("--min-impressions") + 1]) if "--min-impressions" in argv else 200
    avoid = int(argv[argv.index("--avoid-pct") + 1]) if "--avoid-pct" in argv else 90
    with open(argv[0], newline="", encoding="utf-8") as fh:
        text, err = feedback(load(fh), min_imp, avoid)
    print(err or text)
    return 1 if err else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
