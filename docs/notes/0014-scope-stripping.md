---
tags:
  - kind/pattern
  - source/new
  - source/claude-desktop
  - theme/skill-authoring
  - theme/failure-modes
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# Scope-stripping — a named failure family (and its two faces)

**What it is.** A recurring failure where *something true in a narrow context loses its scope
and gets applied globally.* Naming it abstractly (once) beats patching instances. Two faces:

- **Always/never flattening.** Told "the default is X," the instinct writes "*never* X" — but
  the right answer is usually **conditional, with a reason.** (In gm-skill: recap, goals, and
  guardrail-review were each first-drafted as "cut it," correctly resolved as "keep it,
  conditionally.")
- **Temporary-going-permanent.** A correctly-scoped, one-moment instruction ossifies into a
  standing mode. (A "keep tonight chill" note becomes a "never escalate" law; a "timeskip
  this beat" becomes "summary mode forever.") Rule of thumb: **an override's default scope is
  the moment it addresses** — snap back after, unless told it's ongoing.

**Where it comes from.** [[gm-skill-RATIONALE]] §"recurring failure modes" — the deep enemy
under most of the skill's corrections.

**Why it matters for next-gen.** A reusable **diagnostic lens** for authoring *and* runtime:
when a rule collapses a conditional into on/off, or lets a scoped instruction become a
permanent mode, that's the enemy. Directly relevant to memory ([[0003-scope-memories-to-context]]
is a scoping failure of a sibling kind) and to [[0011-identity-pinned-state-evicted]] (stale
state = a temporary fact gone permanent). Counterpart to [[0015-compounding-loops]].

**Open threads.** Can scope be made *explicit metadata* (every instruction carries a scope:
moment / scene / session / permanent) so stripping is detectable mechanically?
