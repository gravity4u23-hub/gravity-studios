# CURRENT TASK — Gravity Studios

**Last updated:** 2026-11-22 by Grok, Atlas reply 21:45 UTC

## Grok Status
- Back online.
- Standing order: When owner sends X links/videos/texts, immediately transcribe/summarize into `research/`, update `research/INBOX.md`, and note here.
- Latest processed: cyrilxbt Amodei advice + Stanford lecture notes.

## Claude Progress
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
