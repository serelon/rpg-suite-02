---
tags:
  - kind/principle
  - source/conversation
  - theme/architecture
  - theme/single-source-of-truth
  - maturity/speculative
  - verdict/unevaluated
created: 2026-06-06
---

# Knowledge entries vs tool data — the KB's first type cut

**What it is.** The user's intended route through the ~50-type zoo of
[[0083-data-type-census]] (2026-06-06): "capture *all* the patterns and exceptions, and
standardize them, and try to find a **unified structure** for them to squeeze into." And
the first, foundational cut in that structure:

- **Knowledge entries** — stories, memories, "and similar… both are really just a special
  variant of a standard knowledge entry, **just with flags to be treated a certain way**."
  One base shape; type-specific behavior comes from flags, not from separate schemas.
- **Tool data** — "unlike say a nameset, which is data to be used by a tool. **the tool
  output is the context snippet**." Tool data never enters context raw; it parametrizes a
  tool, and the *output* is what the GM/writer sees.

**Why it matters for next-gen.** This collapses the type explosion:
- Memories, stories, texture-bank entries ([[0055-register-anchor-banks]]), transcripts
  ([[0062-conversation-transcripts-as-gm-context]]), lore snippets — one **knowledge-entry
  base type** with treatment flags (tells the consumers: verbatim-preserve, POV-scoped,
  injection-eligible, zoom tier…). The flags are [[0058-flag-lifecycle-set-at-build-select-at-prep]]'s
  load-tags given a real home, and the entry shape can carry provenance
  ([[0076-self-canonizing-hallucinations]]) uniformly.
- Namesets, pools, oracle tables, calendars — **tool-data types**, owned by their modules
  ([[0036-every-subsystem-a-module]]); the KB stores them but consumers never inject them
  directly. (Cleanly explains why namesets are simultaneously the most complex *and* most
  mature format ([[0084-rpg-tools-data-layer]]) — tool data can afford complexity because
  no context-window reader ever pays for it.)
- The standardization path is the same as 0080's harvest: **capture all patterns and
  exceptions first** (census done), *then* squeeze — exceptions as input, not noise
  ([[0026-exceptions-are-features]]).

**Open threads.** Where do hybrid types fall — characters are knowledge entries (read into
context) but also tool-targets (characters.py filters/loads them)? Is "treated a certain
way" a closed flag vocabulary or extensible per module? Do entity pages (characters,
locations, factions) form a third kind — *registry entries* — or are they knowledge
entries with identity flags? Rosters dissolve into folders+tags+index-pages (user) — are
index-pages generated (custodian output) or authored?

**Verdict.** _(unevaluated.)_
