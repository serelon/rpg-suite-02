---
tags:
  - kind/pattern
  - source/claude-desktop
  - theme/context-economy
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-04
---

# Mandatory presence, not length — tuning the thinking block without dropping enforcement

**What it is.** Field-diagnosed refinement of [[0016-thinking-as-enforcement]], from a live
drift incident (Lumina City s04): the campaign's most common counter-default rule
("transform the player's input, never transcribe") degraded mid-session **without any data
loss** — full context intact, the rule simply stopped *firing*. Trigger: a reasonable
"stop overthinking" instruction thinned the thinking blocks, and the **enforcement layer
went down with the fat**. Root mechanism: *attention is the scarce resource* — counter-default
rules exist only while actively held, so anything that reduces thinking (be-concise
instructions) or competes for attention (injected guidance, dense narrative) starves them
first.

The fix: **"length is not the lever — mandatory-presence is."** Thinking blocks as a short
checklist of mandatory boxes that always run, everything else as lean as it wants. Guard
both failure modes: too loose (sprawl returns) and rote (hollow box-ticking does no work).
Spec: **short, fixed, genuine.**

**Where it comes from.** [[gm-skill-thinking-tuning]] (preserved verbatim in design-notes) —
the first inbox report, written in Desktop before the research-report skill existed.
Extends the gm-skill family ([[gm-skill]], notes 0013–0019).

**Why it matters for next-gen.** Sharpens 0016 with an empirically observed failure mode:
enforcement doesn't fail by deletion, it fails by **attention starvation** — and
well-meaning efficiency tuning is a trigger. Any next-gen craft skill needs its
load-bearing checks marked *non-negotiable separately from* its verbosity dial; "be
concise" must never be able to shed the enforcement layer. Also a clean instance of
[[0014-scope-stripping]]'s cousin: an optimization instruction silently widening its scope.

**Open threads.** The report's candidate mandatory-check list (transform, live wire,
don't-mirror-density + standing guards) is campaign-tuned — does the *mechanism* (a
fixed always-run checklist with a free-form tail) belong in the spec as the standard
craft-skill shape? How does this interact with models' native thinking budgets changing
generation to generation ([[0031-beware-transient-constraint-architecture]] cuts both ways)?

**Verdict.** _(unevaluated.)_
