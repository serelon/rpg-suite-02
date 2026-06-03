---
tags:
  - kind/idea
  - source/old-erpg
  - source/new
  - theme/architecture
  - theme/extensions
  - theme/memory-architecture
  - theme/context-economy
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-03
---

# The vector-DB as the lore-search module — centralization *is* a module

**What it is.** `E:\rpg`'s abandoned Qdrant vector store, reframed (per user) as **one module
among many** in the [[0036-every-subsystem-is-a-module]] system: the **lore-search module** —
the searchable **source-of-truth for everything that has happened across many sessions**.
*Everything* gets indexed; semantic search makes the entire campaign history easily queryable.
The user is considering **resurrecting** it for exactly this role.

**Where it comes from.** User, resolving the appraisal tension I raised (modules-that-refer-
back vs. one-central-authoritative-store): "0036 doesn't entirely conflict with the E:\rpg
approach — the vector-DB would be one module of many… it'd give the source-of-truth for
lore-searching." First captured idea from the queued `E:\rpg` resurrection mine.

**Why it matters for next-gen.** It **dissolves the modules-vs-centralization tension**: a
central authoritative store isn't an *alternative* architecture to "everything is a module" —
it's the *internal implementation of one module*, and everyone else **refers back** to it
([[0036]]). Centralization becomes local to a module, not global. It also fills a real gap:
flat files + per-session bundles can't do long-horizon, cross-session, cross-era recall;
semantic search over an indexed history can. That makes it the **cold store** the eviction
model implies — [[0009-jit-context-and-eviction]] evicts detail from live context;
lore-search is where it goes and how it's recalled on demand — and the natural counterpart to
[[0030-summary-as-compression]] (summaries carry forward state; the store holds the full
texture, retrievable).

**Open threads.** Retrieval is the easy half (E:\rpg knew this; *eviction/curation* and
**campaign-isolation** are the hard parts — [[0003-scope-memories-to-context]],
[[0029-information-boundary-enforcement]]: the index must respect scope, incl.
[[0020-observed-vs-actual]] secrecy). Index raw sessions, or curated memories, or both? Is
lore-search a **layer over the memory module** or its own module — and where's that boundary
([[0034-outgrown-scaffold]] warns against fuzzy ownership)? Write/sync path. E:\rpg's
entity-registry/disambiguation patterns (still unmined) likely belong to this module. Re-test
against [[0031-beware-transient-constraint-architecture]]: with 1M context, is full-history
*search* still needed, or does more just fit? (Likely yes — total history ≫ any window.)
