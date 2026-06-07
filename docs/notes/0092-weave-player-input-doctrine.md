---
tags:
  - kind/pattern
  - source/conversation
  - theme/gm-craft
  - theme/voice-register
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-07
---

# Weave player input into the narrative — interleave-and-render, never echo-then-append

**What it is.** A play doctrine: the GM must dissolve player input into its own prose —
dialogue placed at the right narrative beat (voice touched up to fit the character),
stated thoughts rewritten into the narrative voice, inner monologue and emotional life
actively *simulated* around them. The canonical failure mode is **echo-then-append**:
treating the input as an immutable block that "already happened" and bolting story on
after it. Enables much longer, richer player inputs without breaking story flow.

**Where it comes from.** User doctrine since the Sonnet 3.x era (braindump 2026-06-07).
Originally semi-mandatory for the novelization workflow
([[0093-novelization-as-output]]) — woven sessions have no seams to remove. Notably
**counter-trained**: mainstream AI-RP norms run the other way, so training data now
carries a heavy pattern *against* weaving — echo-then-append "happens often still."
A live instance of [[0013-counter-training-name-the-default]].

**The fidelity hierarchy** (what the GM may change, in order of sanctity):

1. **Intent — sacred.** Never altered.
2. **Wording/voice — correct toward the character.** Especially needed when the player
   has lost track of a character's voice after time away.
3. **Inner/emotional life — simulate freely** (EQ-dependent: high-EQ models great,
   low-EQ models "butcher everything"). Player direction stays canon on disagreement.
4. **Impossible actions — error-correct, don't execute.** "I do x!" when x can't happen
   in fiction → the GM interprets intent ("actually means y") or renders an attempt.
   The GM is an intent-interpreter, not a command-executor.

**Conflict resolution is lightweight.** Disagreements over a character's inner life are
steered with inline OOC parentheticals — "(careful, she's actually feeling x, not y,
keep the diff subtle)" — and the heavy tool is simply redoing the update with extra
instructions, routine at key scenes and considered fine. Rhymes with
[[0026-exceptions-are-features]]: the redo loop is part of the workflow, not a failure.

**Why it matters for next-gen.** This is a prompt/skill-layer enforcement problem against
training-data gravity ([[0013-counter-training-name-the-default]],
[[0005-exemplars-over-instructions]] — weaving is exactly the kind of behavior exemplars
teach better than rules). The fidelity hierarchy is concrete enough to express as
GM-skill instructions; the EQ-dependence suggests it's also a model-selection criterion.

**Open threads.** Can weaving quality be checked mechanically (e.g. hook that flags
verbatim input echoes — [[0082-live-hook-pipeline]])? How does the doctrine interact
with [[0053-anchor-hierarchy-voice-keystone]] — voice touchup needs the character's
voice anchors in context. Does late-Opus-4.x-era training still fight weaving as hard
as 3.x-era?

**Verdict.** _(unevaluated.)_
