---
tags:
  - kind/question
  - source/conversation
  - theme/context-economy
  - maturity/speculative
  - verdict/adapt
created: 2026-06-06
---

# Context injection vs cache economics — scheduling mutations for the cache

**What it is.** A [[0074-project-unicorn]] design tension (user, 2026-06-06): "ST-style
context engineering, vs modern cache algorithms. we'll need to be smart about it, schedule
mutations in a way thats optimized for caching."

The doctrines fight: SillyTavern-style context engineering **rebuilds the prompt each
turn** — lorebook entries swap in and out mid-prompt by keyword — while prefix caching
makes every token *after the first changed byte* a cache miss. Naive ST-style injection
pays full input price every turn; naive static context wastes the window on unused lore.

**Reconciliation sketch (captured, not decided).**
- **Layout by volatility:** stable layers (system/persona/setting canon) at the front,
  volatile injections at the tail, never interleaved.
- **Mutations batched to natural boundaries:** mid-scene, only *append* (cache-friendly by
  definition — extends the prefix); at a boundary, pay one deliberate re-layout
  (drop stale injections, promote new canon, re-sort).
- This is the **same boundary problem as [[0075-postprocessing-as-vault-librarian]]'s
  scene-by-scene streaming** — scene breaks double as cache-flush points. One boundary
  detector, two payoffs (librarian condensation + context re-layout).
- Echoes [[0073-structured-mutation-beats-rewrite]] at the prompt layer: append/patch the
  context, don't regenerate it.

**Why it matters for next-gen.** Token cost is a first-order constraint for a client meant
for long-running play ("we'll run out of steam/tokens" is Unicorn's named failure mode —
cache discipline literally extends Unicorn's life expectancy). But
[[0031-beware-transient-constraint-architecture]] looms: cache TTLs, pricing, and
mechanics are *provider/era variables*. So cache-scheduling belongs in the **presentation
consumer** ([[0069-one-knowledge-base-many-presentation-layers]]), never baked into the
KB's shape — when cache economics change, only the consumer's scheduler updates.

**Open threads.** What's the volatility taxonomy for RP context (canon < active-scene
lore < live state < last-N-turns)? Do keyword-RAG injections go in the tail every turn or
only at boundaries (latency vs freshness)? Measure: what does a typical session's
cache-hit profile look like under each policy — can be simulated from existing session
transcripts ([[0064-unharvested-archive]] as test corpus again)?

**Verdict.** **Adapt** (appraised 2026-06-06). The cache-scheduling problem itself is
Unicorn-era — parked. But one piece lands *now*, on the KB side: **"the rules for where to
inject data must start with the data itself"** — KB pages/blocks should carry placement
metadata (volatility tier, injection position hints) so future consumers can schedule for
caching without re-deriving it. Data carries the hints; consumers own the algorithm.
