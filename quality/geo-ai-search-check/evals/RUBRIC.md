# GEO / AI Search Check — eval set and model-graded rubric (Atlas)

**Code first.** `python3 check_reports.py` runs 15 hard cases from `cases.json` against `base-report.md` (Saguaro Drain Co. and its competitor Desert Pipe Pros are SYNTHETIC; no real business was checked). Each case is a request a buyer could make, or a shortcut a tired seller could take: promise a ChatGPT spot, promise more calls, count Unknowns as zero, soften the band, hide the Unknowns, drop the screenshots, point a fix at a check we never saw, say the ChatGPT profile boosts placement, add an unsourced "60% of customers" stat, drop the limits section, skip the crawler/profile lines, ship with template brackets, and (added Nov 23, the Business Hub fold-in) claim the ChatGPT profile for the buyer with their login or code, hide that claiming is free, or cut the can't-unpublish warning. The gold report passes every rule; the bad report fails on the exact rule it breaks (15/15, and no bad version trips a second rule; 31/31 with the base and gold runs). `python3 check_reports.py REPORT.md` checks one real report. `--test` runs the helper self-tests (16/16).

This sits after the work-log gate (Gravity-Studio `revenue-command-center/geo_worklog_check.py`, PR #54): the log proves the 9 checks were done; this proves the report built from it says only what the log shows.

Code proves a report breaks no hard rule. It can't tell whether the fixes are the right ones. Atlas scores what code can't, 1–5 each, one line of evidence per row. A report ships only if every row is 4+ and `check_reports.py` passes.

| # | Row | 5 looks like | 1 looks like |
|---|---|---|---|
| 1 | **Matches the screenshots** | Every "Cited / Mentioned / Not mentioned" and every competitor name can be seen in the named screenshot. | A finding the screenshot doesn't show. |
| 2 | **Right top 3** | The three fixes are the ones most likely to change what a customer is told (wrong phone, blocked crawler, missing service page), not the easiest to write. | Generic fixes ("post more on social media") that ignore the findings. |
| 3 | **Owner can act today** | Each fix names the exact place and action and an honest effort; a non-technical owner could do the 5-minute ones tonight. | "Improve your online presence." |
| 4 | **Honest about limits** | No promise of placement, calls or rankings; Unknowns explained in plain words; the snapshot date is clear. Answers benchmark complaints 1, 2 and 5. | Implies the fixes will get them named. |
| 5 | **Sources shown** | Each scored check lists the sources the engine cited, and at least one fix uses them (benchmark complaint 3). | Sources column empty or ignored. |
| 6 | **Would the owner pay $149 for this over a free grader?** | Yes: it shows their own customer questions, the exact answers and what to do, which the free tools don't. | No: a free 60-second score says the same. |

**Known traps to check by hand** (code can't): a competitor named who isn't in the screenshot; a "What could happen" line stated as a fact instead of "may"; a fix the owner can't do without paying someone, marked "5 min"; "#1" used harmlessly ("our #1 fix") is flagged by code on the safe side, and a human clears it.

Run: before gate step 3, after any change to the report template or runbook, and on every 10th delivered audit.
