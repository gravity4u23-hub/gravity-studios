# GEO / AI Search Check — Gold sample (Quality Gate step 2), part A of 2

**Business:** Davias Earthbound Jewelry (our own shop), https://daviasearthboundjewelry.love
**Status:** Part A (site side) done by Claude, 2026-11-23 02:25 UTC run. **Part B (the 9 engine checks) is not run yet:** it needs a browser (Perplexity, Google, and a signed-in ChatGPT), which this cloud session can't use. Nothing below is a score.
**Why Davias:** the benchmark's step-2 plan says "run the full 9-check audit on our own business first". The Davias *website work* is paused (owner, Nov 21 4:20 PM); this audit reads the site and changes nothing. It is a labelled self-audit (COMMAND_CENTER: "a labelled self-audit demo, not a case study"), never shown to buyers as a customer result.

## 1. The 3 questions, fixed before the first check (committed 2026-11-23 02:28 UTC, `563e634`)
Davias sells online with no shop address, so the questions are what an online buyer would type, not "near me". They may not change after the first check (runbook rule). No engine check has been run yet, so they were fixed before any check. (An earlier version of this line said 02:40 UTC; the commit time, 02:28:25Z, is the right one. Atlas caught it.)

1. `where to buy handmade natural crystal bracelets online`
2. `crystal bracelet shop that is honest about healing claims`
3. `Davias Earthbound Jewelry`

Q2 is the shop's own promise ("Real stones, real science" on the home page). Q3 is the name check: does an engine know the shop, and does it give the right contact details?

## 2. Part A — the site side (done, from the site's source)
**Source, said straight:** this cloud session can't open daviasearthboundjewelry.love (the network refuses the domain). These checks ran on the site's source in `gravity4u23-hub/davias-earthbound-jewelry`, `main` at `b150217`, folder `website/site/` (last changed `beede32`, Nov 17). **Atlas confirms the live robots.txt and one live page match before this goes in a report.**

### Crawler access — `robots_ai_check.py`, result in `gold-sample/robots-result.txt`
robots.txt is `User-agent: * / Allow: /` plus the sitemap line. **All 7 crawlers ALLOWED**, including ChatGPT search, Perplexity and Googlebot. *Allowed is not a promise of being named.*
Work-log line: `Robots: No search-crawler block found in robots.txt. (Allowed is not a promise of being named.)`

### Pages, schema, contact details — new `site_ai_check.py`, result in `gold-sample/site-check-davias.txt`
| Check | Result |
|---|---|
| Text readable without JavaScript | **OK.** All 20 pages have 135–498 words in the plain HTML, so a crawler that doesn't run scripts still sees the words. |
| Sitemap | **OK.** All 20 pages are listed, and every listed page exists. |
| Structured data | **13 findings.** Every page carries the same `Organization` block. The 13 product pages (`p/*.html`) have no `Product` block (name, image, stones). The pages also show no price ("order by message"), so a Product block would carry name, image and description only until checkout opens. |
| Contact details | **1 finding, on all 20 pages.** Every page shows `747-528-7039`, once in the footer text and once in the `Organization` data the engines read. Your Nov 21 steering says the business line is **(747) 222-6980** for every public post, the personal number stays for Zelle/bank only, and the personal phone is "unreliable right now". **Owner decision:** which number should Davias show? Until then this stays a question, not a fix. |

### What part A would put in the report (draft fix lines, not final until part B runs)
1. **If Davias should use the business line:** "Your site gives 747-528-7039 on all 20 pages, including the contact data search engines read. What could happen: an AI answer that quotes your site may give customers that number. Fix: change it to the line you answer, in the footer and the Organization data. Effort: needs your web person (one find-and-replace)."
   - *404 page: it also shows 747-528-7039 twice. The checker skips 404 pages on purpose; the buyer report should still say "all 20 pages plus the not-found page".*
2. **Product data:** "Your 13 product pages have no Product data. What could happen: engines may read them as general pages, not products. Fix: add a Product block (name, image, description) to each. Effort: needs your web person."
Part B decides whether these make the top 3. A fix only reaches the top 3 if an engine's answer shows the problem (rubric row 2).

## 3. Part B — the 9 engine checks (to run, Atlas's or the owner's browser)
Follow the runbook top to bottom. **Where the files are:** they are in the *other* repo, `gravity4u23-hub/Gravity-Studio`, on branch `claude/geo-runbook-gaps` (Gravity-Studio PR #54, open, head `844bb85`), not in this repo and not on any `main` yet, which is why a code search finds nothing: `revenue-command-center/geo-audit-runbook.md`, `geo_worklog_check.py`, `geo_score.py`, `geo-report-template.md`. `check_reports.py` is in this repo (`quality/geo-ai-search-check/evals/`). Screenshots G1–G9 in this order; every Unknown still gets a file with its reason:

| ID | Engine | Query |
|---|---|---|
| G1 | Perplexity | where to buy handmade natural crystal bracelets online |
| G2 | Google AI Overview | where to buy handmade natural crystal bracelets online |
| G3 | ChatGPT | where to buy handmade natural crystal bracelets online |
| G4 | Perplexity | crystal bracelet shop that is honest about healing claims |
| G5 | Google AI Overview | crystal bracelet shop that is honest about healing claims |
| G6 | ChatGPT | crystal bracelet shop that is honest about healing claims |
| G7 | Perplexity | Davias Earthbound Jewelry |
| G8 | Google AI Overview | Davias Earthbound Jewelry |
| G9 | ChatGPT | Davias Earthbound Jewelry |

Also, in the signed-in ChatGPT session: `ChatGPT profile: Claimed / Not claimed / Unknown - <reason>`.
Then (from a checkout of that Gravity-Studio branch): `python3 revenue-command-center/geo_worklog_check.py worklog.md` must print READY → `geo_score.py` → report from `geo-report-template.md` → `check_reports.py REPORT.md` must pass.
**For step 3, same day:** run the same shop through the two free tools the benchmark names (Insites, HubSpot AI Search Grader) and save what they show, so Atlas compares like for like. HubSpot's form asks for company details; the owner decides whether to submit it.

**Expected honestly:** a new online shop with no reviews or press will most likely be "Not mentioned" on Q1 and Q2. That is a real result, not a failed sample. The gold sample is judged on whether the report is true, specific and useful (rubric rows 1–6), not on Davias scoring well.

## 4. What part A adds to the service (for Atlas)
`site_ai_check.py` is a new standing check for every audit. It runs on a saved copy of the buyer's pages and costs $0. Self-tests 11/11 (`--test`): a page whose text only arrives by JavaScript, a product page with no Product data, JSON-LD that won't parse, an old number hidden only in the JSON-LD, an old number in a `tel:` link, pages missing from the sitemap, and sitemap entries with no page are all caught. One number written three ways is not a finding, and the 404 page is skipped. **Known limit:** any 10-digit run (an order number) reads as a phone, so a human clears that kind of finding. The test pins that behaviour so it can't change silently.
Proposed runbook line (Gravity-Studio, after the crawler step; not applied in this PR): *"Site check (2 min): save the home page + 2 service/product pages, run `site_ai_check.py <folder> --phone <the number the buyer answers>`, paste the SUMMARY line into the work log."*
