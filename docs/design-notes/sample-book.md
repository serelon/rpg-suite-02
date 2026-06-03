---
tags:
  - kind/design-note
  - source/new
  - source/sillytavern
  - theme/voice-register
  - theme/context-architecture
  - theme/docs-as-code
  - theme/small-models
  - maturity/growing
  - verdict/unevaluated
created: 2026-06-03
origin: inbox/sample-book-design-notes.md
atomized-into:
  - "[[0005-exemplars-over-instructions]]"
  - "[[0006-sample-book-grid]]"
  - "[[0007-harvest-vs-workshop]]"
  - "[[0008-form-is-the-lesson]]"
  - "[[0009-jit-context-and-eviction]]"
  - "[[0010-docs-as-code-context-compiler]]"
  - "[[0011-identity-pinned-state-evicted]]"
  - "[[0012-intelligence-in-scaffolding]]"
---

> **Preserved design-note (verbatim).** This is a primary source — the user's own design
> thinking. Its distinct ideas are extracted as atomic notes (see `atomized-into` above);
> this file keeps the full argument and voice intact. Appraise the atomic notes; cite this.

# Design Notes — The Sample Book (Style-Library Feature)

*Captured June 2026, from the SillyTavern / "Gleaners" session. These are the transferable principles for the next-gen RPG framework — not the campaign-specific build. The Gleaners work (card `mes_example`, the worldbook register-directive, the PTSD-doc-as-violence-key story) was effectively a hand-built prototype of the feature described here.*

---

## 1. The core feature

A **Sample Book**: a first-class library of concentrated *register exemplars*, indexed on a **(scene-type × register) grid**. Each cell holds a small style guide for "write a type-A scene in B-style" — ideally a worked passage, not a description.

**Why exemplars instead of instructions.** Register is *tacit*. You cannot fully specify a voice declaratively — "write violence flat, concrete, unsentimental" always leaks, and the model fills the gaps loosely. A sample carries all of it at once, in the right proportions, including the parts you couldn't name. *"Like this"* transmits what *"do these twelve things"* can't. A reference exemplar is the highest-bandwidth way to steer voice — for any model, and especially for small/local ones, which imitate examples far more reliably than they obey rules.

**Assembly: precompiled OR on demand.** Two modes, same split that runs through the whole architecture:
- **Precompiled** — a campaign-level style profile, set at creation, that loads default register keys for that campaign's tone.
- **On demand (JIT)** — pull the specific cell when a scene-type fires and wants its key.

---

## 2. How the library gets built

Two sources, and they are **sorted by difficulty**, not competing:

**Harvest from play** — for registers the model can already roughly hit. Clip your hits: when a scene lands exactly right, file it into its grid cell. The corpus grows itself out of successes and captures *your* emergent voice for free. Build in the "clip" affordance as a core interaction.

**Workshop in advance** — for the hard registers the model *can't* hit unprompted. This is non-optional, because of a **bootstrapping deadlock**: harvest assumes play can produce a clipworthy example, but a hard register is hard precisely because the model can't produce it without one to imitate. You'd wait forever for a hit that never comes. Hard cells must be seeded by hand.

Two bonuses of advance-authoring that harvest structurally cannot give:
- It **defines** the register. You often don't know what "right" even is for a hard one until you've fought to write a single clean instance. Authoring is discovery, not just production — it surfaces a register you couldn't yet name.
- It yields a **cleaner key** — honed and fingerprint-stripped — instead of whatever play happened to throw off.

**Findability is the actual first product.** A usable corpus already exists, scattered across years of past play; it just isn't indexed. Half the win is pure *collect-and-tag* — turning "I wrote a great one of these somewhere" into a cell you can point at. Build retrieval before building generation.

---

## 3. Laws of a good exemplar (example-craft)

**Form is the lesson — an example transmits its *method*, not its subject.** The model copies *how* you wrote, not *what* you wrote about. Consequences:
- An oblique, metaphor-heavy passage teaches obliqueness even when it's nominally "about" something direct.
- A flowery *description* of how to be plain is the worst case of all: it demonstrates floweriness while claiming to teach plainness.
- The only thing that can key a *directness* register is a passage that is itself uncomfortably plain — short, concrete, figurative language stripped out, the thing simply stated. This is hard for any skilled writer, because craft-instinct always reaches for the metaphor and the withhold. Directness is a discipline reached by suppressing one's own skill. (Flag these cells; they need the most deliberate authoring.)

**Tag by register, not by source.** An exemplar's value is the voice it transmits, not the document it came from. Decouple it from its origin-purpose or cross-purpose reuse never happens. (The PTSD-flashback doc that became the violence key only worked because it was, in effect, filed under "close-up violence, this voice.")

**Tightest sample wins.** A single paragraph in the right register out-steers a page of instruction and costs almost no context. Harvest the nub, not the whole document.

**Sanitize for portability.** A register key drags its *specifics* along too — one character's particular interiority bleeding into a scene it has no business in. The cleaner and more fingerprint-stripped the sample, the further it travels. ("Similar to X, *ish*" — the "ish" is the instruction *texture, not contents*; make it explicit where possible.)

**Directness-vs-withhold is its own axis.** Some scenes want the withhold (the gap is the point); some want the plain hit (the directness is the point). Both are legitimate registers. The *error* is letting craft-instinct **default** to the withhold when the scene wanted directness. Store both a withheld key and a plain key for charged scene-types, and let the system's quiet job be forcing that choice to be **conscious** instead of habitual.

**Validation test for a plainness cell:** strip every figure of speech out — did it lose anything? If yes, it isn't a plainness key yet. If no, it was already plain, and plain is what it will teach.

---

## 4. The substrate it plugs into (context architecture)

The Sample Book is the *voice layer* of the same architecture the framework should use for everything:

- **Crispness is a salience problem, not a capacity one.** Throwing everything into a large context flattens emphasis; the model can't tell load-bearing from ambient. Absence is load-bearing. Curate what's present.
- **JIT context + eviction.** Retrieval (what to load) is the easy, well-trodden half; **eviction** (what to drop, and when) is the underbuilt half. Context wants a lifecycle, not a growing transcript. Narrative **beats are natural eviction boundaries** — the pacing model and the context model want to be the same model.
- **Docs-as-code is the enabling substrate.** Structured source (frontmatter: scene-type, register, tags, load conditions) gives *declarative, auditable* handles, so context can be compiled per-beat like a build target — rather than fuzzy vector retrieval over an unstructured pile. The Sample Book is this idea applied to *registers* instead of *facts*: a prompt build system for voice.
- **Hybrid runtime.** Deterministic skeleton assembled from frontmatter rules + agentic top-up where the model pulls extra on demand. (This is the fusion of positional/declarative control with the agentic paradigm.)
- **Evergreen vs. evictable.** Anything that rides in context every turn must hold only *always-true* identity — the smallest set of fixed facts. Time-bound *state* belongs somewhere updatable/clearable (e.g. an author's-note layer), or it quietly fights the live game as it goes stale. Identity pinned, state evicted.

---

## 5. Why this matters extra for small / local models

Move the intelligence **out of the weights and into the scaffolding** — compile the craft into the exemplars and the assembly rules so the model only has to do the one thing small models are now genuinely good at: fluent, in-voice continuation. The dumber the model, the more good context engineering pays rent. Calibration is model-specific: the same scene wants more explicit edge for a small model and more restraint for a frontier one, so register keys should be tunable/swappable per target model.

**Worked failure to remember — the "blankets bug":** an elegant withhold ("nobody offers you the rest of it") *is itself* an instruction to withhold; a small model obeys the form and the intended subtext evaporates (e.g. raiders read as mere "thieves," the violence glossed). Same root as "form is the lesson." The fix is to make the load-bearing thing *materially present and plainly depicted*, not implied — and to teach that via a plain exemplar, never a description of one.

---

## 6. One-line summary

> Steer voice by demonstration, not specification; store demonstrations in a (scene-type × register) grid; grow the easy cells from play and hand-author the hard ones; and never forget that an example teaches its method — so a plain register can only be keyed by a plainly-written sample.
