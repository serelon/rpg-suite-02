---
tags:
  - kind/pattern
  - source/new
  - source/claude-desktop
  - theme/skill-authoring
  - theme/context-economy
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# Counter-training: name the default pull, give the correction, explain the why

**What it is.** When a desired behavior *diverges from defaults baked into model training*,
a bare rule won't hold — under long context the trained reflex reasserts and overrides the
listed directive. The fix: author each divergence as **(1) name the default pull, (2) give
the correction, (3) explain the why.** An *explained* correction survives context pressure
because the model can **reconstruct the intent** rather than merely recall a directive.

**Where it comes from.** [[gm-skill]] — its central authoring technique, stated in
[[gm-skill-RATIONALE]] §"Core premise" and applied in nearly every section of
[[gm-skill-SKILL]].

**Why it matters for next-gen.** This is a *general* prompt/skill-authoring law, not
GM-specific — it governs how any counter-default behavior should be written across the whole
framework (and this project's own skills/docs). It reframes "skill = list of rules" into
"skill = durable counter-training." Pairs hard with [[0016-thinking-as-enforcement]] (the
explained rule still needs an interrupt to fire) and is the technique behind
[[0005-exemplars-over-instructions]]'s cousin problem (tacit knowledge resists bare rules).

**Open threads.** Cost: explained corrections are token-heavy — tension with context economy.
When is a bare rule enough vs. worth the full why? Does this compose with exemplars (show
*and* explain)?
