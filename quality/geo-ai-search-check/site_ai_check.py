#!/usr/bin/env python3
"""site_ai_check.py — can an AI search engine read the business's own pages, and do they agree?

GEO gate step 2 (part A, site side). The 9 engine checks need a signed-in browser; this half
does not. It reads a saved copy of the buyer's public pages (or their site's source folder) and
reports four things the engines depend on, from the files only (no network, no credentials):

  1. Text without JavaScript. Many AI crawlers do not run scripts. A page whose words only
     appear after JavaScript may look empty to them. Reports words visible in the raw HTML.
  2. Structured data (JSON-LD). Lists the schema.org @type on each page; flags product pages
     with no Product data and any block that does not parse.
  3. Contact details agree. Every phone number on every page is compared with the number the
     buyer says is current (--phone). A different number is a finding: an engine that quotes
     the page may give customers the wrong line.
  4. Sitemap coverage. Pages that are not in sitemap.xml, and sitemap entries with no page.

Honesty rules baked in (same as robots_ai_check.py and the report rubric):
  - Nothing here says a fix "will" get the business named. Findings use "may".
  - Readable text and valid schema are not a promise of being named.
  - It reports what the files show. If the files are a repo copy, say so in the report and
    confirm against the live site before it goes to a buyer.

Usage:
  python3 site_ai_check.py SITE_DIR --phone 747-222-6980 [--products p/] [--min-words 100]
  python3 site_ai_check.py --test
Exit 0 = no findings, 1 = findings listed, 2 = usage error.
"""
import json
import os
import re
import sys

PHONE = re.compile(r"(?<!\d)(?:\+?1[\s.-]?)?\(?(\d{3})\)?[\s.-]?(\d{3})[\s.-]?(\d{4})(?!\d)")
LD = re.compile(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', re.S | re.I)
STRIP = re.compile(r"<script.*?</script>|<style.*?</style>|<noscript.*?</noscript>", re.S | re.I)
TAG = re.compile(r"<[^>]+>")
LOC = re.compile(r"<loc>\s*([^<\s]+)\s*</loc>", re.I)


def norm_phone(s):
    m = PHONE.search(s)
    return "-".join(m.groups()) if m else None


def visible_words(html):
    body = re.search(r"<body.*?</body>", html, re.S | re.I)
    text = TAG.sub(" ", STRIP.sub(" ", body.group(0) if body else html))
    text = re.sub(r"&[a-z#0-9]+;", " ", text)
    return len(re.findall(r"[A-Za-z][A-Za-z'’-]*", text))


def ld_types(html):
    types, errors = [], 0
    for block in LD.findall(html):
        try:
            data = json.loads(block)
        except ValueError:
            errors += 1
            continue
        items = data if isinstance(data, list) else data.get("@graph", [data])
        for it in items:
            t = it.get("@type") if isinstance(it, dict) else None
            types += t if isinstance(t, list) else ([t] if t else [])
    return types, errors


def phones(html):
    # phone numbers in text and in tel: links; JSON-LD counts too (engines read it)
    return {"-".join(m.groups()) for m in PHONE.finditer(TAG.sub(" ", html) + " " + " ".join(re.findall(r'tel:([^"\']+)', html)))}


def pages(site_dir):
    out = {}
    for root, _, files in os.walk(site_dir):
        for f in files:
            if f.endswith(".html"):
                p = os.path.join(root, f)
                out[os.path.relpath(p, site_dir).replace(os.sep, "/")] = open(p, encoding="utf-8", errors="replace").read()
    return out


def sitemap_paths(site_dir):
    p = os.path.join(site_dir, "sitemap.xml")
    if not os.path.exists(p):
        return None
    paths = set()
    for url in LOC.findall(open(p, encoding="utf-8", errors="replace").read()):
        path = re.sub(r"^https?://[^/]+", "", url).lstrip("/")
        paths.add(path if path and not path.endswith("/") else (path + "index.html"))
    return paths


def check(site, expected_phone, products="p/", min_words=100, sitemap=None, skip=("404.html",)):
    """site: {relpath: html}. Returns (rows, findings)."""
    want = norm_phone(expected_phone) if expected_phone else None
    rows, findings = [], []
    other_phones = {}
    for path in sorted(site):
        if path in skip:
            continue
        html = site[path]
        words = visible_words(html)
        types, errs = ld_types(html)
        ph = phones(html)
        rows.append((path, words, types, errs, sorted(ph)))
        if words < min_words:
            findings.append(f"THIN  {path}: {words} words readable without JavaScript (under {min_words}). "
                            "AI crawlers that don't run scripts may see little here.")
        if errs:
            findings.append(f"LD    {path}: {errs} JSON-LD block(s) do not parse. Engines may ignore them.")
        if path.startswith(products) and "Product" not in types:
            findings.append(f"NOPRD {path}: product page with no schema.org Product data (has: {', '.join(types) or 'none'}).")
        if want:
            for p in ph - {want}:
                other_phones.setdefault(p, []).append(path)
    for p, where in sorted(other_phones.items()):
        findings.append(f"PHONE {p} appears on {len(where)} page(s) (e.g. {where[0]}), not the current number {want}. "
                        "An engine that quotes these pages may give customers this number.")
    if sitemap is not None:
        listed = {p for p in site if p not in skip}
        for p in sorted(listed - sitemap):
            findings.append(f"MAP   {p} is not in sitemap.xml.")
        for p in sorted(sitemap - set(site)):
            findings.append(f"MAP   sitemap.xml lists {p}, but there is no such page.")
    elif sitemap is None and site:
        pass
    return rows, findings


def report(rows, findings, sitemap_found=True):
    out = [f"{'page':34} {'words':>5}  schema types · phones"]
    for path, words, types, errs, ph in rows:
        out.append(f"{path:34} {words:>5}  {', '.join(types) or '-'}{' (+%d bad)' % errs if errs else ''} · {', '.join(ph) or '-'}")
    if not sitemap_found:
        findings = findings + ["MAP   no sitemap.xml found."]
    out.append("")
    out += findings or ["No site-side findings. (Readable pages and valid schema are not a promise of being named.)"]
    by = {}
    for f in findings:
        by[f[:5].strip()] = by.get(f[:5].strip(), 0) + 1
    out.append("SUMMARY: " + (", ".join(f"{k} {v}" for k, v in sorted(by.items())) if by else "0 findings"))
    return "\n".join(out)


# ---------------------------------------------------------------- self-tests
def _page(body="", ld=None, extra=""):
    ld_html = "".join(f'<script type="application/ld+json">{x}</script>' for x in (ld or []))
    return f"<html><head>{ld_html}</head><body>{body}{extra}</body></html>"


WORDS = " ".join(["stone"] * 120)
ORG = '{"@context":"https://schema.org","@type":"Organization","name":"X","telephone":"747-222-6980"}'
PRD = '{"@context":"https://schema.org","@type":"Product","name":"Ring"}'


def selftest():
    T = []

    def t(name, ok):
        T.append(ok)
        print(("PASS " if ok else "FAIL ") + name)

    good = {"index.html": _page(WORDS + " call 747-222-6980", [ORG]), "p/ring.html": _page(WORDS, [ORG, PRD])}
    _, f = check(good, "(747) 222-6980", sitemap={"index.html", "p/ring.html"})
    t("clean site: 0 findings", f == [])

    js_only = {"index.html": _page("<div id=app></div>", [ORG], "<script>document.body.innerHTML='" + WORDS + "'</script>")}
    _, f = check(js_only, "747-222-6980")
    t("text that only arrives by JavaScript is THIN", any(x.startswith("THIN") for x in f))

    _, f = check({"p/ring.html": _page(WORDS, [ORG])}, "747-222-6980")
    t("product page without Product schema is NOPRD", any(x.startswith("NOPRD") for x in f))

    _, f = check({"index.html": _page(WORDS, ['{"@type": "Organization",}'])}, "747-222-6980")
    t("JSON-LD that does not parse is LD", any(x.startswith("LD") for x in f))

    old = '{"@type":"Organization","telephone":"747-528-7039"}'
    _, f = check({"index.html": _page(WORDS + " 747-222-6980", [old])}, "747-222-6980")
    t("old number hidden in JSON-LD only is still a PHONE finding", any("747-528-7039" in x for x in f))

    _, f = check({"index.html": _page(WORDS + ' <a href="tel:+17475287039">Call</a>')}, "747-222-6980")
    t("old number in a tel: link is a PHONE finding", any(x.startswith("PHONE 747-528-7039") for x in f))

    _, f = check({"index.html": _page(WORDS + " (747) 222-6980 or 747.222.6980 or +1 747 222 6980")}, "747-222-6980")
    t("same number written 3 ways is not a finding", f == [])

    _, f = check({"index.html": _page(WORDS + " order #2025550142 ships in 3-5 days, $1,250.00")}, "747-222-6980")
    t("a 10-digit order number is read as a phone (safe side: human clears it)",
      any(x.startswith("PHONE 202-555-0142") for x in f))

    _, f = check({"index.html": _page(WORDS), "new.html": _page(WORDS)}, "747-222-6980", sitemap={"index.html", "gone.html"})
    t("page missing from sitemap + sitemap entry with no page are both MAP",
      sum(x.startswith("MAP") for x in f) == 2)

    _, f = check({"404.html": _page("Not found")}, "747-222-6980")
    t("404 page is skipped", f == [])

    rows, f = check(good, "747-222-6980", sitemap={"index.html", "p/ring.html"})
    r = report(rows, f) + report(*check(js_only, "747-222-6980"))
    t("report never says 'will be named' / 'guarantee'", not re.search(r"will be (named|cited|listed)|guarantee", r, re.I)
      and "not a promise" in report(rows, f))

    n = len(T)
    print(f"{sum(T)}/{n} self-tests {'pass' if all(T) else 'FAILED'}")
    return all(T)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["--test"]:
        sys.exit(0 if selftest() else 1)
    if not a or a[0].startswith("-"):
        print(__doc__)
        sys.exit(2)

    def opt(name, default=None):
        return a[a.index(name) + 1] if name in a else default

    site_dir = a[0]
    smap = sitemap_paths(site_dir)
    rows, findings = check(pages(site_dir), opt("--phone"), opt("--products", "p/"), int(opt("--min-words", "100")),
                           sitemap=smap)
    print(report(rows, findings, sitemap_found=smap is not None))
    sys.exit(1 if findings or smap is None else 0)
