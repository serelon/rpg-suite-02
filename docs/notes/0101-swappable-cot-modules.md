---
tags:
  - kind/pattern
  - source/new
  - theme/reasoning-discipline
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-10
---

# Chain-of-thought as a swappable, per-model / per-genre module

**What it is.** In the SillyTavern presets (`inbox/`), the reasoning block is itself a
**toggle in the fragment library** ([[0100-fragment-library-prompt-assembly]]), not baked
into the system prompt. BOLT+ ships one CoT (`⚡️BOLT CoT`); MAX+ ships **five
interchangeable variants** under a `CHOOSE ONLY 1 CHAIN OF THOUGHT` divider — Realism /
Freaky / Novel / Freaky-Novel / and a dedicated `⭐️Claude/Gemini Pro` one. Reasoning
strategy is tuned **per model and per genre** and hot-swapped like any other fragment.

**The shape of the BOLT CoT block** (the mechanics, separate from its content):
- Reasoning happens inside `<think>` tags; **"no full drafting"**, bullets only — brainstorm/
  calculate, don't pre-write the prose.
- A fixed **numbered checklist of 7 tasks**, declared as "review each sequentially,
  skipping any = failure." (Bias control, scene-isolation, show-don't-tell, natural
  dialogue, user-boundary, anti-slop sweep, length budget.)
- An explicit **leak gate** at the end: `<generate_output>` instructs "do not leak any
  reasoning from `<think>` into the response."
- An OOC escape hatch: the *one* case where `<think>` is skipped is out-of-character
  user commands.

**Where it comes from.** `docs/sources/Freaky Frankenstein 4 BOLT+/MAX+ Updated.json`
(mined from `inbox/`, archived as primary sources). The user
flagged **CoT-in-general** (not this exact block) as a pattern worth exploring for the
future.

**Why it matters for next-gen.** Two distinct transferable ideas:
1. **CoT as a hot-swappable module**, selected by the same manifest that assembles
   everything else — so reasoning strategy becomes a *(campaign × model)* choice, not a
   constant. A frontier model and a small local model can get different reasoning
   scaffolds from one library; so can "tense thriller" vs "slow novelization"
   ([[0093-novelization-as-output]]).
2. **Checklist-discipline reasoning** — the "N sequential tasks, skipping = failure"
   shape. This directly echoes [[0097-interleaved-checklist-thinking]] (checklist-
   discipline is the keeper) and the thinking-tuning incident ([[0066-thinking-block-tuning]]
   via [[gm-skill-thinking-tuning]]): enforce *mandatory checks*, not length.

**The known trap (carry the 0097 warning forward).** Several of the 7 tasks are
**self-referential checks** — "have I used purple prose?", "did I overstep {{user}}?",
"omit anything repeated in the last 4 responses." [[0097-interleaved-checklist-thinking]]
showed the damning failure mode: a self-check that grades the model's own output against
its own judgment self-confirms (the fact-check example checked drift against its own
prose and passed itself). The anti-slop banned-vocabulary list is the partial antidote
here — it's an **external reference** to check against, not a vibe. Lesson for our CoT:
checklist *structure* is good; every check needs an **external referent** (a banned list,
a state file, the canonical vault) or it's theater. Also note modern Opus may collapse an
over-engineered checklist — calibrate to the model.

**Open threads.** Which checks genuinely need CoT vs. can be enforced structurally
(write-time validation, [[knowledge-base-canonical-vault]])? Does per-model CoT selection
belong in the manifest, or is it inferred from a model capability tag? How does the
"no drafting in `<think>`, bullets only" rule interact with models that reason better by
drafting? Is the leak-gate needed when the host already strips think-blocks? Relationship
to pseudocode encoding ([[0099-pseudocode-as-encoding]]) — the CoT itself is written in
the bracketed DSL.

**Verdict.** _(unevaluated.)_
