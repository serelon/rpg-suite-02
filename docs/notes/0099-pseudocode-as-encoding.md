---
tags:
  - kind/idea
  - source/conversation
  - theme/context-architecture
  - theme/voice-register
  - maturity/experimental
  - verdict/adopt
created: 2026-06-08
appraised: 2026-06-13
reappraised: 2026-06-15
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
2. **Logic-as-control-flow** — the GM's *procedure* as pseudocode. The right example is
   **procedural, not narrative**: `if new_scene: scene_header()` — where `scene_header()` is
   defined elsewhere as the formatting to apply and/or the reasoning to do at a scene boundary.
   This encodes the GM's **operating procedure** (formatting, what-to-think-about at structural
   junctures), not the story's path. *(An earlier draft used
   `if player.enters(temple): foreshadow(...)` — that's a **bad** example: it encodes narrative
   **content**, which is exactly what would railroad. Discard it; it mischaracterizes the
   idea.)* **The guardrail isn't "control-flow is risky" — it's a layer rule:** control-flow
   belongs on **procedure**, never on **narrative content**. A railroad smell means you've
   applied it to the wrong layer ([[0080-engineer-and-gardener]]: this is squarely the
   *engineer's* side — scaffolding/process — not the gardener's emergent narrative). Used on
   procedure, it doesn't fight the doctrine; it serves it.

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

**Verdict.** _adopt — scoped to reading 1; reading 2 stays gated (reappraised 2026-06-15)._
First appraised 2026-06-13 (`undecided`) inside the three-category encoding model
([[0118-encoding-by-data-type]]); reappraised 2026-06-15 → **adopt, scoped.**

- **Reading 1 (lore-as-data: `vekris.knows = [secret_01]`) → adopt.** The relational slice
  (category 3) — barely a stretch, since [[0118-encoding-by-data-type]] already commits to
  pseudocode for relational lore. Low risk; the human-auditability win already landed in the
  lore-as-code trial. *This is the direction, not yet the proof:* `maturity/experimental`
  stays — adopt here means "our committed direction," not "tested in my workflow." Came from
  outside (SillyTavern) and is the most experimental idea in the cluster, untested in the
  user's own play — the verdict gate flagged this; the adopt is deliberate-direction, not
  proven-result.
- **Reading 2 (logic-as-control-flow, *procedural*: `if new_scene: scene_header()`) →
  deferred, not adopted — and deferred by *phase*, not danger.** Encoding GM procedure as
  control-flow is a **prompt-engineering** move, and we haven't reached the prompt-rebuild
  stage (research/speculation phase, per CLAUDE.md). So it waits for that phase, not for a
  hazard to clear. **Correction (2026-06-15, user):** there is *no* inherent railroad risk —
  that fear came from a bad narrative example. The real guardrail is a layer rule: control-flow
  on **procedure** (formatting, reasoning-at-junctures) is fine and is the engineer's job;
  control-flow on **narrative content** is the wrong layer and the only thing that would
  railroad ([[0080-engineer-and-gardener]]). Revisit when prompt rebuilding starts.

Tightened open question (unchanged): not "prose vs pseudocode" but **"when must a category-2
fact-record graduate to category-3 relational pseudocode?"** Structured records (sheets,
stats) are category 2 and already solved — they don't need pseudocode at all.
