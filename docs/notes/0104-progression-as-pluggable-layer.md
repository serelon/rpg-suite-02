---
tags:
  - kind/idea
  - source/conversation
  - theme/architecture
  - theme/progression
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-12
---

# Progression is a pluggable layer dialed off → light → heavy

**What it is.** The user's progression systems across generations aren't a sequence of
replacements — they're **three points on one axis: how heavy the progression module is.**
- **Freeform** = module *off* (story-driven growth, prose layer only).
- **Tarot Tales** = a *light* module (star-rated aspects, Discoveries, traits) — but it
  rotted (see [[0105-tarot-progression-unifying-failure]]).
- **Aegis** = a *heavy* module (full rules engine: CRUD statblocks, auto-xp/levelling),
  welded to one specific ruleset (1940s tactical).

Next-gen shouldn't pick one. It should own **the axis itself**: progression as a
*pluggable layer* dialed per campaign — off (freeform), a light kit, up to full Aegis.

**Where it comes from.** Interview, 2026-06-12, mapping the user's progression history.
Aegis reframed: it stops being "the weird exception that follows its own rules" and
becomes **the maxed-out setting of a dial that also has an off position.**

**Why it matters for next-gen.** This is [[0024-pluggable-extension-modules]] (the
north-star: freeform core that can slot in a rules engine) applied specifically to
*progression*. It also resolves the generic-vs-specific tension the user named ("Aegis is
a specific engine, not a generic system"): you don't generalize Aegis's *rules* — you
extract the **pattern** (`defined statblock + interpretation contract + prose layers`, see
[[0106-three-layer-character-record]]) and let each campaign supply its own content into
that shape.

**Open threads.** Is progression clean enough to be a *dial*, or is it too entangled with
the rest of the character record to factor out? (User bought the dial framing.) How does a
campaign *change* its dial setting mid-life (freeform campaign that wants to slot in stats
later)? Where does the semantic/interpretation layer live when the dial is "light" — and
can [[0099-pseudocode-as-encoding]] carry it? Aegis as a *source* worth a dedicated
character-sheet/xp design note (the proof-of-fix).

**Verdict.** _(unevaluated.)_
