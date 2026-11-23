# Review Reply Desk — Free trial pack (Quality Gate step 5, prepared)

**Status (2026-11-22, 06:25 UTC hourly run):** prepared, **not sent**. Step 5 opens only after step 4 (owner read, tap 18) is "Yes". Each send needs its own owner OK on the exact text below. **Nobody has been contacted.**

**Update (2026-11-22, 19:25 UTC hourly run):** Trial 1 now has a **route candidate outside Etsy**: the shop's own Facebook Page, `facebook.com/sweetsoftskin`, which the shop itself listed (with its Etsy shop and Pinterest) in a Soap Queen interview. The cloud can't open Facebook (robots.txt refusal), and the interview is from June 1, 2015, so the Page may be inactive. Trial 1 stays **HOLD** until someone opens the Page in a browser and sees it is live. The message is now in Messenger form (no subject line). `trial_check.py` gained two rules: every route must cite where it was found, and a DM route can't carry an email subject line (self-tests 18/18).

Check: `python3 trial_check.py` (this folder): Trial 1 prints **HOLD** until its route is verified. It fails any message that names a price, compares us to software, sells "no replies" as the gap, edits a verified reply, skips the business line, or goes through Etsy Messages. Self-tests: `python3 trial_check.py --self-test`.

## What step 5 needs (from QUALITY_GATE.md)
1–3 free samples to real businesses, owner OK on each send. **Pass = at least 1 of 3 used it or asked for more.** We record what each one did in the log at the bottom, and nothing else (no invented outcomes).

## Blocker found this run: SweetSoftSkin has no confirmed contact route outside Etsy
- Our rule (Gravity-Studio PR #42): **never Etsy Messages.** Etsy's messaging policy bars unsolicited sales messages, and a report could flag the shop.
- A web search on 2026-11-22 (~06:30 UTC, "SweetSoftSkin Peoria Arizona handmade soap website Instagram") found only the Etsy shop page. No website, email or Instagram showed up. That is a search miss, not proof there is none: the shop's Etsy "About" section may link one, and the cloud can't read it.
- **Until Atlas's browser finds a route on the shop's own pages, Trial 1 can't be sent.** The message is ready, so the send is one tap once a route exists.
- **19:25 UTC run, second search** (`"Sweet Soft Skin" handmade soap Peoria Arizona Margaret`) found two more public pages: the shop's Facebook Page (`facebook.com/sweetsoftskin`) and a Soap Queen interview, *Interview with Margaret of Sweet Soft Skin Handmade Soaps* (Anne-Marie Faiola, June 1, 2015), whose "Find Sweet Soft Skin Handmade Soaps" section links exactly three places: Etsy, that Facebook Page and a Pinterest board. No website, email or Instagram is listed. So the Facebook Page is the shop's own channel, but it is 11 years old as evidence. **Before the owner taps:** open the Page, check it posted or answered something in 2025–2026 and that Messages are on. If not, we skip this shop.

## Trial 1 — SweetSoftSkin (Peoria, AZ, Etsy soap shop)
**Route:** UNVERIFIED: a Facebook Page message to facebook.com/sweetsoftskin, sent by the owner. Confirm in a browser that the Page is active (a post or reply in 2025–2026) and has Messages on; if not, skip this shop.
**Route source:** https://soapqueen.com/business/interview-with-margaret-of-sweet-soft-skin-handmade-soaps/ (June 1, 2015: the shop lists Etsy, this Facebook Page and Pinterest; no website or email)
**Why them:** the gold sample (`gold-sample-replies.md`) was written on their real reviews, and every quote was verified by Atlas. The one real gap is Michael's 4★ review on the Chrism bars, which has no shop response.
**Day-of checks before the owner taps:** (1) re-read the shop: is Michael's Sep 22 review still without a response? If one has been posted, drop item 1 and send only the two 5★ replies; (2) don't quote any sales or review counts; (3) owner OKs this exact text.

```message
Hi Margaret,

I'm David from Gravity Studios in Arizona. We write review replies for small shops, in the owner's voice. I read your recent Etsy reviews and drafted replies to three of them. They're free and yours to use, change or ignore.

1. Michael's 4-star review of the Chrism bars (Sep 22). Etsy gives a shop one public response per review, it can't be edited, and it locks his review, so I'd start with a private message:
> Hi Michael, thank you for the honest review of the Chrism bars, and I'm glad they lather well for you. You're right that I want the chrism oil to come through, so I'm taking a closer look at the blend. If you'd like to tell me more about how it smelled to you, just reply here. — Margaret, SweetSoftSkin

A few days later, the public response:
> Thank you for the honest review, Michael, and we're glad the Chrism bars lather well for you. Thank you too for telling us the patchouli comes through more than the chrism oil; that's useful, and I'll take a closer look at the blend. If you'd like to talk about it, send me a message here on Etsy any time. — Margaret, SweetSoftSkin

2. Dana, Emerald Rainfall (Oct 9):
> Thank you, Dana! We're so glad both the scent and the name of Emerald Rainfall won you over. Enjoy every bar. — Margaret, SweetSoftSkin

3. Kaitlin, Peach Tea (Oct 5):
> Thank you so much, Kaitlin! We love hearing that Peach Tea looks as good as it smells. We'll be happy to see you back whenever you're ready for more. — Margaret, SweetSoftSkin

The replies only use what each review says. I didn't guess anything about your recipes. No reply needed. If they're useful, I'd love to hear it.

David — Gravity Studios
(747) 222-6980
```

## Next: trials 2–3 (not chosen yet)
A trial needs a real business with a **real gap**: a recent review under 5★ with no owner response. The Flagstaff list (Gravity-Studio `pipeline/tracker.csv`, P004–P010) is "count unanswered Google reviews first", and Google review text can't be read from the cloud. **Atlas (local browser):** for P004–P010, record the newest review under 5★ that has no owner response (date, stars, first 10 words). Claude drafts the replies with the `review-reply` skill, lints them, and adds a Trial 2/3 section here. Health clinics: the replies must never confirm that the reviewer was a patient (HIPAA-safe pattern in `skills/review-reply/SKILL.md`).

**Nov 23 13:25 UTC run:** Birdeye's public pages copy these Google reviews and can be read from the cloud, so the list is now triaged in `trial-prospects.md` (checked by `review_gap_check.py`, 0 errors, self-tests 20/20). **P009 The Vitality Doctor** is the best lead: 23 Google reviews, 4.5 average, reviews from the last 1–2 months, no reply text seen. P010 has no gap (5 reviews, all 5★). P005 needs a look. P004, P006, P007 and P008 aren't read yet. Atlas now opens 1–2 Google profiles, not 7.

**Nov 23 14:25 UTC run:** the other 4 were looked up. P008 has no gap (16 reviews, all 5★). The only pages found for P006 and P007 were other businesses (a Tucson "Cedar Health", and Munderloh Chiropractic), so they are marked WRONG-PAGE. `review_gap_check.py` now checks the page's name and city against the prospect, self-tests 22/22. P004 had no Birdeye page. P009 is the only live lead.

## Results log (fill only with what actually happened)
| Trial | Sent (date, by owner) | Route | What they did (used / thanks / ignored / complained) | Notes |
|---|---|---|---|---|
| 1 SweetSoftSkin | — | — | — | not sent |
| 2 | — | — | — | not chosen |
| 3 | — | — | — | not chosen |
