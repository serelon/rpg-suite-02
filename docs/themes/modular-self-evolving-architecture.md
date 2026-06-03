---
tags:
  - kind/theme
  - theme/single-source-of-truth
  - theme/extensions
  - theme/self-evolution
  - theme/architecture
  - maturity/growing
  - verdict/unevaluated
created: 2026-06-03
synthesizes:
  - "[[0034-outgrown-scaffold]]"
  - "[[0036-every-subsystem-is-a-module]]"
  - "[[0024-pluggable-extension-modules]]"
  - "[[0037-rpg-tools-modularization]]"
  - "[[0038-shared-infra-vs-modules]]"
  - "[[0039-bundle-template-composition]]"
  - "[[0040-vector-db-as-lore-search-module]]"
  - "[[0041-self-evolving-versioned-spec]]"
  - "[[0042-async-fleet-migration]]"
  - "[[0043-campaigns-as-testbeds]]"
  - "[[0010-docs-as-code-context-compiler]]"
  - "[[0033-workflow-defers-to-canonical-guides]]"
  - "[[0026-exceptions-are-features]]"
---

# Modularity, Single Source of Truth, and the Self-Evolution Loop

> **First synthesis doc.** Gathers the densest cluster in the vault into one stated thesis.
> The underlying notes are still `verdict/unevaluated` — this is *what the research is
> pointing at*, not a ratified decision. It exists to be pressure-tested in appraisal.

## The thesis (what we believe so far)

**Every concern has exactly one home; everything else refers to it and composes from it; and
that web of homes stays current by promoting proven campaign experiments into a versioned
canonical spec.** Three moves — *single source of truth*, *composition over duplication*, and
*self-evolution* — that turn out to be one idea seen at different layers.

## The disease: scattered authority

The same failure recurred at every layer we mined, which is the strongest evidence it's *the*
problem:

- **Guides** — the memory guide is forked across repos into *incompatible* schemas, and the
  flagship workflow uses the stale local copy ([[0034-outgrown-scaffold]]). Knowledge lives in
  drifting copies with no authority.
- **Packaging** — rpg-tools crams ~12 tools into *one* skill ([[0037-rpg-tools-modularization]]);
  there's no clean unit of ownership.
- **Conventions** — every campaign follows different conventions and best practice survives as
  folklore: *"go look at campaign A for how they did X"* ([[0041-self-evolving-versioned-spec]]).
- **History** — session knowledge is trapped in flat files, not searchable as a whole
  ([[0040-vector-db-as-lore-search-module]]).

One disease, four faces: **forked/scattered authority with no single source of truth.**

## The cure: modules with one authority, composed not copied

- **Everything is a self-owning module** ([[0036-every-subsystem-is-a-module]]) — a subsystem
  owns its tool, its packaging, its bound (versioned) skills, its guide, its design-docs, in
  one place. **Consumers refer back, never copy.** This is the anti-drift invariant whose
  absence produced the memory-guide fork.
- **Modules scale from thin to thick** — a *dice* module is one wrapper skill; a *memory*
  module is a small suite; a whole rules engine (aegis) is just a **large** module
  ([[0024-pluggable-extension-modules]]). `0024` is subsumed by `0036`: pluggable extensions
  aren't special, they're big modules.
- **Composition over duplication** — sessions are *assembled*, not hand-built. The bundle
  system already prototypes this ([[0039-bundle-template-composition]]): inheritance +
  multi-chain merge (swappable sub-settings) + glob includes + **automatic reference-following**
  (the refer-back contract resolved at build time). This is [[0010-docs-as-code-context-compiler]]
  made real for content.
- **Honest unsolved seam** — horizontal shared infra (`lib/`: discovery, persistence,
  validation) cuts across vertical modules ([[0038-shared-infra-vs-modules]]). Foundation
  module? vendored lib? host's job? The module *contract* isn't defined yet.

A workflow, then, is a **lean spine that defers to its modules** ([[0033-workflow-defers-to-canonical-guides]])
— "read the memory module's guide," not "read this hardcoded path."

## Staying current: the self-evolution loop

A module-web and a spec would rot without a way to evolve. The loop has two arms:

- **Downward — spec → campaigns.** A single **versioned canonical spec** ("the current meta,
  refactor to this", [[0041-self-evolving-versioned-spec]]) propagates to campaigns by **async
  migration** ([[0042-async-fleet-migration]]) — each campaign upgrades on its own schedule,
  never a forced lockstep rewrite.
- **Upward — campaigns → spec.** Every campaign is an **architectural experiment**
  ([[0043-campaigns-as-testbeds]]); proven experiments **graduate** into the spec or become
  modules. (aegis grew an engine; the Gleaners campaign prototyped the entire sample-book.)

This **dissolves the apparent contradiction** between "uniform spec" and "every campaign is
unique": the spec is the *settled floor*; campaigns explore *above* it; proven experiments
promote down-to-up; the rest remain **intentional, declared exceptions**
([[0026-exceptions-are-features]]) — distinct from accidental drift only *because* a baseline
now exists.

## Why it's one idea

"Single source of truth, refer back, don't fork" is `0036` for **subsystems**, `0034`'s cure
for **guides**, and `0041` for **conventions**. "Compose, don't duplicate" is `0039`/`0010` for
**sessions** and `0024`/`0038` for **capabilities**. Self-evolution is just how the web of
single-source-of-truth homes *stays* singular as it grows. The four north-stars
([[0004-frontend-agnostic-core]], `0036`, `0024`, `0041`) are this one principle pointed at
surface, subsystem, extension, and convention respectively.

## What's still soft (carry into appraisal)

- **The module contract** — what a module exposes; how a consumer "refers back" (import?
  registry resolve? link?); where shared infra lives (`0038`).
- **The graduation mechanism** — how a campaign experiment is judged worth promoting, and
  whether it becomes spec-default / module / optional-extension. (Note the recursion: this
  project's own [[appraisal-protocol]] verdict gate *is* a graduation mechanism.)
- **Spec representation & versioning** — template? schema? a "campaign-zero" reference
  (`rpg-tools/references/campaign-zero-guide.md` may be a seed)?
- **Risk** — self-evolution is drift-prone; leans hard on review gates
  ([[0028-checkpointed-human-gates]]) and anti-regression ([[0019-companion-rationale-as-anti-regression]]).
- **The transient-constraint test** ([[0031-beware-transient-constraint-architecture]]) — re-run
  on every claim here before enshrining it.
