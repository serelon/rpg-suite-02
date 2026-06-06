# Census: solorpg data types (agent sweep, 2026-06-06)

> Explore-agent census of every data type across the solorpg vault (~25 main campaigns +
> branches). Preserved as reference for the KB-structure design work
> ([[knowledge-base-canonical-vault]] headline item). Distilled findings in
> [[0083-data-type-census]]. Condensed from the agent report; inventory and analysis kept
> in full, per-type prose trimmed.

## Summary statistics

- **~25 main campaigns** + many branches (sophie, mitchi, kailani, einherjar, vitae,
  heliodyne, tessera, vekris, xel-iri, zhiraska, frieda, wolf-bit, the-red, …)
- **Format distribution:** ~60% JSON, ~35% Markdown, ~3% JSONL, ~2% TXT, minor zip/html

## Inventory (type | format | location | breadth | schema? | variance)

| Type | Format | Location Pattern | Breadth | Schema/Template? | Variance |
|------|--------|------------------|---------|------------------|----------|
| Character profile | JSON | `characters/*.json` | 25/25 | template in bundles | dual minimal/full/sections; custom sections per campaign |
| Character profile (MD) | MD | `characters/*.md` | ~15 | templates exist | archived/supporting chars; mixed |
| Roster/group record | JSON | `characters/*-roster.json` | 20+ | repeated pattern | faction/subfaction grouping |
| Character archive | TXT/MD | `characters/*/archive/` | 18+ | none | mixed formats, historical versions |
| Memory record | JSON | `memories/*.json` | **7** | defined schema | array of memory objects |
| Location profile | JSON | `locations/*.json` | **2+** | basic | minimal+full pattern |
| Story collection | JSON | `stories/session-NN-stories.json` | **3+** | structured | told/private collections (eternal-witness) |
| Savefile (character) | MD | `Savefiles/*.md` | 25/25 | standard pattern | headers vary; kill counts, intel summaries |
| Savefile (campaign state) | MD | `Savefiles/*-state.md` | 18+ | varies | merged multi-character |
| Savefile (branch) | MD | `branches/*/savefiles/*.md` | 12+ branches | consistent | session-numbered |
| Nameset | JSON | `namesets/*.json` | 23/25 | defined schema | simple/aggregate/grouped |
| Primer (campaign) | MD | `primer.md` | 25/25 | template pattern | **high variance** |
| Primer (session) | MD | `reference/*-primer.md` | 15+ | none | context-specific |
| Primer (arc) | MD | `branches/*/arc-N-primer.md` | 6+ branches | none | multi-section |
| Primer (branch) | MD | `branches/*/primer.md` | 12+ branches | template pattern | variant setup |
| CLAUDE.md (campaign) | MD | `CLAUDE.md` | 25/25 | standard format | instructions + postprocess rules |
| CLAUDE.md (branch) | MD | `branches/*/CLAUDE.md` | 12+ branches | inherits | branch variations |
| Session summary | MD | `session summaries/*.md`, `Sessions/` | 20+ | **no strict schema** | narrative format varies |
| Intelligence brief | MD | special naming | 5+ | none | mission-formatted |
| Template (character) | MD | `templates/`, `character_capture_template.md` | 15+ | yes, examples | atomic/detailed variants |
| Reference document | MD | `reference/*.md` etc. | 25/25 | varies | **no consistent schema** |
| Bundle (session) | JSON/ZIP | `bundles/session-NN/` | 18+ | yes, manifest | session.json + assets |
| Bundle (story/AU) | JSON/ZIP | `branches/*/au-bundles/` | 12+ | template pattern | AU/oneshot variants |
| Bundle manifest | JSON | `bundles/*/session.json` | 18+ | **tight schema (100%)** | session #, POV, templates, includes |
| Bundle template | JSON | `bundle-template.json` | multi-level | standard | extends chains |
| aegis data/* | JSON | `aegis/data/*.json` | aegis only | custom schemas | threads, strategic, equipment, vault, enemy-templates, loadouts, blueprints, roster |
| aegis intel/* | JSON | `aegis/intel/*.json` | aegis only | custom | observed/actual enemies, tech |
| Session import | JSONL | `imports/*.jsonl` | 22+ | Claude export format | one per session |
| Session chunks | MD | `imports/chunks/session-NN-chunk-NN.md` | 22+ | generated | 1–5 per session, ~15–20k tokens |
| Session manifest | TXT | `imports/chunks/session-NN-manifest.txt` | 22+ | simple | metadata + chunk list |
| Branch index | MD | `branches/*/index.md` | 12+ | custom | file manifest |
| Branch arc summary/profile | MD/JSON | `arc-N-summary.md`, `arc-N-profile.json` | 6+ | custom | arc synthesis + state |
| Session guide | MD | branch bundles | 6+ | custom | per-session context |
| Skill definition | MD | `.claude/skills/*/SKILL.md` | 7 root skills | defined format | postprocess-v2, prep, workshop, campaign-setup, cheatsheet |
| Postprocess instructions | MD | `postprocess-instructions.md` | 3+ | template pattern | per-campaign automation rules |
| Timeline document | MD | `timeline.md` | 3+ | table format | session chronology |
| Writing/voice guide | MD | special naming | 5+ | none | voice + thematic guidance |
| Mission/location briefing | MD | au-bundle reference/ | 6+ | custom | objectives / spatial layout |
| Technical specs | MD | `Ship Classes/*.md`, `*-specs` | 8+ | custom | world-dependent |
| Faction guide | MD | various | 10+ | custom | structure/philosophy |
| Character manifest | TXT | `characters/*.txt` | 3+ | simple list | plain rosters |
| Branch/session memories | JSON | `branches/*/memories/`, `memories/session-NN-memories.json` | 4+/2+ | same as root | branch-scoped |
| Cheatsheet | HTML | `branches/*/player/cheatsheet.html` (and elsewhere — "abit all over the place") | many branches (user correction; census undercounted at 1) | yes — dedicated `cheatsheet` skill generates them | player-facing generated views; proven render pattern |
| Conversation transcript | MD | `transcripts/*-transcript.md` | 1 (lumina-city, 2 files) | emergent format (header + source-chunk citations + dialogue-only body) | **missed by original census**; undocumented type, see [[0062-conversation-transcripts-as-gm-context]] |

## Shape variance analysis (the census's key finding)

**High variance:** primers, reference documents, session summaries, technical specs —
human-authored prose, no tool in the loop.

**Low variance:** character JSON (~95% consistent), savefiles (~90%), namesets (~95%),
bundle manifests (100%) — formats with a tool and/or template behind them.

**Campaign-specific patterns:** aegis = heavy meta-game data; eternal-witness = story
collections + timeline; long-watch = heaviest branching + savefiles; AU bundles =
oneshots/timeskips as non-canonical explorations.

## Adoption gradient

Universal: characters, savefiles, primers, CLAUDE.md, namesets (23/25).
Narrow: memories (7), stories (3, really 1 systematic), locations (2). Confirms
[[0059-datastruct-census-underused-and-superseded]] with hard counts.

## Skills as format-definers

`session-postprocess-v2` → summaries, savefiles, memories. `campaign-setup` → CLAUDE.md,
primer, bundle-template.json. `session-prep` consumes primers/CLAUDE.md. The skills are
the de-facto schema authorities for the prose types.
