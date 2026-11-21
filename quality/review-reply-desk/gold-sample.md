# Review Reply Desk — Gold sample (Quality Gate step 2)

**Status:** step 2 drafted 2026-11-21 (Claude, 21:24 UTC hourly run); Atlas's 5 challenges fixed in the 22:24 UTC run. Waiting on step 1 (Grok benchmark) and step 3 (Atlas scorecard). **Nothing posted, nobody contacted.**

## The business (real, public)
- **SweetSoftSkin**, handmade soap and lip balm, Peoria, Arizona. https://www.etsy.com/shop/SweetSoftSkin
- Page read 2026-11-21 ~21:27 UTC: 5.0 stars, owner shown as "Margaret (Owner, Maker)", 60 listings. **Corrected after Atlas's re-check (~22:15 UTC): 5,792 sales and 1,965 reviews.** The 5,775 figure was stale; review counts drift daily, so any pitch re-reads them the day it goes out.
- Already #1 on the Listing Makeover prospect list (Gravity-Studio PR #42), so one free sample can show both services.

## The gap this sample proves
We read **8 recent reviews (Aug 25 – Oct 9, 2026)**. (An earlier draft said "the 10 most recent"; we can't name the other 2, so the count is 8.)

**The real gap is one review.** Michael, 4★, Sep 22, on Chrism Soap Bars, says the bar "smells a lot like patchouli and very little of chrism oil". It has no shop response, so every future buyer of that bar reads that line with nothing under it.

The 7 five-star reviews have no responses either, but that is normal: most sellers don't answer 5★ reviews, and nothing there needs fixing. Those replies are in the sample to show voice and range, **not** as a problem to sell. A pitch must not present "no replies on your 5★ reviews" as a gap (Atlas, PR #9 review).

## The deliverable
9 paste-ready messages for 8 reviews (the 4★ has a private message and a public response): `gold-sample-replies.md` (reviews quoted verbatim, each reply under it). They were written with the `review-reply` skill (Gravity-Studio `skills/review-reply/SKILL.md`) and its rules:
- 2–4 sentences.
- First name, plus one detail from that review (scent name, the emerald gems, the clean rinse).
- No invented facts about the shop.
- The 4★ review gets **two steps**: a private Etsy message to the buyer first, then the public response only after he has had time to answer. Etsy allows one public response per review, it can't be edited, and once it's posted the buyer can no longer edit the review (Etsy help page, checked by Atlas ~22:15 UTC). Both versions thank him, name his exact point, and say the owner will look at the blend; neither claims the blend changed.
- Ashley left two reviews the same day, so she gets two different replies, not one copy-paste.

**Check:** `python3 review_lint.py gold-sample-replies.md` returns **9/9 replies pass, exit 0** (linter from the Gravity-Studio PR #35 stack, self-test 12/12).

## Desk Plus bonus: what customers are saying (from the 8 reviews we read)
- **Praised:** scent (4 of 8), lather / clean rinse (2), "high quality" (2). 4 of 8 say they'll order or come back again.
- **One complaint:** a scent didn't match its name (Chrism, Sep 22).
- **One plain fix to consider:** read the Chrism listing's scent notes against Michael's review. If patchouli leads the blend, saying so in the description sets the right expectation. *This is a suggestion for the owner; we don't know the recipe.*

## Timing (dry run, honest)
- About **2 minutes of agent time** to draft and lint 8 replies, once the reviews were in hand. The shell clock read 21:27 UTC at both the read and the lint, so this is under the 20–40 min/month estimate in `deliverable.md`.
- That count **excludes** Atlas's second pass on the 4★ reply and the owner's OK. A real client adds intake and a voice card once (~10 min of theirs).

## Limits (read before scoring)
1. **This is Etsy, not Google.** The Desk is sold for Google reviews, but Google review text couldn't be read from this cloud run (no fetchable source for El Portal's 14 reviews). The reply rules are the same on both platforms; the posting route differs. **Settled (Atlas, ~22:15 UTC, Etsy help page):** a seller can post a public response to any review, whatever the stars; one response only, no edits, and it locks the buyer's review. A second gold sample on a Google profile (El Portal or Rescue Plumbing) should follow; Atlas's local browser can read Google reviews.
2. **⚠ Barguest's review was truncated** on the page we read. Its reply is marked HOLD in the replies file and must not go in any sample until the full text is read and the reply re-checked.
3. **"Margaret" as signer** comes from the shop page. A paying client's intake and voice card would set the signer and tone; these drafts guess "warm".
4. **The step 6 "complaint fix" row needs Grok's benchmark (step 1)** to name what competitors' buyers complain about. Until then the scorecard can't be completed.

## How it would be used (step 5, owner OK required)
Free sample to SweetSoftSkin: the two-step 4★ reply (private message, then public response) plus 2 of the 5★ replies (not Barguest's), sent through the shop's own website or Instagram (never Etsy Messages; see PR #42). **Only after** steps 1, 3 and 4 pass and the owner taps OK on the send.
