# Synthesis and stress test (report sections 15–19 and memo inputs)

## 15. Growth opportunities

- Every opportunity needs **at least two independent signals**. For example, a customer theme plus a hiring pattern, or a use-of-funds statement plus a launch.
- Give each one:
    - a one-line statement
    - its type: new feature, fixing a churn driver, new segment, packaging/pricing, platform/API, or geographic
    - the target segment
    - the evidence, with links
    - whether it aligns with the company's stated direction
- Score each on six dimensions from 1–5: Demand, Fit, Revenue, Ease, Urgency, and **Moat**. Moat asks whether the opportunity deepens defensibility or only adds revenue. The default weights are 0.20 / 0.15 / 0.20 / 0.10 / 0.15 / 0.20.
- Compute the scores with `scripts/score.py opportunities`, and sort by priority.
- Flag the **blind spot**: something customers clearly want that the company isn't signaling it will build.

## 16. Partnerships and strategic options

- **Partner table:** Partner | Type (integration, co-sell, OEM, marketplace or distribution) | Mutual value | Evidence | Effort | Dependency risk.
- **Where to look:**
    - integrations users keep asking for
    - tools that appear alongside the company's in the same threads or GitHub stacks
    - strategic investors, and portfolio companies of the same investors
    - cloud marketplaces
    - systems integrators
    - model providers
- **Partners to avoid depending on:** partners who own a critical data source or channel and could restrict access.
- **Strategic options:**
    - build, buy or partner for each top gap
    - acquisition targets that would deepen the moat
    - likely acquirers of the company, with the strategic logic for each
    - the case for selling vs. staying independent

## 17. Revenue impact model

Use one of these for each opportunity:

```
Impact = addressable accounts × adoption × ΔARPA
Impact = ARR base × Δretention
```

- Model the top 3–5 opportunities with low, base and high cases, the time to impact in quarters, and a **gross-margin-adjusted** version.
- State every assumption and its source (disclosed, pricing page, comparables, analyst). Name the weakest assumption.
- Compute everything with `scripts/score.py revenue`.
- Note where opportunities overlap, and treat the totals as upper bounds.
- Label all of it as estimates.

## 18. Leadership charters

- Write 4–5 charters sized to the role. Principal PM is the default; use VP level if the lens is an executive hire.
- Put them in a table: Charter | Problem | Key bets | North-star metric | Guardrails | Linked opportunity (number and priority).
- Lead with the charter that has the most leverage, and say why.
- For the top charter, give a 90-day plan in three phases:
    - **Days 0–30, discover:** instrumentation, customer interviews, cost to serve.
    - **Days 31–60, define:** PRD, pricing, partner alignment.
    - **Days 61–90, ship and decide:** design partners, a dashboard, a go/no-go decision.
- Note which executive decisions would unblock it.

## 19. Stress test

Do all of this before writing the memo.

1. **Red team.** If the Agent tool is available, spawn a subagent. Give it the draft thesis, the defensibility scores and the key evidence, with this brief: "Argue the strongest case that this thesis is wrong. Search the web for disconfirming evidence. Return the top 5 objections, each with evidence URLs and severity." If no Agent tool is available, do a separate adversarial pass yourself. For each objection, either incorporate it or rebut it.
2. **Cross-model review (optional).** See `cross-model-review.md`.
3. **Pre-mortem.** Imagine it is two years from now and the company has failed or been acquired cheaply. Name the top three causes.
4. **Scenarios.** Write bull, base and bear cases over 24–36 months. Give each a rough probability (the three sum to 100%), its drivers, and 2–3 **leading indicators**: observable events that would tell you which scenario is unfolding. Compute probability-weighted values with `scripts/score.py scenarios` when you have values to weight.
5. **What you'd have to believe.** List the 3–5 assumptions the recommendation rests on, with the evidence and confidence for each.
