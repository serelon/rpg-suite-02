---
tags:
  - kind/pattern
  - source/solorpg
  - theme/single-source-of-truth
  - theme/corpus-building
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-13
---

# Classification is multi-label & relational — typed edges, not folder assignment

**What it is.** From the import design brief ([[import-design-brief]]): when routing corpus
material (here, 1,201 exported conversations) to where it belongs, **don't assign one
folder — emit a *set* of typed edges.** A conversation can belong to two campaigns
(crossover), be the ancestor of one (seed), be a failed sibling of a success (variant), or
be meta-talk *about* a campaign rather than play. One path can't express that; a set of
relationships can.

**The edge vocabulary (illustrative):** `belongs-to`, `crossover-between [A,B]`,
`seed-of A/branch`, `variant-of <uuid>`, `about A`, `cluster <discovered-label>`,
`unrelated` (kept & labeled, not deleted). Each edge carries **confidence** *and*
**provenance-of-decision** (heuristic / embedding / model / human). The decision's origin
is metadata on the edge — so you know *why* a thing was filed where it was, and a human
ruling outranks a heuristic guess.

**Where it comes from.** `../solorpg/imports/IMPORT-DESIGN-BRIEF.md`, "Classification is
multi-label & relational" + the edge-type table. The user's own pre-planning.

**Why it matters for next-gen.** This is the vault's **"tags are source of truth, folders
are convenience"** doctrine applied to *routing*, and it's the concrete realization of the
cross-reference/links layer flagged in [[0102-catalogue-metadata-shape]]. A single-folder
importer would be lossy by construction — it would discard exactly the crossover/seed/
variant structure that's most interesting ([[0111-provenance-graph-as-secret-history]]).
**Provenance-of-decision on each edge** is the sharp, reusable idea: it generalizes to any
agent-made classification in the toolchain (precedence: human > model > embedding >
heuristic), and serves the audit imperative ([[0057-compiled-context-needs-audit-tooling]]).

**Open threads.** Is the edge set its own graph store, or just metadata fields on the
entry ([[0102-catalogue-metadata-shape]])? How do edges interact with the bitemporal model
([[0103-bitemporal-subentry-versioning]]) — can an edge itself be versioned/retconned (a
conversation reclassified later)? Shared vocabulary between *import routing* and *in-play
linking*, or two different edge taxonomies?

**Verdict.** _(unevaluated.)_
