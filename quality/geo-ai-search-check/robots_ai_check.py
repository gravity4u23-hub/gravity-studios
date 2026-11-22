"""robots_ai_check.py — does a site's robots.txt block the AI search crawlers?

Closes a gap the GEO benchmark found (red flag #7 in edthi.com's Nov 6, 2026 list:
"They don't check whether AI crawlers can reach your site"). Our $149 audit screenshots
what the engines say; it never checked whether the engines are even allowed to read
the buyer's site. This adds that check at $0, from the public robots.txt only.

Usage:
  python3 robots_ai_check.py robots.txt [page-path]   # check a saved robots.txt
  python3 robots_ai_check.py --test                     # self-tests

Reports per crawler: ALLOWED / BLOCKED for the page path (default "/").
It reads a file the auditor saved from https://<site>/robots.txt (public data only).
It never fetches anything itself, so it needs no network and no credentials.

Honesty rules baked in:
- A crawler that is allowed is NOT a promise the engine will name the business.
- Google-Extended does NOT control Google AI Overviews (those use Googlebot); it is
  reported separately and never called an AI Overview blocker.
- No robots.txt at all means everything is allowed (that's how robots.txt works).
"""
import sys
from urllib.robotparser import RobotFileParser

# user-agent token, engine, what blocking it affects (wording kept narrow on purpose)
CRAWLERS = [
    ("OAI-SearchBot", "ChatGPT search", "can stop the site showing as a source in ChatGPT search answers"),
    ("ChatGPT-User", "ChatGPT", "can stop ChatGPT opening the page when a user asks it to"),
    ("GPTBot", "OpenAI training", "training only; not the same as ChatGPT search"),
    ("PerplexityBot", "Perplexity", "can stop the site showing as a source in Perplexity answers"),
    ("ClaudeBot", "Anthropic training", "training only"),
    ("Googlebot", "Google Search + AI Overviews", "blocks Google Search itself, including AI Overviews"),
    ("Google-Extended", "Gemini apps / training", "does NOT affect AI Overviews in Google Search"),
]
SEARCH_CRITICAL = {"OAI-SearchBot", "PerplexityBot", "Googlebot"}


def check(robots_text, path="/"):
    rp = RobotFileParser()
    rp.parse(robots_text.splitlines())
    url = "https://example.invalid" + (path if path.startswith("/") else "/" + path)
    return [(ua, eng, note, rp.can_fetch(ua, url)) for ua, eng, note in CRAWLERS]


def report(rows):
    lines = []
    for ua, eng, note, ok in rows:
        lines.append(f"{'ALLOWED' if ok else 'BLOCKED':7}  {ua:15} {eng:30} {'' if ok else '— ' + note}".rstrip())
    blocked = [ua for ua, _, _, ok in rows if not ok and ua in SEARCH_CRITICAL]
    if blocked:
        lines.append("FINDING: robots.txt blocks " + ", ".join(blocked) +
                     ". Fix: remove the Disallow for these user-agents (5 min, or 'needs your web person').")
    else:
        lines.append("No search-crawler block found in robots.txt. (Allowed is not a promise of being named.)")
    return "\n".join(lines)


def _t(name, robots, path, expect):
    got = {ua: ok for ua, _, _, ok in check(robots, path)}
    bad = {k: (got[k], v) for k, v in expect.items() if got[k] != v}
    print(("PASS " if not bad else "FAIL ") + name + ("" if not bad else f" {bad}"))
    return not bad


def selftest():
    cases = [
        ("empty robots.txt allows all", "", "/", {u: True for u, _, _ in CRAWLERS}),
        ("wildcard disallow blocks all", "User-agent: *\nDisallow: /", "/",
         {u: False for u, _, _ in CRAWLERS}),
        ("GPTBot-only block leaves ChatGPT search open",
         "User-agent: GPTBot\nDisallow: /", "/",
         {"GPTBot": False, "OAI-SearchBot": True, "ChatGPT-User": True, "Googlebot": True}),
        ("Google-Extended block leaves Googlebot (AI Overviews) open",
         "User-agent: Google-Extended\nDisallow: /", "/",
         {"Google-Extended": False, "Googlebot": True}),
        ("PerplexityBot blocked, others open",
         "User-agent: PerplexityBot\nDisallow: /\n\nUser-agent: *\nAllow: /", "/",
         {"PerplexityBot": False, "OAI-SearchBot": True}),
        ("wildcard block but OAI-SearchBot allowed by its own group",
         "User-agent: OAI-SearchBot\nAllow: /\n\nUser-agent: *\nDisallow: /", "/",
         {"OAI-SearchBot": True, "PerplexityBot": False, "Googlebot": False}),
        ("path-level block only hits that path",
         "User-agent: *\nDisallow: /private/", "/menu",
         {u: True for u, _, _ in CRAWLERS}),
        ("path-level block on the checked path",
         "User-agent: *\nDisallow: /private/", "/private/x",
         {u: False for u, _, _ in CRAWLERS}),
        ("user-agent match is case-insensitive",
         "User-agent: oai-searchbot\nDisallow: /", "/", {"OAI-SearchBot": False, "GPTBot": True}),
    ]
    ok = all(_t(*c) for c in cases)
    # report wording: never claims Google-Extended blocks AI Overviews; finding names only search-critical bots
    r = report(check("User-agent: Google-Extended\nDisallow: /\nUser-agent: GPTBot\nDisallow: /"))
    w1 = "FINDING" not in r and "does NOT affect AI Overviews" in r
    print(("PASS " if w1 else "FAIL ") + "training-only blocks are not reported as a search finding")
    r2 = report(check("User-agent: OAI-SearchBot\nDisallow: /"))
    w2 = "FINDING: robots.txt blocks OAI-SearchBot." in r2
    print(("PASS " if w2 else "FAIL ") + "OAI-SearchBot block is a finding with a fix line")
    r3 = report(check(""))
    w3 = "not a promise" in r3
    print(("PASS " if w3 else "FAIL ") + "all-clear line never promises being named")
    n = len(cases) + 3
    allok = ok and w1 and w2 and w3
    print(f"{n if allok else '<'+str(n)}/{n} self-tests {'pass' if allok else 'FAILED'}")
    return allok


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sys.exit(0 if selftest() else 1)
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    text = open(sys.argv[1], encoding="utf-8", errors="replace").read()
    print(report(check(text, sys.argv[2] if len(sys.argv) > 2 else "/")))
