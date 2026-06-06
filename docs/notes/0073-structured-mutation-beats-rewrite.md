---
tags:
  - kind/principle
  - source/solorpg
  - source/aegis-tools
  - theme/single-source-of-truth
  - maturity/proven
  - verdict/adopt
created: 2026-06-05
---

# Structured mutation beats rewrite — regeneration is where drift gets in

**What it is.** Why the threads tracker ([[0070-threads-tracker-design]]) earned trust
while savefiles ([[0061-continuity-artifacts-under-suspicion]]) didn't, confirmed by the
user: threads are **append-and-transition** — add a timestamped note, flip a state, never
rewrite the record — while savefiles get **regenerated wholesale** each update. User:

> i've always had to fight the rewrite when prompting for savefiles. fighting drifts. …
> rewrite looses data, thats bad. can cause critical drift. proper housekeeping and
> structured mutation works better

Same mechanism as the postprocessor rewriting verbatim scenes
([[0054-verbatim-capture-lost-intent]]): any step where a model *re-emits* existing
content is a drift aperture. Structured mutation (append, toggle, patch a named field)
keeps the existing bytes untouched.

**Where it comes from.** User interview after the aegis mine (2026-06-05). **Mining
lead:** "there's a few files with old prompts somewhere, back when i did the housekeeping
by cut'n'pasting those" — find the old savefile-housekeeping prompts; they're the fossil
record of fighting the rewrite.

**Why it matters for next-gen.** A spec-level rule candidate: **continuity artifacts must
be mutated through operations, not regenerated** — the toolchain should offer
append/transition/patch primitives so the model never has to re-emit a whole file to
change one fact. Dovetails with [[0051-live-context-delta]] (deltas, not reloads) and
explains what "proper housekeeping" means: compaction is a *separate, deliberate* step
(with review, like the postprocessing PRs in [[0052-evolution-vs-drift]]) — never a side
effect of an update.

**Open threads.** What are the mutation primitives for prose (notes-append is easy;
what's "patch" for a narrative summary)? Does the savefile survive at all, or does it
dissolve into structured-mutation artifacts (threads-like state + memories)? Find the old
cut'n'paste housekeeping prompts.

**Verdict.** **Adopt — as a hard rule** (appraised 2026-06-06). "rewritten is how we get
extreme drift… likely still [drifts] with opus 4.8. we want as subtle and as atomic edits
as possible." Spec phrasing from the user: **unless specifically audited, never change the
wording or data context of files — only datastructs** (e.g. migrating one JSON schema to
another is fine; the content riding in it is untouchable). Wording changes require an
explicit audited pass; they never happen as a side effect.
