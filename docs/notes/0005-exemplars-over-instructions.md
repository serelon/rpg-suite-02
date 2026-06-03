---
tags:
  - kind/pattern
  - source/new
  - source/sillytavern
  - theme/voice-register
  - theme/small-models
  - maturity/growing
  - verdict/unevaluated
created: 2026-06-03
---

# Steer voice by demonstration, not specification

**What it is.** Register (voice/tone) is *tacit* — it can't be fully specified declaratively.
"Write violence flat, concrete, unsentimental" always leaks; the model fills gaps loosely.
A single worked example carries the whole register at once, in the right proportions,
*including the parts you couldn't name*. "Like this" transmits what "do these twelve things"
can't. Highest-bandwidth way to steer voice — for any model, most of all small/local ones,
which imitate examples far more reliably than they obey rules.

**Where it comes from.** [[sample-book]] §1, the load-bearing premise the whole feature
rests on. Prototype evidence: the "Gleaners" SillyTavern session.

**Why it matters for next-gen.** If true, voice control should be *exemplar-first*, not
prompt-instruction-first — a different design center of gravity than rule/instruction stacks.

**Open threads.** How does this coexist with rule-based mechanics (cf. `aegis-tools`'
declarative rules engine)? Examples steer voice; do they steer *mechanics* too, or is that a
separate channel? Pairs with [[0008-form-is-the-lesson]] (the craft constraints that make an
exemplar actually work) and [[0012-intelligence-in-scaffolding]].
