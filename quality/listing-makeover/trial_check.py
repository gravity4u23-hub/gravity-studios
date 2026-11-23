#!/usr/bin/env python3
"""Standing check for Listing Makeover free trials (Quality Gate step 5).

Checks free-trial.md (the message) and trial-listings.md (the free rewrites) before the owner
is asked to OK a send. Hard rules (code, not judgment):

MESSAGE
  1. Route is the shop's own channel, never Etsy Messages (Etsy bars unsolicited sales messages).
  2. '**Route source:**' gives the URL where the shop itself published that channel.
  3. A DM route (Instagram / Facebook / Messenger) carries no email 'Subject:' line.
  4. No price, discount, guarantee, ranking / views / more-sales promise, or "cheaper/faster".
  5. Every quoted line ("> ") is a title copied verbatim from trial-listings.md.
  6. Says the drafts were made with AI help; says no reply is needed; signed Gravity Studios
     with the business line (747) 222-6980; at most 200 words.
  7. Never tells the seller their listings are bad ("weak", "poor", "missing tags", ...).
  8. A route marked UNVERIFIED passes the text rules but prints HOLD (not sendable).
  2b. The route source quotes the shop's own words ("...", 20+ chars), and every such quote is
     verbatim in trial-intake.json "shop" (captured with a date), so the route never rests on
     an uncited quote (Atlas, PR #47).
LISTINGS
  9. Every number in a listing traces to the seller (trial-intake.json facts/title) or to a
     sourced Mohs value; the "(n/140)" counter and the "13 / 20" tag header are exempt.
 10. METAL: "gold" / "silver" outside a [question] must be qualified (plated, filled, tone,
     colored, sterling) - an unqualified metal word is a claim the seller hasn't made
     specifically enough (FTC Jewelry Guides, 16 CFR Part 23).
 11. mohs_check.py passes (FAIL = error; OPEN = printed for Atlas).
 12. With --gs <Gravity-Studio checkout>: listing_lint.py --strict-titles passes.

Usage:  python3 trial_check.py [--gs ../../../gravity-studio]
        python3 trial_check.py --self-test
Exit 0 = everything passes (HOLD is not a failure); 1 = at least one ERROR.
Offline, standard library only. Never sends anything.
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mohs_check  # noqa: E402

PHONE = "(747) 222-6980"
MAX_WORDS = 200
BANNED = [
    (r"\$\s?\d", "names a price; a free trial carries no price"),
    (r"\b(discount|% off|per month|/mo)\b", "pricing language in a free trial"),
    (r"\bcheaper\b|\bfaster than\b", "price/speed comparison"),
    (r"\bguarantee", "guarantee claim"),
    (r"\b(rank|ranking|more sales|more views|boost|page one|first page)\b", "promises results we can't show"),
    (r"\b(weak|poor|bad|missing tags|no tags|wrong)\b", "criticises the seller's listings"),
]
NO_PRESSURE = re.compile(r"no reply needed|no need to reply|no strings", re.I)
AI_LINE = re.compile(r"\bAI\b")
ETSY_ROUTE = re.compile(r"etsy\s*(messages?|conversations?|convo|inbox)", re.I)
DM_ROUTE = re.compile(r"facebook|messenger|instagram|\bDM\b", re.I)
URL = re.compile(r"https?://\S+")
METAL = re.compile(r"\b(gold|silver)\b", re.I)
QUALIFIER = re.compile(r"(plated|filled|tone|colou?red|sterling)", re.I)
NUM = re.compile(r"\d+(?:\.\d+)?")


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


# ---------- message ----------
def parse_trials(text):
    for sec in re.split(r"^## ", text, flags=re.M)[1:]:
        if not sec.startswith("Trial"):
            continue
        name = sec.splitlines()[0].strip()
        route = re.search(r"^\*\*Route:\*\*\s*(.+)$", sec, re.M)
        source = re.search(r"^\*\*Route source:\*\*\s*(.+)$", sec, re.M)
        msg = re.search(r"```message\n(.*?)```", sec, re.S)
        yield name, (route.group(1) if route else ""), (source.group(1) if source else ""), (msg.group(1) if msg else "")


def titles_of(listings_text):
    return {norm(t) for t in re.findall(r"^\*\*Title[^*]*:\*\*\s*(.+)$", listings_text, re.M)}


def check_message(name, route, source, message, titles, shop_lines=None):
    errs = []
    if shop_lines is not None:
        quotes = [q for q in re.findall(r'"([^"]{20,})"', source or "")]
        if not quotes:
            errs.append(f"{name}: route source must quote the shop's own words (\"...\", 20+ chars)")
        for q in quotes:
            if not any(norm(q) in norm(l) for l in shop_lines):
                errs.append(f"{name}: route-source quote not captured in trial-intake.json shop: {q[:50]}")
    if not message.strip():
        return [f"{name}: no ```message block"]
    if not route or ETSY_ROUTE.search(route):
        errs.append(f"{name}: route must be the shop's own channel, not Etsy Messages (got {route!r})")
    if not URL.search(source or ""):
        errs.append(f"{name}: '**Route source:**' must give the URL where the shop published this channel")
    if DM_ROUTE.search(route or "") and re.search(r"^\s*Subject:", message, re.M | re.I):
        errs.append(f"{name}: DM route can't carry an email 'Subject:' line")
    for pat, why in BANNED:
        m = re.search(pat, message, re.I)
        if m:
            errs.append(f"{name}: '{m.group(0)}' - {why}")
    quoted = [norm(l[1:]) for l in message.splitlines() if l.startswith(">")]
    if not quoted:
        errs.append(f"{name}: no quoted title ('> ' lines) - the trial must show the work")
    for q in quoted:
        if q not in titles:
            errs.append(f"{name}: quoted line is not a title from trial-listings.md: {q[:60]}")
    if not AI_LINE.search(message):
        errs.append(f"{name}: say the drafts were made with AI help")
    if PHONE not in message or "Gravity Studios" not in message:
        errs.append(f"{name}: sign-off needs 'Gravity Studios' and {PHONE}")
    if not NO_PRESSURE.search(message):
        errs.append(f"{name}: say plainly that no reply is needed")
    words = len(message.split())
    if words > MAX_WORDS:
        errs.append(f"{name}: {words} words (max {MAX_WORDS})")
    return errs


# ---------- listings ----------
def blocks(listings_text):
    """{name: block} for each '## n. Name' listing."""
    out = {}
    heads = list(re.finditer(r"^##\s+\d+\.\s*(.+)$", listings_text, re.M))
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(listings_text)
        out[h.group(1).strip()] = listings_text[h.start():end]
    return out


def strip_exempt(block):
    block = re.sub(r"^##\s+\d+\.", "##", block, flags=re.M)              # heading number
    block = re.sub(r"\*\*Title\s*\(\d+/\d+\)", "**Title", block)          # (n/140) counter
    block = re.sub(r"\*\*Tags\s*\(13,\s*≤20 chars\)", "**Tags", block)    # tag header
    return block


def check_listing(name, block, intake, sourced):
    errs = []
    if intake is None:
        return [f"{name}: no entry in trial-intake.json - every rewrite needs the seller's facts"]
    seller = " ".join([intake.get("title", "")] + intake.get("facts", []) + intake.get("highlights", []))
    allowed = set(NUM.findall(seller)) | set(sourced)
    for n in NUM.findall(strip_exempt(block)):
        if n not in allowed:
            errs.append(f"{name}: number {n} is not in the seller's text or a sourced Mohs value")
    outside = re.sub(r"\[[^\]]*\]", "", block)
    for line in outside.splitlines():
        for m in METAL.finditer(line):
            window = line[max(0, m.start() - 12): m.end() + 12]
            if not QUALIFIER.search(window):
                errs.append(f"{name}: unqualified metal word '{m.group(0)}' outside a [question]: {norm(line)[:70]}")
    return errs


def run(gs_root=None):
    errors = 0
    lt = open(os.path.join(HERE, "trial-listings.md"), encoding="utf-8").read()
    intake = json.load(open(os.path.join(HERE, "trial-intake.json"), encoding="utf-8"))
    sourced = {v for k, v in intake.get("sourced_numbers", {}).items() if not k.startswith("_")}
    for name, block in blocks(lt).items():
        errs = check_listing(name, block, intake["listings"].get(name), sourced)
        for e in errs:
            print("ERROR", e)
        errors += len(errs)
        if not errs:
            print(f"OK   listing: {name}")
    fails, opens, seen = mohs_check.check_text(lt)
    for f in fails:
        print("ERROR mohs:", f)
    for o in opens:
        print("OPEN  mohs:", o)
    errors += len(fails)
    if gs_root:
        lint = os.path.join(gs_root, "portfolio", "listing-makeover", "listing_lint.py")
        if not os.path.exists(lint):
            print(f"ERROR listing_lint.py not found under {gs_root}")
            errors += 1
        else:
            r = subprocess.run([sys.executable, lint, os.path.join(HERE, "trial-listings.md"), "--strict-titles"],
                               capture_output=True, text=True)
            print("lint:", (r.stdout.strip().splitlines() or ["(no output)"])[-1])
            if r.returncode:
                print(r.stdout)
                errors += 1
    else:
        print("NOTE  listing_lint not run (pass --gs <Gravity-Studio checkout>)")
    titles = titles_of(lt)
    trials = list(parse_trials(open(os.path.join(HERE, "free-trial.md"), encoding="utf-8").read()))
    if not trials:
        print("ERROR no '## Trial' sections in free-trial.md")
        errors += 1
    held = 0
    for name, route, source, msg in trials:
        shop_lines = [str(v) for k, v in intake.get("shop", {}).items() if k.startswith("about")]
        errs = check_message(name, route, source, msg, titles, shop_lines)
        for e in errs:
            print("ERROR", e)
        errors += len(errs)
        if not errs:
            if route.upper().startswith("UNVERIFIED"):
                held += 1
                print(f"HOLD {name} ({len(msg.split())} words): text passes, route unverified - not sendable yet")
            else:
                print(f"OK   {name} ({len(msg.split())} words)")
    print(f"{errors} errors; {held} trial(s) on HOLD for an unverified route")
    return 1 if errors else 0


def self_test():
    titles = {norm("Amethyst Chunk Necklace — Wire Wrapped Crystal Pendant on Black Cord, 17-19 in")}
    good = ("Hi! I rewrote two listings, drafted with AI help.\n"
            "> Amethyst Chunk Necklace — Wire Wrapped Crystal Pendant on Black Cord, 17-19 in\n"
            "No reply needed.\nDavid — Gravity Studios\n(747) 222-6980\n")
    ig, src = "UNVERIFIED: Instagram @shop", "https://www.etsy.com/shop/X (About: IG @shop)"
    mcases = [
        ("good message passes", ig, src, good, 0),
        ("Etsy Messages route fails", "Etsy Messages", src, good, 1),
        ("missing route source fails", ig, "", good, 1),
        ("Subject: on an Instagram DM fails", ig, src, "Subject: hi\n" + good, 1),
        ("price fails", ig, src, good + "Then $79.\n", 1),
        ("ranking promise fails", ig, src, good + "You'll rank higher.\n", 1),
        ("criticism fails", ig, src, good + "Your titles are weak.\n", 1),
        ("edited title fails", ig, src, good.replace("Black Cord", "Cord"), 1),
        ("no quoted title fails", ig, src, "Hi, AI help.\nNo reply needed.\nGravity Studios (747) 222-6980\n", 1),
        ("no AI line fails", ig, src, good.replace("drafted with AI help", "drafted by me"), 1),
        ("no phone fails", ig, src, good.replace(PHONE, ""), 1),
        ("pressure fails", ig, src, good.replace("No reply needed.\n", ""), 1),
        ("too long fails", ig, src, good + "word " * 210, 1),
    ]
    shop = ["I would love to see pictures of your plants! IG @shop.name"]
    qsrc = 'https://www.etsy.com/shop/X (About: "I would love to see pictures of your plants! IG @shop.name")'
    qcases = [
        ("route-source quote captured in intake passes", qsrc, 0),
        ("route-source quote not in intake fails", qsrc.replace("plants", "crystals"), 1),
        ("route source with no quote fails", src, 1),
    ]
    intake = {"title": "Amethyst Necklace/ Gold Wire Wrap/ BlackCord17-19in",
              "facts": ["Black Cord 17 inch plus 2 inch extension chain (total of 19 inches)"]}
    blk = ("## 1. A\n**Title (10/140):** Amethyst Necklace\n**Length:** 17 inches plus 2 (19 total). "
           "[Wire: gold-filled or gold-colored? confirm]\n- **Amethyst** — *Proven:* Mohs 7.\n"
           "**Tags (13, ≤20 chars):** a · b\n")
    lcases = [
        ("traced listing passes", blk, intake, 0),
        ("invented number fails", blk + "Pendant is 2.5 cm.\n", intake, 1),
        ("unqualified 'gold' fails", blk + "Wrapped in gold wire.\n", intake, 1),
        ("'gold-filled' outside brackets passes", blk + "Wrapped in gold-filled wire.\n", intake, 0),
        ("'silver-plated chain' passes", blk + "Silver-plated chain.\n", intake, 0),
        ("no intake entry fails", blk, None, 1),
    ]
    passed = total = 0
    for label, r, s, m, want in mcases:
        got = 1 if check_message("t", r, s, m, titles) else 0
        total += 1
        passed += got == want
        print(("PASS " if got == want else "FAIL ") + label)
    for label, s_, want in qcases:
        got = 1 if check_message("t", ig, s_, good, titles, shop) else 0
        total += 1
        passed += got == want
        print(("PASS " if got == want else "FAIL ") + label)
    for label, b, it, want in lcases:
        got = 1 if check_listing("t", b, it, {"7"}) else 0
        total += 1
        passed += got == want
        print(("PASS " if got == want else "FAIL ") + label)
    print(f"self-tests {passed}/{total}")
    return 0 if passed == total else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    gs = None
    if "--gs" in sys.argv:
        gs = sys.argv[sys.argv.index("--gs") + 1]
    sys.exit(run(gs))
