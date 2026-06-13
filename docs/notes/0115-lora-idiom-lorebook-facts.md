---
tags:
  - kind/principle
  - source/conversation
  - theme/voice-register
  - theme/local-finetuning
  - theme/single-source-of-truth
  - maturity/seed
  - verdict/undecided
created: 2026-06-13
---

# Fine-tune for voice + idiom; keep hard facts in the lorebook

**What it is.** A clean division of labor between a fine-tuned model and a retrieval
layer. Fine-tuning (a LoRA) is excellent at shifting **idiom and defaults** — "this world
*feels* like this," ships move like X not like sailing — because that's reshaping
probability mass. It is a **blunt instrument for exact facts**: drive numbers, named tech,
who's-who. Overload the adapter with physics and it memorizes them sloppily and forgets
half. So: **weights carry voice and setting-idiom; the lorebook / worldinfo carries the
hard facts.** Pin the physics in retrievable data; let the model handle the feel.

**Where it comes from.** Inbox conversation [[Claude-export-custom-lora]] (2026-06-13),
closing distinction. The user already runs worldinfo in SillyTavern, so the split maps
onto an existing tool boundary.

**Why it matters for next-gen.** It's the **single-source-of-truth doctrine applied to a
trained model**: facts live in exactly one canonical, editable place (the
[[knowledge-base-canonical-vault]]), and everything else is a view or a learned disposition.
A model's weights are the *worst* place to store a fact — unauditable, un-updatable without
retraining, silently lossy — which is the same argument as
[[0011-identity-pinned-state-evicted]] (pin stable identity, evict mutable state) and
[[0107-prose-deprecation-doctrine]] (prose is the wrong substrate for data), now extended:
**model weights are also a substrate, and they're for idiom, not data.** Reinforces that a
local fine-tune doesn't replace the KB/retrieval layer — it sits beside it.

**Open threads.** Where exactly is the line between "idiom" (safe to bake) and "fact"
(must stay in the lorebook)? "Ships don't have sails" reads as idiom but is enforced by a
fact (this is an FTL setting). Likely the same payload-vs-carrier cut as
[[0107-prose-deprecation-doctrine]]. Does a fine-tune *plus* lorebook double-source the
idiom (baked-in **and** in worldinfo prose), and is that redundancy a feature or a drift
risk? Touches the context-injection economics of [[0077-context-injection-vs-cache-economics]].

**Verdict.** _(2026-06-13.)_ **undecided** — only bites if local-model play actually
happens (gated by [[0116-lora-earns-its-keep]]), so parked. The underlying half — *facts
live in the lorebook, not in any model's weights* — is independently true and already
carried by [[0011-identity-pinned-state-evicted]] / [[0107-prose-deprecation-doctrine]] /
[[knowledge-base-canonical-vault]]; this note's specific contribution (weights as an
idiom-only substrate) waits for a real local-model experiment to evaluate.
