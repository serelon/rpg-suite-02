---
tags:
  - kind/pattern
  - source/solorpg
  - theme/campaign-isolation
  - theme/corpus-building
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-13
---

# k-NN, not centroids — classify against neighbours because campaigns drift

**What it is.** From the import brief ([[import-design-brief]], Spine A): to classify an
orphan conversation into a campaign by embedding similarity, use **k-nearest-neighbours
(majority vote over nearest *individual* labeled points), not a per-campaign centroid.**
The reason is drift: a long campaign drifts in arc, tone, POV, and even the model that
wrote it. An arc-3 orphan matches *other arc-3 points* even when arc-1 points are tonally
distant. Averaging a campaign to one centroid **blurs exactly the campaigns that matter
most** — the long, rich, evolved ones.

**The bonus: the geometry is itself the crossover detector.** If the top-2 neighbours come
from *different* campaigns, the point genuinely sits between two clouds → emit
`crossover-between` ([[0108-multi-label-relational-routing]]) and/or escalate. "The
geometry honestly reporting 'between two clouds' IS the crossover detector" — you don't
need a separate mechanism for crossovers; contested k-NN *is* it.

**Where it comes from.** `../solorpg/imports/IMPORT-DESIGN-BRIEF.md`, "Spine A — Supervised
routing." The user's own pre-planning.

**Why it matters for next-gen.** A specific, non-obvious correction to the naive "embed
each campaign as a vector" approach, and it extends [[0098-vector-index-over-vault-not-store]]:
the index isn't just for retrieval, it's for *classification under drift*, and its
nearest-neighbour structure carries signal (contestedness = crossover) a centroid throws
away. Ties to campaign isolation — drift is *within*-campaign variance, and k-NN respects
it instead of flattening it.

**Open threads.** Choice of k and the contested-threshold (when is "between clouds" a real
crossover vs noise?). Does the same drift-respecting logic apply to *in-play* retrieval
(loading the right arc-relevant context), not just import routing? Embed granularity
(sample vs full-doc, an open decision in the brief) interacts with how clean the neighbour
geometry is.

**Verdict.** _(unevaluated.)_
