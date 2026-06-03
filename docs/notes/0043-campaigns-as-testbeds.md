---
tags:
  - kind/idea
  - source/new
  - theme/self-evolution
  - theme/architecture
  - theme/experimentation
  - theme/extensions
  - maturity/growing
  - verdict/unevaluated
created: 2026-06-03
---

# Campaigns are architectural testbeds — proven experiments graduate into the spec

**What it is.** (User:) *every* campaign has experimental/unique features that differ from the
rest — aegis (a whole rules engine) at one extreme, tiny bespoke details at the other, but
**each is architecturally different**. The reframe: this isn't mess to standardize away —
campaigns are the **experimentation / R&D layer**. The system must (a) support per-campaign
architectural divergence as **first-class**, and (b) provide a **graduation path** so proven
experiments flow *up* into the shared spec ([[0041-self-evolving-versioned-spec]]) or become
modules ([[0036-every-subsystem-is-a-module]] / [[0024-pluggable-extension-modules]]).

**This closes the self-evolution loop.** `0041`/`0042` described one direction — spec →
campaigns (downward standardization via [[0042-async-fleet-migration]]). This is the **other
arm** — campaigns → spec (upward innovation). Together they *are* the evolution engine: the
fleet experiments, the best experiments are promoted to canon, canon propagates back out.

**It dissolves the uniform-spec vs. unique-campaign tension.** The spec is the **settled
floor** of proven patterns; campaigns explore *above* it; proven experiments graduate to the
floor; the rest stay as **campaign-local exceptions** ([[0026-exceptions-are-features]]).
Divergence is the **R&D surface, not drift** — provided the graduation mechanism and the
floor/exception distinction ([[0042]]) exist to tell innovation from staleness.

**Where it comes from.** User instinct. Already real: aegis = a campaign that grew an engine;
the Gleaners campaign hand-prototyped the whole sample-book feature ([[sample-book]],
[[0007-harvest-vs-workshop]] — "harvest from play," now applied to *architecture*, not just
content).

**Why it matters for next-gen.** It answers `0041`'s open question *"what evolves the spec?"* —
**proven campaign experiments do.** And it reframes per-campaign divergence from the
[[0034-outgrown-scaffold]] *problem* into an *asset*, on the condition that graduation exists.

**Open threads.** What's the **graduation mechanism**? (Note the recursion: this project's own
**[[appraisal-protocol]]** / verdict gate — interview-first, then adopt/adapt/reject — is
exactly a graduation mechanism, applied to mined patterns; it could apply to campaign features
too.) How to tell a worth-graduating experiment from a one-off (cf. [[0007-harvest-vs-workshop]]
findability, [[0031-beware-transient-constraint-architecture]] durable-vs-transient)? Does
promotion mean *becomes spec default* (`0041`), *becomes a module* (`0036`), or *becomes an
optional extension* (`0024`)? Who curates — human, or agent-proposed behind
[[0028-checkpointed-human-gates]]?
