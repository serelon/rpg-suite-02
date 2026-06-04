---
tags:
  - kind/pattern
  - source/solorpg
  - theme/composition
  - theme/context-economy
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-04
---

# Portable bundles — away-from-repo play is first-class, and it forces two delivery modes

**What it is.** (User, countering the extract-on-demand insight of
[[0062-conversation-transcripts-as-gm-context]]:) **bundles must be portable** — "can't
always expect me to have access to the datastore repo and the Claude Code workflows. I use
Claude Desktop/web/mobile so I can play on my phone when far from home." When away, the
bundle zip is the *entire available world*: no JIT reads, no retroactive extraction, no
agentic tooling against the repo.

**Where it comes from.** Live solorpg practice — the whole bundle/zip workflow exists for
this. Surfaced 2026-06-04 as a check on at-home-only design thinking.

**Why it matters for next-gen.** It hard-splits the delivery question:
- **At home (Claude Code + repo):** JIT loading ([[0060-jit-loading-retry]]), runtime
  composition ([[0045-runtime-composition-briefing-py]]), on-demand re-extraction — all live.
- **Away (Desktop/web/mobile):** only what the compiler baked in exists. Anything plausibly
  needed mid-session must be **predicted at compile time** — so the selection problem 0062
  "dissolved" comes back for away-play, and tag-based selection
  ([[0058-flag-lifecycle-set-at-build-select-at-prep]]) does real work there.

So the scenario compiler ([[0044-scenario-compiler]]) needs *target profiles*: same
sources, two builds — a thin manifest-y build for at-home (resolve live) and a fat
self-contained build for away. This is [[0004-frontend-agnostic-core]] with teeth: frontends
differ not just in surface but in *capability class* (repo-attached vs artifact-only).

**Open threads.** Is capability-class detectable/declared per frontend in the spec? Does
away-play state (savefile written on phone) sync back through a gate
([[0028-checkpointed-human-gates]])? How fat can a fat build get before context economy
breaks ([[0001-tiered-progressive-loading]] inside the bundle)?

**Verdict.** _(unevaluated.)_
