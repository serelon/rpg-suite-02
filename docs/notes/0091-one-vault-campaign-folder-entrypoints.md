---
tags:
  - kind/decision
  - source/new
  - source/solorpg
  - theme/architecture
  - theme/campaign-isolation
  - maturity/seed
  - verdict/adopt
created: 2026-06-06
appraised: 2026-06-06
---

# One vault, campaign-folder entrypoints, tool-enforced boundaries

**What it is.** The campaign-isolation structural decision (user, 2026-06-06), closing
the question deferred in [[0003-scope-memories-to-context]],
[[0029-information-boundary-enforcement]], [[0040-vector-db-as-lore-search-module]] and
the [[knowledge-base-canonical-vault]] appraisal:

> "one big vault with campaign folders. similar to how solorpg has a campaigns folder
> with campaigns/[campaignname]/ as subfolders … but **entrypoint is that campaign
> folder. boundary-enforcement will have to happen via tool.**"

So isolation is **operational, not physical**: one repo/vault; `campaigns/<name>/` is
the only thing a session gets pointed at; tooling polices reads and writes across the
boundary. Mirrors solorpg's proven layout.

**Why it matters for next-gen.**
- Campaign isolation and information boundaries ([[0029-information-boundary-enforcement]])
  become **the same tool problem** — one guard, two duties (cross-campaign leakage and
  cross-POV/branch leakage differ only in where the fence is drawn).
- Cross-campaign shared material (settings shared by branches/subsettings, shared tool
  data) lives *above* the campaign folders in the same tree — reachable by the compiler
  ([[0044-scenario-compiler]]) at build time, outside the session's entrypoint at play
  time.
- One vault keeps the graph whole for the human (Obsidian browsing, cross-campaign
  archaeology) while sessions see only their slice — the same read-scoping move as
  [[0089-sealed-secrets-files]], applied at campaign granularity.

**Open threads.** What does the enforcement tool actually check — read paths, write
paths, or compiled-bundle contents ([[0057-compiled-context-needs-audit-tooling]]'s
manifest is the natural audit point)? How do shared-setting writes get gated when two
campaigns disagree? Does the lore-search module ([[0040-vector-db-as-lore-search-module]])
index per-campaign or globally-with-scope-filters?

**Verdict.** adopt — user decision, recorded from the pillar-1 review session 2026-06-06.
