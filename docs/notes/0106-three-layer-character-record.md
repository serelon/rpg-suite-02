---
tags:
  - kind/pattern
  - source/conversation
  - theme/progression
  - theme/data-driven
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-12
---

# The three-layer character record: mechanical / semantic / prose

**What it is.** A character (and its progression) is recorded in **three distinct layers**,
each on its right substrate:

| Layer | What it is | Substrate |
|-------|-----------|-----------|
| **Mechanical** | the stats that progress | defined **statblock**, inline JSON schema, CRUD-able, readable directly *or* via tools |
| **Semantic** | what the stats *mean* / how the GM interprets them | an **interpretation contract** attached to the stat (candidate encoding: [[0099-pseudocode-as-encoding]]) |
| **Prose** | voice, appearance, texture | **curated prose**, only where prose *is* the payload |

**Where it comes from.** Interview 2026-06-12. The user's forward answer to "what is
'marking' if not a star or a prose sentence?": *"a defined stat, or statblock — inline JSON
schema, accessible both via direct reading or tools… but key insight is we need multiple
layers: stats for progression, their meanings for interpretation, layers of prose where it
matters (voice, appearance)."*

**Why it matters for next-gen.** It explains every prior failure as a *missing or collapsed
layer*:
- **Tarot** ([[0105-tarot-progression-unifying-failure]]) = broken mechanical layer, **no
  semantic layer**, everything collapsed into prose.
- **Freeform** = mechanical + semantic layers off, prose carries all of it.
- **Aegis** = solid mechanical layer **and** semantic layer (the rules *are* the
  interpretation contract) — which is exactly why "Tarot's lessons are fixed in Aegis."

The **semantic layer is the one Tarot fatally lacked** — a stat with no contract for what it
*does* is just decorative. Naming it as a first-class layer is the core insight. This is the
per-character expression of [[0104-progression-as-pluggable-layer]] (the dial sets how heavy
the mechanical+semantic layers are) and the canonical-vault data model
([[knowledge-base-canonical-vault]], [[0085-knowledge-entries-vs-tool-data]]).

**Open threads.** Does the semantic layer live *with* each campaign's ruleset (Aegis-style,
authored once) or *with* each stat (portable contract)? Granularity: one statblock per
character, or per-subsystem? How the layers map onto the cherrypick contract
([[0090-cherrypick-contract-three-layers]] — frontmatter/json-blocks/sections is suggestively
the *same* three-way split). Does the prose layer obey the prose-deprecation doctrine
([[0107-prose-deprecation-doctrine]])?

**Verdict.** _(unevaluated.)_
