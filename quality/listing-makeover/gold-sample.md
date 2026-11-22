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

**Why a hardness check:** each listing states a Mohs hardness under *Proven*. A wrong number there would be a false "proven" fact on a live shop, which breaks scorecard row 1 (Accuracy). `mohs_check.py` holds a table of values copied from pages opened today (USGS gemstone minerals, the International Gem Society hardness chart, GIA amber, geology.com and minerals.net aventurine, CAMEO obsidian). It fails any listing value outside the sourced range and any stone with no source.

**What it changed:** Green Aventurine said "Mohs ~6.5". The sources say 6.5–7 (geology.com, minerals.net) or 7 (IGS). That wasn't wrong, but it was at the low edge, so it now reads **"Mohs 6.5–7"** (davias `fb2055e`). Note: that commit's message says the check "found" it. More exactly, the sourcing work behind the check found it; the check itself accepts "~6.5".

**Open for Atlas (local browser):**
1. **Tiger's Eye "Mohs ~7":** consistent with quartz at 7 (USGS). But no page that names tiger's eye could be opened from the cloud (geology.com's tiger's-eye page is off the allowlist).
2. **Obsidian "Mohs 5–5.5":** CAMEO gives 5–7, so 5–5.5 fits inside that range, but no opened page states 5–5.5 exactly. If a gem reference such as GIA says 5–5.5, add it to `SOURCES`. If not, the listing should say "about 5–6".

## Owner read (step 4) — what to look at
Read listing 1 (Violet Vortex) and listing 8 (Amber Mist) in `gold-sample-listings.md`. The question: **"Would I pay $79 to get 20 of these for my shop?"** The titles to judge are the fixed ones (10–12 words). The older 15+ word titles are gone.

## What's left for the gate
- **Step 1:** benchmark drafted (`benchmark.md`); Atlas verifies it.
- **Step 3:** Atlas scores this sample with `RUBRIC.md` (Gravity-Studio PR #52) and the benchmark.
- **Step 4:** owner read (above).
- **Step 5:** free trial with SweetSoftSkin (2 listings rewritten free), using the same route check as the Review Desk trial.
