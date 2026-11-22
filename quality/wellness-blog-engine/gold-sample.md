# Wellness Blog Engine — Gold sample (Quality Gate step 2 record, step 3 packet)

**Status:** written 2026-11-22 (Claude, 22:25 UTC hourly run). The post itself is `gold-sample-002-winter-sun.md` (written earlier on PR #16). This page puts the sample, its checks and its sources in one place so Atlas can score step 3 and the owner can do step 4 from one page. **Nothing posted, nobody contacted. Winter Sun has not been contacted.**

## The business
**Winter Sun Trading Co.**, an herb shop and apothecary in Flagstaff, AZ. It sells dried ashwagandha root, and its "Apothecary Journal" blog's newest visible post is from 2020 (`prospect-blog-check.md`). It is a real, public business, so this sample tests the actual use case: an ingredient post for a shop that already stocks the herb. It is a spec sample, not paid work.

## The deliverable
`gold-sample-002-winter-sun.md`: an 1,052-word post with 3 headline options, a meta title and description, labelled TRADITIONAL / PROVEN / FRINGE sections, a "who should skip it" safety block, a CTA placeholder for the shop's own product page, 3 opened sources and a hero-image note.

## Checks (code, run 2026-11-22 22:25 UTC)
| Check | Result |
|---|---|
| `post_lint.py --presale` (Gravity-Studio) | **OK**, 1,052 body words |
| `check_posts.py` eval rules (Gravity-Studio PR #55) on this **real** sample. Its gold set only held sample 001 before. | **OK**: headline, disease, safety, lineage and testimonial rules all pass |
| `gold_eval.py gold-sample-002-winter-sun.md` (new): eval rules + every quotation in the body checked against the source page | **OK: 15 of 15 quotations are on an opened source page**, exit 0 |
| `gold_eval.py --test`: errors planted in this real post | **7/7 caught**: cure in a headline, a disease claim in the body, the safety block cut, "3,000 years" with no source, an invented customer story, a quote stretched ("reliably reduces"), and a quote invented and pinned on NIH. Unit 3/3 |

**Bug found and fixed (Gravity-Studio PR #56, branch `claude/wellness-negation-scope`, stacked on PR #55).** The plant *"ashwagandha reverses diabetes and is not a quick fix"* passed both checkers. So did *"It cures anxiety, no prescription needed."* Any "not" or "no" anywhere in a sentence cancelled the claim. Now a negation only counts when it governs the claim (same clause, before the claim word), so *"has not been shown to treat cancer"* is still fine. The new tests are post_lint 19/19 and check_posts 10/10 caught + unit 9/9. Both real samples still pass. This is the same kind of hole our buyers' complaints are about: a confident claim that slips through.

## Sources, opened 2026-11-22
Every quotation below was found **verbatim** on the page (straight vs curly quotes ignored).
| # | Source | Quotes | Also confirmed |
|---|---|---|---|
| A | Singh et al. 2011, *AJTCAM* 8(5 Suppl):208–213, pmc.ncbi.nlm.nih.gov/articles/PMC3252722 | 5 (name, rasayana, churna, milk, "Large scale clinical studies are needed…") | — |
| B | NIH ODS Health Professional Fact Sheet, **Updated: May 2, 2025** | 8 (Unani/adaptogen, both dose lines, "may help reduce…", "challenging to develop recommendations", 3-month tolerance, liver, thyroid) | 7 studies / 491 adults / 6–8 weeks / 240–1,250 mg; 5 studies / 372 adults / 6–12 weeks; Denmark banned it in 2023 |
| C | Memorial Sloan Kettering, About Herbs, **Last Updated: July 28, 2026** | 3 (pregnancy, autoimmune, "not been observed in humans") | — |

**Said straight (for Atlas's row 1):**
- The "Large scale clinical studies" quote stops where the page goes on: *", specially in stress related diseases, neuronal disorders and cancers."* The cut drops a scope, not a hedge, and the post claims nothing about those diseases.
- NIH says the 7 stress studies were "all **from** India". The post says "all in India", which is a paraphrase, not a quote.
- The bullet "It 'might also affect thyroid function'" sits under a line naming both NIH and MSK. The words are NIH's.
- What code can't check: whether the post says more than its sources in its own words (rubric row 1), and whether the kitchen method reads as a dose. The post calls it *"a kitchen method, not a tested dose"*. That's for Atlas's read.

## Benchmark, for rows 4–6
`benchmark.md`: $150/mo for 4 posts beats agencies ($390–$600/mo), **matches but doesn't beat** the best Fiverr writer (wafa_94, $30 per 1,000 words, verified live by Atlas), and loses on price to $99 software (never pitched as cheaper than software). Buyer complaint #1 (3 of 5): AI-written or copied text sold as a writer's work. Our fix is to say AI-assisted up front, check every claim against a source, and take payment only after the buyer approves post 1. Claude's suggested row 6 was 4/5; Atlas decides.

## Step 3 result (Atlas, Nov 22 ~22:40 UTC, PR #35 comment)
**PASS at 4.5**: rubric 4 / 5 / 5 / 4 / 5 / 4 (faithful 4, lineage 5, safety 5, buyer-specific 4, reads like a person 5, publish as is 4). He re-opened all 3 pages himself and found the 15 quotes verbatim, reproduced the 7/7 plants and the missed plant on PR #55's branch. His 2 fixes were made 22:45 UTC: "all from India", and "All but one of the trials used concentrated extracts" (NIH: one study used "12,000 mg/day of whole root granules"). Checks re-run: `gold_eval.py` OK 15/15, `--test` 7/7, `post_lint --presale` OK (1,077 words). Not re-verified by Atlas: Winter Sun's 2020 blog date.

## For Atlas (step 3): score with `QUALITY_GATE.md` rows 1–6 + `evals/RUBRIC.md` rows 1–6
Re-open the 3 sources yourself; don't take the table above on trust. Gate bar: code checks exit 0, average ≥ 4.5, no score below 4.

## For the owner (step 4), after Atlas scores it
Read the "What the research has tested" and "Who should skip it" sections. Question: **"Would I pay $150 a month for four of these on my shop's blog?"**
