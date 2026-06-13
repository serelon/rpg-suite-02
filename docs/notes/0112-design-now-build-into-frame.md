---
tags:
  - kind/principle
  - source/solorpg
  - theme/architecture
  - theme/self-evolution
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-13
---

# Design now, build into the new frame — durable capabilities, not bolt-on scripts

**What it is.** The posture behind the whole import brief ([[import-design-brief]]), worth
extracting as a principle. The brief *deliberately does not build the pipeline yet*,
because its load-bearing pieces — multi-label relationships, a provenance graph,
UUID-keyed incremental merge, a semantic index — are **data-model decisions**, and the
next-gen refactor is where the data model gets redrawn. Building them against the current
layout means rebuilding in months. The reframe: *"a semantic index + relationship graph
over the corpus is plausibly a **native capability** the refactored framework wants, not an
import script."* So: **design now, build into the new frame.** Today's artifact is the
brief, not code.

**Where it comes from.** `../solorpg/imports/IMPORT-DESIGN-BRIEF.md`, "Why this waits for
the refactor" + "Don't add load before the refactor." The user's own pre-planning — and it
*is* the operating posture of rpg-suite-02 itself.

**Why it matters for next-gen.** Two things. (1) It's a **discipline against premature
scripting**: when a needed thing is really a data-model decision, capturing the design and
*waiting* beats shipping a script you'll tear out — the same "don't rush ahead" stance in
this repo's CLAUDE.md, here stated as an architectural test ("is this a native capability
or a bolt-on?"). (2) It validates treating the **import pipeline as one entrypoint of the
future workflow** ([[0110-wilderness-survey-idea-recovery]]) rather than a side tool —
hence its **roadmap-candidate** status. Connects to the modular/self-evolving doctrine
([[modular-self-evolving-architecture]]): capabilities live in one home in the frame, not
forked into per-task scripts.

**Open threads.** What's the test for "native capability vs bolt-on script" in general?
Which *other* deferred tools in the ecosystem are secretly data-model decisions waiting on
the refactor? Does "design now, build later" need a holding pen (this vault) so designs
don't rot before the frame exists — i.e. is the brief itself the proof the holding pen
works?

**Verdict.** _(unevaluated.)_
