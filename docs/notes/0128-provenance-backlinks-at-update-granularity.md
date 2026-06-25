---
tags:
  - kind/principle
  - source/solorpg
  - theme/single-source-of-truth
  - theme/knowledge-base
  - theme/workflow
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-25
---

# Every derived datum backlinks to its source updates — provenance at update granularity

**What it is.** A hard cross-cutting requirement surfaced while shaping postprocess
([[0127-postprocess-as-controlled-mess]]): **every piece of derived data must carry strict
backlinks to the source it was distilled from, at *update* granularity.** Character A's profile
records that it's based on `[session03/45]`, `[session03/68]`, etc. — not just "session 03." This
lets you **pull the exact source context back without rereading massive amounts of data.**

**The address space is the chunk granularity from the loop.** [[0124-the-grand-loop]]'s import
step "chunks down to update-sized pieces." Those update-chunks *are* the addressable anchors:
`session03/45` = update 45 of session 03. Chunking isn't just processing prep — it **mints the
provenance address space.** Three loop stages, one mechanism: *chunk* (mint IDs) → *postprocess*
(emit data backlinked to IDs) → *review/derive* (resolve IDs to retrieve source).

**Where it comes from.** Owner, 2026-06-25, designing the postprocess control layer (visibility
pillar). Grounded against the live skill `solorpg/.claude/skills/session-postprocess/`: chunks
*are* addressable (`session-N-chunk-NN.md`; the timeline even cites `[Chunk 1-2]`), but **no
emitted output carries a source backlink** — the memory schema's `connections` are entity→entity
edges only. So v1's actual "get the source back" mechanism is **re-read the chunks** (the
self-check steps say to re-read on noticing a gap). Backlinks replace *reread-whole-chunks* with
*targeted retrieval*. (Note: this is **not** about retiring a persistent context-holding agent —
that v2 "Lorekeeper" approach is already deprecated, "context window now sufficient.")

**Why it matters for next-gen.** It's the keystone under two otherwise-stuck pillars:
- **Visibility / review** ([[0127]] pillar 3) — an audit step or DB-review GUI needs "click a
  datum → see its sources → go back." Impossible without the backlinks; trivial with them.
- **Re-derivation** — [[0094-save-everything-deferred-compute]] wants to re-render derived
  artifacts when models improve. Backlinks make re-derivation *targeted* (re-distill just the
  updates a datum depends on) instead of reprocessing whole sessions.

**The diagnosis→mechanism link with the lossy-capture notes.** [[0125-texture-has-no-capture-path]]
and [[0126-reinterpretation-sands-off-load-bearing-edges]] are *failure diagnoses* — the stages
where the workflow loses things (texture never captured; verbatim sanded off by summarize-as-default).
Those are about **details/content**; 0127/0128 are about **workflow**. The seam: **backlinks are what
make those losses recoverable rather than fatal.** Because every datum points back to its source
updates, you can *go back, re-tune, redo, reinterpret* a lossy datum without rereading everything —
the loss becomes *re-derivable on demand* instead of permanent. So 0125/0126 say "we lose X here,"
and 0128 says "…and here's why that's fixable." (Pairs with 0126's own proposed fix — route
verbatim *around* the lossy stages — which the backlink address space makes addressable.)

It's the concrete, addressable form of patterns the vault already holds: [[0111-provenance-graph-as-secret-history]]
(routing edges as lineage), [[0076-self-canonizing-hallucinations]] (check the layer below — the
backlink *is* the pointer to the layer below), [[0103-bitemporal-subentry-versioning]] (provenanced
subentries), [[0102-catalogue-metadata-shape]] (the provenance anchor that makes everything else
backfillable). It also sharpens **T8 / SSoT**: if every render backlinks to canonical-raw updates,
the raw layer's primacy is *enforced by reference*, not just asserted.

**Open threads.** Granularity floor: is the `update` the finest addressable unit, or do
sub-update spans matter (a single sentence)? Multi-source data (a profile built from 20 updates)
— store all edges, or a provenance *set* with confidence? Does the backlink live on the datum
(frontmatter `source:`), in a separate provenance graph, or both ([[0077]] placement-in-data vs
consumer)? How does provenance survive *compaction* — when updates roll into arc/season summaries
([[0122]]), do backlinks re-target to the summary or keep pointing at now-cold raw? Who *writes*
the backlink — is emitting it a non-skippable contract of every step-skill?

**Verdict.** _(unevaluated — captured as design requirement, not yet appraised.)_
