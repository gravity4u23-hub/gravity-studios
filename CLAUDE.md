# CLAUDE.md — gravity-studios

Kept short on purpose: everything here is loaded on every request (Anthropic token-efficiency webinar, X-batch rrrangle 2026-11-23). Task-specific rules live next to the task (each `quality/<service>/` folder), not here.

- Read `HIVEMIND.md`, `OWNER_STEERING.md` and `QUALITY_GATE.md` before work. Steering overrides the plan; HIVEMIND overrides everything.
- Branches and pull requests only. Never push to main and never merge. Never spend, publish, send or contact anyone. Those are owner taps in `OWNER_BRIEF.md`.
- No invented customers, results, numbers or quotes. Every quote must be word for word from a source we opened.

## Checks (quiet: prints failures only)
```
python3 tools/run_checks.py                      # all standing checks, one summary line
python3 tools/run_checks.py --gs-listing ../gs-listing --gs-wellness ../gs-wellness   # + the 2 that need Gravity-Studio branches
python3 quality/eval_coverage.py                 # every eval set has control + edge + refuse cases
```
