---
tags:
  - kind/principle
  - source/conversation
  - theme/voice-register
  - theme/corpus-building
  - theme/single-source-of-truth
  - maturity/seed
  - verdict/adapt
created: 2026-06-13
---

# Rewrite belongs to the curated layer, copy to the verbatim layer — the contract, not the operation, decides

**What it is.** A head-on tension, now **resolved**. **Distillation**
([[0113-distill-dont-imitate]]) rewrites messy scenes toward the canonical voice to
manufacture a consistent corpus. But [[0054-verbatim-capture-lost-intent]] names a
postprocessor *rewriting scenes it was meant to copy* as a suspected drift source, and
[[0094-save-everything-deferred-compute]] holds the raw transcript layer permanent and
lossless. Same operation — strong-model rewrite of captured prose — opposite verdicts.

**The resolution: the layer's contract decides, not the operation.**
- **Verbatim layer** (transcripts, memories — 0054, 0094): contract is *faithful copy*.
  Rewriting here is the sin; that's the drift 0054 caught — a rewrite that *replaced* what
  it should have copied and fed back up the canon chain.
- **Curated layer** (sample book, texture bank — [[0006-sample-book-grid]],
  [[0055-register-anchor-banks]], [[0007-harvest-vs-workshop]]): contract is *workshopped*.
  Rewriting here is the **feature** — the user's "tune it better than mid-scene allows."

So 0054 was never a warning against rewriting; it was a warning against rewriting in the
**wrong layer**. The rule: **rewrite freely into curated renders, copy-only into the
verbatim source; never in-place, never up the canon chain** — the build-product / render
relationship ([[0056-files-as-build-products]]).

One guardrail rides on top (the [[0008-form-is-the-lesson]] / [[0076-self-canonizing-hallucinations]]
lesson): a rewrite teaches whatever voice it's *aimed at*. Aimed at an **explicit anchor**
(your best scenes, the canonical register) it tunes toward target; aimed at nothing, the
model's defaults fill in and you've laundered sails-onto-starships
([[0114-voice-vs-setting-fidelity]]) into your own exemplar bank. **Curated-layer rewrite
is safe only with the anchor present.** That single condition is the whole difference
between 0113 (workshop) and 0054 (drift).

**Where it comes from.** Inbox conversation [[Claude-export-custom-lora]] (2026-06-13),
read against the verbatim-preservation notes; resolved in appraisal 2026-06-13 once the
user reframed distillation as a *sample-book production technique* rather than dataset prep.

**Why it matters for next-gen.** It's a reusable doctrine for **every** strong-model
rewrite the toolchain will be tempted to run (postprocessing, summary, exemplar tuning,
eventual dataset distillation): ask *which layer, and is the anchor present* before
allowing a rewrite. Defends [[0073-structured-mutation-beats-rewrite]] and the
single-source-of-truth stance without banning the genuinely useful rewrite.

**Open threads.** The one case that still strains the rule: a **fine-tune bakes a derived
voice into weights**, so at the point of play the "captured vs normalized" distinction is
erased — the adapter *is* the GM's voice. Is that the goal (a deliberately unified register)
or laundering at one remove? Parked with the rest of the local-model sidequest
([[0116-lora-earns-its-keep]], [[0115-lora-idiom-lorebook-facts]]).

**Verdict.** _(2026-06-13.)_ **adapt** — promoted from open question to resolved principle:
*the layer's contract, plus the presence of an anchor, decides whether a rewrite is workshop
or drift.* The remaining fine-tune-bakes-voice edge stays genuinely open but is sidequest-gated.
