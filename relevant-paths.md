# Relevant Paths & Index

Living index for the research/speculation phase. Two jobs: (1) catalogue the **source
repos** we mine for patterns, (2) index every **note** we capture in `docs/notes/`.

Update this whenever a new source surfaces or a new note is written.

---

## Source repos (research material — read-only)

| Path | Role | User's framing |
|------|------|----------------|
| `../rpg-tools/` | Portable, stdlib-only Python toolbox (dice, oracle, tarot, namegen, characters/locations/memories). Packs into a Claude Desktop `.skill`. | Half obsolete, half cutting-edge, always used. |
| `../solorpg/` | The main vault: ~16 active campaigns, session import/export, bundling, post-processing agents, skills. Embeds `rpg-tools` as a submodule. | Data *very* important; workflows key but having growing pains; lots to refurbish. |
| `../aegis-tools/` | A modular rules/tool engine — an RPG *system* as CLI layers (`tactical` / `strategic` / `threads` / `intel` / `gm`) over `lib/` + `modules/`. | Rules engine in modular shape. |
| `E:\rpg` | Old, obsolete infra repo: Qdrant + Wiki.js + MCP, a 5-agent session pipeline (parse → entity → timeline → wiki → briefing). | Obsolete, but holds patterns never transferred over. Mine, don't run. |
| `E:\campaigns` | **Data-store** for `E:\rpg` (campaigns kept separate from tools, per that repo's design). Holds `the-great-awakening`, `the-long-watch`, `docker-data`. | Confirmed data-store; tools and data are deliberately split there. |
| `G:\My Drive\Projects\Tarot Tales` | An **earlier-generation system** (~gen 2–3): the "Tarot Tales RPG System" rulebook + worldbook + theme-flow rules, with settings (Celestial Empire, Moonlit Heritage, Throne of Stars, Whispers of the Old Gods, **The Great Awakening**, **Threads of Berlin**). Files are Google Docs (`.gdoc`) — content lives in Drive, not local. | Gen 2/3. Lineage: settings here resurface as `solorpg` campaigns. |

> More sources will surface over time (the user expects undiscovered folders). Add a row when they do.
> **Note:** data and tools are often split across folders (e.g. `E:\rpg` ↔ `E:\campaigns`). When a tool repo appears, look for its separate data-store.

---

## Notes index

One line per note in `docs/notes/`. Newest at top. See `docs/README.md` for conventions.

| Note | Kind | Source | One-line |
|------|------|--------|----------|
| [[0002-read-anywhere-write-canonical]] | pattern | rpg-tools | Tools read merged data from many locations, write only to a canonical path. |
| [[0001-tiered-progressive-loading]] | pattern | rpg-tools | Load minimal profiles by default; deepen on demand to protect context budget. |
| [[0000-note-template]] | — | — | Copy this to start a new note. |

---

## Themes (synthesis — grows later)

Themes start life as `theme/*` tags on notes. When a tag earns enough mass, it
graduates into a synthesis doc in `docs/themes/`. None promoted yet.
