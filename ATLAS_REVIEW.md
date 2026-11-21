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
