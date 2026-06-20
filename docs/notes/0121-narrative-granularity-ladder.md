---
tags:
  - kind/idea
  - source/conversation
  - theme/narrative-structure
  - maturity/proven
  - verdict/adopt
created: 2026-06-20
---

# The narrative granularity ladder — and why it isn't a clean tree

**What it is.** A model of the units of play, finest to coarsest:

```
update < scene < act? < session < arc? < season < campaign
```

- **update** — one back-and-forth between player and GM. The atom; contiguous.
- **scene** — a unit of place/situation. Contiguous. Mostly recognized retroactively, though
  some stories run proactively scene-by-scene.
- **act?** — a sub-session beat: when we want multiple acts organized under the **same session
  number**. Contiguous, lives *inside* one session.
- **session** — one sitting. The **load-bearing unit** and the only one reliably given a
  **global, monotonic number** (play-order). Historically also called **episode** (we ran a
  full TV metaphor in an earlier generation).
- **arc?** — a narrative movement grouping multiple sessions, smaller than a season, **within a
  single branch** (one POV line). A subdivision of the story shape — *not* the cross-cutting
  organizational axis (that's the **branch**; see below). On the global session counter an arc
  looks gappy, but only because *other branches* interleave between its sessions.
- **season** — a major division (contiguous span of play-order). See
  [[0122-compaction-boundary-descends]] for its origin.
- **campaign** — the world. Top.

**The key structural finding: it isn't a tree — a session is a point in THREE independent axes.**
The ladder above is only the *telling-order* spine. Two more axes sort the same numbered sessions:

| Axis | What it orders | Linear case |
|------|----------------|-------------|
| **Telling order** (session #) | when the table saw it | the spine — always monotonic |
| **Story time** (timeline) | when it happened in-world | sorts *with* telling order; jumps when non-linear |
| **Branch** (POV workspace) | which protagonist line it belongs to | a cross-cutting **organizational** axis; interleaves |

**Telling-order is the only always-monotonic axis.** The other two are free to scramble against it:

- **Branch** — a session is played within exactly one branch (one POV line), but branches
  **interleave** non-contiguously on the global session counter. Branch is an **organizational**
  axis, *not* narrative — see [[0123-branch-as-organizational-axis]]; the example below is the
  owner's:
  ```
  Season 1
  ├─ Branch A (POV X):  s1 ──── s3 ──────────── s7
  ├─ Branch B (POV Y):  ── s2 ──── s4 ── s6 ────
  └─ Branch C (POV Z):  ──────────── s5 [act i | act ii]
                        1   2   3   4   5   6   7   ← telling order
  ```
  (`arc` is a narrative subdivision *inside* a branch — e.g. Branch C's run could split into
  arcs — and is therefore **not** what interleaves here.)
- **Story time (timeline)** — *when events happen in-world*, tracked **regardless** of linearity
  (even a linear campaign carries in-world dates). **Linear:** timeline sorts with telling order
  (s01 = days 1–4, s02 = 5–8, s03 = 11–15 — gaps, never backward). **Non-linear** (the exception):
  telling order stays 01/02/03 but story-time jumps (s01 = day 80, s02 = day 1, s03 = day 50).

So everything `update`→`session` is **contiguous nesting in telling-order**; `branch` and
`timeline` are each a **separate sort** of the numbered sessions. The two *times* (telling vs
story) are the **bitemporal** shape ([[0103-bitemporal-subentry-versioning]]) at session
granularity; `branch` is a third, **organizational** cross-cut that lives in a different system
from the narrative ladder entirely (it must — see [[0123-branch-as-organizational-axis]]).

**Where it comes from.** Owner, 2026-06-20 ("random thoughts" capture). The interleaving example
(branches A/B/C splitting odd/even session numbers within one season) is the owner's own.
Branch mechanics corrected against solorpg's the-long-watch / pale-horizon multi-branch structure
(see [[0123-branch-as-organizational-axis]]) after an initial mis-read of branch as canon-versioning.

**Why it matters for next-gen.** First note to name the **temporal/narrative units themselves**
(the other ~120 notes are all data/context/tooling). Consequences:
- **arc wants to be a tag, not a folder** — directly the tags-over-folders principle in CLAUDE.md.
  (Branch, by contrast, *is* the folder in the source repos — because it's the organizational
  axis, not the narrative one. The two genuinely sit in different systems.)
- The units are **apply-when-earned annotations, not rigid containers**: act/arc are valid
  declared **either** ahead-of-time **or** retroactively; scene mostly retroactive. *Only*
  `session number` is reliably pre-declared (and usually drags a season with it).
- **Promotion case** (a tell): unnumbered **sidestories get promoted into the numbered
  sequence** — an off-axis thread pulled into play-order, becoming a "real" session
  retroactively. Same shape as the interleave.
- The vocabulary is **TV-register, historically layered** (episode→session, season), partly
  migrated to tabletop terms (session/campaign) across generations — a voice/register decision
  with a history; cf. [[0114-voice-vs-setting-fidelity]], [[0055-register-anchor-banks]].

**Open threads.** The **units are settled** (owner: this is foundation, not exception); only the
**storage/hierarchy shape is deferred** (and the interleaving makes any literal tree hard). Is
`season` strictly play-order-contiguous, or can an arc cross a season boundary? (Current rule:
season = contiguous play-order container; arc = a narrative subdivision within a branch.)
**Timeline** is folded in as the second sort-axis (story-time). **Branch** (the organizational
cross-cut) is split out to its own note — [[0123-branch-as-organizational-axis]] — because it
**must not be conflated with narrative structure**; that note also carries the keep-them-separate
principle.

> **Design note (three axes are *capacity*, not mandatory population).** Tracking telling-order,
> story-time, and branch independently is the **baseline that must not preclude complexity** —
> not an instruction to populate all three for every session. Linear/single-branch is the cheap
> default (timeline sorts with telling-order; one branch); the model just has to *express*
> divergence without re-architecting. (Guards against the [[0031-beware-transient-constraint-architecture]]
> / `E:\rpg` over-build trap.)

**Verdict.** **Adopt** — foundation, carry as-is. The granularity ladder + the two time-axes are
ratified by the owner as the settled baseline (units fixed, storage deferred). The three-axis
*capacity* (not mandatory population) is the next-gen stance. Branch handled in
[[0123-branch-as-organizational-axis]].
