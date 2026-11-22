# Wellness Blog Engine — Benchmark (Quality Gate step 1)

**Status:** Claude's draft from the 2026-11-22 02:25 UTC run. Step 1 is Grok's job; Grok is back Nov 22 and owns the open rows marked **GROK**. Claude also wrote the gold sample (`Gravity-Studio/portfolio/wellness-blog-engine/sample-post-001-draft.md`), so **Atlas should re-open every source and not take these numbers on trust.**

Pages read 2026-11-22, ~02:30 UTC.
- **[S]** = taken from a summary of a page whose text was cut off, not verbatim. Re-check these first.
- "Not shown" = the page didn't say.

## What we sell
- **Direct** (Gravity-Studio `portfolio/wellness-blog-engine/offer.md` + `deliverable.md`, on main):
  - **Starter:** $150/mo, 4 posts of 800–1,200 words (**$37.50 a post**)
  - **Growth:** $250/mo, + 10-keyword plan + internal-link map
  - **Authority:** $300/mo, + one 2,000+ word guide a quarter
  - Every post: 3 headline options, meta title + description, a licensed stock-image suggestion, 1 revision round, a Sources section (3–6 links, each opened), PROVEN / TRADITIONAL / FRINGE labels, a "see a qualified clinician" line. Topics approved by the 5th; 1 post a week. First month paid only after the buyer approves post 1.
- **Fiverr gig 3** (Gravity-Studio `portfolio/fiverr/gig-3-wellness-blog.md`, branch `claude/fiverr-gigs`, PR #37):
  - Basic $25 (800 words + meta, 3 days) · Standard $59 (1,500 words + meta + 3 headlines, 4 days) · Premium $199 (4 posts/month + topic calendar, 30 days)

## The competitors
### A. Done-for-you blog subscriptions (the real comparison)
| Who | Price | Posts / words | Included | Delivery | Rating | Source |
|---|---|---|---|---|---|---|
| **BKA Content**, Standard Lvl 2 (US agency since 2009) | **$390/mo** (3- and 6-month plans save 5% / 10%) | 4 posts: 2 × 1,000 + 2 × 500 words | Keyword research, topics, proofreading, meta title + description free at Lvl 2+. Stock image is a paid add-on, and **the page itself conflicts**: "For an additional $6 per blog post" in the body, "Social Package (Stock Photo/Social Media Post) - $13/post" in the options list. Revisions not shown. FAQ "How does billing work?": "Your subscription is set to auto renew once the billing cycle has ended." | FAQ: "You will recieve your content within a few weeks of starting your subscription." (sic) | G2: 0 reviews | https://bkacontent.com/product/standard-blog-package-lvl2/ , https://www.bkacontent.com/success/ , https://www.g2.com/sellers/bka-content |
| **BKA Content**, health & wellness page | "$195 to $1,270" a month for blog packages | — | "consult respected sources… Our editing team demands accuracy"; "Zero Tolerance for Plagiarism policy… That also means no AI." **No clinician review and no citation policy stated.** | Not shown | — | https://www.bkacontent.com/?p=94040 |
| **Innocensia Kambewe**, Contra (South Africa) | **$600/mo** | 4–6 posts, 800–1,000 words | SEO keywords + "meta tags", topic research, headlines, "with references", **2 revision rounds** | Not shown | No ratings shown | https://contra.com/s/6rlqqNbA-health-and-wellness-monthly-blog-content-package |
| **Lifting Oseiwel**, Contra (Nigeria) | from **$1,200** (period not stated; 3-month discount) | 4 articles, 1,200–2,500 words | Topic calendar, SEO keywords, 1 revision round | "4 weeks" | No ratings shown | https://contra.com/s/g2cmbBbX-wellness-content-package-four-articles-per-month-ongoing |
| **Therapist Site Toolbox** (therapists only) | **Not shown** (quarterly or annual, paid monthly) | 2, 3 or 4 posts/month | Long-tail + secondary keywords, links, 1 royalty-free stock image, Google Docs; upload add-on | First delivery on the 1st of the month after purchase, then "the first Monday of the month" (per Atlas) | Not shown | https://www.therapistsitetoolbox.com/blog/outsource-your-blogging |

### B. Single-post freelancers (cheapest human option)
**VERIFIED live by Atlas** (browser, read-only, 2026-11-22 ~05:31–05:38 UTC; his PR #15 follow-up). Challenge #4 closed.

| Who | Price | Words | Delivery | Rating / orders | Source |
|---|---|---|---|---|---|
| **wafa_94**, Fiverr — "evidence based nutrition and health blog articles" | **$30** Basic | 1,000 | 3 days | 5.0 from 22; 241 orders | https://fiverr.com/wafa_94/write-thorough-seo-articles-on-medical-nutrition-therapy |
| **brightleaf_w**, Fiverr — "research backed wellness or nutrition content" | $35 Basic | 500 | 1 day | 5.0 from 1; 4 orders | https://fiverr.com/brightleaf_w/write-seo-optimized-health-and-wellness-blog-posts-that-attract-readers |
| **traviseric17**, Fiverr Pro — chiropractic articles | $40 Basic | 500 | 4 days | 5.0 from 1; 41 orders | https://fiverr.com/traviseric17/craft-seo-chiropractic-articles-and-blogs (**on hold**: "Looks Like This Service Is On Hold") |

### C. Software (the substitute)
| Who | Price | What | Rating | Source |
|---|---|---|---|---|
| **Blawgy** | $99/mo Pro (31 AI articles a month, published daily to your CMS, AI images, internal links); $149/mo Pro+ | 3-day free trial, no contract, 30-day refund; a "judge model" checks each article | GetApp 0 reviews; G2 5.0 from 1 (Buddy R., Founder, 10/28/2026: "Founder is very helpful. The software just works!" — per Atlas) | https://www.getapp.com/all-software/a/blawgy/ , https://www.g2.com/products/blawgy/reviews |

Market range for context (an AI-writer vendor's guide, so biased toward AI): professional blog writing "$250 – $800 per post"; value tier "$0.04 – $0.15 per word". https://www.eesel.ai/blog/blog-writing-service-pricing (published 2026-02-01)

## Side by side — where we stand
| Against | Price | Speed | Verdict |
|---|---|---|---|
| Managed subscriptions (BKA $390, Contra $600) | **$150 for 4 posts — 38% of BKA, 25% of Contra** | Ours 1 a week (all 4 by the 25th); BKA "a few weeks" to start; Contra not shown | **Beat on price** with more included than BKA Lvl 2 (image suggestion, sources section, revision round stated). Contra gives 2 revision rounds vs our 1. |
| Fiverr single-post writers (wafa_94 $30/1,000 words, 3 days — verified by Atlas) | 4 × $30 = **$120 vs our $150** | Same 3 days on our Fiverr Basic | **We do not beat the best freelancer on price.** Our $150 adds the topic calendar, 3 headlines, meta, the image suggestion and checked sources; that is a "match on price, more included", not a beat. |
| Software (Blawgy $99/mo, 31 posts) | Software is cheaper per post | Software is daily | **Never pitch cheaper or faster than software.** Pitch: written for your practice, every claim sourced and labelled, you approve topics. |

**Pitch rule (same as the Review Desk):** never say "cheapest" or "fastest". Say "a quarter to a third of what agencies charge, every source checked."

## What buyers complain about (row 6) — PARTIAL, GROK
No buyer complaint text was found on the pages read: BKA has 0 G2 reviews; every Fiverr gig read is 5.0; Contra shows no ratings. What we have is weaker than real buyer reviews:
- **Generic content:** basic-tier content is "usually generic, lacks any real strategy, and probably won't rank" — eesel.ai (an AI-writer vendor, so self-interested).
- **Jargon and borrowed authority:** a physical-therapist health writer: "Super technical and jargony content is a huge pitfall in wellness marketing" and "Phrases like 'According to so-and-so' or 'Studies say' are worshipped in the health industry." — https://writeraccess.com/blog/2020-07-health-marketing-secrets-from-professional-health-writer (2020)
- **Unsupported health claims are the buyer's legal risk:** the FTC publishes "Health Products Compliance Guidance" for health claims — https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance — Atlas quoted it verbatim on PR #15: health claims need "competent and reliable scientific evidence"; "Anecdotal evidence… [is] never sufficient"; the guidance "doesn't have the force or effect of law.". BKA's wellness page states no citation policy.
- **Our fix, if the complaint is confirmed:** every "studies say" line links the real study or is cut; PROVEN / TRADITIONAL / FRINGE label on each claim; buyer approves topics first.

**GROK (Nov 22):** find 3+ real buyer complaints about outsourced health/wellness blog writing (Reddit r/smallbusiness, r/chiropractic, r/Etsy wellness sellers; Trustpilot for WriterAccess, Textbroker, Content Cucumber) and add them here with links. Row 6 can't score above 3 without them.

## Gold sample (step 2) — what's still open before Atlas scores
- `sample-post-001-draft.md` (Black Seed tea), Nov 22 (Gravity-Studio PR #49): the traditional section now names *Sahih al-Bukhari* 5687 and Avicenna's *Canon* (both opened), and the seller-blog source is gone. A new standing check, `post_lint.py`, passes 15/15 self-tests and the sample passes the rules. `--presale` still fails, as it should: the two meta-analysis abstracts (PMID 40714301, 41858302) can't be opened from the cloud (PubMed blocks it), so **Atlas or the owner re-reads them in a browser.** The post is on a topic of our choosing, not a real business.
- **Done Nov 22:** `gold-sample-002-winter-sun.md`, an ashwagandha post written for Winter Sun Trading Co. (a Flagstaff apothecary that sells the dried root and has no journal post newer than Aug 2020 among those we could see). It has 3 sources, all opened, and `post_lint.py --presale` is OK at 1,052 words. Nobody was contacted. The 10-prospect blog check is in `prospect-blog-check.md`. **Sample 002 is ready for Atlas's scorecard (step 3)** even while sample 001 waits on PubMed.

## Verdict (draft, for Atlas)
- **Step 1:** Atlas PASS conditional (PR #15 review, 2026-11-22): fixes 1–3 and 5 made; fix 4 closed (Atlas verified the Fiverr rows live). Row 6 complaints partial (GROK). Step 3 not scored yet — premature until the sample is final and row 6 is filled.
- **Price:** beats managed subscriptions clearly; matches, doesn't beat, the best single freelancer; loses to software.
- **Owner decision this raises:** none yet. If Atlas rules the freelancer comparison is the one that counts, the choice is $150 with more included vs dropping Starter to $120. *Claude's recommendation: keep $150 — the buyer gets a calendar and sourced, labelled posts, and $150 is still 38% of the cheapest agency.*
