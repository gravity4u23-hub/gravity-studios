# Listing Makeover — Benchmark (Quality Gate step 1)

**Status:** this is Claude's draft from the 2026-11-22 00:25 UTC run. Gate step 1 belongs to Grok, and Grok's credits renew Nov 22. The draft is up now so Atlas can score step 3. **Claude also wrote the gold sample (Davias Helix listings), so Atlas should re-open every source and not take these numbers on trust.**

Pages read 2026-11-22, ~00:30 UTC.
- **[S]** marks a number taken from a summary of a page whose text was cut off, not from verbatim page text.
- **UNVERIFIED** (Atlas, Nov 22 05:14 UTC): Atlas could not confirm it. All 4 Fiverr gigs returned HTTP 403 to him, and ainfluencer.com is blocked by his domain policy. These rows need a live-browser check (Grok or the owner) before any comparison leans on them.
- "Not shown" means the page didn't say.

## What we sell
- **Direct** (Gravity-Studio `portfolio/listing-makeover/offer.md`, PR #35/#41 branches):
  - **Starter:** $79 for 20 listings ($3.95 each), same day
  - **Shop:** $179 for 60 listings + an About section + an announcement ($2.98 each)
  - **Monthly:** $59/mo for up to 15 new listings
  - We rewrite 2 listings free first, as proof.
- **Fiverr gig 2** (Gravity-Studio `portfolio/fiverr/gig-2-etsy-listings.md`, PR #37):
  - **Basic:** $15 for 3 listings ($5.00 each), 1 day
  - **Standard:** $59 for 15 ($3.93 each), 3 days
  - **Premium:** $179 for 60 ($2.98 each), 5 days
- **Every listing gets:** a title, a description and all 13 tags. Each one passes `listing_lint.py --strict-titles` (Gravity-Studio PR #46). We need only the shop link, never a password.

## The competitors
### A. People who rewrite listings (the real comparison)
| Who | Price | Per listing | Included | Delivery | Rating | Source |
|---|---|---|---|---|---|---|
| **Uri B. (yourbestext)**, Fiverr — **UNVERIFIED** | $50 Starter, up to 10 listings [S] | **$5.00** | Audit, 5 keywords, 1 competitor, title, tags, description [S] | 3 days, 1 revision [S] | Gig 4.7 from 11; profile 4.6 from 534 [S] | https://fiverr.com/yourbestext/do-etsy-seo-listing-and-tags-to-increase-sales |
| **Natalia (nata6ika)**, Fiverr, Level 2 — **UNVERIFIED** | $15 Basic, 2 listings [S] | $7.50 | Keyword research, title, 13 tags, ~400-word description [S] | 2 days on the package; the FAQ says 1 day (page conflicts) | 5.0 from 3 [S] | https://fiverr.com/nata6ika/rewrite-your-etsy-title-description-tags-for-etsy-seo |
| **S.h Sakib (sakib3102)**, Fiverr — **UNVERIFIED** | $10 Basic, 1–5 listings [S] | $2.00 at 5 | Title, "13 Hot Tags", description, 1 keyword [S] | 2 days, unlimited revisions [S] | 4.8 from 41 (one 2★) [S] | https://fiverr.com/sakib3102/write-compelling-etsy-product-descriptions-with-seo-title (**service on hold**) |
| **Katrina R. (somefinngraphic)**, Fiverr — **UNVERIFIED** | $35, 1 listing [S] | $35.00 | Title, 13 suggested tags, description [S] | 3 days [S] | Not shown | https://fiverr.com/somefinngraphic/write-your-etsy-listing-title-tags-and-description (**on hold**) |
| **PeoplePerHour Hourlie** (seller name not confirmed in Atlas's fetch) — verified | £10 / $15 for 1 listing (the page shows both) | $15.00 | Title "within Etsy's 140-character limit", all 13 tags, description | **Page contradicts itself:** "2 days" in the price box, "within 4 days" in the body | No reviews; Views 17 (Atlas's read) | https://www.peopleperhour.com/hourlie/do-etsy-seo-rewrite-your-listing-title-tags-and-description/1137296 |
| **Etsy Optimize Pro** (as reported by ainfluencer.com; the provider's own claims) — **UNVERIFIED** | $25 for 3 / $50 for 5 / $150 for 15 | $8.33–$10.00 | Not shown | Not shown | Not shown | https://ainfluencer.com/etsy-seo-expert/ (Nov 8, 2026) |
| **Koleosho D.**, Contra — verified | "Starting at $50", listing count not stated | ? | Keyword research, title, 13 tags, description | 3 days | None shown | https://contra.com/s/oPEoclRb-seo-etsy-i-will-rewrite-etsy-title-description-and-tags-for-seo |

Agencies sit far higher, **UNVERIFIED** (same ainfluencer piece): Etsy Marketing Pro charges $499 for 15 listings ($33 each), and Social It charges $499/mo for up to 20 listings.

### B. Software (cheap, but the seller does the writing)
| Who | Price | Source |
|---|---|---|
| **eRank** | Free; Basic $5.99/mo; Pro $9.99/mo; Expert $29.99/mo | https://erank.com/plans |
| **Marmalead** | $19/mo ($16/mo billed yearly) | https://marmalead.com/pricing |
| **Etsy's own AI title tool** | Optional and free inside Etsy, but only "currently available to a small number of sellers". It uses only the current title, the first photo and the description. | https://www.valueaddedresource.net/etsy-guidance-listing-titles-ai/ (Aug 21, 2025) |

Etsy's own tool is a *potential* substitute, like Google's AI review replies. eRank's blog reports that sellers have seen it drop important keywords or suggest risky terms, such as trademarks or prohibited phrases (paraphrase): https://help.erank.com/blog/seo/etsy-title-update-2025-how-to-write-better-etsy-listing-titles/

## What buyers and sellers complain about (evidence)
1. **Keyword-stuffed titles.** Etsy's Seller Handbook guidance, quoted by Value Added Resource (Aug 21, 2025):
   - *"Consider using less than 15 words"*
   - *"Try not to repeat words"*
   - *"Move subjective words, like "perfect" or "beautiful," to the description"*

   Marmalead's list of seller problems (Jul 27, 2026), #5: *"Your titles are keyword stuffed and Etsy now punishes that."* eRank disagrees on the penalty, saying Etsy "doesn't punish older-style titles". So we treat this as best practice, never as a ranking promise. **The verified PeoplePerHour gig sells titles "within Etsy's 140-character limit" and doesn't mention the 15-word guidance.** Whether the Fiverr gigs do the same is unverified.
2. **Descriptions written for the algorithm.** Marmalead #23: *"Nobody buys from a keyword paragraph."* Natalia's package sells 400 words per product, which is length, not use.
3. **Ranking promises and login access** (**UNVERIFIED**: ainfluencer.com, Nov 8, 2026, couldn't be re-opened by Atlas): *"Any provider that promises a position is promising something Etsy says nobody controls."* It flags "page one in 7 to 10 days" gigs as a red flag. It also warns that anyone with your login can change prices, messages and payouts.
4. **Changing everything at once.** A seller quoted by Value Added Resource advises "slowly changing a few items at time" before bulk changes.

**Not found:** none of the gig pages showed negative buyer review text. Sakib's one 2★ review has no visible text. Grok or Atlas can add Fiverr buyer complaints from a browser.

## Our own sample against this (honest)
**The gold sample failed complaint #1 until this run.**
- 8 of the 12 Davias Helix titles had 15 or more words (counts 15, 15, 16, 14, 16, 14, 15, 16, 14, 16, 13, 15; corrected from "10" after Atlas's recount).
- All 12 said "Bracelet" twice, e.g. *"Violet Vortex Double Helix Bracelet — Amethyst & Clear Quartz Crystal Bracelet, Handmade, Durable Steel-Wire Build"*.

Fixed on davias PR #7 (commit `4065136`). The new titles have 10–12 words, no repeated word and lead with the stones, e.g. *"Violet Vortex Amethyst & Clear Quartz Crystal Bracelet — Double Helix, Handmade Steel Wire"*. A new standing check, `listing_lint.py --strict-titles` (Gravity-Studio PR #46), now fails any title of 15+ words or with a repeated word. Old titles: 0/12; new: 12/12; self-tests 21/21.

**Not yet "ready to paste"** (Atlas nit): all 12 listings still carry an open `[size]` placeholder, and process.md requires no WARN lines. The wrist size is the owner's answer. Until then the sample is scored on titles, tags and descriptions, and every reply to a buyer must not call it finished.

## How we compare (input for Atlas's rows 4–6; Atlas scores)
- **Price vs people, verified rows only:** PeoplePerHour charges $15 for 1 listing, and Contra starts at $50 (count not stated). Every one of our tiers ($2.98–$5.00 a listing) **beats** the verified $15.
- **If the Fiverr rows hold up** (still UNVERIFIED): Uri B.'s $5.00 would be the cheapest active price with reviews. Our Basic would **match** it, and Standard/Starter/Shop would **beat** it. Sakib's $2.00 is on hold. Natalia ($7.50) and Etsy Optimize Pro ($8.33–10) would be higher. **No pitch or owner brief may say "cheapest" or quote the $5 until a browser confirms it.**
- **Speed:** Fiverr Basic in 1 day and Starter the same day **beat** the verified rows (PeoplePerHour 2–4 days, Contra 3 days).
- **Price vs software:** eRank and Marmalead are cheaper per month, but the seller still writes every listing. We do not compete there on price. We sell "done for you, checked".
- **The complaint fix (row 6):**
  - **Titles:** under 15 words with no repeats, enforced by a check, so not just promised.
  - **No ranking promise:** the gig FAQ already says "No one can honestly guarantee sales".
  - **No login needed:** we work from the shop link.
  - **Gradual rollout:** "test a few first" fits our free 2-listing proof.

## Gate rule this benchmark implies
**Pitch rule:** never promise rankings or sales, and never claim we're cheaper than software. Say "done for you, Etsy's current title guidance, checked".

**Step 4 must wait.** The owner read (dashboard "Etsy listing sample" tap) should use the **fixed** titles on davias PR #7, not the old ones.
