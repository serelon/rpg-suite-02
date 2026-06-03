---
tags:
  - kind/idea
  - source/solorpg
  - theme/composition
  - theme/architecture
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# Multi-axis data management — campaign/branch/subsetting are axes, not a fixed hierarchy

**What it is.** (User's reframe of what I first read as a containment hierarchy:) the lesson
of The Silence's structure is a **multi-axis approach to data management and imports**. The
axes that exist today: main campaign folder, branches, subsettings. Plausible future axes:
per-character, per-location, **per-era** (at least two timeline-bending campaigns exist — one
time-travel, one asynchronous). The hierarchy is just the axes that happened to be needed so far.

**Where it comes from.** `solorpg/campaigns/the-silence/` — the most advanced live example:
five subsettings (Lodestone, Covenant of Hands, The Solramis, The Drift, Buried Light), nested
protagonist branches (`branches/solramis/{shanti,zuri}/`), and a bundle `extends` chain that
mirrors the structure exactly: `branches/bundle-base.json` →
`reference/subsettings/lodestone/bundle-template.json` →
`branches/lodestone/bundle-template.json` → `…/greta/bundle-template.json`. The composition
mechanism ([[0039-bundle-template-composition]]) *is* the axes' implementation.

**Notable design facts.**
- The Silence was deliberately designed with **capacity to hold two subsettings
  simultaneously** if needed — structural headroom designed ahead of need (the *good* cousin
  of [[0031-beware-transient-constraint-architecture]]: capacity for structure, not
  workarounds for model limits).
- User: **subsettings should always be an option**, even if rarely used — a good pattern for
  complex campaigns.
- But note: subsettings **never graduated out of The Silence**. They stayed campaign-local
  until this refactor — evidence for why [[0043-campaigns-as-testbeds]] wants *tight*
  graduation cycles rather than waiting for major-version refactors like this one.

**Why it matters for next-gen.** The spec should model campaign data as composable axes with
optional levels (subsetting layer collapses when unused), not a fixed tree. New axes
(per-era for time-travel) must be addable without restructuring. The compiler
([[0044-scenario-compiler]]) resolves across axes.

**Open threads.** Two unreconciled branch models exist: The Silence's nested-folders+extends
(proven) vs `campaign.py`'s flat array with convergence points (**built, never used** —
see [[0050-built-never-used-inventory]]). Convergence is paper-only; does it earn a place?

**Verdict.** _(unevaluated — appraisal owed, parked 2026-06-03 at user's request.)_
