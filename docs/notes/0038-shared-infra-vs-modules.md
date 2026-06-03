---
tags:
  - kind/idea
  - source/rpg-tools
  - theme/architecture
  - theme/extensions
  - theme/packaging
  - maturity/proven
  - verdict/undecided
created: 2026-06-03
---

# Shared infrastructure vs. vertical modules — what happens to `lib/` when you split?

**What it is.** rpg-tools splits cleanly along one line that modularization has to reckon
with. **Instant instruments** (`dice`, `tarot`, `oracle`, `pool`) are **fully standalone** —
no imports — so they modularize trivially into thin per-tool skills. But the **8 data/stateful
tools** (`characters`, `locations`, `memories`, `stories`, `factions`, `namegen`, `log`,
`campaign`) *all* import a **shared `scripts/lib/`** (`discovery`, `lookup`, `parsers`,
`persistence`, `validation`, `calendars`). That `lib/` is **horizontal infrastructure cutting
across every vertical subsystem** — the exact thing that resists clean per-module splitting.

**Where it comes from.** rpg-tools structure (`grep` confirms which scripts import `lib`;
instruments don't, data tools do). The standalone/shared split maps onto the
instrument-vs-subsystem granularity in [[0037-rpg-tools-modularization]].

**Why it matters for next-gen.** [[0036-every-subsystem-is-a-module]] forbids duplication, so
shared `lib/` **can't be copied into each module**. Options, each a real trade:
- **A foundation/core module** every data-module depends on (clean, but introduces an
  inter-module dependency graph — modules referring back to a *core*, per `0036`).
- **A vendored/runtime library** outside the module system (simpler, but it's infrastructure
  the module system doesn't own — a seam to watch).
- **Push shared concerns into the host/core** (discovery, persistence, validation become the
  platform's job; modules carry only their domain logic).

This is the **vertical-modules vs. horizontal-concerns** tension every plugin architecture
hits. Resolving it is part of defining the module *contract* ([[0036-every-subsystem-is-a-module]]
open thread) and the layering ([[0018-layered-skill-architecture]]).

**Open threads.** Is `lib/` one foundation module or several (a `persistence` module, a
`calendars` module…)? Do instruments and subsystems even live in the *same* module system, or
two tiers? Does read-anywhere/write-canonical ([[0002-read-anywhere-write-canonical]], which
*is* `discovery`+`persistence`) become a platform guarantee rather than a per-module behavior?

**Verdict.** `undecided` — genuinely unresolved fork (foundation module / vendored / host-owned); decide together with the module contract. *(appraised 2026-06-03)*
