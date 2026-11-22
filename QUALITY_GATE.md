# Quality Gate — nothing launches until it beats the best

Owner order, Nov 21, 2026: "How do you know the services you produce are good enough? … Add a quality gate."

Our own checks (Atlas review, honesty rules, scripted limits) prove the work is **careful**. They don't prove it's **better than what buyers can already get**. The gate does.

## The gate — every service passes all 5 before its first pitch, gig or post

| # | Check | Who | Pass = |
|---|---|---|---|
| 1 | **Benchmark the best.** Top 3 competitors for this exact service (Fiverr, Etsy, agencies): price, delivery time, what's included, what their reviews praise and **complain about**. | Grok | `quality/<service>/benchmark.md` committed with sources |
| 2 | **Gold sample.** One real, complete deliverable made with the service's skill, on a real (public) business or our own (Davias, Gravity Studios). | Claude | `quality/<service>/gold-sample.md` |
| 3 | **Side-by-side.** Sample scored against the benchmark on the scorecard below. Must **beat or match the best on quality AND beat on price or speed**, and fix at least one thing competitors' buyers complain about. | Atlas (blind where possible) | Scorecard committed, all rows ≥ competitor |
| 4 | **Owner read.** David reads the sample and answers one question: *"Would I pay for this?"* | Owner (dashboard card) | "Yes" |
| 5 | **Free trial with a real business.** 1–3 free samples to real prospects (with owner OK on each send). Record what they did: used it / said thanks / ignored / complained. | Claude drafts, owner sends | At least 1 of 3 used it or asked for more |

**Gate status lives on the dashboard** (lane blocker reads "Quality gate: step N").

## Scorecard (1–5, with one line of evidence each)
1. **Accuracy** — every fact true and sourced; zero invented claims.
2. **Specificity** — about *this* business, not a template.
3. **Usefulness** — buyer can use it in under 5 minutes (paste-ready, clear next step).
4. **Speed** — delivery time vs competitors.
5. **Price/value** — what they get per dollar vs competitors.
6. **The complaint fix** — names the #1 thing competitors' reviews complain about and shows how ours avoids it.

## After launch — the gate keeps running
Tracked per service on the dashboard:
- **Revision requests** > 1 in 4 orders → back to step 2.
- **Any refund** → Atlas root-cause review before the next order.
- **Rating** below 4.8 after 10 orders → fix or pause.
- **Repeat or monthly buyers** = the real proof it's good.

## Services and where they stand (Nov 21)
| Service | Steps passed |
|---|---|
| Review Reply Desk | 1 verified by Atlas (Nov 22 00:17 UTC, conditional fixes made: Marqii row, "free" dropped, Smith & Floyd marked unverified); 2 done (SweetSoftSkin, quotes 8/8, lint 9/9; Google-profile sample still to follow); **3 PASS** (Atlas scorecard 5 / 5 / 4 / 5 / 4 / 4, with the pitch rule: never claim cheaper or faster than software); needs 4 (your read), 5 (free trial: pack prepared Nov 22, `quality/review-reply-desk/free-trial.md`, `trial_check.py` 14/14 self-tests; Trial 1 SweetSoftSkin text passes but is on HOLD until a contact route outside Etsy is found; trials 2–3 wait on Atlas reading Google reviews) |
| Listing Makeover | 1 drafted by Claude (Nov 22, `quality/listing-makeover/benchmark.md`, Grok away; Atlas to verify); 2 (Davias Helix listings; titles fixed Nov 22 to Etsy's under-15-words / no-repeat guidance, `listing_lint.py --strict-titles` 12/12); eval set built Nov 22 (Gravity-Studio PR #52: 8 synthetic hard cases, invented-number check, gold 8/8, known-bad 8/8 caught); needs 3 (Atlas scorecard + eval rubric), 4, 5 |
| Wellness Blog Engine | 1 drafted by Claude (Nov 22, `quality/wellness-blog-engine/benchmark.md`: beats agencies on price at $150 vs $390–$600, matches but does not beat the best $30 Fiverr writer, loses to $99 software; Atlas PASS conditional on PR #15, Fiverr rows verified live; buyer-complaints row filled Nov 22 09:30 UTC by Claude with 5 verbatim buyer reviews from WriterAccess and Textbroker, Atlas to re-open); 2 nearly done: real-business sample written (Nov 22, `quality/wellness-blog-engine/gold-sample-002-winter-sun.md`, ashwagandha for Winter Sun Trading Co., 3 sources opened, `post_lint.py --presale` OK, 1,052 words; Winter Sun not contacted); Black Seed sample 001: both meta-analyses re-checked Nov 22 (PubMed Central full text + DOAJ abstract; one fix, "pooled 82" → "reviewed 82, 79 pooled"), `post_lint.py --presale` OK, Atlas to confirm "79 pooled" on ScienceDirect (Gravity-Studio PR #53); **ready for 3** (Atlas scorecard), then 4, 5 |
| GEO / AI search check | 1 drafted by Claude (Nov 22 10:25 UTC, `quality/geo-ai-search-check/benchmark.md`, Grok away; Atlas to verify): $149 beats the two Fiverr audits ($40–$50, 3 days) on speed only, loses on price to them and to **free** tools (Insites, HubSpot AI Search Grader, ChatGPT's free business profiles); no verbatim buyer complaints found yet (seller warning lists only). Gap fix prototyped: `robots_ai_check.py` (AI-crawler block check, 12/12 self-tests). Step 2 prep Nov 22 11:25 UTC (Gravity-Studio PR #54): all 3 benchmark gaps are now runbook steps (crawler check, ChatGPT profile line, sources cited per check), enforced by `geo_worklog_check.py` (15/15); needs 2 (gold sample on our own business, needs a signed-in browser for ChatGPT), 3, 4, 5. **Not passed, so not pitched** — see owner decision on tap 2 / tap 17 |
| Resume + LinkedIn | 1 drafted by Claude (Nov 22 12:25 UTC, `quality/resume-linkedin/benchmark.md`, Grok away; Atlas to verify): $25/$59/$89 in 2–3 days beats 4 Fiverr sellers ($40–$150, 1–7 days) on price and TopResume ($149–$179 entry, ~1 week) on price and speed, but not the fastest Fiverr seller (1 day) and we have 0 reviews; 8 verbatim Trustpilot complaints, #1 about the work = generic/template/AI-sounding output. Complaint fix prototyped: `resume_lint.py` (invented numbers + stock phrases, 9/9 self-tests). Gig must add an AI-assisted line. Needs 2 (gold sample on a marked synthetic resume, so no real person's details go in the repo), 3, 4, 5 |
| Spanish page | — |
| Fiverr gigs | inherit their service's gate — no gig goes live until its service passes |

Rule for every agent: **if a service hasn't passed, don't pitch it, don't post it, don't list it.** Build toward the gate instead.
