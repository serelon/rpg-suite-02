---
tags:
  - kind/pattern
  - source/solorpg
  - theme/context-economy
  - theme/workflow
  - theme/data-pipeline
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# Preprocessing — strip junk tokens before anything reads the export

**What it is.** Before a session export is used, run it through `preprocess_export.py`, which
**removes non-signal tokens** (tool calls, thinking blocks, system content) and splits the
result into chunks. Two distinct jobs, with two different fates:
- **Token hygiene** (the durable core) — cut everything that isn't the actual narrative, so
  whatever reads next sees signal, not cruft. The user: *"preprocessing is definitely always
  gonna be a good pattern to follow."*
- **Chunking for readability** (the transient shell) — split into ~20k pieces, originally to
  fit a **25k max file-read limit**. That limit may no longer exist; this half is a
  capability-workaround, not a principle.

**Where it comes from.** `solorpg` `tools/preprocess_export.py`, the standard first step of
postprocess. Built in the 165k era but **still in active use** — unlike the v2 team split it
predates.

**Why it matters for next-gen.** Token hygiene is pure **context economy** that *grows* more
valuable with bigger windows, not less: a 1M window full of tool-call noise is still mostly
noise. It passes [[0031-beware-transient-constraint-architecture]]'s verdict-test cleanly
(salience, not capacity) — and is that note's headline example of a **durable core wrapped in
a transient shell**: keep the stripping, be ready to drop the chunking. Feeds
[[0030-summary-as-compression]] (clean input → better summaries) and the broader
[[0009-jit-context-and-eviction]] thread (curate what's present).

**Open threads.** Is the 25k read-limit still real? If not, drop chunking, keep stripping.
What else is "junk" beyond tool/thinking blocks — and is some of it actually signal for
*some* downstream task (e.g. dice rolls for a mechanics-aware capture)? Generalizes: every
ingestion point probably wants a hygiene pass tuned to *what reads it next*.