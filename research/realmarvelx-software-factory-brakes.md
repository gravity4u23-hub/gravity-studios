# The software factory: accelerators vs brakes (realmarvelx video)

Source: https://x.com/realmarvelx/status/2123824160602304852
Author: @realmarvelx. Video ~19.7 min conference talk (speaker from the AIHero / XState background — cites AIHero.dev skills, XState core team). Transcribed by Atlas local transcriber (faster-whisper base, 462 segments), Nov 21, 2026.
Post text: not yet retrieved — X post page blocked in cloud browser (403); the video transcript below is the substance. Local transcript: `~/workspace/ai-leads/transcripts/2123824160602304852.txt`.

## Transcript — key points

"Code is cheap" is wrong. Code is not just production — it's maintenance, and it's the primary prompt / environment your agent operates in. A healthy codebase constrains the agent to certain paths and restricts its design choices, so you get better output. Software fundamentals still matter — more than ever — because speed is the central promise of AI.

The "software factory" has two parts: accelerators and brakes. Accelerators trigger the factory autonomously (bug reports, feature requests, support tickets → the system prompts the agent). Brakes slow the agent down and raise quality — without brakes you drive into a "slop cannon." The three brakes:

1. **Automated checks** — deterministic, cheap (CPU cycles, not tokens). Stack them high: max out lint rules, type checking, tests. Agents BENEFIT from friction — reducing the design space is a massive benefit. Tests are the most important check because they actually execute code. Bad tests: (a) tautological — the test reasserts the implementation (e.g. "expect X post-character limit to be 280"); (b) structure-sensitive — the test reads the source file and checks button order, so any refactor breaks it; (c) cannot fail — mocks don't match reality (e.g. stubbing out AudioContext validation that will fail in production). Prompt to find them: "Explore my test suite and identify tests that are tautological, structure-sensitive, or where mocks don't match reality."
2. **Deep modules + centralized state (make checks harder to cheat).** Deep modules (Ousterhout, A Philosophy of Software Design): lots of implementation hidden behind a tiny interface (e.g. JSON.parse) — the agent can only test through the interface, so fewer structure-sensitive tests. Agents typically write shallow modules that export everything. React pushes shallow modules; extract state into reducers / state machines (Redux-like) — locality: all state in one place, one file for the agent to read, testable as pure functions without a browser. His "improve codebase architecture" skill restructures messy front-end state into reducers/state machines.
3. **Automated review** — a separate reviewer agent with a fresh context window takes the diff and imposes coding standards. Do NOT trust the implementer with coding standards (it's overloaded: explore + implement + debug + fix checks). Do NOT put standards in AGENTS.md (the steering file loaded every session — the implementer ignores it under load). Do NOT outsource to generic review tools (CodeRabbit etc.) — automated review must be built from mistakes YOU have seen the agent make. Two-phase: implementer makes it work; reviewer makes it good.
4. **Human review** — review the SYSTEM that produces the code, not just the code. Never write the same PR comment twice: upstream your taste into automated checks and review (his "retro" skill). "Leading words" — domain vocabulary (e.g. "error boundary", "optimistic updates") compresses a ton of knowledge into one word; agents pick the word up and use it in their own thinking. Farm existing PR comments to generate new checks and standards updates.

## Atlas verification

- Concepts match established software engineering: Ousterhout deep modules, CI lint/typecheck/test practice, code review. The "brakes" framing is the speaker's own model; the practices are standard and sound.
- Speaker's skills repo (AIHero.dev) is a commercial product — noted, not endorsed. No prices verified.
- The talk is about React/front-end apps; the brakes model generalizes to any agent-built code.

## Apply / build commands — this maps directly onto the hivemind

- The hivemind ALREADY runs this model: Atlas as challenger = brake 2 (automated review) + brake 3 (human review upstreaming taste). Superpowers' method (tests first, then build) = brake 1. Name it explicitly in HIVEMIND.md so the crew uses the vocabulary: accelerators vs brakes.
- Claude's builds must carry automated checks (lint/typecheck/tests) AND a reviewer pass before merge. The Windows launch blocker (subliminal-rewire issue #1, black window, no user-tested artifact) is exactly what happens without brakes.
- Coding standards live in the REVIEW step, not in AGENTS.md/HIVEMIND.md alone — the implementer is overloaded and ignores them. Atlas's challenges must upstream into standing checks so they're never repeated (retro loop).
- Applies to subliminal-rewire PRs #4/#5/#6 (tests-first, reviewer pass, no merge without a user-tested artifact) and the Davias site build.
- No new spend. No skills purchase.
