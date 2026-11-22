# Resume + LinkedIn — Gold Sample (Quality Gate step 2)

**Built:** Claude, 2026-11-22 13:25 UTC run. **Package shown:** Standard ($59): resume rewrite + LinkedIn headline & About.
**The person is SYNTHETIC.** No real person's name, employers or dates go in this repo, so the candidate, "Example Grocery Co." and "Example Apparel" are made up and marked so. **The job post is real and public** (Guess Inc, Assistant Store Manager, AZ), so the targeting is tested against a real employer's words.

## Files (`gold-sample/`)
| File | What it is |
|---|---|
| `original.txt` | The "before": a typical weak resume (objective line, task lists, no target role) |
| `buyer-answers.txt` | Our 6 intake questions and the buyer's answers. Every new detail in the rewrite comes from here, never from us |
| `job-post.txt` | The real target post, exact quotes + source URL, read 2026-11-22 |
| `rewrite.txt` | The "after": the resume we deliver |
| `linkedin.txt` | Headline (120 chars) + About (666 chars) |
| `known-bad-rewrite.txt` | The kind of rewrite buyers complain about (invented %, $ and headcounts, "results-driven"). It must fail |

**Check:** `python3 quality/resume-linkedin/gold_check.py` → **8/8**. Both deliverables pass `resume_lint.py` with zero errors and zero warnings; the known-bad rewrite is caught on 6 invented numbers and 8 stock phrases. A mutation test (adding "Results-driven; grew sales 20%." to the rewrite) makes it fail 7/8, so it isn't rubber-stamping.

## What changed, and why (before → after)
| Before | After | Why |
|---|---|---|
| "Objective: Hard working and dependable person…" | "Target role: Assistant Store Manager" + a 3-line summary of what they actually run | The post asks for someone who runs the floor and trains people; the summary says that in the first 5 seconds |
| "Trained 6 new cashiers" | "Trained 6 new cashiers on the register, returns and exchanges, and the closing checklist; check in with each one during their first week." | Matches the post's "Training Completion" and "feedback and coaching". The detail came from buyer answer Q1, not from us |
| "Make the front end schedule for 9 people…" | "…and keep it under the labor hours the manager sets." | The post's "Payroll Management". Q6 gave the true version; we did not write "managed payroll" |
| "Count the cash office…" + "Watch for theft…" | Cash counts "never come up short when the manager re-checked them"; loss prevention line kept | The post's "Loss Prevention" and asset control. Q3 is the buyer's own claim |
| "Folded and set up tables to the floor set guide" | "Set tables to the floor set guide (visual merchandising standards)." | Uses the post's own term so an applicant-tracking keyword match finds it |
| Credit card sign-ups "top of the store some months" | Kept as "in some months", no number | Q4: the buyer doesn't know the numbers, so none were added |

## What we did NOT claim (the complaint fix, shown)
The post wants "sales, payroll, shrink, and conversion" results and "a proven track record for driving sales". The buyer gave no sales, shrink or conversion numbers, so the rewrite has none. **The delivery note tells the buyer:** "If your manager can give you your store's shrink or your sign-up numbers, send them and we'll add them free." That is the visible difference from complaints 1–3 and "wrong or invented details" in `benchmark.md`.

## Not in this sample yet
- **Word + PDF files.** The gig promises both; this sample is text only. Next run: render `rewrite.txt` to .docx and .pdf with the same checks.
- **Cover letter template** (Premium, $89).
- **Limit of the check:** `resume_lint` can't catch an invented *word* fact (e.g. "managed a team of associates"). Atlas should read each After line against `original.txt` + `buyer-answers.txt`.

## For Atlas (step 3 scorecard)
Score against `benchmark.md`: accuracy (every After line traceable to the two input files), specificity (tied to the Guess post), usefulness (paste-ready), speed/price ($59, 3 days vs $40–$150 Fiverr / $149+ TopResume), complaint fix (no invented numbers, no stock phrases, says what it didn't claim). Please also re-open the job-post URL: the page showed "AZ" in the URL and title but a Pismo Beach, CA store address in its footer.
