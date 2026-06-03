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

**Grounding from a structural read (the modules are already *latent*).** rpg-tools today is:
`scripts/` (12 tools) + shared `scripts/lib/` + `references/` (all the guides) + `skills/`
(bundled skills) + `modifiers/`, packed by `build-skill.sh`/`bundle.py` into one `.skill`.
Three findings:
- **rpg-tools is the canonical guide home.** `references/` holds `memories-guide.md`,
  `character-guide.md`, etc. — confirming `solorpg` *copied* from here and diverged
  ([[0034-outgrown-scaffold]]). The reorg makes each guide travel **with its module**.
- **Per-subsystem material is already co-located** — tool + guide (+ sometimes a bound skill)
  per subsystem. So modularizing **promotes latent structure to explicit modules**, it doesn't
  invent it.
- **Bound-skill precedent already ships.** `skills/character-creator.md` (a `model: haiku`,
  `allowedTools`-scoped extraction skill bound to the character subsystem) and
  `skills/next-scene.md` (a workflow skill) exist *inside* rpg-tools. And `next-scene`
  literally says **"use the dice skill if available"** — a live, embryonic example of the
  `0036` **refer-back contract** (one module referencing another, not copying it). *(Caveat
  per user: next-scene is a small, as-yet-untested trick — illustrative of the contract, not
  proof of a mature pattern.)*

**Why it matters for next-gen.** This is **`0036` made concrete on the toolbox** — the first
real migration target and proving ground for the module principle. The "memory module" of
[[0034-outgrown-scaffold]] is exactly one of these: `memories.py` + its create-memory skill +
its guide/extraction-philosophy + design-docs, packaged as **one** self-owning skill, so the
divergence that started this whole thread can't recur. Each per-tool skill is also
independently loadable on a frontend ([[0004-frontend-agnostic-core]]), and the set composes
into a session bundle as needed.

**Open threads (the real design work).**
- **Granularity scales with capability, not uniformly.** (User:) **dice** will only ever need
  *one* skill — wrap the tool, state the syntax, done. **memories** needs *multiple* skills
  (capture, query, the create-memory authoring flow…). So a module's skill-count tracks how
  stateful/rich the subsystem is: thin instruments → a single wrapper skill; stateful
  subsystems → a small suite. Not "one skill per tool" flatly.
- **Frontend-target axis: Desktop-skills vs Code-skills.** (User:) some of a module's skills
  are exposed as **Claude Desktop** skills, others as **Claude Code** skills. So a module
  declares not just *what* skills it has but *which frontend each targets* — the packaging-side
  face of [[0004-frontend-agnostic-core]]. A module is a unit that can emit skills to more than
  one surface. (E.g. play-time capture → Desktop; postprocess authoring → Code.)
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
