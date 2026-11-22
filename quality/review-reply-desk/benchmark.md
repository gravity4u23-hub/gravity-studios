# Review Reply Desk — Benchmark (Quality Gate step 1)

**Status:** Claude draft, 2026-11-21 23:24 UTC run. Gate step 1 is Grok's, and Grok is back Nov 22 (dashboard). This draft is up now so Atlas can score rows 5–6. **Grok and Atlas, please check every source below.** One conflict to note: Claude also wrote the gold sample. Atlas should re-open each source himself and not take these numbers on trust.

Pages read 2026-11-21, ~23:30 UTC. "Not shown" means the page didn't say.

## What we sell (Gravity-Studio `portfolio/review-reply-desk/offer.md`, on PR #35 branch `claude/review-reply-desk` until it merges)
- **Desk:** $79/mo. Every new Google review answered, up to 30 a month. Turnaround is 2 business days, with a same-day alert on 1–2★.
- **Desk Plus:** $149/mo. Adds Yelp and Facebook drafts and a monthly "what customers say" page with 3 fixes.
- First week free. No passwords. Every reply goes through `review_lint.py`.

## The competitors
### A. Human / managed services (the real comparison: someone writes the replies)
| Who | Price | What's included | Turnaround | Source |
|---|---|---|---|---|
| **Business Reputation Works** (signup form) | **$149/mo**, 1 location; also "Monthly Review Care" **$79/mo** (contents not shown); $100 one-time tune-up | Up to 30 Google review replies/mo, approved by the owner before posting; monthly GBP check; up to 2 profile updates; review link/QR; monthly summary. Google only. | not shown | https://form.jotform.com/262750900294154 |
| **Smith & Floyd LLC** (Fiverr, Erin Smith) — **UNVERIFIED** (Atlas couldn't load Fiverr; Grok re-checks from a browser) | $695/mo for 3 locations ($232/location); +$195/mo per extra location | Responses to all ratings, monthly report, quarterly strategy. Aimed at multi-location businesses. | Page text read "2448hr" (24–48h is a guess) | https://fiverr.com/erinfloydsmith/manage-gmb-reputation-for-multi-location-businesses |
| **Marqii** (restaurants) | Base $90; **Growth $145/mo per location, annual contract**, adds review monitoring + response on Yelp, Google, Facebook; Scale $180; Package $250 (100 automated responses/location) | Responses across Google, Yelp, Facebook | not shown | https://marqii.com/pricing (Claude's first fetch also reported per-brand "managed" tiers of $100/50 reviews; Atlas's re-read at 00:17 UTC found no such tiers, so they are dropped) |

### B. Software (cheap, but the owner does the work or replies are auto-posted)
| Who | Price | Notes | Source |
|---|---|---|---|
| **RightResponse AI** | $19 Core / $29 Pro / $44 Pro+ per location per month | Software, not a person. ("100 responses, auto-publish" was in Claude's fetch but Atlas didn't find it on the page, so it's dropped.) | https://g2.com/products/rightresponse-ai/pricing |
| **AI Review Response Generator** | $14.99/mo, unlimited | AI suggestions; the owner posts them. No free trial. 0 reviews on Capterra. | https://www.capterra.com/p/10033946/AI-Review-Response-Generator/ |
| **Birdeye** | Price not on the page read | Enterprise/multi-location platform, 4.7★ from 4,327 G2 reviews; G2 says about 1 month to implement | https://g2.com/products/birdeye/reviews |

**Google's own AI replies (Atlas read it, 00:17 UTC):** Search Engine Land reports Google is **testing** "Reply to reviews with AI" inside Google Business Profile. It is a limited test with patchy availability (seen in the US, Brazil and India). The article gives **no price and never says free**. It is a *potential future* substitute. If it rolls out widely, the pitch leans harder on what a built-in drafter can't do: accurate, specific, checked, and the angry ones flagged to the owner the same day. https://searchengineland.com/google-business-profile-test-reply-to-reviews-with-ai-472167

## What buyers complain about (evidence, not opinions)
1. **Canned replies.** Birdeye user Terry Lind S. (Business Manager, G2, Jul 31, 2026, 5★, tagged "Incentivized"), under "What do you dislike": *"The canned feedback responses and having to disable so many automations at the beginning."* https://www.g2.com/survey_responses/birdeye-review-13192521
2. **AI replies that leak details or promise things that aren't happening.** Univ. of Arkansas Walton College (Daniel Villanova, Sep 8, 2026), summarizing research in *Journal of Public Policy & Marketing* (2026). In tests, ChatGPT-3.5 replies *sometimes repeated sensitive medical details and sometimes implied actions that were not underway* (paraphrase). Consumers liked a reply less once told AI wrote it. Quote: *"Non-disclosure might be a non-starter."* https://walton.uark.edu/insights/posts/should_businesses_use_ai_to_respond_to_online_reviews.php
3. **"Feels AI-written" reads as fake.** RetailWire (Tom Ryan, Mar 21, 2025) cites BrightLocal's 2025 survey: 46% judge a review fake if it "feels like it was written by AI". *That figure is about reviews, not owner replies. Use it only as a signal that AI tone costs trust.* The same piece cites BrightLocal blind tests where 58% preferred ChatGPT replies to human ones. So AI drafting is fine; generic AI tone is the problem. https://retailwire.com/discussion/should-ai-respond-customer-reviews/

**Not found:** no buyer complaint text on the Fiverr or managed-service pages (none show review sections in the fetched text). Two Upwork review-response listings wouldn't load. Grok can add Fiverr buyer reviews from a browser.

## How we compare (input for Atlas's rows 5–6; Atlas scores)
- **Price vs human services (verified rows only):** Desk $79 **beats** Business Reputation Works' $149 plan at about half the price, for the same up-to-30 Google replies. Desk Plus $149 **matches** BRW $149 with more included (Yelp and Facebook drafts, monthly fixes page). It also matches Marqii Growth at $145/location, and we are month-to-month where Marqii needs an annual contract. BRW's $79 tier can't be compared because its contents aren't shown. Smith & Floyd ($232/location) would be the priciest, but it's unverified.
- **Price vs software:** **loses.** $15–19/mo tools are 4–5× cheaper. We should not compete on price there. We compete on the complaints above: software is where the canned replies come from.
- **Speed:** software is instant; we promise 2 business days, plus a same-day alert on 1–2★. Smith & Floyd says 24–48h (unclear). **We do not beat the best on speed.** The dry run took about 2 minutes of agent time (gold sample), so a 1-business-day promise for 1–2★ reviews looks possible. That is a pricing/promise change, so it is the owner's decision, not made here.
- **The complaint fix (row 6):** the #1 complaint is canned, generic replies, and the next is replies that leak private details or claim fixes that aren't real. `review_lint.py` blocks the second one mechanically: patient details for clinics, unconfirmed "we changed X" claims, review-asks and compensation. The gold sample shows the first: each of the 8 replies names the reviewer and one detail from their review, and the same reviewer's two reviews got two different replies. **Not yet enforced by a check:** "no two replies share a sentence". Suggested standing check for Atlas to weigh.

## Gate rule this benchmark implies
The gate says *beat or match the best on quality AND beat on price or speed*. Against **human** services we match/beat on price, so the Desk can pass. Against **software** we lose on both, so the pitch must never claim to be cheaper or faster than software. It must say "written for you, specific, checked", and the free first week proves it.
