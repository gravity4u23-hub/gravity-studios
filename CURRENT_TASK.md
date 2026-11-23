# CURRENT TASK — Gravity Studios

**Last updated:** 2026-11-22 by Grok, Atlas reply 21:45 UTC

## Grok Status
- Back online.
- Standing order: When owner sends X links/videos/texts, immediately transcribe/summarize into `research/`, update `research/INBOX.md`, and note here.
- Latest processed: cyrilxbt Amodei advice + Stanford lecture notes.

## Claude Progress
- **2026-11-23 15:25 UTC (Claude, hourly run):**
  - **Inputs:** no new INBOX items, no for-claude issues in either repo, sprint #6 unchanged, no Grok tasks, no Atlas comments on PRs #55–#56 since 14:25 UTC (last main commit 08:29 UTC).
  - **Moved:** Review Desk trial 2 lead P009 re-read from the cloud. Page name + city now recorded (The Vitality Doctor- Dr Christina Kovalik NMD, LAc, Flagstaff AZ; passes the match). Two traps found for Atlas's browser look: (1) the same doctor has a second Birdeye page in Paradise Valley, AZ, so Atlas must open the Flagstaff profile; (2) 2 of the 5 visible reviews are "a year ago", which Google uses for roughly 12–23 months. `review_gap_check.py` rule 7: the age cell is whole months, "12-23" for "a year ago", or "-", and a range never makes a row ELIGIBLE. 0 errors, self-tests 27/27 (5 new). Massage Therapy by Bliss checked and not added (newest review ~3 years old). No review text or names in the repo.
  - **Next:** Atlas opens P009's **Flagstaff** Google profile: under-5★ review, its date (not just "a year ago"), reply, name + city → if ELIGIBLE, Claude drafts trial 2's replies (`review_lint.py --health`).
- **2026-11-23 14:25 UTC (Claude, hourly run):**
  - **Inputs:** no new INBOX items, no for-claude issues, sprint #6 unchanged, no Grok tasks, no Atlas comments on any open Claude PR in either repo since 13:00 UTC (last main commit 08:29 UTC).
  - **Moved:** Review Desk trials 2–3, the 4 unread clinics. Site searches turned up Birdeye pages for 3 of them: P008 Synergistic Healthcare NO-GAP (16 Google, 5.0, so all 5★); P006's only match is "Cedar Health" in **Tucson**, and P007's only match is **Munderloh Chiropractic**, not Munderloh Integrated Medical. Both are WRONG-PAGE. P004 had no Birdeye page. Hole found and closed: `review_gap_check.py` trusted that the page was the prospect. It now needs a "Page name, city" column, matches the city to the file's `**Prospect city:**` line and the name by key words, and has a WRONG-PAGE status. Legacy 13:40 rows may say "unrecorded" but can't be ELIGIBLE. 0 errors, self-tests 22/22 (9 new). No review text or reviewer names in the repo.
  - **Next:** unchanged and now sharper. P009 The Vitality Doctor is the only live lead for trials 2–3. Atlas opens its Google profile (stars, age, reply, name + city) → if ELIGIBLE, Claude drafts trial 2's replies. Optional: Atlas checks whether Munderloh Integrated Medical has its own Google profile.
- **2026-11-23 13:25 UTC (Claude, hourly run):**
  - **Inputs:** no new INBOX items, no for-claude issues, sprint #6 unchanged, no Grok tasks, no Atlas comments on any open Claude PR in either repo since 12:00 UTC (last main commit 08:29 UTC).
  - **Moved:** Review Desk trials 2–3. Google Maps is blocked from the cloud, but Birdeye's public copies of the Google/Facebook reviews can be read. New `quality/review-reply-desk/trial-prospects.md` triages P004–P010: P009 The Vitality Doctor is the best lead (23 Google reviews, 4.5, last 1–2 months, no reply text seen); P010 NO-GAP (5 reviews, 5.0); P005 NEEDS-BROWSER; P004/P006–P008 not read. New `review_gap_check.py` refuses ELIGIBLE unless the stars (1–4), age (12 months or less) and the no-reply were seen on a rendered page, and refuses review text in health-clinic rows. 0 errors, self-tests 13/13. Review text is kept out of the public repo.
  - **Next:** Atlas opens P009's Google profile (stars + reply) → if ELIGIBLE, Claude drafts the trial 2 replies (HIPAA-safe) and lints them.
- **2026-11-23 12:25 UTC (Claude, hourly run):**
  - **Inputs:** no new INBOX items (last item Nov 21; all carry a review note), no for-claude issues, sprint #6 unchanged since Nov 22, no Grok tasks, no Atlas comments on any open Claude PR in either repo since 10:00 UTC. Atlas's PR #57 points were already answered (125a007 / e02980a); his build.py "8 planted" nit is already fixed.
  - **Moved:** Business Hub Claim folded into the GEO audit (the 11:25 recommendation, no tap needed): the synthetic report's ChatGPT-profile line now says you claim it yourself (own phone/email/website + ID check), never share the codes with anyone including us, and a published profile reportedly can't be unpublished, so check details first. New `check_reports.py` rule `profile_claim` (only when the profile is Not claimed): fails if the line hides "free", drops the can't-unpublish warning, or asks for a login, code or ID. 3 new hard cases (claim-it-for-me, hide-free, cut-the-warning): 31/31, self-tests 16/16, each bad case trips only its own rule.
  - **Not done, on purpose:** the open "browser look" checks (SweetSoftSkin Facebook, Winter Sun stock, CareerBuilder location) stay with Atlas/owner; those sites refused our fetch, and the cloud doesn't route around a refusal.
- **2026-11-23 11:25 UTC (Claude, hourly run):**
  - **Inputs:** no new INBOX items, no for-claude issues, no new Grok tasks, no Atlas comments on gravity-studios #41–#52 or Gravity-Studio #47–#59 since 10:25.
  - **Moved:** Business Hub Claim gate step 1 drafted (Grok's task from 09:25, nothing from Grok by 11:25): `quality/business-hub-claim/benchmark.md` (5 pages read, LocalIQ blocked; none is OpenAI's own) + `offer_check.py` (free line, you-verify line, no placement promise, no logins/codes/ID, no review/introductions condition, can't-unpublish warning; self-tests 9/9). Finding: verification is the owner's own phone/email/DNS + Persona ID scan, so only a guided claim is possible; only agencies sell it, no posted prices; no Fiverr gig found. Recommendation: fold into the GEO audit as a fix line. QUALITY_GATE row + dashboard lane updated; build.py runs.
  - **Next:** Atlas verifies the benchmark (re-open the sources; help.openai.com if his browser can); owner tap 18.
- **2026-11-23 10:25 UTC (Claude, hourly run):**
  - **Inputs:** no new INBOX items, no for-claude issues, no new Grok tasks, no Atlas comments on #49–#51 / Gravity-Studio #57–#59 since 09:25.
  - **Moved:** Wellness step 5, day-of check 2. A site search finds Winter Sun's product page "Ashwagandha (Dried Root)" (`/products/ashwagandha-dried-root`). Stock is unread because wintersun.com is blocked from the cloud (proxy 403, WebFetch not allowlisted), so it's a browser look on send day. Message unchanged; trial_check 1/1, self-tests 24/24; step4_check 0 errors; build.py runs (LEDGER set). QUALITY_GATE + dashboard Wellness lane updated.
  - **Next:** Atlas opens the product page + reviews #59; owner tap 18.
- **2026-11-23 09:25 UTC (Claude, hourly run):**
  - **Research:** new Gravity-Studio main commits `498c5de`–`e012af2` (Claude transcripts pack, Mind-Ware OS + mentalist pack, OPERATING_PRINCIPLES adoption) were read.
  - **3 transcripts:** the X links missing at 08:25 now have a read. ishh_021 gave 10 verbatim prompt blocks; reyainami and aresotik had none. `prompt_check.py --quotes` now reads the Claude pack too: self-test 13/13 (was 9/9), 47/47 blocks match.
  - **Mind-Ware review:** core rule adopted; 8 items reviewed, not applied. Business Hub is free to claim per reports; review-for-discount conflicts with tap 17; the Barnum line isn't true. Gravity-Studio PR #59, which contains #58.
  - **Dashboard:** Business Hub Claim lane added at Idea.
  - **Other inputs:** no for-claude issues, no new Grok tasks for Claude. Atlas's 08:22 points on #57 were already answered at 08:30.
  - **Next:** Atlas reviews #59; Grok benchmarks Business Hub; owner tap 18.
- **2026-11-23 08:25 UTC (Claude, hourly run + owner's live X-links ask):** Atlas's PR #57 points #3/#4 fixed (`125a007`): cite_check short cites + Id., primary sources by kind, no Wikipedia; the ", Inc." regex bug meant Mata was never checked; 21/21; top-20 #10/#11 rescored, Tier 1 now says "awaiting tap". Owner's 13 X links: 0 openable (robots_disallowed), read from pack transcripts; 37 verbatim spoken-prompt blocks, 37/37 re-checked; 4 Claude-written prompts + prompt_check.py (9/9, 0 errors) + first GER run (4/4) → review_lint "free bar" gap fixed on Gravity-Studio PR #47 (`960228c`, 20/20). PR #58. No new INBOX items, no for-claude issues.
- **2026-11-23 07:25 UTC (Claude, hourly run):** Research: no new INBOX items, no for-claude issues, no new Grok tasks. Atlas's 07:14 follow-up on PR #47 = PASS (conditional on the Instagram HOLD), no new gaps, nothing to fix. **Moved:** Resume + LinkedIn gate step 5 prepared (PR #48, stacked on #47): `quality/resume-linkedin/free-trial.md` (owner-sent message to someone he already knows who is job-hunting, intake, delivery steps + note, results log as Person A/B/C) + `trial_check.py` (no price/job/interview/ATS promise; AI, nothing-invented, privacy + deletion and no-reply lines; business line; ≤150 words; [first name] placeholder only; delivery note offers free fixes and free number adds; **public-repo privacy scan**: no email or non-business phone in this folder, gold-sample/ or evals/ except the 555-01xx fiction range): 0 errors, HOLD (no person chosen); self-tests 16/16. `trace_check.py --dir DIR` runs a real order kept in the private repo and needs that order's own `reword_allowlist.json` (gold reasons cite the synthetic buyer, so they don't carry over): self-tests 12/12 (was 9/9). gold_check 8/8, file_check 6/6, step4_check 0 errors. Dashboard Resume lane + tap 21 updated.
- **2026-11-23 06:25 UTC (Claude, hourly run):** Research: no new INBOX items, no for-claude issues, no new Grok tasks. Atlas's 06:25 review of PR #47 (PASS conditional on the route HOLD) was already answered in `1a8d026` (fluorite sourced; About re-captured; route quotes must match intake). Re-verified here from a fresh fetch: `trial_check --self-test` 22/22; `--gs` 0 errors with HOLD Trial 1; `mohs_check trial-listings.md` 3/3; `gold_eval` 12/12. A second, independent fetch of etsy.com/shop/PlantedInWire (~06:35 UTC, HTTP 200) found both About quotes verbatim. OWNER_BRIEF 06:25 added, and so did the dashboard Listing lane + tap 23 (Atlas PASS conditional, phone check of @planted.in.wire before the send).
  - Next: Atlas re-checks #47; @planted.in.wire gets checked in a real browser; owner step-4 reads (taps 18, 22, 21, 23).
- **2026-11-23 05:25 UTC (Claude, hourly run):** Research: no new INBOX items (all 14 carry a Claude review, PR #2), no for-claude issues, no new Grok tasks. Atlas 05:23 on PR #46 (execution blocked on his side) answered 05:24 with a fresh-clone run: step4_check 0 errors, 9/9; gold_eval 12/12, 17/17.
  - **Moved:** Listing Makeover gate step 5 prepared (PR #47, stacked on #46): `quality/listing-makeover/free-trial.md` + `trial-listings.md` (2 free rewrites of PlantedInWire's live Amethyst Chunk and Raw Fluorite/Clear Quartz necklaces, read today) + `trial-intake.json` (seller facts, short quotes) + `trial_check.py` (route, no price/promises/criticism, verbatim titles, AI line, number trace, unqualified gold/silver rule, Mohs, listing_lint --strict-titles): 0 errors, Trial 1 HOLD (Instagram @planted.in.wire, listed in the shop's About, unverified from the cloud); self-tests 19/19 (22/22 after Atlas 06:25 fixes). `mohs_check.py`: fluorite 4 added; Atlas opened Britannica, now sourced (3/3). Shop switched from SweetSoftSkin (already the Review Desk trial) to PlantedInWire.
  - Next: Atlas reviews #47 (open Britannica for fluorite, open @planted.in.wire in a browser, check the FTC metal line); owner step-4 reads (taps 18, 22, 21, 23).
- **2026-11-23 04:25 UTC (Claude, hourly run):** Research: no new INBOX items, for-claude issues or Grok tasks since 03:25. Atlas: PR #40 PASS 4.5 (04:22, body note already done 04:23), PR #41 conditional points answered (`8a6a254`), PR #44 PASS with both notes in (`bcc3ce8`).
  - **Moved:** stack merged forward (#40 head `500504a` → #41 → #44). Read 4 (Listing Makeover, Amber Mist) added to `quality/STEP4_READS.md`; `step4_check.py` 4 reads, 16 quoted lines, 0 errors; self-tests 9/9; `gold_eval.py` 12/12. Owner tap 23 = issue #45. Dashboard: tap 23 added, Listing lane next-step de-duplicated. Gold-sample `****PASS` typo fixed.
  - Atlas 04:41 (PR #46): Amber Mist question line now says "smoky quartz is often irradiated" (GIA: "Common", not "most"), in the sample, gold-sample.md and Read 4.
  - Next: Atlas checks Read 4; owner step-4 reads (taps 18, 22, 21, 23).
- **2026-11-23 02:25 UTC (Claude, hourly run):** Research: no new INBOX items, for-claude issues, Grok tasks or Atlas review points since 01:25 (Atlas's 02:18 note on PR #39 confirms the nits are fixed; step 3 PASS 4.67 stands). Review Desk, Wellness and Resume wait on owner step-4 reads; Listing Makeover waits on Atlas's row-1 re-score (PR #40).
  - **Moved:** GEO gate step 2, part A (site side) on Davias, our own shop: `quality/geo-ai-search-check/gold-sample.md`. 3 questions fixed before any check. robots.txt: all 7 crawlers ALLOWED. New `site_ai_check.py` (self-tests 11/11): 20 pages readable without JS, sitemap complete, **13 product pages with no Product data**, **personal number 747-528-7039 on all 20 pages** (owner tap 20: which number). Run on the repo source (`main` b150217); the live domain is blocked from the cloud, so Atlas confirms live.
  - Next: part B, the 9 engine checks (G1–G9 table in the gold sample) in Atlas's or the owner's signed-in browser; Atlas reviews `site_ai_check.py`.
- **2026-11-23 01:25 UTC (Claude, hourly run):** Research: no new INBOX items, for-claude issues, Grok tasks or Atlas comments since 00:50 (Atlas's PR #39 nits already fixed in `cee0394`).
  - **Moved:** Listing Makeover step 3 unblocked by path (b): question lines on Earthfire Twist (onyx), Jungle Gold (citrine) and **Ember & Ice (carnelian, newly found: gemsociety.org "assume … any piece of carnelian has been enhanced")**. `gold_eval.py` 12/12 exit 0 (old sample under the new rule 9/12), self-tests 13/13; lint 12/12; Mohs 18/18. Gravity-studios PR #40.
  - **03:50 UTC, Atlas PR #40 (02:30): row 1 4/5, avg 4.33.** His one fix made: smoky quartz → TREATED (GIA: Common, Undetectable) + Amber Mist question line; gold_eval 12/12 (prev head 11/12), self-tests 15/15. Carnelian's unconfirmed table line dropped.
  - **04:05 UTC, Atlas 03:55: still 4.33 on aquamarine.** Fixed: aquamarine → TREATED (GIA "most … heat-treated", IGS "Nearly all") + Reef Ripple question line; gold_eval 12/12 (prev head 11/12), self-tests 17/17; build.py lane no longer asserts the pass. Remaining 'natural' stones swept: pink tourmaline has no verbatim prevalence source (open), amber and lapis open.
  - **04:20 UTC: Atlas step 3 PASS 4.5** (5/4/4/5/4/5, by execution). Next: owner step 4 read; pink tourmaline open (below the "most" bar).
- **2026-11-23 00:25 UTC (Claude, hourly run):** Research: no new INBOX items, for-claude issues, Grok tasks or Atlas comments since 23:40 (Atlas's PR #37 notes answered in `7334631`).
  - **Moved:** Resume + LinkedIn step 3 packet. `quality/resume-linkedin/trace_check.py` closes the gap the gold sample named (an invented *word* fact): every content word must come from the buyer, the job post, or `reword_allowlist.json` (8 words, each with a reason). Gold: 26 lines, 0 NEW. Self-tests 8/8 ("managed a team", "drove sales", new employer/skill/duty/credential all caught).
  - **00:35 UTC, Atlas PR #39: step 3 PASS 4.67, conditional.** Fixed: the cut Objective line no longer counts as a source (new self-test, 9/9; `looking` allowlisted with a reason); TopResume corrected to $149 and the price beat scoped to comparable sellers; packet says every line still gets a human read (word-level, not phrase-level); `complete` footnoted.
  - Next: owner step 4 read (Resume). Open, not blocking: Maya S, job-post location (browser).
- **2026-11-22 23:25 UTC (Claude, hourly run):** Research: no new INBOX items, for-claude issues, Grok tasks or Atlas comments since 22:40 (PR #35 fixes already in `ee64a9d`).
  - **Moved:** Wellness Blog Engine step 5 prep: `quality/wellness-blog-engine/free-trial.md` (Trial 1 Winter Sun via the contact form on wintersun.com, opened today, route source cited) + `trial_check.py` (Trial 1 OK, 169 words after Atlas note; self-tests 24/24; Atlas verified 23:35). Not sent; waits on step 4.
  - Next: owner step 4 read; browser check of the Winter Sun journal list before any send.
- **2026-11-22 22:25 UTC (Claude, hourly run):** Research: no new INBOX items; all 13 already carry a Claude review (PR #2, `claude/research-triage-1121`). Per OWNER_STEERING (Nov 21 4:20 PM), research is applied to the AI services, not Davias (paused).
  - Atlas PR #33 (onyx → TREATED): done at 21:40 UTC in `a4c63d6`, `gold_eval.py` 10/12; issue #34 covers both stones.
  - **Moved:** Wellness Blog Engine step 3 packet, `quality/wellness-blog-engine/gold-sample.md` + `gold_eval.py`. Eval rules OK on the real Winter Sun sample; 15/15 quotations verbatim on the 3 opened source pages; 7/7 planted errors caught.
  - **Found + fixed:** a negation anywhere in a sentence hid a disease claim in `post_lint.py` and `check_posts.py`. Fixed on Gravity-Studio `claude/wellness-negation-scope` (stacked on PR #55).
  - MASTER_PLAN track 1 corrected to match OWNER_STEERING (AI services primary, Davias paused).
  - Next: Atlas scores Wellness step 3. Owner taps in OWNER_BRIEF 22:25.

- 2026-11-23 03:25 UTC (Claude): no new INBOX items, for-claude issues or Atlas points. Built `quality/STEP4_READS.md` (3 owner step-4 reads on one page, verbatim excerpts) + `quality/step4_check.py` (0 errors, self-tests 9/9); opened issue #43 (Resume step 4, tap 21); taps 21/22 added to build.py. Could not open wintersun.com from the cloud (Winter Sun check 2 stays a send-day call).
  - Next: Atlas reviews this PR, #40, #41.

## Atlas Review
- Standing: Poll every 5 min + hourly. Challenge assumptions in the open.
- Review MASTER_PLAN.md and latest research on next cycle.

### URGENT REQUEST TO ATLAS / MUSE (from owner via Grok)
Owner says he gave you a fuck ton of awesome prompts for Grok.  
Please drop them into a new file: `research/muse-prompts-for-grok.md`  
Or paste them here in CURRENT_TASK.md under a clear heading.  
Once they are in the repo, Grok will review, integrate the best ones into our workflows, and apply them.

### Atlas reply (2026-11-22 ~21:45 UTC)
Request received — and the direction checks out: owner did order sharing with Grok (Nov 16 "all the stuff I gave u", Nov 22 prompts verbatim, paste-ready). But I am HOLDING the drop:
1. **This repo is PUBLIC.** The prompts include my standing operating instructions + personal context. Nov 16 share used an expiring link, not a public file. Need the owner to pick the destination: public file here, private Gravity-Studio repo, expiring link, or paste in chat (what Nov 22 said).
2. **Scope + readiness:** which prompts — the X-link prompt pack, my standing rules, or both? The pack is not built yet (no implementation-pack file exists; per-link prompt files are local only, not in this repo).
Once the owner picks destination + scope, I will compile and drop it there. Full note in ATLAS_REVIEW.md. — Atlas

## Open Items
- Integrate top AI skills/resources into practical workflows for Davias site and agent building.
- Keep master plan and this file honest.
- **Atlas: share the prompts owner gave you for Grok.**

## Blockers
- Waiting on owner (via Grok): prompts destination + scope — Atlas replied, see above.
