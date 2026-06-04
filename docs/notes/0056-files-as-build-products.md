---
tags:
  - kind/idea
  - source/new
  - theme/composition
  - theme/context-economy
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-04
---

# Files as build products — compilation drops below the bundle to the individual file

**What it is.** (User:) "I'm drifting towards dynamically built *files* rather than just
dynamically built *bundles*." Concrete example: a texture bank
([[0055-register-anchor-banks]]) compiled from **both a campaign source and a character
source, following tags and flags** — e.g. world-texture entries merged with the active POV's
register entries, filtered for the scene at hand. The artifact a session reads is no longer
an authored file that bundling *selects*; it's a **build product** the compiler *assembles*.

**Where it comes from.** User, morning workshop bounce (2026-06-04), answering whether
per-POV registers (texture bank's "Solace's register" section) are a third anchor kind —
the answer dissolves the question: with compiled files, campaign-voice and character-lens
entries are just differently-tagged *sources* composed per build.

**Why it matters for next-gen.** Extends [[0044-scenario-compiler]] one level down: the
compilation unit isn't only the bundle/briefing — individual artifacts are themselves
compile targets. This is [[0010-docs-as-code-context-compiler]] realized at file granularity
(tagged frontmatter as the selector), and it gives [[0006-sample-book-grid]] its JIT
delivery mechanism. It also recasts [[0047-multi-axis-data-management]]: the axes
(campaign/branch/subsetting/character/era) are the *source dimensions* a file-build can
draw from.

**Open threads.** Tag/flag schema — who defines the vocabulary, and is it per-campaign or
spec-level? Are built files cached artifacts (diffable, [[0051-live-context-delta]]) or
ephemeral? Does *every* artifact type become compilable (savefiles? primers?) or only
anchor/reference types? Where does authored content end and assembly begin — provenance
must survive the build ([[0052-evolution-vs-drift]]: a built file must show which gated
sources it came from).

**Verdict.** _(unevaluated.)_
