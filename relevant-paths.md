# Relevant Paths & Index

> **Status (2026-06-05):** 66 notes — campaign-setup batch 0046–0050 now **appraised**
> (4 adopt, 1 adapt; 0050 = adopt-lesson / reject-campaign.py) — 6 preserved design-notes,
> first theme promoted **and appraised** ([[modular-self-evolving-architecture]]).
> Four north-stars: 0004 · 0024 · 0036 · 0041. **Work owed:** appraise the bounce batch
> (0051–0066, all unevaluated), bundle.py flaw audit (gates the compiler build-path),
> version-skew note, graduation mechanism, module contract (resolves 0038),
> re-read 0034 to settle the dropped 0049 linkage, circle back to the parked 0067
> questions (post-process as vault librarian? cherrypick contract?). Candidate second theme:
> **verbatim-anchors / voice-and-register** (0005–0008, 0030, 0053–0055, 0062).
> Unmined veins: **rpg-tools built-never-used sweep (0050 lead)**, **postprocess
> verbatim-rewrite audit (0054)**, three-primer drift check (0048 lead),
> hallucinated-tag corpus (0058), early-vs-late savefile diffs (0061),
> E:\rpg entity-registry → lore-search (0040), gm-skill craft layer, Tarot Tales,
> solorpg workshop handoff seam, guide-drift mapping.

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
| `C:\Users\serel\Code\reverse-mcp-rpg` | **"GM Assistant"** — a *reverse-MCP* experiment: Claude Code drives a live web GM dashboard in real time (Claude → MCP/stdio → bridge → WebSocket → FastAPI → browser). SQLite persistence + ChromaDB RAG; links to `solorpg` campaign folders. Python/`uv` + web frontend. | User's "most ridiculous entry — but the ideas are rich." **Experimental, but proven to work** (it shipped and ran). A different *axis*: live UI + inverted MCP flow — an existence proof, not just a concept. |
| `G:\My Drive\Projects\Tarot Tales` | An **earlier-generation system** (~gen 2–3): the "Tarot Tales RPG System" rulebook + worldbook + theme-flow rules, with settings (Celestial Empire, Moonlit Heritage, Throne of Stars, Whispers of the Old Gods, **The Great Awakening**, **Threads of Berlin**). Files are Google Docs (`.gdoc`) — content lives in Drive, not local. | Gen 2/3. Lineage: settings here resurface as `solorpg` campaigns. |

### Known sub-veins worth dedicated mining

- **`../solorpg/.claude/`** — rich and under-mined: `skills/` (campaign-setup,
  session-postprocess-v2, session-prep, workshop, cheatsheet), `agents/`, `plans/`, and the
  Claude-memory store `projects/*/memory/` (hard-won feedback like [[0003-scope-memories-to-context]]).
- **`../solorpg/campaigns/*/memories/`** — the campaign-memory JSON corpus (the data the
  memory tooling operates on). Data, not patterns — mine for *schema/workflow*, not lore.

### Frontends / external systems (targets, not core — also minable for patterns)

These are *surfaces the core might bind to*, per the frontend-agnostic aim
([[0004-frontend-agnostic-core]]) — not part of the core, but relevant.

| System | Relevance |
|--------|-----------|
| **Claude Desktop** | Primary target frontend; the `.skill` bundle workflow already targets it. |
| **Claude Code** | Want to be able to play here too (where we are now). |
| **reverse-mcp-rpg** | The user's own live-UI frontend (also a source above). |
| **SillyTavern** | A completely separate, isolated suite (character-card / chat frontend). Radical idea: bind the core to it too. Different paradigm — stress-tests how far agnosticism stretches. |

> More sources will surface over time (the user expects undiscovered folders). Add a row when they do.
> **Note:** data and tools are often split across folders (e.g. `E:\rpg` ↔ `E:\campaigns`). When a tool repo appears, look for its separate data-store.

---

## Notes index

One line per note in `docs/notes/`. Newest at top. See `docs/README.md` for conventions.

| Note | Kind | Source | One-line |
|------|------|--------|----------|
| [[0030-summary-as-compression]] | pattern | solorpg | Summaries = forward-looking state, "will it matter in 10 sessions?"; texture evicted to memories. |
| [[0029-information-boundary-enforcement]] | question | solorpg | Unmet need: secrets must not leak across POVs/saves; currently prose-only, no checkpoint. |
| [[0028-checkpointed-human-gates]] | pattern | solorpg | Draft→review→adjust→write at every artifact; additive-only diffs for core data. Agents propose, gates dispose. |
| [[0027-recurring-exception-taxonomy]] | reference | solorpg | Catalogue of per-campaign workflow-exception classes (non-linear, multi-branch, custom outputs…). |
| [[0026-exceptions-are-features]] | idea | solorpg | Well-defined workflow must absorb per-campaign deviation by design; move from prose patches to declared exception-profiles. |
| [[0066-mandatory-presence-not-length]] | pattern | claude-desktop | Thinking-block enforcement fails by attention starvation, not deletion; fix = mandatory checks + lean tail ("short, fixed, genuine"). |
| [[0067-campaign-data-as-linked-vault]] | idea | e-rpg | Resurrect the (never-built) wiki idea as an Obsidian-style vault: flat files are all-or-nothing reads; links make relations walkable — for humans and for JIT/compiler loading. |
| [[0068-multi-lens-data]] | pattern | solorpg | Same entity at several fidelities (full spec / GM brief / faction / character / location — Eisrand walkers in 5+ places, zero drift, by manual discipline). Killer app for vault+compiler: lenses as renders. |
| [[0065-oneshots-as-spawning-pool]] | pattern | solorpg/claude-desktop | Oneshots mostly fizzle but graduate 3 ways (→campaign, →branch, →canon arc); need cheap home, graduation paths, dignified fizzle. |
| [[0064-unharvested-archive]] | question | solorpg/claude-desktop | ~58 exports in repo vs ~500 RP sessions in Desktop; substrate mostly missing — bulk dump-and-triage is an agent-scale job. |
| [[0063-portable-bundles-constraint]] | pattern | solorpg | Away-from-repo play (phone/Desktop/web) is first-class: the bundle is the whole world → compiler needs thin (at-home/JIT) and fat (away/self-contained) target profiles. |
| [[0062-conversation-transcripts-as-gm-context]] | pattern | solorpg | Verbatim dialogue as GM context — "keeps the story from mutating." Third independent reinvention of verbatim capture. |
| [[0061-continuity-artifacts-under-suspicion]] | question | solorpg | Summaries (format doubt) and savefiles (structure + "wrong kind of datadrift") — used everywhere, trusted nowhere. Redesign candidates. |
| [[0060-jit-loading-retry]] | idea | solorpg | Pre-session infodump = architecture around old models' weak agency (0031 live); retry JIT with 4.7/4.8 as a testbed experiment. |
| [[0059-datastruct-census-underused-and-superseded]] | question | solorpg/rpg-tools | Locations barely used; story tool = one-campaign memory-predecessor. Port datastructs by load, not existence. |
| [[0058-flag-lifecycle-set-at-build-select-at-prep]] | idea | new | Tag at content-build (workshop/postprocess), select at session prep; both actors. Tag quality at write time is the crux. |
| [[0057-compiled-context-needs-audit-tooling]] | idea | new | Compiled files are hard to debug; need review/audit tooling (build manifest first, GUI later — reverse-mcp-rpg is the existence proof). |
| [[0056-files-as-build-products]] | idea | new | Compilation drops below the bundle: individual files (e.g. texture bank) compiled from campaign+character sources via tags/flags. |
| [[0055-register-anchor-banks]] | pattern | solorpg | Texture bank (harvested) + living dictionary (workshopped) anchor the *world's voice*; sample-book grid living in production. |
| [[0054-verbatim-capture-lost-intent]] | pattern | solorpg | Postprocessor rewrites scenes meant to be verbatim copies — workflow drifted from its own spec; suspected style-drift source. |
| [[0053-anchor-hierarchy-voice-keystone]] | pattern | tarot-tales/solorpg | Drift anchors learned one at a time: description failed, voice samples worked. Characters first; world after. |
| [[0052-evolution-vs-drift]] | idea | solorpg | Curation gates are canon *defense*: gated changes = evolution, uncurated divergence = drift, retconned back. Drift can eat whole settings. |
| [[0051-live-context-delta]] | idea | new | Bundles get patched *mid-session*; the running session must ingest just the delta, never a reload. Inter-session diffs already solved via git/PRs. |
| [[0050-built-never-used-inventory]] | question | rpg-tools | campaign.py built & never used; sweep rpg-tools for other shipped-but-dormant patterns before trusting their docs. |
| [[0049-disposable-bootstrap-primer]] | pattern | rpg-tools | Session-01-primer is scaffolding with declared expiry — consumed into data files after play. |
| [[0048-canon-precedence-and-naming-is-permission]] | pattern | solorpg | Naming a campaign = permission to load; primers are design intent, not canon, once play exists. |
| [[0047-multi-axis-data-management]] | idea | solorpg | Campaign/branch/subsetting are *axes*, not a fixed tree; per-era/per-character plausible next; The Silence is the proven exemplar. |
| [[0046-campaign-lifecycle-geological-strata]] | pattern | rpg-tools/solorpg | Campaign setup has 4 homes from 4 eras, no canonical source; entry is asynchronous & seed-heterogeneous, not a pipeline. |
| [[0045-runtime-composition-briefing-py]] | idea | new | Runtime composition: executable `briefing.py` with inline tool calls instead of static briefing.md. |
| [[0044-scenario-compiler]] | idea | new | The refer-back mechanism: a universal build process — modules as sources, spec as target, scenarios compiled. ✅adopt |
| [[0043-campaigns-as-testbeds]] | idea | new | Every campaign is an architectural experiment; proven experiments graduate into the spec — the upward arm of self-evolution. |
| [[0042-async-fleet-migration]] | idea | new | Campaigns upgrade to the current spec independently, not lockstep; separates intentional exceptions from stale drift. |
| [[0041-self-evolving-versioned-spec]] | idea | new | **North-star (4th):** self-evolving system governed by a single versioned canonical spec — kills "go look at campaign A" folklore. |
| [[0040-vector-db-as-lore-search-module]] | idea | old-erpg/new | E:\rpg's Qdrant store reframed as the lore-search module; centralization *is* a module — dissolves modules-vs-central tension. |
| [[0039-bundle-template-composition]] | pattern | solorpg | Declarative session composition: inheritance + multi-chain merge + glob includes + auto reference-following. The assembly layer for modules. |
| [[0038-shared-infra-vs-modules]] | idea | rpg-tools | Instruments are standalone, but 8 data tools share `lib/`; horizontal infra vs vertical modules is the modularization crux. |
| [[0037-rpg-tools-modularization]] | idea | new/rpg-tools | Split rpg-tools' one monolithic desktop skill into one skill per tool/workflow — `0036` made concrete; first migration target. |
| [[0036-every-subsystem-is-a-module]] | idea | new | **North-star (3rd):** every subsystem is a self-owning module; consumers refer back, never copy. Cure for the scaffold problem. |
| [[0035-surgical-git-staging]] | pattern | solorpg | Branch-per-run, never `git add -A`; stage only what this run wrote. Agent-in-shared-repo safety. |
| [[0034-outgrown-scaffold]] | idea | solorpg | **Key lesson:** the system outgrew its scaffold; knowledge composition (hand-wired paths, drifting duplicate guides) is the bottleneck. |
| [[0033-workflow-defers-to-canonical-guides]] | pattern | solorpg | Lean workflow spine reads canonical guides JIT at point-of-use instead of embedding them. |
| [[0032-preprocessing-token-hygiene]] | pattern | solorpg | Strip junk tokens before reading (durable); chunking-to-fit-read-limit is the transient shell. |
| [[0031-beware-transient-constraint-architecture]] | pattern | solorpg/new | Don't architect around transient model limits; the v2 team split died when 165k→1M (v1 lives on). |
| [[0025-lead-plus-persistent-lorekeeper]] | pattern ⚠️obsolete | solorpg | Persistent source-holder + thin orchestrator. **Obsolete:** existed only to fit 165k; 1M killed it. |
| [[0024-pluggable-extension-modules]] | idea | new/aegis-tools | **North-star:** freeform core that can slot in a whole rules-engine module (aegis-scale) when wanted. |
| [[0023-event-bus-orchestrator]] | pattern | aegis-tools | Thin core emits time events; self-registering modules subscribe — decoupled, pluggable. |
| [[0022-reference-vs-state-data-driven-types]] | pattern | aegis-tools | Rulebook (reference) vs savegame (state); types are runtime-editable data, lore grows in play. |
| [[0021-data-required-as-prompt]] | pattern | aegis-tools | Missing data halts and prompts the GM to author it (exit 2), never crashes or fabricates. |
| [[0020-observed-vs-actual]] | pattern | aegis-tools | Model fog-of-war as data: parallel observed (known) vs actual (true) field sets. |
| [[0019-companion-rationale-as-anti-regression]] | pattern | claude-desktop | Ship a "why" doc with each artifact so future edits don't re-poison it back toward the norm. |
| [[0018-layered-skill-architecture]] | pattern | claude-desktop | Split craft skill ⟂ mechanics module ⟂ tools ⟂ bundle data; each owns one concern. |
| [[0017-recap-as-verification]] | pattern | claude-desktop | Reframe resume-recap as a checkpoint that verifies state survived compaction; gaps aim tuning. |
| [[0016-thinking-as-enforcement]] | pattern | claude-desktop | A skill only fires if a pre-commit thinking check interrupts the trained reflex; heavy but genuine. |
| [[0015-compounding-loops]] | pattern | claude-desktop | Failure family: small misread reinforces itself turn-over-turn; cure = target tempo, not gradient. |
| [[0014-scope-stripping]] | pattern | claude-desktop | Failure family: narrow-true things go global (always/never flattening; temporary→permanent). |
| [[0013-counter-training-name-the-default]] | pattern | claude-desktop | Author counter-default rules as default-pull + correction + why, so intent survives context load. |
| [[0012-intelligence-in-scaffolding]] | idea | sillytavern | Compile craft into scaffolding so small/local models only need fluent in-voice continuation. |
| [[0011-identity-pinned-state-evicted]] | pattern | sillytavern | Pin always-true identity in context; push time-bound state to an updatable/evictable layer. |
| [[0010-docs-as-code-context-compiler]] | idea | sillytavern | Compile context per-beat from tagged frontmatter (build target), not fuzzy RAG over a pile. |
| [[0009-jit-context-and-eviction]] | idea | sillytavern | Eviction (not retrieval) is the underbuilt half; beats are eviction boundaries; pacing=context. |
| [[0008-form-is-the-lesson]] | pattern | sillytavern | An example teaches its method, not subject; plainness can only be keyed by plain text. |
| [[0007-harvest-vs-workshop]] | pattern | sillytavern | Grow easy cells from clipped play, hand-seed hard ones (bootstrapping deadlock); findability first. |
| [[0006-sample-book-grid]] | idea | sillytavern | A (scene-type × register) grid of worked voice exemplars; precompiled or JIT. |
| [[0005-exemplars-over-instructions]] | pattern | sillytavern | Register is tacit; steer voice by demonstration, not specification — "like this" > rules. |
| [[0004-frontend-agnostic-core]] | idea | new/cross | North-star: a frontend-agnostic core that factors into Claude Desktop, Claude Code, reverse-mcp, SillyTavern… |
| [[0003-scope-memories-to-context]] | pattern | solorpg | Scope every memory to campaign/branch/character or it degrades into soup at scale. |
| [[0002-read-anywhere-write-canonical]] | pattern | rpg-tools | Tools read merged data from many locations, write only to a canonical path. |
| [[0001-tiered-progressive-loading]] | pattern | rpg-tools | Load minimal profiles by default; deepen on demand to protect context budget. |
| [[0000-note-template]] | — | — | Copy this to start a new note. |

---

## Design-notes (preserved long-form sources)

Rich, multi-idea docs (the user's own design thinking, companion/"why" docs) are kept
**verbatim** in `docs/design-notes/`, with their distinct ideas extracted as atomic notes
that link back. See `docs/README.md` → "Design-notes".

| Doc | Atomized into | One-line |
|-----|---------------|----------|
| [[sample-book]] | notes 0005–0012 | Steer voice by demonstration via a (scene-type × register) exemplar grid; the voice-layer of a docs-as-code context architecture. |
| [[gm-skill]] (+ [[gm-skill-SKILL]], [[gm-skill-RATIONALE]]) | notes 0013–0019 (meta layer) | Working Claude Desktop GM skill + its anti-regression rationale doc. Craft layer preserved, not yet atomized. |
| [[gm-skill-thinking-tuning]] | note 0066 | Field incident (Lumina City s04): thinking-block enforcement starved by a "stop overthinking" instruction; fix = mandatory checks, not length. First inbox report. |
| [[session-postprocess]] (+ [[session-postprocess-SKILL]]) | notes 0033–0035 (+0028/0030/0032) | The flagship live workflow. Headline lesson: outgrown scaffold / knowledge-composition bottleneck. |

## Themes (synthesis)

Themes start life as `theme/*` tags on notes. When a tag earns enough mass, it
graduates into a synthesis doc in `docs/themes/`.

| Theme doc | Synthesizes | Thesis |
|-----------|-------------|--------|
| [[modular-self-evolving-architecture]] | 0034·0036·0024·0037·0038·0039·0040·0041·0042·0043 (+0010·0033·0026) | One home per concern; refer back & compose, don't fork; evolve by graduating campaign experiments into a versioned spec. |
