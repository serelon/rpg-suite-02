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

**Hybrid question resolved (user, same day): characters are knowledge entries — and the
oldest living example of [[0068-multi-lens-data]]'s zoom pattern.** The current character
format (and the legacy .md one before it): "there's a short profile, to be loaded in bulk
for many characters. there's the long profile to be loaded for the most important
spotlight characters. and there's room for extra sections to be loaded on demand. also
some metadata." So: minimal = bulk zoom, full = spotlight zoom, sections = on-demand
hops, metadata = selection layer. characters.py is not a tool consuming tool-data — it's
a *presentation consumer* ([[0069-one-knowledge-base-many-presentation-layers]]) pulling
zoom tiers. The two-kind cut survives clean: knowledge entries zoom; tool data computes.

**Zoom tiers settled (user, same day): per-type, with standard ones + extensibility.**
And a new *smallest* standard tier: the **index-line** — e.g.
`[Marcus Chen] - Captain of [Generic Ship]` — one line, identity + hook, **with links
embedded** (the brackets are wikilinks: the index-line carries graph edges). The tier
ladder so far: **index-line → bulk/minimal → spotlight/full → on-demand sections**.
Index-lines are also the obvious building block for the index-pages that replace rosters —
an index-page is just a curated/generated list of index-lines, which means the
roster-replacement may be a *render* (custodian/build output), not an authored doc.

**Sharpened (user, pillar-1 review 2026-06-06): the cut is by *substrate*, not shape.**
"tool data is raw json data, doesnt become an md in the obsidian tree. knowledge entries
do, they're fully standardized with obsidian as the base template, *regardless* of how
complex they become. memories, characters, savefiles, maybe even spreadsheets, all go in
there. **it's about the base template, not the end shape.**" So: knowledge entry = vault
page on ONE base template ([[0090-cherrypick-contract-three-layers]]'s three layers);
tool data = raw JSON outside the tree; **images/raw assets are a third substrate**.
Complexity lives *inside* the template, never as a schema fork. **Multi-template pages
kept open** as a possibility (one page validly carrying two subtemplates) — no design,
just not foreclosed. Savefiles land here too — see [[0061-continuity-artifacts-under-suspicion]]'s
amendment (savefile-as-page is a growth play).

**Flag vocabulary settled (user, same review): extensible per module, but *always*
documented.** "we want the repo to be self-evolving, but we also want to avoid the trap
of undocumented innovations." Module owns its flags' docs ([[0036-every-subsystem-is-a-module]]),
spec owns the core set ([[0041-self-evolving-versioned-spec]]), undocumented-flag-hunting
is a custodian audit job ([[0075-postprocessing-as-vault-librarian]]).

**Open threads.** Index-pages: generated (custodian output) or authored — or authored-order over
generated-content? Is the index-line *derived* from page frontmatter (name + role + key
links) or hand-written — and if hand-written, it's the one tier where
[[0079-relational-anchoring-antipattern]] is *allowed* (relational hooks are the point of
an index-line).

**Verdict.** _(unevaluated.)_
