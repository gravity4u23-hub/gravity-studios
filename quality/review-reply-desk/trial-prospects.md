# Review Reply Desk: trial 2–3 prospects (gate step 5)

**Why this file:** trials 2–3 need a real gap, meaning a review under 5★ from the last 12 months with no owner response. Google Maps is blocked from the cloud. Birdeye's public review pages (reviews.birdeye.com) copy Google and Facebook reviews and **can** be read from the cloud. So one look covers most of the list, and Atlas only has to open the rows marked NEEDS-BROWSER.

**Prospect city:** Flagstaff, AZ

**What the cloud read can't see (Nov 23, 13:40 UTC):** the star count on each review and, for certain, whether the owner replied. The reader saw no reply text, which is weaker than "no reply". So no row is ELIGIBLE yet, and `review_gap_check.py` refuses ELIGIBLE until someone looks at the rendered page.

**Privacy:** P004–P010 are health clinics. No reviewer names or review words go in this public repo. Their replies must never confirm that the reviewer was a patient (`skills/review-reply/SKILL.md`, HIPAA-safe pattern).

| ID | Business | Health | Source URL | Page name, city | Read (UTC) | Reviews / avg | Under-5 stars | Under-5 age (months) | Owner response | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| P004 | Harmonizing Healthcare PLLC | yes | - | - | - | - | - | - | - | NOT-READ |
| P005 | Flagstaff Clinic of Naturopathic Medicine | yes | https://reviews.birdeye.com/flagstaff-clinic-of-naturopathic-medicine-148061800835039 | unrecorded | 2026-11-23 13:40 | 55 / 4.6 | unknown | - | not-in-text | NEEDS-BROWSER |
| P006 | Cedar Health Center | yes | https://reviews.birdeye.com/cedar-health-176946178189941 | Cedar Health, Tucson AZ | 2026-11-23 14:30 | 7 / 4.4 | unknown | - | not-in-text | WRONG-PAGE |
| P007 | Munderloh Integrated Medical | yes | https://reviews.birdeye.com/munderloh-chiropractic-157254650808482 | Munderloh Chiropractic, Flagstaff AZ | 2026-11-23 14:30 | 197 / 4.8 | unknown | - | not-in-text | WRONG-PAGE |
| P008 | Synergistic Healthcare PLLC | yes | https://reviews.birdeye.com/synergistic-healthcare-155743603329035 | Synergistic Healthcare, Flagstaff AZ | 2026-11-23 14:30 | 16 / 5.0 | none | - | not-in-text | NO-GAP |
| P009 | The Vitality Doctor (Dr Christina Kovalik NMD, LAc) | yes | https://reviews.birdeye.com/the-vitality-doctor-dr-christina-kovalik-nmd-lac-169623344289589 | The Vitality Doctor- Dr Christina Kovalik NMD, LAc, Flagstaff AZ | 2026-11-23 15:35 | 23 / 4.5 | unknown | - | not-in-text | NEEDS-BROWSER |
| P010 | Acupuncture Wellness Center (Cynthia Hull) | yes | https://reviews.birdeye.com/hull-cynthia-acupuncture-wellness-center-168633802417920 | unrecorded | 2026-11-23 13:40 | 5 / 5.0 | none | - | not-in-text | NO-GAP |

**What each read found (no review text):**
- **P009 The Vitality Doctor is the best lead.** It has 23 reviews, all from Google, with a 4.5 average, so at least one is under 5★. Three reviews are 1–2 months old, and no reply text showed under any of the 5 reviews on the page. *Atlas: open the Google profile and find the under-5★ review. Record its stars and age, whether a reply is visible, and the profile's name and city. If it's within 12 months with no reply, mark it ELIGIBLE.*
- **P005 Flagstaff Clinic of Naturopathic Medicine** has 55 reviews averaging 4.6 (35 Google, 16 Facebook, 4 Yellow Pages). The newest one Birdeye showed is about 7 years old. Its directory page said 52 reviews and its own page said 55, so Birdeye's list may be out of date. Low priority: check Google only after P009.
- **P010 Acupuncture Wellness Center: no gap for a trial.** It has 5 Google reviews averaging 5.0, so every one is 5★. It isn't a trial candidate under this rule. It's still a Review Desk prospect, since no reply text showed under any of them.
- **Read 2 (Nov 23, 14:30 UTC): a site search can hand back the wrong business.** So each row now records the name and city the page shows, and the check refuses a gap on a page that isn't the prospect.
  - **P008 Synergistic Healthcare: no gap.** 16 Google reviews averaging 5.0. One 4★ among 16 would average 4.94 and show as 4.9, so all 16 are 5★. No reply text showed under the 5 reviews on the page. Still a Review Desk prospect, not a trial.
  - **P006 Cedar Health Center: wrong page.** The only Birdeye match is "Cedar Health" in **Tucson**, not our Flagstaff clinic. No Flagstaff page found yet.
  - **P007 Munderloh Integrated Medical: wrong page.** The only Birdeye match is **Munderloh Chiropractic**, Flagstaff (197 reviews, 4.8). It shares the surname, but it isn't the same name, so we don't use it. The newest review the cloud saw on it was about 10 years old. *Atlas: on Google, check whether Munderloh Integrated Medical has its own profile.*
  - **P004 Harmonizing Healthcare:** no Birdeye page turned up in a site search. Stays NOT-READ.
- **Read 3 (Nov 23, 15:35 UTC): P009 re-read, two traps for Atlas found.**
  - **Name and city now recorded:** the page shows "The Vitality Doctor- Dr Christina Kovalik NMD, LAc", Flagstaff AZ (Yancey Ln). It passes the name + city match.
  - **Trap 1, a second office.** Birdeye also has a page for the same doctor in **Paradise Valley, AZ** (a search result titled it "25 Reviews"; that page itself was not opened). Atlas must open the **Flagstaff** Google profile; the check marks the Paradise Valley page WRONG-PAGE (self-test "same doctor, other office").
  - **Trap 2, rounded ages.** Per the cloud fetch of the Flagstaff page (Atlas's read of the same page showed no per-review ages, so treat this as unconfirmed), the 5 visible Google reviews are "a month ago" (2), "2 months ago" (1) and "a year ago" (2). Google's "a year ago" can mean up to about 23 months, so a low review with that label can't count as "last 12 months". The check now takes "12-23" for that label and never marks it ELIGIBLE. *Atlas: if the under-5★ review says "a year ago", hover or open it for the date before calling it eligible.*
  - **Still unseen:** the star on each review (the histogram cells were empty in the text the cloud got) and the other 18 reviews. No owner reply showed under the 5 visible ones. The Birdeye profile is unclaimed.
  - **Not a new lead:** Massage Therapy by Bliss (Flagstaff, 15 reviews, 4.9) showed up in the same search. Its newest visible review is about 3 years old, so it can't give a 12-month gap. Not added.
- **Where trials 2–3 stand:** of 7 clinics, P009 is the only live lead. Two have no gap, two returned the wrong page, and two (P004, P005) need Google itself.

**Check:** `python3 review_gap_check.py` → `SUMMARY rows=7 errors=0`. Self-tests: `python3 review_gap_check.py --self-test` (38/38).
