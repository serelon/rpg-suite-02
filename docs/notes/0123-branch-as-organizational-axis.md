---
tags:
  - kind/principle
  - source/solorpg
  - theme/narrative-structure
  - theme/data-model
  - maturity/proven
  - verdict/adopt
created: 2026-06-20
---

# Branch is the organizational POV axis — keep it separate from narrative structure

**What it is.** A **branch** is a parallel **protagonist/POV workspace** inside *one shared world
and one shared timeline* — **not** an alternate-canon fork. The Long Watch runs Val, Lyra, David,
Rosa, Carmen, Sophie, Thalia, Mitchi… as branches of the *same* campaign, sharing one global
session counter and one continuity. A branch is an **organizational / context-assembly** unit; it
is **not** part of the narrative ladder (update→scene→act→session→arc→season→campaign,
[[0121-narrative-granularity-ladder]]). The two **must be tracked separately** — conflating them
breaks things (owner, hard rule).

**Where it comes from.** solorpg, mined 2026-06-20:
- `campaigns/the-long-watch/CLAUDE.md` — explicit **multi-branch structure**: a table of
  `Branch | Character | Focus`, branches running *in parallel*.
- `campaigns/pale-horizon/branches/kailani/` — a branch is a **folder** owning its own
  `CLAUDE.md`, `savefiles/`, `bundles/`, `bundle-template.json`, `reference/`, `characters/`,
  `sessions/`, `arc-1-tala-moana-*`.

What the source proves about branch (each point is why it ≠ arc):
- **It's a workspace, not a story shape.** A branch owns *what loads when you play this POV*:
  savefiles, bundle templates, branch-local reference/characters. That's filing + context
  assembly ([[0001-tiered-progressive-loading]], [[0039-bundle-template-composition]]), not plot.
- **It nests for *state* reasons, not narrative ones.** `Leviathan` (parent) holds
  **ship/fleet-level** savefiles; Val/Lyra/David are **sub-branches** with character-level
  savefiles. The parent isn't a "story" — it's a **shared-state container** so multiple POVs
  share the fleet ledger/mission save. Two savefile tiers (mission/fleet vs character) map to
  *nothing* in the narrative ladder.
- **Branches share one timeline and interleave** on the global session counter (Kailani = s01–03
  then s06+, because "sessions 04–05 belong to other branches"). This is the interleaving in
  0121 — it's **branch** interleaving, not arc.
- **Arc lives *inside* a branch** (`arc-1-tala-moana` = Kailani sessions 06+). So arc is a
  narrative subdivision of one branch's run; branch is the organizational container around it.
- **Cross-branch events + shared NPCs** are explicit: branches affect each other, the same NPC
  appears in several. (More evidence they're lenses on one canon, not separate canons.)

**Why it matters for next-gen.** Branch and arc *correlate* ("an arc belongs to one branch") and
both sound like "a character's storyline" — which is exactly why they're easy to conflate and why
the owner found the distinction hard to articulate. But they live in **different systems**:

> **Principle: organization (branch / sub-branch) and narrative structure (arc / season / …) are
> separate axes, tracked separately.** Branch = *how material is filed and assembled* (the folder,
> the savefile tiers, the bundle). Arc = *story shape*. They are not the same; treating them as one
> risks breakage — e.g. forcing the branch hierarchy to carry narrative meaning, or making arcs own
> savefiles. The Leviathan parent (a pure shared-state container with no story of its own) is the
> proof the two can't be merged.

Corollary to **tags-over-folders**: arc wants to be a **tag** (re-labelable, retroactive), whereas
branch legitimately **is the folder** in the source — because it's the organizational axis. So the
"folders are convenience" caveat has a real exception here: the branch folder is load-bearing for
bundling/state, not just convenience.

**Open threads.** Next-gen mechanics: do sub-branches stay a folder tree, or become a
relation/tag ([[0108-multi-label-relational-routing]])? How are the **two savefile tiers**
(shared parent-state vs per-POV state) modeled when state stops being flat files
([[0073-structured-mutation-beats-rewrite]], [[0094-save-everything-deferred-compute]])? How do
**cross-branch events** get represented without duplicating state across branches? Relates to
campaign-isolation vs within-campaign POV-isolation ([[0091-one-vault-campaign-folder-entrypoints]],
[[0029-information-boundary-enforcement]]).

**Verdict.** **Adopt** — proven in solorpg's multi-branch campaigns; the branch/arc separation is
a hard next-gen requirement (organization ≠ narrative). The *mechanics* of nesting and the
two-tier savefile model are the design deltas to carry forward, not re-decide.
