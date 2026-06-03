---
tags:
  - kind/idea
  - source/new
  - source/sillytavern
  - theme/context-architecture
  - theme/context-economy
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-03
---

# JIT context + eviction — and beats are the eviction boundary

**What it is.** Crispness is a **salience problem, not a capacity one**: dumping everything
into a large context flattens emphasis — the model can't tell load-bearing from ambient.
*Absence is load-bearing.* So context wants a **lifecycle, not a growing transcript**:
- **Retrieval** (what to load) is the easy, well-trodden half.
- **Eviction** (what to drop, and when) is the **underbuilt** half — the real work.
- Narrative **beats are natural eviction boundaries**. Corollary: the **pacing model and the
  context model want to be the same model.**

**Where it comes from.** [[sample-book]] §4.

**Why it matters for next-gen.** This sharpens the project's recurring `theme/context-economy`
thread. Tiered loading ([[0001-tiered-progressive-loading]]) is the *retrieval* half done
well; this names the missing *eviction* half and ties it to pacing — a genuinely novel design
hook. "Beats = eviction boundaries" is the kind of claim that could shape the whole runtime.

**Open threads.** What detects a beat boundary? Is eviction lossy (summarize-then-drop) or
addressable (move to cold store, recall on cue)? Tension with `E:\rpg`'s
keep-everything-in-a-vector-store instinct. Pairs with
[[0011-identity-pinned-state-evicted]] (what's *exempt* from eviction).
