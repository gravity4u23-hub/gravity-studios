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
 ("Magnetico sale", "$1,000 cash", 1000, 5, "None — sold", "Done: $1,000 collected (owner-confirmed, Nov 21)"),
 ("GEO audit", "$149", 149, 3, "El Portal's form is dead; Instagram DM needs Instagram Messages connected", "Owner connects Instagram Messages"),
 ("Visibility Pack (GBP+GEO)", "$179", 179, 3, "Same as GEO audit", "Pitch after first GEO audit"),
 ("GBP audit", "$49", 49, 3, "Record says '3 buyers' with no proof (Atlas #24)", "Owner answers #24, approves outreach"),
 ("Resale Concierge", "30% of sale (~$120 on a $400 item)", 120, 3, "Launch post still has the personal phone number", "Owner sets up Google Voice number"),
 ("Wellness Blog Engine", "$150–$300/mo", 150, 3, "Prospects' blogs not checked yet; message drafts need approval", "Claude checks 10 prospects; owner approves drafts"),
 ("Paid diagnostic", "$250", 250, 2, "Ladder step after an audit", "Sell only to audit buyers"),
 ("Healing Guide PDF", "$39", 39, 2, "Manuscript lives on the owner's laptop (~/workspace/recipe-book)", "Owner shares the manuscript folder"),
 ("Rewire Packs", "$12 / $45 bundle", 12, 2, "Depends on Subliminal Rewire app (Windows blocker #1)", "Fix Windows launch blocker"),
 ("Davias storefront", "Jewelry sales", None, 2, "Atlas #4 / #5: 7 of 12 Helix designs missing, 7 launch fixes", "Claude fixes #5 then #4"),
 ("The Gut Letter", "Free + affiliate", None, 2, "No send platform picked (Substack vs Beehiiv)", "Owner picks a platform"),
 ("The Bridge HQ", "Affiliate", None, 2, "Needs traffic first", "After Gut Letter"),
 ("Haul Partner Split", "50/50 split", None, 1, "Needs a partner", "Parked"),
]
lanes = [dict(lane=a, price=b, first_sale_usd=c, stage=STAGES[d], stage_num=d, blocker=e, next_step=f) for a,b,c,d,e,f in L]
T = [
 (2, "Connect Instagram Messages", "GEO audit", 149),
 (3, "Set up a Google Voice business number", "Resale Concierge", 120),
 (4, "Answer Atlas #24: were the 3 GBP buyers real?", "GBP audit", 49),
 (5, "Approve the Blog Engine message drafts", "Wellness Blog Engine", 150),
 (6, "Pick hosting for the sales site (GitHub Pages or a domain)", "Sales site", None),
 (7, "Confirm the PayPal address on the sales page", "Sales site", None),
 (8, "Test the Subliminal Rewire Windows build", "Rewire Packs", None),
]
taps = [dict(n=n, tap=t, unlocks=u, first_sale_usd=v) for n,t,u,v in T]
led = open(os.environ.get("LEDGER", "../Gravity-Studio/revenue-command-center/ledger.md")).read()
m = re.search(r"invoiced \$(\d+); collected \$(\d+); expenses \$(\d+).*?net retained \$(-?\d+)", led)
contacted = re.search(r"leads contacted (\d+)", led).group(1)
cash = [dict(metric="Collected", usd=int(m.group(2))), dict(metric="Invoiced", usd=int(m.group(1))),
        dict(metric="Expenses", usd=int(m.group(3))), dict(metric="Net retained", usd=int(m.group(4)))]
prs = []
for r in ["gravity-studios", "Gravity-Studio", "davias-earthbound-jewelry", "subliminal-rewire"]:
    out = subprocess.run(["gh","api",f"repos/gravity4u23-hub/{r}/pulls?state=open&per_page=100","--jq","length"],capture_output=True,text=True).stdout.strip()
    prs.append(dict(repo=r, open_prs=int(out or 0)))
def dump(name, rows, inp):
    json.dump({"rows": rows, "meta": [{"label": "build.py", "value": code, "type": "code", "lang": "python"},
              {"label": "Input", "value": inp}, {"label": "Built", "value": now}]}, open(os.path.join(here, name), "w"), indent=1)
dump("lanes.json", lanes, "Gravity-Studio README lane table + lane folders, Atlas reviews")
dump("taps.json", taps, "gravity-studios/OWNER_BRIEF.md tap list")
dump("cash.json", cash, f"revenue-command-center/ledger.md (leads contacted: {contacted})")
dump("prs.json", prs, "GitHub REST: open pull requests per repo")
print(now, cash, prs)
