# Defensibility analysis

This is the core of the assessment. For each moat, give a score from 0–5, a **durability** rating over 24–36 months (rising, stable or eroding), the evidence behind the score, and what would erode it. A score with no evidence is 0.

| Moat | What to look for |
|---|---|
| Proprietary data and context | Data others can't get; data that compounds with usage through a feedback loop; access that someone else could revoke, such as platform API terms |
| Workflow embedding and switching costs | Whether it's the system of record or a layer on top. Also integration depth, cost to re-implement, number of departments using it, and admin configuration built up over time |
| Network effects | Direct, data, or ecosystem (developers or partners). Name the specific effect, or score 0 |
| Scale economies | Unit costs that fall with scale, such as indexing, inference routing, and R&D spread over more customers |
| Distribution | Owned channels, marketplace positions, co-selling with partners, and brand with the budget owner |
| Counter-positioning | Things incumbents can't copy without hurting their own business, such as being model-neutral or cloud-neutral |
| Trust, compliance and security | Certifications, the permissions model, and on-prem or sovereign deployment. These hold up well in regulated segments |
| Process power and talent | Hard-to-copy capabilities such as rigorous evals, shipping speed and research depth |
| Brand and category ownership | Whether buyers name this company first when they think of the category |

Put the scores into `scripts/score.py moats` to get a sorted table and the average. Show a chart when the output medium supports one.

## Three AI-era tests

Give each test a verdict (passes, mixed or fails) and two or three sentences of reasoning.

1. **Next-model test.** Suppose the next frontier model generation is twice as good at long context, tool use and agents. Does the product become more valuable because it rides the curve, or less valuable because it existed to compensate for weak models?
2. **Lab encroachment test.** Suppose OpenAI, Anthropic or Google ships this as a feature at no extra cost inside their enterprise plans. What share of customers stays, and why?
3. **Bundle test.** Suppose the dominant suite vendor gives away a version that is 70% as good. Which segments and use cases does the company still win?

## Overall rating

Write one paragraph with the overall rating (weak, moderate or strong) and its trend. Name the load-bearing moat, meaning the one that most of the valuation depends on, and the single event most likely to erode it.
