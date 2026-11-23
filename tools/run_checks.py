#!/usr/bin/env python3
"""run_checks.py — every standing check in this repo, quietly.

From Anthropic's Claude Code token-efficiency webinar (rrrangle, X-batch 2026-11-23):
command output stays in the conversation for the rest of the session, so a runner that
prints a line per passing test wastes context on every later request. Keep the commands
you run all day in CLAUDE.md, written exactly, with a quiet reporter that prints only
failures.

This prints ONE line per failing check (plus its last lines of output) and one summary
line. Passing checks print nothing unless -v.

Usage:  python3 tools/run_checks.py [-v] [--gs-listing DIR] [--gs-wellness DIR]
Exit 0 = all pass. Standard library only, offline. Two checks import an eval checker
from an unmerged Gravity-Studio branch: listing needs a checkout of
claude/listing-makeover-evals (PR #52), wellness needs claude/wellness-negation-scope
(PR #56; its base #55 alone fails one self-test). Without the flag they are listed as
skipped, never counted as passed.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Q = "quality"
# Placeholders filled from --gs-listing DIR / --gs-wellness DIR (Gravity-Studio checkouts).
GS_FLAGS = {"<gs-listing>": "--gs-listing", "<gs-wellness>": "--gs-wellness"}

# (label, folder relative to repo root, argv). Self-tests first, then real runs.
CHECKS = [
    ("eval coverage self-test", Q, ["eval_coverage.py", "--self-test"]),
    ("eval coverage", Q, ["eval_coverage.py"]),
    ("step4 reads", Q, ["step4_check.py"]),
    ("step4 self-test", Q, ["step4_check.py", "--self-test"]),
    ("geo report evals", f"{Q}/geo-ai-search-check/evals", ["check_reports.py"]),
    ("geo report self-test", f"{Q}/geo-ai-search-check/evals", ["check_reports.py", "--test"]),
    ("geo robots self-test", f"{Q}/geo-ai-search-check", ["robots_ai_check.py", "--test"]),
    ("geo site self-test", f"{Q}/geo-ai-search-check", ["site_ai_check.py", "--test"]),
    ("listing gold eval", f"{Q}/listing-makeover", ["gold_eval.py", "gold-sample-listings.md", "--gs", "<gs-listing>"]),
    ("listing gold self-test", f"{Q}/listing-makeover", ["gold_eval.py", "--test"]),
    ("listing mohs self-test", f"{Q}/listing-makeover", ["mohs_check.py", "--test"]),
    ("listing trial self-test", f"{Q}/listing-makeover", ["trial_check.py", "--self-test"]),
    ("resume evals", f"{Q}/resume-linkedin/evals", ["check_resumes.py"]),
    ("resume evals self-test", f"{Q}/resume-linkedin/evals", ["check_resumes.py", "--test"]),
    ("resume gold", f"{Q}/resume-linkedin", ["gold_check.py"]),
    ("resume files", f"{Q}/resume-linkedin", ["file_check.py"]),
    ("resume lint self-test", f"{Q}/resume-linkedin", ["resume_lint.py", "--test"]),
    ("resume trace", f"{Q}/resume-linkedin", ["trace_check.py"]),
    ("resume trace self-test", f"{Q}/resume-linkedin", ["trace_check.py", "--test"]),
    ("resume trial", f"{Q}/resume-linkedin", ["trial_check.py"]),
    ("resume trial self-test", f"{Q}/resume-linkedin", ["trial_check.py", "--self-test"]),
    ("review trial", f"{Q}/review-reply-desk", ["trial_check.py"]),
    ("review trial self-test", f"{Q}/review-reply-desk", ["trial_check.py", "--self-test"]),
    ("spanish self-test", f"{Q}/spanish-page", ["spanish_check.py", "--test"]),
    ("wellness gold self-test", f"{Q}/wellness-blog-engine", ["gold_eval.py", "--test", "--gs", "<gs-wellness>"]),
    ("wellness trial", f"{Q}/wellness-blog-engine", ["trial_check.py"]),
    ("wellness trial self-test", f"{Q}/wellness-blog-engine", ["trial_check.py", "--self-test"]),
    ("hook feedback self-test", "tools", ["hook_feedback.py", "--self-test"]),
    ("prompt quotes self-test", "research", ["verify_prompt_quotes.py", "--self-test"]),
]


def main(argv):
    verbose = "-v" in argv
    gs = {ph: os.path.abspath(argv[argv.index(fl) + 1]) for ph, fl in GS_FLAGS.items() if fl in argv}
    failed = skipped = 0
    for label, folder, args in CHECKS:
        cwd = os.path.join(ROOT, folder)
        ph = next((a for a in args if a in GS_FLAGS), None)
        if ph:
            if ph not in gs:
                skipped += 1
                print(f"skip {label}: needs {GS_FLAGS[ph]} DIR (Gravity-Studio checkout)")
                continue
            args = [gs.get(a, a) for a in args]
        if not os.path.isfile(os.path.join(cwd, args[0])):
            skipped += 1
            if verbose:
                print(f"skip {label} (not on this branch)")
            continue
        p = subprocess.run([sys.executable, *args], cwd=cwd, capture_output=True, text=True, timeout=300)
        if p.returncode != 0:
            failed += 1
            tail = (p.stdout + p.stderr).strip().splitlines()[-8:]
            print(f"FAIL {label}: {folder}/{' '.join(args)} (exit {p.returncode})")
            for line in tail:
                print("     " + line)
        elif verbose:
            print(f"ok   {label}")
    ran = len(CHECKS) - skipped
    print(f"{ran} checks run, {failed} failed" + (f", {skipped} skipped" if skipped else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
