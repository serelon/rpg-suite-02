---
tags:
  - kind/pattern
  - source/aegis-tools
  - theme/architecture
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-05
---

# Fog-of-war as data structure — observed/actual splits and hidden thresholds

**What it is.** aegis-tools' intel codex and rumor engine encode *incomplete knowledge*
directly in the data:

- **Observed/actual split.** Every enemy/UFO entry has an `observed` block (what the
  player has seen — accumulating prose field-notes) and an `actual` block (true stats,
  shown only via `--actual` or once research earns it). **Field-name whitelists** enforce
  the boundary: `ALLOWED_OBSERVED` vs `ALLOWED_ACTUAL` — you cannot typo a secret into the
  visible side, and unknown fields error loudly instead of silently corrupting.
- **Hidden randomized thresholds.** A rumor's difficulty is rolled at creation
  (`random.randint` within its grade's range), **stored in the entity but never
  displayed**. No metagaming ("exactly 2 more successes"), no mid-investigation GM
  fudging (it's immutable), still auditable in raw JSON.
- **Encounter log as knowledge ledger.** `encounters[]` per enemy tracks not kills but
  *discovery milestones* — observed notes accumulate per session like an investigation
  journal ("Body shots slow but don't stop" → "Headshots required" → "TACTICAL: adapted
  overnight…").

**Where it comes from.** `aegis-tools/intel.py` + `modules/intel/` +
`modules/strategic/intel/` (Explore sweep 2026-06-05); live data in
`solorpg/campaigns/aegis/intel/`.

**Why it matters for next-gen.** This is **lenses with stakes** — the same entity at
different *knowledge levels*, not just different zooms ([[0068-multi-lens-data]] adds an
epistemics axis: what the reader is *allowed* to know, not just how much detail they
want). For a GM-led solo system the use-case is direct: the GM model needs the actual
block, the player-facing narration only the observed one — a KB
([[0067-campaign-data-as-linked-vault]]) whose pages carry visibility-scoped blocks could
serve both without two documents drifting apart. Also the second strong showing for
**validation-at-write** (with [[0070-threads-tracker-design]]): whitelists and write-time
errors are cheap and the live data stayed clean.

**Open threads.** Do solo narrative campaigns want mechanical fog-of-war, or is the
pattern's value there purely "GM-secrets vs player-knowledge" page scoping? Hidden-but-
auditable (in-file but undisplayed) only works while the player doesn't read the raw KB —
for solo play where user == player == co-author, is the discipline boundary enough (it was
for aegis)?

**Verdict.** _(unevaluated.)_
