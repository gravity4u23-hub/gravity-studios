"""Builds the Gravity Command Center data files from the hivemind repos.
Lanes and taps are taken from Gravity-Studio/README.md, the lane folders and
gravity-studios/OWNER_BRIEF.md (Nov 21, 2026); cash from revenue-command-center/ledger.md;
open pull requests from the GitHub REST API."""
import json, re, subprocess, datetime, os
here = os.path.dirname(os.path.abspath(__file__))
code = open(os.path.join(here, "build.py")).read()
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
STAGES = {1: "Idea", 2: "Building", 3: "Ready to sell", 4: "Buyer in talks", 5: "Paying"}
# lane, offer price text, first-sale USD (one sale at the listed low price; None = no fixed price), stage, blocker, next step
L = [
 ("Magnetico sale", "$1,000 cash", 1000, 5, "None — sold", "Done: $1,000 cash collected Nov 19 (owner-confirmed; ledger fixes in Gravity-Studio PR #32)"),
 ("GEO audit", "$149", 149, 3, "Runbook scoring fix in review; El Portal reachable only by Instagram DM", "Atlas re-checks Gravity-Studio PR #33 (runbook fix + tested scorer); owner confirms PayPal + connects Instagram Messages"),
 ("Missed-Call Rescue", "$149 reactivation kit", 149, 2, "Offer + tested list cleaner in review (Gravity-Studio PR #34); outreach rides the GEO audit taps (PayPal, approval)", "Atlas reviews PR #34; then same buyer list as the audits"),
 ("Visibility Pack (GBP+GEO)", "$179", 179, 3, "Same as GEO audit", "Pitch after first GEO audit"),
 ("GBP audit", "$49", 49, 3, "Needs its first real buyer (owner confirmed no earlier buyers)", "Pitch alongside GEO and Review Desk"),
 ("Resale Concierge", "30% of sale (~$120 on a $400 item)", 120, 3, "Post is ready with the business number (747) 222-6980", "You post it (tap 11)"),
 ("Wellness Blog Engine", "$150–$300/mo", 150, 3, "Messages approved; prospects' blogs not checked yet", "Claude sharpens the messages and checks 10 prospects"),
 ("Review Reply Desk", "$79–$149/mo", 79, 3, "Atlas's 6 points fixed + reply linter added (Gravity-Studio PR #35, review_lint.py 12/12; caught and fixed 2 sample replies that stated unconfirmed facts); review gaps not counted yet; pitch needs your OK", "Atlas re-checks PR #35; one timed dry run on a real public profile; you approve the pitch"),
 ("Listing Makeover", "$79 per 20 listings", 79, 3, "Prospect shops not picked yet; pitch text needs your OK", "Claude picks 10 Etsy shops; you approve the pitch"),
 ("Fiverr gigs", "$15–$199 per order", 15, 3, "Seller account not created yet; 6 gig pages (PR #37) and 6 cover images (PR #38, checks 8/8) ready", "Owner creates the account; we paste 6 gigs with covers; Atlas reviews #37/#38"),
 ("Paid diagnostic", "$250", 250, 2, "Ladder step after an audit", "Sell only to audit buyers"),
 ("Healing Guide PDF", "$39", 39, 2, "Manuscript lives on the owner's laptop (~/workspace/recipe-book)", "Owner shares the manuscript folder"),
 ("Rewire Packs", "$12 / $45 bundle", 12, 2, "Depends on Subliminal Rewire app (Windows blocker #1)", "Fix Windows launch blocker"),
 ("Davias storefront", "Jewelry sales", None, 2, "Helix built (Davias PR #8); Atlas #4 launch fixes done on PR #9 (126 checks + finder browser test pass); waits on your Octavia wording tap", "Atlas reviews Davias PRs #8 and #9; you answer the Octavia/Founders tap"),
 ("The Gut Letter", "Free + affiliate", None, 2, "No send platform picked (Substack vs Beehiiv)", "Owner picks a platform"),
 ("The Bridge HQ", "Affiliate", None, 2, "Needs traffic first", "After Gut Letter"),
 ("Haul Partner Split", "50/50 split", None, 1, "Needs a partner", "Parked"),
]
lanes = [dict(lane=a, price=b, first_sale_usd=c, stage=STAGES[d], stage_num=d, blocker=e, next_step=f) for a,b,c,d,e,f in L]
# Owner approvals: n, tap, brief (why, in a sentence or two), button label, unlocks, first-sale USD
T = [
 (2, "Connect Instagram Messages — or just DM El Portal", "El Portal's website form is broken, so Instagram is the only way to send the $149 audit pitch. Fastest: open ig.me/m/elportalmexicanphx, paste the approved pitch (in your chat with Claude), send, then tap Mark done.", "Mark done", "GEO audit", 149),
 (8, "Approve the two new pitches", "Review Reply Desk: 'I noticed [Business] has [N] Google reviews without a reply… $79/month, first week free, no passwords.' Listing Makeover: 'I'll redo two of your listings free so you can see the difference.' Approve and each goes out only to checked prospects.", "Approve", "Review Reply Desk + Listing Makeover", 158),
 (11, "Post the Resale Concierge offer", "Your business number is in. The post is ready: 'Flagstaff-area neighbors — got stuff sitting around you want gone? I'll sell it for you on Facebook Marketplace… You keep 70%, I take 30%… text (747) 222-6980.' Post it on your Facebook and in the biggest Flagstaff buy/sell group, then tap Mark done.", "Mark done", "Resale Concierge", 120),
 (13, "Create your Fiverr seller account", "Fiverr checks your ID, so only you can open it: fiverr.com → Join → Become a Seller. Then tap Mark done; we hand you the 6 gig pages (titles, packages, descriptions) and their 6 cover images to paste — review replies, Etsy listings, wellness blogs, AI search checks, resumes, Spanish pages.", "Mark done", "Fiverr (6 gigs)", 15),
 (12, "Link your social accounts in Metricool", "Metricool is connected to Claude. Open app.metricool.com/brands/connections?blogId=8264531 and connect your Facebook Page, Instagram (Business or Creator), and any of TikTok, Threads, Pinterest, Google Business Profile. Then tap Mark done and we start scheduling posts.", "Mark done", "Posting everywhere", None),
 (14, "Davias: is Octavia making pieces now?", "The site says 'Made by Octavia, by hand' on every page. If she is making them now, tap Yes and it stays. If not yet, tap No and we change it to 'Designed by Octavia' until she is. Same tap: Founders Drops are numbered 1 to 100. Keep that line (Yes) or we drop it (No).", "Yes / No", "Davias launch", None),
 (10, "Flip the GitHub Pages switch (2 minutes)", "You approved free hosting, but only you can turn it on. On github.com: gravity-studios → Settings → Pages → Deploy from a branch → main / root → Save. Then tap Mark done.", "Mark done", "Sales site", None),
]
taps = [dict(n=n, tap=t, brief=br, button=bt, unlocks=u, first_sale_usd=v) for n,t,br,bt,u,v in T]
led = open(os.environ.get("LEDGER", "../Gravity-Studio/revenue-command-center/ledger.md")).read()
m = re.search(r"invoiced \$(\d+); collected \$(\d+); expenses \$(\d+).*?net retained \$(-?\d+)", led)
contacted = re.search(r"leads contacted (\d+)", led).group(1)
cash = [dict(metric="Collected", usd=int(m.group(2))), dict(metric="Invoiced", usd=int(m.group(1))),
        dict(metric="Expenses", usd=int(m.group(3))), dict(metric="Net retained", usd=int(m.group(4)))]
prs = []
for r in ["gravity-studios", "Gravity-Studio", "davias-earthbound-jewelry", "subliminal-rewire"]:
    # PR_COUNTS='{"repo": n}' overrides gh when gh has no token (cloud runs count via the GitHub MCP tools)
    override = json.loads(os.environ.get("PR_COUNTS", "{}"))
    out = str(override[r]) if r in override else subprocess.run(["gh","api",f"repos/gravity4u23-hub/{r}/pulls?state=open&per_page=100","--jq","length"],capture_output=True,text=True).stdout.strip()
    prs.append(dict(repo=r, open_prs=int(out or 0)))
def dump(name, rows, inp):
    json.dump({"rows": rows, "meta": [{"label": "build.py", "value": code, "type": "code", "lang": "python"},
              {"label": "Input", "value": inp}, {"label": "Built", "value": now}]}, open(os.path.join(here, name), "w"), indent=1)
dump("lanes.json", lanes, "Gravity-Studio README lane table + lane folders, Atlas reviews")
dump("taps.json", taps, "gravity-studios/OWNER_BRIEF.md tap list")
dump("cash.json", cash, f"revenue-command-center/ledger.md (leads contacted: {contacted})")
dump("prs.json", prs, "GitHub REST: open pull requests per repo")
print(now, cash, prs)
