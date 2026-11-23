# Resume + LinkedIn — Free trial pack (Quality Gate step 5, prepared)

**Status (2026-11-23, 07:25 UTC hourly run):** prepared, **not sent**. Step 5 opens only after step 4 (owner read, tap 21 / issue #43) is "Yes". Each send needs its own owner OK on the exact text below. **Nobody has been contacted, and no person has been chosen.**

Check: `python3 trial_check.py` (this folder). Every trial prints **HOLD** until the owner has picked the person. Self-tests: `python3 trial_check.py --self-test`.

## How this trial differs from the other three
The Review Desk, Listing and Wellness trials go to a **business** we can name in public. A resume trial goes to a **private person**, and their resume holds their name, phone, employers and dates. So:
- **This public repo never holds a trial person's name or files.** The results log uses "Person A/B/C" only. `trial_check.py` fails this folder if it finds an email address, a phone number other than the business line, or a name in the log.
- **Their files live in the private Gravity-Studio repo** under `clients/resume/<person-letter>/` (or the owner's Google Drive if he prefers), and are deleted 30 days after delivery unless they ask us to keep them.
- **We don't go looking for strangers.** The owner picks up to 3 people he already knows who are job-hunting now (family, friends, people from church or work), and sends the message himself. No cold outreach, no job-board scraping, no posts in groups.

## Trial message (owner sends; text, Messenger or WhatsApp)
**Route:** UNVERIFIED: no person chosen. The owner picks someone he knows who is job-hunting and sends this from his own phone or account.
**Day-of checks before the owner taps:** (1) the person is applying for jobs now; (2) the owner has the job post they want most, or they'll send it; (3) owner OKs this exact text.

```message
Hi [first name],

I'm testing a new service at Gravity Studios: we rewrite resumes and LinkedIn profiles for one job you want. I'd like to do yours for free.

How it works: you send your current resume and the link to the job. I'll ask you 6 short questions about what you really do at work. We write it with AI help, and every line comes from your resume or your answers. Nothing made up, no fake numbers.

Your resume stays private. It isn't posted or shared, and we delete it 30 days after you get yours back.

You'd get a Word file, a PDF, and a LinkedIn headline and About section. No reply needed if the timing's wrong.

David — Gravity Studios
(747) 222-6980
```

## Intake (after they say yes)
Ask these in the same thread. Their answers go in `buyer-answers.txt` in the private folder, word for word.
1. Can you send your current resume (Word, PDF or a photo is fine)?
2. What is the link to the job you want most?
3. Is it OK if we keep your files for 30 days and then delete them?
4. Then the 6 role questions, written for their resume the way `gold-sample/buyer-answers.txt` was: one question for each vague line ("What did you train them on?"), and one asking for any numbers they know. If they don't know a number, we don't add one.

## Delivery (Claude builds, owner sends)
In the private folder `clients/resume/<letter>/`, with the same file names as `gold-sample/`:
```
python3 render_resume.py rewrite.txt rewrite.docx        # then the PDF the same way as the gold sample
python3 resume_lint.py original.txt rewrite.txt linkedin.txt
python3 trace_check.py --dir clients/resume/<letter>      # 0 NEW words, with this person's own reword_allowlist.json
python3 file_check.py                                     # Word/PDF match the text, 1 page, no tables
```
`trace_check.py --dir` needs the order's **own** `reword_allowlist.json`: every reworded word cites *this* person's answer. The gold sample's reasons cite the synthetic buyer, so they never carry over (self-tested).

**Delivery note** (owner sends with the files):
```delivery
Here's your resume (Word and PDF) and your LinkedIn headline and About section.

Every line comes from your resume or your answers. We didn't add anything you didn't tell us. If anything is wrong or sounds unlike you, tell me and I'll fix it free.

If your manager can give you real numbers (sales, sign-ups, how many people you trained), send them and we'll add them free.

Your files get deleted in 30 days unless you ask us to keep them.

David — Gravity Studios
```

**What we ask afterwards (once, a week later):** "Did you use it to apply anywhere?" We log the answer as given and nothing more. We never ask whether they got the job as a selling point, and we never quote them without written OK.

## Results log (fill only with what actually happened; never a real name)
| Trial | Sent (date, by owner) | What they did (used / thanks / ignored / complained) | Notes |
|---|---|---|---|
| Person A | — | — | not chosen |
| Person B | — | — | not chosen |
| Person C | — | — | not chosen |
