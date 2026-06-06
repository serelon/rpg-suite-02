---
tags:
  - kind/question
  - source/solorpg
  - theme/single-source-of-truth
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-04
---

# Continuity artifacts under suspicion — summaries and savefiles work, but aren't trusted

**What it is.** The two most load-bearing continuity artifacts are both under the user's
quiet suspicion, despite universal use:
- **Session summaries** (every campaign): recurring format doubt — "that keeps being one of
  those 'what's a useful format here, likely not *this*.'"
- **Savefiles**: "we have a savefile. and I'm not sure that's the ideal way of storing
  state either. I'm not sure how well-tuned the structure is, and I'm worried there's the
  **wrong kind of datadrift**."

Note the asymmetry with [[0059-datastruct-census-underused-and-superseded]]: those are
underused-but-believed-in; these are **used-everywhere-but-doubted**. Highest stakes,
because everything downstream (canon precedence [[0048-canon-precedence-and-naming-is-permission]],
recap verification [[0017-recap-as-verification]]) treats the savefile as truth.

**Where it comes from.** Light workshop bounce (2026-06-04), while untangling story tool
vs summaries.

**Why it matters for next-gen.** If the savefile is canon's top-ranked source *and* its
structure invites drift, that's drift at the root of the trust chain
([[0052-evolution-vs-drift]] — the gates defend changes *into* the savefile, but nothing
audits whether the savefile's *shape* makes the right things land in the right places).
The summary-format doubt connects to [[0030-summary-as-compression]]'s test ("will it
matter in 10 sessions?") — the *criterion* is trusted, the *format* isn't. Next-gen
shouldn't port either format by momentum; both are redesign candidates with years of
corpus to study.

**Open threads.** What is the "wrong kind" of datadrift in savefiles — structure rot
(fields accreting per-campaign), semantic rot (same field meaning different things over
time), or state leaking into places that should be development-tier (cf. rpg-tools'
tiered mutability)? **Mining lead:** diff early vs late savefiles of a long campaign and
look at what the structure did under pressure. Same study for summary formats across
campaigns ([[0027-recurring-exception-taxonomy]] angle: did campaigns fork the format?).

**Amended (user, pillar-1 review 2026-06-06): the savefile doubt was overstated.** "the
savefile format as is now is actually fairly mature, the issues are in the details, in
the **guidelines for capture** (they need tuning), and for **maintaining**." So the
format survives; the redesign target is capture guidance + maintenance practice. And
savefile-as-knowledge-entry ([[0085-knowledge-entries-vs-tool-data]]) is a **growth
play**, not a rescue: "having the core subsections of the savefile.jsons be subsections
in a potentially much larger page … means the loremaster can track *alot* more data —
a full history section, a full changelog, etc." The summary-format doubt stands
unchanged.

**Verdict.** _(unevaluated — summary half still owes its appraisal; savefile half
reframed above.)_
