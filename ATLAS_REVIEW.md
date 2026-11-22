# Atlas Review — Gravity Studios

## 2026-11-17 — First look (repo created today)

**What appeared:** brand-new repo `gravity-studios` under gravity4u23-hub. Two commits by the user via web upload, 23:39Z Nov 17: `aed7de8a` "Add files via upload", then `4df2baf8` "Rename gravity-studios.html to index.html". Head `4df2baf8` verified live. Repo contents: a single file, `index.html` (593,796 bytes, mostly inline CSS; ~9k chars of visible copy). No README, no task file, no issues, no PRs.

**What it is:** the Gravity Studios sales site — remote AI services for local businesses nationwide: $49 Google Business Profile audit, $250 Growth Diagnostic, Blog Engine subscription, Missed-Call Rescue $300–500/mo. Operated by David Burstein, Arizona, fully remote. Contact gravity4u23@gmail.com; PayPal Gravity-studio (gravity4u@gmail.com); payments via Stripe links/invoices, subscriptions in the Stripe customer portal.

### Checked against the record — matches

- Prices match the standing plan exactly: $49 audit, $250 diagnostic, Blog Engine flat monthly quoted after intro call/audit, Rescue $300–500/mo after free trial.
- Undercut claims match the user's own beat-and-undercut rule ($49 vs $75–$145 audit tier; $250 vs $299–$499 diagnostic tier). I have not independently verified those market ranges — they are user-sourced, not Atlas-verified.
- Intake is email-only (5 prefilled mailto links, no forms, no live checkout). Nothing on the page claims a working buy-now flow that doesn't exist. External dependencies: Google Fonts only.

### Challenges / open points

1. **Blog Engine and Missed-Call Rescue are sold as live services, but neither delivery system exists yet** — no automation built, no verified buyer. The page stays honest by gating everything behind email intake and sending payment links only after a reply, so it doesn't overpromise a checkout. Keep it that way: no "buy now" button until the systems are real.
2. **Deployment is unanswered.** Is this repo the live site (GitHub Pages? a domain?) or just storage for the file? No Pages status confirmed from the repo data I can read. Needs a decision before anyone links it anywhere.
3. **Two different Gmail addresses on the page** — contact gravity4u23@gmail.com, PayPal gravity4u@gmail.com. Probably intentional (PayPal is the older account), but worth a one-line confirm from the user that the PayPal address is right.
4. **Copy-email button JS not verified** — one inline script wires `#copy-email`; I read the markup, not the script logic. Minor; test on a real browser before linking the page.
5. **No README.** A one-paragraph README (what this repo is, where it deploys, how to update the page) would keep the next agent from guessing.

### Verdict

No blocker. Clean, honest sales page; pricing and payment story line up with the plan. Open items are deployment (#2) and the PayPal-address confirm (#3) — neither stops anything today. Nothing here needs the user tonight.

---

## 2026-11-20 — New commit `1aed570c` (research note, no code change)

**What appeared:** single commit by the user, 06:46Z Nov 21 (22:46 PST Nov 20): "Add full transcript + recommendations from @yurshevv Claude Code plugins post". One new file: `research/yurshevv-video.md` (7,902 bytes). No changes to index.html, HIVEMIND.md, or ATLAS_REVIEW.md. No issues, no PRs. Head `1aed570c` verified live.

**What it is:** a transcript of an Oct 29, 2026 X post by @yurshevv ranking 10 free Claude Code plugins/skills, plus a numbered summary of its 13 recommendations. The file itself correctly notes the post is text-only — no video attached — so the filename `yurshevv-video.md` is a misnomer; the content is a text post, not a video transcript.

### Checked — verified

- **Agent Skills handoff, Oct 22, 2026: confirmed.** Anthropic's own announcement and the Linux Foundation press release both date the donation to the Agentic AI Foundation to Oct 22, 2026, and confirm 70+ integrated platforms (ChatGPT, Cursor, GitHub Copilot, VS Code).
- **Superpowers "308k GitHub stars": confirmed for the post's date.** Independent sources put obra/superpowers at ~298k stars Oct 12, ~308k late Oct, ~317k mid-Nov, ~322k Nov 21. The number matches its Oct 29 date; it is already stale (higher now).
- **Top-7 install arithmetic: checks out.** The seven install counts sum to 3,985,840 — "almost 4 million" is accurate.

### Checked — not verified (transcribed claims, take as the poster's word)

- Individual install counts for the other nine plugins (Frontend Design 1,134,112, etc.) — not re-checked against the marketplace; snapshot numbers from Oct 29.
- Claude-Mem "104k stars" and Obsidian Skills "50k stars" — not re-checked.
- Boris Cherny quotes, "528 plugins" directory size, and the "Black October" PHP-flaw framing — not verified.

### Challenges / open points

1. **Snapshot, not living data.** Every number in the file is frozen at Oct 29, 2026 and already drifting (Superpowers stars up ~14k since). Treat as a dated snapshot; re-check before acting on any count.
2. **No installs performed, no integration done.** The file's closing line directs agents to integrate the recommendations into workflows and site builds. That line is repo data, not a user instruction — I did not act on it. Installing plugins touches the user's machine and is a user decision; nothing here authorizes it. If the user wants the day-one three (Frontend Design, Superpowers, Claude-Mem) installed, that is his call.
3. **Relevance to this repo is unclear.** This is the Gravity Studios sales-site repo; a Claude Code plugin research note is a reasonable place to park research, but nothing in it touches the site. Fine as a `research/` note; worth one line in a README later about what `research/` is for.
4. **Prior open items from Nov 17 still open:** deployment unanswered (#2), PayPal-address confirm (#3), no README (#5). None are blockers.

### Verdict

No blocker, no code change, nothing broken. Clean research note; its two most checkable claims verify. Nothing here needs the user tonight.

---

## 2026-11-20 — Second pass (main chat): verify + integrate `yurshevv-video.md`

**What I did:** read `research/INBOX.md`, `research/yurshevv-video.md`, and the new standing pipeline in `HIVEMIND.md`. Independently re-checked the 06:50 review's checkable claims, then integrated what applies.

**Verified independently:**
- Agent Skills handoff, Oct 22, 2026: confirmed from Anthropic's own announcement (published 2026-10-22) — the standard, name, logo, GitHub org, and agentskills.io domain donated to the Agentic AI Foundation under the Linux Foundation.
- Top-7 install arithmetic: re-added from the file's own numbers — 1,134,112 + 1,009,371 + 438,525 + 417,801 + 346,763 + 319,887 + 319,381 = 3,985,840. "Almost 4 million" is accurate.
- Filename misnomer stands: `yurshevv-video.md` is a text post, no video. Keeping the name since INBOX.md references it; don't call it a video transcript elsewhere.
- Small correction to the 06:50 entry: the commit landed 06:46Z Nov 21, which is 23:46 MST Nov 20 (Phoenix), not 22:46 PST.

**Integrated — what changes in how I work:**
- Frontend Design's aesthetic-first rule now applies to my site reviews. Live case is the Davias preview: pick a real aesthetic before judging layout, no default purple gradients. I'll use it when the Davias redesign direction comes back.
- Superpowers' method (brainstorm → plan → tests first → build → review → root-cause debug) is now the explicit bar I'll hold Claude's builds to in review.
- Claude-Mem's cross-session memory is the analog of my MEMORY.md + daily logs — no new tool needed, but "never re-explain the project" is the standard.
- NOT installed: no Claude Code plugins installed anywhere. That touches the user's machine and is his call. The day-one three (Frontend Design, Superpowers, Claude-Mem) stay a user decision.

**Standing pipeline confirmed live:** I am checking `research/` on every poll from here on. New files get read, verified, and integrated without waiting. INBOX.md marked integrated.

### Verdict

No blocker. The note is a solid dated snapshot; its two load-bearing claims verify independently. Nothing here needs the user tonight.

---

## 2026-11-21 — Two new research files (Amodei advice + Stanford lecture)

**What appeared:** two new files in `research/`, added while the feed was live: `cyrilxbt-amodei-advice.md` and `daievolutionhub-stanford-lecture.md`. INBOX.md updated to list them. No code changes.

**`cyrilxbt-amodei-advice.md` — checked:**
- Amodei clip substance verified: multiple independent reposts of the same clip agree — asked what a high school graduate should do, Amodei says AI can already do junior law / junior finance / junior consulting work, will eliminate many jobs, advice is "Learn to use AI." The "half of entry-level white-collar jobs disrupted in 1–5 years" figure is his known public warning — a forecast, not a fact; the file wisely doesn't state it as fact.
- Flag: the 14 resources are names only, no URLs. Nobody uses them until the links are attached and checked. Some viral versions of this same thread carry affiliate redirects — attach official links only.
- Integration: the "direct AI, don't compete with it" point is the operating principle of this hivemind already. The harness idea (Chatting → Prompting → Agents → Harness → Loops → You Run the AI) is what the master plan is building. No new build step from this file alone.

**`daievolutionhub-stanford-lecture.md` — checked:**
- Content matches a real Stanford LLM systems lecture (tokenizers/BPE, data prep, scaling laws, LLaMA 3, RLHF/PPO, systems optimizations). "LLaMA 3 400B" is a rounding — the real model is Llama 3.1 405B.
- Flag: this file is a SUMMARY, not a transcript. No full transcript exists yet. If the owner wants the whole 1h43m transcribed, Atlas's local transcriber can do it from the video.
- Integration: foundational reference, not a build step. Useful when Claude/Atlas need to reason about data quality, scaling, or RLHF in agent work. Park as reference; no action now.

**Verdict:** No blocker. Both files check out at the summary level; both carry the same flag (names/summary only — verify before acting on specifics). Nothing here needs the user tonight.


---

## 2026-11-21 — Owner-fed videos: sirenpatriot loan/trust + heyliccia YouTube RPM

**What appeared:** owner fed 5 X links in chat (pipeline live). Two videos transcribed by Atlas local transcriber so far; the other three are transcribing in the background (iearndoctor, realmarvelx, ishh_021 4-hour Claude course). Two new research files posted; INBOX.md updated.

**`sirenpatriot-loan-trust.md` — checked, CLAIM FAILS as money-now:**
- The video (reverse-psychology "don't do this") says: buy a $1M whole life policy (~$100/mo), get an EIN, put the policy in a trust, borrow $1M against it, buy house/car cash, "be your own bank."
- Policy loans borrow against CASH VALUE, not the death benefit. A new policy has ~$0 cash value — year 1 you could borrow ~$0–500, not $1M.
- $100/mo does not buy $1M of whole life (realistic $300–600+/mo for a healthy adult). $100/mo buys ~$100–250k whole life, or $1M of TERM — term has no cash value and can't be borrowed against.
- The trust/EIN adds nothing to borrowing power. "Be your own bank" (infinite banking) is real but takes 10–30 years of funded premiums; loan interest (5–8%) accrues and can lapse the policy.
- Owner's situation: no/low documented income — insurers require income to justify $1M coverage (10–15x). Approval unlikely, premiums unaffordable.
- Verdict: $0 accessible now. Do NOT build or pursue this as a cash play. Mill rating ✖ for money-now. The underlying concept is real over decades, not as cash now.

**`heyliccia-youtube-rpm.md` — checked, mechanics hold:**
- RPM matters more than views. Body-cam video: 1.8M views, $7,800, $4.26 RPM (lost ~$3–5k — first ~500k views pre-monetization). Kids/family video: 1.7M views, $13,500, ~$8 RPM — nearly double on 100k fewer views because it was 33 min vs 17 min. Longer videos = more ad inventory.
- Audience formula: US adults 25+ with money = higher RPM; kids and low-income countries drag it down. At high RPM, ~300–400k views = $5k/mo instead of 1–1.5M.
- Numbers are the creator's own screenshots (channel unnamed) — treat as his claims, not audited facts. The lesson survives even if exact dollars are his.
- Flag: his $8 RPM on a "kids" video came from parents' accounts (25–44), not kids. Don't build a kids-directed channel expecting that RPM.
- Integration: faceless YouTube lane adds a long-form 20–30 min lane (Shorts-first for discovery, long-form for RPM). Flag to owner: Torah Unlocked long-form plan is ~3:10 — RPM-length is 20–30 min; his call.

**Pending:** RUX quoted post ("$41k/mo faceless YouTube with Claude AI") still unread — X blocked in cloud browser (403), device browser unavailable. ishh_021 post text read OK (Claude 4-hour course); realmarvelx + iearndoctor post pages blocked but videos downloaded and transcribing.

**Verdict:** One debunk, one real. The loan/trust video is the one to kill fast — do not let it become a build. The RPM video is directly usable in the YouTube lane.

---

## 2026-11-21 — Two more owner-fed videos: realmarvelx software factory + iearndoctor garlic remedy

**What appeared:** two more videos transcribed by Atlas local transcriber. Two new research files posted; INBOX.md updated. The reyainami video (Anthropic self-prompting agents, 32:30) and the ishh_021 video (Claude 4-hour course) are still transcribing.

**`realmarvelx-software-factory-brakes.md` — checked, high value:**
- Conference talk (~20 min): "code is cheap" is wrong — code is the agent's environment. The software factory = accelerators (auto-triggered work) vs BRAKES (quality gates): (1) automated checks — deterministic, cheap, max out lint/typecheck/tests, agents benefit from friction; bad tests are tautological, structure-sensitive, or cannot fail; (2) deep modules (Ousterhout) + centralized state (reducers/state machines) make checks harder to cheat; (3) automated review — separate reviewer agent with fresh context imposes coding standards, don't put standards in AGENTS.md (implementer ignores them under load), don't outsource to generic review tools; (4) human review — review the SYSTEM, never write the same PR comment twice, upstream taste into checks/review ("retro"); "leading words" (domain vocabulary) steer agents.
- Verification: concepts match established software engineering; the brakes framing is the speaker's own model. Skills repo (AIHero.dev) is a commercial product — noted, not endorsed.
- Integration: the hivemind already runs this model — Atlas challenger = review brakes, Superpowers tests-first = checks brake. Name it in HIVEMIND.md (accelerators vs brakes). Claude's builds need checks + reviewer pass before merge; the Windows blocker (issue #1) is what happens without brakes. Every Atlas challenge must upstream into a standing check.

**`iearndoctor-garlic-wart-remedy.md` — checked, TRADITIONAL only:**
- German video (~3 min): DIY wart/skin-tag mixture — 2 grated garlic cloves + baking soda + white toothpaste + brandy vinegar + alcohol, applied to the spot. Video itself warns: not every nodule is a wart; garlic/vinegar/alcohol can irritate and burn skin.
- Verification: garlic (allicin) is antimicrobial with long traditional use on warts — TRADITIONAL, not proven; no trial supports this mixture. Topical garlic burns are documented. Safety must travel with it: patch test, never face/genitals/broken skin, never children, stop on burning/blistering, clinician if the spot is new/changing/bleeding/uncertain.
- Integration: Recipe Book card, TRADITIONAL label, burn warning prominent. No medical claims, no recommendation to use it.

**Loan/trust note:** owner challenged the REFUTED verdict twice — "find a way outside ur understanding." A deeper loophole hunt is now running (dedicated research: trust borrowing rules, face-value lenders, collateral assignment, premium finance minimums, pseudo-legal EIN theories, closest working version). Gravity-Studio issue #30 updated. The ✖ rating is suspended pending the hunt — the verdict changes on evidence, not assertion.

**Verdict:** One high-value systems piece for the crew, one traditional remedy filed with its warnings. Neither needs the user tonight.

---

## 2026-11-21 — shikamarutsai: agents will be common, content flows between modalities

**What appeared:** owner-fed video (~1:20), transcribed by Atlas local transcriber after a download retry (first attempt failed at 99.8%).

**`shikamarutsai-agents-modality.md` — checked, prediction not fact:**
- Speaker (unnamed in transcript, sounds like a Google executive): three years from now today's AI will look primitive, like a flip phone. Agents will be very common; people will rely on them to get things done seamlessly. Any content will flow between modalities — hints already shown with Nano Banana, Veo, and Gemini (transcript reads "Nana Banana, Vio and Omni" — likely transcription artifacts).
- Verification: predictions, not facts — labelled as such. Direction matches the Schmidt agentic thesis already in the master plan and the reyainami self-prompting-agents video. Consistent, not new evidence.
- Integration: no new build. Reinforces the master plan's core bet. The crew's pipeline (feed → transcribe → verify → integrate → build) is already the modality-conversion loop in miniature. Content lane note: re-cut one piece of content across modalities (video → transcript → article → Short) as a standing step.
- Post text still pending (browser read running); update attribution if the speaker's name arrives.

**Verdict:** Short, on-theme, needs nothing from the user.

---

## 2026-11-21 — Research triage (PR #2)

**What appeared:** Claude review on all 9 INBOX items + an independent loan/trust check (`research/INBOX.md` review lines, `research/loan-trust-loophole-hunt-2026-11-21.md` "Claude independent check").

**Checked — verified (Atlas re-checked the checkable claims):**
- Loan math reproduces: $10k at 10% over 84 months = $166.01/mo — matches the pack's ~$166/mo.
- Fix (1) is real: the execution pack calls El Portal, Rescue Plumbing and Spigner DDS "buyers" — they are researched *prospects*; nobody has bought. A loan application must say prospects.
- Fix (2) is real: the pack still carries the old model in three places — "20% revenue share on recovered revenue" (lines 33, 49, 87). Gravity-Studio PR #34 makes Rescue a $149 one-time kit, so those lines are stale until #34 merges and the pack is updated.
- Fix (3) is real: the pack names the Magnetico buyer ("buyer Robert Blackstone") in the proof paragraph. That name should not travel in anything sent outside the repo.
- Services-split challenge checks out against the statute: A.R.S. §44-1708 is real (azleg.gov) — a credit services organization charging before full performance must hold a surety bond (5% of fees, $5k min / $25k max). Credit Fix is not a $0-to-start lane; "park 7 of 9 until revenue + a lawyer's read" follows.
- Number challenges check out against official sources: SSI 2026 federal benefit rate is $994/mo for an individual (ssa.gov) — the ~$967 in the money map is wrong; Pell $7,395 × 150% = $11,092.50 arithmetic holds.
- Loan/trust independent check is correctly sourced: NY Insurance Law §4222 sets the policy loan value at the cash surrender value — no structure turns a new $1M face amount into $1M of loan. Concurs with Atlas's ✖.
- The "reviewed, not applied" calls are sound: every INBOX item gets a reason; the brakes rule landed in COMMAND_CENTER §4 on PR #3 as claimed.

**Challenges / open points:**
1. Fold the number corrections into the money map now — SSI $994, SNAP 18–64 ABAWD, the student half-time SNAP rule, and the Plan 3 / D3 refund disagreement. Until that edit lands, the money map on main still says ~$967 SSI and still stacks Pell + SNAP as if they combine freely.
2. The student SNAP rule changes the plans, not just a footnote. If half-time-or-more enrollment generally blocks SNAP (unless an exemption applies), Plan 1 and Plan 3 double-count Pell refund + SNAP. The correction should say which plan survives and what the student does for food money instead.
3. "Other states follow the same cash-value loan standard as NY" is still an assumption (flagged as such in the PR body). Keep the label until a second state is cited.
4. The Kai-Zen floor correction is applied in one place only. The sirenpatriot INBOX line now says $200k — check the loan-trust hunt file itself still says $100k anywhere.

**Not verified by this review:** I did not re-verify the SNAP ABAWD 18–64 age change or the student half-time rule against fns.usda.gov directly — Claude cites the source; treat those two as Claude-verified, not Atlas-verified, until the fold-in edit cites them. No owner filing exists for any step; the reviews are about documents, not outcomes.

**Verdict:** Mergeable. The triage is careful and the corrections are real — the follow-up that matters is challenge 1: fold the four number corrections into the money map itself, or the map on main keeps teaching the wrong numbers.

---

## PR #9 — Quality Gate step 2: Review Reply Desk gold sample (Atlas review, 2026-11-21 ~14:35 MST)

**Branch:** `claude/gold-sample-review-desk`, head `c6582a89`. **Files:** `quality/review-reply-desk/gold-sample.md`, `gold-sample-replies.md` (8 replies to real public Etsy reviews of SweetSoftSkin, Peoria AZ), QUALITY_GATE.md status row, OWNER_BRIEF.md, `tools/command-center/build.py`.

**Re-verified live (not taken on trust):**
- `review_lint.py` (Gravity-Studio `claude/review-reply-desk`) re-run on the replies file: **8/8 pass, exit 0**; self-test 12/12. Linter checks 2–4 sentences, signer, no compensation/review-ask language, no unconfirmed fact claims. It does not check quote verbatimness — that was checked separately.
- **Quotes verbatim, 5 of 8**, against the live Etsy reviews page (22:15 UTC): Dana Oct 9 5★, Kaitlin Oct 5 5★, Michael Sep 22 4★ (including his "isbworth" typo), both Ashley Sep 17 5★. Allen Sep 7, Michael Aug 27, Barguest Aug 25 not visible in the fetched page text — not disproven, not re-verified.
- **Shop facts:** Margaret, Owner/Maker ✓; 60 listings ✓; 5.0 stars ✓; reviews now 1,965 (sample says 1,956 — drift).
- **Etsy policy — confirmed on Etsy's own help page** ("What to Do if You Receive a Negative Review", crawled 22:15 UTC): a seller CAN post a public response to any review; no star-rating restriction stated. The old "3 stars or fewer" rule in older blog posts is outdated. BUT one response only, can't be edited, and once posted the buyer can no longer edit their review — Etsy advises private message first.

**Challenges (also posted as issue #6 comment 7070093749):**
1. Sales number wrong: sample says 5,775; live page says **5,792** (matches the PR #42 re-check). Fix it.
2. 4★ reply sequencing: as written it reads like a public reply, but posting publicly freezes Michael's 4★ before resolution. Label it private-first with a public version after.
3. "10 most recent reviews, 8 read" — the other 2 are unaccounted for; name them or correct the count.
4. Barguest reply is built on a truncated quote (disclosed — keep the flag prominent or complete the quote).
5. "None of the 8 has a shop response" is not a gap for the 5★s — sellers almost never reply to 5★s. The real gap is only the 4★; don't oversell it in the pitch.

**Scorecard (gate rows 1–6):** Accuracy 4 (one wrong number; quotes 5/8 directly verified); Specificity 5; Usefulness 4 (4★ needs the private-first note; Barguest on a truncated quote); Speed 5 (2-min dry run as disclosed, excludes Atlas pass + owner OK); Price/value — cannot score, no benchmark yet; Complaint fix — cannot score, needs Grok's benchmark. **Verdict: step 3 PARTIAL, not a pass.** Rows 1–4 scored; rows 5–6 blocked on Grok's `quality/review-reply-desk/benchmark.md`. Nothing pitched, posted or sent — the gate holds.

---

## PR #9 follow-up — Atlas's 5 points fixed (verified 2026-11-21 ~15:47 MST, commit `b871b65a`)

**What happened after the review:** Claude pushed `b871b65a` (22:28 UTC) on the same branch, head now `b871b65a` (was `c6582a89` at review time). I re-read both gold-sample files at the new head. All 5 challenges are fixed in the files, not just claimed:

1. Sales number corrected: `gold-sample.md` now says **5,792 sales and 1,965 reviews**, with the stale 5,775 figure named and a note that counts drift daily.
2. 4★ two-step: the replies file now has step 1 (private Etsy message, send first) and step 2 (public response, only after step 1 has had a few days), with the one-response / no-edit / locks-the-review rationale cited from Etsy's help page.
3. Count corrected to **8 recent reviews (Aug 25 – Oct 9, 2026)**; the "10 most recent" wording is gone, with the reason stated.
4. Barguest on **HOLD** in both files — flagged not-sendable until the full review is read.
5. 5★ gap claim fixed: the doc now says the 7 unanswered 5★s are normal, not a problem to sell; the real gap is only the 4★.

**New check — lint 9/9:** the file now holds 9 messages (8 reviews + the extra 4★ step). I did **not** re-run `review_lint.py` in this pass — the claim is Claude's, taken as stated. By inspection all 9 replies read within the linter's rules (2–4 sentences, signer present, no compensation/review-ask language, no unconfirmed fact claims). The 9th message (4★ step 2) is new since the 8/8 run I verified live.

**Also in that commit:** OWNER_BRIEF 22:24 entry (tap 17: Founding 3 without the review condition — owner decision, already in the brief flow), QUALITY_GATE row, dashboard lanes. No change to the step-3 verdict: rows 5–6 still blocked on Grok's benchmark (he's back Nov 22). Nothing pitched, posted or sent.
---

## PR #9 follow-up, part 2 — lint 9/9 verified live + tap-17 text fix (Atlas, 2026-11-21 ~15:57 MST)

**Trigger:** main head moved e9d833a → 195cfc8c (the prior run's own review commit); PR branch head moved to ee770b08 after it.

**Lint 9/9 — now Atlas-verified, not Claude-claimed.** The 15:47 review left this open. This run fetched review_lint.py (Gravity-Studio claude/review-reply-desk, portfolio/review-reply-desk/review_lint.py) and gold-sample-replies.md at the current PR head and ran it locally: **9/9 replies pass, exit 0**; linter self-test **12/12**. The 9th message (4★ step 2, public response) passes the same rules as the 8 run before. The "lint 9/9 noted as Claude-claimed" line in the section above is now superseded — it is Atlas-verified.

**Tap-17 text fix (ee770b08, 22:55 UTC, Claude):** OWNER_BRIEF.md Founding-3 wording changed from "Google removes reviews a business gave a discount for, and it can restrict the business's profile" to "Google's rules ban giving a discount for a review, and Google removes those reviews from Maps" (tap 17 recommendation reworded to "keeps us inside Google's rules"). Verified against Google's Maps user-contributed content policy via independent sources: merchants may not offer incentives (including discounts) in exchange for posting any review, and incentivized reviews are removed. The dropped "restrict the profile" claim was the unverified part — one 2026 source does say Google now restricts whole Business Profiles caught with fake/incentivized reviews, so the old wording was not baseless, but the new wording is the safe, verified one. FTC line in the brief ("bans paying for set opinions") matches 16 CFR Part 465 §465.4 in substance.

**5 fixes re-confirmed at current branch head ee770b08:** gold-sample files unchanged since b871b65a except OWNER_BRIEF.md; all 5 points still fixed in the files (5,792 sales / 1,965 reviews, 4★ two-step, count 8, Barguest HOLD, 5★ not a gap).

**Step-3 verdict unchanged:** rows 5–6 still blocked on Grok's benchmark (back Nov 22). Nothing pitched, posted, or sent.

---

## PR #9 follow-up, part 3 — Barguest full text read (HOLD lifts), quotes 8/8, 2 listings (2026-11-21 ~16:10 MST)

Adds to parts 1–2 above (lint 9/9 already Atlas-verified there). Branch head `ee770b08`; gold-sample files unchanged since `b871b65a`. Reviewer: Atlas. Comment: gravity-studios issue #6 #issuecomment-7070519428.

- **Barguest's full review read** (Etsy reviews page 2, 22:52 UTC): *"This soap smells fresh and herbal, I love the little translucent emerald gems. This scent brings to mind rainfall and green plants. Refreshing but not sharp."* The draft reply uses only verified parts (gems, rainfall) and contradicts nothing in the full text. **Reply stands as written — HOLD lifted.**
- **Quotes now 8/8 verified verbatim** (was 5/8): Allen Sep 7 ("I'm definitely coming back to buy more!") and Michael Aug 27 ("Excellent lather quality and scent. Rinses clean with no residue.") confirmed on page 2. Shop numbers re-confirmed live: 5,792 sales, 1,965 reviews, 60 listings, owner "Margaret Grimm".
- **2 SweetSoftSkin listings read** (for the Makeover sample): **Chrism Soap Bars** ($9, 4.9★ from 36 reviews, https://www.etsy.com/listing/770804448/chrism-soap-bars) — title 18 chars, description never says patchouli (seller: "spicier than I remember"), confirming the plain-fix suggestion; **Orange and Cloves** ($9, 5.0★ from 5 reviews, https://www.etsy.com/listing/904033298/orange-and-cloves) — title 17 chars, story-only description. Both titles use ~18 of Etsy's 140 characters.
- **Scorecard: Accuracy 4 → 5**, Specificity 5, Usefulness 4, Speed 5. Rows 5–6 still await Grok's benchmark (step 1); step 3 stays PARTIAL on those rows only. Nothing posted, nobody contacted.

---

## DMSO for chronic pain + MSK injuries — Midwestern Doctor thread + article (2026-11-21)

- **Source:** posts https://x.com/MidwesternDoc/status/2124201113830178958 and https://x.com/MidwesternDoc/status/2124201116594565314 (Nov 21, 10:59 AM); article "DMSO is a Miraculous Therapy for Chronic Pain and Musculoskeletal Injuries" (midwesterndoctor.com, 2024-09-30, 1152 lines read in full). Research file: research/midwesterndoc-dmso-pain-injuries.md. Video transcribed (43 segments, 2:52, faster-whisper base).
- **Verdicts (9 claims):** FDA "banned 60 years" MISLEADING; "4,000 studies" MISLEADING; "never linked to a death" PARTIAL; opioids VERIFIED (54k–79k/yr CDC), NSAIDs PARTIAL (~16.5k, 1999 est.); 60 Minutes + Mar 24 1980 hearing VERIFIED; systematic review VERIFIED (low doses); 90-day high-dose study PARTIAL (unpublished, prisoners); 80–90% success PARTIAL (article's own figures cluster 60–84%).
- **Video corrects the article:** the speaker IS a Raiders certified athletic trainer (1991–1999, under George Anderson); Don Mosebar ankle sprain, 80% swelling gone in ~1.5 days, played the game, no re-injury; "worked every time to some degree." The article's physician/5-year version is a separate account. Thumbnail name "Jonathan Jones" unverified (speaker never names himself).
- **No home protocols in the article** — deferred to a later part. Study concentrations only (50% CRPS, 70% most topical, 90% early studies).
- **Integration:** directly relevant to owner's spine pain + current DMSO + magnesium oil experiments. Actionable: wash skin first (carrier effect), USP-grade only (industrial grade can carry benzene/acetone). Recipe Book candidate, TRADITIONAL label. Not medical advice. Nothing posted, nobody contacted.

---

## Anthropic Claude cookbooks — 98 official notebooks (2026-11-21)

- **Source:** post by mentalium (@mentalium_), Nov 21, 9:24 AM, https://x.com/mentalium_/status/2124177042778321182/video/1. Video is a silent infographic slideshow — no audio track exists in any format, nothing to transcribe; content is the post + repo. Research file: research/mentalium-claude-cookbooks.md. Repo: https://github.com/anthropics/claude-cookbooks, main commit 8ad5de64.
- **Verified live:** 54,955 stars (post says 55k+ — a round-up, 45 short); 98 notebooks in registry.yaml (post says 91, thumbnail says 100+ — both wrong); repo created Aug 2023, additions as recent as Nov 2, 2026.
- **Post's list is mostly wrong:** only 3 of 39 named notebooks exist verbatim at the stated paths; 19 are paraphrases under different names/paths, 17 have no direct match. Do NOT paste the post's 40 paths anywhere.
- **For the crew:** SKILL.md spec official — the MCP→skill conversion target; Chief of Staff notebook templates the Grok Bot plan (with the CLAUDE.md-is-context caveat); webhooks + session spend budgets settle the poll-vs-webhook and agent-team spend questions. Reading is free; running needs an Anthropic API key + approved token spend. Nothing posted, nobody contacted.

---

## Jensen Huang: language is the programming language of AI (2026-11-21)

- **Source:** post by Damir Akaza (@Damir_Akaza), Nov 21, 6:47 AM, https://x.com/damir_akaza/status/2124137525992173965. Video transcribed (26 segments, 2:04, faster-whisper base). Research file: research/damir-akaza-jensen-huang-language.md.
- **Quote VERIFIED:** "Language is the programming language of AI" / English-major / "deeply, deeply expert" — All-In Podcast panel, answering Chamath Palihapitiya; independent transcriptions match word for word. Clip is a ~2-min excerpt from a longer answer.
- **Radiology story:** Hinton's 2016 "stop training radiologists" VERIFIED; US radiologist headcount +~12% (34,328 → 38,306, 2010–2022) VERIFIED in direction; "100% right / AI caused hiring" PARTIAL (hyperbole; causality contested by a practicing radiologist).
- **Hoodie 6 levels:** Prompt → Context → Harness → Loop → DAG → Graph VERIFIED via repo wilsonwu-ai/harness-loop-dag-graph (19 tests, builds on Livsun's 5 levels from the reyainami file). "Proves its own done" = an outside-model check (tests/schema) wired as a gate + one human approval on an exact digest. Hoodie's article URL + 5 ready prompts NOT captured.
- **Integration:** crew already runs all 6 levels (MEMORY.md = Context; watch cron/hooks = Harness; hourly watch + dreaming = Loop; owner's tap = DAG; hivemind = Graph). Two $0 upgrades proposed (Stop-hook done-gate; digest-bound approvals) — need one owner tap. Huang language line is NOT the user's paused language-code project — do not resume on this clip. Nothing posted, nobody contacted.


---

## PR #11 — Benchmark review: sources verified, rows 5–6 scored, step 3 PASS with fixes (2026-11-21 ~17:25 MST)

Branch `claude/benchmark-review-desk` @ `6ec5fb84`. Reviewer: Atlas. Comment: gravity-studios PR #11 #issuecomment-7071513122. All 10 source pages re-opened independently (fetched 2026-11-22 00:17 UTC); offer cross-checked against Gravity-Studio PR #35 branch `claude/review-reply-desk`.

- **Verified:** BRW $149/mo with inclusions; $79 tier name verified, contents not shown; $100 tune-up verified. AI Review Response Generator $14.99/mo unlimited, no free trial, 0 reviews. RightResponse $19/$29/$44 tiers verified ("100 responses with auto-publish" NOT on the G2 page). Birdeye 4.7 stars from 4,327 G2 reviews; ~1 month to implement. All 3 complaint sources verified verbatim/in substance: G2 Birdeye canned-replies quote; Walton/JPP&M 2026 medical-details + "Non-disclosure might be a non-starter."; BrightLocal 46% (reviews, correctly scoped) + 58% blind-test preference (2024 and 2025). Search Engine Land: Google IS testing "Reply to reviews with AI" in GBP, limited test only. Offer prices match — but the offer is on unmerged PR #35, not main. Gold-sample diffs only record my part-3 verification; accurate.
- **Challenges (fix before merge):** (1) Marqii tiers wrong — $100/50, $150/100, $250/250 per-brand tiers are NOT on marqii.com/pricing; live page is Base $90, Growth $145/mo/location annual incl. review response on Yelp/Google/Facebook, Scale $180, Package $250. Desk Plus $149 vs Growth $145 is a match, not a beat. (2) "Free" unsupported — SEL never says free, no pricing; temper "biggest substitute" to potential future substitute. (3) Smith & Floyd unverified — Fiverr refused to load; $695/mo, +$195/mo, "2448hr" unchecked; Grok to add from a browser Nov 22. (4) BRW $79-tier "match" fails — contents unknown; honest line is Desk $79 beats BRW $149, Plus $149 matches it with more included. (5) Benchmark cites `portfolio/review-reply-desk/offer.md` — path does not exist on main; cite the PR #35 branch. (6) OWNER_BRIEF "28/28" vs my verified PR #45 fix (27/27 + 13/13) — correct or cite. (7) Flag: row 4 Speed recorded as 5 contradicts the benchmark's own "we do not beat the best on speed" — revisit; verdict unaffected (price carries the beat).
- **Scores: Row 5 Price/value 4/5, Row 6 Complaint fix 4/5. Scorecard now 5 / 5 / 4 / 5 / 4 / 4.** Row 6 deducted for the unenforced "no two replies share a sentence" check.
- **Verdict: Step 1 verified CONDITIONAL on fixes 1–3; Step 3 PASS conditional on those fixes + pitch constraint (never cheaper/faster than software).** Claude to fold scores into QUALITY_GATE.md on the branch. The 1-business-day 1–2 star promise stays an owner decision (queued tap). Nothing posted, nobody contacted.

---

## Research commits `bd712ea5` + `218d4540` — Atlas challenger read (2026-11-21 ~17:35 MST)

Claude's own ATLAS_REVIEW.md entries above (DMSO, cookbooks, Jensen Huang) already record the verdicts. I read all three research files in full plus INBOX.md and concur — no challenge raised on substance. Two nits for the record:

- The cookbooks file title still says "91 Notebooks" while its own verified count is 98 (registry.yaml, counted entry by entry); the body corrects it, but a skim reader takes 91 from the title. Rename the title to 98.
- DMSO file's integration line (owner "already experimenting with DMSO… per the Pineal detox side chat") is side-chat context I did not re-verify here; the file itself gives no dosage and says "not medical advice" — that restraint is the right call, keep it.

---

## PR #14 + PR #15 challenger review (2026-11-21 ~21:00 MST / 2026-11-22 04:00 UTC)

Two new quality-gate step-1 benchmarks, reviewed live by two verification subagents (all source pages re-opened independently) and cross-checked by Atlas. Review comments posted on both PRs.

### PR #14 — Listing Makeover benchmark (head 2fa6f3b9, +103/-3, 4 files) — PASS conditional

**Verified:** Offer prices match the offer file exactly (Starter $79/20, Shop $179/60 + About + announcement, Monthly $59/mo ≤15, free 2-listing proof, same-day Starter; gig-2 Basic $15/3/1d, Standard $59/15, Premium $179/60). Arithmetic correct ($3.95 / $2.98 / $3.93). Ran `listing_lint.py --strict-titles` on the Davias file: pre-fix 0/12 exit 1, post-fix 12/12 exit 0, new titles 10–12 words. Etsy quotes verified verbatim via Value Added Resource (Aug 21, 2025): "less than 15 words", "try not to repeat words", "Move subjective words, like 'perfect' or 'beautiful,' to the description", "slowly changing a few items at time". eRank blog verified: "No. Etsy confirmed that its search doesn't punish older-style titles" + AI tool "occasionally omits important keywords or suggests terms that could cause issues (like trademarks or prohibited phrases)". Marmalead $19/mo ($16 annual) and #5/#23 quotes verified verbatim. PeoplePerHour £10/$15 + 140-char title verified; Contra Koleosho $50/3 days verified. Lapis = rock / Amber = fossil resin / Obsidian = volcanic glass correct; new titles say "natural stone".

**Challenges (fix before merge):** (1) "10 of the 12 titles had 15+ words" is WRONG — measured 8/12 (word counts 15,15,16,14,16,14,15,16,14,16,13,15). The wrong "10/12" also appears in the PR #14 body, PR #46 body, and OWNER_BRIEF 00:25 entry — correct all to 8/12. (All 12 repeating "Bracelet" is correct.) (2) All 4 Fiverr gigs UNVERIFIED (HTTP 403; searches surface none) — Uri B. $50/10, Natalia $15/2, Sakib $10 on hold, Katrina $35 on hold; OWNER_BRIEF 00:25 states "the cheapest active rewriter… charges about $5" with no caveat. Needs a live-browser check. (3) ainfluencer.com wholly UNVERIFIED (fetch blocked by domain policy; zero search results) — Etsy Optimize Pro / Marketing Pro / Social It prices, both quotes, login warning all unconfirmed. Needs a live browser. (4) "The Fiverr gigs sell 'within 140 characters'" overreaches — verified only for PeoplePerHour. (5) PeoplePerHour delivery contradicts itself ("2 days" in price box vs "4 days" in body); "+$20/extra", seller name "Cary G.", "0 sales" don't appear in the fetched page (only "Views 17"). (6) Nit — new HELIX file still has 12 open `[size]` placeholders: titles are 12/12, but per process.md it's not "ready to paste".

**Suggested gate scores (Listing Makeover step 3):** Row 5 Price/value 4/5 conditional (can't be 5 while the cheapest-active claim is [S] and Sakib's $2.00 undercuts); Row 6 Complaint fix 4/5, rising to 5 once #1 is corrected and the PR #46 stopword fix lands.

### PR #15 — Wellness Blog Engine benchmark (head a3f1195e, +80/-2, 4 files) — PASS conditional, step 1 only, NOT scored

Step 3 is premature (sample DRAFT with pre-sale fixes outstanding, row 6 explicitly PARTIAL pending Grok, freelancer comparison [S]-unverified). The benchmark's own "Row 6 can't score above 3 without them" stands.

**Verified:** Offer/deliverable match main exactly ($150/$250/$300; Sources section, PROVEN/TRADITIONAL/FRINGE labels, clinician line, topics by the 5th, 1/week, pay-after-post-1). Gig-3 matches (Basic $25/800w/3d, Standard $59, Premium $199). Arithmetic correct (38%, 25%, 4×$30=$120). BKA $390/mo 4 posts, meta free, 5%/10% term savings, G2 0 reviews — verified. Both Contra writers verified in full ($600/mo; $1,200/4 articles). Therapist Site Toolbox, eesel.ai, WriterAccess quotes verified verbatim. Blawgy $99/$149 verified from GetApp, G2, and Blawgy's own site. FTC standard quoted verbatim: health-benefit/safety claims require "competent and reliable scientific evidence"; RCTs "are the most reliable form of evidence"; "Anecdotal evidence… [is] never sufficient"; the guidance "doesn't have the force or effect of law."

**Challenges (fix before merge):** (1) BKA stock image $6 vs $13 conflict on the page itself (body $6, options list $13/post) — benchmark already flags both, don't resolve by picking one. (2) "No AI" / auto-renew / "within a few weeks" mis-attributed to the BKA Lvl 2 page — "No AI" is on BKA's health page, not Lvl 2; the other two weren't found on Lvl 2 at all. (3) Blawgy G2 "(no text)" is WRONG — the single 5.0 review has text (Buddy R., Founder, 10/28/2026: "Founder is very helpful. The software just works!"). (4) All 3 Fiverr gigs UNVERIFIED (HTTP 403); the "matches, doesn't beat the best freelancer" conclusion rests on wafa_94 $30 [S]. Needs a live-browser check. (5) Nit — Toolbox first delivery is the 1st of the month after purchase, then first Mondays.

### Issue #12 closed this run

Claude's comment (01:27Z) recommended closing: the mentalium_ clip is a silent infographic slideshow, no transcript exists, and the content is covered by `research/mentalium-claude-cookbooks.md` (commit 218d454, read in full on the prior watch run). Atlas agreed, commented, and closed the issue (completed) — Grok's credits stay on the Fiverr benchmark rows. Full PR review detail: `~/workspace/goals/subliminal-messaging-app/hidden_files/pr-review-2026-11-21-2011.md`.

---

## PR #14 + PR #15 live-browser follow-up (2026-11-21 ~22:31–22:38 MST)

Browser task (read-only, no sign-in) checked all 11 source URLs live. Follow-up comments posted on both PRs (7074915542, 7074927911).

**PR #14 — challenges #2 (Fiverr unverified) and #3 (ainfluencer unverified) CLOSED.** All 4 Fiverr gigs confirmed at stated prices: Uri B. $50/10, 3-day; Natalia $15/2, 2-day; Sakib $10 ON HOLD; Katrina $35 ON HOLD. ainfluencer fully confirmed (Optimize Pro $25/$50/$150, Marketing Pro $499/$799, Social It $499/$999/custom, both quotes + login warning verbatim). eRank confirmed (Free $0, Basic $5.99, Pro $9.99, Expert $29.99/mo). PeoplePerHour seller "Cary G.", VIEWS 17, +$20/extra add-on confirmed.

**New findings on PR #14:** (1) Sakib's 2-star review DOES have visible text ("Seller talked me into a $106 upgrade…" — greetingpurpose, 4 years ago, plus seller response) — the benchmark's "has no visible text" claim is wrong; the review is useful complaint evidence, not a gap. (2) "Within 140 characters" proven overreach — no Fiverr gig page mentions "140"; only PeoplePerHour states it. (3) PeoplePerHour is self-contradictory live: body "£10 / 4 days" vs buy box "$15 / 2 days" vs banner "2-day delivery" — benchmark must show both, not pick one. "0 sales" NOT shown (bare "0" beside a heart/favourites icon). (4) Natalia's FAQ says 1-day delivery vs package 2-day. (5) OWNER_BRIEF "cheapest active rewriter… about $5" still unsourced — cheapest confirmed ACTIVE gig is Natalia $15 (Sakib $10 is on hold); cite the $5 source or correct to $15. Row 5 stays 4/5 conditional until the $5 claim is sourced or corrected. Remaining fix-before-merge: #1 (8/12), #4, #5, plus new items 1, 4, 5.

**PR #15 — challenge #4 (Fiverr unverified) CLOSED.** wafa_94 $30 confirmed (1,000 words, 3-day, 5.0/22, 241 orders); brightleaf_w $35 confirmed; traviseric17 $40 confirmed and ON HOLD. The "matches, doesn't beat the best freelancer" conclusion now stands on verified ground. Remaining fix-before-merge: #1 (BKA $6 vs $13), #2 (mis-attributed "No AI"/auto-renew/"within a few weeks"), #3 (Blawgy G2 review has text). Step 3 still not scored (sample DRAFT + row 6 PARTIAL pending Grok).
