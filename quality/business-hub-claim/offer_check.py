#!/usr/bin/env python3
"""Checks Business Hub Claim offer text against the facts in benchmark.md.

Fails (exit 1) if the offer:
  - doesn't say claiming is free,
  - promises placement, recommendations, ranking or more customers from ChatGPT,
  - asks for the buyer's password, login, codes or ID,
  - ties the price to a review or introductions (owner dropped this on tap 17),
  - leaves out the owner-verifies line or the can't-unpublish warning.
Usage: offer_check.py FILE   |   offer_check.py --self-test
"""
import re, sys

REQUIRED = [
    ("free to claim", r"\bfree\b[^.]{0,40}\bclaim|\bclaim\w*[^.]{0,40}\bfree\b"),
    ("you verify it yourself", r"\byou\b[^.]{0,40}\bverif"),
    ("no placement promise", r"(doesn'?t|does not|won'?t|will not|can'?t|cannot)\s+(guarantee|change|improve)[^.]{0,40}(placement|recommend|rank|visib)"),
    ("can't-unpublish warning", r"(can'?t|cannot)\s+(be\s+)?(un-?publish|delet|tak\w*\s+down|remov)"),
]
BANNED = [
    ("placement promise", r"\b(rank(ed|s)?\s*(#?1|higher|first)|top of chatgpt|get (you )?recommended|recommended more|more (customers|calls|sales) from chatgpt|boost\w* (your )?(visibility|ranking|placement)|guaranteed?\b(?![^.]{0,5}(higher )?placement or sales))"),
    ("asks for credentials or ID", r"\b(send|share|give|text|email)\b[^.]{0,30}\b(password|login|log-in|code|codes|id photo|photo of your id|selfie|driver'?s licen[cs]e)\b"),
    ("review or introductions as a condition", r"\b(google review|leave (us )?a review|review us|introduc\w+)\b"),
]

def check(text):
    errs = []
    low = text.lower().replace("’", "'")
    for name, pat in REQUIRED:
        if not re.search(pat, low):
            errs.append("missing: " + name)
    for name, pat in BANNED:
        m = re.search(pat, low)
        if m:
            errs.append("banned (%s): %r" % (name, m.group(0)))
    return errs

GOOD = ("Claiming your business in ChatGPT is free, and you can do it yourself. "
        "For $49 we write your profile details from your own website, check your DNS record format, "
        "and show you what ChatGPT says about you before and after. You verify it yourself with your "
        "own phone, email and ID; we never ask for your logins or codes. OpenAI says claiming doesn't "
        "guarantee higher placement or sales. Once published, a profile can't be unpublished, so we get "
        "the details right first.")

BAD = {
    "hides free": GOOD.replace("Claiming your business in ChatGPT is free, and you can do it yourself. ", ""),
    "placement promise": GOOD + " Get recommended more by ChatGPT.",
    "rank higher": GOOD + " You'll rank higher in ChatGPT.",
    "asks for code": GOOD + " Just text us the code OpenAI sends you.",
    "asks for password": GOOD + " Share your password and we'll handle it.",
    "review condition": GOOD + " The $49 price is for buyers who leave a Google review.",
    "no unpublish warning": GOOD.replace(" Once published, a profile can't be unpublished, so we get the details right first.", ""),
}

def self_test():
    ok = 0
    total = 1 + len(BAD) + 1
    e = check(GOOD)
    if not e: ok += 1
    else: print("FAIL gold:", e)
    for name, t in BAD.items():
        if check(t): ok += 1
        else: print("FAIL not caught:", name)
    # curly apostrophes must not hide a required line
    if not check(GOOD.replace("'", "’")): ok += 1
    else: print("FAIL curly apostrophes")
    print("self-tests %d/%d" % (ok, total))
    return ok == total

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        sys.exit(0 if self_test() else 1)
    if len(sys.argv) != 2:
        print(__doc__); sys.exit(2)
    errs = check(open(sys.argv[1], encoding="utf-8").read())
    for x in errs: print(x)
    print("%d errors" % len(errs))
    sys.exit(1 if errs else 0)
