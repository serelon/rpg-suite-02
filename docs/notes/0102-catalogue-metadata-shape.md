---
tags:
  - kind/idea
  - source/conversation
  - theme/architecture
  - theme/single-source-of-truth
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-10
---

# Cataloguing KB entries: validated core + additive periphery (shape, not schema)

**What it is.** A *shape* for the metadata every knowledge-bank entry carries. Not a field
spec — the point of capturing now is the **organizing principles**, because the fear that
drove the conversation is "pick the wrong fields too late → too late to fix." (Research
altitude: shape only. Field-level detail is deferred to the design phase.)

**The reframe that dissolves most of the fear — two different fears, one fatal:**
1. *"Wrong schema"* — **not fatal** if the metadata model is **additive/extensible**
   (small mandatory core + open tags/keys you can grow). Matches this vault's own
   tags-are-truth philosophy. Adding a field later = start writing a key, no migration.
2. *"Didn't record a capture-time-only fact"* — **the fatal one.** Some facts exist only
   at the moment of capture and are unrecoverable later.

So the irreversible decision is narrow: not "all fields," but **which *field slots* must
exist at birth** (the lossy ones). Everything else can be added whenever.

**The master key: a provenance anchor makes most things backfillable.** If every entry
ties back to its source (**session** + real-world timestamp + stable id), an agent can
re-read the session later and extract characters/factions/location/dates. So enrichment is
deferrable; only the anchor is non-negotiable. ("Session added → you can always
backprocess.")

**Mandatory vs validated are orthogonal axes** (don't conflate). Mandatory = must be
present; validated = constrained to a controlled vocabulary. And **validation implies a
registry** — validating `faction` means maintaining a faction registry (≈ the
[[knowledge-base-canonical-vault]] project). Because the model is additive, **validation
can be phased in**: stamp a field loosely now, turn on validation when its registry
matures. The field *slot* is the irreversible part; its validation is not.

**The relational layer.** Entries also carry **cross-references / links to other entries**
(characters, locations, related facts) — the wikilink/graph layer. Whether those links
live at item or version level (see [[0103-bitemporal-subentry-versioning]]) is a
design-phase detail; that they're part of the shape is the point.

**Illustrative tiers (not prescriptive):** required core ≈ `id · campaign · kind ·
template-version` (+ per-version provenance, see 0103); validated-but-optional ≈ seal-level
(default *open* — so omission = exposure, sealing must be an active step,
[[0089-sealed-secrets-files]]/[[0098-vector-index-over-vault-not-store]]), status;
loose-until-registries-exist ≈ characters / faction / location / ingame-dates.
**`template-version`** is the keystone — it's what lets old entries be upgraded on read,
turning "figured it out too late" into "migrate selectively."

**Why it matters for next-gen.** Gets ahead of the one genuinely irreversible thing
(unstamped capture-time facts) while refusing to over-commit on schema. Directly serves
campaign isolation (`campaign` in the core), audit/provenance ([[0057-compiled-context-needs-audit-tooling]]),
and the canonical-vault program.

**Open threads.** Which fields truly earn validation (i.e. earn a maintained registry)?
Does the additive periphery attach at item or version level? Granularity of links. How the
capture workflow *prompts* for lossy/seal fields so they aren't forgotten.

**Confirmed by independent planning (2026-06-13).** The import design brief
([[import-design-brief]]) leans on exactly this anchor: UUID + `last_processed_dump` +
`embedding_ref` make re-import idempotent, and `rulings` (human decisions) are durable
metadata that survive every re-import — the "provenance anchor makes the rest backfillable"
claim, validated against a real 2-year corpus. Its routing edges
([[0108-multi-label-relational-routing]]) are the relational layer this note flagged.

**Verdict.** _(unevaluated.)_
