#!/usr/bin/env python3
"""Standing check for Resume + LinkedIn free trials (Quality Gate step 5).

A resume trial goes to a private person, not a business, so on top of the usual message
rules this check guards the PUBLIC repo against that person's data. Hard rules (code):

MESSAGE (```message block in free-trial.md)
  1. No price, discount, guarantee, or job / interview / "ATS score" promise.
  2. Says it is written with AI help; promises nothing invented (matches trace_check.py);
     says the resume stays private and when it is deleted; says no reply is needed.
  3. Signed Gravity Studios with the business line (747) 222-6980; at most 150 words.
  4. Only the [first name] placeholder; no real name is filled in.
DELIVERY (```delivery block)
  5. Says nothing was added; offers free fixes; offers to add real numbers free; says when
     files are deleted. No price, no promise.
PUBLIC-REPO PRIVACY (every text file in this folder and gold-sample/)
  6. No email address and no phone number except the business line (555-0100..0199,
     reserved for fiction, is allowed in synthetic eval data).
  7. Results log rows are "Person A/B/C" only.
ROUTE
  8. A route marked UNVERIFIED (no person chosen yet) passes but prints HOLD.
  9. The delivery steps run trace_check.py --dir (the order's own allowlist).

Usage:  python3 trial_check.py            python3 trial_check.py --self-test
Exit 0 = everything passes (HOLD is not a failure); 1 = at least one ERROR.
Offline, standard library only. Never sends anything.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.join(HERE, "free-trial.md")
PHONE = "(747) 222-6980"
MAX_WORDS = 150

BANNED = [
    (r"\$\s?\d", "names a price; a free trial carries no price"),
    (r"\b(discount|% off|per month|/mo)\b", "pricing language in a free trial"),
    (r"\bguarantee", "guarantee claim"),
    (r"\b(get|land|win)\s+(you\s+)?(the|a|more)?\s*(job|interviews?|hired|offers?)\b", "promises a job or interviews"),
    (r"\b(more|double|triple)\s+interviews\b", "promises interviews"),
    (r"\bATS[- ](score|proof|approved|guaranteed)|beat the ATS\b", "promises an ATS result we can't show"),
]
MESSAGE_NEEDS = [
    (r"\bAI\b", "says it is written with AI help"),
    (r"nothing (made up|invented)|no fake numbers", "promises nothing invented"),
    (r"private|isn't (posted|shared)", "says the resume stays private"),
    (r"delete", "says when files are deleted"),
    (r"no reply needed|no need to reply", "says no reply is needed"),
]
DELIVERY_NEEDS = [
    (r"didn't add anything|nothing (added|made up)", "says nothing was added"),
    (r"fix it free|fix(ed)? (it )?for free", "offers free fixes"),
    (r"numbers.*add them free", "offers to add real numbers free"),
    (r"delete", "says when files are deleted"),
]
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
PHONE_RX = re.compile(r"\(?\b\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}\b")
LOG_ROW = re.compile(r"^\|\s*(?!\s|Trial\b|-)([^|]+?)\s*\|", re.M)
# 555-0100..0199 is reserved for fiction (NANP), so synthetic eval data may use it.
FICTIONAL = re.compile(r"555[\s.-]01\d\d$")
PERSON = re.compile(r"^Person [ABC]$")


def block(text, tag):
    m = re.search(r"```" + tag + r"\n(.*?)```", text, re.S)
    return m.group(1) if m else None


def check_pack(text):
    """Return (errors, holds) for the pack text."""
    errs, holds = [], []
    msg = block(text, "message")
    if msg is None:
        return ["no ```message block"], holds
    for rx, why in BANNED:
        if re.search(rx, msg, re.I):
            errs.append(f"message: {why}")
    for rx, why in MESSAGE_NEEDS:
        if not re.search(rx, msg, re.I):
            errs.append(f"message: must say it {why.split('says ', 1)[-1]}" if why.startswith("says")
                        else f"message: missing - {why}")
    if PHONE not in msg or "Gravity Studios" not in msg:
        errs.append("message: not signed Gravity Studios with the business line")
    words = len(msg.split())
    if words > MAX_WORDS:
        errs.append(f"message: {words} words (max {MAX_WORDS})")
    first = msg.strip().splitlines()[0] if msg.strip() else ""
    if not re.match(r"^Hi \[first name\],$", first):
        errs.append(f"message: greeting must keep the [first name] placeholder in the public repo (got '{first}')")

    dlv = block(text, "delivery")
    if dlv is None:
        errs.append("no ```delivery block")
    else:
        for rx, why in BANNED:
            if re.search(rx, dlv, re.I):
                errs.append(f"delivery: {why}")
        for rx, why in DELIVERY_NEEDS:
            if not re.search(rx, dlv, re.I | re.S):
                errs.append(f"delivery: must {why.replace('says', 'say').replace('offers', 'offer')}")

    if "trace_check.py --dir" not in text:
        errs.append("delivery steps don't run trace_check.py --dir (the order's own allowlist)")

    log = text.split("## Results log", 1)
    if len(log) < 2:
        errs.append("no '## Results log' section")
    else:
        rows = [r.strip() for r in LOG_ROW.findall(log[1])]
        if not rows:
            errs.append("results log has no rows")
        for r in rows:
            if not PERSON.match(r):
                errs.append(f"results log row '{r}' must be 'Person A/B/C' (no real names in a public repo)")

    route = re.search(r"\*\*Route:\*\*\s*(.+)", text)
    if not route:
        errs.append("no **Route:** line")
    elif route.group(1).startswith("UNVERIFIED"):
        holds.append("HOLD trial: no person chosen yet (owner picks someone he knows; tap 21 first)")
    return errs, holds


def privacy_scan(folder):
    """Every text file here and in gold-sample/: no email, no phone but the business line."""
    errs = []
    for sub in ("", "gold-sample", "evals"):
        d = os.path.join(folder, sub)
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            if not name.endswith((".md", ".txt", ".json")):
                continue
            with open(os.path.join(d, name), encoding="utf-8", errors="replace") as f:
                t = f.read()
            for m in EMAIL.findall(t):
                errs.append(f"privacy: {os.path.join(sub, name)} has an email address ({m})")
            for m in PHONE_RX.findall(t):
                if m.strip() != PHONE and not FICTIONAL.search(m):
                    errs.append(f"privacy: {os.path.join(sub, name)} has a phone number ({m})")
    return errs


def run():
    with open(PACK, encoding="utf-8") as f:
        text = f.read()
    errs, holds = check_pack(text)
    errs += privacy_scan(HERE)
    msg = block(text, "message") or ""
    for e in errs:
        print("ERROR", e)
    for h in holds:
        print(h)
    print(f"message {len(msg.split())} words; {len(errs)} errors")
    return 1 if errs else 0


def selftest():
    import shutil, tempfile
    with open(PACK, encoding="utf-8") as f:
        good = f.read()
    msg = block(good, "message")
    dlv = block(good, "delivery")
    cases = [
        ("real pack passes", good, True),
        ("a price fails", good.replace(msg, msg.replace("for free.", "for $25.")), False),
        ("a job promise fails", good.replace(msg, msg + "This will get you more interviews.\n"), False),
        ("an ATS promise fails", good.replace(msg, msg + "It's ATS-proof.\n"), False),
        ("no AI line fails", good.replace(msg, msg.replace(" with AI help", "")), False),
        ("no privacy line fails", good.replace(msg, re.sub(r"Your resume stays private\..*?\n", "", msg)), False),
        ("no business line fails", good.replace(msg, msg.replace(PHONE, "")), False),
        ("a real first name fails", good.replace(msg, msg.replace("Hi [first name],", "Hi Maria,")), False),
        ("too long fails", good.replace(msg, msg + "word " * 60 + "\n"), False),
        ("delivery without the numbers offer fails",
         good.replace(dlv, re.sub(r"If your manager.*?\n", "", dlv)), False),
        ("delivery with a guarantee fails", good.replace(dlv, dlv + "Guaranteed to work.\n"), False),
        ("a real name in the log fails", good.replace("| Person B |", "| Maria G |"), False),
        ("no trace_check --dir step fails", good.replace("trace_check.py --dir", "trace_check.py"), False),
    ]
    ok = 0
    for name, text, expect_pass in cases:
        errs, _ = check_pack(text)
        good_result = (not errs) == expect_pass
        ok += good_result
        print(("ok  " if good_result else "FAIL") + f" {name}" + ("" if good_result else f" -> {errs}"))
    # HOLD while no person is chosen; a chosen route clears it
    _, holds = check_pack(good)
    _, holds2 = check_pack(good.replace("**Route:** UNVERIFIED:", "**Route:** owner's own phone:"))
    hold_ok = bool(holds) and not holds2
    ok += hold_ok
    print(("ok  " if hold_ok else "FAIL") + " HOLD until a person is chosen")
    # privacy scan: a stray email or phone in a folder file fails; the business line passes
    tmp = tempfile.mkdtemp(prefix="privacy_")
    try:
        with open(os.path.join(tmp, "a.md"), "w") as f:
            f.write("Call " + PHONE + "\nReference: (928) 555-0144 (fictional range)\n")
        clean = not privacy_scan(tmp)
        with open(os.path.join(tmp, "b.txt"), "w") as f:
            f.write("Jane Doe | jane.doe@example.com | 480-555-2368\n")
        dirty = len(privacy_scan(tmp)) == 2
    finally:
        shutil.rmtree(tmp)
    ok += clean + dirty
    print(("ok  " if clean else "FAIL") + " privacy scan passes the business line")
    print(("ok  " if dirty else "FAIL") + " privacy scan catches an email and a phone")
    total = len(cases) + 3
    print(f"{ok}/{total}")
    return 0 if ok == total else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--self-test" in sys.argv else run())
