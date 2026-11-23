# Business Hub Claim (ChatGPT) — Benchmark (Quality Gate step 1)

**Status:** Claude's draft, 2026-11-23 11:25 UTC run; corrected 16:25 UTC after Atlas's review (Fiverr gig exists; "free for now"; OpenAI's own wording). Step 1 is Grok's job. It was assigned at 09:25 UTC, and no Grok work on it was found in either repo by 11:25, so Claude drafted it the same way as the GEO, Resume and Spanish benchmarks. **Atlas: re-open every source. Claude's sources are third-party;** Atlas opened OpenAI's help article on Nov 23 and confirmed the core facts in OpenAI's own words (rows marked "per Atlas").

Pages read 2026-11-23 ~11:30 UTC. **LocalIQ** (localiq.com/blog/businesses-in-chatgpt) returned a bot-check page and was not read.

## What it is (facts that shape the offer)
| Fact | Quote | Source |
|---|---|---|
| Launched in beta Nov 10, 2026 | "Beta since Nov 10" (page's facts checked Nov 12) | getpassionfruit.com/lp/businesses-in-chatgpt |
| **Claiming costs nothing — for now.** OpenAI's pages list no fee; OpenAI's VP of monetization told Digiday it is "free for now" and didn't rule out paying later (per Atlas; Digiday: digiday.com/marketing/openais-new-business-agents-give-brands-a-free-way-into-the-conversation) | "It's free and takes minutes." / "OpenAI doesn't list a fee for claiming a business." | eesel.ai/blog/how-to-claim-your-business-on-chatgpt |
| | "We weren't asked to pay." | rankability.com/blog/how-to-claim-your-business-in-chatgpt |
| **Claiming doesn't change placement** | OpenAI's own help article (help.openai.com/en/articles/20001635, opened by Atlas Nov 23): "Claiming a profile or disputing ownership doesn't change its visibility in ChatGPT." Passionfruit's version (Atlas did not find this exact sentence on OpenAI's page): "ChatGPT continues to make independent recommendations and comparisons. Claiming does not guarantee higher placement or sales." | getpassionfruit.com (only verbatim quote found) |
| **The owner must verify, in person** | Business phone, business email, DNS TXT record or Shopify; then a Persona ID check that gates edits, insights and the blue check | eesel.ai; sqspthemes.com ("Persona is required before it can update information or access analytics"); rankability.com (DNS + email + SMS + ID scan with facial recognition) |
| **Local shops can only claim an existing US listing** | Local stores and restaurants "can only claim an existing US listing." | eesel.ai; sqspthemes.com ("can currently claim only existing U.S. listings") |
| **Can't be taken down once published** (OpenAI's own words, per Atlas: "OpenAI Support is unable to delete, unpublish, or hide a published profile") | A Persona-approved new profile "publishes automatically", and OpenAI Support "can't delete, unpublish or hide a published profile." | eesel.ai |
| Name can't be edited after claiming (one tester) | Business name not editable in any of the editor's five tabs | rankability.com |
| Business Agents | US e-commerce or online-service businesses with a website only | eesel.ai, passionfruit, sqspthemes, upgrowth.in |

## Who sells it now
| Who | Price | What's included | Delivery | Source |
|---|---|---|---|---|
| **upGrowth** (agency, India) | **No price shown**: "quoted after a 30-minute call" | "Readiness Sprint": 20-prompt baseline, audit of up to 10 listings, schema for up to 5 offerings, profile copy with up to 2 revision rounds, agent context pack | Not shown | upgrowth.in/chatgpt-business-hub-agency-india |
| **Passionfruit** (agency) | **No price shown**: "custom pricing: after a strategy call we share a proposal" | Claim and verify "from an account you control", product connection, agent build, monthly insights review, content brief | Not shown | getpassionfruit.com/lp/businesses-in-chatgpt |
| **Rankability** (AEO agency) | No claim price; "Book a strategy call" | General AEO services | Not shown | rankability.com |
| **Free how-to guides** | **$0** | Step-by-step claim guides: eesel, Rankability, B12, findskill.ai, gauravtiwari.org and others | Instant | search results 2026-11-23 |
| **Jafir_digital**, Fiverr: "I will create your business profile on chatgpt to get ai recommendations" | **$15–$80** (found by Atlas, Nov 23; not re-opened by Claude, whose own two searches missed it) | Not read | Not read | Atlas review on PR #53 |
| Other Fiverr "ChatGPT visibility" gigs (adjacent, not claim-specific), e.g. hcroft42 "improve your visibility on chatgpt and ai search" | Not read | — | — | web search, 2026-11-23 |

## What buyers complain about (evidence)
**Honest gap: no buyer review of a paid claiming service was found** (the Fiverr gig's reviews were not read). The service is 13 days old. What owners report about **claiming itself** (eesel's troubleshooting section, Rankability's test):
1. DNS TXT checks fail on a trailing dot or an auto-added host name.
2. Persona ID checks fail or expire.
3. "Listing is locked" with only "Contact support."
4. Saved changes don't show in answers right away.
5. Published profiles can't be unpublished; the name can't be edited after claiming.
6. upGrowth's own claim ended on a waitlist, and ChatGPT showed three lookalike firms for its name.

## Our offer against this (honest)
- **We can't do it for them, and must not try.** Verification is the owner's own phone, email, domain and face. Taking a client's logins, codes or ID photo would break our hard rules (no credentials) and likely OpenAI's. Any offer is a **guided claim**: we prepare everything, the owner taps the verification steps.
- **"Done-for-you" claims are free to do yourself.** A $49 fee is only fair if the buyer gets something a free guide doesn't: correct, sourced profile copy, the before/after of what ChatGPT says about them, and a fix for complaints 1–5 above (we check their DNS record format and listing before they start).
- **Price:** agencies hide prices behind a call, but **a Fiverr seller already posts $15–$80** for setting up the profile, which brackets our $49 idea. We can't claim to be cheaper.
- **Speed:** unknown for everyone; OpenAI publishes no review time.
- **Placement:** we can never say it gets them recommended more. OpenAI says it doesn't.
- **Risk to say up front:** once published, the profile can't be taken down (OpenAI's help article, per Atlas), and the name can't be changed after claiming (one tester). Get the details right **before** the claim.

## Gate read and recommendation
Against the gate's bar (match the best on quality AND beat on price or speed), a standalone $49 claim service is weak: the best substitute is free (for now), and a Fiverr seller already sells it from $15. **Recommendation:** don't open a separate $49 lane now. Make it a fix line inside the GEO audit (already proposed in the GEO benchmark: "Claim your free ChatGPT business profile so your details are correct"). Revisit a paid guided-claim add-on once the GEO audit has a paying buyer.

`offer_check.py` (this folder) fails any offer text that hides that claiming is free, promises placement, asks for the buyer's logins, codes or ID, ties the price to a review or introductions, or leaves out the can't-unpublish warning. Self-tests 9/9.
