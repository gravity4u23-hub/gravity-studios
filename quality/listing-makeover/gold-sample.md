# Listing Makeover — Gold sample (Quality Gate step 2)

**Status:** step 2 record written 2026-11-22 (Claude, 20:25 UTC hourly run). The listings themselves were written earlier on davias PR #7 (branch `claude/helix-listings`); this file puts the gate's sample, its checks and its sources in one place so Atlas can score step 3 and the owner can do step 4 from one page. **Nothing posted, nobody contacted.**

## The business
**Davias Earthbound Jewelry**, the owner's own crystal bracelet shop. The gate allows "a real (public) business or our own". It is our own, so this sample proves the writing, **not** that a buyer wants it (that's step 5).

## The deliverable
`gold-sample-listings.md`: 12 Etsy-ready listings for the Helix collection, each with a title, description and 13 tags. Copied verbatim from davias `HELIX_LISTINGS.md` at commit `fb2055e`.
- Titles follow Etsy's current guidance: under 15 words, no repeated word, stones first.
- Every stone has a *Proven* line (mineral facts) and a labelled *Tradition* line, which is lore and never a health claim.
- Things the seller hasn't told us stay as questions: price is "Ask for price" and size is `[size]`.

## Checks (code, run 2026-11-22)
| Check | Result |
|---|---|
| `listing_lint.py gold-sample-listings.md --strict-titles` (Gravity-Studio PR #46) | **12/12 pass**, 12 WARN = `[size]` is still open for the seller (expected) |
| `mohs_check.py gold-sample-listings.md` (new, this PR) | **18/18 stones match an opened source**, exit 0; 2 OPEN for Atlas (below) |
| `mohs_check.py --test` | 8/8 |
| `gold_eval.py gold-sample-listings.md` (new, 21:25 UTC run): the eval set's code rules (Gravity-Studio PR #52 `check_listings.check`) run on these 12 **real** listings, with Davias's own intake (`helix-intake.json`, verbatim from davias `HELIX_COLLECTION.md` @ `005b877` + README maker line) as the source of truth | **11/12 pass**, exit 1. Every number is the seller's or a sourced Mohs value; no banned word; `[size]` kept as a question. **1 FAIL: Jungle Gold (citrine), below** |
| `gold_eval.py --test` | 8/8. Planted "8 mm beads, sterling silver clasp" in every listing → 0/12 (invented number + "sterling" caught); planted "fits most wrists" for `[size]` → 0/12 |

**Why a hardness check:** each listing states a Mohs hardness under *Proven*. A wrong number there would be a false "proven" fact on a live shop, which breaks scorecard row 1 (Accuracy). `mohs_check.py` holds a table of values copied from pages opened today (USGS gemstone minerals, the International Gem Society hardness chart, GIA amber, geology.com and minerals.net aventurine, CAMEO obsidian). It fails any listing value outside the sourced range and any stone with no source.

**What it changed:** Green Aventurine said "Mohs ~6.5". The sources say 6.5–7 (geology.com, minerals.net) or 7 (IGS). That wasn't wrong, but it was at the low edge, so it now reads **"Mohs 6.5–7"** (davias `fb2055e`). Note: that commit's message says the check "found" it. More exactly, the sourcing work behind the check found it; the check itself accepts "~6.5".

**Open for Atlas — RESOLVED 2026-11-22 (Atlas, browser):**
1. **Tiger's Eye "Mohs ~7" — CONFIRMED.** Wikipedia infobox gives tiger's eye Mohs **6.5–7** (en.wikipedia.org/wiki/Tiger's_eye, opened 2026-11-22); geology.com classes tiger's eye as a quartz gemstone, hardness 7. Listing "~7" sits inside 6.5–7. `SOURCES` updated, open flag removed.
2. **Obsidian "Mohs 5–5.5" — CONFIRMED exactly.** IGI: "On the Mohs hardness scale, obsidian sits at around 5-5.5" (igi.org/all-about-colored-stones-obsidian, Mark Reyes G.G., opened 2026-11-22); Fire Mountain Gems lists "Hardness: 5 to 5-1/2 (Mohs)". `SOURCES` now (5, 5.5), open flag removed. `mohs_check.py` re-run: **18/18, 0 OPEN**, self-test 8/8.

## New finding, 2026-11-22 21:25 UTC: citrine needs a treatment answer
Every listing says *"Every stone is natural."* For Jungle Gold that's not safe yet:
- **GIA:** *"Since natural citrine is rare, most of the citrine on the market is the result of heat treatment"*, which turns pale amethyst yellow (gia.edu/citrine-description; same on gia.edu/gia-faq-treated-citrine, both opened 2026-11-22).
- **FTC Jewelry Guides** (FTC's own summary, "Loupe" business guidance, opened 2026-11-22): sellers *"should tell consumers about the treatment if it significantly affects the value of the gemstone."*
- Atlas already raised this on davias (ATLAS_REVIEW: "is the citrine natural or heated amethyst"), and it's still unanswered.

**Fix, two ways:** (a) the owner or Octavia says which it is and the line states it; or (b) until then the citrine line carries the question: *Citrine: [natural or heat-treated? confirm with the maker]*. That's how we already treat `[size]` and price. Either way `gold_eval.py` passes. **The davias listing is not edited here** (Davias is paused; this is an owner-read item).
**Why it matters for the gate:** this is the exact failure we sell against, a confident fact the seller never gave us. Finding it in our own sample is scorecard row 1 working. Black onyx is often dyed too, but no source was opened for that yet, so it is **not** in the check. Atlas: if a gem reference you can open says so, add it to `TREATED`.

## Scorecard draft for Atlas (step 3)
| Row | Score | Evidence |
|---|---|---|
| 1 Accuracy | Atlas | Mohs 18/18 sourced, 0 OPEN (Atlas, browser); 11/12 eval-rule pass; Jungle Gold citrine open (above) |
| 2 Specificity | Atlas | Each listing names its own stones, helix build and color matching from the seller's intake |
| 3 Usefulness | Atlas | Paste-ready except `[size]` (12) and the citrine question (1), both questions the seller must answer |
| 4 Speed | Atlas | Starter same day, Fiverr Basic 1 day vs the 2–3 day norm (Uri 3, Contra 3, Natalia 2, PeoplePerHour 2 or 4; `benchmark.md`) |
| 5 Price/value | **4/5 conditional** (Atlas, PR #14 review) | Condition was "$5 claim sourced or corrected": benchmark now sources the $5 as Uri B.'s active gig ($50 for 10 = $5.00 a listing); Natalia's $15 package covers 2 ($7.50 each) (commit `ae7026e`, merged into this stack in this PR) |
| 6 Complaint fix | **4/5 → 5/5 once confirmed** (Atlas, PR #14 review) | Both conditions are met: 8/12 recount fixed (`d688eb3`) and the PR #46 stopword fix landed (Gravity-Studio `212fab6` + `dddcb18`, 25/25) |
Rubric (Gravity-Studio `portfolio/listing-makeover/evals/RUBRIC.md`): pass = code checks exit 0 **and** average ≥ 4.5 with no score below 4. So step 3 can't pass until the citrine line is fixed.

## Owner read (step 4) — what to look at
Read listing 1 (Violet Vortex) and listing 8 (Amber Mist) in `gold-sample-listings.md`. The question: **"Would I pay $79 to get 20 of these for my shop?"** The titles to judge are the fixed ones (10–12 words). The older 15+ word titles are gone.

## What's left for the gate
- **Step 1:** Atlas PASS conditional (PR #14 review); all fixes made on PR #14 and merged into this stack 2026-11-22 21:25 UTC (they had been left out of the stacked branches).
- **Step 3:** citrine line fixed (owner answer or question), then Atlas scores rows 1–4 + `RUBRIC.md` and confirms 5–6.
- **Step 4:** owner read (above).
- **Step 5:** free trial with SweetSoftSkin (2 listings rewritten free), using the same route check as the Review Desk trial.
