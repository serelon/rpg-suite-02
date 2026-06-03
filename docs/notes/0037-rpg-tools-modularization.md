---
tags:
  - kind/idea
  - source/new
  - source/rpg-tools
  - theme/architecture
  - theme/extensions
  - theme/packaging
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-03
---

# rpg-tools modularization — split the monolith skill into one skill per tool/workflow

**What it is.** `rpg-tools` today is **one Claude Desktop skill** (a single `SKILL.md` +
`scripts/` for ~8 tools — dice, tarot, oracle, namegen, characters, locations, memories, pool
— plus shared `lib/`, `guides/`, `modifiers/`, built via `build-skill.sh`/`bundle.py`). The
user wants to **split it into one skill per tool or workflow** instead — each a self-contained
module.

**Where it comes from.** User intent, tied explicitly to [[0036-every-subsystem-is-a-module]]:
"the 'everything is a module' also ties into how I want to reorganize rpg-tools… currently a
bunch of tools packed into *one* desktop skill; I want to split that into one skill per tool
or workflow." (We previously mined *patterns* from rpg-tools — [[0001-tiered-progressive-loading]],
[[0002-read-anywhere-write-canonical]] — but never its packaging.)

**Why it matters for next-gen.** This is **`0036` made concrete on the toolbox** — the first
real migration target and proving ground for the module principle. The "memory module" of
[[0034-outgrown-scaffold]] is exactly one of these: `memories.py` + its create-memory skill +
its guide/extraction-philosophy + design-docs, packaged as **one** self-owning skill, so the
divergence that started this whole thread can't recur. Each per-tool skill is also
independently loadable on a frontend ([[0004-frontend-agnostic-core]]), and the set composes
into a session bundle as needed.

**Open threads (the real design work).**
- **Granularity: per-*tool* vs per-*workflow*.** "One skill per tool" (dice, oracle…) vs "one
  per subsystem/workflow" (a *memory* module = `memories.py` + create-memory + guide). The
  `0036` framing favors the latter for stateful subsystems; pure instruments (dice, oracle)
  may be fine as thin per-tool skills. Likely a mix.
- **Shared `lib/`** (`discovery.py`, `lookup.py`, `parsers.py`) — a common dependency across
  modules. Is that itself a module, a vendored lib, or duplicated? (Duplication is the very
  sin `0036` forbids.)
- **Cross-tool integration** — rpg-tools tools are *interconnected* (bidirectional
  characters↔memories↔locations lookups). Splitting must preserve modules **referring back**
  to each other (per `0036`), not copying — a concrete test of the "refer back" contract.
- **Composition/bundling** — how independently-packaged skills get assembled for a session
  (cf. `solorpg`'s bundle templates; [[0010-docs-as-code-context-compiler]]).
- A deeper structural mine of rpg-tools (bundling system, build, lib, cross-tool wiring) is
  still owed — flagged, not yet done.
