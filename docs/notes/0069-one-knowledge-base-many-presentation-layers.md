---
tags:
  - kind/idea
  - source/conversation
  - theme/architecture
  - theme/context-economy
  - theme/composition
  - maturity/speculative
  - verdict/unevaluated
created: 2026-06-05
---

# One knowledge base, many presentation layers

**What it is.** The architecture that ties the vault thread together (user, 2026-06-05):
the **context-presentation layer gets modular** — one knowledge base (the canonical linked
vault of [[0067-campaign-data-as-linked-vault]], two-trunk shape per [[0068-multi-lens-data]]),
consumed by interchangeable presentation strategies:

1. **Bundle compiler** (today's pattern, kept): assembles a primer from KB context —
   "one monolith, portable, contains everything" — and also **bundles the db itself for
   exploration-reading**. The [[0044-scenario-compiler]] / [[0063-portable-bundles-constraint]]
   fat-bundle path.
2. **Agentic flow**: the GM explores the KB live, following links as needed — the
   [[0060-jit-loading-retry]] path. Known hard part: "needs us to figure out the prompting
   for taking enough initiative" (0060's three judgment failure modes are exactly this).
3. **Keyword-injection / RAG**: SillyTavern-style — keywords in play trigger a search of
   the KB and inject matching context on demand; the KB "serves as a rag backend."

**The invariant:** "the knowledge base will be setup to handle all this without changing
its shape, it's just one layer in a workflow." Consumers vary by platform and era; the KB
doesn't.

**Why it matters for next-gen.** This is [[0024-pluggable-extension-modules]] /
[[0036-every-subsystem-a-module]] applied to context delivery: presentation strategies are
modules over a stable data contract. It also future-proofs against
[[0031-beware-transient-constraint-architecture]] — agentic initiative and RAG quality are
*model-era variables*, so they belong in swappable consumers, never baked into the data.
And it resolves where E:\rpg went wrong: it welded the data to one heavyweight delivery
mechanism (Qdrant+wiki+MCP); here delivery is deliberately disposable.

**Open threads.** What exactly is the KB's contract surface — files+links only, or also a
query/index layer the consumers share (the RAG path needs *some* search primitive; does the
compiler reuse it)? Does keyword-injection need authored trigger-keywords on entity pages
(another set-at-build flag, [[0058-flag-lifecycle-set-at-build-select-at-prep]])? Which
consumer fits which platform — Desktop/web/mobile likely get bundles or RAG, Claude Code
gets agentic? And the initiative-prompting problem (0060) is now a named blocker for
consumer #2.

**Verdict.** _(unevaluated.)_
