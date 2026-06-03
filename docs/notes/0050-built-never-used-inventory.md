---
tags:
  - kind/question
  - source/rpg-tools
  - theme/architecture
  - maturity/speculative
  - verdict/unevaluated
created: 2026-06-03
---

# Built-but-never-used — rpg-tools contains untested patterns; inventory them before adopting

**What it is.** `campaign.py` (campaign init, flat branch array with convergence points,
changelog tracking, export/import) was **built and never used** — "completely untested" (user).
Its branch/convergence model therefore has *zero* play-proof, unlike The Silence's
nested-folders model which is battle-tested. The user suspects **several more rpg-tools
patterns share this fate**: designed, implemented, never exercised.

**Where it comes from.** User disclosure during appraisal interview (2026-06-03), triggered
by the two-branch-models question. `rpg-tools/scripts/campaign.py`, `log.py`,
`references/campaign-state-guide.md` document the untested system in detail.

**Why it matters for next-gen.** `maturity/` tags must distinguish *shipped-and-used* from
*shipped-and-dormant* — a detailed guide + working code can look "proven" while having zero
play-hours. Adopting an untested pattern on the strength of its documentation would repeat
the original mistake at higher stakes.

**Open threads.** **Mining lead:** sweep rpg-tools for other built-never-used features
(candidates: log.py event system? changelog tiers? convergence points?) and mark each
note's maturity honestly. Also: *why* did campaign.py go unused — wrong abstraction, wrong
era, or just never needed? The answer is itself a design datum. Related:
[[0047-multi-axis-data-management]], [[0043-campaigns-as-testbeds]].

**Verdict.** _(unevaluated — appraisal owed, parked 2026-06-03 at user's request.)_
