---
tags:
  - kind/question
  - source/rpg-tools
  - theme/architecture
  - maturity/speculative
  - verdict/adopt
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

**The why, answered (2026-06-05).** The user drifted away from campaign.py's underlying
approach right after building it: it was (probably) made for the brief era when
autocompaction in Claude Desktop made "track a whole multi-session campaign in one Desktop
thread" look viable — which "turned out to work soso anyway (it keeps *everything* in
memory... you run out of ram long before this pays off)". So campaign.py is a **textbook
[[0031-beware-transient-constraint-architecture]] specimen**: architecture built around a
model-era constraint that evaporated. User: "not even sure what it does anymore."

**Open threads.** **Mining lead:** sweep rpg-tools for other built-never-used features
(candidates: log.py event system? changelog tiers? convergence points?) and mark each
note's maturity honestly. Related: [[0047-multi-axis-data-management]],
[[0043-campaigns-as-testbeds]].

**Verdict.** **Adopt the lesson, reject campaign.py itself** (appraised 2026-06-05).
Maturity tags must distinguish shipped-and-used from shipped-and-dormant — stands. The
artifact is doubly damned: never play-tested *and* built for a vanished constraint. Its
convergence-points idea earns no seat unless it resurfaces somewhere proven.
