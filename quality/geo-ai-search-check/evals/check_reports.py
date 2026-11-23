#!/usr/bin/env python3
"""check_reports.py: GEO / AI Search Check eval set runner (code-graded rules on the REPORT).

The work log already has a gate (Gravity-Studio revenue-command-center/geo_worklog_check.py,
PR #54). This checks the buyer-facing report that is built from it, against the hard requests a
buyer (or a tired seller) could push us toward.

Runs every case in cases.json against base-report.md (a SYNTHETIC business):
  * GOLD = base report + the case's gold_edits: must pass every rule, and
  * BAD  = base report + the case's bad_edits: must fail on the rule named in 'bad_breaks'
    (proves the checker isn't rubber-stamping).

Rules (all code, no judgment):
  score_math         stated score / denominator / % / band must equal the recomputed score
                     (Cited 3, Mentioned 2, Not mentioned 0, Unknown excluded; denominator
                     27 - 3 x Unknown; band on the exact %), and each line's Points must match
  hidden_check       all 9 checks G1..G9 appear once (scored in FULL FINDINGS or Unknown in
                     NOT SCORED), and every Unknown names its reason
  promises           a ranking / placement / results promise anywhere outside WHAT THIS AUDIT
                     IS NOT (guarantee, "will rank", "#1", "more calls", ...), unless negated
  profile_placement  wording that claiming the ChatGPT profile raises how often you're named
                     (OpenAI: "Claiming a profile ... doesn't change its visibility in ChatGPT")
  fix_evidence       exactly 3 top fixes, each with "Evidence: screenshot G#" pointing at a
                     scored check (not an Unknown, not a missing one)
  unsourced_stats    any % other than the score line, or "studies/research/surveys show"
  limits_missing     WHAT THIS AUDIT IS NOT section with "No ranking guarantee", and the
                     snapshot line "These are the answers on YYYY-MM-DD"
  crawler_profile    CAN THE AI ENGINES READ YOUR SITE? section with a
                     "ChatGPT business profile: Claimed / Not claimed / Unknown" line
  profile_claim      when the profile is "Not claimed" (the Business Hub fold-in, Nov 23): the
                     profile block (that line + the lines under it) must say claiming is free, warn that a published profile
                     can't be unpublished (check details first), and never ask the buyer for
                     their login, password, verification code or ID (they verify it themselves)
  unfilled           a template bracket left in, e.g. "[Business name]"

Code proves a report breaks no hard rule. It can't tell whether the fixes are the right ones.
That is Atlas's rubric (RUBRIC.md).

Usage:
  python3 check_reports.py              run the eval set (exit 0 = all as expected)
  python3 check_reports.py REPORT.md    check one real report
  python3 check_reports.py --test       self-tests for the helpers
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
POINTS = {"cited": 3, "mentioned": 2, "not mentioned": 0}
BANDS = [(85, "Strong"), (65, "Needs work"), (40, "Significant gaps"), (0, "Needs urgent attention")]
UNKNOWN_REASONS = ("unreachable", "no ai overview", "no ai answer", "unreadable", "sign-in", "sign in", "login")
NEGATION = re.compile(r"\b(no|not|never|doesn't|does not|don't|do not|can't|cannot|won't|isn't)\b", re.I)
PROMISE = re.compile(
    r"\bguarantee[ds]?\b|\bwill (rank|appear|show up|be (named|recommended|cited|listed))\b|"
    r"#\s?1\b|\bnumber one\b|\btop spot\b|\bfirst page\b|"
    r"\b(more|extra|double|triple) (calls|customers|bookings|leads|sales|clients|traffic)\b|"
    r"\bincrease (your )?(calls|sales|traffic|bookings|leads)\b", re.I)
PROFILE_LIFT = re.compile(r"\b(rank|ranking|higher|more often|recommend|recommended|boost|named more|show up more|get you named)\b|"
                          r"\b(raise|raises|improve|improves|increase|increases|lift|lifts)( your)? visibility\b", re.I)
STATS = re.compile(r"\d+(\.\d+)?\s?%|\b(studies|research|surveys|statistics|data) (show|shows|prove|proves|suggest|suggests)\b", re.I)
FINDING = re.compile(r"^(G\d)\b.*?—\s*(Cited|Mentioned|Not mentioned)\s*—\s*Points:\s*(\d)\s*/\s*3", re.I)
UNKNOWN = re.compile(r"^-?\s*Unknown:\s*(G\d)\b(.*)$", re.I)
CLAIM_FREE = re.compile(r"\bfree\b|\bno (fee|cost|charge)\b|\bcosts nothing\b", re.I)
CLAIM_LOCK = re.compile(r"\b(can't|cannot|can not) be (unpublished|taken down|deleted|removed|hidden)\b|"
                        r"\b(can't|cannot) (unpublish|take down|delete|remove|hide)\b", re.I)
CLAIM_CREDS = re.compile(r"\b(send|give|share|forward|text|email)\b[^.]*\b(login|log-in|password|"
                         r"verification code|code|ID|photo ID|driver'?s license|sign-in)\b", re.I)
SCORE = re.compile(r"^##\s*YOUR SCORE:\s*(\d+)\s*/\s*(\d+)\s*\((\d+)%\)\s*—\s*(.+?)\s*$", re.I)


def sections(text):
    """{UPPER heading: body} for every '## ' heading; '_top' = text before the first one."""
    out, name, buf = {}, "_top", []
    for line in text.splitlines():
        m = re.match(r"^##\s+(.*)$", line)
        if m:
            out[name] = "\n".join(buf)
            name, buf = m.group(1).strip().upper(), [line]
        else:
            buf.append(line)
    out[name] = "\n".join(buf)
    return out


def find(secs, prefix):
    for k, v in secs.items():
        if k.startswith(prefix):
            return v
    return None


def sentences(text):
    return [s for s in re.split(r"(?<=[.!?])\s+|\n", text) if s.strip()]


def score(outcomes):
    unknown = outcomes.count("U")
    awarded = sum(POINTS[o] for o in outcomes if o != "U")
    denom = 27 - 3 * unknown
    exact = 100 * awarded / denom if denom else 0
    band = next(n for floor, n in BANDS if exact >= floor)
    return awarded, denom, round(exact), band


def check(text):
    broken = {}
    secs = sections(text)

    # score_math + hidden_check
    scored, unknowns, bad_points = {}, {}, []
    for line in text.splitlines():
        s = line.strip()
        m = FINDING.match(s)
        if m:
            gid, out, pts = m.group(1).upper(), m.group(2).lower(), int(m.group(3))
            scored[gid] = out
            if POINTS[out] != pts:
                bad_points.append(f"{gid} {out} shows {pts}/3, should be {POINTS[out]}/3")
        m = UNKNOWN.match(s)
        if m:
            gid = m.group(1).upper()
            unknowns[gid] = m.group(2)
    ids = list(scored) + list(unknowns)
    expected = {f"G{i}" for i in range(1, 10)}
    hidden = []
    if set(ids) != expected or len(ids) != 9:
        missing = sorted(expected - set(ids))
        dup = sorted({i for i in ids if ids.count(i) > 1})
        hidden.append(f"checks missing {missing}" if missing else f"checks listed twice {dup}")
    for gid, why in unknowns.items():
        if not any(r in why.lower() for r in UNKNOWN_REASONS):
            hidden.append(f"Unknown {gid} has no reason")
    if hidden:
        broken["hidden_check"] = "; ".join(hidden)

    stated = None
    for line in text.splitlines():
        m = SCORE.match(line.strip())
        if m:
            stated = (int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4).strip())
    math = list(bad_points)
    if stated is None:
        math.append("no '## YOUR SCORE: X / Y (Z%) — Band' line")
    elif len(ids) == 9 and set(ids) == expected:
        outs = ["U" if g in unknowns else scored[g] for g in sorted(expected)]
        if outs.count("U") < 9:
            want = score(outs)
            if stated != want:
                math.append(f"stated {stated[0]}/{stated[1]} ({stated[2]}%) {stated[3]}, "
                            f"recomputed {want[0]}/{want[1]} ({want[2]}%) {want[3]}")
    if math:
        broken["score_math"] = "; ".join(math)

    # promises (outside the limits section)
    limits = find(secs, "WHAT THIS AUDIT IS NOT") or ""
    rest = "\n".join(v for k, v in secs.items() if not k.startswith("WHAT THIS AUDIT IS NOT"))
    hits = [s.strip() for s in sentences(rest) if PROMISE.search(s) and not NEGATION.search(s)]
    if hits:
        broken["promises"] = hits[0][:120]

    # profile_placement
    # every sentence on a line that talks about the ChatGPT profile (the claim often sits in the
    # sentence after the one that names the profile)
    lifts = [s.strip() for line in text.splitlines()
             if "profile" in line.lower() and "chatgpt" in line.lower()
             for s in sentences(line) if PROFILE_LIFT.search(s) and not NEGATION.search(s)]
    if lifts:
        broken["profile_placement"] = lifts[0][:120]

    # fix_evidence
    fixes = find(secs, "TOP 3 FIXES") or ""
    items = re.findall(r"^\d\.\s.*?(?=^\d\.\s|\Z)", fixes, re.M | re.S)
    ev = []
    if len(items) != 3:
        ev.append(f"{len(items)} fixes, need exactly 3")
    for n, item in enumerate(items, 1):
        m = re.search(r"Evidence:\s*screenshot\s+(G\d)\b", item, re.I)
        if not m:
            ev.append(f"fix {n} has no 'Evidence: screenshot G#'")
        elif m.group(1).upper() not in scored:
            ev.append(f"fix {n} points at {m.group(1).upper()}, which is not a scored check")
    if ev:
        broken["fix_evidence"] = "; ".join(ev)

    # unsourced_stats (score line excluded)
    stat_hits = []
    for line in text.splitlines():
        if SCORE.match(line.strip()):
            continue
        m = STATS.search(line)
        if m:
            stat_hits.append(line.strip()[:120])
    if stat_hits:
        broken["unsourced_stats"] = stat_hits[0]

    # limits_missing
    lim = []
    if not limits:
        lim.append("no WHAT THIS AUDIT IS NOT section")
    elif "no ranking guarantee" not in limits.lower():
        lim.append("limits section lacks 'No ranking guarantee'")
    if not re.search(r"These are the answers on \d{4}-\d{2}-\d{2}", text):
        lim.append("no dated snapshot line")
    if lim:
        broken["limits_missing"] = "; ".join(lim)

    # crawler_profile
    crawl = find(secs, "CAN THE AI ENGINES READ YOUR SITE")
    if not crawl:
        broken["crawler_profile"] = "no crawler section"
    elif not re.search(r"ChatGPT business profile:\s*(Claimed|Not claimed|Unknown)\b", crawl):
        broken["crawler_profile"] = "no 'ChatGPT business profile: Claimed / Not claimed / Unknown' line"

    # profile_claim: only when we're telling them to claim it
    # only the profile block: the "ChatGPT business profile:" line and the lines right under it,
    # up to the next blank line or heading (a "free" elsewhere, e.g. "Claim your free re-check",
    # must not satisfy it; Atlas, PR #54)
    plines, inblock = [], False
    for l in text.splitlines():
        if re.match(r"\s*ChatGPT business profile:", l):
            inblock = True
        elif inblock and (not l.strip() or l.startswith("#")):
            inblock = False
        if inblock:
            plines.append(l)
    pl = "\n".join(plines)
    if re.search(r"ChatGPT business profile:\s*Not claimed\b", text):
        pc = []
        if not CLAIM_FREE.search(pl):
            pc.append("doesn't say claiming is free")
        if not CLAIM_LOCK.search(pl):
            pc.append("no warning that a published profile can't be unpublished")
        creds = [x.strip() for x in sentences(pl) if CLAIM_CREDS.search(x) and not NEGATION.search(x)]
        if creds:
            pc.append("asks for the buyer's login/code/ID: " + creds[0][:80])
        if pc:
            broken["profile_claim"] = "; ".join(pc)

    # unfilled template brackets
    br = re.findall(r"\[[A-Za-z0-9][^\]]{0,60}\]", text)
    if br:
        broken["unfilled"] = ", ".join(br[:3])
    return broken


def apply(base, edits, cid):
    out = base
    for old, new in edits:
        if out.count(old) != 1:
            raise SystemExit(f"{cid}: edit target must occur once in base-report.md: {old!r}")
        out = out.replace(old, new, 1)
    return out


def run():
    data = json.load(open(os.path.join(HERE, "cases.json"), encoding="utf-8"))
    base = open(os.path.join(HERE, "base-report.md"), encoding="utf-8").read()
    ok = total = 0
    b0 = check(base)
    good = not b0
    print(f"{'ok ' if good else 'BAD'} base report: {'passes all rules' if good else b0}")
    ok += good
    total += 1
    for c in data["cases"]:
        g = check(apply(base, c.get("gold_edits", []), c["id"]))
        good = not g
        print(f"{'ok ' if good else 'BAD'} {c['id']}: gold {'passes' if good else 'FAILS ' + str(g)}")
        ok += good
        total += 1
        b = check(apply(base, c["bad_edits"], c["id"]))
        good = c["bad_breaks"] in b
        extra = sorted(set(b) - {c["bad_breaks"]})
        if good:
            print(f"ok  {c['id']}: bad caught on {c['bad_breaks']}" + (f" (also {', '.join(extra)})" if extra else ""))
        else:
            print(f"BAD {c['id']}: bad NOT caught on {c['bad_breaks']} (got {sorted(b)})")
        ok += good
        total += 1
    print(f"{ok}/{total}")
    return ok == total


def _test():
    cases = [
        ("score: 2 Unknown (worklog GOOD case)", score(["mentioned", "U", "not mentioned", "cited", "not mentioned",
                                                        "U", "not mentioned", "mentioned", "not mentioned"]),
         (7, 21, 33, "Needs urgent attention")),
        ("score: all cited", score(["cited"] * 9), (27, 27, 100, "Strong")),
        ("score: 14/24 = 58% Significant gaps", score(["cited"] * 4 + ["mentioned"] + ["not mentioned"] * 3 + ["U"]),
         (14, 24, 58, "Significant gaps")),
        ("negated promise allowed", bool(PROMISE.search("We can't guarantee placement")) and bool(NEGATION.search("We can't guarantee placement")), True),
        ("plain promise caught", bool(PROMISE.search("This will get you more calls.")), True),
        ("'#1 fix' is caught on the safe side (known limit)", bool(PROMISE.search("Our #1 fix")), True),
        ("score line % is not a stat", bool(SCORE.match("## YOUR SCORE: 7 / 21 (33%) — Needs urgent attention")), True),
        ("$49 price is not a stat", bool(STATS.search("Order the GBP audit ($49)")), False),
        ("'Visibility Pack' is not a profile claim", bool(PROFILE_LIFT.search("the Visibility Pack ($179)")), False),
        ("'improves your visibility' is", bool(PROFILE_LIFT.search("Claiming it improves your visibility")), True),
        ("claim lock: 'can't be unpublished'", bool(CLAIM_LOCK.search("guides report it can't be unpublished")), True),
        ("claim lock: 'can be edited' is not a warning", bool(CLAIM_LOCK.search("it can be edited later")), False),
        ("creds: 'send us the verification code'", bool(CLAIM_CREDS.search("Send us the verification code and we'll finish it.")), True),
        ("creds: 'never share your login' is negated", bool(CLAIM_CREDS.search("Never share your login with us.")) and bool(NEGATION.search("Never share your login with us.")), True),
        ("free: 'no fee'", bool(CLAIM_FREE.search("OpenAI lists no fee for it")), True),
        ("brackets found", bool(re.findall(r"\[[A-Za-z][^\]]{0,40}\]", "AUDIT — [Business name], [City]")), True),
    ]
    ok = 0
    for name, got, want in cases:
        good = got == want
        ok += good
        print(f"{'ok ' if good else 'BAD'} {name}: {got!r}")
    print(f"{ok}/{len(cases)}")
    return ok == len(cases)


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["--test"]:
        sys.exit(0 if _test() else 1)
    if len(args) == 1:
        res = check(open(args[0], encoding="utf-8").read())
        if res:
            print("NOT READY:")
            for k, v in res.items():
                print(f" - {k}: {v}")
            sys.exit(1)
        print("READY: report breaks no hard rule (Atlas rubric still applies)")
        sys.exit(0)
    sys.exit(0 if run() else 1)
