---
tags:
  - kind/theme
  - theme/voice-register
  - theme/corpus-building
  - theme/context-economy
  - maturity/growing
  - verdict/adopt
created: 2026-06-15
appraised: 2026-06-15
synthesizes:
  - "[[0005-exemplars-over-instructions]]"
  - "[[0006-sample-book-grid]]"
  - "[[0007-harvest-vs-workshop]]"
  - "[[0008-form-is-the-lesson]]"
  - "[[0053-anchor-hierarchy-voice-keystone]]"
  - "[[0054-verbatim-capture-lost-intent]]"
  - "[[0055-register-anchor-banks]]"
  - "[[0062-conversation-transcripts-as-gm-context]]"
  - "[[0092-weave-player-input-doctrine]]"
  - "[[0099-pseudocode-as-encoding]]"
  - "[[0113-distill-dont-imitate]]"
  - "[[0114-voice-vs-setting-fidelity]]"
  - "[[0115-lora-idiom-lorebook-facts]]"
  - "[[0116-lora-earns-its-keep]]"
  - "[[0117-distill-vs-verbatim-tension]]"
  - "[[0118-encoding-by-data-type]]"
---

# Voice & Register — tacit, so demonstrated; demonstrated, so harvested

> **Third synthesis doc — appraised 2026-06-15, verdict: adopt.** The nine-move thesis below
> was ratified by the user (with the explicit understanding that later material may refine it —
> the normal life of a `growing` theme, not a reservation). **Scope of the adopt:** it
> ratifies the *spine* — "this is the shape of how voice works for us" — and does **not**
> promote the components underneath. Their own verdicts stand: Sample Book spine 0005–0008 +
> 0092 **adopt**, 0099 **undecided**, distill cluster 0113/0114/0117 **adapt**, 0116 **adopt**,
> 0115 **undecided**. The open threads remain open.

## The thesis (adopted)

**Register — voice, tone, texture — is *tacit*: it cannot be specified declaratively, only
shown. So the next-gen system treats demonstrated voice as a first-class data type with its
own encoding (prose exemplars) and its own lifecycle (harvested from play, preserved
verbatim, organized by scene-type × register, anchored on characters first).** Prose's *only*
job in the vault is to carry voice by example ([[0118-encoding-by-data-type]]); facts go to
structured records, logic to pseudocode. The recurring five-year failure has one shape — the
system *paraphrasing what it should have copied* — and the recurring fix has one shape:
capture the exact words.

This is the **category-1 (tacit) layer** of the encoding doctrine
([[0118-encoding-by-data-type]]), worked out in full: what it is, how it's filled, how it's
preserved, and where it stops.

## The disease: specification leaks, paraphrase drifts

Two failure modes, learned the hard way across generations:

- **Specification leaks.** "Write violence flat, concrete, unsentimental" always
  under-determines — the model fills the gaps loosely ([[0005-exemplars-over-instructions]]).
  This is empirical, not theoretical: the anchor scar ([[0053-anchor-hierarchy-voice-keystone]])
  records that ~50 words of character *description* still drifted, and drift only stopped when
  voice *samples* were added. Description failed where demonstration worked — discovered years
  before the Sample Book framing, independently.
- **Paraphrase drifts.** The corpus that should *demonstrate* the campaign's voice keeps
  getting silently re-voiced by the tools that maintain it. The memory postprocessor began
  **rewriting** scenes it was meant to copy verbatim ([[0054-verbatim-capture-lost-intent]]) —
  a suspected style-drift source, and a case of a *pipeline* drifting from its own spec, not
  the campaign drifting from canon.

## The moves (what the thesis actually commits to)

**1. Tacit → demonstrate.** A single worked example carries a register at once, in the right
proportions, including the parts you couldn't name ([[0005-exemplars-over-instructions]]).
This holds for *any* model via two different failure modes with one cure: small/local models
**can't obey** declarative rules; frontier models (Opus included) **over-interpret** them and
drift while "centering" a voice — both are fixed by giving the model something to *pattern-match*
rather than interpret. The craft laws ([[0008-form-is-the-lesson]]) govern what makes an
exemplar work: **method not subject** (a flowery description of plainness teaches floweriness),
**tag by register not source**, **tightest sample wins**, **sanitize for portability**, and
**store both directness and withhold** so the choice stays conscious.

**2. The Sample Book — a scene-type × register grid.** The buildable artifact that
operationalizes move 1 ([[0006-sample-book-grid]]): a library of concentrated exemplars,
indexed on a grid, assembled precompiled (campaign style profile) or JIT (pull the cell when a
scene-type fires). **This already exists in production** — `rust-and-ruin`'s texture bank and
`lumina-city`'s living dictionary are the grid alive ([[0055-register-anchor-banks]]):
exemplars organized by domain × POV register, harvested from play with session provenance. The
dictionary even carries *generative rules*, teaching the model to coin in-register terms, not
just reuse listed ones.

**3. Verbatim is a mode, not weak paraphrase — the mechanism that serves moves 1–2.**
Exemplar value lives in the *exact words*; a rewritten exemplar teaches the rewriter's voice
([[0008-form-is-the-lesson]]). So a pipeline must distinguish **copy** operations from
**summarize** operations and never let one decay into the other ([[0054-verbatim-capture-lost-intent]]).
The strongest evidence this is real: the user reinvented verbatim capture **three independent
times** — lost memory-scenes ([[0054-verbatim-capture-lost-intent]]), texture banks
([[0055-register-anchor-banks]]), and conversation transcripts ([[0062-conversation-transcripts-as-gm-context]]).
*Caveat on attribution:* only the texture half is voice-register. 0062's core motive is
**canon-as-state** — "dialogue is sometimes state; compressing discards canon, not texture" —
which belongs to the [[knowledge-base-canonical-vault]] / single-source-of-truth line, not
here. Verbatim serves two masters (preserve the voice, preserve the fact); this theme claims
only the first.

**4. Harvest / workshop / rewrite — how the grid gets filled.** Three gears sorted by
difficulty ([[0007-harvest-vs-workshop]]): **harvest** (clip your hits) for registers the
model can already roughly hit; **workshop** (hand-seed) for hard registers, non-optional
because of a bootstrapping deadlock (you can't clip an example the model can't produce); and
**rewrite-harvested** (the middle gear) — tune a real scene toward the anchor with a strong
model. *Findability is the first product*: a usable corpus already exists scattered across
years of play — build retrieval before generation. This is **already loadbearing** in the
current post-processing flow, which is why 0007 reads `maturity/proven`.

**5. Two error classes — voice vs idiom.** "Sails on a starship" is **not** a voice failure
([[0114-voice-vs-setting-fidelity]]). Voice (cadence, beat structure) is taught by
demonstration; **setting-fidelity / idiom** (how ships move, what jump-travel feels like) is a
*default-association* error — which way the probability mass leans at a fork. They route to
different fixes: exemplars/register banks for voice; **contrastive anchors + a banned-furniture
list** for idiom. Corollary: **discover registers, don't enumerate them** — tag each scene
freeform, cluster, and let the taxonomy fall out of play (combat self-splits into its real
5–10 sub-types; cliché-dominated clusters flag the hotspots).

**6. The rewrite contract — distill in the curated layer, copy in the verbatim layer.** Move 3
(preserve exact words) and move 4's rewrite gear (deliberately re-voice) look contradictory.
The resolution ([[0117-distill-vs-verbatim-tension]]): the **layer's contract decides, not the
operation**. Rewrite belongs to the *curated* layer (sample book / texture bank — the feature),
and only with an **explicit anchor present** — otherwise the rewrite launders the strong
model's own defaults into the bank ([[0113-distill-dont-imitate]], [[0114-voice-vs-setting-fidelity]];
a self-check needs an external referent, never its own output, per
[[0076-self-canonizing-hallucinations]]). **Copy-only** in the verbatim source (transcripts,
memories). 0054's sin was rewriting the *wrong* layer.

**7. Anchor priority — characters first, voice is the keystone.** When budgeting context
([[0001-tiered-progressive-loading]]), spend on character voice first — it's the empirically
load-bearing anchor ([[0053-anchor-hierarchy-voice-keystone]]). The keystone for *world* drift
turns out to be the same thing: demonstrated voice — characters get voice samples, worlds get
texture banks and living dictionaries ([[0055-register-anchor-banks]]).

**8. Weaving is exemplar-taught, and counter-trained.** The weave doctrine
([[0092-weave-player-input-doctrine]]) — dissolve player input into the prose, never
echo-then-append — is exactly the kind of behavior exemplars teach better than rules, and it
runs *against* mainstream AI-RP training. Adopted **firm in the spec, forgiving in the
judgement**: the instruction stays absolute because relaxing it lets the bad default reconquer
([[0013-counter-training-name-the-default]]).

**9. Fine-tuning is a sidequest, and weights carry idiom not facts.** A LoRA earns its keep
only where prompting can't reach — canonically, making a *small/local* model hold a register
zero-shot can't ([[0116-lora-earns-its-keep]]); play stays on Opus in Desktop, so it's a
sidequest, never the driver. And if a fine-tune happens, **weights carry voice + setting-idiom;
the lorebook carries hard facts** ([[0115-lora-idiom-lorebook-facts]]) — model weights are the
worst place to store a fact (unauditable, un-updatable, lossy). The distill-toward-spec data
move ([[0113-distill-dont-imitate]]) is reframed away from "LoRA dataset prep" into its real
job: a workshop technique for producing curated exemplars whether or not a fine-tune ever
ships.

## Where it sits

Parent: [[0118-encoding-by-data-type]] — this theme *is* the fully worked category-1 (tacit)
register. Sibling: [[knowledge-base-canonical-vault]] — that theme owns the canonical *facts*
and the verbatim-as-canon-state motive (0062); this one owns the canonical *voice*. They share
the verbatim mechanism from opposite ends. Upstream: [[modular-self-evolving-architecture]]
(one home per concern) and context-economy (anchor budgeting, JIT loading).

## Open threads (consolidated)

- **Register anchors as a first-class artifact type?** Only two campaigns have texture
  banks/dictionaries today — can harvesting become a standard debrief output so every campaign
  accretes one ([[0055-register-anchor-banks]])? How do they load — always-in or per-scene?
- **Register vocabulary.** "Tag by register" needs a register taxonomy. 0114 argues to
  *discover* it by clustering rather than define it up front — does that scale?
- **Verbatim extraction tooling.** Currently manual ("read session X, give me scene Y").
  On-demand vs extract-once-then-cache; the imports archive as permanent harvest substrate
  ([[0062-conversation-transcripts-as-gm-context]]).
- **The idiom/fact line.** "Ships don't have sails" reads as idiom but is enforced by a fact
  (FTL setting) — where exactly does bakeable idiom end and lorebook fact begin
  ([[0115-lora-idiom-lorebook-facts]])?
- **Mechanical weave check.** Can a hook flag verbatim input echoes ([[0092-weave-player-input-doctrine]],
  [[0082-live-hook-pipeline]])?

## Appraisal record

**Appraised 2026-06-15 — adopt.** The user ratified the nine-move thesis. The one
reservation raised — "I might think of more later that affects it" — was judged *not* a
blocker: a `maturity/growing` theme is expected to absorb later refinement without losing its
verdict (cf. [[0098-vector-index-over-vault-not-store]] refining adopted 0040). The adopt is
scoped to the **spine**, not the components: it does not promote 0099 (stays `undecided`),
0113/0114/0117 (stay `adapt`), or 0115 (`undecided`), and the open-threads list above stays
live. What's settled is the *shape*: voice is tacit → demonstrate → harvest and preserve
exemplars verbatim, encoded as category-1 prose ([[0118-encoding-by-data-type]]).
