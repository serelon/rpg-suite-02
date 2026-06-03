---
tags:
  - kind/pattern
  - source/tarot-tales
  - source/solorpg
  - theme/single-source-of-truth
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# Anchor hierarchy — characters first, and voice is the keystone anchor

**What it is.** Empirical lineage of what anchors actually stop drift, learned by adding
them one at a time across generations: at the very start *nothing* was captured (voice and
personality drifted freely) → then ~50 words of character description (still drifted — no
voice) → then **voice samples were added, and it started working well**. Anchor priority,
from the user directly: **characters most important; world, concept, locations after.**

**Where it comes from.** Tarot Tales era (gen 2/3) through solorpg, recounted 2026-06-03.
Explains *why* today's character JSON puts voice samples in the immutable tier
(rpg-tools character-guide) — that placement is a scar, not a guess.

**Why it matters for next-gen.** When budgeting anchors (context economy, [[0001-tiered-progressive-loading]]),
spend on character voice first — it's the empirically load-bearing anchor. Converges with
the whole exemplar thread: voice can't be specified, only demonstrated
([[0005-exemplars-over-instructions]]); 50 words of *description* failed where voice
*samples* succeeded — same lesson, discovered independently years earlier.

**Open threads.** "There's more we'd want to capture" (user) — the anchor set is still
incomplete. Known candidates: writing style ([[0054-verbatim-capture-lost-intent]]), the
**style palette** pattern, **lingo files/data** (both located somewhere in the source repos —
mining leads). Is there an equivalent "keystone anchor" for *world* drift?

**Verdict.** _(unevaluated.)_
