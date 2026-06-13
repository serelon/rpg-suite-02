---
tags:
  - kind/idea
  - source/conversation
  - theme/voice-register
  - theme/corpus-building
  - theme/local-finetuning
  - maturity/seed
  - verdict/adapt
created: 2026-06-13
---

# Distill, don't imitate — normalize messy data toward a spec with a strong model

**What it is.** When the training corpus is *inconsistent* and unifying it is the whole
goal, training on it raw is self-defeating — you teach the model the exact inconsistency
you're trying to escape. The move is **distill, not curate**: hand a strong model (Opus)
a raw scene plus the canonical-voice spec (the userstyle) and have it *rewrite* the scene
into the unified voice. The rewrite is the training pair; the dataset becomes consistent
**by construction**, and "curation" collapses to a glance-and-discard QC pass. Anchor the
rewrites in your *best* existing scenes so the unified voice is grounded in material you
already loved, not an abstract spec.

The method has **two filters on two different criteria** (conflating them is what makes
curation feel impossible):
- **Filter 1 — raw scenes going *in*.** Select on *situation, not polish* (the strong
  model fixes prose): voice-bearing (not mechanical bookkeeping)? rewritable (is
  what-happened clear, so a rewrite is *normalization* not *invention*)? new (a beat you
  don't already have five of)?
- **Filter 2 — post-rewrite QC gate.** Where strictness lives, and it's cheap: kill
  anything that drifted off-voice, invented plot, or went incoherent. Ten-second
  judgments, not craft evaluations.

**Where it comes from.** Inbox conversation [[Claude-export-custom-lora]] (2026-06-13), on
building a per-campaign style LoRA from ~70 imperfect Long-Watch sessions. The technical
LoRA framing is incidental; the transferable design idea is the **rewrite-toward-spec data
move**, which generalizes to any corpus-unification task (memory normalization, savefile
voice, texture banks).

**Why it matters for next-gen.** It's a concrete mechanism for the voice-unification
problem the vault keeps circling ([[0053-anchor-hierarchy-voice-keystone]],
[[0055-register-anchor-banks]], [[0005-exemplars-over-instructions]]): instead of
hand-grading thousands of scenes, anchor 50 spanning the register range as a **style
bible**, let the strong model normalize the rest toward them, QC the output. The anchors
are chosen to *span the range* (combat / dread / tenderness / quiet / exposition), not
"top-50 by quality" — fifty great combat scenes teach a lopsided voice.

**Open threads.** Hard tension with the verbatim-preservation stance —
[[0054-verbatim-capture-lost-intent]] names the postprocessor *rewriting scenes it should
copy* as a suspected drift source, and [[0094-save-everything-deferred-compute]] holds the
raw transcript layer as permanent and lossless. Distillation is *deliberate* rewriting
toward a target; is it the good twin of the same operation that caused the drift, or the
same hazard wearing a goal? Captured as [[0117-distill-vs-verbatim-tension]]. Second
thread: the rewrite step can *launder* clichés (see [[0114-voice-vs-setting-fidelity]] /
[[0076-self-canonizing-hallucinations]]) — a blind rewrite imports the strong model's own
defaults into your training data.

**Verdict.** _(2026-06-13.)_ **adapt** — reframed away from "LoRA dataset prep" into its
real job: a **workshop technique for producing curated exemplars** (sample book / texture
bank), tuned in ways you can't manage mid-scene. Live and sample-book-adjacent, not parked
for a hypothetical fine-tune. Safe **only with an explicit anchor present** (else it
launders the model's defaults — [[0114-voice-vs-setting-fidelity]]) and **only in the
curated layer, never the verbatim source** — see the resolution in
[[0117-distill-vs-verbatim-tension]]. The middle gear of [[0007-harvest-vs-workshop]].
