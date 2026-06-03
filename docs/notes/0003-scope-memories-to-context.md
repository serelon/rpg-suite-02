---
tags:
  - kind/pattern
  - source/solorpg
  - theme/memory-architecture
  - theme/context-economy
  - maturity/growing
  - verdict/unevaluated
created: 2026-06-03
---

# Scope every memory to its campaign / branch / character — or it becomes soup

**What it is.** Auto-saved memories must carry explicit scope (campaign, subsetting, branch,
character) in both filename and content. Generic, unscoped memories degrade into an
"undifferentiated mess" once many campaigns share themes and character archetypes.

**Where it comes from.** `solorpg/.claude/projects/.../memory/feedback_memory_campaign_scoping.md`
— a feedback memory the user wrote after running 12+ active campaigns with overlapping
themes. Filed as `type: feedback` in that repo's Claude-memory store.

**Why it matters for next-gen.** This is a hard-won failure mode, not a hypothetical: a flat
memory pool collides with itself at scale. Any next-gen memory/knowledge layer needs scope
as a *first-class key*, not an afterthought — which rhymes with the campaign-isolation
principle seen across the source repos. It's the memory-layer face of the same concern as
[[0001-tiered-progressive-loading]] (don't let irrelevant context bleed in).

**Open threads.** Scoping by hand (filename convention) is the cheap version; an
entity-ID / registry approach (see `old-erpg`'s entity registry) is the heavyweight version.
Where's the right point on that line? Relates to [[0002-read-anywhere-write-canonical]]'s
single-source-of-truth tension. Note: this came from solorpg's **`.claude/` directory**,
which also holds skills, agents, and plans — a rich, under-mined vein (see [[relevant-paths]]).
