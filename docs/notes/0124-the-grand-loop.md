---
tags:
  - kind/pattern
  - source/conversation
  - theme/workflow
  - theme/context-economy
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-21
---

# The grand loop — the whole-system lifecycle, one closed cycle with inlets and a drain

**What it is.** The end-to-end lifecycle the next-gen system runs on, captured as a *shape*
(step 3: get it down faithfully) before it becomes the roadmap spine (step 1). It's an **engine
cycle** with **injection inlets** on the side and one **drain** at the bottom. Owner sketch,
2026-06-21: *"import → chunk down to update-sized chunks → [lotsa postprocessing] → 〈stable
archive〉 → session prep → bundle → play → export finished session → import."* That's the
**simplest view**; the folds below are what make it real.

```
 claude.ai dump ─► [bulk ingest / corpus-routing] ─► sessions ─┐
                                                               ▼
   workshopping ─┬─► bootstrap (seeds) ───────────► session-prep   import
                 ├─► reference (engineered) ─► 〈vault〉             │
                 └─► scratch / quarantine                          ▼
                                                                   …
   〈campaign vault〉 ─► session-prep ─► bundle ─► play ─► export ─► import ─► [postprocess] ─► 〈campaign vault〉
        │
        └─► [archive old data] ─► 〈archive / cold storage〉
```

**The engine cycle.** `〈campaign vault〉 → session-prep → bundle → play → export → import →
[postprocess] → 〈campaign vault〉`. Play produces the export that becomes the next import; the
vault is the **still point** every stage writes into and reads out of. The session is the
load-bearing unit moving around the loop ([[0121-narrative-granularity-ladder]]).

**Folds that make it not-linear.**

- **Import is two-phase.** A front-stage **bulk ingest** processes a whole **claude.ai data
  dump** — a *collection* of sessions (and "…other") — a workflow in its own right (this is the
  corpus-routing cluster, [[0108]]–[[0112]]); only then does **per-session import** (chunk →
  postprocess) run. The single `import` arrow hid a pipeline.
- **The workshop inlet** injects net-new material — not only at genesis (**new campaign** =
  cold-start seeding) but **mid-flight** (**new branch / new character**). It forks **three** ways:
  - **bootstrap (seeds)** → feeds **session-prep**. *Grown from*: organic, may not all sprout,
    leftover seeds can carry forward (default lifespan = consume-to-prime-one-session, with the
    known exception that un-sprouted seeds persist).
  - **reference (engineered)** → lands straight in the **vault**. *Built*: deliberate, canonical,
    persists by design (things already "true" in the world).
  - **scratch / quarantine** → off to the side, **must not contaminate the main repo**. Raw
    speculation, shapeless on purpose; only *graduates* inward if it earns a shape. Kin to the
    `inbox/` staging idea and the model-layer sidequest-quarantine.
  - Path is decided by **lifespan × readiness**: seeds = still being brought into play; reference
    = already true; scratch = not yet anything.
- **The drain.** The loop is **not conservative**: `[archive old data] → 〈archive / cold
  storage〉` removes material aging out of the live working set. **Vault is alive; archive is
  cold.** (Relabel that matters: the live store is the *vault*, the word *archive* is reserved for
  where retired things go — not an ambiguous noun for the live store.)

**Branch is NOT in the loop.** Multi-branch does **not** change this topology — branch is a
**selector/filter** that scopes which data flows through; the loop runs identically regardless.
Folding it into the flow would be exactly the "confuse organization with narrative/flow structure"
error [[0123-branch-as-organizational-axis]] warns against. At most: every *read-from-vault* step
takes a branch scope.

**Two named black boxes — the next two design drill-downs (not pretended-solved):**
1. **`[postprocess]`** — what happens between a raw exported session and it being safely folded
   into the vault: entity extraction, summaries, savefiles, memories, timeline placement (cf.
   [[0075-postprocessing-as-vault-librarian]], the compaction-granularity tunable
   [[0122-compaction-boundary-descends]]).
2. **`〈campaign vault〉`** — what the live store *is* internally: canonical-raw vs. renders, the
   summary granularity-ladder, the catalogue/index, how session-prep reads **selectively** (cf.
   SSoT [[0093]]/[[0094]]/[[0098]], catalogue+bitemporal [[0102]]/[[0103]],
   [[knowledge-base-canonical-vault]]).

**Why it matters for next-gen.** This is the candidate **roadmap spine**: every pillar of
STATE-OF-RESEARCH hangs off a stage of this loop (P1 = vault + import/postprocess; P2 = session-prep
→ play → export; P3 = backends under the vault/archive; P4 = the play frontend; P5 progression and
P6 model-layer ride inside play/postprocess). Getting the *shape and vocabulary* right first means
the sequencing later attaches to something accurate.

**Open threads.** Are `bootstrap`/`reference`/`scratch` three stores or three *entry depths* into
one? Is the bulk-ingest front-stage a one-time migration or a recurring intake? Does the drain feed
*back* (cold→warm re-activation) or is archival terminal? Both black boxes need their own passes.

**Verdict.** _(unevaluated — captured as shape, not yet appraised.)_
