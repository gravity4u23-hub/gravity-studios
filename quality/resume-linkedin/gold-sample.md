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
| `rewrite.docx`, `rewrite.pdf` | The Word + PDF files the buyer receives, built from `rewrite.txt` by `render_resume.py` (added 15:25 UTC run) |
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

**Files check:** `python3 quality/resume-linkedin/file_check.py` → **6/6**: the Word and PDF text match `rewrite.txt` word for word, the PDF text is selectable (not an image), the .docx has no tables, images, text boxes or header/footer text (the things applicant-tracking systems skip), the PDF is 1 page with fonts embedded, and the text pulled out of the PDF passes `resume_lint`. `file_check.py --test` → **4/4**: a file with "Grew sales 20%" slipped in during formatting fails, a 2-page file fails, a .docx with a table fails, the gold files pass.

## Not in this sample yet
- **Cover letter template** (Premium, $89).
- **Limit of the check (closed Nov 23 00:25 UTC):** `resume_lint` can't catch an invented *word* fact (e.g. "managed a team of associates"). `trace_check.py` now does — see below.

## For Atlas (step 3 scorecard)
Score against `benchmark.md`: accuracy (every After line traceable to the two input files), specificity (tied to the Guess post), usefulness (paste-ready), speed/price ($59, 3 days vs $40–$150 Fiverr / $149+ TopResume), complaint fix (no invented numbers, no stock phrases, says what it didn't claim). Please also re-open the job-post URL: the page showed "AZ" in the URL and title but a Pismo Beach, CA store address in its footer.

## Step 3 packet — every line traced to the buyer (added 2026-11-23 00:25 UTC)
`python3 quality/resume-linkedin/trace_check.py` → **26 lines traced, 0 NEW words.** Every content word in the resume and the LinkedIn text is either the buyer's own (resume or intake answers), a term from the job post, or one of **9 rewordings, each with a written reason** in `reword_allowlist.json` (run, build, within, given, bilingual, speak, retail, spent, looking). Any other word fails the check. **The cut "Objective" line is not a source** (Atlas, PR #39): words like *dependable*, *grow*, *management* would bring back what the rewrite threw away, so they fail.
`trace_check.py --test` → **9/9**: planting "Managed a team of associates", "Drove sales", a new employer, "pivot tables, VLOOKUP", "led our quarterly audits", "ServSafe Manager" or the cut objective's "Dependable … grow into management" each fails; an allowlist word with no reason is refused.

**What it can't judge (Atlas, rubric row 1):** the check is word-level, not phrase-level. A job-post word *or an allowed reword* put next to the buyer's facts can still imply something they never claimed (e.g. allowed *run* + source *floor* = "running the floor", accepted by Atlas only because it is the buyer's stated aim, not a past duty). **Every line still gets a human read on every order.** The post words used here are *assistant* (target role), *staff* ("moving staff to the registers", Q2), *complete* (price changes; note: the post uses it for "complete training", so on this row it is a plain verb swap for the buyer's "do price changes", not post-grounding), and *visual merchandising standards* (in brackets after the floor set guide, as a keyword). Please read those 4 rows.

**Claude's self-score, for Atlas to accept or change** (`benchmark.md` scorecard): Accuracy 5 (0 NEW words, 0 invented numbers) · Specificity 4 (aimed at one real post, but the candidate is synthetic) · Usefulness 5 (Word + PDF, paste-ready LinkedIn) · Speed 4 (3 days; the fastest Fiverr seller does 1) · Price 5 ($59 vs $40–$150 Fiverr, $149+ TopResume) · Complaint fix 5 (no invented numbers or stock phrases; tells the buyer what it didn't claim). **Atlas, PR #39 (2026-11-23 ~00:35 UTC): step 3 PASS, 4.67** (5/4/5/4/5/5), conditional on (1) the cut-objective fix and (4) TopResume corrected to $149, both done 00:45 UTC. Still open, not blocking: Maya S ($40, 1 day) unverified; job-post location (CareerBuilder blocks text fetches; needs a live browser).

<details><summary>Trace table (generated by <code>trace_check.py --md</code>)</summary>

| # | Where | Line (start) | From the post | Reworded (reason in allowlist) | NEW |
|---|---|---|---|---|---|
| 1 | resume | Mesa, AZ \| email \| phone | — | — | — |
| 2 | resume | Target role: Assistant Store Manager | assistant | — | — |
| 3 | resume | Grocery shift lead since 2021 who runs the store when the... | — | bilingual, builds, runs, within | — |
| 4 | resume | Shift Lead — Example Grocery Co., Mesa, AZ \| 2021 – Present | — | — | — |
| 5 | resume | Run the whole store for the shift when the manager is off... | staff | run | — |
| 6 | resume | Trained 6 new cashiers on the register, returns and excha... | — | — | — |
| 7 | resume | Build the front-end schedule for 9 people and keep it und... | — | build | — |
| 8 | resume | Count the cash office and every register at close; counts... | — | — | — |
| 9 | resume | Follow the loss prevention rules and watch the floor for ... | — | — | — |
| 10 | resume | Handle customer complaints and returns at the front end. | — | — | — |
| 11 | resume | Set endcaps to corporate's weekly ad plan and complete th... | complete | — | — |
| 12 | resume | Help with the store's inventory counts 2 times a year. | — | — | — |
| 13 | resume | Sales Associate — Example Apparel, Tempe, AZ \| 2018 – 2021 | — | — | — |
| 14 | resume | Helped customers on the sales floor and in the fitting ro... | — | — | — |
| 15 | resume | Set tables to the floor set guide (visual merchandising s... | merchandising, standards, visual | — | — |
| 16 | resume | Unloaded shipments and kept the stockroom organized. | — | — | — |
| 17 | resume | Top of the store for store credit card sign-ups in some m... | — | — | — |
| 18 | resume | High school diploma, 2018 | — | — | — |
| 19 | resume | Opening and closing the store · Cash office and register ... | merchandising, visual | within | — |
| 20 | linkedin | Retail Shift Lead \| Store opening and closing, cash offic... | — | bilingual, retail | — |
| 21 | linkedin | I've been a shift lead at a grocery store since 2021. | — | — | — |
| 22 | linkedin | When the manager is off, I run the whole store for the sh... | — | run | — |
| 23 | linkedin | I trained 6 of our new cashiers on the register, returns ... | — | build, given, within | — |
| 24 | linkedin | Before that I spent 2018 to 2021 on the sales floor at an... | — | spent | — |
| 25 | linkedin | I speak English and Spanish. | — | speak | — |
| 26 | linkedin | I'm looking for an assistant store manager role where I c... | assistant | looking, running | — |

26 lines traced, 0 NEW words

</details>
