---
tags:
  - kind/idea
  - source/new
  - source/aegis-tools
  - theme/architecture
  - theme/extensions
  - theme/rules-engine
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-03
---

# Pluggable extension modules — freeform by default, slot in a whole engine when wanted

**What it is.** A **north-star requirement** (the user states it as a must, not a maybe): the
core runs **freeform** — the usual mode, no resolution system — but must be able to **slot in
an entire extension module**, up to and including a full rules engine the scale of
`aegis-tools` (roster, combat, strategic base-management, intel, time advancement). The
freeform majority and the heavy-crunch campaign are the *same system* with an optional module
attached — not two codebases.

**Where it comes from.** User framing on `aegis-tools`: "Aegis is different from my usual
campaigns in that it comes with this whole rules engine. Usually I do freeform, but this has
an extra module. The system we make must slot in a whole module like aegis-tools, if we want
to." So `aegis-tools` is the **proof case for the slot**, not a thing to copy wholesale.

**Why it matters for next-gen.** This is a top-level architectural constraint, parallel to
[[0004-frontend-agnostic-core]] — together they bracket the design: *frontend-agnostic* on
the surface side, *extension-pluggable* on the mechanics side, with a freeform core between.
It promotes [[0018-layered-skill-architecture]] from "nice separation" to a **hard
requirement**, and the aegis patterns become the *mechanism* for the slot:
- [[0023-event-bus-orchestrator]] — how a module attaches (subscribe, don't edit the core).
- [[0021-data-required-as-prompt]] — how a module enforces structure without breaking improv.
- [[0022-reference-vs-state-data-driven-types]] — a module brings its own per-campaign data.
- [[0020-observed-vs-actual]] — a module brings its own data model.

**Open threads.** What exactly is the *contract* of the slot — what does the core expose for
a module to bind to (events? state? the context build? the turn loop)? Can a module reach the
*narrative/voice* layer (e.g. inject combat tone), or only mechanics/state? Does "freeform" =
"the always-present zero-module baseline"? Granularity: one big module (aegis) vs. many small
ones (a wounds module, a faction-clock module) composed together? Strong candidate to become a
`kind/decision` once the contract is sketched.
