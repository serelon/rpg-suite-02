---
tags:
  - kind/pattern
  - source/solorpg
  - theme/workflow
  - theme/knowledge-layer
  - theme/docs-as-code
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# A workflow should be a lean spine that defers to canonical guides at point-of-use

**What it is.** The postprocess skill doesn't *embed* the schemas and craft it needs — it
**reads the canonical guide at the step that needs it**: "read `prompts/memory-extraction-guide.md`
and `templates/memory-template.md` before drafting memories"; "read
`rpg-tools/guides/location-guide.md` before drafting locations"; same for characters. Each
body of knowledge lives **once**, in its canonical home; the workflow stays thin and pulls it
**JIT**. A "Reference: Existing Guides" table maps guide → location → use-for.

**Where it comes from.** [[session-postprocess]] v1 (Steps 4.3a / 4.4b / 4.5c; the Existing
Guides table). The skill is mostly *orchestration*; the *knowledge* is elsewhere.

**Why it matters for next-gen.** The right instinct: **single source of truth for knowledge,
referenced not duplicated** — a workflow composes behavior from a knowledge layer rather than
hardcoding it. It's [[0010-docs-as-code-context-compiler]] applied to a *workflow's* own
inputs, and JIT loading ([[0001-tiered-progressive-loading]], [[0009-jit-context-and-eviction]])
applied to instructions, not just data. Keeps the orchestration legible and the guides
authoritative. **But** the *mechanism* of deferral here has hit its limits — that's the
crucial sequel, [[0034-outgrown-scaffold]]. (Pattern good; current implementation strained.)

**Open threads.** What's the deferral *mechanism* in next-gen — hand-wired "read this path"
(today), or a resolver where the workflow declares a need ("memory schema") and the system
binds it? The latter is what [[0034-outgrown-scaffold]] argues for.
