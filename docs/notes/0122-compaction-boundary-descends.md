---
tags:
  - kind/observation
  - source/conversation
  - theme/narrative-structure
  - theme/context-economy
  - maturity/seed
  - verdict/adapt
created: 2026-06-20
---

# The season boundary was a coupled constraint — and the compaction boundary is descending

**What it is.** The **season** unit ([[0121-narrative-granularity-ladder]]) originated as a
**two-way coupling** of narrative and technical limit, not one masquerading as the other:

- *Technical side:* all session summaries stayed in context until they had to be **compacted** —
  that compaction point **was** the season break.
- *Narrative side:* the season finale was a **real chosen beat**, and a season shift usually
  involved **refactoring** after a grand finale.

The two shaped each other: the context-window pressure **tended to push the story toward a
finale**. Constraint and narrative co-produced the boundary.

**The live move: the compaction boundary is descending.** Doing **smaller compactions after
arcs** makes the whole thing more granular. As compaction gets cheaper/finer and context is
built **dynamically** rather than accreted-until-full, the forcing function that bunched stories
into grand season finales **relaxes** — pacing can breathe instead of being herded toward a
season wall. The unit didn't die; the **compaction granularity moved down a level** (season →
arc), and *that* changes story pacing.

**Where it comes from.** Owner, 2026-06-20. "Seasons started out as an organizational unit, all
summaries stayed in context... had to compact at some time, that was the season break... now that
we're building context more dynamically, it doesn't have as strong a role anymore." Correction
captured: it was **both** narrative and constraint, with the constraint *forcing* toward finale.

**Why it matters for next-gen.** A clean instance of
[[0031-beware-transient-constraint-architecture]]: a story structure partly produced by a
context-window limit. The thing dissolving it (dynamic context-building, [[0009-jit-context-and-eviction]],
[[0051-live-context-delta]]) is exactly what this repo reaches toward — so next-gen should treat
**finale/refactor as a *chosen* beat**, decoupled from any technical compaction trigger. Compaction
granularity becomes a **tunable** (per-arc, per-season, per-update?) rather than a fixed wall;
relates to [[0030-summary-as-compression]], [[0075-postprocessing-as-vault-librarian]].

**Open threads.** If compaction can happen at arc granularity, what's the **summary hierarchy**
(per-arc summaries rolling into season summaries rolling into campaign)? Does the descending
boundary make `season` vestigial, or does it survive purely as a narrative-pacing choice once the
constraint is gone? Tie to the refactor ritual — is "season refactor" still worth keeping as a
deliberate maintenance cadence?

**Verdict.** **Adapt.** Two claims, two fates (owner appraisal 2026-06-20):
- **Compaction granularity as a tunable** (per-update / per-arc / per-season) → **adopt, a
  next-gen commitment** — "we're pushing towards more granularity and more context engineering."
  Consistent with [[0009-jit-context-and-eviction]], [[0051-live-context-delta]], [[0094-save-everything-deferred-compute]].
- **Season's survival as a unit** → **undecided, keep as an option.** Owner: *barely used it since
  the current solorpg system; only legacy campaigns lean on it.* So season is a **legacy-coupled
  structure on probation** — not confirmed dead, not confirmed carried. Don't settle it either way.
