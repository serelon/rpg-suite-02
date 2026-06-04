---
tags:
  - kind/idea
  - source/solorpg
  - theme/context-economy
  - maturity/speculative
  - verdict/unevaluated
created: 2026-06-04
---

# Retry JIT loading — the pre-session infodump is a transient-constraint artifact

**What it is.** The current default — a **pre-session infodump** (load everything that
might matter up front) — exists because **JIT-loading struggled in practice** with earlier
models' agentic ability, not because infodump is the right design. (User:) newer models
(4.7/4.8-era) "are supposed to be much better at agentic stuff, so I'm wondering if it's
time to try JIT-loading again."

The location ideal-case that prompted it: a location must fire **before** writing it or
going there — the guide/schema loads pre-authoring, then **smart-load whatever else the
scene needs** as play arrives. Two-phase: know-how first, scene payload JIT.

**Where it comes from.** Light workshop bounce (2026-06-04), on what finished location
wiring would look like ([[0059-datastruct-census-underused-and-superseded]]).

**Why it matters for next-gen.** This is [[0031-beware-transient-constraint-architecture]]
caught *live*: infodump-by-default is the v2-team-split of context loading — built around a
model limit that may have expired. If JIT works now, it changes the compiler's delivery
shape: less precompiled bundle, more runtime resolution
([[0045-runtime-composition-briefing-py]], [[0009-jit-context-and-eviction]]), and
half-wired datastructs like locations get their "pulls" as JIT hooks rather than bundle
inclusions. Worth an explicit *experiment* rather than a belief — a campaign testbed
([[0043-campaigns-as-testbeds]]) comparing infodump vs JIT on the same scenario.

**Open threads.** What broke historically — models not reaching for tools mid-scene, or
reaching wrong? (Determines whether better agency actually fixes it.) Failure mode if JIT
misses mid-scene: fiction stalls or model fabricates ([[0021-data-required-as-prompt]]'s
halt-don't-fabricate applies). Hybrid floor: identity pinned, texture JIT
([[0011-identity-pinned-state-evicted]]).

**Verdict.** _(unevaluated.)_
