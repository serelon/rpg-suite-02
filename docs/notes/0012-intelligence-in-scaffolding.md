---
tags:
  - kind/idea
  - source/new
  - source/sillytavern
  - theme/small-models
  - theme/context-architecture
  - maturity/growing
  - verdict/unevaluated
created: 2026-06-03
---

# Move intelligence out of the weights and into the scaffolding

**What it is.** Compile the craft into the exemplars and assembly rules so the model only has
to do the one thing small models are now genuinely good at: **fluent, in-voice continuation.**
The dumber the model, the more good context engineering pays rent. Calibration is
**model-specific** — the same scene wants more explicit edge for a small model, more restraint
for a frontier one — so register keys should be **tunable/swappable per target model.**

**The "blankets bug" (worked failure to remember).** An elegant withhold ("nobody offers you
the rest of it") *is itself* an instruction to withhold; a small model obeys the *form* and
the intended subtext evaporates (raiders read as mere "thieves," the violence glossed). Same
root as "form is the lesson" ([[0008-form-is-the-lesson]]). Fix: make the load-bearing thing
*materially present and plainly depicted*, not implied — and teach it via a *plain exemplar*,
never a description of one.

**Where it comes from.** [[sample-book]] §5.

**Why it matters for next-gen.** This is the *why* behind the whole exemplar/docs-as-code
stack ([[0005-exemplars-over-instructions]], [[0010-docs-as-code-context-compiler]]): if the
scaffolding carries the craft, the framework isn't locked to frontier models — which feeds
[[0004-frontend-agnostic-core]] *and* model-agnosticism (run local). Per-model calibration is
a concrete requirement on the cell schema.

**Open threads.** Per-model register variants multiply the grid — how is that managed without
combinatorial explosion? Who tunes (author, or an automated calibration pass)?
