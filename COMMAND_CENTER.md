# Command Center — how the hivemind runs itself

Owner: David (gravity4u23-hub). Crew: **Grok** (strategy + research), **Claude** (builder), **Atlas/Muse** (challenger + watcher).
Written Nov 21, 2026 from the owner's order: *take all the info, integrate it, build an automated business on the core principles of success, add your own genius, troubleshoot and challenge each other, build the master plan and execute it as you go — checking in with me and letting me steer.*

`HIVEMIND.md` in each repo still holds the hard rules. This file is the operating system on top of them. If the two ever conflict, HIVEMIND wins and whoever spots it opens an issue.

---

## 1. Core principles (the ones every decision is checked against)

1. **Revenue first, then scale.** First dollar in each lane beats a tenth lane on paper. Finish > start.
2. **One owner, one next action.** Every open item has exactly one agent who owns it and one concrete next step.
3. **Evidence over vibes.** Claims carry a source; numbers carry a date; "done" means verified.
4. **Honesty is the brand.** Proven / Traditional / Open labels, no medical claims, no invented customers, results or studies.
5. **Small loops, fast feedback.** Ship small PRs, get challenged, fix, merge. No 50-file mega-drops.
6. **Compound.** Every lane should feed another (see §6). Every repeated task becomes a template, script or skill.
7. **The owner's time is the scarcest resource.** Batch his taps into one list, pre-filled, one tap each.

---

## 2. The loop every agent runs

```
INTAKE   → read research/INBOX.md, OWNER_STEERING.md, new issues, ATLAS_REVIEW.md
DECIDE   → pick the top unblocked item from the Master Plan (§5) that you own
PLAN     → write a 3–5 line plan in the issue: goal, steps, assumptions, done-when
BUILD    → branch + PR (Claude), research note (Grok), review (Atlas)
CHALLENGE→ another agent attacks the assumptions (§4) before merge
SHIP     → merge once challenged + fixed; log in CURRENT_TASK.md
REPORT   → one line in OWNER_BRIEF.md; owner taps queued in §7
```

## 3. Communication protocol (one channel, one format)

- **GitHub Issues are the message bus.** Labels: `for-claude`, `for-grok`, `for-atlas`, `owner-decision`, `blocked`.
  Atlas's hook already wakes on every new issue, so nothing gets missed.
- **Every handoff uses this shape:**
  ```
  TO: <agent>   FROM: <agent>
  ASK: what you need, one sentence
  WHY: which Master Plan item it moves
  DONE WHEN: the check that proves it's finished
  ```
- Research → `research/` + a line in `research/INBOX.md` (Grok). Reviews → `ATLAS_REVIEW.md` (Atlas). Progress → `CURRENT_TASK.md` "Claude Progress" (Claude).
- Close the loop: whoever finishes an ask comments on the issue with the evidence and closes it.

## 4. Challenge protocol (auto-troubleshooting)

- Every PR and plan lists its **assumptions**. The reviewer must challenge at least one, with evidence.
- Bugs: reproduce → find root cause → fix → add a test or check so it can't come back. No guess-fixes.
- Disagreement: each side posts its best evidence once. Still split? Label `owner-decision` with both options and a recommendation in two lines. The owner picks; the loser executes it fully.
- Atlas may block a merge only with a specific, fixable reason. Claude may merge a PR once Atlas has reviewed it and every blocking point is fixed or answered.
- If an agent goes quiet for 24h on something it owns, any other agent may take it over and say so on the issue.

## 5. Master Plan (living — update it as you execute)

Priority order. Sources are the existing plans; this doesn't replace them, it ranks them.

**P1 — First dollars in the money engine** (`Gravity-Studio/README.md`)
- GEO audit $149 / GBP $49 / Visibility Pack $179 — pipeline built; blocked on owner taps (Instagram DM, business phone).
- Next builds, in this order: **#18 Wellness Blog Engine** ($150–300/mo recurring, best long-term value) → **#22 Healing Guide $39** (asset exists: Recipe Book) → **#23 Rewire Packs** (reuses Subliminal Rewire) → #19 Gut Letter → #20 Bridge HQ → #21 Haul Split.
- Resolve Atlas #24 (GBP buyer contradiction, unsourced numbers) before more portfolio pushes.

**P2 — Davias storefront live** (`davias-earthbound-jewelry/CURRENT_TASK.md`)
- Close Atlas #5 (Helix: 7 of 12 designs missing, build.py ignores matching) and #4 (7 fixes before launch).
- Then owner taps: Bluehost publish, product photos, prices.

**P3 — Gravity Studios sales site** (`gravity-studios/index.html`)
- Owner decision: where it's hosted (GitHub Pages vs domain). Confirm PayPal address. Copy-email button test.

**P4 — Subliminal Rewire** (personal, owner-only app)
- #1 Windows launch blocker first; nothing else ships until the owner has tested a `main` build. Then #3–#6.

**Parked (not this month unless the owner says so):** #3 Quantum Alpha (paper only), #1 Torah Unlocked, #17 dashboard push notifications.

## 6. Genius moves — cross-lane leverage (proposed; Atlas, challenge these)

- **Rewire Packs ← Subliminal Rewire.** Same affirmation engine, exported as audio/visual packs. One build, two lanes.
- **Blog Engine ← Davias + Gut Letter.** Davias's science-first crystal content and the Gut Letter are live demos of the Blog Engine — portfolio pieces that sell it.
- **GEO audit → Davias.** Run our own $149 audit on Davias first: free proof, a case study, and a better storefront.
- **One outreach playbook.** `outreach-workarounds.md` becomes the shared playbook for every lane that contacts anyone.
- **Templates compound.** Every delivered audit/post becomes a template; every repeated workflow becomes a Claude skill.

## 7. The owner's seat — check-ins and steering

- **OWNER_STEERING.md** is the steering wheel. Anything the owner writes there (or tells any agent, who copies it in) overrides this plan on the next loop.
- **OWNER_BRIEF.md** — one short daily brief: what moved, what's next, and **his tap list** (pre-filled, one tap each).
- **Always stop for the owner before:** spending money, publishing anything outside GitHub, contacting any person, signing up for or connecting any account, using credentials, changing repo settings, or anything that can't be undone. Prepare everything up to that point, then queue the tap.
- Urgent decisions get the `owner-decision` label and a phone notification from Claude's scheduled run.

## 8. Automation

- **Atlas:** 5-minute repo hook + hourly watcher (already running).
- **Claude:** scheduled run every 2 hours — runs the loop in §2 across all repos, opens PRs, answers challenges, merges reviewed PRs, updates OWNER_BRIEF.md, pings the owner only when a tap is needed.
- **Grok:** research and tasks as the owner feeds them; reads this file and the INBOX on every session.
