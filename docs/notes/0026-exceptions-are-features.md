---
tags:
  - kind/idea
  - source/solorpg
  - theme/workflow
  - theme/exceptions
  - theme/extensions
  - maturity/growing
  - verdict/unevaluated
created: 2026-06-03
---

# Exceptions are features — a workflow must absorb per-campaign deviation by design

**What it is.** `solorpg` has well-defined workflows (prep → play → postprocess → bundle),
but **each campaign hits ~a dozen points where the standard flow needs manual intervention**
(user's framing). The deviations aren't bugs — they're the campaigns being genuinely
different. Today they're absorbed by **ad-hoc prose escape-hatches**: a per-campaign
`postprocess-instructions.md` (5 campaigns) plus conventions buried in each campaign's
`CLAUDE.md` (all 19). It works for 1-3 special rules per campaign, but: every campaign
re-documents the same kinds of exception independently, exceptions are *invisible across
campaigns*, and the workflow skill itself still assumes standard structure and leans on the
agent to read the docs and adapt on the fly.

**Where it comes from.** `solorpg` skills + a survey of all 19 `campaigns/*/CLAUDE.md` and 5
`postprocess-instructions.md`. ~7 campaigns are nearly exception-free (linear, single-POV);
~12 carry one or more major exceptions.

**Why it matters for next-gen.** This is the **central workflow lesson**, and the sibling of
[[0024-pluggable-extension-modules]]: a stable core must tolerate variation *as a designed-in
capability*, not as prose patches. The proposed shift: from ad-hoc override docs to a
**declared exception-profile** per campaign (machine-readable: "multi-branch with shared
band-save", "non-linear, timeline-driven", "custom output: tactical-debrief") that
**parameterizes the workflow** — building the right discovery questions, output schemas, and
guardrails automatically. See the catalogue in [[0027-recurring-exception-taxonomy]]. It's
also [[0014-scope-stripping]] inverted: don't force the narrow-standard onto every campaign.

**Open threads.** Where's the line between "declare the exception and auto-adapt" vs. "let the
agent improvise from prose" (the prose is flexible; the schema is rigid — cf.
[[0021-data-required-as-prompt]])? Can exception-profiles be *detected* at setup, not just
declared? Risk: over-formalizing kills the improv that prose escape-hatches allow.
