# 10-minute demo script

A live run takes 15–30 minutes, so **kick off the run before the demo starts** and show the finished report alongside it.

## Before the demo (15 minutes of prep)

1. Install the plugin (see the README) and do one warm-up run so every site-access approval has already been granted.
2. Pick a company your audience knows well: a vendor they use, a competitor, or a company where one of them is interviewing. Familiarity is what makes the "is it right?" moment work.
3. About 20 minutes before the demo, start the main run:
   ```
   Assess <Company>, operator lens, decision: where should they place their next bets
   ```
4. Keep a second report ready in case of network problems. The [Glean sample](examples/glean-sample-report.md) works.
5. Optional: set `GEMINI_API_KEY` or `OPENAI_API_KEY` so you can show the cross-model review live. Or prepare the copy-paste packet and have Gemini open in a tab.

## The demo (10 minutes)

| Min | Show | Talking point |
|---|---|---|
| 0–1 | The one-line prompt | "One sentence in. What comes out is the memo a VP of Product would write." |
| 1–3 | **Executive memo**: the thesis, "what you'd have to believe", the CEO questions | "It takes a position and tells you what would change its mind." |
| 3–5 | **Defensibility scorecard** and the three AI-era tests | "Moats scored with evidence. What happens when OpenAI or Microsoft ships this for free?" |
| 5–6 | Architecture diagram and the encroachment map | "It works out which layer holds the value." |
| 6–7 | Voice-of-customer themes and the interview kit | "It admits public forums skew negative, then gives you questions to check it." |
| 7–8 | Opportunities, the revenue model and the leadership charters | "Scored bets, math done in code, a 90-day plan." |
| 8–9 | **Cross-model review table** | "Gemini and GPT argue against the thesis. It checks their evidence before accepting anything." |
| 9–10 | Claims ledger and methodology gaps | "Every load-bearing claim is sourced, and it says what it couldn't see." |

## The audience-participation trick

Ask someone to name a company, and start that run live at the beginning of the demo. Come back to it during Q&A: the first sections will have filled in on screen by then.

## Questions to expect

- **"Is this accurate?"** Point to the claims ledger and the confidence labels. It uses public data only and is only as good as its sources.
- **"How much does it cost?"** It runs on your Claude plan. The cross-model review costs about $1–5 per report on your own API keys, or nothing with copy-paste.
- **"Can I change the framework?"** Yes. Fork the repo and edit `references/defensibility.md` or the scoring weights in `scripts/score.py`.
