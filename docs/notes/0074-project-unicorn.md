---
tags:
  - kind/idea
  - source/conversation
  - theme/architecture
  - maturity/speculative
  - verdict/unevaluated
created: 2026-06-05
---

# Project Unicorn — the ultimate RP client, the final frontend

**What it is.** The user's declared endgame for all of this (2026-06-05):

> it'll be my attempt at building the ultimate rp client, the final frontend to all this.
> my most ambitious project thus far. aka, a unicorn.
> it'll probably fail, because we'll run out of steam/tokens before the finish line.
> but still :)

A dedicated RP client sitting on top of the next-gen stack — named with full awareness of
its odds.

**Why it matters for next-gen.** Even as a probably-unreachable star, it disciplines the
architecture *now*:
- It's the reason [[0004-frontend-agnostic-core]] is a north-star: the core must not care
  whether the consumer is Claude Code, Claude Desktop, or Unicorn.
- It slots into [[0069-one-knowledge-base-many-presentation-layers]] as a future *fourth
  consumer* — likely the one that would fuse all three strategies (compiled bundles +
  agentic exploration + keyword-RAG injection) behind one UI.
- The failure mode is named up front ("run out of steam/tokens"), which argues for the
  stack being valuable *without* Unicorn ever shipping: every layer (KB, compiler,
  presentation modules) must stand alone. Unicorn is the capstone, never a dependency.

**Open threads.** What does "ultimate RP client" mean concretely — a chat UI with the KB
live behind it? Session management, portability ([[0063-portable-bundles-constraint]]),
the audit GUI ([[0057-compiled-context-needs-audit-tooling]]) folded in? Deliberately
unscoped for now — research phase; this note just gives the star a name so other notes
can point at it.

**Verdict.** _(unevaluated.)_
