---
tags:
  - kind/pattern
  - source/aegis-tools
  - theme/rules-engine
  - theme/data-driven
  - theme/docs-as-code
  - maturity/growing
  - verdict/unevaluated
created: 2026-06-03
---

# Reference vs. State, and types-as-data — the rulebook is editable at runtime

**What it is.** Two-axis data split:
- **`reference/`** = the *rulebook* — type templates (vehicle-types, weapon-types, enemies…).
  Changes only when a new type is *discovered*.
- **`state/`** = the *savegame* — instances and observations. Changes every session.

Instances reference types (`{id: komet-1, type: komet, fuel: 6}`); operations validate
against the type definition. Crucially, **types are loaded from data, not hardcoded** — the
explicit refactor goal was "hardcoded type definitions → runtime-loadable data files, enabling
emergent gameplay where lore is built during play." New types can be `add`ed, `update`d, even
`merge`d (two labels turn out to be the same craft) from the CLI, mid-campaign.

**Where it comes from.** `aegis-tools` data-driven-types design (`docs/plans/2025-12-28`).

**Why it matters for next-gen.** The **rules-axis instance of docs-as-code**
([[0010-docs-as-code-context-compiler]]): the *ruleset itself* is structured, editable data,
so the system is moddable and the lore grows during play without code changes. The
reference/state split is a cousin of [[0011-identity-pinned-state-evicted]] (stable vs.
volatile) and of `rpg-tools`' read-anywhere/write-canonical ([[0002-read-anywhere-write-canonical]]).
"Types as data" is what lets [[0018-layered-skill-architecture]]'s mechanics-module be
per-campaign.

**Open threads.** Where's the line between "reference grows on discovery" and a fixed core
ruleset? Versioning/retcon of a type after instances exist (the `merge` op hints at this).
How does this meet `E:\rpg`'s entity-registry approach to the same template/instance problem?
