---
tags:
  - kind/pattern
  - source/aegis-tools
  - theme/rules-engine
  - theme/emergent-lore
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# DataRequired — missing data halts and *prompts the GM to author*, never fails silently

**What it is.** Operations declare **tiered data requirements** (log a contact needs `id,
region`; attempt intercept additionally needs `actual.evasion`; resolve attack needs
`actual.soak`). When a required field is missing, the engine raises **`DataRequired` — "not
an error, a prompt for GM decision"** — carrying the missing fields *and the exact
`define ...` commands to supply them*, on a **distinct exit code (2)**, separate from real
errors (1). So the rules engine never fabricates a stat and never crashes; it **stops and
asks the GM to define the lore**, then continues.

**Where it comes from.** `aegis-tools` — designed in `docs/plans/2025-12-28-data-driven-types`,
implemented in `lib/validation.py` (`DataRequired`, `require_fields`).

**Why it matters for next-gen.** This is the **reconciliation of a rules engine with
narrative-first / emergent play** — the central tension across the source repos (cf.
`rpg-tools`/`gm-skill` being deliberately ruleless). The engine enforces structure *only when
an operation actually needs it*, and turns each gap into authored worldbuilding rather than a
blocker. Directly answers the open thread in [[0018-layered-skill-architecture]] ("can a rules
engine plug in as a module?") — yes, if it defers like this. The actionable-error pattern
(tell the caller exactly how to proceed) is reusable far beyond games.

**Open threads.** Who answers the prompt mid-session — GM by hand, or the model authoring
provisionally then flagging? Tension with flow: a hard stop mid-combat could jar. Could tiers
be *soft* (proceed with a provisional value, mark it `observed`)? Pairs with
[[0020-observed-vs-actual]].
