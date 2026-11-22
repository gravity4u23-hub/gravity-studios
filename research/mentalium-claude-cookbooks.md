# Anthropic's Claude Cookbooks: 91 Notebooks, Official Reference (mentalium)

**Source:** https://x.com/mentalium_/status/2124177042778321182/video/1
**Poster:** mentalium @mentalium_ (verified), Nov 21, 2026, 9:24 AM
**Video:** infographic slideshow, **NO audio track** — yt-dlp `--list-formats` shows video-only formats only. Nothing to transcribe; the content is the post text + the repo itself. Thumbnail reads: "ANTHROPIC BUILD WITH CLAUDE 100+ OFFICIAL NOTEBOOKS - 40 HANDPICKED RESOURCES".
**Repo:** https://github.com/anthropics/claude-cookbooks — public, MIT license, created Aug 15, 2023, 652 commits, head `8ad5de64` at check time.

**Post text (as captured):** "Anthropic quietly put 91 REAL Claude notebooks on GitHub and almost NOBODY talks about them. If you're building with Claude, these 91 notebooks are the cleanest FREE path. Tool use. Agents. RAG. Vision. Skills. Cost. Evals. Production. 55k+ stars."

## What the post says

- Anthropic's official `claude-cookbooks` repo holds 91 notebooks, free, covering tool use, agents, RAG, vision, skills, cost, evals, production.
- It lists 40 handpicked notebooks (39 names captured — see Verification), all supposedly under `tool_use/`, `skills/`, `multimodal/`, `misc/`.
- Framing: the repo is a quiet, overlooked drop; the notebooks are "the cleanest FREE path" for building with Claude.

## The headline finding — read this first

**The repo is real, official, and excellent. The post's list is not.** Of the 39 names captured from the post, only **3 exist verbatim at the stated paths**: `calculator_tool`, `best_practices_for_vision`, `prompt_caching`. The rest are loose paraphrases of real notebooks (with different filenames, often in different folders) or have no matching notebook at all. **Do not click the post's paths blindly — most are dead links.** The real names are in the audit table below.

Three numbers, all different: the thumbnail says **100+**, the post text says **91**, the repo's own registry lists **98**. The registry count (98, counted entry by entry from `registry.yaml` at main, see Verification) is the number to use. The repo is also **not a new drop** — it was created Aug 2023 and is a living repo with additions as recent as Nov 2, 2026 (`latency_optimization`, dated 2026-11-02). "Quietly put" is hype framing; the repo has been public and growing for three years.

## The 40-list audit (39 names captured)

Method: read all four folder listings live (`tool_use/`, `skills/`, `multimodal/`, `misc/`) + the full `registry.yaml` (98 entries). Verdicts: **✓ exact** = file exists at the stated path; **≈ paraphrase** = a real notebook covers the topic under a different name/path; **✗ no match** = nothing in the registry covers it.

| # | Post name | Verdict | Real notebook |
|---|---|---|---|
| 1 | calculator_tool | **✓ exact** | `tool_use/calculator_tool.ipynb` |
| 2 | all_tools | ✗ no match | Closest: `tool_use/parallel_tools.ipynb` (parallel calls) |
| 3 | structured_outputs | ≈ paraphrase | `tool_use/extracting_structured_json.ipynb` |
| 4 | create_a_skill | ≈ paraphrase | `skills/notebooks/03_skills_custom_development.ipynb` |
| 5 | writing_effective_prompts | ✗ no match | Closest: `misc/metaprompt.ipynb` |
| 6 | sql_tool | ≈ paraphrase | `misc/how_to_make_sql_queries.ipynb` |
| 7 | bash_tool | ✗ no match | Covered inside `claude_agent_sdk/01_The_chief_of_staff_agent.ipynb` (Feature 1) |
| 8 | best_practices_for_vision | **✓ exact** | `multimodal/best_practices_for_vision.ipynb` |
| 9 | use_a_skill | ≈ paraphrase | `skills/notebooks/01_skills_introduction.ipynb` |
| 10 | image_understanding | ≈ paraphrase | `multimodal/getting_started_with_vision.ipynb` |
| 11 | long_context | ≈ paraphrase | `tool_use/automatic-context-compaction.ipynb` |
| 12 | rag_with_tool_use | ✗ no match | Closest: `capabilities/retrieval_augmented_generation/guide.ipynb` |
| 13 | tool_use_with_memory | ≈ paraphrase | `tool_use/memory_cookbook.ipynb` |
| 14 | agent_with_memory | ≈ paraphrase | `tool_use/memory_cookbook.ipynb` (also `managed_agents/CMA_remember_user_preferences.ipynb`) |
| 15 | structured_data_extraction | ≈ paraphrase | `tool_use/extracting_structured_json.ipynb` |
| 16 | structured_data_from_documents | ✗ no match | Closest: `multimodal/how_to_transcribe_text.ipynb` |
| 17 | create_a_plugin | ✗ no match | Nothing in the registry |
| 18 | package_a_skill | ✗ no match | Covered inside `03_skills_custom_development.ipynb` |
| 19 | create_and_use_a_plugin | ✗ no match | Nothing in the registry |
| 20 | prompt_caching | **✓ exact** | `misc/prompt_caching.ipynb` |
| 21 | batch_api | ≈ paraphrase | `misc/batch_processing.ipynb` ("Batch processing with Message Batches API") |
| 22 | batch_api_with_tool_use | ✗ no match | Nothing in the registry |
| 23 | memory_and_contextual_memory | ≈ paraphrase | `tool_use/memory_cookbook.ipynb` / `capabilities/contextual-embeddings/guide.ipynb` |
| 24 | simple_rag | ≈ paraphrase | `capabilities/retrieval_augmented_generation/guide.ipynb` |
| 25 | rag_with_citations | ≈ paraphrase | `misc/using_citations.ipynb` |
| 26 | rag_with_memory | ✗ no match | No single notebook; combine `memory_cookbook.ipynb` + RAG guide |
| 27 | agent_with_tools | ≈ paraphrase | `tool_use/customer_service_agent.ipynb` |
| 28 | tool_use_with_multiple_tools | ≈ paraphrase | `tool_use/parallel_tools.ipynb` |
| 29 | tool_use_with_mcp | ✗ no match | MCP is covered in `managed_agents/CMA_operate_in_production.ipynb` and `claude_agent_sdk/02_The_observability_agent.ipynb` |
| 30 | effective_agent_design | ✗ no match | Closest: `patterns/agents/basic_workflows.ipynb`, `claude_agent_sdk/01_The_chief_of_staff_agent.ipynb` |
| 31 | contextual_memory | ≈ paraphrase | `tool_use/memory_cookbook.ipynb` / `tool_use/context_engineering/context_engineering_tools.ipynb` |
| 32 | long_horizon_agent | ✗ no match | Closest: `tool_use/automatic-context-compaction.ipynb` |
| 33 | price_perf_evals | ≈ paraphrase | `cost_optimization/cost_optimization.ipynb` (top-level folder, not in the post's four) |
| 34 | price_perf_evals_llm_judge | ✗ no match | Closest: `misc/building_evals.ipynb` + `cost_optimization.ipynb` |
| 35 | quality_evals | ≈ paraphrase | `misc/building_evals.ipynb` |
| 36 | cost_optimization | ≈ paraphrase | `cost_optimization/cost_optimization.ipynb` — exists, but under top-level `cost_optimization/`, not the four folders |
| 37 | cost_optimization_evals | ✗ no match | Covered inside `cost_optimization.ipynb` (eval-driven) |
| 38 | production_best_practices | ≈ paraphrase | `managed_agents/CMA_operate_in_production.ipynb` |
| 39 | production_monitoring | ≈ paraphrase | `observability/usage_cost_api.ipynb` |

Score: **3 exact, 19 paraphrases, 17 no direct match** (of 39 names; the post says 40 but only 39 names were captured — one may have been missed in the slideshow, or the post miscounts).

The post's four-folder framing also misses where the most production-relevant material lives: `cost_optimization/`, `latency_optimization/`, `managed_agents/`, `claude_agent_sdk/`, `patterns/agents/`, `observability/`, `capabilities/`. The repo is bigger than the post's map.

## The 5 notebooks read (real paths, not the post's)

The task's five paths don't exist as written. These are the real equivalents, read in full intro + core sections:

### 1. `skills/notebooks/01_skills_introduction.ipynb` (the post's "use_a_skill")

What it teaches: the Skills feature end to end — setup (venv, `.env`, Anthropic SDK ≥ 2.0.0), what skills are ("expertise packages" Claude discovers and loads dynamically), and why they beat raw prompting. Key content:
- **Skills vs MCPs, stated by Anthropic itself:** skills are higher-level than individual tools — they combine instructions, code, and resources; composable; efficient via progressive disclosure; they ship proven helper scripts.
- **Progressive disclosure, 3 tiers:** metadata (name ≤ 64 chars, description ≤ 1024 chars) always visible → full instructions (< 5k tokens) loaded when relevant → linked files/scripts loaded only if needed.
- **Token math (their numbers):** manual instructions 5,000–10,000 tokens/request vs skills metadata-only minimal, ~5,000 tokens only when the skill is used. "The 98% savings applies to the initial context. Once you use a skill, the full instructions are loaded."
- Built-in skills: `xlsx`, `pptx`, `pdf`, `docx`. Skills need the code-execution tool; created files come back as `file_id`s, downloaded via the Files API. Generation times: Excel ~2 min, PowerPoint 1–2 min, PDF 40–60 s.
- Quick starts for Excel, PowerPoint, PDF.

### 2. `skills/notebooks/03_skills_custom_development.ipynb` (the post's "create_a_skill")

What it teaches: how to build, deploy, and manage custom skills. Key content:
- **Structure: `SKILL.md` is the ONLY required file.** Everything else optional: extra `.md` files (all loaded, not just SKILL.md/REFERENCE.md), `scripts/`, `resources/` (templates, data).
- **Frontmatter limits:** `name` ≤ 64 chars (lowercase alphanumeric + hyphens), `description` ≤ 1024 chars; instructions < 5,000 tokens recommended.
- **API workflow (SDK 2.x, GA — no beta header):** `client.skills.create(display_name=..., files=files_from_dir(path))`, then use via `container={"skills": [{"type": "custom", "skill_id": ..., "version": "latest"}]}` in `messages.create`.
- Utility functions for create / list / delete / test skill, with versioning (deleting a skill deletes all versions).
- Three worked examples: financial ratio calculator, company brand guidelines skill, financial modeling suite. Management & versioning + best practices sections.

### 3. `tool_use/memory_cookbook.ipynb` (the post's "tool_use_with_memory" / "agent_with_memory")

What it teaches: context editing + memory for long-running agents — Anthropic's own implementation of the file-based memory idea from the reyainami talk. Key content:
- **Memory tool (`memory_20250818`):** Claude writes what it learns for future reference; file-based system under a `/memories` directory; client-side implementation, you keep full control. Supported on Opus/Sonnet/Haiku 5.5.
- **Context editing:** `clear_tool_uses_20250919` (clears old tool results as context grows) and `clear_thinking_20251015` (manages extended-thinking blocks), with configurable triggers and retention.
- The pitch: "Session 1: Claude solves a problem, writes down the pattern. Session 2: Claude applies the learned pattern immediately (faster!)." Demo is a code review assistant that learns debugging patterns; also covers research assistant, support bot, data analysis helper.
- Best-practices section covers memory security and organization (the poisoning problem, in Anthropic's own words).

### 4. `claude_agent_sdk/01_The_chief_of_staff_agent.ipynb` (the post's "effective_agent_design")

What it teaches: building a Chief of Staff agent with the Claude Agent SDK (`ClaudeSDKClient`, `ClaudeAgentOptions`), Opus 5.5 for planning — the direct template for the crew's Grok Bot Chief of Staff plan. Key content:
- Scenario: AI Chief of Staff for a 50-person startup, coordinating specialized subagents, aggregating insights, giving executive summaries. Features introduced one at a time with What/Why/How: **CLAUDE.md memory → Bash tool → subagents → hooks → output styles → plan mode**.
- **The CLAUDE.md caveat (important):** agents naturally prefer granular data files over CLAUDE.md. "CLAUDE.md provides *context and guidance*, not hard constraints on data sources." You steer it with explicit prompt phrasing ("high-level financial numbers from context"). Design rule: CLAUDE.md holds high-level context, strategy, and pointers to where detailed data lives.
- Bash tool section: scripts live in a directory the agent can reach, described in CLAUDE.md (or the subagent's MD file). Five toy scripts: hiring impact, talent scorer, simple calculation, financial forecast, decision matrix.

### 5. `managed_agents/CMA_operate_in_production.ipynb` (the post's "production_best_practices")

What it teaches: the machinery around the agent loop before you put a Managed Agents app in front of real users. Key content:
- **MCP toolsets:** the agent calls an external MCP server directly from inside the sandbox; Anthropic proxies, no round-trip through your app. Rule of thumb: public internet + bearer token → MCP works; internal-only network → use a custom tool instead.
- **Vaults:** per-end-user credential containers, registered once, referenced by ID on every session. The agent never sees the token; the audit trail is tied to the vault (you always know which end user the agent acted for).
- **Webhooks for production human-in-the-loop:** register a webhook for `session.status_idled` (agent done OR waiting on a tool result) — your server inspects events, puts pending escalations in front of a reviewer, POSTs `user.custom_tool_result` back whenever the human finishes. No long-lived connection held open. Also `session.budget_reached` for spend caps. Webhook secret (`whsec_...`) shown once at creation.
- Resource lifecycle verbs (list/retrieve/update/archive/delete) and `inference_geo` pinning for compliance.
- End-to-end demo: vault → GitHub Copilot MCP credential (static bearer) → session with `vault_ids` → run a turn as the end user.

## Verification — what checks out, what doesn't

| Claim | Status |
|---|---|
| Repo exists: `anthropics/claude-cookbooks`, public, MIT, official Anthropic org | **VERIFIED** — live at main, commit `8ad5de64`, 652 commits |
| 55k+ stars | **ESSENTIALLY VERIFIED** — 54,955 stars at check (Nov 22, 00:23 UTC), 6,681 forks, 637 watchers. 45 stars short of 55,000; the post rounds up. Will cross 55k any day. |
| 91 notebooks | **MISMATCH** — the repo's own `registry.yaml` lists **98** notebooks (counted entry by entry: 33 + 38 + 27 across the file's three pages). At least one more file exists in the tree but not the registry (`tool_use/tool_search_alternate_approaches.ipynb`), so the true file count is ≥ 98. The post's 91 is stale or undercounted. |
| 100+ notebooks (thumbnail) | **MISMATCH, other direction** — 98 registered, not 100+. Thumbnail and text disagree with each other and with the registry. |
| 40 handpicked notebooks listed | **PARTIAL** — only 39 names captured; 3 exist verbatim at the stated paths, 19 are paraphrases of real notebooks, 17 have no direct match. See audit table. |
| "Anthropic quietly put [them] on GitHub" (new drop) | **MISLEADING** — repo created Aug 15, 2023; a living public repo with additions as recent as Nov 2, 2026. Not a new or quiet drop. |
| "Cleanest FREE path" | **VERIFIED with a caveat** — reading the notebooks is free; *running* them needs an Anthropic API key and spends API tokens (they're API notebooks, not Claude Code). The crew builds on Claude Code (subscription), so treat these as reference/patterns, not runnable code, unless API spend is approved. |
| Notebooks are tested | **VERIFIED** — repo ships `.claude/skills/cookbook-audit` (a skill + `validate_notebook.py`) and CI workflows (`notebook-tests.yml`, `notebook-quality.yml`). Not untested dumps. |
| Video has content to transcribe | **N/A — no audio.** Infographic slideshow only; video-only formats, no audio track. Post text is the content. |

## INTEGRATION — what this changes for the owner's crew

The crew (Claude builds, Grok, Atlas challenges, GPT-6 reviews) builds with Claude Code. The ishh_021 Claude course research already established: **skills beat MCPs on cost, MCPs win on setup speed — prototype with an MCP, convert to a lean skill**. These cookbooks are the official reference for the second half of that pipeline, and they add three things the course didn't have: the exact skill spec, the production machinery, and the memory implementation.

**What maps to live work:**
- **MCP→skill conversion (highest value):** notebooks 01 + 03 are the spec. When Claude converts the crew's Gmail/Instagram MCP tooling into lean skills, the rules are: one `SKILL.md` (name ≤ 64 chars, description ≤ 1024 chars, instructions < 5k tokens), scripts + templates as resources, progressive disclosure doing the cost work (metadata-only until used). Notebook 01's token math is the cost argument for the conversion.
- **Chief of Staff (Grok Bot plan, Nov 22):** `01_The_chief_of_staff_agent.ipynb` is the template — one primary orchestrator, specialized subagents, CLAUDE.md as memory, Bash tool for scripts. Its CLAUDE.md caveat is a direct warning for the hivemind charter: the charter is context, not a constraint — enforcement needs explicit prompt phrasing and the challenger (Atlas) as the check, not an assumption the agent will obey the file.
- **Memory + dreaming:** `memory_cookbook.ipynb` is Anthropic's own file-based memory (memory tool + `/memories` dir + context editing) — the production version of the reyainami talk's endpoint. Its best-practices section on memory security/organization is a second vote for the poisoning guardrails (versioning, permissioning, human accept/reject) already planned for the weekly dreaming job.
- **Webhooks beat polling (again):** `CMA_operate_in_production.ipynb` makes the same point as the Grok Bot Q&A — webhooks (`session.status_idled`, `session.budget_reached`) instead of holding connections or polling. The hivemind's 5-minute hook poll should move to GitHub webhooks; this notebook is the reference for how.
- **Spending caps:** `CMA_cap_session_spend.ipynb` (referenced in the production notebook) is the answer to the ishh_021 warning (agent teams burning ~$80 in 15 min): an enforced list-cost budget per session with a `budget_reached` pause. Any agent-team work gets a cap before it runs.
- **GEO audit pipeline / payment checks:** `cost_optimization/cost_optimization.ipynb` (eval-driven, apply cost levers one at a time, find the Pareto-optimal config) and `latency_optimization/latency_optimization.ipynb` are the eval-driven loop for the GEO pipeline and `payment_check.py`. `misc/building_evals.ipynb` is the evals starter. The post's `price_perf_evals` names don't exist — these are the real ones, and both are dated Aug–Nov 2026 (the newest material in the repo).
- **Subliminal app:** `patterns/agents/` (basic workflows, evaluator-optimizer, orchestrator-workers) for the app's agent features; `claude_agent_sdk/06_The_vulnerability_detection_agent.ipynb` as a security-review pattern.

**Read-first order for the crew:** 01 intro → 03 custom skills → memory_cookbook → 01 chief of staff → CMA operate in production → cost_optimization. Six notebooks, in that order, cover the whole pipeline from "what is a skill" to "how do we run agents in production with a budget."

**What NOT to do:** don't paste the post's 40 paths into any doc, README, or message to Claude/Grok — 36 of 39 are wrong as written and will send the crew to dead links. Use the audit table's real paths. Don't run the notebooks on the API without approval — reading is free, running costs tokens. Don't treat the post's "100+" or "91" as the count; the registry says 98.

**Version drift warning (from reading the notebooks):** the skills notebooks mix two API styles — notebook 03 uses the SDK 2.x GA Skills API (`client.skills`, no beta header) while notebook 01 still uses `client.beta.messages.create()` with `betas=[...]` in places. Check the installed SDK version before copying code; prefer the GA style.

## Most actionable integration (single item)

**Give Claude the skill spec from notebooks 01 + 03 as the conversion target for the MCP→skill pipeline: one `SKILL.md` per tool area (name ≤ 64 chars, description ≤ 1024 chars, instructions < 5k tokens, scripts + templates as resources), starting with the Gmail tooling — and pair it with the `CMA_cap_session_spend` budget pattern before any agent-team run.** That turns the ishh_021 "prototype with an MCP, convert to a lean skill" rule from a slogan into a checkable spec with a spending guardrail.

## Sources

- Post: https://x.com/mentalium_/status/2124177042778321182/video/1
- Repo: https://github.com/anthropics/claude-cookbooks (main, commit `8ad5de64`; stars 54,955, forks 6,681, at Nov 22, 00:23 UTC)
- Registry (98 entries, counted): https://raw.githubusercontent.com/anthropics/claude-cookbooks/main/registry.yaml
- Folder listings (live): `tool_use/`, `skills/`, `multimodal/`, `misc/` directory pages at main
- Notebooks read: `skills/notebooks/01_skills_introduction.ipynb`, `skills/notebooks/03_skills_custom_development.ipynb`, `tool_use/memory_cookbook.ipynb`, `claude_agent_sdk/01_The_chief_of_staff_agent.ipynb`, `managed_agents/CMA_operate_in_production.ipynb` (raw JSON, intro + core sections)
- Prior crew research: `~/workspace/research/ishh_021-claude-full-course.md` (MCP→skill pipeline), `~/workspace/research/reyainami-self-prompting-systems.md` (memory + dreaming)
