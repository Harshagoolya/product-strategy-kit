# Research playbook (report sections 6–14)

Open primary sources. Cross-check ARR, valuation, rounds and customer counts against a second source, because aggregators often mislabel rounds and dates. Label every figure **disclosed**, **estimated** or **unknown**.

## 6. Funding and revenue quality

- **Rounds:** for each round, give the date, amount, leads, valuation and stated use of funds. Quote the use-of-funds language. Note strategic and corporate investors, who are often partnership candidates.
- **Revenue:** the trajectory with dates. Separate contracted ARR from annualized run-rate and consumption revenue.
- **Multiples:** valuation divided by ARR, compared with public comps and recent private rounds in the category.
- **Capital efficiency:** total raised divided by ARR. Estimate a burn multiple where headcount allows (headcount × loaded cost − revenue).
- **Liquidity path:** IPO readiness signals, secondaries and tender offers, and flat-round or down-round risk.
- **Public companies:** use the latest 10-K and 10-Q and earnings-call commentary.

## 7. Product direction and shipping velocity

- **Launches:** a table of launches over the last 12 months, newest first, with columns Date | Launch | What it signals.
- **Velocity:** releases per month from the changelog, and whether the pace is rising or falling.
- **Pricing and packaging:** the model (seat, consumption or hybrid), whether prices are public, and any changes. Use third-party buyer data (Vendr, buyer guides) for ACV and discounting.
- **Leadership statements:** what the CEO and CPO say about strategy compared with what the company actually ships. Flag mismatches.
- **Hiring:** open roles by function and geography, and new product areas. Job boards: Greenhouse, Lever, Ashby.

## 8. Architecture and where value accrues

Reconstruct the product's architecture from:

- docs: how it works, deployment, security, connectors, API reference
- engineering blogs
- the developer portal
- trust and security pages
- job descriptions, which reveal the stack

Deliver:

- **A Mermaid `flowchart TD`** of at most ~15 nodes, flowing from sources → data or context layer → intelligence (models, ranking, agents) → governance → surfaces and APIs. Add one sentence explaining how to read it.
- **A layer table:** Layer | Function | Proprietary or commodity | Source.
- **Deployment model:** multi-tenant SaaS, single-tenant, customer cloud, or on-prem, and where data and model calls live.
- **Value-accrual read (inference):**
    - which layer holds the moat
    - which layers become commodities as models improve
    - which dependencies (model provider, data owner, cloud) could squeeze margin or access

Label anything not stated publicly as inferred.

## 9. Market structure and AI value chain

- **TAM/SAM:** bottom-up (target accounts × realistic ACV) with a top-down cross-check. Show the math.
- **Budget owner:** who pays (CIO, CISO, line of business, engineering), and whether that budget is growing or being consolidated.
- **Value-chain position:** where the company sits in the chain (chips → cloud → models → infra and tools → apps → services), who captures margin at each layer, and where margin is moving.
- **Bundling threat:** which platforms can bundle this capability at near-zero marginal price. Candidates include Microsoft, Google, Salesforce, Atlassian, ServiceNow and the frontier labs.
- **Standards and protocol shifts:** for example MCP, agent-to-agent protocols and open-weight models. Say whether each one strengthens or weakens the company's position.

## 10. Voice of the customer

**Reddit.** Search with `site:reddit.com "<company>"`, `"<product>" alternative`, `"<product>" vs`, `"switched from <product>"` and `"<product>" pricing`. If WebFetch can reach it, use the JSON endpoint: `https://www.reddit.com/search.json?q=<company>&sort=relevance&t=year&limit=100`. Read the comments, not only the post titles.

**Hacker News.** Use `https://hn.algolia.com/api/v1/search?query=<company>&tags=comment` and `tags=story`. Ignore unrelated uses of the company's name.

**Reviews and forums:** G2 pros-and-cons pages, AWS/Azure/GCP marketplace reviews, Capterra, TrustRadius, Blind, community forums and Product Hunt.

Build a theme table with columns Theme | Type | Mentions | Intensity | Segment | Trend | Evidence (2–3 short quotes, with links). Types are pain point, feature request, praise, churn reason and competitor comparison.

Public forums over-represent unhappy customers and smaller organizations. Say so in the report, and weight the evidence accordingly.

**Primary-research kit.** Public data isn't enough for a VP-level call, so give the reader questions for their own interviews:

- 8–10 for current customers
- 5 for churned customers and competitors' customers
- 5 for former employees
- win/loss hypotheses to test

## 11. Developer and ecosystem signal

- **GitHub:** repos, stars and star velocity, archived or deprecated repos, the issues with the most reactions (`/search/issues?q=repo:<org>/<repo>+is:issue+is:open&sort=reactions-+1`), and release cadence. If the API is blocked, read the github.com pages and the developer changelog instead.
- **Ecosystem depth:** third-party integrations, marketplace listings, ISVs building on the platform, and community size. Say whether an ecosystem is actually forming or is only partner logos.
- **If the company isn't developer-facing:** say that the signal comes from what it ships, not from community issues.

## 12. Competition and encroachment

- **Competitor table:** 3–6 direct competitors, bundled platform offerings, frontier-lab offerings and open-source alternatives. Columns: positioning, price, recent moves (including M&A), and where each wins or loses against the target.
- **Encroachment map:** for each of the target's top 5 capabilities:
    - Is a frontier lab or suite vendor already shipping it, announcing it, or likely to ship it within 12 months?
    - How good is their "good enough" version?
    - What does the target keep if that happens?

## 13. Unit economics and AI cost structure

- **Gross margin:** estimate it under the current model mix. Benchmarks: SaaS runs about 75–80%, and AI applications often 50–65%. Inference costs, model pass-through and customer-cloud hosting all drag margin.
- **Pricing power:** list price vs. negotiated discount, and pressure from bundled offerings. Say whether seat pricing can survive as agents replace seats.
- **Model cost curve:** say whether falling token prices widen the company's margin (because it resells capability) or erode its value (because it existed to work around model limits).
- **Retention and efficiency:** NRR, GRR, CAC payback and sales-cycle length from disclosures, interviews or analysts. Label each figure disclosed, estimated or unknown.

## 14. Team, execution and GTM engine

- **Leadership:** founders' and leaders' pedigree, executive hires and departures (especially CPO, CTO, CRO and CFO), and board composition.
- **Morale:** Glassdoor and Blind trends, and signs of layoffs, hiring freezes or an "AI-washing" pivot.
- **GTM motion:** product-led vs. sales-led, evidence of land-and-expand, share of sales through channels and marketplaces, and international footprint.
- **Execution scorecard:** sample what the company announced 12 months ago and check what is live today.
