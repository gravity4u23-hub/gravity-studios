# Review Reply Desk: trial 2–3 prospects (gate step 5)

**Why this file:** trials 2–3 need a real gap, meaning a review under 5★ from the last 12 months with no owner response. Google Maps is blocked from the cloud. Birdeye's public review pages (reviews.birdeye.com) copy Google and Facebook reviews and **can** be read from the cloud. So one look covers most of the list, and Atlas only has to open the rows marked NEEDS-BROWSER.

**What the cloud read can't see (Nov 23, 13:40 UTC):** the star count on each review and, for certain, whether the owner replied. The reader saw no reply text, which is weaker than "no reply". So no row is ELIGIBLE yet, and `review_gap_check.py` refuses ELIGIBLE until someone looks at the rendered page.

**Privacy:** P004–P010 are health clinics. No reviewer names or review words go in this public repo. Their replies must never confirm that the reviewer was a patient (`skills/review-reply/SKILL.md`, HIPAA-safe pattern).

| ID | Business | Health | Source URL | Read (UTC) | Reviews / avg | Under-5 stars | Under-5 age (months) | Owner response | Status |
|---|---|---|---|---|---|---|---|---|---|
| P004 | Harmonizing Healthcare PLLC | yes | - | - | - | - | - | - | NOT-READ |
| P005 | Flagstaff Clinic of Naturopathic Medicine | yes | https://reviews.birdeye.com/flagstaff-clinic-of-naturopathic-medicine-148061800835039 | 2026-11-23 13:40 | 55 / 4.6 | unknown | - | not-in-text | NEEDS-BROWSER |
| P006 | Cedar Health Center | yes | - | - | - | - | - | - | NOT-READ |
| P007 | Munderloh Integrated Medical | yes | - | - | - | - | - | - | NOT-READ |
| P008 | Synergistic Healthcare PLLC | yes | - | - | - | - | - | - | NOT-READ |
| P009 | The Vitality Doctor (Dr Christina Kovalik NMD, LAc) | yes | https://reviews.birdeye.com/the-vitality-doctor-dr-christina-kovalik-nmd-lac-169623344289589 | 2026-11-23 13:40 | 23 / 4.5 | unknown | - | not-in-text | NEEDS-BROWSER |
| P010 | Acupuncture Wellness Center (Cynthia Hull) | yes | https://reviews.birdeye.com/hull-cynthia-acupuncture-wellness-center-168633802417920 | 2026-11-23 13:40 | 5 / 5.0 | none | - | not-in-text | NO-GAP |

**What each read found (no review text):**
- **P009 The Vitality Doctor is the best lead.** It has 23 reviews, all from Google, with a 4.5 average, so at least one is under 5★. Three reviews are 1–2 months old, and no reply text showed under any of the 5 reviews on the page. *Atlas: open the Google profile and find the under-5★ review. Record its stars and age, and whether a reply is visible. If it's within 12 months with no reply, mark it ELIGIBLE.*
- **P005 Flagstaff Clinic of Naturopathic Medicine** has 55 reviews averaging 4.6 (35 Google, 16 Facebook, 4 Yellow Pages). The newest one Birdeye showed is about 7 years old. Its directory page said 52 reviews and its own page said 55, so Birdeye's list may be out of date. Low priority: check Google only after P009.
- **P010 Acupuncture Wellness Center: no gap for a trial.** It has 5 Google reviews averaging 5.0, so every one is 5★. It isn't a trial candidate under this rule. It's still a Review Desk prospect, since no reply text showed under any of them.
- **P004, P006–P008:** not read yet. Next step: find each Birdeye page through a site search and add a row.

**Check:** `python3 review_gap_check.py` → `SUMMARY rows=7 errors=0`. Self-tests: `python3 review_gap_check.py --self-test` (20/20).
