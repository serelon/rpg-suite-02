---
tags:
  - kind/idea
  - source/solorpg
  - theme/architecture
  - theme/knowledge-layer
  - theme/scaffold
  - theme/workflow
  - maturity/growing
  - verdict/unevaluated
created: 2026-06-03
---

# The system has outgrown the scaffold — knowledge composition is the bottleneck

**What it is.** The user's flagged lesson ("fixate on this"), about the most important
workflow in the whole system. session-postprocess is a *semi-living document* meant to pull
in data/knowledge from guides in `rpg-tools` and elsewhere — and it does so **only so-so,
because the system has outgrown the scaffold.** The deferral pattern
([[0033-workflow-defers-to-canonical-guides]]) is right; its *mechanism* is what's strained:

- **Scattered sources, no registry — with confirmed drift.** Guides live across ≥3 homes
  (`rpg-tools/guides/`, `solorpg/prompts/`, `solorpg/templates/`) with inconsistent
  conventions. **Smoking gun:** memory guidance exists as `rpg-tools/references/memories-guide.md`
  (263 lines, the *portable canonical* one) **and** as solorpg-local
  `prompts/memory-extraction-guide.md` (201) + `templates/memory-template.md` (206) — and the
  flagship workflow points at the **local copies, ignoring the rpg-tools one**. Yet for
  *characters and locations* the same workflow sources correctly from `rpg-tools/guides/`. So
  the same class of knowledge has two homes and the "canonical" source is ambiguous and almost
  certainly diverged. This asymmetry *is* the scaffold problem in miniature.
- **Hand-wired paths.** Every "read this guide" is a literal path baked into the prose. The
  workflow must *know about* each guide; adding/moving one means editing the skill. A
  manually-maintained "Existing Guides" table is the only index, and it drifts.
- **Inline exception accretion.** Per-campaign behavior (Eternal Witness stories, AEGIS data
  restoration, non-linear timelines) is **hardcoded as prose branches** inside the skill —
  the same smell as [[0026-exceptions-are-features]].
- **Monolith bloat.** ~1087 lines doing six jobs (git, setup, discovery, validation, capture,
  bundling). The orchestration and the knowledge and the exceptions are tangled in one file.

The diagnosis: the knowledge base and campaign variety have grown faster than a
hardcoded-reference scaffold can compose. The workflow is straining to be a *composition
engine* using only string literals and a hand-kept table.

**Where it comes from.** User framing + [[session-postprocess]] read.

**Why it matters for next-gen.** This argues for a **first-class knowledge/composition
layer**: a registry/resolver where a workflow **declares a need** ("memory schema", "location
craft", "this campaign's custom outputs") and the system **binds** it — instead of literal
paths and inline branches. It's the connective tissue between [[0010-docs-as-code-context-compiler]]
(structured, resolvable handles), [[0018-layered-skill-architecture]] (separate the layers),
[[0024-pluggable-extension-modules]] (modules register their guides/outputs), and
[[0026-exceptions-are-features]] (declared, not hardcoded). Possibly *the* core problem the
next-gen system exists to solve.

**Open threads.** What's the resolver keyed on — capability tags? content-type? A manifest per
guide/module? How does a campaign or module *contribute* knowledge to the registry rather than
the workflow reaching out for it (inversion of control)? Where's the line between a thin
declarative spine and losing the legibility of "just read this file"? Strong
`kind/decision` candidate. Also: re-test against [[0031-beware-transient-constraint-architecture]]
— is any of the bloat actually a context-era workaround, or is it genuine composition debt?
(Mostly the latter.)
