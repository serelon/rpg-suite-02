---
tags:
  - kind/anti-pattern
  - source/conversation
  - source/solorpg
  - theme/context-economy
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-06
---

# Relational anchoring — the LLM describes the world as relatives of what's in context

**What it is.** The mechanism behind [[0078-zoom-out-first-worldbuilding]]'s
container-world failure, named (user, 2026-06-06): an LLM **pattern-matches onto whatever
already exists in context**, so during worldbuilding it will

> favor writing things as relatives (aka describe a place as "character a's favorite
> place!" rather than an evergreen description)

If a character is in context, every new location, faction, and event gets authored *in
relation to them* — and those relational descriptions then live in the primers as canon.
That's how character-first gravity bakes in and survives refactors: the bias isn't in the
structure, it's in the *prose of every entity written while the character was in context*.

**Current workaround (effortful, imperfect):** "ensure there's no unwanted context for the
llm to draw from" — i.e. workshop world material with the character deliberately *out* of
context. "Takes time and effort to workshop this out. not impossible, but hard to get
perfect." Note this is **context-exclusion as a creative tool** — the same instrument as
[[0052-evolution-vs-drift]]'s fresh-context drift detection, pointed at generation instead
of review.

**Why it matters for next-gen.** User: "this is something we need to nail down as an
anti-pattern." Implications worth carrying:
- Workshop tooling could make exclusion *cheap*: a "world-only mode" that loads setting
  context but withholds characters (the KB consumers of
  [[0069-one-knowledge-base-many-presentation-layers]] make selective loading natural).
- An **evergreen-description rule** for entity pages ([[0067-campaign-data-as-linked-vault]]):
  the page's base description must stand alone; relationships are expressed as *links/
  relationship entries*, never woven into the core prose. The custodian
  ([[0075-postprocessing-as-vault-librarian]]) could flag relational phrasing in base
  descriptions as a lint.
- This is also an argument for the two-trunk/lens split ([[0068-multi-lens-data]]):
  "character A loves this place" belongs in a *relationship* lens, not the place's trunk.

**Open threads.** Is relational anchoring detectable mechanically (descriptions containing
character names / possessives in base-description fields)? Does the same bias affect
post-processing (session summaries describing the world only through the POV's eyes — is
that fine there, since summaries *are* POV artifacts)? How does "no unwanted context"
interact with naming-is-permission ([[0048-canon-precedence-and-naming-is-permission]]) —
loading eagerly is the opposite instinct?

**Verdict.** _(unevaluated.)_
