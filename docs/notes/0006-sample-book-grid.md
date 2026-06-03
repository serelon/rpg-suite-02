---
tags:
  - kind/idea
  - source/new
  - source/sillytavern
  - theme/voice-register
  - theme/context-architecture
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-03
---

# The Sample Book: a (scene-type × register) grid of voice exemplars

**What it is.** A first-class library of concentrated register exemplars, indexed on a
**scene-type × register grid**. Each cell answers "write a type-A scene in B-style" with a
*worked passage*, not a description. Assembly has two modes (the same precompiled/JIT split
that runs through the whole architecture): **precompiled** — a campaign-level style profile
loading default register keys for the campaign's tone; **on-demand (JIT)** — pull the
specific cell when a scene-type fires.

**Where it comes from.** [[sample-book]] §1. The voice-layer instance of the broader
context architecture ([[0010-docs-as-code-context-compiler]]) — "a prompt build system for
voice," applied to *registers* instead of *facts*.

**Why it matters for next-gen.** A concrete, buildable artifact that operationalizes
[[0005-exemplars-over-instructions]]. The grid is the data structure; the rest of the notes
are how it gets filled and used.

**Open threads.** What's the cell schema (frontmatter: scene-type, register, tags, load
conditions)? How do scene-types get named/detected at runtime? Relation to namesets/pools in
`rpg-tools` (also tagged, retrievable libraries). Built status: not built — `seed`.
