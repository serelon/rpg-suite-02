---
tags:
  - kind/idea
  - source/conversation
  - theme/architecture
  - theme/context-economy
  - theme/composition
  - maturity/speculative
  - verdict/adopt
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

**Retrieval layering (settled direction, 2026-06-05).** Vector search is the *fallback*,
not the front door:
1. **Exact match** — entity names, aliases, page titles: already in the KB for free, never
   send these through embeddings (vectors smear precision into vibes; grep wins on names).
2. **Link-graph walking** — "related things" via the edges the vault already has;
   capitalize on the graph before reaching for similarity.
3. **Vector search** — fuzzy/thematic recall only ("a scene like this happened before").
   Known costs to respect: similar ≠ relevant (no built-in "nothing is near enough");
   chunking granularity is the real design problem (E:\rpg's multi-granularity chunking was
   about exactly this); the index is a derived artifact that lies when stale — another
   build product for [[0057-compiled-context-needs-audit-tooling]] manifests.

**Trigger-keyword criterion (defuses [[0058-flag-lifecycle-set-at-build-select-at-prep]]'s
hallucinated-tag problem for this case).** Keywords are written by the agent writing the
entry, but with a *testable* validity rule: a trigger is only valid if it's **a string
likely to literally appear in play prose** — surface words ("walker collar", "the Drift"),
never concepts ("redemption-arc"). And it's empirically checkable: run candidate keywords
against the session-transcript archive ([[0064-unharvested-archive]]) — a trigger that
never fires in the historical corpus is noise; delete it. **The archive becomes a
validation set.**

**Open threads.** What exactly is the KB's contract surface — files+links only, or also a
query/index layer the consumers share (does the compiler reuse the RAG search primitive)?
Which consumer fits which platform — Desktop/web/mobile likely get bundles or RAG, Claude
Code gets agentic? The initiative-prompting problem (0060) is a named blocker for consumer
#2. And does corpus-validation of triggers generalize to *all* set-at-build tags (0058's
is-tags), or only to keyword-shaped ones?

**Verdict.** **Adopt** (appraised 2026-06-06). Shape-invariant KB, presentation as
swappable consumers, layered retrieval (exact → graph → vector), corpus-validated trigger
keywords. The initiative-prompting blocker (consumer #2) and the KB contract surface stay
open as design work.
