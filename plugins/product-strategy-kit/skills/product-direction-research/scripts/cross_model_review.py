#!/usr/bin/env python3
"""Send a challenge packet to other frontier models and collect structured critiques.

Standard library only. Reads API keys from environment variables and never logs them.

  GEMINI_API_KEY      -> Google Gemini API, with Google Search grounding
  OPENAI_API_KEY      -> OpenAI Responses API, with the web_search tool
  OPENROUTER_API_KEY  -> any models listed in OPENROUTER_MODELS (comma-separated)

Override models with GEMINI_MODEL, OPENAI_MODEL and OPENROUTER_MODELS. Model names
change often; check each provider's model list if a call fails.

Usage:
  python3 cross_model_review.py --packet challenge-packet.md --out critiques.json
  python3 cross_model_review.py --packet challenge-packet.md --dry-run
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

DEFAULTS = {
    "gemini": os.environ.get("GEMINI_MODEL", "gemini-3.1-pro"),
    "openai": os.environ.get("OPENAI_MODEL", "gpt-6-sol"),
    "openrouter": os.environ.get("OPENROUTER_MODELS", "google/gemini-3.1-pro,openai/gpt-6-sol"),
}
KEYS = {"gemini": "GEMINI_API_KEY", "openai": "OPENAI_API_KEY", "openrouter": "OPENROUTER_API_KEY"}
TIMEOUT = int(os.environ.get("CROSS_MODEL_TIMEOUT", "300"))


def _post(url, headers, body):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return json.loads(r.read().decode())


def call_gemini(packet, model, key):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    body = {"contents": [{"role": "user", "parts": [{"text": packet}]}], "tools": [{"google_search": {}}]}
    data = _post(url, {"Content-Type": "application/json", "x-goog-api-key": key}, body)
    parts = data.get("candidates", [{}])[0].get("content", {}).get("parts", [])
    return "".join(p.get("text", "") for p in parts)


def call_openai(packet, model, key):
    body = {"model": model, "input": packet, "tools": [{"type": "web_search"}]}
    data = _post("https://api.openai.com/v1/responses",
                 {"Content-Type": "application/json", "Authorization": f"Bearer {key}"}, body)
    if data.get("output_text"):
        return data["output_text"]
    out = []
    for item in data.get("output", []):
        if item.get("type") == "message":
            out += [c.get("text", "") for c in item.get("content", []) if c.get("type") == "output_text"]
    return "".join(out)


def call_openrouter(packet, model, key):
    body = {"model": model, "messages": [{"role": "user", "content": packet}],
            "plugins": [{"id": "web"}]}
    data = _post("https://openrouter.ai/api/v1/chat/completions",
                 {"Content-Type": "application/json", "Authorization": f"Bearer {key}"}, body)
    return data["choices"][0]["message"]["content"]


def parse_json(text):
    """Pull the first JSON object out of a model reply (handles code fences and chatter)."""
    fence = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.S)
    candidates = [fence.group(1)] if fence else []
    start, end = text.find("{"), text.rfind("}")
    if start != -1 and end > start:
        candidates.append(text[start:end + 1])
    for c in candidates:
        try:
            return json.loads(c)
        except json.JSONDecodeError:
            continue
    return None


def plan(providers):
    jobs = []
    for p in providers:
        key = os.environ.get(KEYS[p])
        if not key:
            continue
        models = [m.strip() for m in DEFAULTS[p].split(",") if m.strip()]
        jobs += [(p, m, key) for m in models]
    return jobs


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--packet", required=True, help="Path to challenge-packet.md")
    ap.add_argument("--out", default="critiques.json")
    ap.add_argument("--providers", default="gemini,openai,openrouter")
    ap.add_argument("--dry-run", action="store_true", help="Show which models would run; make no calls")
    a = ap.parse_args()

    packet = open(a.packet, encoding="utf-8").read()
    providers = [p.strip() for p in a.providers.split(",") if p.strip() in KEYS]
    jobs = plan(providers)
    if not jobs:
        print("NO_KEYS: set GEMINI_API_KEY, OPENAI_API_KEY or OPENROUTER_API_KEY "
              "(or use the copy-paste packet).", file=sys.stderr)
        sys.exit(2)
    if a.dry_run:
        for p, m, _ in jobs:
            print(f"would call {p}:{m} ({len(packet):,} chars)")
        return

    callers = {"gemini": call_gemini, "openai": call_openai, "openrouter": call_openrouter}
    results = []
    for p, m, key in jobs:
        rec = {"provider": p, "model": m}
        try:
            raw = callers[p](packet, m, key)
            rec["critique"] = parse_json(raw)
            rec["status"] = "ok" if rec["critique"] else "unparsed"
            if not rec["critique"]:
                rec["raw"] = raw[:20000]
        except urllib.error.HTTPError as e:
            rec["status"] = f"http_{e.code}"
            rec["error"] = e.read().decode(errors="replace")[:2000]
        except Exception as e:  # network blocked, timeout, schema change
            rec["status"] = "error"
            rec["error"] = f"{type(e).__name__}: {e}"[:2000]
        print(f"{p}:{m} -> {rec['status']}", file=sys.stderr)
        results.append(rec)

    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"wrote {a.out}")
    if not any(r["status"] == "ok" for r in results):
        sys.exit(1)


if __name__ == "__main__":
    main()
