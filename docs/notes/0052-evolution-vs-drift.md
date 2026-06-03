---
tags:
  - kind/idea
  - source/solorpg
  - theme/single-source-of-truth
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# Evolution vs drift — curation gates exist to tell legitimate growth from corruption

**What it is.** Two opposite movements look identical from inside a session: **evolution**
(play legitimately grows past the seed — savefile/character JSON then outrank the primer,
per [[0048-canon-precedence-and-naming-is-permission]]) and **drift** (play accidentally
diverges from truth — small missed details, which get **retconned back into primer canon**).
Drift is dangerous at scale: (user) "can lose whole settings or characters to that."
The defense: **evolution is heavily curated** — that's *why* the "ridiculous" machinery
exists (PRs on post-processing flows, draft→review→adjust→write,
[[0028-checkpointed-human-gates]], [[0035-surgical-git-staging]]). The gates aren't generic
quality control; they're **canon defense** — only curated changes count as evolution,
everything uncurated is presumed drift.

**Where it comes from.** User, during light workshop exchange (2026-06-03), explaining why
mid-session patches that contradict table-speech usually win ([[0051-live-context-delta]]'s
contradiction thread, answered).

**Why it matters for next-gen.** Canon precedence (0048) is incomplete without this: the
ordering "savefile > primer" only holds for *curated* state. The spec needs the distinction
explicit — something like: canon = seed + sum of gated changes; anything else is drift to be
retconned. Currently only the user can tell evolution from drift; a system that knows which
changes passed a gate could at least flag the unattested ones.

**Drift detection — already half-proven.** User wants suspected drift *surfaced at debrief*
("fits the workflow"). The trap: a drifted session can't judge its own drift — countering
context-rot with a rotted context. The answer shape already exists: **fresh context as the
instrument** — post-processing agents spin up clean, load canon, read the transcript as
foreign material. And in fact they *already catch drift incidentally, fairly often* today.
The design move is promoting that side-effect to an explicit debrief output (recap-as-
verification pointed at canon, [[0017-recap-as-verification]]).

**Lineage evidence.** Tarot Tales-era campaigns (gen 2/3) "used to go haywire *fast* — just
not enough static anchors, or working frameworks." Drift rate fell as the anchor machinery
(primers, savefiles, gates) arrived. Anchors are empirically what tamed drift.

**Open threads.** What does the explicit drift-check load — full compiled context
([[0044-scenario-compiler]]) or canon-critical subset? False-positive cost: how is
"divergence" presented so legitimate evolution isn't nagged? Relates to
[[0015-compounding-loops]] and [[0029-information-boundary-enforcement]].

**Verdict.** _(unevaluated.)_
