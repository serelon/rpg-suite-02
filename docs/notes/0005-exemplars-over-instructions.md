---
tags:
  - kind/pattern
  - source/new
  - source/sillytavern
  - theme/voice-register
  - theme/small-models
  - maturity/growing
  - verdict/adopt
created: 2026-06-03
appraised: 2026-06-13
---

# Steer voice by demonstration, not specification

**What it is.** Register (voice/tone) is *tacit* — it can't be fully specified declaratively.
"Write violence flat, concrete, unsentimental" always leaks; the model fills gaps loosely.
A single worked example carries the whole register at once, in the right proportions,
*including the parts you couldn't name*. "Like this" transmits what "do these twelve things"
can't. Highest-bandwidth way to steer voice — for *any* model, via **two failure modes with
one cure**: small/local models **can't obey** declarative rules and imitate examples far more
reliably; frontier models (Opus included) **over-interpret** rules and drift while "centering"
a voice, but will faithfully *pattern-match* an exemplar instead of interpreting it. The
exemplar sidesteps both interpretation and disobedience at once.

**Where it comes from.** [[sample-book]] §1, the load-bearing premise the whole feature
rests on. Prototype evidence: the "Gleaners" SillyTavern session.

**Why it matters for next-gen.** If true, voice control should be *exemplar-first*, not
prompt-instruction-first — a different design center of gravity than rule/instruction stacks.

**Open threads.** How does this coexist with rule-based mechanics (cf. `aegis-tools`'
declarative rules engine)? Examples steer voice; do they steer *mechanics* too, or is that a
separate channel? Pairs with [[0008-form-is-the-lesson]] (the craft constraints that make an
exemplar actually work) and [[0012-intelligence-in-scaffolding]]. **Exemplar-vs-instruction
ratio is a per-register dial, not a fixed target** — a hard register leans almost entirely on
its exemplar, an easy one can ride mostly on instruction (the difficulty gradient 0007 sorts
by). Lean show-heavy overall, but resist fixing a global ratio; it would flatten that gradient.

**Verdict.** _adopt._ Exemplars-first is a ratified next-gen pillar ("more show, less tell").
Confirmed to hold for frontier models too (pattern-match, don't interpret; centers the voice),
not just small/local. Sits inside the three-category encoding model
([[0118-encoding-by-data-type]]): prose/exemplar is for *tacit* data only.
