---
tags:
  - kind/design-note
  - source/solorpg
  - theme/workflow
  - theme/knowledge-layer
  - theme/scaffold
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
origin: solorpg/.claude/skills/session-postprocess/SKILL.md
preserves:
  - "[[session-postprocess-SKILL]]"
atomized-into:
  - "[[0033-workflow-defers-to-canonical-guides]]"
  - "[[0034-outgrown-scaffold]]"
  - "[[0035-surgical-git-staging]]"
related:
  - "[[0028-checkpointed-human-gates]]"
  - "[[0030-summary-as-compression]]"
  - "[[0032-preprocessing-token-hygiene]]"
---

# session-postprocess (v1) — wrapper / index

> **Preserved flagship workflow** — the user's single most-used, most-important workflow.
> Verbatim in [[session-postprocess-SKILL]]. (v1 is the *live* one; the v2 team variant is
> obsolete — see [[0031-beware-transient-constraint-architecture]].)

**What it is.** The constantly-used session-postprocess skill: a 6-phase interactive workflow
(setup → discovery → validation → capture → bundle-integration → completion) that turns a
session export into structured campaign content (summary, savefile, memories, locations,
characters, + campaign-specific outputs). ~1087 lines.

**Why it matters for next-gen.** Two things, captured separately:
1. **The good pattern** — it's a *lean spine that defers to canonical guides* at point-of-use
   rather than embedding schemas ([[0033-workflow-defers-to-canonical-guides]]). The
   knowledge lives once, in `rpg-tools/guides/`, `prompts/`, `templates/`; the workflow pulls
   it JIT.
2. **The headline lesson (user: "fixate on this")** — that deferral works only *so-so*
   because **the system has outgrown the scaffold** ([[0034-outgrown-scaffold]]): the
   composition mechanism is hand-wired paths + a manually-maintained guide index + inline
   per-campaign branches, and it can't keep pace with the growing knowledge base and campaign
   variety.

Already-captured patterns this workflow also exhibits: human-gated capture
([[0028-checkpointed-human-gates]]), summary-as-compression ([[0030-summary-as-compression]]),
preprocessing ([[0032-preprocessing-token-hygiene]]). New small op-pattern:
[[0035-surgical-git-staging]].

**Open threads.** The per-campaign exception handling is hardcoded inline (Eternal Witness,
AEGIS examples in prose) — same smell as [[0026-exceptions-are-features]]. Phase 5
(bundle-integration) is itself a content-composition layer worth a later look.
