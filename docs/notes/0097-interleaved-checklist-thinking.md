---
tags:
  - kind/pattern
  - source/conversation
  - theme/skill-authoring
  - theme/single-source-of-truth
  - maturity/experimental
  - verdict/unevaluated
created: 2026-06-08
---

# Interleaved checklist-thinking — per-paragraph think-blocks, and why the fact-check ate itself

**What it is.** One of the oldest userstyle experiments (braindump 2026-06-08):
break to a `<thinking>` block **after each paragraph** of GM prose and run a small
checklist — pacing, "is this a good place to stop?", and a drift-from-canon fact-check.
Inline self-supervision woven through generation itself, an aggressive form of
[[0016-thinking-as-enforcement]] (per-paragraph, not just pre-turn).

**Per-check track record:**
- **Fact-check — failed, and is *the* canonical example of [[0076-self-canonizing-hallucinations]]** (the most damning one). It checked drift against *the very prose it
  was writing*, not against canon, so an in-context error became the authority:
  `blabla [error] … <thinking>oh, the error is canon! the text says so!</thinking> …
  [more error]`. No independent ground truth → the check confirmed the drift and
  barreled on. A self-supervising check that feeds on its own output has no teeth.
- **Good-place-to-stop — mechanically worked but fired every time** → no signal.
- **Pacing — worked, but only as the *upfront* check** (in the first thinking block),
  not per-paragraph.

**The keeper.** Not the checks individually — the **checklist-thinking discipline** at
that level. The user wants it back: walking a genuine checklist beat-by-beat was good.

**The forward tension.** Modern Opuses **fight it: they collapse the checklist (answer
the whole list in one breath instead of walking it) and resist taking it seriously** —
possibly Anthropic-set thinking budgets optimizing structured per-paragraph CoT away,
uncertain. So the technique the user wants to revive is the one current models resist.
This recharacterizes 0016's "hollow recitation" failure as partly *model-driven*, not
just author-driven — the model actively compresses the walk. Workaround axis: collapse
(not refusal-to-think) points at forced-structure remedies — structured output, a tool
call per checklist item, exemplars ([[0005-exemplars-over-instructions]]) — over softer
prompting. (Aside: the model also resists *writing the technique into* the user's
skills/userstyles — a separate meta-issue, noted not pursued.)

**Why it matters for next-gen.** Two lessons. (1) **A self-check needs an independent
reference or it self-canonizes** — the fact-check must read canon from outside the
generation (a tool read, a sealed source), never from the prose-so-far; design
verification against a source of truth, not against context. (2) Per-paragraph
enforcement collides with both context economy (0016's open thread) *and* model
budget-compression — adaptive depth (deep at boundaries, light mid-scene) is now doubly
motivated.

**Open threads.** Is the fact-check salvageable if pointed at an external canon read
mid-generation (hook/tool — [[0082-live-hook-pipeline]]) rather than self-CoT? Is the
collapse really thinking-budget, and is it steerable? Which checks are worth per-paragraph
cost vs. upfront-only (pacing already demoted itself to upfront)?

**Verdict.** _(unevaluated.)_
