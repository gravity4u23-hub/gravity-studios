# Claude build standards

Read `HIVEMIND.md` first; its rules win over anything here. These standards come from `research/yurshevv-video.md` in gravity-studios (Grok's transcript, Nov 20 2026) and apply to every Claude session in this repo: Claude Code, the Claude app, or cloud.

## How every piece of work runs
1. **Design before code** (frontend-design). For any screen or page, name one aesthetic first (editorial, brutalist, retro, minimal, deep space...), write it in the PR, and build to it. No default purple gradients, no stock system-font look.
2. **Process, not vibes** (superpowers). Clarify the ask → short plan → tests first → build → review → debug from the root cause. Never guess at a fix.
3. **Current docs only** (context7). Check the current docs for any library or API before using it; don't write from memory.
4. **Prove it works** (playwright / tests). Run it or open it before calling it done. "Done" means verified, not "should work".
5. **Simplify pass** (code-simplifier). Once it works, clean it up for readability without changing behaviour.
6. **Review before merge** (code-review + Atlas). Every change goes through a PR; nothing merges unreviewed.
7. **Leave memory behind.** Log decisions and status in `CURRENT_TASK.md` (Claude Progress) so the next session — any agent — starts with full context.

## Plugins
`.claude/settings.json` enables the vetted plugins from Anthropic's official directory; Claude Code offers to install them when this repo is opened.
- Enabled: frontend-design, superpowers, code-review, context7, code-simplifier, playwright, github.
- **Claude-Mem** is community-built and runs code locally — the owner installs it by hand on the laptop after reading it (`npx claude-mem install`). Not auto-enabled.
- Security rule: only verified plugins from the official directory. For anything else, read its SKILL.md and scripts before installing.

## This repo
- Single-page site (`index.html`). Verify it in a real browser at desktop and phone widths before calling it done.
- Check `research/INBOX.md` on every session and integrate new items (HIVEMIND standing order).
