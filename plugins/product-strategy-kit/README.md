# product-strategy-kit (plugin)

This plugin contains one skill, **product-direction-research**. It produces an executive-grade assessment of a company's product direction and defensibility, and it can optionally run a cross-model review with Gemini, GPT or other models through OpenRouter.

Trigger it with a request like "Assess <company>'s product direction and defensibility". You can add a lens (investor, acquirer, operator, competitor or candidate) and the decision you're facing.

Environment variables are optional. They're only needed for the automatic cross-model review:

- `GEMINI_API_KEY`
- `OPENAI_API_KEY`
- `OPENROUTER_API_KEY`
- `GEMINI_MODEL`, `OPENAI_MODEL` and `OPENROUTER_MODELS`, to choose which models run

See the repository README for installation, costs and a sample report.
