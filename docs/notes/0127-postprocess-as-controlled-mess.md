---
tags:
  - kind/pattern
  - source/solorpg
  - theme/workflow
  - theme/modular-architecture
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-25
---

# Postprocess is an irreducible mess — design the thing that *controls* it, not a clean pipeline

**What it is.** `[postprocess]` — the export→vault stage of the grand loop
([[0124-the-grand-loop]]) — is the most fleshed-out, most question-marked, most knob-laden,
most-to-build box in the system. Owner's design thesis (2026-06-25): **it is a mess, it will
stay a mess; the key is to accept that and build a way to *control* the mess.** It's a whole lot
of smaller tasks in one workflow — *its own loop* — so it wants a control layer, not a tidied
linear pipeline.

**Three control pillars** (taken one at a time, not all at once):
1. **Orchestration** — which atomic tasks run, in what order, with what dependencies.
2. **Steering / override** — re-run, skip, correct, hand-tune individual steps without redoing
   the batch.
3. **Visibility** — know *what happened* across dozens of small steps; catch the one that
   silently went wrong. (Owner: steering + visibility are *partially the same thing*.)

**Where it comes from (the live skill, mined 2026-06-25).** `solorpg/.claude/skills/
session-postprocess/SKILL.md` (v1 — the one actually used; **v2's team/Lorekeeper variant is
deprecated, "context window now sufficient"**, a 0031 transient-constraint workaround the owner
*already retired*). v1 is single-conversation, six phases:
- **Setup → Discovery → Validation → Capture → Bundle-integration → Completion.**
- **Capture (Phase 4)** is the per-thing fan-out: `summary` (density-gated, "matter in 10
  sessions?"), `savefile` (a *merge*: update/preserve-dormant/add/close), `memories` (8–12, six
  typed shapes), `locations` (new/update), `characters` (new full/minimal + the **core-character
  guardrail**: additive-only, never rewrite voice; "appeared-on-screen vs merely-mentioned"
  rule), campaign-specific (stories / era-markers / tactical data-restore / checklists).
- Each capture step **reads its own guide before drafting** (`memory-extraction-guide.md`,
  `location-guide.md`, `character-guide.md`) — this is the owner's "one big skill calling a
  couple guides for formatting."
- Heavy human-in-loop already: **draft → review → adjust → write** per output, escape hatches
  (skip / later / stop), git **branch-per-run + PR** for review.

**The next-gen move.** *Orchestrator skill + atomic step-skills.* The phase spine already **is**
the orchestrator skeleton; modularizing = lift each Phase-4 output (**+ its existing guide + its
strict inline thinking**) into its own skill, leaving a thin orchestrator that sequences them.
"Strict thinking/guidance per step" = [[0016-thinking-block-as-enforcement]] /
[[0097-interleaved-checklist-thinking]] pushed down to step granularity. The guides are the
seeds of the step-skills — most of the per-step content already exists, just fused.

Maps onto the three pillars:
- **Orchestration** → the orchestrator skill + the step registry (which steps, deps, order).
  Kin to [[0036-everything-is-a-module]], the event-bus [[0023-event-bus-orchestrator]], and the
  abandoned `E:\rpg` 5-agent pipeline (parse→entity→timeline→wiki→briefing) — the heavyweight
  prior art for exactly this control layer.
- **Steering/override** → re-run/skip/correct a *single* step-skill in isolation (today: redo
  the whole conversation or fix in the PR). Modular steps make per-step re-runs cheap.
- **Visibility** → automated **audit step** + eventual **DB-review GUI** (inspect → go back →
  correct) — but that rides on provenance backlinks ([[0128-provenance-backlinks-at-update-granularity]]).

**Why it matters for next-gen.** This is the Pillar-1 black box the loop-as-spine mapping flagged
as the natural first design dive (both black boxes are P1). It's also the [[0075-postprocessing-as-vault-librarian]]
"propose-never-commit" custodian, now given an internal structure. The mess is real; the design
target is governing variety, not eliminating it.

**Open threads.** What's the *step registry* shape — static list, or dependency graph (memories
depend on character IDs existing; bundle-integration depends on everything)? Where do the
draft→review gates live in a modular world — per step-skill, or a single orchestrator gate
([[0028]] T4 gates-vs-streaming)? Does the savefile *merge* survive or dissolve into
threads-like structured state ([[0073]])? Is "campaign-specific outputs" a fourth extensibility
seam (per-campaign step-skills)?

**Verdict.** _(unevaluated — captured as design shape, not yet appraised.)_
