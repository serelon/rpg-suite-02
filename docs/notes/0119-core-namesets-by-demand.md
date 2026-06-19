---
tags:
  - kind/decision
  - source/conversation
  - theme/namesets
  - theme/data-types
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-18
---

# Grow the core nameset library by *demand*, not by harvesting supply

**What it is.** A method (and a derived target) for next-gen's core nameset library. The
core today is modern-only and is just the leaf set behind one aggregate (`metropolitan`).
"Grow the core" should be driven by a two-pass **demand** question, not by promoting
existing campaign sets:

1. *What would each **current** campaign pull from core, if it shipped no namesets of its own?*
2. *What would **hypothetical** campaigns in the same vein want?*

The union of those demands = the core target taxonomy. See [[census-namesets]] for the
full inventory this builds on.

**Why demand, not supply.** The walk (with the owner) killed the supply-side harvest plan:
- **core defaults — owner-vouched, most-used.** The 🟢 gold standard / quality template.
- **longwatch — "a mess"** even after a polish+replenish remediation pass
  (`tools/polish_namesets.py` + `replenish_namesets.py`). Write-off, not salvage.
- **aegis 1940s — suspect, never polished.** Subagent/Haiku-made; rebuild before any use.
- **emberfall species — setting-bound**, *including* dwarves/elves/goblins/lizardfolk. The
  census wrongly tagged these "generic core candidates" from their **names**; the owner says
  the **content** is Emberfall worldbuilding. → **reusability needs owner-validation exactly
  like quality does** (a label can read generic while the content is setting-baked).

So the clean, generic, promotable harvest is **thin — basically only Lumina's real-world
SE-Asian leaves** (malay/thai/indonesian/filipino/chinese-/indian-malaysian; Opus-made,
fill the exact SE-Asia gap). Everything else is rebuild, leave-it, or already-core.

**Therefore: grow-core is an *authoring* project**, built to the core-defaults quality bar —
not a reshuffle of a trove that isn't there. The Haiku/subagent generation route is the thing
to **retire**, not just its outputs (it produced both 🔴 veins). Demand-driven targeting is
*supply-independent*: the rot in longwatch/aegis is irrelevant to *what* to build.

**The derived target taxonomy** (every entry traces to ≥1 real campaign + its vein):

- **A. Modern real-world leaves** (extend place axis — demand-exposed gaps): SE Asia ·
  Pacific/Oceanic · Nordic/Scandinavian · Celtic/Irish · Greek · *real* Africa (today only
  nigerian+ethiopian) · Central Asian.
- **B. Historical era leaves** (new time axis; author clean): 1940s/WWII · Ancient
  (Rome/Greece/Egypt/Celtic/Germanic) · Prehistoric (paleolithic + neolithic, epithet
  structure) · Historical East-Asian · (medieval, victorian — hypothetical demand).
- **C. Genre/speculative archetype packs**: fantasy species · sci-fi human (imperial-formal /
  spacer-informal / void-born / evolved-substrate) · post-apoc · cyberpunk.
- **D. Smart default aggregates** (keep *few* — owner's constraint): metropolitan
  (American-city ✅) · European-city · SE-Asian-city · global-diverse · multinational-military ·
  ancient-city/arena · modern-civilian.
- **E. Generators** (procedural patterns: corporate/org names · handles/callsigns ·
  designations/serials (ships, specimens) · place names). **First-class namesets, co-equal
  with person-rosters** (owner, 2026-06-18) — *not* a separate tool-type. Rationale: the
  counter-default purpose ([[0013-counter-training-name-the-default]]) is **domain-general** —
  places/ships/orgs collapse to the model's tiny default set ("…Meridian", Aurora, Nexus) as
  hard as people collapse to "Marcus Chen", and arguably *louder* (fewer place-names per
  campaign, so each cliché repeats). See [[0120-default-naming-is-domain-general]].

Leaves/packs (A–C) combine freely → stock generously. D is curation → small. E is co-equal
with A–C and equally worth stocking.

**Open threads.**
- ~~E may not be "namesets" at all~~ **Resolved (owner):** generators *are* first-class
  namesets, co-equal with person-rosters — see above + [[0120-default-naming-is-domain-general]].
  (Procedural-pattern *mechanics* still relate to [[0087-spreadsheet-semantics-tool-data]], but
  that's an implementation detail, not a typing split.)
- Verify Lumina's SE-Asian leaves are real-world-generic and **not** Lumina-baked the way
  Emberfall's species turned out — same owner-validation gate.
- Audit the core defaults' *own* coverage gaps (they're vouched for quality, not completeness).
- Sequencing: which packs first? (SE-Asia harvest is the cheapest real win + proof-of-method
  for regional expansion.) Roadmap candidate once appraised.
- The leaf/aggregate seam is the clean core(leaves + few archetype aggregates)/campaign
  (bespoke weightings) split — refines [[census-namesets]]'s rule.

**Verdict.** _(unevaluated — but this note *is* the product of an appraisal walk; the
direction is owner-endorsed, pending formal judgement.)_
