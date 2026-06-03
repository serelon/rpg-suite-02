---
tags:
  - kind/idea
  - source/new
  - theme/architecture
  - theme/self-evolution
  - theme/single-source-of-truth
  - maturity/seed
  - verdict/adopt
created: 2026-06-03
---

# Self-evolving by design, governed by a single versioned spec ("the current meta")

**What it is.** A load-bearing requirement (user): the whole system must be designed to
**self-evolve** — its conventions and "meta" (the current best way to shape a campaign, a
module, a workflow) improve over time as a *first-class capability*, not via periodic manual
rewrites. The non-negotiable enabler: a **single, versioned, canonical spec** — *"this is the
current meta, refactor to this"* — replacing today's reality where the best way is **tacit and
scattered across exemplar campaigns**.

**The diagnosis (grounding).** "Every single campaign in the repo follows different
conventions, and there's not a single uniform template that says 'this is the current meta.'
There's a lot of 'go look at campaign A for a good example of how they did <small thing>'
happening." So best practice lives as **folklore in exemplars**, not as an authority. This is
[[0034-outgrown-scaffold]] and the memory-guide drift, but at the **campaign-convention**
level — knowledge in scattered copies, no source of truth. (Possible existing seed:
`rpg-tools/references/campaign-zero-guide.md` may be an early attempt at "the canonical
starting spec.")

**Where it comes from.** User, flagged as load-bearing and new to the vault.

**Why it matters for next-gen.** A top-level constraint — the **fourth north-star** (with
[[0004-frontend-agnostic-core]], [[0024-pluggable-extension-modules]],
[[0036-every-subsystem-is-a-module]]). It's `0036` applied to *conventions themselves*: the
spec is a canonical, versioned thing everyone refers back to — not exemplar folklore. It lets
the system **get better without forking**, and it's what the async migration mechanism
([[0042-async-fleet-migration]]) upgrades toward. Self-evolution needs the anti-regression
discipline of [[0019-companion-rationale-as-anti-regression]] and review gates
([[0028-checkpointed-human-gates]]) so "evolution" doesn't become drift. (Meta: this project's
own note→theme→roadmap vault, with its verdict gate, is itself a self-evolving knowledge
system — a small proof of the shape.)

**Open threads.** What *evolves* the spec — human curation, or agent-proposed improvements
behind review gates? How is the spec expressed — a template, a schema, a "campaign-zero"
reference, a module? How is it versioned, and how does a self-evolving spec avoid regression
([[0031-beware-transient-constraint-architecture]] is one guardrail: distinguish durable from
transient before enshrining it)? Strong `kind/decision` candidate.

**Verdict.** `adopt` — with the drift-risk caveat: self-evolution leans on review gates (0028) and anti-regression rationale docs (0019). *(appraised 2026-06-03)*
