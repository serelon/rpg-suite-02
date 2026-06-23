---
tags:
  - kind/map
  - maturity/growing
created: 2026-06-06
---

# State of the Research — the whole board

> **What this is.** A synthesis-of-everything map: all notes digested, grouped under the
> pillars of the vision ("next-gen RPG workflows, backends, and frontend — reimagining
> the whole loop and datastorage") plus a meta bucket. One line per note; tensions and gaps
> surfaced centrally. **This doc does not appraise** — verdicts stay in the notes. It exists
> to answer "what have we got?" and to make "what next?" mechanical.
>
> Pillars are an *overlay* for orientation; tags remain the source of truth. Many notes
> belong to several pillars — each is listed where it carries the most weight.
>
> **Frame update (2026-06-20):** grown from four pillars to **six**. The 0092–0123 fold-in
> surfaced two axes the original four couldn't house: **P5 Progression / rules-engine** (the
> "system as code" axis `aegis-tools` embodies) and **P6 Model layer / fine-tuning** (a
> deliberately sidequest-quarantined bucket). A third, **encoding/representation**, is a
> cross-cutting spine folded into P1, not a pillar.

## Census (2026-06-20)

| | |
|---|---|
| Notes | 123 (0001–0123; + template) |
| Appraised | ~35 — bulk **adopt**, adapt: 0049/0077/0113/0114/0117/0122, undecided: 0038/0072/0115, 0 reject |
| Unevaluated | ~88 — incl. most of the corpus-routing (0108–0111), catalogue (0102–0103), SSOT (0093/0094/0098), progression (0104–0107) clusters |
| Theme docs graduated | 2 — [[modular-self-evolving-architecture]], [[knowledge-base-canonical-vault]] |
| Pillars | 6 (+ Meta) — P5/P6 added 2026-06-20 |
| Inbox | being mined down |

> **Counts are approximate** — the 0092–0123 fold-in (2026-06-20) digested 32 notes into the
> pillars below and added P5/P6; an exact verdict tally hasn't been recomputed. Notes 0001–0091
> retain their 2026-06-06 digest; spot-check before quoting a number as fact.

**Appraisal lens going forward (agreed 2026-06-06):** we are auditing our own previous
gen, not gatekeeping a stranger's patterns. The question is not "adopt/reject?" but
**"what's the next-gen delta?"** — *carry as-is / carry with this evolution / superseded
by [x]*. Zero rejects is the expected outcome, and the deltas are design input.

---

## The loop as spine (2026-06-23)

The pillars are a *what-have-we-got* overlay; **the grand loop**
([[0124-the-grand-loop]]) is the *what-does-it-all-add-up-to* overlay. They cross-reference:
every pillar hangs off one or more **stages** of the loop, so "which pillar to advance" and
"which stage to design" become the same question.

```
 claude.ai dump ─► [bulk ingest] ─► sessions ─► import ─► [postprocess] ─► 〈campaign vault〉
   workshop ─┬─► bootstrap ─► session-prep ─► bundle ─► play ─► export ──┘
             ├─► reference ─► 〈vault〉            〈vault〉 ─► [archive old data] ─► 〈cold storage〉
             └─► scratch / quarantine
```

| Loop stage | Owner pillar(s) | Anchors |
|---|---|---|
| bulk ingest / corpus-routing | **P1** (import cluster) | 0108–0112, [[import-design-brief]] |
| per-session import (chunk) | **P1** | 0032, 0094 |
| **`[postprocess]`** ⬛ *black box* | **P1** librarian · **P2** summaries · **P5** record updates | 0075, 0122, 0106 |
| **`〈campaign vault〉`** ⬛ *black box* | **P1** — the whole pillar *is* the vault | 0093/4/8, 0085, 0102/3, [[knowledge-base-canonical-vault]] |
| session-prep | **P3** compose · **P1** selective read | 0039, 0100 |
| bundle | **P3** · **P4** (portable) | 0044/0056, 0063 |
| play | **P2** loop · **P5** progression · **P6** writer · **P4** surface | 0080, 0104, 0081 |
| export | **P2 / P3** | [[export-structure-map]] |
| workshop inlet | **P2** engineer/gardener · **Meta** | 0080 (seeds); reference→vault = P1; scratch = quarantine |
| archive / drain | **P1** lifecycle | 0046 |
| branch (*selector, not a stage*) | **P3** composable axes | 0047, 0123 |

**What the mapping reveals** (the reason to keep this overlay):

1. **P1 owns the entire bottom arc** — import → postprocess → vault → drain (four stages), and
   *both black boxes are P1*. The next design drill-down (postprocess internals or vault
   internals) is unambiguously a **Pillar-1 dive**, established structurally, not by gut.
2. **P3 and `branch` are the same kind of thing** — neither is a *stage*; both are *how stages
   compose/run*. P3 is connective tissue threaded through session-prep/bundle/export; branch is a
   selector over reads. The flow is the loop; composition is orthogonal to it. (Generalizes 0123's
   "branch isn't narrative structure": *composition isn't flow* either.)
3. **P4 maps to a single, thin stage (`play`)** — which makes the long-flagged frontend gap
   *spatial*: one box with almost nothing behind it.

This is the seed of the roadmap spine (step 1): sequence work by walking the loop, with P1's
bottom-arc as the natural first object of design.

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

### Single-source-of-truth: canonical raw vs derived renders (cluster, ripe — folded in 2026-06-20)
The densest new cluster; `theme/single-source-of-truth` is now one of the most populated themes.
One spine: **the raw layer is permanent, everything else is a regenerable render.**
- 0094 — **save-everything, deferred compute** (the rationale): hoard raw session data losslessly;
  derived artifacts are disposable renders, re-render when models improve. (Tension with 0032
  preprocessing: preprocessing must *fork*, never replace the raw export.)
- 0093 — **novelization as output**: render a campaign as one seam-free novel; a presentation
  layer over the canonical record, pipelined chapter-by-chapter. (Also a P2 postprocessing artifact.)
- 0098 — **vector index over the vault, not the store**: the vector DB is a derived, rebuildable
  index *over* the `.md` vault; vault stays SSOT; sealed/isolation as hard filters. **Inverts
  0040** (see Tension T8).
- Joins existing 0056 files-as-build-products, 0069 one-KB-many-layers, 0002 write-canonical, 0040.

### Catalogue & versioning shape (cluster — folded in 2026-06-20, corroborated by import-design-brief)
- 0102 — **catalogue metadata shape**: small mandatory core + additive periphery; the only
  irreversible birth decision is which lossy capture-time slots exist; provenance anchor makes
  the rest backfillable.
- 0103 — **bitemporal subentry versioning**: a KB item = stable identity holding versioned,
  provenanced subentries on two time axes (transaction vs valid); one mechanism yields
  history/audit/retcon/time-travel. (Now also the backbone of 0121's narrative axes.)

### Corpus-routing / import (cluster, RIPE — folded in 2026-06-20; one source: solorpg IMPORT-DESIGN-BRIEF)
A tight five-note spine for the export→import pipeline (Roadmap candidate, below).
- 0108 — **multi-label relational routing**: route material as a set of *typed edges*
  (belongs-to/crossover/seed-of/variant-of), each with confidence + decision-provenance; one
  folder is lossy by construction.
- 0109 — **k-NN, not centroids**: classify orphans by k-NN majority over labeled points;
  contested top-2 neighbours *is* the crossover detector (campaigns drift, centroids lie).
- 0110 — **wilderness survey**: two spines on one embed pass — supervised routing + unsupervised
  survey of the remainder; the survey (recovering lost seeds) is the higher-value, *standing* half.
- 0111 — **provenance graph as secret history**: the routing edges reconstruct how settings
  actually evolved — lineage as a first-class artifact, not routing residue.
- (0112 — the "design now, wait for the refactor" posture — filed under Meta.)

### Encoding / representation (cross-cutting spine — NOT a pillar; folded in 2026-06-20)
How to encode meaning per data-type; governs substrate choice across P1/P3/P5.
- 0118 — **encoding-by-data-type** (adopt, maturity/growing — the headline): three encodings by
  tacitness — tacit→exemplar (prose), explicit→structured records, relational→pseudocode; the old
  system over-leaned on prose and drifted.
- 0099 — **pseudocode as encoding** (adopt, scoped): structural/relational lore as pseudocode for
  legibility+audit; control-flow on *procedure*, never narrative; voice stays prose.
- 0107 — **prose-deprecation doctrine**: deprecate prose by default; keep it only where it *is*
  the payload (voice/texture). The payload/carrier split. (Tension with 0094's hoard-raw-prose.)

### Voice-as-corpus & namesets (folded in 2026-06-20 — the non-training halves of the LoRA cluster)
- 0113 — **distill, don't imitate** (adapt): a strong model rewrites scenes toward a canonical-voice
  spec anchored on best scenes — consistency by construction, *no training required*.
- 0114 — **voice vs setting-fidelity** (adapt): two error classes, two fixes — voice (taught by
  demonstration) vs idiom/"sails on a starship" default-association; discover registers by clustering.
- 0117 — **distill-vs-verbatim tension** (adapt): the layer's *contract* decides — rewrite into
  curated renders, copy-only into the verbatim source, never up the canon chain; safe only with an anchor.
- 0119/0120 — **namesets by demand**: grow the core nameset library by demand not harvest (0119);
  the "Marcus Chen" default-pull is **domain-general** — generators are first-class namesets (0120).
  Join 0013 counter-default, 0087 spreadsheet-semantics, census-namesets.

### What this pillar still owes
The KB theme doc's soft list stands: cherrypick contract, campaign isolation design,
provenance granularity, migration path, custodian shape. Plus, newer: does 0085's two-kind
cut hold against all ~50 census types? What happens to the savefile (0073 asks: survive, or
dissolve into threads-like structured state + memories)? And the new fold-in adds: resolve the
**0040↔0098 ownership inversion** (T8); decide the **encoding floor** (0107 — where over-structuring
starts killing what LLMs are good at); appraise the corpus-routing and catalogue clusters (all unevaluated).

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
texture banks & living dictionary already work in production (0055) · **weave player input**
into the GM's own prose — echo-then-append is the counter-trained failure; fidelity hierarchy
intent>voice>inner-life (0092, proven, **adopt**).

### Craft-skill authoring (cluster ripe for graduation — 0013–0017, 0066)
Counter-training: name the default, correct, explain why (0013) · scope-stripping failure
family (0014) · compounding loops failure family (0015) · thinking block as enforcement
surface (0016) · recap as verification, not "previously on" (0017) · **mandatory presence,
not length** — attention is the scarce resource (0066) · **interleaved checklist thinking** —
per-paragraph think-block (pacing/stop/fact-check); modern Opuses collapse the walk so it needs
forced structure, and a self-fed fact-check self-canonizes unless given an external referent (0097).

### Context delivery in play
- 0009/0010/0011 — JIT + eviction at beat boundaries; docs-as-code context compiling; identity pinned, state evicted.
- 0001 — tiered/progressive loading (proven everywhere).
- 0048 — canon precedence; naming is permission; 0052 — evolution vs drift, gates are canon defense.
- 0060 — JIT retry: infodump-by-default was a model-era workaround; 4.7/4.8 agentic models may make JIT viable (testbed candidate).
- 0051 — live context delta: mid-session patches as diffs, never reloads.
- 0054 — verbatim capture, lost intent: the pipeline drifted from its own spec (rewrite instead of copy).

### Narrative structure — the units & axes of play (new cluster, 2026-06-20)
The first notes to name the *temporal/narrative units themselves* (all prior ~120 are
data/context/tooling). Cross-cuts Pillars 1 and 2.
- 0121 — **the granularity ladder** (**adopt**, owner-ratified *foundation*, maturity/proven):
  `update < scene < act? < session < arc? < season < campaign` (session = the numbered,
  load-bearing unit, fka *episode*). It *isn't a tree*: a session sorts on two **time-axes**
  (telling-order = session #, the monotonic spine; story-time = timeline, jumps when non-linear
  → bitemporal, cf. 0103) plus a separate **organizational** cross-cut (branch, below). Three
  axes are **capacity, not mandatory population** — linear/single-branch is the cheap default;
  the model just must not *preclude* complexity (guards the 0031 / `E:\rpg` over-build trap).
- 0123 — **branch is the organizational POV axis** (**adopt**, proven in solorpg). A branch is a
  parallel protagonist *workspace* in one shared world+timeline (Long Watch: Val/Lyra/Rosa/…),
  **not** a canon fork; owns the folder/savefiles/bundle-template; nests for *shared-state*
  reasons (Leviathan parent = fleet-save container). **Hard rule: organization (branch) ≠
  narrative structure (arc); track separately** — conflating breaks things. This is the branch
  half of 0047's "campaign/branch/subsetting as composable axes" (Pillar 3), now with the
  separate-from-narrative constraint made explicit.
- 0122 — **the compaction boundary is descending** (**adapt**). Season was a *coupled*
  context-window/narrative constraint (summaries accreted → forced compaction = season break,
  which *pushed* the story toward a finale). Compaction granularity → a finer **tunable** is a
  next-gen commitment (cf. 0009/0051/0094); season-the-unit is **on probation** (legacy-only
  since the current system) — kept optional, settled neither way. A clean 0031 instance.

### What this pillar still owes
No end-to-end picture of *a next-gen session* exists — prep → play → harvest as one
walkthrough. Voice/register and craft-skill clusters each have enough notes to graduate.
Scene-boundary detection is flagged "genuinely unsolved" (0075) and three threads depend on
it (streamed librarian, cache flush points, eviction boundaries) — and it now also blocks
0122's per-scene/per-arc compaction tunability and 0121's scene/act boundary recognition.

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

#### Folded in 2026-06-20
- 0100 — **fragment-library prompt assembly** (proven): prompt = decoupled fragment pool + ordered enable-manifest + marker/data-hole slots; a custom framework should add cardinality/dependency/conflict natively (SillyTavern does on/off only). The compiler's fragment model.
- 0101 — **swappable CoT modules** (proven): CoT is a hot-swappable fragment selected per (campaign × model × genre); checklist-discipline is the keeper but every check needs an external referent or it's theater. (Pairs with 0097, P2.)
- 0095 — **two-repo public/private split** (seed): next-gen = public core repo + private campaigns repo nested in `campaigns/`; the nested-repo boundary is *simultaneously* campaign-isolation and public/private; core never wikilinks into campaign data.
- 0096 — **enforcement matches reversibility** (principle, seed): match enforcement strength to failure reversibility — discipline → tool-enforced → mechanically-gated → structurally-impossible; climb the ladder as reversibility drops (campaign bleed = soft; public leak = structural). Written to reconcile 0095 with 0091.

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
- 0112 — **design now, build into the frame** (folded in 2026-06-20): when a needed thing is really a data-model decision (semantic index, provenance graph, UUID merge), capture the design and *wait for the refactor*; the test is "native capability vs bolt-on script." The discipline that keeps the corpus-routing cluster (0108–0111) parked instead of hacked in now.
- This vault's own conventions (tags as truth, verdict gate, mine→report→appraise→commit) are themselves a prototype of the spec discipline 0041 wants.

---

## Pillar 5 — Progression / rules-engine (the "system as code" axis)

*New pillar, stood up 2026-06-20. The axis CLAUDE.md names as a core tension: `aegis-tools`
embodies enforced rules-as-code; `rpg-tools`/`solorpg` deliberately avoid it. The four original
pillars had no home for it. Already gestured at from P3 (0024 pluggable-up-to-a-rules-engine,
0023 event-bus, 0020–0022 aegis data) — this pillar is where the **progression/mechanics content**
lives, distinct from P3's plumbing for *how* modules plug in.*

- 0104 — **progression as a pluggable layer** (seed): progression isn't a sequence of systems but
  one **dial** — off (freeform) → light kit → heavy (Aegis); next-gen owns the *axis*, not one point.
- 0105 — **tarot progression, a unifying failure** (proven): Tarot's four gears all died of one
  flaw — under-specified symbolic markers with no semantic layer decayed into prose flavor; plus
  token cost (⭐-strings) and rewrite-only updates. The negative case that defines the requirement.
- 0106 — **three-layer character record** (seed): mechanical (statblock/JSON) + semantic
  (interpretation contract) + prose (only where prose is payload); the **semantic layer is exactly
  what Tarot fatally lacked**. Bridges to P1's type system (0085) and encoding spine (0118).
- 0107 — **prose-deprecation doctrine** — also listed under P1's encoding spine; it's the doctrine
  that governs which progression data is structured vs prose.

**What this pillar owes:** all four notes are `verdict/unevaluated` — the most architecturally
consequential unjudged cluster. The dial's *interface* (how off/light/heavy bind to the same KB),
and how the semantic layer is actually authored, are open. Appraise before graduating.

---

## Pillar 6 — Model layer / fine-tuning (sidequest, quarantined)

*New pillar, stood up 2026-06-20 — deliberately **thin and out-of-mainline**. Exists mostly to
quarantine model-training as a sidequest: default play stays Opus/Desktop. The corpus/exemplar
techniques that pay off **without** training were evacuated to P1 (0113/0114/0117); only the
genuine "make and use a trained adapter" material lives here.*

- 0116 — **a fine-tune earns its keep** (adopt): only where prompting can't reach — canonically,
  making a small/local model hold a register zero-shot. Explicitly scoped as a *sidequest*; flags
  per-campaign hot-swap adapters as possibly premature (0031/0112).
- 0115 (weights-half) — **LoRA carries idiom, lorebook carries facts** (undecided): weights hold
  voice + setting-idiom; hard facts must stay in the auditable lorebook — *SSoT applied to a trained
  model* (weights are the worst place to store a fact). The facts-half is P1; the weights-half is here.
- Natural pairing: 0081 (writer/planner split — local RP-finetune writes prose, Opus guards canon)
  is the P4/P6 bridge; whether that split is durable or model-era economics is an open T6 question.

**What this pillar owes:** almost everything beyond the scoping decision — it's intentionally
under-built. Revisit only if a concrete register-holding need appears that prompting can't meet.

---

## Cross-cutting tensions (the contradictions worth resolving on purpose)

- **T1 — read-anywhere vs single-source-of-truth.** 0002's multi-path merge discovery (proven, portable) sits uneasily with 0036/0067's "one canonical home, consumers refer back." Likely resolution: discovery becomes a platform guarantee (0038's third option) *pointing at* the canonical home — but nobody has written that down.
- **T2 — retroactive extraction vs away-play.** 0062 says verbatim needs no prediction (raw chunks persist, extract on demand); 0063 says away-bundles must pre-bake everything (prediction is back); 0064 says for ~90% of historical play the raw substrate isn't even in the repo. Two delivery modes with different selection problems — the compiler must serve both.
- **T3 — validate loudly vs tolerate silently.** 0070/0071 prove validation-at-write keeps data clean; 0072 shows silent tolerance hid drift for the system's whole life — but 0072's *cause* is unknown and the hand-edited schema was arguably *better* (evolution the tools never absorbed). Stance pending the aegis git-history dig.
- **T4 — gates vs streaming.** 0028's draft-review-adjust-write gate model is proven canon defense; 0075/0082's streamed librarian wants a flow of small live mutations. "What review for a stream?" is open; the widget-lane exemption (ephemeral ≠ canon) is the one settled piece.
- **T5 — enforcement cost vs context economy.** 0013/0016's explained-counter-training and thinking-block enforcement are token-expensive every turn; 0066 reframes (attention, not length, is scarce; mandatory presence). 0081's two-attention split is one structural answer. No synthesis yet.
- **T6 — transient or durable?** 0031's lens has confirmed kills (Lead+Lorekeeper, chunking, campaign.py) and live suspects: infodump-by-default (0060 wants the JIT retry), cache-economics scheduling (0077 — provider-variable, pushed consumer-side), writer/planner split (model-era economics?). Each design element owes a core-or-shell tag.
- **T7 — markdown vault vs real database. RESOLVED 2026-06-06: go.** The cherrypick PoC ([[0090-cherrypick-contract-three-layers]], `experiments/cherrypick/`) demonstrated targeted sub-data extraction from fully Obsidian-compliant pages. Binding constraint shifts to template discipline (stable keys + controlled section vocabulary per page-type).
- **T8 — who owns the search truth? (new, 2026-06-20).** 0040 (**adopt**) called the vector store "the searchable *source-of-truth*"; 0098 (unevaluated) inverts it — the vault `.md` is SSoT, the index is a rebuildable *view* over it. An adopted note now has a contradicting refinement sitting unjudged. Appraising 0098 must decide whether it amends 0040. (Leaning 0098, per the whole SSoT cluster — but it's a verdict, not a default.)
- **T9 — the encoding floor (new, 2026-06-20).** 0118/0099/0107 push toward structured/pseudocode encoding to stop prose-drift; 0107 itself asks where the floor is — over-structuring kills what LLMs are actually good at (tacit pattern-matching from exemplars, 0005/0008). The payload/carrier split is the proposed rule; the floor is unset.
- **Counter-default needs an external referent, *everywhere* (cross-cluster thread).** 0113's voice-rewrite can launder the strong model's own clichés (0114 "sails on a starship"); 0120's name generators hit the identical default-pull on the non-person axis. Same fix both places: an explicit banned/overused list as external referent (cf. 0076). Ties the voice cluster (P1) to namesets (P1) to 0097's self-canonization problem (P2).

## Coverage gaps (vision says it; vault barely does)

1. **Frontend** — see Pillar 4. ~6 notes, no cluster, biggest gap vs the named vision.
2. **Backend as runtime** — where code executes, hook orchestration, model routing, cost. Architecture is rich; operations are absent.
3. **Campaign isolation** — ~~no design note owns it~~ structural decision made 2026-06-06 ([[0091-one-vault-campaign-folder-entrypoints]]): one vault, campaign-folder entrypoints, tool-enforced boundaries. Remaining gap: the enforcement tool's design.
4. **Migration** — 0042 gives the *policy* (async, declared versions); nothing on the actual path from today's 19 live campaigns.
5. **An end-to-end session walkthrough** — no artifact shows the reimagined loop as one story: workshop → compile → play → harvest → vault.
6. **Progression interface** (P5, new) — the *content* is now mapped (the dial, three-layer record, the Tarot autopsy) but how off/light/heavy bind to one KB, and how the semantic layer is authored, are open. All unevaluated.

## Standing mining leads (named in notes, never executed)

E:\rpg entity-registry & disambiguation (0040) · deeper rpg-tools structural mine — bundling/build/cross-tool wiring (0037) · aegis data git-history, cause of 0072 · hallucinated-tag corpus study before designing the flag vocabulary (0059/0058) · Desktop archive bulk dump & triage (0064) — **now grounded**: census done + pre-planning captured ([[import-design-brief]], notes 0108–0112) · bundle.py audit before the compiler decision (0039/0044) · early-campaign memories before/after for 0054's style-drift proof · factions.py economy usage check (0084) · reverse-mcp-rpg as a source repo · SillyTavern mechanics (lorebook assembly, long-context handling) as a source.

## Ripe to graduate (theme-doc candidates, in rough order of readiness)

1. **Voice & register** (0005–0008, 0012, 0053, 0055 + sample-book) — coherent, partially production-proven, self-contained.
2. **Craft-skill authoring** (0013–0017, 0066) — proven in gm-skill, clean failure taxonomies.
3. **The compiler / composition stack** (0010, 0039, 0044, 0045, 0051, 0056–0058, 0063) — blocked partly on the bundle.py audit.
4. **The play-loop doctrine** (0080, 0078/0079, 0089, 0048/0052, 0060) — newest, still settling.
5. **Narrative structure — units & axes** (0121–0123) — small but already 2-of-3 adopted and
   owner-ratified as foundation; would graduate fast once branch mechanics + season's fate
   settle. The cleanest candidate to *start* a theme doc from since its spine is already fixed.
6. **Import / corpus-routing** (0108–0111 + 0112) — RIPE: five coherent notes, one authoritative
   source (solorpg IMPORT-DESIGN-BRIEF), clear spine (edges → k-NN → survey → provenance). All
   `unevaluated` — appraise first, then graduate. Pairs with the roadmap candidate below.
7. **Progression / rules-engine** (0104–0107, the new P5) — coherent arc (axis → failure → fix →
   doctrine) and surfaces the new pillar; **all unevaluated**, the gate must clear first.
8. **SSoT: canonical-raw vs derived renders** (0093/0094/0098 + 0056/0069/0002/0040) — now one of
   the densest themes; one sharp blocking decision (T8, the 0040↔0098 inversion) before it graduates.
9. **Namesets** (0119/0120 + 0013/0087/census-namesets) — nearly ripe; 0119/0120 await formal verdict.

*(Reordering note: 0092–0123 added four new graduation candidates. Voice & register and
craft-skill authoring remain the two most ready; import/corpus-routing is the strongest of the
newcomers because it has a single source and a roadmap consumer waiting on it.)*

## Roadmap candidates (concrete enough to sequence once the frame exists)

- **Export→import pipeline** ([[import-design-brief]] + [[export-structure-map]]; notes
  0108–0112). The user's own framework-agnostic pre-planning — one entrypoint of the future
  workflow, deliberately waiting on the refactor ([[0112-design-now-build-into-frame]]).
  Consumer of the KB data-model (Pillar 1) and composition stack (Pillar 3); recurring
  idea-recovery tool, not a one-time migration. Unappraised.
