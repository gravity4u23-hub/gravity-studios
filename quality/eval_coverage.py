#!/usr/bin/env python3
"""eval_coverage.py — does each service's eval set cover the three kinds of case?

From Anthropic's "prompting playbook" talk (Code with Claude, transcribed in the X-batch pack:
rahultechx, 2026-11-23): an eval set should start with
  * a "control case" that always passes, so a change that breaks normal work shows up;
  * "edge cases" where the model went wrong before; and
  * cases where it should hand off to a human or refuse.
Our sets were built from hard cases only, so this check counts kinds per set:

  control  an ordinary request; gold must pass
  edge     a seller shortcut / known failure
  refuse   the buyer asks for something we decline (in part) and say why
  handoff  goes to David instead of being answered (optional kind, counted, not required)

A set FAILS if any case has no "kind", or it has no control, no edge or no refuse case.

Usage:
  python3 eval_coverage.py                 sets under quality/*/evals/ (this repo)
  python3 eval_coverage.py --gs DIR        also Gravity-Studio portfolio/*/evals/ in checkout DIR
  python3 eval_coverage.py --self-test
Exit 0 = every set covered. Offline, standard library only.
"""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
KINDS = ("control", "edge", "refuse", "handoff")
REQUIRED = ("control", "edge", "refuse")


def coverage(cases):
    counts = {k: 0 for k in KINDS}
    untagged = []
    for c in cases:
        k = c.get("kind")
        if k in counts:
            counts[k] += 1
        else:
            untagged.append(c.get("id", "?"))
    gaps = [f"no {k} case" for k in REQUIRED if counts[k] == 0]
    if untagged:
        gaps.insert(0, f"{len(untagged)} case(s) without a kind")
    return counts, gaps


def load(path):
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    return d["cases"] if isinstance(d, dict) else d


def report(paths, root):
    bad = 0
    print(f"{'set':58} {'ctl':>3} {'edge':>4} {'ref':>3} {'hand':>4}  result")
    for p in paths:
        counts, gaps = coverage(load(p))
        bad += bool(gaps)
        name = os.path.relpath(p, root)
        print(f"{name:58} {counts['control']:>3} {counts['edge']:>4} {counts['refuse']:>3} {counts['handoff']:>4}  "
              + ("OK" if not gaps else "GAP: " + "; ".join(gaps)))
    print(f"\n{len(paths)} sets, {bad} with gaps")
    return bad


def selftest():
    cases = [
        ("all three kinds pass", [{"id": "a", "kind": "control"}, {"id": "b", "kind": "edge"},
                                  {"id": "c", "kind": "refuse"}], True),
        ("no control fails", [{"id": "b", "kind": "edge"}, {"id": "c", "kind": "refuse"}], False),
        ("no refuse fails", [{"id": "a", "kind": "control"}, {"id": "b", "kind": "edge"}], False),
        ("untagged case fails", [{"id": "a", "kind": "control"}, {"id": "b", "kind": "edge"},
                                 {"id": "c", "kind": "refuse"}, {"id": "d"}], False),
        ("misspelled kind fails", [{"id": "a", "kind": "contrl"}, {"id": "b", "kind": "edge"},
                                   {"id": "c", "kind": "refuse"}], False),
        ("handoff is optional", [{"id": "a", "kind": "control"}, {"id": "b", "kind": "edge"},
                                 {"id": "c", "kind": "refuse"}, {"id": "d", "kind": "handoff"}], True),
    ]
    ok = 0
    for name, cs, expect in cases:
        _, gaps = coverage(cs)
        good = (not gaps) == expect
        ok += good
        print(("ok  " if good else "FAIL") + f" {name}")
    print(f"{ok}/{len(cases)}")
    return 0 if ok == len(cases) else 1


def main(argv):
    if "--self-test" in argv:
        return selftest()
    paths = sorted(glob.glob(os.path.join(HERE, "*", "evals", "cases.json")))
    root = os.path.dirname(HERE)
    if "--gs" in argv:
        gs = os.path.abspath(argv[argv.index("--gs") + 1])
        paths += sorted(glob.glob(os.path.join(gs, "portfolio", "*", "evals", "cases.json")))
        root = os.path.dirname(root)
    return 1 if report(paths, root) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
