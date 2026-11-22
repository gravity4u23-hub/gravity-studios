# Wellness Blog Engine — Free trial pack (Quality Gate step 5, prepared)

**Status (2026-11-22, 23:25 UTC hourly run):** prepared, **not sent**. Step 5 opens only after step 4 (the owner's read: *"Would I pay $150 a month for four of these?"*) is "Yes". Each send needs its own owner OK on the exact text below. **Nobody has been contacted, and no form was filled in.**

Check: `python3 trial_check.py` (this folder). It fails any message that names a price, promises traffic or rankings, uses a health-claim word (cure, heal, treat, prevent, detox...), quotes the post inexactly, names a title that isn't one of the post's headline options, hides that the post was drafted with AI help, comments on how often the shop blogs, leaves a `[` placeholder, skips the business line, or runs past 220 words (a contact-form comment box). Self-tests: `python3 trial_check.py --self-test`.

## What step 5 needs (from QUALITY_GATE.md)
1–3 free samples to real businesses, owner OK on each send. **Pass = at least 1 of 3 used it or asked for more.** The log at the bottom records only what actually happened.

## Trial 1 — Winter Sun Trading Co. (Flagstaff herb shop and apothecary)
**Route:** Contact form on the shop's own website (fields: Name, Email, Phone number, Comment), sent by the owner. The text below goes in the Comment box.
**Route source:** https://www.wintersun.com/pages/contact-winter-sun-trading-co (opened 2026-11-22 ~23:30 UTC: "Drop us a line using the form and we'll get back to you as soon as possible." Same page also lists the phone, 928-774-2884; the footer links Facebook and Instagram. No email address and no policy on vendor or sales messages appear on the contact, home or About Us pages.)
**Why them:** the gold sample (`gold-sample-002-winter-sun.md`) was written for this shop on an herb it already stocks. Atlas scored it 4.5 (step 3 PASS) after re-opening all 3 sources. The About Us page names the founder: *"The Winter Sun Trading Company was established in 1976 in Arizona by Phyllis Hogan."*
**How the post gets to them:** a contact form can't carry a file, and 1,000+ words won't fit a comment box. So the message shows the title and one line and offers the full post as a Word file by email. If they ask, that counts as "asked for more" in the log.

**Day-of checks before the owner taps:**
1. Open `wintersun.com/blogs/articles`. **Atlas checked it 2026-11-22 ~23:33 UTC:** 6 articles, newest Aug 10, 2020, no ashwagandha post. Re-check on send day. If they've posted on ashwagandha since, pick another herb they stock and write a new sample first. Don't send this one.
2. Confirm the shop still sells ashwagandha root (a call to 928-774-2884 settles it). Atlas couldn't find the product page by search on Nov 22. So the message no longer says "an herb you carry". If they don't sell it, ask the owner whether to send anyway or pick an herb they do sell.
3. **Owner's choice:** the Email field. Use the address you want Gravity Studios replies to go to. It's not written here because this repo is public.
4. Owner OKs this exact text. Re-run `python3 trial_check.py` after any edit.

```message
Hello Phyllis and the Winter Sun team,

I'm David from Gravity Studios in Arizona. We write blog posts for herb shops and wellness businesses. As a free sample, I wrote one for your Apothecary Journal on ashwagandha. It's yours to use, change or ignore.

Title: Ashwagandha, Honestly: The "Smell of the Horse" Root, From Ayurveda to Today's Trials

It keeps the tradition and the research apart, labels which is which, and has a "Who should skip it" section (pregnancy, liver, thyroid, autoimmune conditions, medicines). One line from it:
> A spoonful of root powder in warm milk is the traditional food form, not the studied dose.

To be upfront: it was drafted with AI help. Then every quote was checked word for word against its source (NIH, Memorial Sloan Kettering and a 2011 Ayurveda review). It doesn't promise anyone a result.

If you'd like the full post as a Word file, write back and I'll email it to you. No reply needed otherwise.

David — Gravity Studios
(747) 222-6980
```

## Next: trials 2–3 (not chosen yet)
From `prospect-blog-check.md`, the businesses with no blog or a quiet one are Flagstaff Clinic of Naturopathic Medicine (#2), Acupuncture Wellness Center (#7), True North Integrative Osteopathic Institute (#8) and Munderloh Integrated Medical (#4). They're clinics, not herb shops, so each needs **its own** sample, on a topic from its own services page, run through `post_lint.py --presale`, `check_posts.py` and a `gold_eval.py` quote table before a trial is written. Clinic posts must never suggest the reader is or was a patient, and must not stand in for a visit. Not started: one trial at a time, after step 4.

## Results log (fill only with what actually happened)
| Trial | Sent (date, by owner) | Route | What they did (used / thanks / ignored / complained) | Notes |
|---|---|---|---|---|
| 1 Winter Sun | — | — | — | not sent; waits on step 4 |
| 2 | — | — | — | not chosen |
| 3 | — | — | — | not chosen |
