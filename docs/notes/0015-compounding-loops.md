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

# Compounding loops — when a small misread reinforces itself turn over turn

**What it is.** A failure family distinct from one-shot errors: a small misread *feeds back*
and worsens each turn until the scene degrades — a spiral the user often can't break from
their side (their being-stuck *is* the input). The **tell is cumulative drift in one
direction.** Two documented instances:
- **Monologue death spiral** — player retreats to thought → GM reads "suppress dialogue" →
  goes silent → nothing to react to → player retreats further.
- **Pacing spiral** — a *relative* "slow down" applied as a recursive direction → each beat
  slower than the last → glacial.

**The cures share a shape:** break the reinforcement, GM-side. Keep dialogue alive regardless
of input density; treat a correction as a **target to hold, not a gradient to keep walking**
("don't rush" = reach the right tempo *and hold it*, not be-slower-than-last-time forever).

**Where it comes from.** [[gm-skill-RATIONALE]] §"The second enemy"; instances in
[[gm-skill-SKILL]] (monologue death spiral, pacing spiral).

**Why it matters for next-gen.** A reusable runtime-health lens: **"when a misbehavior gets
*worse over a session* rather than just being wrong once, suspect a loop, not a bad rule."**
That diagnostic should inform any self-monitoring/anti-drift layer. The "target not gradient"
fix also immunizes regardless of *where* the bad instruction lives (memory, bundle, old
turns) — a skill-level cure beats source-hunting. Counterpart to [[0014-scope-stripping]];
relates to [[0009-jit-context-and-eviction]] (beats/pacing as the monitored signal).

**Open threads.** What's the cheapest automatic detector of "cumulative one-directional
drift" (e.g. scene-header dates barely advancing)? Could the system flag loops itself?
