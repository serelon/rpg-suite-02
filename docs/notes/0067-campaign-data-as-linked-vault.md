---
tags:
  - kind/idea
  - source/e-rpg
  - theme/architecture
  - theme/context-economy
  - maturity/speculative
  - verdict/unevaluated
created: 2026-06-05
---

# Campaign data as a linked vault — relations instead of flat files

**What it is.** Resurrection (modified) of E:\rpg's wiki pipeline idea — which **never ran**;
the repo never got that far, so this is *designed-never-built* (a rung below
[[0050-built-never-used-inventory]]'s built-never-used). What survives the dead infra is the
structural insight:

> right now we have alot of flat data, flat files, flat everything. you either read
> everything or nothing. no way to see relations between data. a wiki structure is all
> about relations.

**The modification:** not a served wiki (Wiki.js + Qdrant + Docker — none of that comes
back), but an **Obsidian-style vault** — campaign data as linked markdown, relations as
plain `[[wikilinks]]`. Exactly the pattern this research repo itself uses.

**Why it matters for next-gen.** Two distinct payoffs:
1. **Navigation/curation (human reader):** see the relations — character → faction →
   location → session — instead of opening flat JSONs one by one.
2. **Context economy (model reader):** flat files force all-or-nothing loads; a linked
   structure lets a GM (or compiler) *walk* from a scene's entities outward, loading only
   the hops needed. Natural substrate for JIT loading ([[0060-jit-loading-retry]]) and a
   compile *source* for the scenario compiler ([[0044-scenario-compiler]]) — relations
   could even drive what a fat bundle includes ([[0063-portable-bundles-constraint]]).

**Where it comes from.** `E:\rpg`'s 5-agent pipeline design (parser → entities → timeline →
wiki → briefing) — the wiki stage's *intent*, not its implementation. The entity-registry
idea ([[0040-entity-registry]]) is the natural link-target layer: entities are the nodes,
this note is about the edges.

**Direction settled (user, 2026-06-05): canonical — and the build arrow inverts.** The
vault IS the data; "the jsons (or whatever next-gen thing we do) *builds* from the vault."
Full inversion of E:\rpg (which compiled wiki *from* data). This makes the vault the source
layer for [[0056-files-as-build-products]] and the scenario compiler's input. Constraint:
vault files "prolly cant be basic .md, we'll need formatting so that alot of tools can
cherrypick data from them" — i.e. **structured markdown**: machine-readable fields
(frontmatter-style) + conventional sections, parseable without losing Obsidian-native
linking. (This research repo's own note format is a working prototype of exactly that.)

**Open threads.** What's the cherrypick contract — frontmatter-only for tools, or do tools
also parse conventional sections (and who enforces the section schema)? Where do links come
from — authored during workshops, extracted at post-processing, or both (same set-at-build
question as [[0058-flag-lifecycle-set-at-build-select-at-prep]])? Per-campaign vaults, given
campaign isolation is a core principle? And migration: today's canonical JSONs (characters,
savefiles, memories) would become *build products* — what's the path from here to there?

**Verdict.** _(unevaluated.)_
