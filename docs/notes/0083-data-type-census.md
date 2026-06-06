---
tags:
  - kind/pattern
  - source/solorpg
  - theme/architecture
  - theme/single-source-of-truth
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-06
---

# Data-type census — ~50 types, and variance tracks tool-backing exactly

**What it is.** Full census of the solorpg vault (~25 campaigns; sweep 2026-06-06,
preserved in [[census-solorpg-data-types]]): roughly **50 distinct data types**, ~60% JSON
/ ~35% markdown / 3% JSONL. Three structural findings:

1. **Shape variance correlates with tool-backing, almost perfectly.** Low-variance types
   all have a tool or tight template behind them: character JSON (~95% consistent),
   namesets (~95%), savefiles (~90%, skill-templated), bundle manifests (100%, bundler-
   enforced). High-variance types are all freeform prose with no tool in the loop:
   primers, reference docs, session summaries, technical specs. **Where a tool exists,
   discipline is free; where none exists, every campaign reinvents.** Empirical
   confirmation of validate-at-write ([[0070-threads-tracker-design]],
   [[0072-schema-drift-tools-vs-hand-edited-json]]) at vault scale.
2. **Adoption gradient, now with hard counts** (confirms [[0059-datastruct-census-underused-and-superseded]]):
   universal — characters, savefiles, primers, CLAUDE.md (25/25), namesets (23/25);
   narrow — memories (7), stories (3, one systematic), locations (2). The narrow ones are
   the *most structured* types — structure alone didn't drive adoption; being wired into
   the play loop did.
3. **Skills are the de-facto schema authorities for prose types** — session-postprocess-v2
   defines what a summary/savefile/memory looks like; campaign-setup defines CLAUDE.md/
   primer/bundle-template. The format spec lives *inside workflow instructions*, not in a
   schema anyone can validate against. (The same disease as
   [[0046-campaign-lifecycle-geological-strata]] — authority embedded in workflows.)

**Why it matters for next-gen.** This is the input inventory for the KB-structure work
([[knowledge-base-canonical-vault]]'s headline item): every one of these ~50 types needs a
home decision — vault page type (with template), build product (compiled, e.g. bundles,
chunks), or retired. Finding 1 is the design argument: **giving prose types real templates
+ write-path tooling is where the variance reduction will come from.** Finding 3 says the
cherrypick/section schemas must move out of skill prose into the KB's own type definitions.

**Open threads.** The aegis data/ cluster (threads, strategic, equipment, vault,
blueprints…) is a whole genre — "campaign-mechanical state" — that the rpg-tools type
system doesn't cover at all; does next-gen absorb it as module-owned page types
([[0036]]-style)? AU bundles encode oneshots/timeskips today — the closest thing
[[0065-oneshots-as-spawning-pool]] has to an existing home. Branch arc-N-{primer,summary,
profile} triplets are a lifecycle pattern nobody designed — worth its own look.

**Verdict.** _(unevaluated.)_
