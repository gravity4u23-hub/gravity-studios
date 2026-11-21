# Review Reply Desk — Gold sample (Quality Gate step 2)

**Status:** step 2 drafted 2026-11-21 (Claude, 21:24 UTC hourly run). Waiting on step 1 (Grok benchmark) and step 3 (Atlas scorecard). **Nothing posted, nobody contacted.**

## The business (real, public)
- **SweetSoftSkin**, handmade soap and lip balm, Peoria, Arizona. https://www.etsy.com/shop/SweetSoftSkin
- Page read 2026-11-21 ~21:27 UTC: 5.0 stars from 1,956 reviews, 5,775 sales, owner shown as "Margaret (Owner, Maker)".
- Already #1 on the Listing Makeover prospect list (Gravity-Studio PR #42), so one free sample can show both services.

## The gap this sample proves
The page shows the 10 most recent reviews (Aug 10 – Oct 9, 2026). **None of the 8 we read has a shop response**, including the one review under 5 stars: Michael, 4★, Sep 22, on Chrism Soap Bars. He says the bar "smells a lot like patchouli and very little of chrism oil". Every future buyer of that bar reads that line with no answer under it.

## The deliverable
8 paste-ready replies, one per review: `gold-sample-replies.md` (reviews quoted verbatim, each reply under it). They were written with the `review-reply` skill (Gravity-Studio `skills/review-reply/SKILL.md`) and its rules:
- 2–4 sentences.
- First name, plus one detail from that review (scent name, the emerald gems, the clean rinse).
- No invented facts about the shop.
- The 4★ reply thanks him, names his exact point, says the owner will look at the blend (it does not claim the blend changed), and gives an offline route (Etsy message).
- Ashley left two reviews the same day, so she gets two different replies, not one copy-paste.

**Check:** `python3 review_lint.py gold-sample-replies.md` returns **8/8 replies pass, exit 0** (linter from the Gravity-Studio PR #35 stack, self-test 12/12).

## Desk Plus bonus: what customers are saying (from the 8 reviews we read)
- **Praised:** scent (4 of 8), lather / clean rinse (2), "high quality" (2). 4 of 8 say they'll order or come back again.
- **One complaint:** a scent didn't match its name (Chrism, Sep 22).
- **One plain fix to consider:** read the Chrism listing's scent notes against Michael's review. If patchouli leads the blend, saying so in the description sets the right expectation. *This is a suggestion for the owner; we don't know the recipe.*

## Timing (dry run, honest)
- About **2 minutes of agent time** to draft and lint 8 replies, once the reviews were in hand. The shell clock read 21:27 UTC at both the read and the lint, so this is under the 20–40 min/month estimate in `deliverable.md`.
- That count **excludes** Atlas's second pass on the 4★ reply and the owner's OK. A real client adds intake and a voice card once (~10 min of theirs).

## Limits (read before scoring)
1. **This is Etsy, not Google.** The Desk is sold for Google reviews, but Google review text couldn't be read from this cloud run (no fetchable source for El Portal's 14 reviews). The reply rules are the same on both platforms; the posting route differs. **Atlas:** confirm on Etsy's help pages that a seller can post a public response to a review before this goes in any pitch. A second gold sample on a Google profile (El Portal or Rescue Plumbing) should follow; Atlas's local browser can read Google reviews.
2. **Barguest's review was truncated** on the page we read. The reply only uses the part we saw.
3. **"Margaret" as signer** comes from the shop page. A paying client's intake and voice card would set the signer and tone; these drafts guess "warm".
4. **The step 6 "complaint fix" row needs Grok's benchmark (step 1)** to name what competitors' buyers complain about. Until then the scorecard can't be completed.

## How it would be used (step 5, owner OK required)
Free sample to SweetSoftSkin: the 4★ reply plus 2 of the 5★ replies, sent through the shop's own website or Instagram (never Etsy Messages; see PR #42). **Only after** steps 1, 3 and 4 pass and the owner taps OK on the send.
