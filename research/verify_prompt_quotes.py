#!/usr/bin/env python3
"""verify_prompt_quotes.py — every prompt in x-batch-2026-11-23-prompts.json must be in its transcript.

Reads the transcript pack (research/x-batch-implementation-pack-2026-11-22-CLEAN-NEUTRAL.md
on main), splits it by "## N. <handle>" sections, strips the "[hh:mm:ss.ss]" stamps, joins
the lines with single spaces, and checks each prompt is a substring of its handle's section
(exact characters; only whitespace runs are collapsed). Also checks the stated timestamp
appears in that section.

Usage:  python3 verify_prompt_quotes.py [--pack PATH]
        python3 verify_prompt_quotes.py --self-test
Exit 0 = every prompt found.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_PACK = os.path.join(HERE, "x-batch-implementation-pack-2026-11-22-CLEAN-NEUTRAL.md")
STAMP = re.compile(r"^\[(\d\d:\d\d:\d\d)\.\d+\]\s*")


def sections(pack):
    out = {}
    for m in re.finditer(r"^## \d+\. (\S+)(?: #\d)?\s*$(.*?)(?=^## \d+\. |\Z)", pack, re.M | re.S):
        handle, body = m.group(1), m.group(2)
        stamps, words = [], []
        for line in body.splitlines():
            s = STAMP.match(line)
            if s:
                stamps.append(s.group(1))
                words.append(line[s.end():])
        out.setdefault(handle, []).append((" ".join(" ".join(words).split()), set(stamps)))
    return out


def verify(prompts, secs):
    errs = []
    for p in prompts:
        want = " ".join(p["text"].split())
        hits = [st for text, st in secs.get(p["source"], []) if want in text]
        if not hits:
            errs.append(f'{p["source"]} {p["timestamp"]}: NOT in transcript: "{p["text"][:60]}"')
        elif not any(p["timestamp"] in st for st in hits):
            errs.append(f'{p["source"]} {p["timestamp"]}: text found but timestamp not in that transcript')
    return errs


def selftest():
    pack = "## 1. demo\n\n[00:00:01.00] please write\n[00:00:02.00] a haiku about rain\n## 2. other\n[00:00:01.00] hi\n"
    secs = sections(pack)
    cases = [
        ("prompt across two lines is found", [{"source": "demo", "timestamp": "00:00:01", "text": "write a haiku"}], True),
        ("changed word fails", [{"source": "demo", "timestamp": "00:00:01", "text": "write a poem"}], False),
        ("wrong handle fails", [{"source": "other", "timestamp": "00:00:01", "text": "write a haiku"}], False),
        ("wrong timestamp fails", [{"source": "demo", "timestamp": "00:09:09", "text": "write a haiku"}], False),
    ]
    ok = 0
    for name, ps, expect in cases:
        good = (not verify(ps, secs)) == expect
        ok += good
        print(("ok  " if good else "FAIL") + " " + name)
    print(f"{ok}/{len(cases)}")
    return 0 if ok == len(cases) else 1


def main(argv):
    if "--self-test" in argv:
        return selftest()
    pack_path = argv[argv.index("--pack") + 1] if "--pack" in argv else DEFAULT_PACK
    with open(pack_path, encoding="utf-8") as f:
        secs = sections(f.read())
    with open(os.path.join(HERE, "x-batch-2026-11-23-prompts.json"), encoding="utf-8") as f:
        prompts = json.load(f)["prompts"]
    errs = verify(prompts, secs)
    roles = {}
    for p in prompts:
        roles[p.get("role", "unlabeled")] = roles.get(p.get("role", "unlabeled"), 0) + 1
        if p.get("role") not in ("instruction", "eval_input", "scenario_input", "illustration"):
            errs.append(f'{p["source"]} {p["timestamp"]}: no valid role')
    for e in errs:
        print("ERROR", e)
    print(f"{len(prompts)} verbatim lines checked against the transcripts, {len(errs)} errors")
    print("by role: " + ", ".join(f"{k} {v}" for k, v in sorted(roles.items())))
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
