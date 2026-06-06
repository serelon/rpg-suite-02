# Census: rpg-tools tools & schemas (agent sweep, 2026-06-06)

> Explore-agent census of every rpg-tools tool, its reads/writes, and documented data
> formats. Preserved as reference for the KB-structure design work
> ([[knowledge-base-canonical-vault]]). Distilled findings in [[0084-rpg-tools-data-layer]].

## Inventory

| Tool | Reads | Writes | Schema documented | Usage status |
|------|-------|--------|-------------------|--------------|
| dice.py | none (embedded) | stdout | README | active |
| tarot.py | none (hardcoded 78-card deck) | stdout | README | active |
| oracle.py | none (hardcoded systems) | stdout | oracle-guide.md | active |
| pool.py | pools/*.json; ~/.rpg-tools/pools/*.state.json | state json | pool-guide.md | active; **NOT multi-path discovery** (cwd only) |
| namegen.py | namesets/ (7-path discovery) | {cwd}/namesets/{id}.json | nameset-guide.md (extensive) | active |
| characters.py | characters/ (discovery); campaign/state.json for location filter | {cwd}/characters/{id}.json | character-guide.md | active |
| locations.py | locations/ (discovery) | {cwd}/locations/{id}.json | location-guide.md | active (but see 0059: barely wired in practice) |
| stories.py | stories/ (loose `*-stories.json`) | {cwd}/stories/{id}.json | story-capture-guide.md | active (1 campaign) |
| memories.py | memories/ (loose `*-memories.json`); probes characters/+locations/ for ref validation | {cwd}/memories/{id}.json | memories-guide.md | active |
| factions.py | factions/ (discovery); characters/ for members | {cwd}/factions/{id}.json | faction-guide.md | active per docs |
| campaign.py | campaign/{config,state}.json | same | campaign-state-guide.md | **built never used** |
| log.py | campaign/{config,log}.json | campaign/log.json | campaign-state-guide.md | **built never used** |

## The discovery pattern (lib/discovery.py) — read-anywhere / write-canonical

Search order (merged, later overrides earlier):
1. `{cwd}/{type}/` → 2. parent-dir walk → 3. `campaigns/*/{type}/` → 4. `tools/data/{type}/`
(bundled) → 5. `/mnt/skills/user/rpg-tools/tools/data/{type}/` (Claude.ai skill mount) →
6. `/mnt/user-data/uploads/{type}/` → 7. loose-pattern uploads (`*-stories.json` etc.) →
8. `/home/claude/*/{type}/` (extracted bundles).

Writes always go to `{cwd}/{type}/{id}.json`. Multi-collection files (namesets, stories,
memories) keyed `namespace:id`; single-item files by bare id. **Note:** paths 5–8 are
Claude.ai-runtime specific — transient-constraint flag (0031).

## Shared lib

- `persistence.py` — save/find-source/delete per item
- `lookup.py` — case-insensitive id/name search, dot-notation field filters
- `parsers.py` — era parsing ("~15000 BCE", "Y3.D45" → sortable), session parsing ("s01" → 1)
- `changelog.py` — update history from session logs
- `calendars/` — modular calendar (offset = structured "Y3.D45"; loose = "three days after
  arrival"); factory-created from campaign config

## Documented schemas (references/) — the proto-KB type system

- **Character:** `{id, name, faction, subfaction, tags, minimal{role, essence(≤35 words),
  voice}, full{appearance, personality, background, motivations, voice_samples[{context,line}]},
  sections{relationships, powers, combat, timeline, secrets, custom…}}` — tiered loading:
  minimal default, `--depth full`, `--section NAME`.
- **Location:** `{id, name, parent, parents[], tags, minimal{type, essence}, full{description,
  atmosphere, history, notable_features, dangers, secrets}, sections{npcs, connections{loc-id:
  path-desc}, resources, factions}}` — tree via parent(s), graph via connections, orphan
  detection in tree view.
- **Memory:** `{id, title, campaign, text, type(turning-point|vivid-moment|quiet-moment|
  revelation|world-building|relationship), format, era, session, intensity, perspective,
  tags, log_entry, story, connections{characters, locations, stories, related_memories,
  log_entries}}` — era/session sortable; **connection validation warns on broken refs**
  (no cascade; orphans flagged).
- **Story:** same metadata family as memory + collections (told/private) — memory's older
  sibling ([[0059]]).
- **Faction:** richest schema — minimal/full tiering + `hierarchy{subfactions}`,
  `members{named, units[{count,morale,role,location}], pools}`, `relationships[{type(ally|
  enemy|rival|debtor|patron|vassal|overseer), target, state, notes}]`, **`economy{accounts,
  running_costs, inventory, assets}`**, `resources{supply, fuel, custom…}`.
- **Nameset (v2):** simple/aggregate/grouped types; `namespace:id` two-segment resolution
  with bare-ref fallback; `extends` inheritance with circular detection; per-entry tags,
  gender, frequency; named format variants with per-slot mix policies; `hidden` flag;
  multi-nameset files with file-level namespace.
- **Campaign config/state/log:** branches[{id, protagonists, status}], convergences
  [{branches, location, era}]; state{active_branch, characters{location,status}};
  log entries{id, date|date_loose, summary, branch, importance, characters{id:role
  (defining|present|witness|mentioned)}, locations, tags, session, memory, story}.
- **Pool:** tokens with counts; draw_mode/auto_shuffle/on_empty settings; state persisted
  in `~/.rpg-tools/pools/`.

## Version skew found

Minor: nameset-guide's "Recommended Namespace Taxonomy" describes worlds-shared-across-
campaigns (valdran, caldworth, solramis as cross-campaign namespaces) — **a use case that
never manifested**; in practice namespaces are campaign-scoped. Docs describe intent, not
reality.

## Notable

- factions.py's economy submodule is the most elaborate schema in the toolbox — usage in
  real campaigns unverified by this sweep (candidate for the built-never-used audit,
  [[0050-built-never-used-inventory]]).
- pool.py is the only data tool *not* using multi-path discovery — an inconsistency.
- memories.py is the only tool doing cross-reference *validation* — the only
  link-integrity custodian behavior in the whole stack today.
