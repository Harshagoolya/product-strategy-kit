#!/usr/bin/env python3
"""Deterministic scoring for the product-direction assessment. Standard library only.

Each subcommand reads a JSON file (or '-' for stdin) and prints a Markdown table.

  opportunities  {"weights": {...optional...}, "items": [{"name": str, "demand": 1-5, "fit": .., "revenue": ..,
                  "ease": .., "urgency": .., "moat": ..}]}
  moats          {"items": [{"moat": str, "score": 0-5, "durability": "rising|stable|eroding"}]}
  revenue        {"gross_margin": 0.65, "items": [{"name": str, "accounts": [l,b,h], "adoption": [l,b,h],
                  "arpa": [l,b,h]}  OR  {"name": str, "base": [l,b,h], "delta": [l,b,h]}]}
  scenarios      {"items": [{"name": str, "probability": 0-1, "value": number}]}
"""
import json
import sys

W = {"demand": 0.20, "fit": 0.15, "revenue": 0.20, "ease": 0.10, "urgency": 0.15, "moat": 0.20}


def load(path):
    return json.load(sys.stdin if path == "-" else open(path, encoding="utf-8"))


def money(x):
    if abs(x) >= 1e9:
        return f"${x / 1e9:,.1f}B"
    return f"${x / 1e6:,.1f}M" if abs(x) >= 1e5 else f"${x:,.0f}"


def opportunities(d):
    w = {**W, **d.get("weights", {})}
    if abs(sum(w.values()) - 1) > 1e-6:
        sys.exit(f"weights must sum to 1 (got {sum(w.values()):.3f})")
    rows = []
    for it in d["items"]:
        for k in w:
            if not 1 <= it[k] <= 5:
                sys.exit(f"{it['name']}: {k} must be 1-5")
        rows.append((round(sum(w[k] * it[k] for k in w), 2), it))
    rows.sort(key=lambda r: -r[0])
    cols = list(w)
    print("| # | Opportunity | " + " | ".join(c.title() for c in cols) + " | Priority |")
    print("|---|---|" + "---|" * len(cols) + "---|")
    for i, (p, it) in enumerate(rows, 1):
        print(f"| {i} | {it['name']} | " + " | ".join(str(it[c]) for c in cols) + f" | **{p:.2f}** |")
    print("\nWeights: " + " / ".join(f"{c} {w[c]:.2f}" for c in cols))


def moats(d):
    items = sorted(d["items"], key=lambda x: -x["score"])
    print("| Moat | Score (0-5) | Durability |\n|---|---|---|")
    for it in items:
        print(f"| {it['moat']} | {it['score']} | {it.get('durability', '')} |")
    avg = sum(i["score"] for i in items) / len(items)
    rating = "strong" if avg >= 3.5 else "moderate" if avg >= 2 else "weak"
    print(f"\nAverage {avg:.2f} -> {rating} (the overall rating also weighs the load-bearing moat, not only the mean)")


def revenue(d):
    gm = d.get("gross_margin")
    tot = [0.0, 0.0, 0.0]
    hdr = "| Opportunity | Low | Base | High |" + (" Base (GM-adj.) |" if gm else "")
    print(hdr + "\n|---|---|---|---|" + ("---|" if gm else ""))
    for it in d["items"]:
        if "accounts" in it:
            v = [it["accounts"][i] * it["adoption"][i] * it["arpa"][i] for i in range(3)]
        else:
            v = [it["base"][i] * it["delta"][i] for i in range(3)]
        tot = [t + x for t, x in zip(tot, v)]
        line = f"| {it['name']} | {money(v[0])} | {money(v[1])} | {money(v[2])} |"
        print(line + (f" {money(v[1] * gm)} |" if gm else ""))
    line = f"| **Total (upper bound; overlap)** | **{money(tot[0])}** | **{money(tot[1])}** | **{money(tot[2])}** |"
    print(line + (f" **{money(tot[1] * gm)}** |" if gm else ""))


def scenarios(d):
    s = sum(i["probability"] for i in d["items"])
    if abs(s - 1) > 1e-6:
        sys.exit(f"probabilities must sum to 1 (got {s:.3f})")
    print("| Scenario | Probability | Value |\n|---|---|---|")
    for it in d["items"]:
        print(f"| {it['name']} | {it['probability']:.0%} | {money(it['value'])} |")
    print(f"\nProbability-weighted value: {money(sum(i['probability'] * i['value'] for i in d['items']))}")


if __name__ == "__main__":
    cmds = {"opportunities": opportunities, "moats": moats, "revenue": revenue, "scenarios": scenarios}
    if len(sys.argv) != 3 or sys.argv[1] not in cmds:
        sys.exit(__doc__)
    cmds[sys.argv[1]](load(sys.argv[2]))
