---
tags:
  - kind/idea
  - source/new
  - theme/composition
  - theme/architecture
  - theme/context-economy
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-03
---

# Runtime composition — `briefing.py` instead of `briefing.md`

**What it is.** (User:) do the composition **at runtime**, not only at bundle time: the bundle
ships an *executable* briefing — `briefing.py` instead of `briefing.md`. **Same data,
programmatically delivered** instead of a static document plus lots of tool calls. The big
perk: **inline tool calls** — e.g. namegen *runs inline* during delivery, instead of the
briefing carrying an instruction telling the model to go run namegen. The artifact is a
program, not a document.

**Where it comes from.** User, during the first appraisal — refining the scenario compiler
([[0044-scenario-compiler]]) with a second delivery mode.

**Why it matters for next-gen.**
- It collapses the *instruct-then-hope* round trip: the model doesn't have to remember to run
  namegen (a known failure class — `gm-skill` prep explicitly pregenerates a name pool to
  avoid stalls); the briefing already ran it. Fewer tool calls, fewer dropped instructions.
- It gives the compiler **two build targets**: compile-time (static bundle) and runtime
  (program that yields context on demand). This is *exactly* the split [[sample-book]] §1
  called out — "precompiled OR on demand, the same split that runs through the whole
  architecture" — now at the briefing level. Also the executable face of
  [[0010-docs-as-code-context-compiler]]'s hybrid runtime (deterministic skeleton + agentic
  top-up) and a natural carrier for JIT/per-beat delivery ([[0009-jit-context-and-eviction]]).
- Pure-Python, stdlib-only ([[0002-read-anywhere-write-canonical]] lineage) keeps it portable.

**Open threads.** Where can it *run* — which frontends allow code execution
([[0004-frontend-agnostic-core]]: Desktop yes via skills; others vary)? Static `.md` likely
remains the fallback target for non-executing surfaces — compiler emits both? Inspectability:
a static briefing is reviewable before play; a program's output varies per run — how to audit
what was actually delivered? Security/simplicity trade. Does runtime composition subsume prep
steps generally (pregen pools, savefile reads), and how far does "inline" go before the
briefing becomes the GM?
