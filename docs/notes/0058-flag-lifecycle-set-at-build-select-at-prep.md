---
tags:
  - kind/idea
  - source/new
  - theme/composition
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-04
---

# Flag lifecycle — tag when content is built, select at session prep; both hands on it

**What it is.** (User:) flags/tags are set by **both user and Claude**, across **multiple
stages**: tagging happens *when content is built* (during workshops, post-processing),
selection happens *during session prep*. Two distinct operations on the same vocabulary —
write-side tagging and read-side selection — separated in time and often in actor.
The acknowledged hard part: "we need to be much smarter about how to set flags. which is
gonna be tricky."

**Where it comes from.** User, morning workshop bounce (2026-06-04), answering "who sets
the flags?" for [[0056-files-as-build-products]].

**Why it matters for next-gen.** The whole compiled-files idea stands or falls on tag
*quality at write time* — selection can only be as good as the tagging was. This makes the
tag vocabulary a spec-level concern ([[0041-self-evolving-versioned-spec]]): freeform
per-campaign tags will fragment ([[0003-scope-memories-to-context]]'s soup problem, but for
metadata), while a rigid global taxonomy will fight campaign weirdness
([[0026-exceptions-are-features]]). Note this vault's own convention — hierarchical tags,
controlled prefixes, freedom below — is one working compromise, in live use one repo over.

**Already-failed baseline (user, 2026-06-04).** The naive version exists today and doesn't
work: instructions say "add tags!", "the model will hallucinate whatever, and the end result
is not very useful." Unconstrained tagging is *empirically* dead — whatever the next-gen
answer is, it isn't "ask the model to tag freely." A schema/vocabulary the tagger must pick
from (with a gated path for proposing new terms) is the minimum viable correction.

**The unresolved axis (named, not answered).** Do tags describe what content *is*
("combat", "camp", "solace-pov") or when it should *load* ("always", "fights-only")?
Is-tags demand a smart selector; load-tags demand the tagger predict the future. User:
"honestly, not sure — this is something we *have* to figure out." Likely a spec-design
work-item, not a mining question.

**Open threads.** Can post-processing *propose* tags with the user gating them
([[0028-checkpointed-human-gates]])? Does drift apply to tags too — stale flags as a decay
mode ([[0052-evolution-vs-drift]])? Selection-side smartness: how much can the savefile
auto-derive ("where the story is" → active tags) vs. explicit prep-time declaration?

**Verdict.** _(unevaluated.)_
