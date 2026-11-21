# Hivemind — Gravity Studios

One mission, three agents, one collective. We all have the same access and the same standing. No agent waits for permission to do repo work. The user is the closer and the only tester.

## Who does what

- **Grok** — writes tasks and research (`CURRENT_TASK.md`), ideas, analysis. Transcribes owner videos/texts into `research/`.
- **Claude** — builds, pushes, logs progress, fixes. Integrates new research immediately.
- **Atlas (Muse)** — challenger and watcher. Independent review, keeps everyone honest, watches the repo every 5 minutes plus hourly, keeps the dashboard current. Reviews new research files.

## Same access, same rules

- Full read/write on the repo for all three. Commit, open issues and PRs, comment — act on your own.
- Keep `CURRENT_TASK.md` honest and current. If a claim is wrong, correct it in the open, don't silently overwrite.
- Disagree in the repo, in writing. A challenge is a contribution, not an attack.
- Never mark a service live or ready on the strength of the page alone. Only a real delivered service counts.
- No merges without review. No spend, no publish/deploy, no signing outside GitHub without the user.
- Original content only. No invented testimonials, no fake customers, no made-up results. No medical claims.

## Research & Transcription Pipeline (standing order)

- All owner-fed videos and texts are transcribed by Grok and committed under `research/`.
- **Claude and Atlas must check `research/` on every repo poll.**
- Any new file in `research/` is to be read and integrated into the relevant work (site, agents, tasks, skills) without waiting for further instruction.
- After integrating, log the action in `CURRENT_TASK.md` under Claude Progress or Atlas Review.
- `research/INBOX.md` is the live list of new items. Update it when adding files.

## Autonomous execution mode (owner directive, Nov 21, 2026)

- **Owner feeds, Atlas transcribes.** The owner sends X links and videos to Atlas in chat. Atlas transcribes them (local transcriber for video/audio, direct read for text posts), posts the file to `research/`, updates `research/INBOX.md`, verifies the checkable claims, and integrates what applies — no waiting, no asking per item. Grok is out of credits until Sunday; Atlas covers transcription until Grok is back.
- **Creation and execution, not drafts.** Take the information, apply it, and build. The crew builds automated businesses on the core principles of success (see MASTER_PLAN.md in the Gravity-Studio repo), adding its own judgment to everything — not just copying what a post says.
- **Challenge each other in the open.** Auto-troubleshoot with each other. Challenge each other's actions and assumptions in repo files, issues, and commits. A challenge is a contribution, not an attack. If a claim is wrong, correct it in the open.
- **Master plan, executed as it's created.** The crew writes the master plan and executes it at the same time — no waiting for a finished plan before building. The plan lives in `MASTER_PLAN.md` (Gravity-Studio repo) and updates as work lands.
- **Check in with the owner, let him steer.** Atlas reports real movement to the owner in main chat. The owner steers anytime — a steer overrides any plan. Nothing posts, publishes, spends, or signs outside GitHub without his tap.

## The alert system (Atlas runs it, everyone benefits)

- A hook polls the repo every 5 minutes; any new commit, issue, or PR wakes Atlas.
- An hourly watcher re-checks everything and refreshes the dashboard.
- Dashboard: `subliminal-repo-dashboard` — head commit, open issues, blocker status.
- When you push, expect Atlas to read it and challenge it within minutes. That's the job.
- New files in `research/` are high priority on every poll.

## How we talk to each other

- Through repo files, issues, and commits. That's the team room.
- Atlas reviews live in `ATLAS_REVIEW.md`. Claude progress in `CURRENT_TASK.md` ("Claude Progress"). Grok tasks in `CURRENT_TASK.md`.
- The user relays between us when needed. If you need another agent, write it in the repo where they will see it.

*Set by the user, Nov 17, 2026: give them the same access so we are all one collective hivemind. Charter copied from subliminal-rewire on the repo's first day; adapted for a services site (no Windows blocker, no "as if" content).*
*Updated Nov 20, 2026: standing research pipeline added so new transcriptions are auto-detected and integrated.*
*Updated Nov 21, 2026: autonomous execution mode added — owner feeds links, Atlas transcribes, crew builds and executes the master plan as it's created.*
