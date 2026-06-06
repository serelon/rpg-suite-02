---
tags:
  - kind/map
  - maturity/growing
created: 2026-06-06
---

# State of the Research — the whole board

> **What this is.** A synthesis-of-everything map: all 89 notes digested, grouped under the
> four pillars of the vision ("next-gen RPG workflows, backends, and frontend — reimagining
> the whole loop and datastorage") plus a meta bucket. One line per note; tensions and gaps
> surfaced centrally. **This doc does not appraise** — verdicts stay in the notes. It exists
> to answer "what have we got?" and to make "what next?" mechanical.
>
> Pillars are an *overlay* for orientation; tags remain the source of truth. Many notes
> belong to several pillars — each is listed where it carries the most weight.

## Census (2026-06-06)

| | |
|---|---|
| Notes | 91 (+ template) |
| Appraised | 25 — 21 adopt, 2 adapt (0049, 0077), 2 undecided (0038, 0072), 0 reject |
| Unevaluated | 66 |
| Theme docs graduated | 2 — [[modular-self-evolving-architecture]], [[knowledge-base-canonical-vault]] |
| Inbox | 1 item |

**Appraisal lens going forward (agreed 2026-06-06):** we are auditing our own previous
gen, not gatekeeping a stranger's patterns. The question is not "adopt/reject?" but
**"what's the next-gen delta?"** — *carry as-is / carry with this evolution / superseded
by [x]*. Zero rejects is the expected outcome, and the deltas are design input.

---

## Pillar 1 — Data storage & the Knowledge Base

*The most mature pillar. Largely synthesized already in [[knowledge-base-canonical-vault]]
(canonical vault, lenses, librarians, defended truth — **adopt**, ratified) and half of
[[modular-self-evolving-architecture]]. Headline standing item from that appraisal: "KB
structure needs a lot of thinking — data types, formats, templates."*

### Synthesized (in the KB theme doc)
0067 linked vault is canon, JSONs build from it · 0068 multi-lens / two trunks (play vs
design) · 0069 one KB, many presentation layers; layered retrieval exact→graph→vector ·
0070 threads tracker — the artifact that *earned* trust (slugs, auto-reverse links, state
machine) · 0071 fog-of-war as observed/actual data · 0072 silent schema drift (undecided;
cause unknown) · 0073 structured mutation beats rewrite (**hard rule, adopted**) · 0075
post-processing as vault librarian (+custodian, propose-never-commit) · 0076
self-canonizing hallucinations → provenance + check-the-layer-below · 0077 placement
metadata in data, cache scheduling in consumers · 0082 live hook pipeline (streamed
librarianship; widget lane exempt from gates).

### The type system (the named standing work item, largely post-dates the theme doc)
- 0083 — data-type census: ~50 types; shape variance tracks tool-backing exactly; skills are de-facto schema authorities.
- 0085 — **the first type cut, by substrate** (sharpened 2026-06-06): knowledge entries = vault pages on ONE base template regardless of complexity (memories, characters, savefiles, maybe spreadsheets); tool data = raw JSON outside the tree; images/raw assets = third substrate. Flags extensible per module, always documented. The spine of the KB type system.
- 0090 — **cherrypick contract (T7 resolved: go)**: three layers per page — frontmatter edges/scalars, json blocks for nested data, sections for prose; working PoC in `experiments/cherrypick/`.
- 0091 — **isolation decided**: one vault, campaign-folder entrypoints, tool-enforced boundaries.
- 0084 — rpg-tools data layer is a proto-KB: steal primitives (tiered loading as schema, namespace+inheritance, link validation, calendars), not plumbing.
- 0088 — player-display artifacts: third audience (model / author / player); redundant by construction, never model-read.
- 0089 — sealed secrets: hidden-from-GM quadrant; trigger-gated unseal.
- 0020/0021/0022 (aegis) — observed/actual split; DataRequired halts-and-prompts instead of fabricating; reference vs state, types-as-data.
- 0059/0086/0050 — the decay spectrum: built-never-used (campaign.py, faction economy) → barely-used (locations) → superseded-surviving (stories) → load-bearing (characters, memories, savefiles). New failure mode named: **illegibility as decay accelerant** (0086); a type without play-loop wiring decays to inert JSON (0059).
- 0087 — spreadsheet semantics as the tool-data shape for "crunch matters" state: CSV canonical, recalc-as-code, HTML render.
- 0061 — savefiles/summaries (amended 2026-06-06): savefile *format* fairly mature — the tuning target is capture guidelines + maintenance; savefile-as-page is a growth play (history/changelog sections). Summary-format doubt stands.
- 0062/0064 — transcripts are knowledge entries the system is blind to; ~500 Desktop sessions unharvested (raw substrate coverage ~10%).
- 0002 — read-anywhere/write-canonical (proven, but see Tension T1).
- 0003 — scope everything or soup; 0029 — information boundaries are declared-nowhere, enforced-by-luck (unmet need); 0030 — summary as compression ("will this matter in 10 sessions?").

### What this pillar still owes
The KB theme doc's soft list stands: cherrypick contract, campaign isolation design,
provenance granularity, migration path, custodian shape. Plus, newer: does 0085's two-kind
cut hold against all ~50 census types? What happens to the savefile (0073 asks: survive, or
dissolve into threads-like structured state + memories)?

---

## Pillar 2 — The play loop (workflows in session)

*Rich but unsynthesized — this is where the biggest ungraduated clusters live.*

### Doctrine
- 0080 — **engineer & gardener** (load-bearing): engineer seeds OOC → gardener grows IC → librarian harvests. Seed-failure taxonomy: overengineered / too-small / signal-drowned. The OOC/IC boundary is a context-policy boundary.
- 0089 (refined into 0080) — goalposting (minimal waypoints, open between) is legitimate; beat-by-beat scripting is the nono. Failure criterion: stifled GM imagination.
- 0078/0079 — zoom-out-first worldbuilding; relational anchoring is the mechanism of container-world failure; context-*exclusion* is the instrument.

### Voice & register (cluster ripe for graduation — 0005–0008, 0012, 0053, 0055)
Exemplars over instructions (0005) · form is the lesson + craft laws (0008) · sample-book
grid, scene-type × register (0006) · harvest vs workshop fill paths, findability first
(0007) · intelligence into the scaffolding; the blankets bug; per-model calibration (0012)
· voice samples are the keystone anchor — description alone empirically failed (0053) ·
texture banks & living dictionary already work in production (0055).

### Craft-skill authoring (cluster ripe for graduation — 0013–0017, 0066)
Counter-training: name the default, correct, explain why (0013) · scope-stripping failure
family (0014) · compounding loops failure family (0015) · thinking block as enforcement
surface (0016) · recap as verification, not "previously on" (0017) · **mandatory presence,
not length** — attention is the scarce resource (0066).

### Context delivery in play
- 0009/0010/0011 — JIT + eviction at beat boundaries; docs-as-code context compiling; identity pinned, state evicted.
- 0001 — tiered/progressive loading (proven everywhere).
- 0048 — canon precedence; naming is permission; 0052 — evolution vs drift, gates are canon defense.
- 0060 — JIT retry: infodump-by-default was a model-era workaround; 4.7/4.8 agentic models may make JIT viable (testbed candidate).
- 0051 — live context delta: mid-session patches as diffs, never reloads.
- 0054 — verbatim capture, lost intent: the pipeline drifted from its own spec (rewrite instead of copy).

### What this pillar still owes
No end-to-end picture of *a next-gen session* exists — prep → play → harvest as one
walkthrough. Voice/register and craft-skill clusters each have enough notes to graduate.
Scene-boundary detection is flagged "genuinely unsolved" (0075) and three threads depend on
it (streamed librarian, cache flush points, eviction boundaries).

---

## Pillar 3 — Backends (composition, modules, spec)

*Synthesized in [[modular-self-evolving-architecture]]: everything is a module (0036),
pluggable up to a whole rules engine (0024), versioned self-evolving spec (0041), async
fleet migration (0042), campaigns as testbeds with graduation (0043), scenario compiler as
the refer-back mechanism (0044) — all **adopt**.*

### Around the synthesis
- 0044/0045/0056/0057/0058 — the compiler stack: universal build process; runtime composition (briefing.py with inline tool calls); compilation drops to file granularity; **compiled context demands audit tooling / build manifests**; flag lifecycle (tag at build, select at prep — "we need to be much smarter about flags").
- 0039 — bundle templates: the proven prototype linker (inheritance, multi-chain merge, reference-following). User caveat: "wonky-ish — audit before building on it."
- 0047 — campaign/branch/subsetting as composable axes, not a fixed tree.
- 0018 — layered separation: craft skill ⟂ mechanics module ⟂ tools ⟂ bundle data — the layering doctrine that 0024 promotes to a hard requirement and 0036 operationalizes.
- 0023 — event-bus orchestrator (aegis): thin core, self-registering modules, time as events — the concrete plug-in seam.
- 0037/0038 — rpg-tools modularization; the unresolved shared-`lib/` question (foundation module / vendored / platform-owned) — **undecided**.
- 0033/0034 — lean-spine workflows deferring to canonical guides; the scaffold is outgrown — knowledge composition needs a registry/resolver, not hand-wired paths.
- 0026/0027 — exceptions are features; nine recurring exception classes across 19 campaigns → exception-profiles parameterize the workflow.
- 0031/0032/0025 — the transient-constraint lens: quarantine capability workarounds (chunking, the dead Lead+Lorekeeper split) from durable architecture (token hygiene, separation of concerns).
- 0046/0049 — campaign lifecycle is geological strata, one concern with many doors; lifespan-tiered primers (adapt: expiry as condition, not date).
- 0065 — oneshots as spawning pool: incubation tier with three graduation paths; the minimal compile target; data model currently ignores them.
- 0040 — vector-DB reframed as the lore-search *module* — centralization as a module's internal implementation.

### What this pillar still owes
The module contract (what a module exposes; how versions bind) is still abstract. The
compiler's build path (evolve bundle.py vs greenfield) is deliberately undecided pending a
bundle.py audit. Nothing yet on *where things run* — what executes hooks, where the
librarian lives, model routing/cost beyond 0081's sketch. "Backend" as runtime is nearly
unmined; what exists is backend as *architecture*.

---

## Pillar 4 — Frontend (thin — flagged as a gap)

*The user named frontend as a pillar of the vision; the vault has ~6 notes that touch it
and no cluster. This is the largest coverage gap.*

- 0004 — frontend-agnostic core (north-star constraint): one brain, playable from Desktop, Code, SillyTavern, reverse-mcp, Unicorn.
- 0074 — **Project Unicorn**: the endgame RP client; deliberately unscoped; disciplines the architecture now ("every layer stands alone, Unicorn is capstone never dependency").
- 0081 — writer/planner split: local RP-finetune writes prose, Opus plans/guards canon — two attentions solve attention starvation.
- 0063 — portable bundles: away-from-repo play is first-class → fat self-contained builds vs thin at-home manifests; capability-class per frontend.
- 0088 — player-display artifacts / widget panes (grows under Unicorn's UI).
- 0057 — audit GUI (reverse-mcp-rpg as existence proof).

### What this pillar still owes
Almost everything: session management, transport (is MCP the binding layer?), what
SillyTavern's context-engineering actually does mechanically (named as a primary influence,
mined only conceptually), UI shape of Unicorn, how a non-executing frontend degrades
(static fallbacks). reverse-mcp-rpg itself is unmined as a source.

---

## Meta — how we work (not what we build)

- 0028/0035 — checkpointed human gates ("agents propose, gates dispose"); surgical git staging, branch-per-run.
- 0019 — companion rationale docs as anti-regression.
- 0043 + appraisal protocol — graduation gates for experiments and notes alike.
- This vault's own conventions (tags as truth, verdict gate, mine→report→appraise→commit) are themselves a prototype of the spec discipline 0041 wants.

---

## Cross-cutting tensions (the contradictions worth resolving on purpose)

- **T1 — read-anywhere vs single-source-of-truth.** 0002's multi-path merge discovery (proven, portable) sits uneasily with 0036/0067's "one canonical home, consumers refer back." Likely resolution: discovery becomes a platform guarantee (0038's third option) *pointing at* the canonical home — but nobody has written that down.
- **T2 — retroactive extraction vs away-play.** 0062 says verbatim needs no prediction (raw chunks persist, extract on demand); 0063 says away-bundles must pre-bake everything (prediction is back); 0064 says for ~90% of historical play the raw substrate isn't even in the repo. Two delivery modes with different selection problems — the compiler must serve both.
- **T3 — validate loudly vs tolerate silently.** 0070/0071 prove validation-at-write keeps data clean; 0072 shows silent tolerance hid drift for the system's whole life — but 0072's *cause* is unknown and the hand-edited schema was arguably *better* (evolution the tools never absorbed). Stance pending the aegis git-history dig.
- **T4 — gates vs streaming.** 0028's draft-review-adjust-write gate model is proven canon defense; 0075/0082's streamed librarian wants a flow of small live mutations. "What review for a stream?" is open; the widget-lane exemption (ephemeral ≠ canon) is the one settled piece.
- **T5 — enforcement cost vs context economy.** 0013/0016's explained-counter-training and thinking-block enforcement are token-expensive every turn; 0066 reframes (attention, not length, is scarce; mandatory presence). 0081's two-attention split is one structural answer. No synthesis yet.
- **T6 — transient or durable?** 0031's lens has confirmed kills (Lead+Lorekeeper, chunking, campaign.py) and live suspects: infodump-by-default (0060 wants the JIT retry), cache-economics scheduling (0077 — provider-variable, pushed consumer-side), writer/planner split (model-era economics?). Each design element owes a core-or-shell tag.
- **T7 — markdown vault vs real database. RESOLVED 2026-06-06: go.** The cherrypick PoC ([[0090-cherrypick-contract-three-layers]], `experiments/cherrypick/`) demonstrated targeted sub-data extraction from fully Obsidian-compliant pages. Binding constraint shifts to template discipline (stable keys + controlled section vocabulary per page-type).

## Coverage gaps (vision says it; vault barely does)

1. **Frontend** — see Pillar 4. ~6 notes, no cluster, biggest gap vs the named vision.
2. **Backend as runtime** — where code executes, hook orchestration, model routing, cost. Architecture is rich; operations are absent.
3. **Campaign isolation** — ~~no design note owns it~~ structural decision made 2026-06-06 ([[0091-one-vault-campaign-folder-entrypoints]]): one vault, campaign-folder entrypoints, tool-enforced boundaries. Remaining gap: the enforcement tool's design.
4. **Migration** — 0042 gives the *policy* (async, declared versions); nothing on the actual path from today's 19 live campaigns.
5. **An end-to-end session walkthrough** — no artifact shows the reimagined loop as one story: workshop → compile → play → harvest → vault.

## Standing mining leads (named in notes, never executed)

E:\rpg entity-registry & disambiguation (0040) · deeper rpg-tools structural mine — bundling/build/cross-tool wiring (0037) · aegis data git-history, cause of 0072 · hallucinated-tag corpus study before designing the flag vocabulary (0059/0058) · Desktop archive bulk dump & triage, ~500 sessions (0064) · bundle.py audit before the compiler decision (0039/0044) · early-campaign memories before/after for 0054's style-drift proof · factions.py economy usage check (0084) · reverse-mcp-rpg as a source repo · SillyTavern mechanics (lorebook assembly, long-context handling) as a source.

## Ripe to graduate (theme-doc candidates, in rough order of readiness)

1. **Voice & register** (0005–0008, 0012, 0053, 0055 + sample-book) — coherent, partially production-proven, self-contained.
2. **Craft-skill authoring** (0013–0017, 0066) — proven in gm-skill, clean failure taxonomies.
3. **The compiler / composition stack** (0010, 0039, 0044, 0045, 0051, 0056–0058, 0063) — blocked partly on the bundle.py audit.
4. **The play-loop doctrine** (0080, 0078/0079, 0089, 0048/0052, 0060) — newest, still settling.
