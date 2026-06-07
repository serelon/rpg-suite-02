---
tags:
  - kind/principle
  - source/conversation
  - theme/architecture
  - theme/campaign-isolation
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-07
---

# Enforcement strength matches failure reversibility

**What it is.** A decision rule reconciling two stances taken days apart.
[[0091-one-vault-campaign-folder-entrypoints]] accepted campaign-to-campaign boundaries
enforced *by tool* (soft: conventions + a guard that can in principle be bypassed).
[[0095-two-repo-public-private-split]] insists the public/private boundary be
*structural* (hard: data physically in a different, nested repo that git cannot see).
The reconciling rule: **match the enforcement mechanism to the cost and reversibility of
the failure it prevents.**

- **Campaign bleed** (lore leaking between campaigns): recoverable and cosmetic — edit
  the offending page, redo the update. Tool-enforced boundaries are proportionate;
  structural separation (separate vaults) was rejected there for good reasons.
- **Public leak** (private data pushed to a public repo): irreversible — push =
  published, assume scraped the moment it lands. Demands structural separation;
  procedural discipline ("remember which remote") is not acceptable as the only line.

**Why it matters for next-gen.** Gives future boundary decisions a rule instead of two
unconnected precedents: ask "what does failure cost, and can we undo it?" before picking
between convention, tool-guard, hook/CI gate, or physical separation. The ladder:
discipline → tool-enforced → mechanically gated → structurally impossible; climb it as
reversibility drops. Also explains the layering in 0095: structural split (irreversible
failure) day-1, denylist hooks and audit gates (defense in depth for the same failure)
deferable machinery.

**Open threads.** Where do *sealed secrets* ([[0089-sealed-secrets-files]]) sit on the
ladder? Premature reveal is semi-irreversible (the twist is spoiled for that campaign) —
arguably deserves more than the GM's judgment, supporting 0089's hook-based unlock-check
thread. Are there other boundaries in the system worth re-grading with this rule
(player-display artifacts [[0088-player-display-artifacts]], info-boundaries
[[0029-information-boundary-enforcement]])?

**Verdict.** _(unevaluated.)_
