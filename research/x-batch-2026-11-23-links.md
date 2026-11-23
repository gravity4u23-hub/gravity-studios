# X-batch, 2026-11-23: 13 owner links, prompts and Claude jobs

**Claude, 2026-11-23 ~09:30 UTC.** David asked me to watch and read these 13 links myself, pull every prompt word for word, and build the Claude jobs from them.

## What I could and couldn't open
- **I could not open any of the 13 X pages.** Every fetch was refused (`robots_disallowed` on x.com) at about 08:40 UTC. I did not try mirrors or workarounds; the rules don't allow them.
- **So the words below come from the transcripts Atlas already made** of these videos with a local speech-to-text model (faster-whisper). They are on main in `research/x-batch-implementation-pack-2026-11-22-CLEAN-NEUTRAL.md`. **9 of the 13 links are in that pack.**
- **I read the transcripts myself.** Where the pack says "No prompts in source", I checked the transcripts and found that 4 videos do contain prompts spoken or read aloud.
- **Every prompt is in `x-batch-2026-11-23-prompts.json`.** `verify_prompt_quotes.py` proves each one is in its transcript, character for character, at the stated time.
- **Speech-to-text errors are kept on purpose** (e.g. "tic-tac 2 app", "obviocavideg"). They are the transcript's words. I didn't guess what was really said.

## Per link
| # | Link | What I had | Prompts (verbatim) | Claude job → status |
|---|---|---|---|---|
| 1 | ishh_021/2123725546748010592 | Not in the repo; the page can't be opened from the cloud. Another research file mentions an "ishh_021 course" (subagent reliability 0.95^n) from Atlas's local notes, which aren't in the repo | **No prompts available. I could not read the source.** | None until someone pastes the text or Atlas commits the transcript |
| 2 | dipanshu_ai/2124475801542553677 | Pack §20: Claude "full course" livestream, about 58 min | **17 prompts** in the json (e.g. "save this as a skill call it YouTube titles", 00:45:21) | **Done:** the self-improving hook loop (00:23:33–00:24:20) → `tools/hook_feedback.py` |
| 3 | mentalium_/2124177042778321182 | `research/mentalium-claude-cookbooks.md` (main). The video is an infographic with no audio track | **No prompts in source** | Already applied Nov 21 (eval sets per service, from the cookbooks' `building_evals`) |
| 4 | rrrangle/2124201044498690557 | Pack §18: Anthropic webinar on Claude Code tokens, about 26 min | **4 prompts** (e.g. "fix the failing test in utils test. Yes", 00:02:29) | **Done:** a lean `CLAUDE.md` plus a quiet runner `tools/run_checks.py` (00:12:37–00:12:47, "a quiet reporter that only prints the failures") |
| 5 | rahultechx/2124428712888369185 | Pack §9: Anthropic "prompting playbook" talk, Code with Claude, about 32 min | **10 prompts** (system-prompt lines read on screen plus 3 eval test messages) | **Done:** a control case and case kinds in our eval sets, plus `quality/eval_coverage.py` (00:03:59: "Those three key cases include having a control case,") |
| 6 | reyainami/2123813338920415441 | Not in the repo. Another research file cites `reyainami-self-prompting-systems.md` in Atlas's local workspace, which isn't committed | **No prompts available. I could not read the source.** | None until the transcript is committed |
| 7 | ky_markets/2124547322822430961 | Pack §8: AI-UGC affiliate video, about 2.5 min | **No prompts in source.** The speaker says "comment UGC" to get them; they aren't in the video | Reviewed, not applied: it needs paid image, video and voice tools before the first dollar, which breaks the bootstrap rule. "One offer, 904 conversions" can't be checked. Of its 4 safety rules, only "no health promises" is already in our `social_check.py` (Gravity-Studio PR #40, which bans cure and heals). Label AI, no real logos and "chance to win" never "free" are not; we have no AI-character or giveaway posts planned |
| 8 | realdrovex/2124534202863440194 | Pack §4: "No transcript in source" | **No prompts in source** (nothing captured) | None |
| 9 | crangerus/2124536678219919582 | Pack §17: Karpathy-style "how I use LLMs", about 65 min | **17 prompts** (e.g. the custom GPT instruction "So first OCR it, then translate it and then break it down", 01:02:02) | Reviewed, not applied as new code. Its lesson (save a prompt you keep reusing, with examples) is what our `skills/` already do |
| 10 | adarshchetan/2124342810463879389 | Pack §12: "No transcript in source" | **No prompts in source** (nothing captured) | None |
| 11 | k1rallik/2124200644366278753 | Pack §1: "No transcript in source" | **No prompts in source** (nothing captured) | None |
| 12 | sharfovii/2124212188000686475 | Pack §10: Karpathy clip on coding with agents, about 4.5 min | **No prompts in source** | Already our practice: agents for boilerplate, and tests whenever AI writes code ("I have tests. So I feel safer", 00:04:04). Every tool we ship has self-tests |
| 13 | aresotik/2124157077035892761 | Not in the repo; the page can't be opened from the cloud | **No prompts available. I could not read the source.** | None |

## Built from the links (gravity-studios PR, this branch)
| Job | Files | Proof (run on this branch) |
|---|---|---|
| Control case and case kinds (rahultechx) | `quality/eval_coverage.py`. The `kind` field was added to all 21 cases, plus 2 new control cases: `control-plain-update` in `quality/resume-linkedin/evals/cases.json` and `control-plain-audit` in `quality/geo-ai-search-check/evals/cases.json` | `eval_coverage.py` → 2 sets, 0 gaps; `--self-test` 6/6; `check_resumes.py` 21/21 (was 19/19); `check_reports.py` 27/27 (was 25/25). With `--gs`, the 3 Gravity-Studio sets (review, listing, wellness) show **gaps: no kinds, no control case**. That's a real gap, not yet fixed |
| Quiet checks + lean CLAUDE.md (rrrangle) | `tools/run_checks.py`, `CLAUDE.md` | `run_checks.py` → "27 checks run, 0 failed, 2 skipped". With both Gravity-Studio checkouts → "29 checks run, 0 failed". It also showed that the wellness self-test needs PR #56; base #55 alone fails 1 |
| Hook feedback loop (dipanshu_ai) | `tools/hook_feedback.py` | `--self-test` 8/8 on a SYNTHETIC fixture. **No real data yet:** Metricool has no network connected, so nothing has been posted |
| Prompt extraction | `research/x-batch-2026-11-23-prompts.json`, `research/verify_prompt_quotes.py` | 48 prompts, 0 errors against the pack; `--self-test` 4/4. The verifier caught 2 wrong timestamps in my first draft, both fixed |

## What David can do to fill the gaps
Paste the post text, or ask Atlas to commit his local transcripts, for **ishh_021, reyainami and aresotik**. Then **realdrovex, adarshchetan and k1rallik** have no captured text at all. They may be image or text posts that need a screenshot.
