# Relevant Paths & Index

> **Status (2026-06-13):** 119 notes. **Voice-register cluster appraised** (0005–0008 +
> 0092 **adopt**, 0099 **undecided**): the Sample Book spine (exemplars-first; works for Opus
> too — pattern-match, don't interpret), retrieval-before-generation (already loadbearing in
> post-processing), and weave-doctrine (firm in spec, forgiving in judgement) all adopt.
> Synthesis: **[[0118-encoding-by-data-type]]** (new) — encode by data type, three registers
> (tacit→exemplar/prose · factual→structured records · relational→pseudocode); prose for
> pattern-matching *alone*; "Excel-sheet doctrine" mixes 2+3 only by exception. **Third theme
> doc promoted: [[voice-and-register]]** (2026-06-15) — **appraised, adopt**; spine ratified,
> components keep their own verdicts (0099 adopt-scoped-to-reading-1, 0113/0114/0117 adapt). **Local-finetuning cluster
> (0113–0117) appraised**
> (from the inbox LoRA conversation, [[Claude-export-custom-lora]] preserved as a source).
> Reframe: the LoRA is a **sidequest** (play stays on Opus in Desktop) — the durable win is a
> **scene/register categorization layer** serving the **sample book** (quickest+best win,
> 0006/0055), with LoRA-dataset prep a free rider. Verdicts: 0113 distill **adapt**
> (workshop technique for curated exemplars), 0114 register-grid **adapt**, 0116 earns-its-keep
> **adopt** (the sidequest gate), 0115 idiom-vs-facts **undecided** (parked), 0117 **adapt →
> resolved principle**: *rewrite belongs to the curated layer + needs an explicit anchor; copy
> to the verbatim layer* (dissolves the 0113↔0054/0094 tension; extends 0007 with a
> rewrite-harvested middle gear). Feeds the **voice-register** theme. Import-pipeline cluster added
> (0108–0112) from
> solorpg pre-planning ([[import-design-brief]] + [[export-structure-map]] preserved as
> design-notes; **roadmap candidate**); confirmations folded into 0001/0102/0103.
> Progression cluster (0104–0107) and ST-preset cluster (0100–0103) also unappraised.
> _(historic, 2026-06-06: 82 notes.)_ Appraised: 0046–0050 (4 adopt, 1 adapt) and the
> **KB cluster** 0067–0069 + 0073 + 0075–0077 (adopts; 0077 adapt; 0072 undecided —
> cause unknown). 6 preserved design-notes, first theme promoted **and appraised**
> ([[modular-self-evolving-architecture]]). Four north-stars: 0004 · 0024 · 0036 · 0041.
> **Process agreed:** appraise (themed batches) → promote themes → feature specs (claims
> cite notes; open questions first-class) → roadmap; never spec ahead of appraisal.
> **Work owed:** appraise remaining backlog (0051–0066, 0070–0071, 0074, 0078–0082),
> promote KB/vault theme; bundle.py flaw audit, version-skew note, graduation mechanism,
> module contract (resolves 0038), re-read 0034. Second theme promoted **and adopted**:
> [[knowledge-base-canonical-vault]] (headline work: KB structure — types, formats,
> templates). Candidate themes:
> **verbatim-anchors / voice-and-register**
> (0005–0008, 0030, 0053–0055, 0062), **engineer-and-gardener doctrine** (0078–0082).
> Unmined veins: rpg-tools built-never-used sweep (0050), postprocess verbatim-rewrite
> audit (0054), aegis schema-drift git-history check (0072), three-primer drift check
> (0048), old cut'n'paste housekeeping prompts (0073), hallucinated-tag corpus (0058),
> early-vs-late savefile diffs (0061), E:\rpg entity-registry → lore-search (0040),
> gm-skill craft layer, Tarot Tales, workshop handoff seam, guide-drift mapping,
> Desktop bulk datadump workflow (0064, planned).

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
- **`../solorpg/imports/`** — pre-planning for the export→import pipeline. Patterns mined
  into 0108–0112; docs preserved as [[import-design-brief]]/[[export-structure-map]]. Holds
  the 116 MB Claude Desktop export zip (the substrate behind [[0064-unharvested-archive]]).

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
| [[0125-texture-has-no-capture-path]] | observation | solorpg/conversation | **The memory system can't capture low-weight texture** — the standing, minor-but-memorable details of a world (how a uniform looks, a dead-drop procedure). A **prompting gap, not storage**: extraction asks "what mattered *most*?" so texture (load-bearing for *immersion/consistency*, not *plot*) falls through; the `sensory` type is for emotional *moments*, not standing *facts*. Punches a hole in [[0030]]'s "texture evicted to memories." Open: same artifact as the texture bank [[0055]] or a sibling? new type / separate store / second sweep-pass? needs a recall path too. **Unevaluated.** |
| [[0124-the-grand-loop]] | pattern | conversation | **The whole-system lifecycle as one closed cycle with inlets + a drain** (captured as *shape* before becoming roadmap spine). Engine: `〈campaign vault〉 → session-prep → bundle → play → export → import → [postprocess] → vault`. Folds: **import is two-phase** (bulk claude.ai-dump ingest / corpus-routing [[0108]]–[[0112]] → per-session); **workshop inlet** forks 3 ways — *bootstrap (seeds, consume-to-prime)* → session-prep, *reference (engineered, persists)* → vault, *scratch/quarantine* (must not contaminate repo); **the drain** = archive old data → cold storage (**vault = live; archive = cold**). **Branch is NOT in the loop** — it's a selector/filter ([[0123]]). Two named black boxes queued for their own passes: `[postprocess]` and `〈vault〉` internals. **Unevaluated.** |
| [[0123-branch-as-organizational-axis]] | principle | solorpg | **A `branch` is a parallel protagonist/POV *workspace* in one shared world+timeline — NOT a canon fork** (Long Watch: Val/Lyra/Rosa/Sophie/… all same campaign, one session counter). Branch is **organizational/context-assembly** (owns the folder, savefiles, bundle template), nests for *shared-state* reasons (Leviathan parent = fleet-save container over Val/Lyra/David sub-branches), and **interleaves** on the global session #. **Arc lives *inside* a branch.** Hard rule: **organization (branch) ≠ narrative structure (arc); track separately** — conflating breaks things. Corrects 0121's earlier "arc interleaves" mis-attribution. **Adopt** (proven in solorpg). |
| [[0122-compaction-boundary-descends]] | observation | conversation | **The season break was a *coupled* constraint** — all summaries lived in context until they had to compact, and *that* was the season boundary; the finale was a real beat the window-pressure *pushed toward*. Now **the compaction boundary is descending** (season → per-arc compactions): dynamic context-building relaxes the finale-forcing, so pacing breathes. A clean [[0031]] instance. **Verdict: adapt** — compaction-as-tunable *adopted* (next-gen commitment); season's survival *undecided/on-probation* (owner barely uses it post-current-system; legacy-only). |
| [[0121-narrative-granularity-ladder]] | idea | conversation | **The units of play, finest→coarsest: `update < scene < act? < session < arc? < season < campaign`** (session = the numbered, load-bearing unit, fka *episode*). **It isn't a tree** — a session sorts on **two time-axes** (*telling-order* = session #, the monotonic spine; *story-time* = timeline, jumps when non-linear → bitemporal [[0103]]) plus a **separate organizational cross-cut, `branch`** (POV workspace; what actually interleaves — see [[0123]]). `arc` is narrative-*within*-a-branch, not the cross-cut. Units are apply-when-earned annotations (act/arc declarable ahead *or* retroactively); only session# is reliably pre-declared. **Verdict: adopt** — owner-ratified foundation (units settled, storage deferred); three axes are *capacity*, not mandatory population (guards the [[0031]] over-build trap). |
| [[0120-default-naming-is-domain-general]] | principle | conversation | **The "Marcus Chen" default-pull ([[0013]]) is domain-general** — places/ships/orgs/handles collapse to defaults ("…Meridian", Aurora, Nexus) as hard as people, arguably *louder* (fewer place-names → each cliché echoes more). So **generators are first-class, co-equal namesets**, not a separate tool-type; stock them generously. Resolves 0119's open thread E. Wants a banned/overused-list referent ([[0076]]). |
| [[0119-core-namesets-by-demand]] | decision | conversation | **Grow the core nameset library by *demand*, not by harvesting supply.** Two-pass lens: what current campaigns would pull from core if they shipped nothing + what hypothetical same-vein campaigns want = target taxonomy (modern-leaf gaps · historical-era leaves · genre archetype packs · few smart aggregates · generator toolkit). Supply-independent: harvest is thin (only Lumina SE-Asia is clean+generic), so grow-core = an *authoring* project built to the core-defaults bar; retire the Haiku/subagent route. Open: generators may be a separate tool-type. Born unevaluated (owner-endorsed walk). |
| [[0118-encoding-by-data-type]] | principle | conversation | **adopt — voice-register synthesis.** Encode by data type: 3 registers sorted by tacitness — tacit→**exemplar/prose** (sample book), factual→**structured records** (sheets/stats, already solved), relational→**pseudocode** (the glue). Prose for pattern-matching *alone*; old system's prose-over-reliance bred drift. "Excel-sheet doctrine" mixes 2+3 only by exception; keep blocks fine-grained for auditability. Open seam: when must a record graduate to relational pseudocode (0099's trial)? |
| [[0117-distill-vs-verbatim-tension]] | principle | conversation | **Resolved:** the *layer's contract* decides, not the operation. Rewrite belongs to the **curated layer** (sample book/texture bank — the feature) + needs an **explicit anchor** present; **copy-only** in the verbatim source (transcripts/memories — 0054's sin was rewriting the wrong layer). Dissolves the 0113↔0054/0094 tension; the anchor-presence is the whole 0113-vs-0054 difference. Open edge: a fine-tune *bakes* derived voice into weights (sidequest-gated). |
| [[0116-lora-earns-its-keep]] | principle | conversation | The skeptic's gate: userstyle+few-shot ≈ 85% on capable models; a fine-tune earns its keep only where prompting can't reach — canonically, making a *small/local* model hold a register zero-shot can't. Keeps fine-tuning in its lane; feeds 0081 writer/planner split. Per-campaign hot-swap adapters (0091) = solution maybe ahead of its problem. |
| [[0115-lora-idiom-lorebook-facts]] | principle | conversation | Single-source-of-truth applied to weights: fine-tune carries voice + setting-*idiom*; hard facts (numbers, named tech, who's-who) stay in the lorebook. Weights are the worst place to store a fact — unauditable, un-updatable, lossy. Extends 0011/0107: model weights are a substrate, and they're for idiom not data. |
| [[0114-voice-vs-setting-fidelity]] | pattern | conversation | "Sails on starships" is a *default-association* error, not a voice error — different layer fixes it. Fine-tuning shifts defaults *better* than it teaches voice → contrastive anchors at the cliché fork. Generalizes as a diagnostic axis. Discover registers by clustering, don't enumerate (0006/0110). Rewrite step launders the cliché unless gated by an external banned-list (0076). |
| [[0113-distill-dont-imitate]] | idea | conversation | When the corpus is inconsistent and *unifying* is the goal, training on it raw teaches the inconsistency. Distill instead: strong model rewrites raw scenes toward the canonical-voice spec → consistent by construction. Two filters (situation-in / QC-out); 50 range-spanning anchors as style bible. Tension w/ 0054/0094 → 0117. |
| [[0112-design-now-build-into-frame]] | principle | solorpg | Design now, build into the refactor — durable capabilities, not bolt-on scripts. The import brief waits *on purpose*: its core pieces are data-model decisions. Test: "native capability or bolt-on?" Discipline against premature scripting; import pipeline = a roadmap-candidate entrypoint, not a side tool. |
| [[0111-provenance-graph-as-secret-history]] | idea | solorpg | seed-of/variant-of/crossover edges reconstruct how settings *evolved* (oneshot→canon, failed sibs orbiting a success) — folder-routing discards it as residue. Lineage = first-class artifact. Same shape as Tarot→solorpg lineage, oneshot graduation (0065), branches (0103). |
| [[0110-wilderness-survey-idea-recovery]] | pattern | solorpg | Two spines on one embed pass: supervised routing + unsupervised wilderness survey. The survey (lost seeds, forgotten campaigns) is the higher-value half. Mechanized answer to 0064; engine for 0065. Idea-recovery as a *standing* tool, not a one-time import. |
| [[0109-knn-not-centroids-drift]] | pattern | solorpg | Classify orphans by k-NN over individual labeled points, NOT centroids — long campaigns drift (arc/tone/POV/model); averaging blurs the campaigns that matter. Bonus: top-2 neighbours from different campaigns = the crossover detector for free. Extends 0098. |
| [[0108-multi-label-relational-routing]] | pattern | solorpg | Routing = a *set of typed edges* (belongs-to / crossover / seed-of / variant-of / about / cluster / unrelated), each with confidence + provenance-of-decision (heuristic/embed/model/human), not one folder. Tags-are-truth applied to routing; the 0102 cross-ref layer made concrete. |
| [[0107-prose-deprecation-doctrine]] | principle | conversation | Deprecate prose for *data* (illegible/lossy/drift/rewrite-only); structure by default. Keep prose only where it's the *payload* (voice/appearance/texture), heavily curated. Splits corpus by payload-vs-carrier. |
| [[0106-three-layer-character-record]] | pattern | conversation | Character/progression in 3 layers: mechanical (defined statblock, JSON, CRUD), semantic (interpretation contract — the layer Tarot fatally lacked), prose (curated, where prose is the payload). Failures = a missing/collapsed layer. |
| [[0105-tarot-progression-unifying-failure]] | pattern | tarot-tales | Tarot's 4 progression gears (aspects/traits/Discovery/Between-Adventures + Powers) all failed one way: under-specified markers, no semantic layer → decay into flavor. Token-heavy stars + rewrite-to-update = a 0073 instance. Cap problem too. Fixed in Aegis. |
| [[0104-progression-as-pluggable-layer]] | idea | conversation | The 3 eras = points on one axis (module off→light→heavy): freeform off, Tarot light(-broken), Aegis heavy. Next-gen owns the *axis* — progression as a pluggable layer (0024 applied to progression); Aegis = the dial maxed, not an exception. |
| [[0030-summary-as-compression]] | pattern | solorpg | Summaries = forward-looking state, "will it matter in 10 sessions?"; texture evicted to memories. |
| [[0029-information-boundary-enforcement]] | question | solorpg | Unmet need: secrets must not leak across POVs/saves; currently prose-only, no checkpoint. |
| [[0028-checkpointed-human-gates]] | pattern | solorpg | Draft→review→adjust→write at every artifact; additive-only diffs for core data. Agents propose, gates dispose. |
| [[0027-recurring-exception-taxonomy]] | reference | solorpg | Catalogue of per-campaign workflow-exception classes (non-linear, multi-branch, custom outputs…). |
| [[0026-exceptions-are-features]] | idea | solorpg | Well-defined workflow must absorb per-campaign deviation by design; move from prose patches to declared exception-profiles. |
| [[0066-mandatory-presence-not-length]] | pattern | claude-desktop | Thinking-block enforcement fails by attention starvation, not deletion; fix = mandatory checks + lean tail ("short, fixed, genuine"). |
| [[0067-campaign-data-as-linked-vault]] | idea | e-rpg | Resurrect the (never-built) wiki idea as an Obsidian-style vault: flat files are all-or-nothing reads; links make relations walkable — for humans and for JIT/compiler loading. |
| [[0068-multi-lens-data]] | pattern | solorpg | Same entity at several fidelities (full spec / GM brief / faction / character / location — Eisrand walkers in 5+ places, zero drift, by manual discipline). Killer app for vault+compiler: lenses as renders. |
| [[0069-one-knowledge-base-many-presentation-layers]] | idea | conversation | One shape-invariant KB; presentation as swappable consumers: bundle compiler (monolith+db), agentic link-following (initiative prompting = blocker), SillyTavern-style keyword RAG. |
| [[0070-threads-tracker-design]] | pattern | aegis-tools | The quest tracker that "worked really well": semantic slugs, auto-reverse bidirectional links, max-one-level nesting, real state machine, prose-next-to-facts. Vault-layer lessons. |
| [[0071-fog-of-war-as-data-structure]] | pattern | aegis-tools | Observed/actual splits with field whitelists; hidden randomized thresholds (stored, undisplayed). Lenses with an epistemics axis — GM-secrets vs player-knowledge page scoping. |
| [[0072-schema-drift-tools-vs-hand-edited-json]] | question | aegis-tools | Live aegis JSON drifted past CLI schemas (and was better for it); tools tolerated it. Validate loudly / fail softly? Needs a "schema PR" loop when humans outgrow the schema. |
| [[0073-structured-mutation-beats-rewrite]] | principle | solorpg, aegis-tools | Why threads earned trust and savefiles didn't: append/transition/patch never re-emits existing content; wholesale regeneration is the drift aperture. Lead: find the old cut'n'paste housekeeping prompts. |
| [[0074-project-unicorn]] | idea | conversation | The declared endgame: the ultimate RP client, final frontend to the stack. Probably fails ("out of steam/tokens") — so every layer must stand alone; Unicorn is capstone, never dependency. |
| [[0075-postprocessing-as-vault-librarian]] | idea | conversation | Post-process = the KB's write path (vault mutations, not regenerated files). Open: second librarian (custodian/gardener)? Streamed scene-by-scene condensation vs end-of-session batch? |
| [[0076-self-canonizing-hallucinations]] | pattern | claude-desktop | Fact-check rounds launder hallucinations: "was written in, so must be canon!" Defenses: provenance pointers, check against the layer below (never a doc against itself/siblings). |
| [[0077-context-injection-vs-cache-economics]] | question | conversation | Unicorn tension: ST-style per-turn injection fights prefix caching. Sketch: layout by volatility, append mid-scene, re-layout at scene boundaries (same boundary problem as 0075). Cache logic lives in the consumer (0031). |
| [[0078-zoom-out-first-worldbuilding]] | principle | conversation, solorpg | Suggested (never enforced) setup order: world → zoom in → first pov character last. Character-first builds a container-world; weighting persists even after refactors (Lumina City, Emberfall/Xel-iri). |
| [[0079-relational-anchoring-antipattern]] | anti-pattern | conversation, solorpg | LLM writes new entities as relatives of in-context material ("character A's favorite place" vs evergreen description). Workaround: exclude unwanted context while worldbuilding. Lint candidate for the custodian. |
| [[0080-engineer-and-gardener]] | principle | solorpg | Load-bearing doctrine: engineer (OOC workshop — design, primers, seeds) and gardener (IC play — grows seeds organically); librarian harvests. One-line seed → played session → 1000-word profile. |
| [[0081-writer-planner-split]] | idea | conversation | Unicorn: local RP-finetune writes prose, Opus plans/judges. Two attentions solve attention starvation; tier-by-judgment applied to live play. Interface = the seed contract? |
| [[0082-live-hook-pipeline]] | idea | conversation | Event-driven agents after the writer (live extraction, widget updates): "run agent x at stage a whenever y happened." Tiny cheap hooks for often-run things; writer never does bookkeeping. The mechanism for streamed librarianship. |
| [[0083-data-type-census]] | pattern | solorpg | ~50 data types censused; shape variance tracks tool-backing almost perfectly; adoption gradient hard-counted; skills are de-facto schema authorities for prose types. Input inventory for KB-structure work. |
| [[0084-rpg-tools-data-layer]] | pattern | rpg-tools | The toolbox is a proto-KB: tiered records (minimal/full/sections), read-anywhere/write-canonical, namespace+extends, ref validation (memories.py only), era parsers. Steal primitives, not plumbing. |
| [[0085-knowledge-entries-vs-tool-data]] | principle | conversation | The KB's first type cut, by *substrate*: knowledge entries = vault pages on one base template regardless of complexity (incl. characters, savefiles); tool data = raw JSON outside the tree; images = third substrate. Flags extensible per module, always documented. |
| [[0086-faction-as-character-economy]] | pattern | rpg-tools, solorpg | Faction-as-character mode (Delacroix mothballed, Askvargr candidate) + its never-deployed economy module ("glorified spreadsheet"). New failure mode: tool illegibility — owner can't read/audit → forgets → mothball. |
| [[0087-spreadsheet-semantics-tool-data]] | idea | conversation | Spreadsheet semantics decomposed for agentic flow: CSV state + recalc-in-code + generated HTML view. One campaign-spreadsheet tool-data type, many templates (faction economy, aegis strategic). |
| [[0088-player-display-artifacts]] | pattern | solorpg | Third audience class: player-only renders (cheatsheets), redundant by construction, GM forbidden to read them. Endpoint-constrained to one member today; Unicorn's widget panes are where it grows. |
| [[0089-sealed-secrets-files]] | pattern | solorpg | Content hidden from the GM model until a declared trigger ("DO NOT READ until…") — prevents foreshadowing leak, enables big twists. Never opened early; sometimes needs prodding open. Railroads legitimate inside sealed bounded segments. |
| [[0090-cherrypick-contract-three-layers]] | decision | new | T7 resolved — go. Working PoC (`experiments/cherrypick/`): dotted-path extraction from vanilla Obsidian pages. Contract: frontmatter = edges/scalars, json blocks = nested data, sections = prose. |
| [[0091-one-vault-campaign-folder-entrypoints]] | decision | new/solorpg | Campaign isolation decided: one big vault, campaigns/ subfolders, session entrypoint = the campaign folder, boundaries enforced by tool. Isolation + info-boundaries become one guard. |
| [[0092-weave-player-input-doctrine]] | pattern | conversation | **adopt** (firm in spec, forgiving in judgement). GM must interleave-and-render player input, never echo-then-append. Fidelity hierarchy: intent sacred → voice corrected → inner life simulated → impossible actions error-corrected. Counter-trained vs AI-RP norms → keep the instruction firm. |
| [[0093-novelization-as-output]] | idea | conversation | Optional output format: seamless novel render of a campaign for the user's own rereading. Sonnet 3.5 one-shot misplaced slices; modern retest + pipeline shape open. |
| [[0094-save-everything-deferred-compute]] | principle | conversation | Raw session data hoarded losslessly as deferred compute — re-render stories when future models can handle it. Renders disposable, transcript layer permanent. (Self-labeled vanity project.) |
| [[0095-two-repo-public-private-split]] | decision | conversation | Next-gen: public core repo (tools/skills/workflows) + private campaigns repo nested in campaigns/; research vault stays private too. Structural boundary now; publishing machinery (dev→public squash-snapshot mirror, denylist hooks) deferred until public is pursued. |
| [[0096-enforcement-matches-reversibility]] | principle | conversation | Match enforcement to failure reversibility: campaign bleed is recoverable → tool-enforced (0091); public leak is irreversible → structural split (0095). Ladder: discipline → tool → gate → structurally impossible. |
| [[0097-interleaved-checklist-thinking]] | pattern | conversation | Old experiment: per-paragraph think-blocks (pacing / stop-point / fact-check). Fact-check is *the* damning 0076 example — checked drift against its own prose, self-confirmed. Checklist-discipline is the keeper; modern Opus collapses it. Self-checks need an external reference. |
| [[0098-vector-index-over-vault-not-store]] | question | conversation | Vector DB as a rebuildable *index over* the vault (vault = source of truth), not a store. Refines 0040's ownership. Multi-granularity (page+section+) with filters = E:\rpg chunking kept, store dropped. Sealed secrets must be hard-filtered or search blows the seal. |
| [[0099-pseudocode-as-encoding]] | idea | conversation | **adopt — scoped to reading 1** (reappraised 2026-06-15; split the readings — see [[0118-encoding-by-data-type]]). Format prompts/lore as pseudocode. Reading 1 lore-as-data (relational, category 3) **adopt** — committed direction, still `maturity/experimental` (untested in own workflow, came from SillyTavern). Reading 2 logic-as-control-flow (*procedural*, `if new_scene: scene_header()`) **deferred to the prompt-rebuild phase** — it's a prompt-engineering move, not yet that stage. No inherent railroad risk (that came from a bad narrative example); layer rule is control-flow on procedure not narrative content. Structured records (sheets) are category 2, already solved. Early win: human auditability. |
| [[0100-fragment-library-prompt-assembly]] | pattern | new (ST presets) | ST preset architecture: fragment pool + ordered enable-manifest + marker/data-hole slots = a prompt compiler (library/linker/live-jacks). The wanted pattern for campaign-context assembly. ST's on/off-only manifest can't do mutual-exclusion/deps → it hacks with convention-as-UI; our custom toolchain should solve cardinality natively. |
| [[0101-swappable-cot-modules]] | pattern | new (ST presets) | CoT as a hot-swappable fragment, per-model/per-genre (MAX+ ships 5 variants + a Claude/Gemini one). Shape: `<think>` bullets-only, 7-task numbered checklist, leak-gate. Echoes 0097 checklist-discipline — but self-checks need an *external* referent (banned list / state file) or they self-confirm. |
| [[0102-catalogue-metadata-shape]] | idea | conversation | Cataloguing shape for KB entries: validated mandatory core + additive periphery. Reframe — "wrong schema" is cheap (additive), only *unstamped capture-time facts* are fatal; a session/provenance anchor makes the rest backfillable. Validation implies a registry → phase it in. template-version is the keystone. |
| [[0103-bitemporal-subentry-versioning]] | idea | conversation | Item = stable identity; subentries = versioned, provenanced fact-slices. Bitemporal (transaction vs valid time) + SCD-2. Free changelog + time-travel queries; distinguish in-world change vs retcon. Provenance lives per-version. Branch axis = open thread. |
| [[0065-oneshots-as-spawning-pool]] | pattern | solorpg/claude-desktop | Oneshots mostly fizzle but graduate 3 ways (→campaign, →branch, →canon arc); need cheap home, graduation paths, dignified fizzle. |
| [[0064-unharvested-archive]] | question | solorpg/claude-desktop | ~58 exports in repo vs ~500 RP sessions in Desktop; substrate mostly missing — bulk dump-and-triage is an agent-scale job. |
| [[0063-portable-bundles-constraint]] | pattern | solorpg | Away-from-repo play (phone/Desktop/web) is first-class: the bundle is the whole world → compiler needs thin (at-home/JIT) and fat (away/self-contained) target profiles. |
| [[0062-conversation-transcripts-as-gm-context]] | pattern | solorpg | Verbatim dialogue as GM context — "keeps the story from mutating." Third independent reinvention of verbatim capture. |
| [[0061-continuity-artifacts-under-suspicion]] | question | solorpg | Summaries (format doubt stands) and savefiles (amended: format fairly mature — tune capture guidelines + maintenance; savefile-as-page is a growth play). |
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
| [[0008-form-is-the-lesson]] | pattern | sillytavern | **adopt.** An example teaches its method, not subject; plainness can only be keyed by plain text. Craft laws for valid sample-book cells. |
| [[0007-harvest-vs-workshop]] | pattern | sillytavern | **adopt** (`proven` — already loadbearing in post-processing). Grow easy cells from clipped play, hand-seed hard ones (bootstrapping deadlock); findability/retrieval before generation. |
| [[0006-sample-book-grid]] | idea | sillytavern | **adopt.** A (scene-type × register) grid of worked voice exemplars; precompiled or JIT. The category-1 (tacit/exemplar) store. |
| [[0005-exemplars-over-instructions]] | pattern | sillytavern | **adopt.** Register is tacit; steer voice by demonstration, not specification — "like this" > rules. Works for Opus too (pattern-match, don't interpret). Ratio = per-register dial, no fixed target. |
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
| [[census-solorpg-data-types]] | note 0083 | Full data-type inventory of the solorpg vault (~50 types, formats, breadth, variance). Reference for KB-structure design. |
| [[census-rpg-tools]] | note 0084 | Full tool/schema inventory of rpg-tools (reads/writes, discovery paths, documented formats, skew). Reference for KB-structure design. |
| [[census-namesets]] | note 0119 | **Pass-two full nameset inventory** (193 namesets via `namegen.py list`) + **trust/provenance column** (owner walk). Headline: `(root)` holds 30 core + 58 campaign sets (namespace discipline never adopted). Trust: core defaults 🟢 (owner's most-used, the quality bar); lumina SE-Asia 🟢 (the one clean harvest); longwatch 🔴 "a mess"; aegis 1940s 🔴 unaudited; emberfall ⛔ setting-bound (corrects the catalog's "generic species" inference). Git provenance is blind to subagent authorship. |
| [[session-postprocess]] (+ [[session-postprocess-SKILL]]) | notes 0033–0035 (+0028/0030/0032) | The flagship live workflow. Headline lesson: outgrown scaffold / knowledge-composition bottleneck. |
| [[import-design-brief]] (+ [[export-structure-map]]) | notes 0108–0112 (+ folds into 0001/0102/0103) | **Roadmap candidate.** User's own framework-agnostic pre-planning for the export→import pipeline (consumer of the coming refactor). Multi-label routing, k-NN, two-spine survey, provenance graph, design-now-build-later. Companion map = empirical census of the 2-yr Desktop export (1,201 convos), grounding 0064. |

## Sources (preserved raw — `docs/sources/`)

Raw mined material kept verbatim as primary citations (non-destructive mining). Distinct
from design-notes: these are *data/config*, not prose.

| Source | Mined into | One-line |
|--------|------------|----------|
| `Freaky Frankenstein 4 BOLT+ Updated.json`, `...MAX+ Updated.json` | notes [[0100-fragment-library-prompt-assembly]], [[0101-swappable-cot-modules]] (+ [[0099-pseudocode-as-encoding]]) | Community SillyTavern Chat-Completion presets. Mined for *structure* (not the ERP payload): fragment-pool + enable-manifest + data-hole composition; pseudocode-DSL prompt encoding; swappable per-model CoT modules. |
| `Claude-export-custom-lora.jsonl` (orig. `Claude_export_Custom LoRA for local RPG campaign model_9a9538e1-ee2c-473a-b91d-ce9016a99b2c.jsonl`) | notes [[0113-distill-dont-imitate]], [[0114-voice-vs-setting-fidelity]], [[0115-lora-idiom-lorebook-facts]], [[0116-lora-earns-its-keep]], [[0117-distill-vs-verbatim-tension]] | Inbox conversation (other-assistant) on building a per-campaign style LoRA for a tiny local model. Mined for the *design ideas* (distill-toward-spec data move; voice-vs-default error split; idiom-vs-facts substrate cut; earns-its-keep gate), not the LoRA tutorial — treat its hardware/dataset-size claims as the other assistant's assertions, not enshrined fact. |

## Themes (synthesis)

Themes start life as `theme/*` tags on notes. When a tag earns enough mass, it
graduates into a synthesis doc in `docs/themes/`.

| Theme doc | Synthesizes | Thesis |
|-----------|-------------|--------|
| [[modular-self-evolving-architecture]] | 0034·0036·0024·0037·0038·0039·0040·0041·0042·0043 (+0010·0033·0026) | One home per concern; refer back & compose, don't fork; evolve by graduating campaign experiments into a versioned spec. |
| [[knowledge-base-canonical-vault]] | 0067·0068·0069·0072·0073·0075·0076·0077·0082 (+0070·0071) | Every fact has one home: canonical linked vault; everything else is a rendered view; writes are operated mutations via librarians; truth defended structurally (provenance, precedence, write-time validation). |
| [[voice-and-register]] | 0005–0008·0053–0055·0062·0092·0099·0113–0118 | Voice is *tacit* → demonstrate, never specify → harvest & preserve exemplars verbatim. Sample Book grid (scene-type × register, alive as texture banks); copy ≠ summarize; rewrite only in the curated layer with an anchor; characters first; fine-tune is a sidequest. **Appraised 2026-06-15 — adopt** (spine ratified; components keep their own verdicts: 0099 adopt-scoped-to-reading-1, 0113/0114/0117 adapt). |
