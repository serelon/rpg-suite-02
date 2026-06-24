---
tags:
  - kind/observation
  - source/solorpg
  - source/conversation
  - theme/voice-and-register
  - theme/single-source-of-truth
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-24
---

# Reinterpretation sands off load-bearing edges — the verbatim mode collapsed into summary

**What it is.** The memory system was *designed* with **two kinds** of capture:
1. **summary-of-events** — condensed, interpreted, "what happened."
2. **verbatim cut'n'paste** — an *exact copy* of the narrative text, nuance and all.

In practice the second kind **collapsed into the first**. Everything gets reinterpreted,
summarized, compacted — so the verbatim mode effectively doesn't exist. The failure isn't
neutral compression; it's **lossy in exactly the wrong place**:
- Details *intended to be pattern-matched against* (exemplars, voice texture) get squished
  into a summary — losing the very nuance that made them worth keeping. A paraphrased
  exemplar teaches the paraphraser's voice, not the source's ([[0008-form-is-the-lesson]]).
- **Load-bearing edges get sanded off.** Owner's sharpest example: horror scenes whose dread
  lived in *specific* exact details get progressively smoothed until **the horror is
  completely gone.** The edges that carried the payload are precisely what a summarizer
  treats as removable.

**Where it comes from.** Owner observation (2026-06-24), watching the live `solorpg`
post-process flow. Concrete, repeated, field-observed — not theoretical.

**Why it matters for next-gen.** The root cause is a **default pull toward
reinterpretation**: every pass that *reads-then-writes* prose silently re-voices and
smooths it, because summarizing is the model's reflex. A pipeline that doesn't hard-separate
**copy** from **summarize** will always let copy decay into summarize — entropy runs one
direction.

- This is **[[0054-verbatim-capture-lost-intent]]** generalized: 0054 = the postprocessor
  rewriting verbatim scenes; this = the *universal* reinterpretation reflex, of which the
  postprocessor rewrite is one instance. The mechanism (compaction/summarization sands edges)
  is the new content.
- It's the structural-mutation argument for prose: **[[0073-structured-mutation-beats-rewrite]]**
  — wholesale regeneration is the drift aperture; verbatim copy is the prose equivalent of
  append-don't-rewrite.
- It's *why* verbatim must be a protected operation, not a strength of paraphrase
  ([[0062-conversation-transcripts-as-gm-context]]: verbatim "keeps the story from
  mutating"; [[0094-save-everything-deferred-compute]]: the transcript layer is permanent
  and lossless *by design*).
- Connects to **[[0125-texture-has-no-capture-path]]**: there, texture isn't *selected*;
  here, even when it *is* captured, the reinterpretation pass *destroys* it. Two ways the
  same nuance dies — never-captured vs captured-then-sanded.

**Open threads.**
- Mechanism is **summarization-as-default**: is the fix (a) a hard copy/summarize mode flag
  honored end-to-end, (b) *no* read-then-rewrite passes over verbatim material at all
  (route it around the lossy stages), or (c) a guard that diffs output against source and
  flags re-voicing? Likely (a)+(b): verbatim material should never enter a summarizing
  agent's mouth.
- **Where does the edge-sanding happen** — at extraction, at compaction, at bundle-build,
  at recompaction? (0054's audit lead: find the divergence point. The descending compaction
  boundary, [[0122]], multiplies the number of passes that can sand.)
- "Load-bearing edge" wants a **definition the tool can honor** — what makes a detail
  load-bearing (horror payload, exemplar nuance, a pattern-match anchor) vs genuinely
  removable? Until that's nameable, a summarizer can't be told to spare it. (Same shape as
  0125's "what makes a detail load-bearing-for-world?")
- Tension with legitimate compression ([[0030-summary-as-compression]]): summary *is* the
  right tool for forward-looking state. The error is summarizing the **wrong layer** — the
  one whose value *is* its exact form. The cut is by *layer/payload*, not by stinginess
  ([[0107-prose-deprecation-doctrine]]: keep prose where it's the payload).

**Verdict.** _(unevaluated — appraise with the voice-register / memory-system cluster
alongside [[0125]] and [[0054]].)_
