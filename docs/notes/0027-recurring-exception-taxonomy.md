---
tags:
  - kind/reference
  - source/solorpg
  - theme/workflow
  - theme/exceptions
  - maturity/growing
  - verdict/unevaluated
created: 2026-06-03
---

# Recurring exception taxonomy (solorpg workflow friction)

**What it is.** The catalogue grounding [[0026-exceptions-are-features]] — the *classes* of
per-campaign deviation found across all 19 campaigns. Recurring, so they're candidate
first-class features for next-gen (not one-off quirks):

- **Non-linear chronology** — session number ≠ in-world time; prep must filter context by
  *era*, not recency. (eternal-witness, timewalkers; implicitly pale-horizon, the-silence.)
  Needs a `timeline.md`, era-aware recency weighting. Cousin of `gm-skill`'s exact-stamp rule.
- **Multi-branch shared-state + information boundaries** — parallel POVs share campaign state
  (band/fleet/faction) but must not leak secrets across saves. (rust-and-ruin's `band-save`,
  the-long-watch's 10 global-numbered branches, the-silence's 5 subsettings.) → [[0029-information-boundary-enforcement]].
- **Custom postprocess outputs** — extra extraction beyond summary/savefile/memories:
  tactical debriefs (aegis), story collections (eternal-witness), `echo` memory type
  (lumina-city), XP reports (sutherlands-cairn).
- **Live game state / multi-repo** — authoritative data files restored before narrative
  (aegis data-export zip); mechanical state in a sibling repo (sutherlands-cairn ↔ megamek).
  → ties to [[0024-pluggable-extension-modules]] (the module brings its own state + repo).
- **Sealed / conditional content** — files not to be read until a trigger (radiance
  `secrets/truth.md`, rust-and-ruin `ashblind.md`). Spoiler-prevention as a load rule.
- **Deep bundle-template inheritance** — beyond base→branch→session: subsettings, sub-branches,
  timestamped location snapshots (the-silence, threadlight `as_of`).
- **Dual-identity / persona splits** — one character, two registers (lumina-city
  Nyx/Lingxia, doll-persona vs. person); monolithic profiles can't hold it.
- **Tone / pacing bounds** — explicit "advance, don't linger" / "slow burn" / "hope before
  horror" guardrails (nightshift, rust-and-ruin, radiance).
- **Naming / namespace scope** — nested namesets the flat resolver can't express
  (the-silence blocked on rpg-tools nested-namespace support).

**Why it matters for next-gen.** Several of these are *the same shape from different angles*
(data-by-volatility, knowledge-scope, persona-splits) — strong evidence for naming them as
features. Many also recur in other sources (non-linear ↔ stamps; personas ↔ observed/actual).

**Open threads.** Which deserve formal support vs. staying prose? Some (sealed content, tone
bounds) may be irreducibly judgment-driven. A "memory type registry" and "exception-profile
schema" are the recurring unmet-tooling asks.
