---
tags:
  - kind/pattern
  - source/new
  - source/claude-desktop
  - theme/skill-authoring
  - theme/docs-as-code
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# Ship a companion "why" doc as an anti-regression device

**What it is.** Pair a built artifact (a skill, a tool, a ruleset) with a companion document
that records *why each choice is the way it is* — and explicitly **"read this before
revising."** The rationale exists because many deliberate choices *look* cleanable toward
something more conventional, and the conventional version is exactly what was diverged from on
purpose. Without the why on record, a future revisit (the user's *or* a model's) quietly
"fixes" the artifact back toward the norm it was built to resist. The companion doc encodes
intent so edits can preserve it.

**Where it comes from.** [[gm-skill-RATIONALE]] is the worked example — it opens by stating
exactly this purpose. The user flagged the *practice itself* as "a good idea too."

**Why it matters for next-gen.** A first-class **documentation pattern** for the whole
framework: every counter-default artifact should carry rationale that protects its divergences.
It's the artifact-level analogue of [[0013-counter-training-name-the-default]] (explain the
why so intent survives) — there it protects behavior against context drift, here it protects
the *source* against well-meaning future edits. Validates this project's `docs/design-notes/`
choice: rationale is preserved, not discarded. Also rhymes with `kind/decision` notes (record
*why* a choice was made) — a rationale doc is a dense cluster of decisions.

**Open threads.** Where do rationale docs live relative to the artifact (co-located, or in
the knowledge vault)? How do you keep them in sync as the artifact evolves — or is drift
between artifact and rationale itself a useful signal?
