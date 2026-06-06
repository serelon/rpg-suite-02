---
tags:
  - kind/question
  - source/aegis-tools
  - theme/architecture
  - maturity/proven
  - verdict/undecided
created: 2026-06-05
---

# Schema drift — the hand-edited JSON won, and the tools didn't fight back

**What it is.** The aegis sweep found the *live campaign data* has drifted from the CLI
code's expected schemas: threads stored as a dict-keyed-by-slug where `load_threads()`
defaults to an array + `nextId`; tech grew a `vault` category the code doesn't know;
enemies file shape diverged (`unknowns` field, array vs dict). The user edited JSON
directly past what the tools defined — and the tools, being load-merge-save permissive,
tolerated it. **The systems the user remembers as "worked really well" are the ones whose
data was human-edited beyond the code.**

**Where it comes from.** Diff between `lib/io.py` default schemas and live
`solorpg/campaigns/aegis/{data,intel}/*.json` (Explore sweep 2026-06-05).

**Key data point (user, same day): the drift was unconscious.** "honestly..havent actually
noticed that until now. huh" — the tools tolerated the divergence silently, so it was
invisible *even to the person doing it*, for the system's whole lifetime — which was only
**a few weeks to a month, mostly coding sessions rather than play** — until a research
sweep happened to diff code against data. That short a window makes it *worse*, not
better: the data diverged from the code almost immediately, while the system was being
actively built. Silent tolerance doesn't just permit drift, it **hides** it. Hardens the
case for validate-loudly: a warning is cheap; invisible divergence means nobody can trust
the schema docs at all.

**Why it matters for next-gen.** A genuine design tension to settle, because the repo
holds both poles:
- aegis's *philosophy* is rules-as-code, validation-at-write
  ([[0070-threads-tracker-design]], [[0071-fog-of-war-as-data-structure]] — and those
  whitelists demonstrably kept data clean)…
- …yet its *practice* shows the human routing around the tools when the shape stopped
  fitting, and that flexibility being part of why the system felt good.

For the canonical vault ([[0067-campaign-data-as-linked-vault]]) this is sharp: if the KB
is the source of truth and many tools cherrypick from it ([[0069-one-knowledge-base-many-presentation-layers]]),
hand-edits that drift from the expected shape either (a) break every consumer, or (b) get
silently ignored — both bad. Candidate stance: **validate loudly, fail softly** — consumers
warn on unknown shapes instead of erroring or ignoring, and migration helpers (not
rejection) absorb drift. The audit tooling of [[0057-compiled-context-needs-audit-tooling]]
is where drift would surface.

**Open threads.** Is the drift here *evolution* or *drift* in [[0052-evolution-vs-drift]]'s
terms — the dict-by-slug threads shape is arguably *better* than the coded array (it
matches [[0070-threads-tracker-design]]'s semantic-slug principle!), it just never got
folded back into the code. That's the same failure as [[0046-campaign-lifecycle-geological-strata]]:
improvements made in the data layer with no path back to the tool layer. Does next-gen
need a "schema PR" loop — when the human outgrows the schema, the schema follows?

**Verdict.** **Undecided — cause unknown** (appraised 2026-06-06). The user can't
reconstruct why the diff exists: "if its tool-worked data, there shouldnt be [a diff],
those are supposed to be tool-first. if its hidden metadata, that the tool just doesnt
see, then thats a trick we've used before (used to hide metadata in namesets before we
made that a canon approach)." So the divergence is either a genuine anomaly or a
deliberate-but-forgotten hidden-metadata move. **Mining lead:** check the aegis data's git
history — did the off-schema shapes (threads-as-dict, tech `vault`) arrive via hand edits,
tool versions that changed, or intentional metadata smuggling? The validate-loudly stance
waits on that answer. (Side capture: *hidden metadata in namesets, later canonized* is
itself an instance of informal-trick-graduates-to-canon-approach — the [[0043-campaigns-as-testbeds]]
graduation path working.)
