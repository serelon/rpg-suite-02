---
tags:
  - kind/pattern
  - source/solorpg
  - theme/workflow
  - theme/human-in-the-loop
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# Checkpointed human-in-the-loop — draft → review → adjust → write, with guardrails

**What it is.** The postprocess workflow is **gated at every artifact**: nothing is written
blind. Each output runs draft → *present to user* → adjust → only then write to disk.
Discovery is incremental ("do **not** ask for everything at once"), validation lets the user
**select** which characters/locations/memories to capture, and there are standing **escape
hatches** ("skip", "later", "stop"). Sensitive edits get extra friction: the **core-character
guardrail** — *don't update core characters by default*; the Lead flags proposed changes,
and if approved the agent returns **additions only (never a rewrite), shown as a diff**, which
the Lead merges. References are validated before commit (flag a memory that points at a
non-existent character).

**Where it comes from.** `solorpg` `session-postprocess-v2` (Phases 3–4; the §4.5c core-character
guardrail). Reinforced per-campaign (rust-and-ruin's additive-only protection).

**Why it matters for next-gen.** A reusable stance: **automation drafts, the human commits**
— especially for irreversible or identity-bearing writes. The "additive-only + diff-before-write"
rule is a clean guardrail for any agent touching curated data. This is the *same shape* as
[[0021-data-required-as-prompt]] (halt and ask rather than fabricate) and as this project's own
[[appraisal-protocol]] (interview-first, don't anchor/auto-commit). Together they suggest a
framework-wide principle: **agents propose, gates dispose.**

**Open threads.** Gate fatigue — too many checkpoints stall flow; which writes are safe to
auto-commit? Can guardrails be *declared per data-type* (core vs. minor character) rather than
hardcoded? Relates to [[0029-information-boundary-enforcement]] (a gate that's currently
manual and should maybe be automatic).
