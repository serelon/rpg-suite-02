---
tags:
  - kind/principle
  - source/solorpg
  - theme/architecture
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-06
---

# The engineer and the gardener — load-bearing doctrine of solo play

**What it is.** One of the user's "more loadbearing doctrines" for solorpg (2026-06-06),
two complementary modes:

- **Engineering-first** — worldbuilding, design, crafting things (including session-0
  primers). Happens **OOC, often in workshop threads**.
- **Gardener** — "takes tiny seeds, maybe just a phrase, often prepped by the engineer.
  and grows story elements from that while we play, organically, in a way that makes
  sense." Happens **IC, often in GM threads**.

"Both depend on each other." The common loop:

> engineer seeds 'protagonist A, has skill B, circumstance C, trait D, E, F'
> gardener puts that into a session, plays, extrapolates and improvises from that. and in
> the session post-process step, instead of that one-line seed, we now extract a
> 1000-word character profile of a very complex character

So the full cycle is **engineer seeds → gardener grows → librarian harvests**
([[0075-postprocessing-as-vault-librarian]] is the harvest step — the 1000-word profile
is what post-processing extracts back into canon).

**What it names retroactively.** This doctrine is the thread tying earlier captures
together:
- [[0049-disposable-bootstrap-primer]]'s "skeleton vs flesh" = engineer builds bones,
  gardener grows flesh; the session-0 primer is engineer output *designed to be consumed
  by the garden*.
- [[0048-canon-precedence-and-naming-is-permission]]'s "primers are design intent, not
  canon after play" = engineer artifacts are demoted once the gardener has grown past them.
- [[0078-zoom-out-first-worldbuilding]] / [[0079-relational-anchoring-antipattern]]:
  "worldbuilding is different from gameplay" (user) — the engineer wants *curated/excluded*
  context (evergreen, unanchored); the gardener wants *rich* context (everything the scene
  touches). The OOC/IC boundary is also a context-policy boundary.

**Why it matters for next-gen.** The two modes have different tooling needs and the spec
should treat them as first-class: engineering wants workshop entrypoints, exclusion modes,
checkpoint writes; gardening wants JIT loading ([[0060-jit-loading-retry]]), live deltas
([[0051-live-context-delta]]), seed-rich bundles. Seed quality is the interface contract
between them — what makes a seed *growable* ("a phrase" suffices) vs overdetermined is a
design question for the KB's seed format.

**Open threads.** What does a *bad* seed look like — overgrown engineering that leaves the
gardener nothing to do (the pre-session infodump failure of 0060?), or too-bare seeds that
grow wild ([[0052-evolution-vs-drift]])? Do gardener-grown elements need an engineering
pass before becoming canon (harvest-review = the postprocessing PRs)? Is the
[[0044-scenario-compiler]] an engineer tool, a gardener tool, or the bridge?

**Verdict.** _(unevaluated.)_
