---
tags:
  - kind/idea
  - source/conversation
  - theme/context-architecture
  - theme/voice-register
  - maturity/experimental
  - verdict/unevaluated
created: 2026-06-08
---

# Pseudocode as an encoding for prompts and lore

**What it is.** A seed idea (braindump 2026-06-08, picked up elsewhere): format prompts
or lore as **pseudocode** rather than prose. The bet — modern LLMs are extremely tuned
toward code, so they may follow threads, dependencies, and structure more reliably when
meaning is encoded code-style. Provenance: "prompt as pseudocode" seen in a SillyTavern
context; the user plans to test **"lore as pseudocode"** in a current campaign soon.
Explicitly unrefined: *"not sure what we'll do with this"* — capture the idea, the
refinement comes from testing.

**Two readings (the axis a test should resolve, not a decision now):**
1. **Lore-as-data-structures** — facts/relationships as declarations:
   `vekris.knows = [secret_01]`, `ashguard.disposition.party = hostile`. Legibility
   through structured state.
2. **Logic-as-control-flow** — the GM's reasoning as pseudocode:
   `if player.enters(temple) and not secret_01.revealed: foreshadow(...)`. Legibility
   through executable-looking branching. **Carries a known risk:** this edges toward the
   railroad / beat-by-beat-planning antipattern ([[0080-engineer-and-gardener]],
   [[0089-sealed-secrets-files]]) — encoding *behavior* as code may invite the rigid
   scripting the doctrine fights. Reading 1 is safer; reading 2 needs that guardrail.

**First observed success — human auditability (not the original bet).** Early in the
lore-as-code trial the payoff that actually landed was for the *human*: structured
pseudocode made a misunderstanding **instantly visible** that was buried and hard to spot
in a prose blob. This is a distinct axis from the LLM-legibility hypothesis — the same
encoding aids *the reader doing the audit*, not just the model. Directly serves
[[0057-compiled-context-needs-audit-tooling]] (compiled/derived context needs to be
auditable): structured lore is self-auditing in a way prose isn't, and the error surfaces
at a glance rather than via tooling. Encoding-for-legibility cuts both ways — model *and*
author.

**Where it sits among existing notes.** Relatives exist but make a *different* claim:
[[0010-docs-as-code-context-compiler]], [[0021-data-required-as-prompt]],
[[0022-reference-vs-state-data-driven-types]] are about pipeline/data *shape*; this is
about the **rhetorical encoding of meaning itself** for model legibility. Tension with
the voice/register line ([[0005-exemplars-over-instructions]],
[[0008-form-is-the-lesson]]): prose exemplars teach voice — pseudocode is the opposite
register, so it likely fits *structural* lore (state, relationships, mechanics) far
better than *characterful* lore (voice, tone, texture). Possibly a per-data-type choice,
not a whole-vault switch.

**Why it matters for next-gen.** If structural lore is more reliably tracked as
pseudocode, that's a cheap legibility win for exactly the data types that are hardest to
keep straight (entity relationships, who-knows-what, faction state — cf.
[[0071-fog-of-war-as-data-structure]], [[0086-faction-as-character-economy]]). Cleanly
testable against the prose status quo.

**Open threads.** **Needs testing** — the campaign trial is the next step; define what
"better thread-following" looks like before running it (fewer continuity drifts? cleaner
recall under load?). Which data types benefit (structural) vs. suffer (voice)? Does
pseudocode-lore compose with the cherrypick contract
([[0090-cherrypick-contract-three-layers]]) — is a `json` block already "pseudocode
enough"? Does it help small/local models more than frontier ones?

**Verdict.** _(unevaluated.)_
