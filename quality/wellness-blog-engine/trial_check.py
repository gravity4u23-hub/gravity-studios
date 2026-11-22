#!/usr/bin/env python3
"""Standing check for Wellness Blog Engine free-trial messages (Quality Gate step 5).

Every trial message in free-trial.md must pass before the owner is asked to OK a send.
Built from review-reply-desk/trial_check.py, with the rules a health-adjacent post needs.
Hard rules (code, not judgment):
  1. Route is the business's own channel, never Etsy Messages, and '**Route source:**' gives the
     URL where the business itself published it.
  2. No price, discount, "cheaper / faster / guarantee / rank / traffic / more sales" claims.
  3. No health-claim verbs in the pitch (cure, heal, treat, reverse, prevent, detox, boost immunity).
     The post carries its own sourced, labelled wording; the pitch claims nothing.
  4. Every quoted line ("> ") is copied verbatim from the gold sample post, and the 'Title:' line
     is one of the post's headline options, so the trial only shows text Atlas has scored.
  5. Says the post was drafted with AI help (benchmark complaint #1: AI text sold as a writer's).
  6. No jab at the buyer's blog ("since 2020", "dormant", "haven't posted", "outdated"...):
     we only saw 3 posts, so we can't state how often they publish, and it's rude.
  7. Signed "Gravity Studios" with (747) 222-6980; says plainly no reply is needed; <= 220 words
     (fits a contact-form comment box); no '[' placeholder left in the text.
  8. A route marked UNVERIFIED passes the text rules but prints HOLD (not sendable).

Usage:  python3 trial_check.py [free-trial.md] [gold-sample-002-winter-sun.md]
        python3 trial_check.py --self-test
Exit 0 = every message passes; 1 = at least one ERROR. Offline, standard library only.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PHONE = "(747) 222-6980"
MAX_WORDS = 220
BANNED = [
    (r"\$\s?\d", "names a price; a free trial carries no price"),
    (r"\b(discount|% off|per month|/mo)\b", "pricing language in a free trial"),
    (r"\bcheaper\b|\bfaster than\b", "price/speed comparison"),
    (r"\bguarantee", "guarantee claim"),
    (r"\b(rank|ranking|traffic|more sales|more customers|boost your)\b", "promises results we can't show"),
    (r"\b(cures?|cured|heals?|healing|treats?|treatment|reverses?|prevents?|detox\w*|boosts? immun\w*)\b",
     "health-claim word in the pitch (the post carries its own sourced wording)"),
    (r"\bsince (19|20)\d\d\b|\bdormant\b|\bhaven'?t (posted|written|updated)\b|\boutdated\b|\binactive\b|\bneglected\b|\bstale\b",
     "comments on how often they blog (we saw 3 posts only; don't judge their blog)"),
]
NO_PRESSURE = re.compile(r"no reply needed|no need to reply|no strings", re.I)
AI_DISCLOSED = re.compile(r"\bAI\b")
ETSY_ROUTE = re.compile(r"etsy\s*(messages?|conversations?|convo|inbox)", re.I)
URL = re.compile(r"https?://\S+")


def norm(s):
    s = s.replace("“", '"').replace("”", '"').replace("’", "'").replace("‘", "'")
    return re.sub(r"\s+", " ", s.replace("**", "").replace("*", "")).strip()


def post_text(text):
    return norm(text)


def headlines(text):
    """Headline options: '1. **Title**' lines under '## Headline options'."""
    m = re.search(r"^## Headline options.*?$(.*?)^\*\*Meta", text, re.S | re.M)
    block = m.group(1) if m else ""
    return {norm(h) for h in re.findall(r"^\d+\.\s*\*\*(.+?)\*\*\s*$", block, re.M)}


def parse_trials(text):
    """Yield (name, route, source, message) for each '## Trial' section."""
    for sec in re.split(r"^## ", text, flags=re.M)[1:]:
        if not sec.startswith("Trial"):
            continue
        name = sec.splitlines()[0].strip()
        route = re.search(r"^\*\*Route:\*\*\s*(.+)$", sec, re.M)
        source = re.search(r"^\*\*Route source:\*\*\s*(.+)$", sec, re.M)
        msg = re.search(r"```message\n(.*?)```", sec, re.S)
        yield name, (route.group(1) if route else ""), (source.group(1) if source else ""), (msg.group(1) if msg else "")


def check(name, route, message, post, heads, source=""):
    errs = []
    if not message.strip():
        return [f"{name}: no ```message block"]
    if not route or ETSY_ROUTE.search(route):
        errs.append(f"{name}: route must be the business's own site/email/form, not Etsy Messages (got {route!r})")
    if not URL.search(source or ""):
        errs.append(f"{name}: '**Route source:**' must give the URL where the business published this channel")
    for pat, why in BANNED:
        m = re.search(pat, message, re.I)
        if m:
            errs.append(f"{name}: '{m.group(0)}' - {why}")
    quoted = [norm(l[1:]) for l in message.splitlines() if l.startswith(">")]
    if not quoted:
        errs.append(f"{name}: no quoted line ('> ') - the trial must show the work")
    for q in quoted:
        if q not in post:
            errs.append(f"{name}: quoted line is not verbatim from the gold sample post: {q[:60]}...")
    t = re.search(r"^Title:\s*(.+)$", message, re.M)
    if not t:
        errs.append(f"{name}: needs a 'Title:' line naming the post")
    elif norm(t.group(1)) not in heads:
        errs.append(f"{name}: 'Title:' is not one of the post's headline options: {t.group(1)[:60]}")
    if not AI_DISCLOSED.search(message):
        errs.append(f"{name}: say the post was drafted with AI help (benchmark complaint #1)")
    if PHONE not in message or "Gravity Studios" not in message:
        errs.append(f"{name}: sign-off needs 'Gravity Studios' and {PHONE}")
    if not NO_PRESSURE.search(message):
        errs.append(f"{name}: say plainly that no reply is needed")
    if "[" in message:
        errs.append(f"{name}: a '[' placeholder is left in the message")
    words = len(message.split())
    if words > MAX_WORDS:
        errs.append(f"{name}: {words} words (max {MAX_WORDS}, a contact-form comment box)")
    return errs


def run(trial_path, post_path):
    raw = open(post_path, encoding="utf-8").read()
    post, heads = post_text(raw), headlines(raw)
    if not heads:
        print(f"ERROR: no headline options found in {post_path}")
        return 1
    trials = list(parse_trials(open(trial_path, encoding="utf-8").read()))
    if not trials:
        print("ERROR: no '## Trial' sections found")
        return 1
    bad = held = 0
    for name, route, source, msg in trials:
        errs = check(name, route, msg, post, heads, source)
        if errs:
            bad += 1
            for e in errs:
                print("ERROR", e)
        elif route.upper().startswith("UNVERIFIED"):
            held += 1
            print(f"HOLD {name} ({len(msg.split())} words): text passes, route unverified - not sendable yet")
        else:
            print(f"OK   {name} ({len(msg.split())} words): text passes; still needs step 4 'Yes' + owner OK on this text")
    print(f"{len(trials) - bad}/{len(trials)} trial messages pass the text rules; {held} on HOLD for an unverified route")
    return 1 if bad else 0


def self_test():
    post = norm("## Headline options\n1. **Root, Honestly**\n**Meta title:** x\n"
                "A spoonful of root powder in warm milk is the traditional food form, not the studied dose.")
    heads = {"Root, Honestly"}
    good = ("Hello Phyllis,\nI wrote a free post for your journal, drafted with AI help.\nTitle: Root, Honestly\n"
            "> A spoonful of root powder in warm milk is the traditional food form, not the studied dose.\n"
            "No reply needed.\nDavid, Gravity Studios, (747) 222-6980\n")
    route, src = "Contact form on the shop's own website", "https://www.example.com/pages/contact"
    cases = [
        ("good message passes", route, good, src, 0),
        ("Etsy Messages route fails", "Etsy Messages", good, src, 1),
        ("missing route fails", "", good, src, 1),
        ("missing route source fails", route, good, "", 1),
        ("route source without a URL fails", route, good, "found it on Google", 1),
        ("UNVERIFIED route passes text (HOLD)", "UNVERIFIED: email", good, src, 0),
        ("price fails", route, good + "Then $150 a month.\n", src, 1),
        ("guarantee fails", route, good + "Guaranteed reads.\n", src, 1),
        ("traffic promise fails", route, good + "It will bring traffic.\n", src, 1),
        ("'cures' in pitch fails", route, good + "Ashwagandha cures stress.\n", src, 1),
        ("'healing' in pitch fails", route, good + "A healing herb.\n", src, 1),
        ("'boosts immunity' fails", route, good + "It boosts immunity.\n", src, 1),
        ("'since 2020' blog jab fails", route, good + "Your journal is quiet since 2020.\n", src, 1),
        ("'haven't posted' jab fails", route, good + "You haven't posted in years.\n", src, 1),
        ("edited quote fails", route, good.replace("traditional food form", "best form"), src, 1),
        ("no quoted line fails", route, "\n".join(l for l in good.splitlines() if not l.startswith(">")), src, 1),
        ("missing Title fails", route, good.replace("Title: Root, Honestly\n", ""), src, 1),
        ("Title not a headline option fails", route, good.replace("Root, Honestly", "Root Miracle"), src, 1),
        ("no AI disclosure fails", route, good.replace(", drafted with AI help", ""), src, 1),
        ("missing phone fails", route, good.replace(PHONE, ""), src, 1),
        ("pressure (no 'no reply needed') fails", route, good.replace("No reply needed.\n", ""), src, 1),
        ("placeholder left fails", route, good + "Reply to [your email].\n", src, 1),
        ("too long fails", route, good + ("word " * 230), src, 1),
        ("empty message fails", route, "", src, 1),
    ]
    passed = 0
    for label, r, m, s, want in cases:
        got = 1 if check("t", r, m, post, heads, s) else 0
        ok = got == want
        passed += ok
        print(("PASS " if ok else "FAIL ") + label)
    print(f"{passed}/{len(cases)} self-tests pass")
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    trial = args[0] if args else os.path.join(HERE, "free-trial.md")
    postp = args[1] if len(args) > 1 else os.path.join(HERE, "gold-sample-002-winter-sun.md")
    sys.exit(run(trial, postp))
