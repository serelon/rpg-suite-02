---
tags:
  - kind/question
  - source/solorpg
  - source/rpg-tools
  - theme/architecture
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-04
---

# Datastruct census — locations barely used, story tool superseded-but-surviving

**What it is.** Two census facts about the data types, from the user (2026-06-04):
- **Locations** is "a datastruct we're barely utilizing" — it exists, tools support it,
  some campaigns have files, but it never became load-bearing the way characters did.
- **The story tool** is used by **exactly one campaign**, and is "more-or-less a different
  variant of memory — although it did come first." A predecessor that memories effectively
  superseded, still alive in its one niche.

Together with [[0050-built-never-used-inventory]] this sketches a maturity spectrum the
next-gen census needs: *built-never-used* (campaign.py) → *built-barely-used* (locations) →
*superseded-but-surviving* (stories) → *load-bearing* (characters, memories, savefiles).

**Where it comes from.** Light workshop bounce, while locating where hallucinated tags live
(answer: **memories, characters, probably locations** — that's the tag-study corpus for
[[0058-flag-lifecycle-set-at-build-select-at-prep]]).

**Why it matters for next-gen.** Don't port datastructs by existence — port by *load*.
Locations' underuse is a design question: is the structure wrong, or did play just never
need it (and would per-location axes in [[0047-multi-axis-data-management]] change that)?
Stories-vs-memories needs a merge-or-sunset decision rather than carrying both
([[0036-every-subsystem-is-a-module]]: one home per concern).

**Locations, answered (user, 2026-06-04):** "It's great, it's needed, but **we never
finished wiring the tooling** — at most we just read the .jsons." So a fifth point on the
spectrum: *wanted-but-half-wired*. The value is believed in; the integration debt killed
adoption. Next-gen lesson: a datastruct without finished workflow wiring decays to inert
JSON regardless of merit — shipping the type means shipping its pulls (what loads it, when,
into what).

**Open threads.** Which campaign uses stories, and does it use them for something
memories genuinely can't do ([[0026-exceptions-are-features]] test)? **Mining lead:** the
hallucinated-tag corpus (memories/characters/locations across campaigns) — study what
unconstrained tagging converged on before designing the vocabulary.

**Verdict.** _(unevaluated.)_
