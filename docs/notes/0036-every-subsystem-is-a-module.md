---
tags:
  - kind/idea
  - source/new
  - theme/architecture
  - theme/extensions
  - theme/knowledge-layer
  - theme/single-source-of-truth
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-03
---

# Every subsystem is a self-owning module — single source of truth, consumers refer back

**What it is.** The user's proposed cure for the scaffold problem
([[0034-outgrown-scaffold]]), stated as a design direction: **every subsystem is managed as a
self-contained module that owns everything about itself.** Take memories: the module owns the
maintained tool, its **own desktop-skill packaging**, a bound **create-memory skill that is
versioned with the memory-system and updated when it updates**, its design-docs, and its
guide/schema/extraction-philosophy — **all in one place.** The rules:

- **One authority per subsystem.** No copied notes, no duplicate guides living elsewhere.
- **Consumers refer back, never embed.** If *any* other process uses memories in any way, it
  **points to the memory module** — it does not copy the guide or hardcode the schema.
- **No diverging files or exceptions outside the module.** Customization happens *through* the
  module, not by forking its knowledge into a workflow.
- **Versioning binds the parts.** The skill/guide/tool of a module move together, so a
  consumer always gets a coherent, current version.

**Where it comes from.** User design direction, triggered directly by the confirmed
memory-guide divergence (see [[0034-outgrown-scaffold]]): "I'm pretty sure the guide was
copied somewhere, and I've since worked on and tuned the memory module… the prompts in the two
files differ." (Verified: they diverged into *incompatible schemas*.)

**Why it matters for next-gen.** This is the **structural answer** the scaffold problem was
asking for — it replaces hand-wired paths + copied guides + inline exceptions with
*module-owned authority + reference-back*. It **generalizes [[0024-pluggable-extension-modules]]**:
not only can a big optional rules-engine plug in as a module — *every* subsystem (memories,
names, characters, locations, oracle, mechanics…) **is** a module, and a big engine is just a
large one. It operationalizes [[0018-layered-skill-architecture]], gives
[[0033-workflow-defers-to-canonical-guides]] a real binding mechanism (defer *to the module*,
not to a path), and the "refer back, never copy" rule is the **anti-drift** invariant that
[[0034-outgrown-scaffold]] proved we need. Each module packaging its own desktop skill also
serves [[0004-frontend-agnostic-core]]. Likely the **third north-star**, with 0004 and 0024.

**Open threads.** What *is* a module's contract (what it exposes; how a consumer "refers
back" — import, registry-resolve, link)? How does the versioned binding actually work
(skill pinned to module version)? How do per-campaign exceptions ([[0026-exceptions-are-features]])
live *inside/through* modules rather than forking them — campaigns *extend*, don't *override*?
Does the legitimate split (schema vs extraction-philosophy) just mean *two docs inside the one
memory module*, not two repos? Migration: how to detangle the current copies. Strong
`kind/decision` candidate — possibly the spine.
