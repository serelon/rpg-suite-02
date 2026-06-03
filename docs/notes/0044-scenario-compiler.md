---
tags:
  - kind/idea
  - source/new
  - theme/composition
  - theme/architecture
  - theme/single-source-of-truth
  - maturity/seed
  - verdict/adopt
created: 2026-06-03
---

# The scenario compiler — a universal build process is how consumers "refer back"

**What it is.** (User, answering the module-contract question:) the refer-back mechanism is a
**build process / composer** — "like the bundler, but bigger, more universal. Like a compiler
for a code project, except we compile RPG scenarios." A session/scenario isn't hand-assembled
from modules; it's **compiled**: modules are the sources, the spec is the target platform, and
the compiler resolves references, pulls the right versions of guides/skills/data, and emits
the playable artifact (bundle, briefing, context).

**Where it comes from.** User instinct during appraisal of
[[modular-self-evolving-architecture]]. Direct lineage: [[0039-bundle-template-composition]]
is the working seed (inheritance + multi-chain merge + reference-following *is* a primitive
linker), and [[0010-docs-as-code-context-compiler]] predicted it verbatim ("compiled per-beat
like a build target", "a prompt build system").

**Why it matters for next-gen.** It closes the biggest soft spot in the thesis: *how* does a
consumer refer back ([[0036-every-subsystem-is-a-module]])? Answer: **consumers don't reach
into modules at all — the compiler resolves the references at build time.** Workflows declare
needs; modules declare what they provide; the compiler binds them
([[0034-outgrown-scaffold]]'s "declare a need, the system binds", realized). It also gives
[[0042-async-fleet-migration]] teeth: a campaign's spec-version is its *compile target*.

**Open threads (the dangers, named early).**
- **The compiler must stay dumb.** If it accretes per-module/per-campaign special cases, it
  *becomes* the next outgrown scaffold (`0034` reborn as a build system). Inversion of
  control: modules carry declarative manifests; the compiler only resolves.
- **Version skew is the hard problem.** Campaign on spec v3, memory module v5, bound skill
  pinned to v4 — what does the compiler do? Nobody owns this yet.
- **Build path: deliberately undecided.** I argued `0031` favors evolving `bundle.py`; the
  user pushed back: bundle.py is "wonky-ish — works, works well, but has flaws," and the
  evolve-vs-greenfield call should wait for a **detailed analysis of those flaws**. Owed: a
  bundle.py audit note before this decision.
- **What's the compilation unit** — a session bundle? a beat ([[0009-jit-context-and-eviction]])?
  a briefing? Possibly all three (build targets).
- **Two delivery modes:** compile-time (static bundle) *and* runtime — an executable
  `briefing.py` with inline tool calls ([[0045-runtime-composition-briefing-py]]). The
  precompiled-vs-JIT split, again ([[sample-book]] §1).

**Verdict.** `adopt` (as direction) — right shape for refer-back. Contract + version-skew unsolved; build-path (evolve bundle.py vs greenfield) deliberately undecided pending a bundle.py flaw audit. *(appraised 2026-06-03)*
