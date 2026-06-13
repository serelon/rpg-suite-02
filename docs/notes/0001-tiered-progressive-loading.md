---
tags:
  - kind/pattern
  - source/rpg-tools
  - source/solorpg
  - theme/context-economy
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# Tiered / progressive loading to protect the context budget

**What it is.** Campaign data tools expose data in tiers instead of dumping everything:
`list` (names only) → `list --short` (minimal profile: role + essence + voice) →
`get NAME` (minimal) → `get NAME --depth full` / `--section powers`. The reader pulls
only the depth the current scene needs.

**Where it comes from.** `rpg-tools/scripts/characters.py` and `locations.py`; documented
in both `rpg-tools/CLAUDE.md` ("Tiered data loading") and `solorpg/CLAUDE.md`
("Character Loading (Incremental)").

**Why it matters for next-gen.** Context economy is the recurring constraint across every
source repo — a long campaign's data vastly exceeds a usable context window. This is the
proven answer at the *tool* layer: progressive disclosure driven by the caller. Any
next-gen retrieval design has to preserve this, not regress to frontloading.

**Confirmed in another domain (2026-06-13).** The import design brief
([[import-design-brief]]) independently reinvents this as a **tier pyramid for *processing*
cost**, not just read cost: regex on name → embed + k-NN → local LLM → Claude, each tier
seeing only the residue the cheaper tier couldn't resolve. Same shape — cheapest engine
first, escalate only the trickle — applied to classification instead of context loading.
Evidence the "narrow cost at each step" principle generalizes beyond the read path.

**Open threads.** This is pull-based and manual (the model decides what to load). The
`old-erpg` answer was push-based retrieval (vector search over chunks). How do tiered
loading and semantic retrieval combine rather than compete? See
[[0002-read-anywhere-write-canonical]] for the sibling data-access pattern.
