---
tags:
  - kind/principle
  - source/conversation
  - theme/data-driven
  - theme/progression
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-12
---

# Prose-deprecation doctrine: structured data by default, prose only where prose is the payload

**What it is.** A stated direction: **deprecate prose more and more.** Prose is the wrong
substrate for *data* — illegible to query, lossy, drift-prone, token-heavy, and updatable
only by rewrite. Use **structured data by default**; reserve prose for the one place it's
irreplaceable — **pattern-matching material that is itself the payload** (voice, appearance,
texture), and even there *heavily curated*.

**Where it comes from.** Interview 2026-06-12: *"I actually want to start deprecating prose
more and more. Unless it's for pattern-matching (which should be heavily curated), it's
pretty awful for pure data."* Crystallized while diagnosing why Tarot's prose character
sheets bloated and drifted ([[0105-tarot-progression-unifying-failure]]).

**Why it matters for next-gen.** It cleanly splits the whole corpus by **whether prose is
the payload or merely the carrier**:
- **Prose is the payload** → keep it (curated): voice exemplars
  ([[0005-exemplars-over-instructions]]), the texture/register banks
  ([[0055-register-anchor-banks]], [[0006-sample-book-grid]]), conversation transcripts as
  GM context ([[0062-conversation-transcripts-as-gm-context]]).
- **Prose is carrying data** → replace with structure: character sheets, savefiles, status,
  stats, relationships, plot-thread state.

This sharpens the KB-as-structured-vault direction ([[knowledge-base-canonical-vault]]) into
a *doctrine*, and supplies the prose layer's discipline in the three-layer record
([[0106-three-layer-character-record]]). Allies: [[0099-pseudocode-as-encoding]] (structured
encoding even of lore/logic), [[0073-structured-mutation-beats-rewrite]] (structure enables
surgical edits), [[0010-docs-as-code-context-compiler]].

**Open threads.** The boundary is not always clean — e.g. a savefile's "current situation
summary" is prose *about* state; does it get structured, or is it a curated render? Tension
with [[0094-save-everything-deferred-compute]] (hoard raw prose transcripts losslessly) —
resolved by the payload/carrier split? (transcripts are payload, derived state is carrier).
Risk: over-structuring kills the things LLMs are *good* at — where's the floor?

**Verdict.** _(unevaluated.)_
