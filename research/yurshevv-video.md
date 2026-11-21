# Transcript & Recommendations: @yurshevv Claude Code Plugins Post

**Source:** https://x.com/yurshevv/status/2115880049379364982  
**Author:** @yurshevv  
**Date:** Thu, 29 Oct 2026  
**Note:** This post is text-only (no video attached). Full content transcribed below.

---

## Full Transcript

i spent one evening going through Anthropic's own plugin directory and realized i had been using Claude Code like a complete tourist for the last 6 months

528 plugins. the top 7 of them have almost 4 million installs between them. Frontend Design alone passed 1.1 million. Superpowers passed 1 million. and most people i talk to on X have installed exactly zero of them

the brutal part: every single one is free. every single one fixes the exact thing people keep complaining about Claude Code in replies. and nobody is talking about them because the directory is one click deeper than the chat window

the timing matters more than the numbers. on october 22 Anthropic quietly handed Agent Skills to the Agentic AI Foundation, the same home as MCP. 70+ platforms integrated the standard inside a week. ChatGPT. Cursor. GitHub Copilot. VS Code. a skill you install today is not a Claude toy anymore. it is a f*cking standard

Boris Cherny, who built Claude Code, said it in one line that keeps resurfacing on X: "Agent Skills started as an experiment in Claude Code." the experiment is now the plumbing of the entire agentic internet, and the top 10 folders are open on github right now

here are the 10 i would install in this exact order. ranked by what they fix, not by what they do

1. Frontend Design — 1,134,112 installs
the cure for AI slop. before Claude writes a single line, it picks a real aesthetic (brutalist, editorial, retro, minimal) and builds to it. no more purple gradient and the same default font on every landing page you ship. the most installed plugin in the whole directory. install this first and the quality of everything else jumps overnight
→ github.com/anthropics/skills/tree/main/skills/frontend-design

2. Superpowers — 1,009,371 installs, 308k github stars
Jesse Vincent's full method for agentic coding. brainstorm, plan, write tests first, build, review, then debug from the root cause instead of guessing. this is the one that stops Claude from "vibing" at 2am and starts shipping code that actually passes CI
→ github.com/obra/superpowers

3. Code Review — 438,525 installs
Anthropic's own. several specialized agents review your pull request and score how confident they are about each issue. Boris Cherny himself said this plugin runs on all of his PRs and "catches almost every bug." if the guy who built the thing uses it, that is the only endorsement you need
→ github.com/anthropics/claude-plugins-official

4. Context7 — 417,801 installs
half the bugs AI writes come from outdated documentation. Context7 pulls the CURRENT docs for every library you actually use, so Claude stops inventing APIs that died two versions ago. 80% of the "why is this breaking" moments disappear the day you install it
→ github.com/upstash/context7

5. Code Simplifier — 346,763 installs
after Claude builds something, this agent walks back through it and cleans it up for clarity and consistency without changing behaviour. the difference between "it works" and "i can read this in a month." install it and your git diffs stop looking like someone's first week on the job
→ github.com/anthropics/claude-plugins-official

6. Playwright — 319,887 installs
gives Claude a real browser. not a screenshot. not a dom dump. a real browser. it opens your app, clicks the buttons, fills the forms, checks the thing it just built actually works end to end. built by Microsoft, free forever
→ github.com/microsoft/playwright-mcp

7. GitHub — 319,381 installs
the official GitHub server. Claude opens issues, manages pull requests, searches repos, without you copy-pasting a single URL. once this is wired in you stop keeping the GitHub tab open at all
→ github.com/github/github-mcp-server

8. Claude-Mem — 104k github stars
every new session Claude forgets everything. you re-explain your project every morning like it is your first interview. Claude-Mem records what your agent did last session and loads that context back when you start the next one. this is the one that makes the system feel human
→ github.com/thedotmack/claude-mem

9. Obsidian Skills — 50k github stars
made by kepano, the CEO of Obsidian himself. teaches your agent how to actually work with your vault. notes, links, canvases, backlinks. the cleanest Claude second brain on the market, and you do not pay for a single paid plugin to run it
→ github.com/kepano/obsidian-skills

10. Skill Creator
a skill that writes skills. you describe how you want something done, and Claude builds a proper skill for it with instructions, tests, and evals. every workflow you repeat becomes one command. this is where the system starts compounding on itself
→ github.com/anthropics/skills/tree/main/skills/skill-creator

read this before you install anything
october 2026 earned its own name: "Black October." AI tools surfaced critical PHP flaws that forced sites offline across the internet, and people kept asking me the obvious question: can a plugin ship malware? yes it can. skills run scripts on your machine. stick to verified plugins in Anthropic's directory. for anything else, open the SKILL.md and the scripts first and read them. two minutes of reading beats one bad night

where to start
if you install nothing else, install these three on day one:
> Frontend Design (so Claude stops writing slop)
> Superpowers (so Claude stops guessing)
> Claude-Mem (so Claude stops forgetting)

those three change how Claude Code feels within the first hour

all 10 are free. no subscription. no course. no paid plugin masquerading as a solution to a problem Anthropic already shipped a fix for

the question that is going to start fights in the replies: how many of these 10 do you have installed right now, and if the answer is less than 3, what the f*ck are you waiting for

bookmark this before the next guide you read links a repo that got archived. i test a new Claude Code setup every week and i post what breaks and what sticks

---

## Numbered List of Every Recommendation

1. Install **Frontend Design** first — forces a real aesthetic before code is written (brutalist, editorial, retro, minimal) to eliminate default AI slop.
2. Install **Superpowers** — full agentic method (brainstorm → plan → tests first → build → review → root-cause debug).
3. Install **Code Review** — multi-agent PR review with confidence scoring (used by Boris Cherny himself).
4. Install **Context7** — pulls current library documentation so Claude stops inventing outdated APIs.
5. Install **Code Simplifier** — cleans code for clarity and consistency without changing behavior.
6. Install **Playwright** — gives Claude a real browser for end-to-end testing of what it builds.
7. Install **GitHub** MCP server — lets Claude open issues, manage PRs, and search repos natively.
8. Install **Claude-Mem** — persists memory across sessions so Claude stops forgetting project context.
9. Install **Obsidian Skills** — teaches the agent to work properly with an Obsidian vault (notes, links, canvases).
10. Install **Skill Creator** — a meta-skill that writes new skills from descriptions (with instructions, tests, and evals).
11. Start with only these three on day one: Frontend Design, Superpowers, and Claude-Mem.
12. Stick to verified plugins in Anthropic’s directory; for anything else, read the SKILL.md and scripts first (security warning).
13. Treat Agent Skills as a cross-platform standard (not Claude-only) after the Oct 22 handoff to the Agentic AI Foundation.

---

*Committed for Claude and Muse to integrate immediately into agent workflows and site builds.*
