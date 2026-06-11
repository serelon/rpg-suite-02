---
tags:
  - kind/pattern
  - source/new
  - theme/context-architecture
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-10
---

# Composable prompt assembly: fragment pool + ordered enable-manifest + data-hole slots

**What it is.** The structural pattern behind SillyTavern Chat Completion presets
(observed in the two "Freaky Frankenstein 4" presets, BOLT+ and MAX+, in `inbox/`).
A preset is **two decoupled tables**, not one prompt:

1. **Fragment pool** (`prompts`) — a flat, unordered bag of named blocks, each just
   *(identifier, name, role, content)*. Inert: a fragment has no opinion on whether it's
   used or where it goes. BOLT+ ships ~43, MAX+ ~48.
2. **Manifest** (`prompt_order`) — a separate *ordered* list of references by id, each
   carrying an `enabled` boolean. The manifest is the **only** place sequence and on/off
   live. Pure references, no content.

Assembly = walk the manifest top-to-bottom, drop `enabled:false`, look up each id in the
pool, emit its content under its role, concatenate. The manifest *is* the build profile —
BOLT+ and MAX+ share most of the pool and differ mainly by manifest (and a few extra
fragments).

**Three moves that make it powerful.**
- **Content/composition decoupling.** Order is data, not structure: whether the lorebook
  splices *before* or *after* the character description is one reference's position. The
  author tunes *where rules sit relative to data* by reordering, never rewriting.
- **Present-but-dormant fragments.** A block can live in the pool and be referenced
  `enabled:false` forever. This powers the shipped-but-off README, and every "pick one
  of {A,B,C}" band (all options present, one enabled).
- **Marker / data-hole slots.** Entries like `Chat History`, `Char Description`,
  `Lorebook Before/After`, `Persona` are `marker:true` with empty content — named
  insertion points the host engine fills with runtime data at assembly time. So one
  ordered stream interleaves *authored fragments* and *live-data holes*, and the author
  controls the interleaving.

Mental model: a **playlist over a sample library, where some tracks are live-input
jacks.** Or, in [[0099-pseudocode-as-encoding]] terms: each fragment's content is the
pseudocode-DSL; the manifest is the **linker** deciding which compilation units link and
in what order; markers are the live-input symbols resolved at link time.

**Where it comes from.** `docs/sources/Freaky Frankenstein 4 BOLT+ Updated.json` and
`...MAX+ Updated.json` (mined from `inbox/`, archived as primary sources) — community
SillyTavern presets. Structure (not the ERP payload)
is the research object. The pattern is *typical* of mature ST profiles, per the user.

**Why it matters for next-gen.** This is exactly the separation a campaign-context
*compiler* wants: fragments = rules modules / POV / pacing / per-model CoT / savefile /
memories / lorebook / sheets; manifest = a per-campaign or per-session profile saying
which subsystems are live and where data splices in. Toggle isolation rules, swap the CoT
for a different model, decide whether memories load before or after the scene — all
without touching fragment text. Strong fit with the docs-as-code compiler line
([[0010-docs-as-code-context-compiler]]), the thin/fat target profiles
([[0063-portable-bundles-constraint]]), and the modular "one home per concern, compose
don't fork" doctrine ([[modular-self-evolving-architecture]]). The marker/data-hole idea
overlaps [[0021-data-required-as-prompt]] / [[0022-reference-vs-state-data-driven-types]].

**The ST-limitation delta (what a custom framework should solve natively).** ST's
manifest is **on/off booleans only**. It cannot express:
- *mutual exclusion* — "exactly one of {3rd, 2nd, 1st, Hybrid POV}";
- *dependencies* — "Freaky Deepy requires DS4";
- *conflicts* — "don't run two CoT modules at once".

ST works around this with **convention-as-UI**: zero-length divider fragments carrying
instructions in their *name* (`👇Pick only 1 Narrative Drive 👇`,
`CHOOSE ONLY 1 CHAIN OF THOUGHT`) plus a dormant README block. The constraint is
documented, not enforced — soft-enforced only by "the model gets confused if you enable
two." The user's framing: **that convention-as-UI is partly a hack to build complexity
inside a limited framework; our custom toolchain should solve mutual-exclusion /
dependency / conflict cardinality in the manifest format itself rather than resorting to
the same hacks.** Think radio-button groups, `requires`/`conflicts` edges — a real
dependency graph over fragments, not a flat boolean list.

**Open threads.** What's the right manifest schema for cardinality groups + dependency
edges? Does the fragment pool want hierarchical tags (like this vault) so manifests can
select *by capability* rather than by hand-listed id? How does this compose with the
cherrypick contract ([[0090-cherrypick-contract-three-layers]]) and the vector index
([[0098-vector-index-over-vault-not-store]]) — is a "fragment" just a vault note selected
into a build? Per-model manifest variants (cf. swappable CoT,
[[0101-swappable-cot-modules]]) suggest profiles may need a *(campaign × model)* matrix,
echoing the (scene-type × register) exemplar grid ([[sample-book]]).

**Verdict.** _(unevaluated.)_
