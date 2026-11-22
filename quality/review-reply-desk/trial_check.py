#!/usr/bin/env python3
"""Standing check for Review Reply Desk free-trial messages (Quality Gate step 5).

Every trial message in free-trial.md must pass before the owner is asked to OK a send.
Hard rules (code, not judgment):
  1. Route is the shop's own channel: never Etsy Messages / Etsy conversations.
  2. No price, no discount, no "cheaper / faster / guarantee / rank / more sales" claims.
  3. Never sells "no replies on your reviews" as the gap (Atlas, PR #9 review).
  4. Every quoted reply ("> " line) is copied verbatim from gold-sample-replies.md,
     so the trial only sends text Atlas has verified.
  5. Signed "Gravity Studios" with the business line (747) 222-6980 (OWNER_STEERING Nov 21).
  6. A route marked UNVERIFIED passes the text rules but prints HOLD (not sendable).
  7. Says plainly that no reply is needed (no pressure), and stays under 320 words.

Usage:  python3 trial_check.py [free-trial.md] [gold-sample-replies.md]
        python3 trial_check.py --self-test
Exit 0 = every message passes; 1 = at least one ERROR.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PHONE = "(747) 222-6980"
MAX_WORDS = 320
BANNED = [
    (r"\$\s?\d", "names a price; a free trial carries no price"),
    (r"\b(discount|% off|per month|/mo)\b", "pricing language in a free trial"),
    (r"\bcheaper\b|\bfaster than\b", "speed/price comparison (pitch rule: never vs software)"),
    (r"\bguarantee", "guarantee claim"),
    (r"\b(rank|ranking|more sales|boost your)\b", "promises results we can't show"),
    (r"\bunanswered\b|\b(no|without)( a| any)? (reply|replies|response|responses)\b(?! needed)",
     "sells missing replies as the gap (Atlas PR #9: not a gap for 5-star reviews)"),
]
NO_PRESSURE = re.compile(r"no reply needed|no need to reply|no strings", re.I)
ETSY_ROUTE = re.compile(r"etsy\s*(messages?|conversations?|convo|inbox)", re.I)


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def gold_replies(text):
    """All '**Reply:** ...' texts from gold-sample-replies.md, normalized."""
    return {norm(m) for m in re.findall(r"\*\*Reply:\*\*\s*(.+)", text)}


def parse_trials(text):
    """Yield (name, route, message) for each '## Trial' section."""
    for sec in re.split(r"^## ", text, flags=re.M)[1:]:
        if not sec.startswith("Trial"):
            continue
        name = sec.splitlines()[0].strip()
        route = re.search(r"^\*\*Route:\*\*\s*(.+)$", sec, re.M)
        msg = re.search(r"```message\n(.*?)```", sec, re.S)
        yield name, (route.group(1) if route else ""), (msg.group(1) if msg else "")


def check(name, route, message, gold):
    errs = []
    if not message.strip():
        return [f"{name}: no ```message block"]
    if not route or ETSY_ROUTE.search(route):
        errs.append(f"{name}: route must be the shop's own site/email/Instagram, not Etsy Messages (got {route!r})")
    for pat, why in BANNED:
        m = re.search(pat, message, re.I)
        if m:
            errs.append(f"{name}: '{m.group(0)}' - {why}")
    quoted = [norm(l[1:]) for l in message.splitlines() if l.startswith(">")]
    if not quoted:
        errs.append(f"{name}: no quoted reply ('> ' lines) - the trial must show the work")
    for q in quoted:
        if q not in gold:
            errs.append(f"{name}: quoted reply is not verbatim from gold-sample-replies.md: {q[:60]}...")
    if PHONE not in message or "Gravity Studios" not in message:
        errs.append(f"{name}: sign-off needs 'Gravity Studios' and {PHONE}")
    if not NO_PRESSURE.search(message):
        errs.append(f"{name}: say plainly that no reply is needed")
    words = len(message.split())
    if words > MAX_WORDS:
        errs.append(f"{name}: {words} words (max {MAX_WORDS})")
    return errs


def run(trial_path, gold_path):
    gold = gold_replies(open(gold_path, encoding="utf-8").read())
    trials = list(parse_trials(open(trial_path, encoding="utf-8").read()))
    if not trials:
        print("ERROR: no '## Trial' sections found")
        return 1
    bad = held = 0
    for name, route, msg in trials:
        errs = check(name, route, msg, gold)
        if errs:
            bad += 1
            for e in errs:
                print("ERROR", e)
        elif route.upper().startswith("UNVERIFIED"):
            held += 1
            print(f"HOLD {name} ({len(msg.split())} words): text passes, route unverified - not sendable yet")
        else:
            print(f"OK   {name} ({len(msg.split())} words)")
    print(f"{len(trials) - bad}/{len(trials)} trial messages pass the text rules; {held} on HOLD for an unverified route")
    return 1 if bad else 0


def self_test():
    gold = {norm("Thank you, Dana! Enjoy every bar. — Margaret, SweetSoftSkin")}
    good = ("Hi Margaret,\nHere is a free reply.\n> Thank you, Dana! Enjoy every bar. — Margaret, SweetSoftSkin\n"
            "No reply needed.\nDavid — Gravity Studios · (747) 222-6980\n")
    route = "Shop's own website contact form"
    cases = [
        ("good message passes", route, good, 0),
        ("Etsy Messages route fails", "Etsy Messages", good, 1),
        ("missing route fails", "", good, 1),
        ("price fails", route, good + "Then $79 a month.\n", 1),
        ("cheaper claim fails", route, good + "Cheaper than an agency.\n", 1),
        ("guarantee fails", route, good + "Guaranteed results.\n", 1),
        ("'unanswered' gap fails", route, good + "You have 7 unanswered reviews.\n", 1),
        ("'without a reply' gap fails", route, good + "Reviews without a reply hurt.\n", 1),
        ("edited reply fails", route, good.replace("Enjoy every bar", "Enjoy them all"), 1),
        ("no quoted reply fails", route, "Hi.\nNo reply needed.\nGravity Studios (747) 222-6980\n", 1),
        ("missing phone fails", route, good.replace(PHONE, ""), 1),
        ("pressure (no 'no reply needed') fails", route, good.replace("No reply needed.\n", ""), 1),
        ("too long fails", route, good + ("word " * 330), 1),
        ("empty message fails", route, "", 1),
    ]
    passed = 0
    for label, r, m, want_errs in cases:
        got = 1 if check("t", r, m, gold) else 0
        ok = got == want_errs
        passed += ok
        print(("PASS " if ok else "FAIL ") + label)
    print(f"{passed}/{len(cases)} self-tests pass")
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    trial = args[0] if args else os.path.join(HERE, "free-trial.md")
    goldp = args[1] if len(args) > 1 else os.path.join(HERE, "gold-sample-replies.md")
    sys.exit(run(trial, goldp))
