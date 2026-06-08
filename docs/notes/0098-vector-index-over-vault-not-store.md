---
tags:
  - kind/question
  - source/conversation
  - theme/memory-architecture
  - theme/context-economy
  - theme/single-source-of-truth
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-08
---

# Vector DB as an index *over* the vault, not a store *of* the data

**What it is.** A question/architecture-direction (braindump 2026-06-08): can the vector
DB index the vault's `.md` files rather than hold the data itself? **The vault stays the
single source of truth; the vector DB is just for search** — a derived, rebuildable index,
disposable and regenerable from the files at any time.

**Refines [[0040-vector-db-as-lore-search-module]].** 0040 (`adopt`) called the vector
store "the searchable *source-of-truth* for everything that has happened." This inverts
ownership: the **vault** is the source of truth, the index is a *view* over it. Same module
role (lore-search), cleaner data-ownership story — and the exact inversion of the E:\rpg
pattern where Qdrant *was* the store. Sits squarely in the read-anywhere/write-canonical
([[0002-read-anywhere-write-canonical]]) and files-as-build-products
([[0056-files-as-build-products]]) lineage: canonical files in, derived artifacts out,
rebuild the derived layer whenever it drifts.

**Granularity: "possibly all of these, with filters."** Multiple granularities indexed
together — whole-page, section-level (matching the cherrypick contract
[[0090-cherrypick-contract-three-layers]]'s `##`-section cut), and finer — with metadata
filters at query time. This is precisely E:\rpg's **multi-granularity chunking**, which
CLAUDE.md flags as a keeper pattern; carry the chunking insight, drop the store-ownership.

**Why it matters for next-gen.** Settles a latent question in 0040 (index raw / curated /
both) toward "index the vault, at every useful granularity." It also makes the index safe
to throw away and rebuild — no migration anxiety, no schema lock-in
([[0072-schema-drift-tools-vs-hand-edited-json]]), and the file layer keeps working when
the index is down.

**Open threads.** **Sealed secrets are the sharp edge** ([[0089-sealed-secrets-files]]):
a naive indexer vectorizes a `DO NOT READ` page and surfaces it via search, blowing the
seal — so the index *must* honor the sealed flag and campaign-isolation
([[0029-information-boundary-enforcement]], [[0003-scope-memories-to-context]]) as
hard filters, not afterthoughts (0096: a leak via search is hard to claw back). What's the
**sync/rebuild trigger** — a hook on file write ([[0082-live-hook-pipeline]]), a prep-stage
reindex, or on-demand? Filter dimensions (campaign, kind, sealed, era, observed-vs-actual
[[0020-observed-vs-actual]]). Embedding choice / local-vs-hosted (constraint:
stdlib-leaning, portable — see [[0063-portable-bundles-constraint]]). Does whole-page +
section double-indexing cause duplicate hits that need dedup at query time?

**Verdict.** _(unevaluated.)_
