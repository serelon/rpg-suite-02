---
tags:
  - kind/idea
  - source/new
  - source/sillytavern
  - theme/context-architecture
  - theme/docs-as-code
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-03
---

# Docs-as-code: compile context per beat, like a build target

**What it is.** Structured source — frontmatter carrying `scene-type`, `register`, `tags`,
`load conditions` — gives *declarative, auditable* handles, so context can be **compiled
per-beat like a build target**, rather than fuzzy vector retrieval over an unstructured pile.
The Sample Book ([[0006-sample-book-grid]]) is this idea applied to *registers*; the same
substrate serves *facts*, *state*, everything. Runtime is **hybrid**: a deterministic
skeleton assembled from frontmatter rules + agentic top-up where the model pulls extra on
demand — fusing positional/declarative control with the agentic paradigm.

**Where it comes from.** [[sample-book]] §4.

**Why it matters for next-gen.** This is a candidate **architecture spine**: "prompt build
system" as the core abstraction. It's the principled alternative to `E:\rpg`'s vector-RAG
pile, and it explains why this very repo is structured as tagged Markdown — the vault *is*
docs-as-code. Strongly reinforces [[0004-frontend-agnostic-core]]: a compiled context bundle
is frontend-portable.

**Open threads.** Deterministic-vs-agentic boundary — where's the seam? How do "load
conditions" get evaluated (a real expression language, or tags + simple rules)? Compare to
`solorpg`'s template-driven bundler (already a primitive context compiler). Relation to
hybrid retrieval (declarative handles *and* semantic search) rather than either/or.
