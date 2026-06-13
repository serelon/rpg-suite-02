---
tags:
  - kind/idea
  - source/conversation
  - theme/architecture
  - theme/data-driven
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-10
---

# Bitemporal subentries: an item holds versioned, provenanced fact-slices

**What it is (shape, not schema).** A KB item is a **stable identity container**; the
actual facts live in **subentries** — each a time-stamped, provenanced *version* of the
data. Same item, many subentries with different timestamps. The user reached this
independently; it's the well-trodden **bitemporal + slowly-changing-dimension (Type 2)**
pattern, which is a good sign it's the right shape and that proven solutions exist to
borrow.

**Two independent time axes — must not be collapsed:**
- **Transaction time** — real-world "when we recorded it" (session + timestamp). The
  audit axis.
- **Valid time** — in-world "when the fact is true" (`authored-at`, plus a validity
  interval `valid-from`/`valid-until`).

Subentries = versions along these axes.

**What it buys, for free:**
- **Time-travel queries** — "what was true *as of* in-world date D" resolves to the right
  subentry. Built for time-travel campaigns, useful for any (retcon, memory drift,
  "what did they know then").
- **A changelog** — the subentry sequence *is* the edit history, each slice traceable to
  the session that produced it. Reprocess a session → know exactly which subentries it
  touched (backprocessing).

**The one distinction to preserve:** a fact can change for two different reasons, and a
naive changelog conflates them —
1. **It genuinely changed in-world** (king died → new ruler; both versions true at
   different valid-times) — ordinary versioning.
2. **We were wrong / history was rewritten** (the old version was *never* true) — a
   correction/retcon along transaction-time.
Tag which it is, or queries get confused. Connects to the retcon/`supersedes` idea and
E:\rpg's branch-versioning.

**The split it implies — provenance lives with the version, not the item:**
- **Item level (immutable identity):** `id · campaign · kind · template-version`.
- **Subentry level (per version, provenanced):** session/slice, real-world timestamp,
  `authored-at`, content, validity interval, seal-level (a secret's secrecy can itself
  change → the reveal is a new subentry), change-type tag.
The item's "created" is just its earliest subentry.

**Why it matters for next-gen.** A single mechanism delivers history, audit, retcon, and
time-travel without bolting on separate systems — and makes the catalogue
([[0102-catalogue-metadata-shape]]) coherent (most metadata is per-version, not per-item).
Strong ties to fog-of-war as data ([[0071-fog-of-war-as-data-structure]]), sealed secrets
([[0089-sealed-secrets-files]]), the canonical vault ([[knowledge-base-canonical-vault]]),
and the vector-index read path ([[0098-vector-index-over-vault-not-store]], which must
resolve "current truth" across subentries).

**Open threads (design-phase, deferred).** How **branches** sit against subentries —
another axis keyed `(branch, valid-time)`, or a fork of the whole item? Time travel can
itself *spawn* a branch, smearing the line. What granularity warrants a new subentry vs an
in-place fix (else the changelog is noise). Read-path cost of collapsing subentries to
"current" on every query.

**Confirmed by independent planning (2026-06-13).** The import design brief
([[import-design-brief]]) reaches the same spine from the data-engineering side: **UUID is
the stable primary key; every stage merges, never rebuilds; re-import diffs by UUID
(new / grew / unchanged) and human `rulings` persist against the UUID, never
re-adjudicated.** That's this note's item-identity + versioned-payload split, plus an
idempotency rule (don't reprocess unchanged versions) worth importing here. Treat re-import
as the *normal* case, not an edge case — the recurring-not-one-shot constraint.

**Verdict.** _(unevaluated.)_
