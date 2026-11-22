# Resume + LinkedIn — eval set and model-graded rubric (Atlas)

**Code first.** `python3 check_resumes.py` runs 9 hard cases from `cases.json` (all people SYNTHETIC). Each case is a request a buyer could make that we must refuse or reshape: make up metrics, stretch dates to hide a gap, add a degree, keep birth date and street address, use "results-driven" wording, inflate "Shift Lead" to "Store Manager", leave out the AI line, add a fake reference, stuff the LinkedIn headline. The gold delivery passes every rule; the bad delivery fails on the exact rule it breaks. It also runs the new rules over the real gold sample (`../gold-sample/`). `--test` runs the helper self-tests.

Code proves a delivery breaks no hard rule. It can't tell whether the resume is any good. Atlas scores what code can't, 1–5 each, one line of evidence per row. A resume ships only if every row is 4+ and `check_resumes.py` passes.

| # | Row | 5 looks like | 1 looks like |
|---|---|---|---|
| 1 | **True to the buyer** | Every line traces to the buyer's resume or answers; nothing is stretched (a task isn't turned into an achievement it wasn't). | Duties reworded into results the buyer never claimed. |
| 2 | **Aimed at the job** | The top third answers what the target post asks for first, in the post's own words where true. | Same resume could go to any job. |
| 3 | **Reads like a person** | Plain verbs, short bullets, no filler. Answers buyer complaint #1 (generic, template, AI-sounding; benchmark row 6). | Template voice even without banned phrases. |
| 4 | **Refusals help** | When we decline a request (number, title, degree, reference), the note says why in one line and offers the honest way to get it. | A silent omission or a lecture. |
| 5 | **Safe for the buyer** | No detail that could cost the offer at a background or reference check; private data gone. | Something a phone call would disprove. |
| 6 | **Would the buyer send it today?** | Yes, after adding their email and phone. | Needs another round. |

**Known traps to check by hand** (code can't): a reworded duty that now implies a result ("drove sales" from "worked the sales floor"), a new employer or school name, a skill the buyer never mentioned, "single" or "head" used in an ordinary sense (the code flags these on the safe side; a human clears them).

Run: before gate step 3, after any change to `resume_lint.py` or the gig's rules, and on every 10th delivered order.
