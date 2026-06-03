---
tags:
  - kind/pattern
  - source/solorpg
  - theme/single-source-of-truth
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# Verbatim capture, lost intent — the postprocessor rewrites scenes it was meant to copy

**What it is.** Memories evolved into "a very fascinating tool" — an alternative to story
summaries that also tracks character development. Part of the original design: capture
**vivid word-by-word copies of scenes** plus writing style. "Somewhere that idea got away" —
the postprocessor started **rewriting** captured scenes instead of copying them verbatim.
User suspects this is a source of **style drift**: the corpus that should demonstrate the
campaign's voice is being progressively re-voiced by the tool that maintains it.

**Where it comes from.** User recollection (2026-06-03). The drift is in
`solorpg`'s post-processing flow (session-postprocess, memory extraction) — exact point of
divergence not yet located.

**Why it matters for next-gen.** Two lessons stacked:
1. **Verbatim is a mode, not a strength of paraphrase.** A pipeline must distinguish
   *copy* operations from *summarize* operations and never let one decay into the other —
   exemplar value lives in the exact words ([[0005-exemplars-over-instructions]],
   [[0008-form-is-the-lesson]]: a rewritten exemplar teaches the rewriter's voice).
2. **Pipelines drift from their own spec** — this is [[0052-evolution-vs-drift]] one level
   up: not the campaign drifting from canon, but the *workflow* drifting from its design
   intent, unnoticed because nothing pinned the intent ([[0019-companion-rationale-as-anti-regression]]
   exists precisely to prevent this).

**Open threads.** **Audit lead:** find where in the postprocess flow scenes get rewritten,
and whether early campaigns' memories contain true verbatim scenes (the before/after would
prove the style-drift suspicion). Harvest-vs-workshop ([[0007-harvest-vs-workshop]]) wants
the verbatim mode back — clipped play is the harvest. Related mining leads: the **style
palette** pattern and **lingo files** ([[0053-anchor-hierarchy-voice-keystone]]).

**Verdict.** _(unevaluated.)_
