---
tags:
  - kind/pattern
  - source/new
  - source/sillytavern
  - theme/voice-register
  - theme/corpus-building
  - maturity/proven
  - verdict/adopt
created: 2026-06-03
appraised: 2026-06-13
---

# Build the corpus two ways, sorted by difficulty — and findability first

**What it is.** Two non-competing sources for filling the grid:
- **Harvest from play** — for registers the model can already roughly hit. *Clip your hits*:
  when a scene lands, file it into its cell. The corpus grows itself from successes and
  captures your emergent voice for free. The "clip" affordance is a core interaction.
- **Workshop in advance** — for hard registers the model *can't* hit unprompted. Non-optional
  because of a **bootstrapping deadlock**: harvest needs a clipworthy example, but a hard
  register is hard precisely because the model can't produce one to clip. You'd wait forever.
  Hard cells must be hand-seeded.

Advance-authoring gives two things harvest can't: it **defines** the register (you don't know
what "right" is until you've fought to write one clean instance — authoring is discovery),
and it yields a **cleaner, fingerprint-stripped key**.

- **Rewrite-harvested** (the middle gear, added 2026-06-13) — for registers the model
  *roughly* hits but never *cleanly*. Take a real harvested scene and tune it up toward the
  anchor with a strong model, producing a better exemplar than either raw play or
  cold-authoring: harvest supplies the situation, the rewrite supplies the polish you can't
  manage mid-scene. Sits between harvest (clip-as-is) and workshop (hand-seed from nothing).
  **Only safe in this curated layer and only with an explicit anchor present** — otherwise
  the rewrite launders the model's defaults into the bank. See
  [[0113-distill-dont-imitate]] and the layer-contract rule in
  [[0117-distill-vs-verbatim-tension]].

**Findability is the actual first product.** A usable corpus already exists, scattered across
years of past play — just unindexed. Half the win is pure *collect-and-tag*. **Build
retrieval before generation.** **Already realized, loadbearing:** this is exactly what the
current post-processing-after-play does — each session generates the indexed data that feeds
the next. So "retrieval before generation" isn't a proposal here; it's a *proven mechanism to
carry forward*, which is why this note reads `maturity/proven`.

**Where it comes from.** [[sample-book]] §2.

**Why it matters for next-gen.** Directly validates this project's own bias:
index/retrieval before tooling. The "clip from play" affordance is a concrete feature ask.
Pairs with [[0003-scope-memories-to-context]] (tag-on-capture) and the inbox→notes pipeline.

**Open threads.** Which cells are "hard" is model-specific — see
[[0012-intelligence-in-scaffolding]]. Authoring-as-discovery resists automation.

**Verdict.** _adopt._ Retrieval-before-generation is already loadbearing in the current
post-processing pipeline; carry it forward. The three gears (harvest / rewrite-harvested /
workshop) and the bootstrapping-deadlock rationale stand. Difficulty-sorting is what makes a
fixed exemplar:instruction ratio wrong ([[0005-exemplars-over-instructions]]).
