# Owner Brief

Updated by Claude's scheduled run. Newest at the top.

## 2026-11-22 — 22:25 UTC hourly run
**Moved:** **The Wellness Blog sample is now one page Atlas can score (step 3 packet), and every quote in it checks out against its source** (`quality/wellness-blog-engine/gold-sample.md`). Review Desk and Listing Makeover are both waiting on your taps, so this run worked on the next service in line.
- **Quotes checked word for word:** the Winter Sun ashwagandha post quotes NIH, Memorial Sloan Kettering and a 2011 Ayurveda review 15 times. All 3 pages were opened today, and **all 15 quotes are on them word for word.** The trial numbers (7 studies, 491 adults; 5 studies, 372 adults) and Denmark's 2023 ban check out too. A new `gold_eval.py` now fails any quote that isn't on a source page.
- **Our own checker had a hole, now fixed:** we planted 7 errors in the real post and checked whether each one was caught. One slipped through: *"ashwagandha reverses diabetes and is not a quick fix"*. Any "not" or "no" anywhere in the sentence switched the claim check off. *"It cures anxiety, no prescription needed"* passed too. Now a "not" only counts when it's about the claim itself. All 7 plants are caught, and both real posts still pass (Gravity-Studio branch `claude/wellness-negation-scope`).
- **Also fixed:** `MASTER_PLAN.md` (written today) called Davias "primary". It now matches your Nov 21 focus: AI services first, Davias paused. Atlas flagged this.
- There were no new research items or Grok tasks since 21:25. All INBOX items already have a Claude review (PR #2). Atlas's PR #33 points were answered at 21:40.

**Next:** Atlas scores the Wellness sample (step 3) from that one page and reviews the checker fix. Listing Makeover passes step 3 as soon as issue #34 is answered.
**Your taps:**
1. **Tap 18 (read the Review Desk sample) is still the one that moves money first.** *Recommendation: Yes, if the 4★ two-step reply reads like one you'd want for your own shop.*
2. **Issue #34: citrine natural or heat-treated, onyx natural or dyed?** *Recommendation: if you don't know today, OK the two question lines. That passes Listing Makeover step 3 without guessing.*
3. **Issue #27 (hold the Spanish gig) and issue #21 (hold El Portal + Founding 3).** *Recommendation: Hold both.*
4. **Atlas's question in CURRENT_TASK.md:** where should he put the prompts you gave him for Grok? *Recommendation: the private Gravity-Studio repo, not this public one, since they include his operating rules and your personal context.*

## 2026-11-22 — 21:25 UTC hourly run
**Moved:** **Listing Makeover's test set was run on our real listings, and it caught one claim we can't back yet** (gate step 3 prep, `quality/listing-makeover/gold_eval.py`).
- **What ran:** the same checks that guard every Listing Makeover delivery, run on the 12 real Davias listings. The source of truth is the shop's own product file. Every number must be the seller's or a sourced hardness value. Nothing may say sterling, hypoallergenic or "heals", and an unknown size stays a question. **11 of 12 pass.** Planting "8 mm beads, sterling silver clasp" fails all 12, so the check isn't rubber-stamping.
- **The one that fails, Jungle Gold:** every listing says "Every stone is natural." GIA says *most citrine on the market is the result of heat treatment* (it starts as amethyst). The FTC's jewelry guidance says sellers should disclose a treatment that significantly affects value. Atlas asked the same question on davias earlier, and it's still open.
- **Atlas closed the 2 hardness values** (Tiger's Eye, Obsidian) in his browser: 18/18 sourced, 0 open.
- **Repair:** Atlas's fixes to the Listing Makeover benchmark (PR #14) had never reached the stacked branches. They're merged in now, so the gate page and the sample point at the corrected numbers (8 of 12 titles, not 10; the lowest active price is Uri B. at $5.00 a listing, sourced).
- **Update 21:45 UTC — Atlas scored it (step 3): FAIL, blocked on one row.** Scores 3/4/4/5/4/5 (accuracy, specificity, usefulness, speed, price, complaint fix), average 4.17. He also found a second stone with the same problem: **onyx** (Earthfire Twist). Most black onyx sold is dyed chalcedony (International Gem Society; GIA). The check now covers onyx too and reads **10/12**. Once both stones are answered or carry a question line, accuracy goes to 5, the average hits 4.5, and it passes.
- There were no new research items, for-claude issues or Grok tasks since 20:25. All INBOX items already have a Claude review.

**Next:** once the citrine and onyx lines are settled, `gold_eval.py` reads 12/12 and Atlas re-scores accuracy, which passes step 3. Review Desk Trial 1 still waits on the Facebook Page check.
**Your taps:**
1. **Tap 18 (read the Review Desk sample) is still the one that moves money first.** *Recommendation: Yes, if the 4★ two-step reply reads like one you'd want for your own shop.*
2. **New (issue #34): is the Jungle Gold citrine natural or heat-treated, and is the Earthfire Twist onyx natural or dyed?** Ask Octavia or check the supplier's listing. *Recommendation: if you don't know today, OK the two question lines ("[Citrine: natural or heat-treated? confirm with the maker]", same for onyx). That passes Listing Makeover step 3 without guessing, and do this before any of these listings goes on the live shop.*
3. **Issue #27 (hold the Spanish gig) and issue #21 (hold El Portal + Founding 3).** *Recommendation: Hold both.*

## 2026-11-22 — 20:25 UTC hourly run
**Moved:** **Listing Makeover's gold sample is now one page Atlas can score and you can read** (gate step 2 filed, `quality/listing-makeover/gold-sample.md`). It's the second service closest to passing, and Review Desk is waiting on you (tap 18) and a browser check, so this run worked on Listing Makeover.
- **What it is:** the 12 Davias Helix listings (title, description, 13 tags each) in the gate folder, with their checks and sources next to them. Titles pass Etsy's current guidance, 12/12.
- **New check, `mohs_check.py`:** every listing states a stone's hardness as a *Proven* fact, so a wrong number would be a false claim on a live shop. Each value was checked against pages opened today (USGS, the Gem Society chart, GIA, geology.com, minerals.net). **All 18 stones match a source.** Self-tests 8/8.
- **One small change:** Green Aventurine said "Mohs ~6.5" and the sources say 6.5–7, so it now reads 6.5–7 (davias PR #7). It wasn't wrong, just at the low edge.
- **Said straight:** two values need a browser to confirm, Tiger's Eye (~7) and Obsidian (5–5.5). Both fit the sources we could open, but no page states them exactly. They go to Atlas.
- There were no new research items, Atlas comments, for-claude issues or Grok tasks since 19:25. All INBOX items already have a Claude review.

**Next:** Atlas scores the Listing Makeover sample (step 3) and checks the 2 hardness values. Review Desk Trial 1 still waits on the Facebook Page check.
**Your taps:**
1. **Tap 18 (read the Review Desk sample) is still the one that moves money first.** *Recommendation: Yes, if the 4★ two-step reply reads like one you'd want for your own shop.*
2. **New, optional: read Listing Makeover listings 1 and 8** in `quality/listing-makeover/gold-sample-listings.md` and answer "Would I pay $79 for 20 of these?" (step 4). *Recommendation: read after Atlas scores it; Yes if the titles read like ones you'd click.*
3. **Issue #27 (hold the Spanish gig) and issue #21 (hold El Portal + Founding 3).** *Recommendation: Hold both.*

## 2026-11-22 — 19:25 UTC hourly run
**Moved:** **The Review Desk free trial has a way to reach its first shop that isn't Etsy** (gate step 5 prep, `quality/review-reply-desk/free-trial.md`). Review Desk is the service closest to passing, so this run worked on it.
- **What was blocking it:** the trial message to SweetSoftSkin (the Peoria soap shop from our sample) was written and checked, but we had no way to send it. We never pitch through Etsy Messages, and the first search found no website, email or Instagram.
- **What was found:** the shop's own Facebook Page, `facebook.com/sweetsoftskin`. The shop listed it in a Soap Queen interview, *Interview with Margaret of Sweet Soft Skin Handmade Soaps*, next to its Etsy shop and Pinterest. That's the shop's own channel, so the message is now in Messenger form, without the email subject line.
- **Said straight:** that interview is from June 2015, and the cloud can't open Facebook. The Page may be quiet now. So Trial 1 stays on **HOLD** until someone opens the Page and sees a 2025–2026 post or reply and that Messages are on. If it's dead, we skip this shop.
- **Checked by code:** `trial_check.py` has 2 new rules. Every route must cite the page where the business itself published it, and a Facebook or Instagram message can't carry an email subject line. Self-tests 18/18, and the real message still passes its text rules.
- There were no new research items, Atlas comments or Grok tasks since 18:25. All INBOX items already have a Claude review.

**Next:** Atlas (local browser) confirms the SweetSoftSkin Page is active and scores Resume + LinkedIn (step 3). Trial 1 can't go out before your read on tap 18 anyway.
**Your taps:**
1. **Tap 18 (read the Review Desk sample) is still the one that moves money first.** Once it's Yes and the Page checks out, Trial 1 is one more tap: you OK the exact message, then send it from Facebook. *Recommendation: Yes, if the 4★ two-step reply reads like one you'd want for your own shop.*
2. **Issue #27: hold the Spanish gig until you name a fluent Spanish reader?** *Recommendation: Hold.*
3. **Issue #21: hold the El Portal DM and Founding 3 until the GEO audit passes the gate?** *Recommendation: Yes, hold.*

## 2026-11-22 — 18:25 UTC hourly run
**Moved:** **The GEO / AI search check now has its test set** (gate step 3 prep, `quality/geo-ai-search-check/evals/`), so when its sample exists, Atlas can score it the same day.
- **What it is:** 12 of the hardest things a buyer could ask for, or a rushed seller could slip in, each one something we refuse or reshape: "promise I'll show up in ChatGPT", "say it brings more calls", "count the checks you couldn't run as zero", "make the band sound less scary", "drop the not-scored part", "skip the screenshots", "say claiming the ChatGPT profile gets me recommended", "add a '60% of customers use AI' line", "remove the 'what this audit is not' part". Each case comes with the one-line answer we'd give the buyer. The business in it is made up and marked that way.
- **How it's checked:** a new `check_reports.py` reads the finished report (the part the buyer sees). It recomputes the score from the 9 checks, makes sure no check is hidden, that each top fix points at a screenshot we actually took, and that nothing promises rankings, calls or a profile boost. Our version passes every rule; a careless version fails on the exact rule it breaks (12 of 12 caught, 25/25 total, self-tests 11/11). `RUBRIC.md` gives Atlas the 6 things code can't judge, like "are these the right 3 fixes?"
- **Why it matters:** the free AI graders give a score in 60 seconds. What we sell is proof and honesty: the exact answer for your own customer's question, and no promises nobody can keep. This test set holds us to that.
- **Said straight:** GEO is still not close to passing. Its sample on our own business needs a signed-in browser for ChatGPT, so it waits for Atlas's local browser.
- There were no new research items, Atlas comments or Grok tasks since 17:25. All INBOX items already have a Claude review.

**Next:** Atlas scores Resume + LinkedIn (step 3) with its rubric. GEO's sample needs Atlas's signed-in browser. Review Desk still waits on your read (tap 18).
**Your taps:** nothing new.
1. **Tap 18 (read the Review Desk sample) is still the one that moves money first.** *Recommendation: Yes, if the 4★ two-step reply reads like one you'd want for your own shop.*
2. **Issue #27: hold the Spanish gig until you name a fluent Spanish reader?** *Recommendation: Hold.*
3. **Issue #21: hold the El Portal DM and Founding 3 until the GEO audit passes the gate?** *Recommendation: Yes, hold.*

## 2026-11-22 — 17:25 UTC hourly run
**Moved:** **Resume + LinkedIn now has its test set, the last thing Atlas needs before scoring it** (gate step 3 prep, `quality/resume-linkedin/evals/`).
- **What it is:** 9 of the hardest things a resume buyer could ask for, each one something we have to refuse or reshape: "make up some numbers", "stretch my dates to hide a gap", "say I have a degree", "keep my birth date and address on it", "make it sound results-driven", "call me Store Manager", "don't mention AI", "put my cousin as a reference", "list everything in my LinkedIn headline". Every person in it is made up and marked that way.
- **How it's checked:** a new `check_resumes.py`. For each case, our delivery passes every rule, and a careless seller's version fails on the exact rule it breaks (9 of 9 caught). Four rules are new: no added degrees or licenses, no bigger job title than the buyer held, no birth date, street address or marital status, and every delivery note says the work is AI-assisted. Our real gold sample passes the new rules too (19/19 total, self-tests 8/8).
- **Why it matters:** these are the lies that cost a buyer the job at a background or reference check, and refusing them in one helpful line is what makes us different from the sellers buyers complain about.
- **Small cleanup:** two compiled Python files were committed by mistake in an earlier run; removed, and a `.gitignore` stops it happening again.
- There were no new research items, Atlas comments or Grok tasks since 16:25. All INBOX items already have a Claude review.

**Next:** Atlas scores Resume + LinkedIn with the new rubric (step 3). The GEO and Spanish test sets come after.
**Your taps:** nothing new.
1. **Issue #27: hold the Spanish gig until you name a fluent Spanish reader?** *Recommendation: Hold.*
2. **Issue #21: hold the El Portal DM and Founding 3 until the GEO audit passes the gate?** *Recommendation: Yes, hold.*
3. **Tap 18 (read the Review Desk sample) is still the one that moves money first.** *Recommendation: Yes, if the 4★ two-step reply reads like one you'd want for your own shop.*

## 2026-11-22 — 16:25 UTC hourly run
**Moved:** **The Spanish page has its first quality-gate step: a benchmark** (gate step 1 drafted, `quality/spanish-page/benchmark.md`). It was the last service with nothing yet.
- **What others charge:** four Fiverr sellers who are native speakers charge $5–$10 for about 500 words. They have 41 to 1,627 five-star reviews. Ours is $20 with 0 reviews, so **we cost 2–4× more**. We only beat agencies (Gengo, about $25–$60 for the same 500 words). Our $79 kit (menu + service pages + 5 Google posts) is the one thing no one else sells.
- **What buyers complain about:** we read 8 one-star Trustpilot reviews of translation companies. 4 of the 8 say the same thing: **they paid for a person and got machine translation.** The top Fiverr sellers advertise "no Google Translate, no ChatGPT".
- **This hits us harder than any other service, said straight:** our drafting is AI-assisted, and no one on the team is a native Spanish speaker. A script can catch the costly mistakes, and a new `spanish_check.py` does. It catches a changed price or phone number, a dropped line, English left in, a missing allergen, and a delivery note with no AI line, no named reviewer or no list of terms to confirm (self-tests 12/12). It can't tell natural Spanish from stiff Spanish. Only a fluent person can.
- There were no new research items, Atlas comments or Grok tasks since 15:25. All INBOX items already have a Claude review.

**Next:** Atlas verifies this benchmark (the Fiverr numbers came from cut-off pages) and scores the Resume sample and files (step 3).
**Your taps:**
1. **New decision (issue #27): hold the Spanish gig (gig 6) until you name a fluent Spanish speaker you trust to read every delivery?** *Recommendation: Hold. Launch the other 5 gigs as each passes the gate.*
2. **Issue #21: hold the El Portal DM and Founding 3 until the GEO audit passes the gate?** *Recommendation: Yes, hold.*
3. **Tap 18 (read the Review Desk sample) is still the one that moves money first.** *Recommendation: Yes, if the 4★ two-step reply reads like one you'd want for your own shop.*

## 2026-11-22 — 15:25 UTC hourly run
**Moved:** **Resume + LinkedIn now has the actual Word and PDF files a buyer gets, so its gold sample is complete** (gate step 2 done, `quality/resume-linkedin/gold-sample/rewrite.docx` + `.pdf`).
- **What it is:** the checked resume text turned into a clean one-page Word file and a PDF made from it. It is a plain one-column layout with no tables or text boxes, so the hiring software that reads resumes doesn't skip any of it.
- **Checked by code:** a new `file_check.py` passes 6/6. Both files say exactly what the checked text says, word for word. The PDF text can be selected, the page count is 1, and the text pulled out of the PDF passes the no-invented-numbers check. Its self-tests catch a file with "Grew sales 20%" slipped in, a 2-page file and a file with a table (4/4).
- **Why it matters:** the gig promises Word + PDF. A formatting slip can add or drop a word after our text check has passed, and now that would fail.
- There were no new research items, Atlas comments or Grok tasks since 14:25. All INBOX items already have a Claude review.

**Next:** Atlas scores the Resume sample and files (step 3), and the two blog samples with the new rubric. After that they come to you to read (step 4).
**Your taps:** nothing new.
1. **Issue #21: hold the El Portal DM and Founding 3 until the GEO audit passes the gate?** *Recommendation: Yes, hold.*
2. **Tap 18 (read the Review Desk sample) is still the one that moves money first.** *Recommendation: Yes, if the 4★ two-step reply reads like one you'd want for your own shop.*

## 2026-11-22 — 14:25 UTC hourly run
**Moved:** **The Wellness Blog Engine now has its test set, the last thing Atlas needs before scoring it** (gate step 3 prep, Gravity-Studio PR #55).
- **What it is:** 10 of the hardest requests a wellness buyer could make, each one something we have to refuse. They include "say it cures diabetes in the headline", "boosts immunity, detoxes the liver", "add a customer story", "say it's been used for 3,000 years" and "cut the scary safety part". The real Black Seed post passes all 10. A broken copy of the post fails each one, on the exact rule it breaks.
- **Why it matters:** our old post checker missed 7 of the 10. It never read headlines or the Google description, so a cure claim there went straight through. Those are the lines that get a health business in trouble, and now they're checked by code. Both real samples (Black Seed and the Winter Sun ashwagandha post) still pass.
- **A bug fixed along the way:** a quoted claim like *"kills cancer." That is not what the evidence says* could hide an unlabelled claim. Fixed and tested.
- **Research:** the DMSO item had no Claude review. It's now marked *reviewed, not applied* (PR #2): it isn't a service, and we won't write client posts on DMSO.
- There were no new Atlas comments or Grok tasks since 13:25.

**Next:** Atlas scores both blog samples with the new rubric (step 3). After that, they come to you to read (step 4).
**Your taps:** nothing new.
1. **Issue #21: hold the El Portal DM and Founding 3 until the GEO audit passes the gate?** *Recommendation: Yes, hold.*
2. **Tap 18 (read the Review Desk sample) is still the one that moves money first.** *Recommendation: Yes, if the 4★ two-step reply reads like one you'd want for your own shop.*

## 2026-11-22 — 13:25 UTC hourly run
**Moved:** **Resume + LinkedIn has its gold sample** (gate step 2 drafted, `quality/resume-linkedin/gold-sample.md`).
- **What it is:** a full $59 order: a weak "before" resume, the 6 questions we ask the buyer, the rewritten resume, and a LinkedIn headline + About. It is aimed at a real, public job post (Guess, Assistant Store Manager, Arizona).
- **The person is made up, and it says so at the top.** A real person's resume would put their name and employers in the repo.
- **It shows the fix for buyers' #1 complaint (generic, AI-sounding, invented).** Every new detail comes from the buyer's own answers. The job post wants sales and shrink numbers; the buyer had none, so we added none, and the delivery note offers to add them free if the buyer gets them.
- **Checked by code:** a new `gold_check.py` passes 8/8. Both deliverables have zero invented numbers and zero stock phrases. A deliberately bad rewrite ("results-driven… cut turnover 30%") is caught. Adding one fake "20%" makes the check fail.
- There were no new research items, Atlas comments or Grok tasks since 12:25.

**Next:** Atlas verifies the benchmark and scores this sample (step 3). Claude renders the Word + PDF files the gig promises.
**Your taps:** nothing new.
1. **Issue #21: hold the El Portal DM and Founding 3 until the GEO audit passes the gate?** *Recommendation: Yes, hold.*
2. **Tap 18 (read the Review Desk sample) is still the one that moves money first.** *Recommendation: Yes, if the 4★ two-step reply reads like one you'd want for your own shop.*

## 2026-11-22 — 12:25 UTC hourly run
**Moved:** **Resume + LinkedIn has its first quality-gate step: a benchmark** (gate step 1 drafted, `quality/resume-linkedin/benchmark.md`). It was the only service with nothing yet.
- **What others charge:** four Fiverr resume sellers charge $40–$150 and deliver in 1–7 days. TopResume starts around $149–$179 and takes about a week. Ours is $25 / $59 / $89 in 2–3 days. So we win on price, and on speed against most, but one Fiverr seller delivers in 1 day. We also have 0 reviews; they have 35 to 523.
- **What buyers complain about:** we read 24 low-star Trustpilot reviews of ZipJob and TopResume and quoted 8 word for word. The top complaint about the work itself is a generic, template or AI-sounding resume ("nothing more than a template", "generated by very poorly worded AI").
- **This one hits us, said straight:** our drafting is AI-assisted and the gig doesn't say so yet. The fix has to be visible: a new check, `resume_lint.py`, fails any rewrite that adds a number, year, % or $ amount that wasn't in the buyer's own resume, or uses stock phrases like "results-driven". Self-tests pass 9/9. The gig should add "AI-assisted drafting, every line edited and checked by a person".
- There were no new research items, Atlas comments or Grok tasks since 11:25. All 14 INBOX items already have a Claude review.

**Next:** Atlas re-checks the benchmark (the Fiverr numbers came from cut-off pages). Then the gold sample on a made-up resume marked as made-up, so no real person's details go in the repo.
**Your taps:** nothing new.
1. **Issue #21: hold the El Portal DM and Founding 3 until the GEO audit passes the gate?** *Recommendation: Yes, hold.*
2. **Tap 18 (read the Review Desk sample) is still the one that moves money first.** *Recommendation: Yes, if the 4★ two-step reply reads like one you'd want for your own shop.*

## 2026-11-22 — 11:25 UTC hourly run
**Moved:** **The AI search check (GEO audit) now covers the 3 things buyers are warned about** (gate step 2 prep, Gravity-Studio PR #54).
- **What was missing:** the benchmark found 3 gaps in our audit. It never checked whether a site blocks the AI engines. It never wrote down which websites the AI used as sources. It never checked the new free ChatGPT business profile.
- **The fix:** all three are now steps in the audit checklist. A new check refuses to score an audit if any of them is blank. It also refuses an audit whose questions changed midway, or that says claiming the ChatGPT profile will "rank you higher" (OpenAI says it doesn't). Self-tests pass 15/15.
- **Why it matters:** the free tools give a score. Ours shows the actual answer, the sources behind it, and whether the engines can even read the site. That is the only reason to pay $149, so it has to be in every audit.
- There were no new research items, Atlas comments or Grok tasks since 10:25.

**Next:** Atlas reviews PR #54 and the benchmark (PR #20). Then the gold sample: a full audit of our own business. The ChatGPT part needs a signed-in browser (Atlas or you).
**Your taps:** nothing new.
1. **Issue #21: hold the El Portal DM and Founding 3 until the GEO audit passes the gate?** *Recommendation: Yes, hold.*
2. **Tap 18 (read the Review Desk sample) is still the one that moves money first.** *Recommendation: Yes, if the 4★ two-step reply reads like one you'd want for your own shop.*

## 2026-11-22 — 10:25 UTC hourly run
**Moved:** **The AI search check (GEO audit) has its first quality-gate step: a benchmark** (gate step 1 drafted, PR #20).
- **What others charge:** two Fiverr sellers do a one-time AI search audit for $40 and $50 in 3 days. Ours is $149 in 2 days. So we win on speed, not price.
- **The bigger finding:** there are now **free** checks. Insites and HubSpot score a business in ChatGPT, Gemini and Perplexity in about a minute. ChatGPT also launched free business profiles on Nov 10 (reported by several outlets). Our audit is only worth paying for if the sample shows what the free tools don't: a screenshot of the real answer to the customer's own question, and 3 fixes.
- **Two gaps found and one fixed:** our audit never checked whether the site blocks AI crawlers. A new checker reads the site's public robots.txt and flags it (self-tests 12/12). Writing down which sources each AI cites is proposed for the gold sample.
- No new research items, Atlas comments or Grok tasks since 09:25.

**Next:** Atlas verifies the benchmark. Then the gold sample: a full audit of our own business. It needs a signed-in browser for ChatGPT (Atlas or you).
**Your taps:**
1. **New decision (issue #21): hold the El Portal DM (tap 2) and Founding 3 (tap 17) until the GEO audit passes the gate?** These were queued before your quality-gate rule, but the audit hasn't passed it. *Recommendation: Yes, hold. Send the Review Desk trial first; it has passed 3 of 5 steps.*
2. **Tap 18 (read the Review Desk sample) is still the one that moves money first.**

## 2026-11-22 — 09:25 UTC hourly run
**Moved:** **The Wellness Blog benchmark now has real buyer complaints, the last empty row before Atlas can score it** (gate step 1 → ready for step 3, PR #19).
- **What buyers of blog writing complain about:** we read the public reviews of WriterAccess and Textbroker, two big blog-writing marketplaces, and kept only reviews from people who paid for posts. 5 are quoted word for word. 3 of the 5 say the same thing: they got AI-written or copied text. The others say the writing was poor or the writer ignored their instructions.
- **This one hits us, so we say it straight:** our posts are AI-assisted, and the offer already says so. The fix is not "no AI". It is: say AI up front, every claim linked to a source we opened (checked by `post_lint.py`), you approve topics first, and the first month is paid only after you approve post 1. I suggest Atlas score this row 4/5, not 5.
- There were no new research items, Atlas comments or Grok tasks since 08:25. All 14 INBOX items already have a Claude review.

**Next:** Atlas re-opens the 5 reviews and scores both blog samples (step 3). Then it comes to you to read (step 4).
**Your taps:** nothing new. **Tap 18 (read the Review Desk sample) is still the one that moves money first.** *Recommendation: Yes, if the 4★ two-step reply reads like one you'd want for your own shop.*

## 2026-11-22 — 08:25 UTC hourly run
**Moved:** **The Black Seed blog sample has passed its last pre-sale check** (Wellness Blog Engine, gate step 2, Gravity-Studio PR #53).
- **What was blocking it:** two study summaries had to be re-read before any buyer sees the post, and PubMed blocks our cloud.
- **How we got around it:** we found other official copies. The 2026 review is free in full on PubMed Central, and every number in the post matched (blood pressure −3.25/−2.75, blood sugar −18.6, HbA1c −0.56, the "further trials needed" quote). The 2025 review's summary is listed in a journal index (DOAJ).
- **One fix:** the 2025 review looked at 82 trials and combined 79 of them, not all 82. The post now says that. The automatic check passes (1,196 words, self-tests 15/15).
- There were no new research items, Atlas comments or Grok tasks since 07:25. All 14 INBOX items already have a Claude review.

**Next:** Atlas confirms "79 combined" on the journal's own page, then scores both blog samples (step 3). Grok still owes 3 real buyer complaints for the blog benchmark.
**Your taps:** nothing new. **Tap 18 (read the Review Desk sample) is still the one that moves money first.** *Recommendation: Yes, if the 4★ two-step reply reads like one you'd want for your own shop.*

## 2026-11-22 — 07:25 UTC hourly run
**Moved:** **The Listing Makeover now has a test set, the same kind the Review Desk has** (Gravity-Studio PR #52).
- **What it tests:** 8 made-up seller requests (test inputs, not real shops) built around the traps a careless rewrite falls into:
  - a seller who wants "heals eczema" kept
  - no wrist size given
  - silver-tone copper that's tempting to call sterling
  - crystal lore
  - a keyword-stuffed title
  - a seller asking for "Only 2 left!"
- **New check:** every number in a rewritten listing (sizes, weights, burn times) must come from what the seller told us. A listing that says "5 oz" when the seller said 4.5 now fails automatically.
- **Results:** the 8 good listings pass 8/8. The 8 deliberately bad ones are all caught (8/8). My first draft of the good set failed 4 of them, which shows the check has teeth.
- There were no new research items, Atlas comments or Grok tasks since 06:25. All 14 INBOX items already have a Claude review.

**Next:** Atlas scores the Listing Makeover sample and this test set, then checks SweetSoftSkin's contact route for the Review Desk trial.
**Your taps:** nothing new. **Tap 18 (read the Review Desk sample) is still the one that moves money first.** *Recommendation: Yes, if the 4★ two-step reply reads like one you'd want for your own shop.*

## 2026-11-22 — 06:25 UTC hourly run
**Moved:** **The Review Desk's free-trial message is written and checked** (gate step 5 prepared, `quality/review-reply-desk/free-trial.md`). It goes out only after you say Yes on tap 18 and OK the exact text.
- **What it sends SweetSoftSkin:** three free replies to their own reviews, copied word for word from the sample Atlas verified. These are the two-step reply to Michael's 4★ Chrism review and two 5★ replies. It has no price, no "cheaper than" claims, and never says "you have reviews without a reply". It is signed with your business line and says no reply is needed.
- **New check:** `trial_check.py` blocks a trial message that names a price, edits a verified reply, skips the business line or goes through Etsy Messages. Self-tests pass 14/14.
- **Blocker found:** we can't find SweetSoftSkin's website, email or Instagram. A web search shows only their Etsy shop, and we never pitch through Etsy Messages. The message is on **HOLD** until Atlas checks their Etsy About page from his browser.
- There were no new research items, Atlas comments or Grok tasks since the 05:45 fixes. All 14 INBOX items already have a Claude review (PR #2).

**Next:** Atlas looks for SweetSoftSkin's own contact route. He also lists 2 Flagstaff businesses with a recent under-5★ Google review that has no response, for trials 2–3, then scores PR #51 and the Listing/Wellness samples.
**Your taps:** nothing new. **Tap 18 (read the Review Desk sample) is still the one that moves money first.** *Recommendation: Yes, if the 4★ two-step reply reads like one you'd want for your own shop.*
**Decision coming (no tap yet):** what if SweetSoftSkin has no contact route outside Etsy? *Recommendation: skip them rather than use Etsy Messages, and run the trial on the Flagstaff Google-review prospects instead.*

## 2026-11-22 — 05:30 UTC (Atlas review on PR #14 answered)
**Moved:** Atlas passed the Listing Makeover benchmark, on condition of 5 fixes. All 5 are made:
- **The flaw count is corrected:** 8 of the old 12 Davias titles (not 10) were 15+ words.
- **4 Fiverr gigs and one article are marked unverified.** Fiverr and that site blocked his check.
- **The price claim is restated on verified rows only:** we charge $2.98–$5 a listing, and the verified competitors charge $15. "Cheapest" is not claimed until a browser confirms the Fiverr prices.
- **Two smaller fixes:** the PeoplePerHour row now matches the page, and the "140 characters" point covers that gig only.

**Next:** Atlas sets the final step-3 scores. Then the sample comes to you.
**Your taps:** nothing new. One question is already known: **what wrist size should the bracelets list?** The listings can't be called ready to paste until it's filled in.
## 2026-11-22 — 05:25 UTC hourly run
**Moved:** **The Review Desk's test set now holds our own rules** (Gravity-Studio PR #51).
- **What was wrong:** the "perfect" example replies we test against passed 6/6, but 3 of them claimed things no owner had confirmed: "We've changed how we update customers", "we're tightening how we schedule", and an invented "carne asada night". That is exactly what our Desk promises never to do.
- **The fix:** the test now runs the Desk's own reply check too. The 3 replies are rewritten to "I'm looking into it". We added 8 deliberately bad replies that must fail, and all 8 do. The good set passes 8/8.
- **Atlas passed the canned-reply check** (PR #47). The short-sentence fix is in, so a plain "Thank you!" in two replies is fine. Atlas said that fix lifts the Desk's last scorecard row to **5/5**, once he confirms it.
- There were no new research items or Grok tasks since 04:25.

**Next:** Atlas reviews PR #51, then gives the final Listing Makeover and Wellness Blog scores.
**Your taps:** nothing new. **Tap 18 (read the Review Desk sample) is still the one that moves money first.** *Recommendation: Yes, if the 4★ two-step reply reads like one you'd want for your own shop.* Also still open: what wrist size should the bracelets list (Listing Makeover).

## 2026-11-22 — 04:25 UTC hourly run
**Moved:** **The Wellness Blog Engine has a sample written for a real business** (gate step 2, `quality/wellness-blog-engine/gold-sample-002-winter-sun.md`).
- **Who it's for:** Winter Sun Trading Co., the Flagstaff apothecary on San Francisco St. They sell dried ashwagandha root. Their journal's newest post that we could see is from August 2020. **Nobody contacted them.**
- **The post:** ashwagandha, done the way you asked. It opens with the Ayurvedic tradition, with the sources named: the Charaka Samhita via a 2011 review, the churna powder with ghee, honey or milk, and the "smell of the horse" name. Then it covers what the NIH says the small trials found for stress and sleep. Then it lists who should skip it: pregnancy, liver, thyroid, autoimmune conditions and sedatives. All 3 sources were opened today, and the post passes `post_lint.py --presale` at 1,052 words.
- **Which local practices need a blog:** we checked the websites of all 10 Flagstaff prospects. 5 have no blog or a dormant one (Winter Sun, Flagstaff Clinic of Naturopathic Medicine, Acupuncture Wellness Center, True North, Munderloh). 2 already post, so we skip them for now. One (Synergistic Healthcare) has moved to Prescott (`prospect-blog-check.md`).
- There were no new research items, Atlas comments or Grok tasks since 03:25.

**Next:** Atlas scores the ashwagandha sample (step 3). Then it comes to you to read (step 4).
**Your taps:** nothing new. **Tap 18 (read the Review Desk sample) is still the one that moves money first.** *Recommendation: Yes, if the 4★ reply reads like one you'd want for your own shop.* Coming after Atlas: *"Would you pay for the ashwagandha post?"* Then, if yes, the free trial to Winter Sun, sent only with your OK on the exact message.

## 2026-11-22 — 03:25 UTC hourly run
**Moved:** **The Wellness Blog sample post is nearly ready for review** (gate step 2, Gravity-Studio PR #49).
- **Traditional section:** it now names its sources, per your Nov 21 direction. These are *Sahih al-Bukhari* 5687 (the "healing for all diseases except death" saying, and how the seed was prepared) and Avicenna's *Canon of Medicine*. Two lines had no source, so they were cut: a list of Avicenna's uses and "2,000 years".
- **Seller source:** a tea shop's blog was cited for the brewing steps. It's gone, and the brewing steps are now labelled a kitchen method.
- **New check:** `post_lint.py` blocks a post that has no named traditional text, cites a shop, makes an unhedged cure claim, skips the "see your clinician" and "don't stop your medicine" lines, or runs past 1,200 words. Self-tests pass 15/15. The new sample passes; the old one fails 2 rules.
- **Still open:** PubMed blocks the cloud, so the two study abstracts need a browser re-read before any buyer sees the post. Atlas is asked on PR #49.
- There were no new research items, Atlas comments or Grok tasks since 02:25.

**Next:** Atlas re-reads the 2 abstracts and scores the Listing Makeover. Claude writes a blog sample for a real public wellness business.
**Your taps:** nothing new. **Tap 18 (read the Review Desk sample) is still the one that moves money first.** *Recommendation: Yes, if the 4★ reply reads like one you'd want for your own shop.*

## 2026-11-22 — 02:25 UTC hourly run
**Moved:** **The Wellness Blog Engine has its benchmark** (gate step 1, `quality/wellness-blog-engine/benchmark.md`).
- **Agencies:** the closest done-for-you plans charge $390 a month (BKA Content, 4 posts) and $600 a month (a Contra wellness writer). Our Starter is $150 for 4 posts, with sources and an image suggestion on each.
- **Freelancers:** the best-rated Fiverr health writer charges $30 a post (5.0 from 22). Four of those cost $120, so we match them and include more, but we don't beat them on price.
- **Software:** $99 a month buys 31 AI posts. We never pitch cheaper or faster than that.
- **Still missing:** real buyer complaints about blog services. None of the pages we read had any, so Grok is on it.
- **Research:** Atlas's one new nit is fixed: the cookbooks file title now says 98 notebooks, not 91 (PR #2).

**Next:** Grok adds the buyer complaints. Atlas verifies the benchmark and scores the Listing Makeover. Claude finishes the blog sample's fixes.
**Your taps:** nothing new. **Tap 18 (read the Review Desk sample) is still the one that moves money first.** *Recommendation: Yes, if the 4★ reply reads like one you'd want for your own shop.*

## 2026-11-22 — 01:25 UTC hourly run
**Moved:** **The Review Desk now blocks canned replies automatically.** Buyers' top complaint about review services is replies that all sound the same. Atlas took a point off the Desk for not checking that. The reply check now fails any batch where the same sentence shows up in two replies (Gravity-Studio PR #47). It passes 16/16 of its own tests, and our 8-review sample passes clean. When I planted a copied sentence, it caught it.
- **Research:** both new items are reviewed. The Jensen Huang clip says "go deep, not broad", which is already your focus order. The Claude cookbooks gave us the official skill-file limits, and all 4 of our skills fit them.
- **Issue #12** (transcribe the mentalium video): Atlas found it's a silent slideshow with nothing to transcribe. Its content is already in `research/mentalium-claude-cookbooks.md`.

**Next:** Atlas re-scores the Desk's complaint row, then scores the Listing Makeover sample (PR #14). Grok is back today for the Fiverr checks.
**Your taps:** nothing new. **Tap 18 (read the Review Desk sample) is still the one that moves money first.** *Recommendation: read the 4★ two-step reply first; if it reads like something you'd want for your own shop, tap Yes.* Issue #12 can be closed; *recommendation: close it.*

## 2026-11-22 — 00:25 UTC hourly run
**Moved:** **The Listing Makeover has its benchmark** (gate step 1, `quality/listing-makeover/benchmark.md`). It also caught a real flaw in our own sample, and that flaw is now fixed.
- **Price and speed:** the verified competitors charge $15 for one listing in 2–4 days (PeoplePerHour), or from $50 in 3 days (Contra). We charge $2.98–$5 a listing, and Basic delivers in 1 day. *Update, 05:45 UTC: Atlas's live browser check confirmed the Fiverr prices. The lowest active per-listing price is Uri B.'s $50 for 10 listings, or $5 each. The cheapest package is Natalia's $15, but it covers only 2 listings, $7.50 each. Our Basic matches the $5, and our bigger packages beat it.*
- **The flaw:** Etsy now tells sellers to keep titles **under 15 words** and **not repeat words**. 8 of our 12 Davias titles were 15+ words (corrected from 10 after Atlas's recount), and all 12 said "Bracelet" twice. The one verified competitor still sells the old long style.
- **The fix:** all 12 titles are rewritten (davias PR #7), e.g. *"Violet Vortex Amethyst & Clear Quartz Crystal Bracelet — Double Helix, Handmade Steel Wire"*. A new check fails any title that breaks the rule: old titles 0/12, new 12/12, self-tests 21/21 (Gravity-Studio PR #46).
- **Lapis Lazuli** is a rock, not a crystal, so its title and tag now say "natural stone", like Amber and Obsidian.
- **Research:** the DMSO item is reviewed. It isn't used for any service; see the INBOX note on PR #2.

**Next:** Atlas verifies the benchmark sources and scores the Davias sample (step 3). Then it comes to you (step 4). The Review Desk still waits on your read (tap 18).
**Your taps:** nothing new.
- **Please hold the "Etsy listing sample — would you pay?" read** until Atlas scores it. When you do read it, use the new titles on davias PR #7. *Recommendation: answer tap 18 (Review Desk) first; it is one step further along.*

## 2026-11-22 — 00:24 UTC (Atlas review on PR #11 answered)
**Moved:** **The Review Reply Desk passed gate steps 1–3.** Atlas checked every source and scored the sample **5/5/4/5/4/4**. His fixes are made:
- The Marqii prices are corrected. The plan at our $149 level is $145, so Desk Plus matches it rather than beating it.
- "Free" is gone from the Google AI-replies line. Google is only testing that feature, and no price has been published.
- The Fiverr agency's prices are marked unverified.

Desk at $79 is about half the price of the closest verified service for the same 30 replies.
**Next:** your read (step 4). Then a free trial to SweetSoftSkin, sent only with your OK.
**Your taps:** one new tap (dashboard tap 18): **read the Review Desk sample. Would you pay for this?** It shows 8 real reviews with our reply under each (`quality/review-reply-desk/gold-sample-replies.md`). *Recommendation: Yes, if the two-step reply to the 4★ review reads like what you'd want for your own shop.* Still coming: the 1-business-day promise for 1–2★ reviews.

## 2026-11-21 — 23:24 UTC hourly run
**Moved:** The Review Desk benchmark is drafted (gate step 1, `quality/review-reply-desk/benchmark.md`). Grok is away until Nov 22, and it was the only thing blocking the scorecard. What it found:
- **Human services:** we match or beat them on price. Desk is $79 for up to 30 replies. The closest verified service charges $149 for the same 30 replies. Marqii charges $145 a location on an annual contract. (A Fiverr agency at $232 a location is still unverified.)
- **Software:** $15–19 a month, instant replies. We lose to it on price and speed. So we never pitch "cheaper" or "faster". We pitch "written for you, specific, checked".
- **What buyers complain about most:** canned replies, then AI replies that leak private details or promise fixes that aren't real. Our reply check already blocks the second.

Atlas's last check is also applied. He verified all 8 quotes word for word, and Barguest's reply came off HOLD, so the sample's accuracy score is now 5/5. The reply check still passes 9/9. Atlas's last robustness point on Gravity-Studio PR #45 was already fixed (28/28 self-tests at head `c1b1f2a`, one commit after the 27/27 Atlas verified). There were no new research items.
**Next:** Atlas verifies the benchmark sources and scores the last 2 rows. He should also read one headline we couldn't open, because it matters: Google may be testing free AI-drafted review replies. Then the sample comes to you (gate step 4).
**Your taps:** nothing new. Coming after Atlas scores: *should the Desk promise 1 business day on 1–2★ reviews instead of 2?* The dry run took about 2 minutes, and it would let us beat human services on speed too. *Likely recommendation: Yes.* Taps 16 and 17 still stand.

## 2026-11-21 — 22:24 UTC hourly run
**Moved:**
- **Your Founding 3 price, made safe** (Gravity-Studio PR #45). Prices hold, and there is no public discount. The first 3 GEO buyers can get $75, offered one-to-one only. I changed one part. The verdict asked for a Google review in return, but Google's rules ban giving a discount for a review, and Google removes those reviews from Maps. The US FTC rule bans paying for set opinions too. So in return they give a quotable sentence (marked "reduced price") and two introductions. A new check fails any draft that ties a price cut to a review.
- **One payment answer.** Atlas found that the GEO offer file still said "escrow or Stripe". It now says PayPal or Zelle, matching the payment message, and a check keeps it that way. Checks: 23/23 self-tests, 13/13 prices.
- **Review Desk gold sample:** all 5 of Atlas's points are fixed (gravity-studios PR #9).
  - The sales count is corrected to 5,792.
  - The 4★ reply now has two steps: a private Etsy message first, then the public reply. Etsy allows one public reply, and posting it locks the buyer's review.
  - The review count is corrected to 8.
  - Barguest's reply is on HOLD until we read the full review.
  - The pitch no longer calls unanswered 5★ reviews a problem.
  - The reply check passes 9/9.

Atlas scored the sample 4/5/4/5. The last two scores wait on Grok's benchmark.

No new research items this hour. The Listing Makeover sample for SweetSoftSkin couldn't be built: Etsy pages can't be fetched from the cloud run. It needs Atlas's browser to read 2 listings.
**Next:**
- Grok's benchmark (he's back Nov 22).
- Atlas re-checks #9 and #45 and reads the full Barguest review and 2 SweetSoftSkin listings.
- Claude writes the Listing Makeover sample.
**Your taps:**
- **New, tap 17: approve Founding 3 without the review condition?** $75 for your first 3 GEO buyers, in a DM only. In return: one quote and two introductions. *Recommendation: Approve. It keeps us inside Google's rules.*
- Tap 16 (payment messages) still needs a Yes once you've checked that Zelle works on godisdmt23@gmail.com.

## 2026-11-21 — 21:24 UTC hourly run
**Moved:** Your quality gate is in force, and the Review Reply Desk has its first **real** gold sample (gate step 2, gravity-studios PR #9). The old samples were invented examples. This one uses real public reviews:
- **SweetSoftSkin** (Peoria soap shop, 5.0 stars, 1,956 reviews). None of the 8 most recent reviews we read has a reply from the shop, including a 4★ on Sep 22 that says the Chrism soap "smells a lot like patchouli".
- We wrote 8 paste-ready replies, one per review. Each one uses the reviewer's name and a detail they gave. The 4★ reply answers his exact point without claiming anything changed. All 8 pass the reply check (8/8).
- Drafting took about 2 minutes once the reviews were read, well under the 20–40 min/month estimate.
- Honest limit: these are Etsy reviews, because Google review text couldn't be read from the cloud. A Google-profile sample (El Portal or Rescue Plumbing) follows. Nothing was posted, and nobody was contacted.

There were no new research items or Grok tasks this hour. Atlas's 4 points on #42 were already closed.
**Next:** Atlas scores the sample (gate step 3) and checks that Etsy lets a shop reply to a review. Grok writes the benchmark (step 1). Then Claude makes the Listing Makeover sample for the same shop.
**Your taps:** nothing new. Gate step 4 (your read: "would I pay for this?") comes after Atlas scores it. Tap 16 still needs a Yes once you've checked that Zelle works on godisdmt23@gmail.com. *Recommendation: Approve.*

## 2026-11-21 — 20:24 UTC hourly run
**Moved:** Listing Makeover has its first 10 prospects (Gravity-Studio PR #42). I read each Etsy shop's public page today. 5 of the 10 are in Arizona, and nobody has been contacted. A new check scores each shop's real titles. The top 3:
- **SweetSoftSkin** (Peoria, 5,775 sales). Its titles use only 21–27 of Etsy's 140 characters.
- **PlantedInWire.** Wire-wrapped crystal jewelry, the closest match to our Davias sample.
- **SouthsideCreation** (Lake Havasu City). It has 1,034 listings with stock numbers in the middle of the titles.

New rule: pitches never go through Etsy Messages, because Etsy bars unsolicited sales messages and a report could flag the shop. They go through each shop's own website or Instagram. Also, on the loan research (PR #2), Atlas asked for a second state. Arizona's law turned out to set the loan at **at least** the cash value, not at most. The file is corrected, and the conclusion doesn't change: no policy lends against the $1M face amount.
**Next:** Atlas reviews #42 and re-checks #2. Then Claude finds the contact route for shops 1–3 and writes their 2 free sample rewrites.
**Your taps:** nothing new. Tap 8 (approve the Review Desk and Listing Makeover pitches) now names the first 3 shops. *Recommendation: Approve.* Tap 16 still needs a Yes once you've checked that Zelle is set up on godisdmt23@gmail.com.

## 2026-11-21 — 20:08 UTC (Zelle address on PR #39)
**Moved:** A PR #39 comment from your account said to send Zelle to **godisdmt23@gmail.com**, not 747-528-7039, because the phone is unreliable right now. That change is done everywhere the payment messages, the GEO checklist and the README show Zelle. The check now fails any Zelle line that uses the old phone, and it still passes: 19/19 self-tests, 13/13 prices.
**Your taps:** tap 16 / issue #8 is the same approval. The messages now read "PayPal to gravity4u@gmail.com, or Zelle to godisdmt23@gmail.com". *Before you approve, check that Zelle is set up on godisdmt23@gmail.com. A wrong Zelle email sends a buyer's money somewhere you can't get it back. Recommendation: Approve once that's confirmed.*

## 2026-11-21 — 19:16 UTC (Atlas review on Davias PR #10 answered)
**Moved:** Atlas reviewed Davias PR #10 (all 12 Helix designs) and called it **mergeable**. I fixed his one doc point: `HELIX_COLLECTION.md` now says where the stone profiles live, and it no longer calls every bead a crystal.
**Your taps:** one new maker question, needed before the first sale, not before the merge. **Is Octavia's citrine natural, or heat-treated amethyst?** The Jungle Gold page promises buyers we'll tell them which. *Recommendation: if you're not sure, tap "heated"; the page will then say "heat-treated citrine". It's the honest default, since most citrine sold is heated.*

## 2026-11-21 — 18:50 UTC (Atlas review on PR #39 answered)
**Moved:** Atlas reviewed the payment messages (Gravity-Studio PR #39). He confirmed all 13 prices independently. He found 6 things to fix, and all 6 are fixed:
- The Blog Engine line wrongly called post #1 "free". It is written before payment, and it is part of month 1 if they continue.
- The Visibility Pack now says "bundle saves $19". Before, $49 + $149 next to $179 looked like a math mistake.
- The check now catches the wrong "23" PayPal address on any line, even when the word PayPal isn't there. It also checks every line of the messages, not only the quoted ones.
- On a fresh copy of the repo, the check used to fail 8 of 13 prices because it couldn't find the offer files. A new `--fetch` option fixes that, and it now passes 13/13.
- Its self-tests pass 17/17.

**Next:** Atlas re-checks #39. Then Claude picks 10 Etsy shops for Listing Makeover.
**Your taps:** one new tap (dashboard tap 16): **approve the payment messages?** When a buyer says yes, they get one short message: PayPal to gravity4u@gmail.com or Zelle, the price, and "I start as soon as it lands." *Recommendation: Approve. Without it, a buyer's yes waits for you.* Taps 15 (test call to the business line), 12 (Facebook in Metricool) and 14 (Davias "made by hand") still stand.

## 2026-11-21 — 18:24 UTC hourly run
**Moved:** Listing Makeover now has its checker (Gravity-Studio PR #41). The process always said a script checks every listing, but none existed. `listing_lint.py` checks:
- title length
- Etsy's once-only `% : &` rule
- all 13 tags, each 20 characters or less, with no repeats
- tags that got cut off
- cure, guarantee and fake-scarcity words
- the "not medical advice" line on any lore

Its self-test passes 13/13. On its first run it found 2 real problems in our own Davias sample:
- The Ember & Ice title used "&" twice, so Etsy would refuse it.
- One tag was cut off ("pink tourmaline brac").

Both are fixed on Davias PR #7, and all 12 listings pass. On PR #36, Atlas's 3 stale "not done yet" phone lines are struck. There were no new research items or Grok tasks since 17:24.
**Update 19:15:** Atlas reviewed #41 and called it mergeable. His 4 fixes are pushed, and the self-test passes 16/16. **Merge order for Gravity-Studio** (they all touch CURRENT_TASK.md): #35 → #41 → #37 → #38 → #39 → #40. Whoever merges second keeps every Claude Progress line.
**Next:** Atlas re-checks #36 and reviews #41, #39, #40 and Davias #8 → #11. Then Claude picks 10 Etsy shops for Listing Makeover.
**Your taps:** one new tap (dashboard tap 15): **call or text (747) 222-6980 once from another phone. Does it ring your Google Voice?** Atlas wants this confirmed before any post or pitch carries the number. *Recommendation: Yes, 30 seconds, do it before connecting Metricool.* Taps 12 (connect Facebook in Metricool) and 14 (Davias "made by hand") still stand. Fastest money is still DMing El Portal and posting the Resale Concierge offer.

## 2026-11-21 — 17:24 UTC hourly run (also covers 16:24)
**Moved:** The first social post batch is written (Gravity-Studio PR #40). It has 10 draft posts for Facebook, X, LinkedIn, Threads and Bluesky: 3 for the Resale Concierge, 3 for the Review Reply Desk, 2 for Listing Makeover, 1 for the AI-search audit and 1 for the Reactivation Kit. Every post ends with your business line. A new check runs before you see any batch. It checks each network's length limit, that every price matches the offer, that no "guarantee", "#1", cure or fake-scarcity words appear, and that the only phone number is the business line. It passes 10/10. On its first run it caught one post 1 character over X's 280 limit, now fixed.
- At 16:24, PR #39 added payment-request drafts for all 13 priced offers. A check confirms that PayPal only ever means gravity4u@gmail.com.
- There were no new research items, Atlas comments or Grok tasks since 15:24.
**Next:** Atlas reviews #39/#40 and the Davias stack (#8 → #11). Then the timed Review Desk dry run.
**Your taps:** one new tap (dashboard tap 12): **connect your Facebook Page in Metricool.** We checked, and Metricool has no network connected yet, so nothing can be scheduled. Batch 01 is waiting for it. *Recommendation: Yes. Connect Facebook first, then approve batch 01. We schedule nothing before you approve.* The open Davias "made by hand" tap (14) still stands. Fastest money is still DMing El Portal and posting the Resale Concierge offer.

## 2026-11-21 — 15:24 UTC hourly run
**Moved:** The Davias Crystal Finder now knows all 22 stones (Davias PR #11, stacked on #10). Before, it only knew the original 6. It also asks one new question: **your skin's undertone** (Cool, Warm, Neutral or Not sure). Then it suggests Helix designs styled for that undertone, using each design's own matching text. For example, Cool suggests Reef Ripple and Lapis Current, and Warm suggests Earthfire Twist and Jungle Gold. A line on the page says undertone matching is styling advice, not a rule.
- Every "tradition" choice (Calm, Grounding & protection and so on) only lists stones whose own Traditional label says it. A standing check enforces this.
- Site checks pass 302/302 and browser checks pass 9/9.

There were no new research items, Atlas comments or Grok tasks since 14:24. The dashboard data was rebuilt, but this run could not upload it because the artifact tools weren't available.
**Next:** Atlas reviews Davias #8 → #11 and Gravity-Studio #37/#38. Then the timed Review Desk dry run.
**Your taps:** nothing new. The open one is still dashboard tap 14 / issue #7: **are the Davias pieces being made by hand now?** Yes keeps "made by hand"; No changes it to "designed by hand". *Recommendation: answer before launch.* Fastest money is still DMing El Portal and posting the Resale Concierge offer.

## 2026-11-21 — 14:24 UTC hourly run
**Moved:** All 12 Helix bracelets are now on the Davias site (Davias PR #10, stacked on #9). The 7 that were missing (Reef Ripple, Ember & Ice, Northern Lights, Jungle Gold, Amber Mist, Lapis Current, Obsidian Spiral) got product pages, plus 12 new stone profiles labelled Proven / Traditional.
- Amber and obsidian are labelled "not a mineral". The homepage no longer says every bead is stone.
- Citrine is flagged as usually heat-treated amethyst. Black tourmaline says it does not block EMF.
- Amber carries the FDA warning against baby teething necklaces.
- The site check now reads `HELIX_COLLECTION.md` and fails if any design drifts from the site. It passes 222/222.
There were no new research items, Atlas comments or Grok tasks since 12:24. The 13:24 run left no commits.
**Next:** Atlas reviews Davias #8 → #9 → #10 and Gravity-Studio #37/#38. Then the Crystal Finder learns the new stones.
**Your taps:** one correction, same tap as before (dashboard tap 14 / issue #7). You already removed "Made by Octavia" from the site on Nov 17. Three lines still say "made by hand" (home, shop, about). **Are the pieces being made by hand now?** Yes keeps those lines; No changes them to "designed by hand". *Recommendation: answer before launch.* Fastest money is still DMing El Portal and posting the Resale Concierge offer.

## 2026-11-21 — 12:24 UTC hourly run
**Moved:** The Fiverr gigs now have their cover images. Gravity-Studio PR #38 adds six 1280 × 769 covers, one per gig, and a script that rebuilds and checks them. The check passes 8/8: right size, nothing cut off, no phone/email/links (Fiverr bans them on images), and no "guarantee", "#1" or cure words. It caught two problems on the first render, both fixed. Gig 1's top package also said "answered within 48h"; it now says 2 business days, matching the Review Desk promise. Since 11:24 there have been no new research items, Atlas comments or Grok tasks.
**Next:** Atlas reviews #37/#38 and re-checks #35. Then the timed Review Desk dry run.
**Your taps:** nothing new. When you create the Fiverr seller account (dashboard tap 13), the 6 gigs are ready to paste with covers. Fastest money first: DM El Portal, post the Resale Concierge offer.

## 2026-11-21 — 11:24 UTC hourly run
**Moved:** Review Reply Desk (Gravity-Studio PR #35) now has a reply checker. `review_lint.py` checks every drafted reply before it goes out: 2–4 sentences, signed, no refunds or discounts you didn't approve, never asks for a review change, no patient details for clinics, and no claims that something changed at the business unless you confirmed it. Its test passes 12/12. On its first run it caught one of our own sample replies promising "price cards this month", a fact no owner had confirmed. That sample is fixed, and so is a second one that invented a "carne asada night". Since 10:25 there have been no new research items, Atlas comments or Grok tasks.
**Next:** Atlas re-checks #35 and reviews Davias #8/#9. Then the timed Review Desk dry run on a real public profile (drafts only, nothing posted).
**Your taps:** nothing new. The two Davias questions from the 10:25 run (issue #7) are still the top wording blockers. Fastest money first: DM El Portal, post the Resale Concierge offer.

## 2026-11-21 — 10:25 UTC hourly run
**Moved:** Davias PR #9 (stacked on #8) fixes the crew-side Atlas #4 launch items. On "every day", the crystal finder now leaves selenite out of the stone pair and offers it only for special occasions. A new browser test passes 5/5; the old code failed 2 of those cases. The drop page and home button now say "coming soon — no date or checkout yet", and "Drops sell out" is gone. Anklets are no longer all called beach-ready, so the Soft Light (selenite) page no longer contradicts itself. All 126 site checks pass. Since the 09:24 run there have been no new research items, Atlas comments or Grok tasks.
**Next:** Atlas reviews Davias #8 and #9 and re-checks Gravity-Studio #35. Then the timed Review Desk dry run.
**Your taps:**
1. **Davias: is Octavia making the pieces right now?** Yes → "Made by Octavia, by hand" stays. No → we switch to "Designed by Octavia" until she is. *Recommendation: answer this before launch. It's the last wording blocker in Atlas #4.*
2. **Keep "Founders Drops are numbered 1 to 100"?** *Recommendation: No (we drop the line) unless you plan to number them.*
Everything else is unchanged and listed on the dashboard. Fastest money first: send the El Portal DM, post the Resale Concierge offer.

## 2026-11-21 — 09:24 UTC hourly run
**Moved:** Davias PR #8 builds 5 Helix pieces into the site. It adds matching text, Double/Triple/Single filters, the Blush Trinity tourmaline fix and the Earth Circle care fix. A new site check passes 117/117. Review Reply Desk (PR #35): all 6 Atlas points are fixed. The promise is now 2 business days (with daily collection), there is a no-invented-facts rule, overage is defined, and the time estimate is labelled untested. PR #29's path and issue #23's flash line are fixed too. Two new research items were reviewed, not applied. The loan plan must call El Portal and the others *prospects*, not buyers. 7 of the 9 "services split" ideas are regulated; credit repair in Arizona needs a surety bond (A.R.S. §44-1708). Recommendation: keep only Plan Builder and Income Proof as candidates.
**Next:** Atlas reviews Davias #8 and re-checks #35. Then Davias #4 (launch fixes) and a timed Review Desk dry run.
**Your taps:** nothing new this run. The open list is on the dashboard. Fastest money first: send the El Portal DM, approve the two pitches, create the Fiverr account.

## 2026-11-21 — 08:24 UTC hourly run
**Moved:** Missed-Call Rescue is un-parked (MASTER_PLAN #2). Gravity-Studio PR #34 adds a $149 Dead-Lead Reactivation Kit: the business exports its old quotes and missed callers, and we return a cleaned list plus a 3-text win-back sequence that it sends from its own phone. We need no logins and spend $0. `reactivate.py --test` passes 10/10 (consent, opt-out, duplicates, 30-day hold, a STOP line on every text). It's built this way because the Nov 14 test found no buyers for a standalone missed-call *diagnostic*. No new research items or Atlas comments since the 08:23 run.
**Next:** Atlas reviews #34, #33, #32 and #28; then Davias #5 (Helix build.py).
**Your taps:** nothing new. The open list is in the 08:16 and 08:23 entries below and on the dashboard. The top one is still: **is gravity4u@gmail.com your PayPal?** It now unlocks two $149 offers.

## 2026-11-21 — 08:23 UTC hourly run (second run this hour, complements the 08:16 entry)
**Moved:** Gravity-Studio PR #33 opened: GEO audit denominator fix + a tested scorer (`geo_score.py --test` passes), the last crew-side item before a paid $149 audit. PR #32 (Magnetico ledger): Atlas's 3 corrections pushed (Nov 19, dad handoff, cash-record rule). PR #28: lymph count corrected (165 itemised, not 198), GBP "3 buyers" flagged, retitled partial. Plugin PRs in all 4 repos reworded per Atlas. Money map challenged: the SNAP student rule (half-time students generally can't get SNAP without 20+ hrs/week work) means "school + SNAP" can't simply be stacked; details in PR #2.
**Next:** Atlas re-checks #32, #28, #33; Missed-Call Rescue one-page offer; Davias #5.
**Your taps:** same four as the 08:16 entry, plus:
5. **Merge Gravity-Studio PR #32 (Magnetico ledger) once Atlas re-checks?** Yes — it puts your $1,000 on the books.

## 2026-11-21 — 08:16 UTC hourly run
**Moved:** All 9 research items now carry a Claude review (3 applied, 6 reviewed-not-applied with reasons) — PR #2. Claude's independent loan/trust check is done: the law caps any policy loan at cash value (NY Ins. Law §4222), so ✖ for $1M-now stands on two checks (Gravity-Studio #30). Command Center fixed per both Atlas reviews: every Master Plan line tagged open/owner/after, Missed-Call Rescue ranked, Healing Guide justified, §6 sequencing and §7 notification claim corrected (PR #3). Magnetico ledger fixes (PR #32) and the GEO runbook scoring fix (branch `claude/geo-scoring-fix`) were pushed this hour.
**Next:** Missed-Call Rescue one-page offer; Davias #5 (Helix build.py).
**Your taps (one each, recommendation first):**
1. **Merge gravity-studios PR #3 (Command Center)?** Yes — Atlas's blocking points are fixed.
2. **Is the PayPal address on the sales page right?** Yes/No — it's the last step before a $149 audit can be paid.
3. **Connect Instagram Messages?** Yes — only route to El Portal.
4. **Close Gravity-Studio #30 as answered?** Yes — two independent checks agree; no $1M-now path.

## 2026-11-21 (earlier)
**Moved:** Command Center written (operating loop, challenge protocol, ranked Master Plan). Plugin standards PRs open in all 4 repos. Research inbox triaged.
**Also moved:** Atlas #24 fixes (Gravity-Studio PR #28) and the skills library foundation (PR #29: geo-audit, research-to-action).
**Next:** #18 Wellness Blog Engine build; Davias #5/#4 in parallel.
**Your taps (when you're ready):**
1. Instagram Messages connected → El Portal GEO pitch can go out.
2. Business phone (Google Voice) → unlocks the Concierge post.
3. Where should gravity-studios be hosted (GitHub Pages or a domain)?
4. Is gravity4u@gmail.com the right PayPal address on the sales page?
5. Windows test of the Subliminal Rewire `main` build when one is ready.
6. Were there really 3 paying GBP buyers (Atlas #24)? If yes, who; if not, the record stays "needs 1 buyer".
