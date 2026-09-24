# Product Strategy Kit

**Give Claude a company name and get back an executive-level assessment:** where the product is heading, whether it can defend its position, and what to do about it.

It is built for product leaders, PMs, investors and job candidates who want more than a list of search results. It reaches a point of view, stress-tests that view, and optionally has **Gemini or GPT argue against it**.

> See a sample: [Glean assessment](examples/glean-sample-report.md). That sample was produced by an early version; the current version adds the defensibility scorecard, AI-era tests and scenarios.

## What you get

A report with a one-page memo up front, followed by the evidence:

| Part | What's inside |
|---|---|
| **Executive memo** | Thesis and recommendation for *your* decision, confidence, the assumptions it depends on, defensibility scorecard, bull/base/bear scenarios with leading indicators, and 5 questions for the CEO or board |
| **Company and funding** | Rounds, investors, use of funds, ARR trajectory, revenue quality, and valuation multiples |
| **Product and architecture** | Launch timeline, shipping velocity, pricing, a Mermaid architecture diagram, and which layer holds the value |
| **Market and competition** | Bottom-up market size, position in the AI value chain, bundling threats, and an encroachment map (what the frontier labs and suite vendors could take) |
| **Customer and developer signal** | Themes from Reddit, Hacker News, G2 and marketplace reviews, plus GitHub and ecosystem signal and a question kit for your own customer interviews |
| **Defensibility** | 9 moats scored 0–5 with durability, plus three AI-era tests: the next-model test, the lab-encroachment test, and the bundle test |
| **Opportunities** | Growth bets scored on six dimensions (including moat contribution), partnerships, M&A options, and a low/base/high revenue model |
| **Leadership charters** | 4–5 charters a Principal PM or VP could own, with a 90-day plan |
| **Stress test** | A red-team pass, a pre-mortem, an optional cross-model critique, and a claims ledger |

Your lens changes the framing: operator/PM (the default), investor, acquirer, partner/BD, competitor, or job candidate.

## Install

### Claude Code

```
/plugin marketplace add <your-github-username>/product-strategy-kit
/plugin install product-strategy-kit@product-strategy-kit
```

### Claude desktop app (Cowork)

Download `product-strategy-kit.plugin` from the [latest release](../../releases/latest) and open it in the app to install the plugin. If your app version supports adding plugin marketplaces from GitHub, you can add this repo instead.

### claude.ai (web)

1. Download `product-direction-research.zip` from the [latest release](../../releases/latest).
2. Go to **Customize → Skills** and upload the ZIP.
3. Make sure code execution is enabled in your settings. Skills need it.

### Other agents

The skill follows the open Agent Skills format (a `SKILL.md` file plus references and scripts). Any agent that supports that format can load `plugins/product-strategy-kit/skills/product-direction-research/`.

## Use it

Just ask:

```
Assess Figma's product direction and defensibility
Assess Glean, investor lens, decision: invest at a $7B valuation
Assess Linear as a job candidate for a Principal PM role
Assess Notion vs. Coda and ClickUp, competitor lens
```

A full run takes roughly **15–30 minutes**. The agent researches the web live, and on some setups it asks you to approve fetches from sites like Reddit, GitHub or Hacker News. Approve them for better coverage.

In the Claude apps, the report is a live Claude Doc that you can edit, comment on and share. Elsewhere it's a Markdown file.

## Optional: cross-model review (Gemini, GPT and others)

After the analysis, the agent can ask other models to attack the thesis. Where the models disagree is usually where the analysis is weakest. The agent checks each critique's evidence, then accepts or rejects it in a table shown in the report.

There are two ways to run it:

- **Automatic.** Set one or more keys where the agent runs:
  ```bash
  export GEMINI_API_KEY=...       # Google AI Studio
  export OPENAI_API_KEY=...
  export OPENROUTER_API_KEY=...   # one key for many models
  # optional overrides:
  export GEMINI_MODEL=... OPENAI_MODEL=... OPENROUTER_MODELS="google/...,openai/..."
  ```
  Expected cost is about **$1–5 per report**, billed to your own API accounts. Model prices change, so check your providers. Gemini's free tier works for occasional use. Some sandboxed environments block these APIs; if that happens, the agent falls back to copy-paste.
- **Copy-paste (no setup).** The agent writes a `challenge-packet.md`. Paste it into Gemini (Deep Research works well) or ChatGPT, then paste the JSON reply back to the agent.

Never paste API keys into the chat.

## Repo layout

```
.claude-plugin/marketplace.json          # makes this repo a plugin marketplace
plugins/product-strategy-kit/
  .claude-plugin/plugin.json
  skills/product-direction-research/
    SKILL.md                             # workflow and memo format
    references/                          # research playbook, defensibility, synthesis, cross-model, quality bar
    scripts/score.py                     # deterministic scoring and revenue math
    scripts/cross_model_review.py        # Gemini / OpenAI / OpenRouter critiques (stdlib only)
examples/glean-sample-report.md
DEMO.md                                  # a 10-minute demo script
build.sh                                 # builds the release ZIP and .plugin files
```

## Limits and honesty

- It uses public sources only, and it labels every estimate. It is **not investment advice**.
- Customer sentiment from public forums skews negative and toward smaller companies. The report says so and gives you interview questions to check it.
- Private-company figures (customer counts, NRR, margins) are usually estimated and labeled that way.
- Vendor-run benchmarks are marked unverified.

## Contributing

Issues and PRs are welcome, especially ones that add sources, sharpen the moat rubric, or share sample reports (with the company name and any non-public information removed if needed).

## License

MIT
