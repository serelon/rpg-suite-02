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

**Seed-failure taxonomy (user, same day):**
1. **Overengineering — the easy one, instant failure.** "giving too much info, too many
   plothooks, laying out railroads." The gardener has nothing to grow; the seed is already
   a (dead) tree. *Refined (2026-06-06):* the precise nono is **unprompted
   session-planning — a detailed beat-by-beat plan**. Some railroading is acceptable when
   it's really **goalposting**: minimal mandatory waypoints, open-ended in between (e.g.
   origin-story beats, or sealed bounded segments per [[0089-sealed-secrets-files]]).
   Rails minimal, goalposts open — the beat-by-beat script is what kills the garden.
   The test isn't the structure itself, it's the effect: **the failure state is where
   goals/railroads stifle the GM's imagination** — "we want it to be creative, not follow
   a script." A script turns the gardener into an executor; the seed-quality bar and the
   goalpost bar are the same bar: does it leave the GM something to *invent*?
2. **Too-small — the insidious one.** The seed "doesnt have enough interesting traits to
   extrapolate." It doesn't fail loudly; it just grows boring.
3. **Signal drowned — the worst.** The seed *has* an interesting trait, "and thats
   overshadowed by the eh traits." The gardener (an LLM, pattern-matching across the whole
   seed — [[0079-relational-anchoring-antipattern]]'s mechanism again) waters everything
   equally, and filler traits steal growth from the live one. Implication: a seed's
   quality isn't its size but its **signal density — every trait present should deserve
   extrapolation**, because everything present *will* get extrapolated.

**Open threads.** Do gardener-grown elements need an engineering pass before becoming
canon (harvest-review = the postprocessing PRs)? Is the [[0044-scenario-compiler]] an
engineer tool, a gardener tool, or the bridge? Could seed review be a workshop step —
the engineer pruning "eh traits" before play, the way 0066 prunes thinking blocks to
"short, fixed, genuine"?

**Verdict.** _(unevaluated.)_
