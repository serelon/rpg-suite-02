---
tags:
  - kind/question
  - source/solorpg
  - theme/campaign-isolation
  - theme/workflow
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-03
---

# Information-boundary enforcement — known unmet need

**What it is.** Several campaigns have **information that must not leak** across POVs or
saves: Ragna's secrets must stay out of Freyke's savefile (rust-and-ruin); cross-branch
events are visible to some branches and not others (the-long-watch, the-silence); sealed
secret files gate lore until a trigger (radiance, rust-and-ruin's ashblind). But the workflow
**doesn't enforce any of this** — the boundaries live as prose warnings in `CLAUDE.md`, and
the only safety net is human review after the fact. A Lorekeeper could write a secret into the
wrong save and nothing would catch it.

**Where it comes from.** `solorpg` survey — flagged as a recurring *unmet* need across
multi-branch campaigns. One proposed shape: a `character-boundaries.json`
(`{ragna: {secrets: [...], visible_to: [...]}}`) the workflow could validate against.

**Why it matters for next-gen.** It's the per-character/per-branch face of **campaign
isolation** — the same concern as cross-campaign leakage in `E:\rpg` and memory-soup in
[[0003-scope-memories-to-context]], but *within* a campaign. It also rhymes with
[[0020-observed-vs-actual]] (who-knows-what as data) and the multi-branch class in
[[0027-recurring-exception-taxonomy]]. A next-gen system that takes scoping seriously should
make boundaries **declared and checkable**, not just narrated.

**Open threads.** Is this a validation gate ([[0028-checkpointed-human-gates]]), a data-model
property ([[0020-observed-vs-actual]]), or both? Granularity: per-secret, per-character,
per-branch? How does a *reveal* (secret becomes known) propagate? Tension: hard enforcement
vs. the GM deliberately bending it for story.
