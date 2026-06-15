---
tags:
  - kind/principle
  - source/conversation
  - theme/voice-register
  - theme/context-architecture
  - theme/single-source-of-truth
  - theme/data-driven
  - maturity/growing
  - verdict/adopt
created: 2026-06-13
appraised: 2026-06-13
---

# Encode by data type — three registers, prose for pattern-matching alone

**What it is.** A unifying doctrine that emerged while appraising the voice-register cluster
(2026-06-13). Campaign data isn't one substance with one best encoding — it partitions into
**three categories, sorted by how *tacit* the meaning is**, and each gets the encoding that
fits:

1. **Tacit → exemplar (prose).** Voice, tone, texture, character feel. Can't be specified,
   only *shown* — the Sample Book ([[0005-exemplars-over-instructions]],
   [[0006-sample-book-grid]], [[0008-form-is-the-lesson]]). Prose belongs **here and only
   here**: prose is for pattern-matching, nothing else.
2. **Explicit / factual → structured records.** Character sheets, stats, inventory, savefile
   state. Declarative, schema'd, tabular/JSON. The *bulk* of the data and the **least exotic
   — already a solved shape** in `rpg-tools` loaders and savefiles. Needs no pseudocode.
3. **Relational / conditional → pseudocode.** The "glue": relationship graphs, who-knows-what,
   faction disposition, conditional foreshadowing — what a flat record can't express cleanly.
   This is where structured data shades into *logic* ([[0099-pseudocode-as-encoding]] reading
   1 = the data edge of this; reading 2 = the control-flow edge, which carries the railroad
   risk).

**The disease it cures.** The old system **leaned on prose for far too much**, which bred
confusing/weird data and **drift** ([[0072-schema-drift-tools-vs-hand-edited-json]],
[[0076-self-canonizing-hallucinations]]). The fix: prose does *one* job (transmit tacit
voice by demonstration); everything else is **strict data or strict pseudocode procedures**.
Pick the register by what the data *is*, not by habit.

**Where it comes from.** User braindump during the voice-register appraisal (2026-06-13),
sharpening an earlier two-way split (exemplar vs pseudocode) that a *character sheet* broke —
a sheet is neither prose nor logic, forcing the third category out. Bridges the voice-register
line and the pseudocode line ([[0099-pseudocode-as-encoding]]); they aren't in tension, they're
two of the three halves of one encoding doctrine.

**The exception — "Excel-sheet doctrine."** Categories 2 and 3 *can* mix (values + formulas in
one sheet) when it's natural to. But the default is **keep them separate**: fine, single-purpose
datablocks are easy to visualize and audit ([[0099-pseudocode-as-encoding]]'s human-auditability
win — a misread surfaces at a glance in structured form, hides in a prose blob). Mix as a
deliberate exception ([[0026-exceptions-are-features]]), not a habit.

**Why it matters for next-gen.** This is a placement/encoding rule for the canonical vault
([[knowledge-base-canonical-vault]], [[0002-read-anywhere-write-canonical]]): every fact has
one home *and* one native encoding. It collapses a vague design space ("how do we represent
lore?") into a typed decision, and it scopes the genuinely-open work to a single seam.

**Open threads.** **The one real question: when must a category-2 fact-record graduate to
category-3 relational pseudocode?** (The campaign trial in [[0099-pseudocode-as-encoding]] is
the test.) Does category 1 (exemplar) ever need metadata that pulls it toward category 2 (the
cell schema in [[0006-sample-book-grid]])? Is a `json` block already "pseudocode enough" for
the relational layer ([[0090-cherrypick-contract-three-layers]])? Register vocabulary for
category 1 still unspecified ([[0008-form-is-the-lesson]]).

**Verdict.** _adopt._ Ratified at birth — this *is* the appraisal synthesis of the
voice-register cluster, confirmed point-by-point by the user. Prose for pattern-matching alone;
strict data or strict pseudocode for the rest; keep blocks fine-grained, mix only by exception.
