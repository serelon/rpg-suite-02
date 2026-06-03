---
tags:
  - kind/pattern
  - source/solorpg
  - theme/context-economy
  - theme/workflow
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# Summary as compression — "will this matter in 10 sessions?"

**What it is.** The session-summary spec is ruthless about *salience*, not completeness:
**one page max (~3KB)**, every sentence load-bearing. **Include** state changes, decisions
that open/close future paths, relationship shifts, threads advanced. **Exclude** flavor,
atmosphere, scenic description (those go to *memories*), comedic asides, blow-by-blow
(summarize outcomes, not processes). The governing test: **"Will this matter in 10 sessions?
If not, it doesn't belong."** Note the deliberate division of labor — the summary carries
*continuation-relevant state*; evocative texture is routed to the memory corpus instead.

**Where it comes from.** `solorpg` `session-postprocess-v2` §4.1 (summary drafting spec).

**Why it matters for next-gen.** A concrete, reusable **compression heuristic** for the
context-economy thread: summaries are forward-looking state, sized by future-relevance, with
texture evicted to a separate retrievable store. This is [[0009-jit-context-and-eviction]] at
the artifact level (what to keep present vs. evict to cold storage), the writing-side mate of
[[0001-tiered-progressive-loading]], and what [[0017-recap-as-verification]] later checks
against. The summary/memory split is itself an instance of identity-vs-state and salience-curation
([[0011-identity-pinned-state-evicted]]).

**Open threads.** "Matters in 10 sessions" is a human judgment — can it be assisted? Tension
with non-linear campaigns (what's "10 sessions later" when chronology is scrambled?). The
summary↔memory routing rule is a clean idea worth generalizing: *every captured thing has a
right-sized home*.
