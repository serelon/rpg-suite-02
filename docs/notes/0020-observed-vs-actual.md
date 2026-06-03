---
tags:
  - kind/pattern
  - source/aegis-tools
  - theme/rules-engine
  - theme/data-driven
  - theme/fog-of-war
  - maturity/growing
  - verdict/unevaluated
created: 2026-06-03
---

# Observed vs. Actual — model fog-of-war into the data, not the prose

**What it is.** Every emergent entity (enemy, alien craft, recovered xenotech) carries **two
parallel field sets**: `observed` (what the characters currently *know* — partial, possibly
wrong) and `actual` (what's *true* — often empty until discovered). Field observations in
`state/` link to reference types; research/analysis migrates facts from `actual` into the
known picture. A "scout" can be `observed: {size: small, speed: fast}` with `actual: {}`
until intel develops.

**Where it comes from.** `aegis-tools` data-driven-types design (`docs/plans/2025-12-28`),
implemented in `lib/validation.py` (dotted-path checks like `actual.evasion`).

**Why it matters for next-gen.** A clean, *structural* answer to fog-of-war and progressive
revelation: knowledge state is first-class data, not something the GM has to hold in their
head or fake in narration. Generalizes beyond combat — any "what the PC knows vs. what's
true" gap (NPC motives, hidden lore) could use it. Sits next to
[[0011-identity-pinned-state-evicted]] (another what-rides-where split) and feeds the
campaign-isolation/knowledge-scoping concerns of [[0003-scope-memories-to-context]].

**Open threads.** Who authors `actual` — the GM up front (then it's a secret to reveal), or
JIT at discovery time (emergent)? Does `observed` belong in `state/` (per-campaign knowledge)
while `actual` is reference truth? Pairs tightly with
[[0021-data-required-as-prompt]] (the tiers that gate when `actual` must exist).
