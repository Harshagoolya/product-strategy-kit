---
name: product-direction-research
description: Executive-grade assessment of a company's product direction and defensibility (moats, AI-era durability, unit economics, scenarios) from funding, customer, developer and market evidence, with an optional cross-model review by Gemini or GPT. Use when asked to research, assess or pressure-test a company's product strategy, moat, growth opportunities or roadmap.
---

# Product Direction & Defensibility Assessment

Act as a fractional product and strategy advisor working at the level of a VP of Product or CPO at a frontier AI company. Reach a **point of view**; don't write a survey. Answer four questions:

1. Where is this company heading?
2. Will what it's building still be defensible in 24–36 months?
3. What should the reader do about it?
4. What would change your mind?

Everything else in the report is evidence for those four answers.

The deliverable is a report that opens with a one-page memo leading with the answer (BLUF), followed by the evidence. Cite every claim, label every inference, and stress-test the thesis before delivering it.

## Inputs

Arguments are free text, in this order: `<company> [lens] [decision] [focus product] [competitors]`.

- **Company (required).** Resolve it to a domain. If the name is ambiguous, ask once.
- **Lens.** One of:
    - operator/PM (the default)
    - investor
    - acquirer/corp dev
    - partner/BD
    - competitor
    - job candidate
- **Decision.** For example "invest at $X", "partner or build", or "take the Principal PM role". When none is given, use "where should this company place its next bets?" and state that assumption in the memo.
- **Time window.** Default to the last 12 months, and go further back only where history matters (funding rounds, for example).

Always end with a recommendation for the decision.

## Output mode

Pick the richest output the environment supports, and say in one line which one you picked.

1. **Claude Docs**, if the `Claude_Docs` tools are available. Create the doc skeleton FIRST, before any research: the title plus one `pending` block per section. Open it, then fill one section per call.
2. **Otherwise, a Markdown file** named `<company-slug>-assessment-<YYYY-MM-DD>.md` in the working or outputs directory. Write the outline first, then fill it section by section. Keep Mermaid in fenced code blocks, which render on GitHub and in most viewers.
3. If the user asks for Word or PDF, build the Markdown first and then convert it, using the docx or pdf skill if one is available.

Report title: `<Company> — Product Direction & Defensibility Assessment`. Sections:

**Part A — Executive memo** (write last):

1. BLUF: thesis, recommendation, confidence
2. What you'd have to believe
3. Defensibility scorecard
4. Scenarios and leading indicators
5. Questions for the CEO or board

**Part B — Evidence:**

6. Company snapshot, funding and revenue quality
7. Product, stated direction and shipping velocity
8. High-level architecture and where value accrues
9. Market structure and AI value chain
10. Voice of the customer (plus a primary-research kit)
11. Developer and ecosystem signal
12. Competitive landscape and encroachment map
13. Unit economics and AI cost structure
14. Team, execution and GTM engine
15. Growth opportunities (scored)
16. Partnerships and strategic options (including M&A)
17. Revenue impact model
18. Leadership charters (Principal PM by default)
19. Risks, red-team and cross-model critique, open questions
20. Sources, methodology and claims ledger

Post short progress lines in chat as you work, such as "Funding done; now customer feedback". Findings go in the report, not in chat.

## Workflow

1. **Research.** Follow `references/research-playbook.md` for sections 6–14. Open primary sources: press releases, filings, docs and changelogs. Never cite a search snippet. Cross-check every load-bearing number against a second source.
    - When a fetch is blocked (it needs approval, is rate-limited, or the domain is unreachable), list the blocked URLs once in chat. Then fall back to web search and record the gap in the Methodology section.
2. **Defensibility.** Score the moats and run the three AI-era tests in `references/defensibility.md`. This is the core of the assessment.
3. **Synthesis.** Build the opportunities, partnerships, revenue model and charters using `references/synthesis.md`. Compute every score and scenario with `scripts/score.py`; never do the arithmetic in your head.
4. **Stress test.**
    - Run the red team and pre-mortem, and build the scenarios, from `references/synthesis.md`.
    - Then run the optional **cross-model review** in `references/cross-model-review.md`. Offer it in one line. Run it through the APIs if keys are present, or produce the copy-paste challenge packet if not.
5. **Memo.** Write Part A last. Keep it to one page.
6. **Quality check.** Apply `references/quality-bar.md` before delivering, including the claims ledger.

## Executive memo (Part A)

- **BLUF:** the thesis in two sentences, the recommendation for the reader's decision, and your confidence (high, medium or low).
- **What you'd have to believe:** the 3–5 assumptions the recommendation depends on. For each, give the current evidence and your confidence.
- **Defensibility scorecard:** the moat table in brief, the verdicts on the three AI-era tests, and an overall rating (weak, moderate or strong) with its trend.
- **Top 3 opportunities and top 2 partnerships,** with the base-case revenue for each.
- **Scenarios:** bull, base and bear, with probabilities and the leading indicators to watch.
- **Cross-model verdict,** if the review was run: where the other models agreed and where they disagreed.
- **Questions for the CEO or board:** the 5 whose answers would move the thesis most.

Tailor the memo to the lens:

- **Investor:** entry valuation against the scenarios, and what would make you pass.
- **Acquirer:** strategic fit, integration risk, and a price range from comparable deals.
- **Operator:** the roadmap and leadership charters.
- **Competitor:** the gaps to attack and the moats to avoid.
- **Candidate:** how much leverage the role has, the company's trajectory, and any red flags.

## Finish

End in chat with:

- one line giving the recommendation and the #1 risk to the company's moat
- the link to the doc, or the file path
- any blocked fetches that are worth approving before a re-run

Then offer, in one line, a monthly refresh that compares against the last run and reports movement on the leading indicators.

State once, in the report footer, that it draws only on public sources and is not investment advice.
