---
tags:
  - kind/question
  - source/aegis-tools
  - theme/architecture
  - maturity/proven
  - verdict/unevaluated
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
invisible *even to the person doing it*, for the system's whole lifetime, until a research
sweep happened to diff code against data. Silent tolerance doesn't just permit drift, it
**hides** it. This hardens the case for validate-loudly: the cost of a warning is small;
the cost of years of invisible divergence is that nobody can trust the schema docs at all.

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

**Verdict.** _(unevaluated.)_
