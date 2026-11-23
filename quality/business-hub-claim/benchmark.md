# Business Hub Claim (ChatGPT) — Benchmark (Quality Gate step 1)

**Status:** Claude's draft, 2026-11-23 11:25 UTC run. Step 1 is Grok's job. It was assigned at 09:25 UTC, and no Grok work on it was found in either repo by 11:25, so Claude drafted it the same way as the GEO, Resume and Spanish benchmarks. **Atlas: re-open every source. None of these pages is OpenAI's own.** The cloud can't open help.openai.com, so OpenAI's wording below is as quoted by third parties.

Pages read 2026-11-23 ~11:30 UTC. **LocalIQ** (localiq.com/blog/businesses-in-chatgpt) returned a bot-check page and was not read.

## What it is (facts that shape the offer)
| Fact | Quote | Source |
|---|---|---|
| Launched in beta Nov 10, 2026 | "Beta since Nov 10" (page's facts checked Nov 12) | getpassionfruit.com/lp/businesses-in-chatgpt |
| **Claiming costs nothing** (no source says this in OpenAI's own words) | "It's free and takes minutes." / "OpenAI doesn't list a fee for claiming a business." | eesel.ai/blog/how-to-claim-your-business-on-chatgpt |
| | "We weren't asked to pay." | rankability.com/blog/how-to-claim-your-business-in-chatgpt |
| **Claiming doesn't change placement** | OpenAI FAQ as quoted: "ChatGPT continues to make independent recommendations and comparisons. Claiming does not guarantee higher placement or sales." | getpassionfruit.com (only verbatim quote found) |
| **The owner must verify, in person** | Business phone, business email, DNS TXT record or Shopify; then a Persona ID check that gates edits, insights and the blue check | eesel.ai; sqspthemes.com ("Persona is required before it can update information or access analytics"); rankability.com (DNS + email + SMS + ID scan with facial recognition) |
| **Local shops can only claim an existing US listing** | Local stores and restaurants "can only claim an existing US listing." | eesel.ai; sqspthemes.com ("can currently claim only existing U.S. listings") |
| **Can't be taken down once published** (reported) | A Persona-approved new profile "publishes automatically", and OpenAI Support "can't delete, unpublish or hide a published profile." | eesel.ai |
| Name can't be edited after claiming (one tester) | Business name not editable in any of the editor's five tabs | rankability.com |
| Business Agents | US e-commerce or online-service businesses with a website only | eesel.ai, passionfruit, sqspthemes, upgrowth.in |

## Who sells it now
| Who | Price | What's included | Delivery | Source |
|---|---|---|---|---|
| **upGrowth** (agency, India) | **No price shown**: "quoted after a 30-minute call" | "Readiness Sprint": 20-prompt baseline, audit of up to 10 listings, schema for up to 5 offerings, profile copy with up to 2 revision rounds, agent context pack | Not shown | upgrowth.in/chatgpt-business-hub-agency-india |
| **Passionfruit** (agency) | **No price shown**: "custom pricing: after a strategy call we share a proposal" | Claim and verify "from an account you control", product connection, agent build, monthly insights review, content brief | Not shown | getpassionfruit.com/lp/businesses-in-chatgpt |
| **Rankability** (AEO agency) | No claim price; "Book a strategy call" | General AEO services | Not shown | rankability.com |
| **Free how-to guides** | **$0** | Step-by-step claim guides: eesel, Rankability, B12, findskill.ai, gauravtiwari.org and others | Instant | search results 2026-11-23 |
| **Fiverr** | **No gig found** for claiming a ChatGPT business profile in a search on 2026-11-23 (one search only; Fiverr pages not opened). Closest: GEO "get your brand found in ChatGPT" gigs (see GEO benchmark) | — | — | web search, 2026-11-23 |

## What buyers complain about (evidence)
**Honest gap: no buyer review of a paid claiming service exists yet.** The service is 13 days old. What owners report about **claiming itself** (eesel's troubleshooting section, Rankability's test):
1. DNS TXT checks fail on a trailing dot or an auto-added host name.
2. Persona ID checks fail or expire.
3. "Listing is locked" with only "Contact support."
4. Saved changes don't show in answers right away.
5. Published profiles can't be unpublished; the name can't be edited after claiming.
6. upGrowth's own claim ended on a waitlist, and ChatGPT showed three lookalike firms for its name.

## Our offer against this (honest)
- **We can't do it for them, and must not try.** Verification is the owner's own phone, email, domain and face. Taking a client's logins, codes or ID photo would break our hard rules (no credentials) and likely OpenAI's. Any offer is a **guided claim**: we prepare everything, the owner taps the verification steps.
- **"Done-for-you" claims are free to do yourself.** A $49 fee is only fair if the buyer gets something a free guide doesn't: correct, sourced profile copy, the before/after of what ChatGPT says about them, and a fix for complaints 1–5 above (we check their DNS record format and listing before they start).
- **Price:** agencies hide prices behind a call. A fixed, posted price is a real difference, but we can't say "cheaper" because we can't see theirs.
- **Speed:** unknown for everyone; OpenAI publishes no review time.
- **Placement:** we can never say it gets them recommended more. OpenAI says it doesn't.
- **Risk to say up front:** once published, the profile can't be taken down (reported by eesel), and the name can't be changed after claiming (one tester). Get the details right **before** the claim.

## Gate read and recommendation
Against the gate's bar (match the best on quality AND beat on price or speed), a standalone $49 claim service is weak: the best substitute is free, and the only competitors are unpriced agencies. **Recommendation:** don't open a separate $49 lane now. Make it a fix line inside the GEO audit (already proposed in the GEO benchmark: "Claim your free ChatGPT business profile so your details are correct"). Revisit a paid guided-claim add-on once the GEO audit has a paying buyer.

`offer_check.py` (this folder) fails any offer text that hides that claiming is free, promises placement, asks for the buyer's logins, codes or ID, ties the price to a review or introductions, or leaves out the can't-unpublish warning. Self-tests 9/9.
