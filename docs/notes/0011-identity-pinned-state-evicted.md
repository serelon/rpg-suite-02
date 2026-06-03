---
tags:
  - kind/pattern
  - source/new
  - source/sillytavern
  - theme/context-architecture
  - theme/memory-architecture
  - maturity/growing
  - verdict/unevaluated
created: 2026-06-03
---

# Identity pinned, state evicted

**What it is.** Split what rides in context by *volatility*. Anything present **every turn**
must hold only **always-true identity** — the smallest set of fixed facts. **Time-bound
state** belongs somewhere updatable/clearable (e.g. an author's-note layer), or it quietly
fights the live game as it goes stale. Evergreen pinned; evictable elsewhere.

**Where it comes from.** [[sample-book]] §4 ("Evergreen vs. evictable").

**Why it matters for next-gen.** A clean, reusable rule for *what is allowed to be
persistent*. It's the structural counterpart to [[0009-jit-context-and-eviction]] (this says
what's *exempt* from eviction) and connects to the savefile-vs-profile split already lived in
`solorpg` (static character profiles vs. dynamic savefiles). The failure mode it prevents —
stale state masquerading as truth — is the same class as
[[0003-scope-memories-to-context]]'s "soup."

**Open threads.** Where exactly is the line between identity and state for a *character who
changes*? (A protagonist's growth is the whole point — so "always-true identity" must be the
*invariant core*, not the current self.) Needs a concrete layering model.
