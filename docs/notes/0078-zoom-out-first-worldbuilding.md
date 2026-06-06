---
tags:
  - kind/principle
  - source/conversation
  - source/solorpg
  - theme/architecture
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-06
---

# Zoom out first — suggested worldbuilding order, and the container-world failure mode

**What it is.** Worldbuilding/campaign-setup flow doctrine (user, 2026-06-06). The process
must be doable **in any order** ([[0046-campaign-lifecycle-geological-strata]]'s
asynchronous, seed-heterogeneous entry stands) — but there is a **suggested optimal
order**: *broad strokes first, details later; write down at big checkpoints.* Concretely:
world as a whole → zoom in → zoom in → **first pov character last**.

Terminology is deliberate: "**first pov character**", not "main protagonist" — "there's no
guarantee this'll be the only one, or a protagonist." (Matches the branch/protagonist
multiplicity of [[0047-multi-axis-data-management]].)

**Suggested, never enforced.** Sometimes the seed *is* "i have this weird character
concept!" or "an idea for <thing that could exist in a world>" — then you start at another
phase. The flow is a gradient to return to, not a gate.

**The key insight — and it has empirical teeth:** start zoomed out, *"or we risk building
the world as a container for a character rather than a well rounded place for anyone."*
Observed in the wild: campaigns that started character-first carry noticeable weighting
**even after refactors** — Lumina City is one; Emberfall started with Xel-iri "and now has
like 6 branches." Character-first gravity persists through structural rework; it's not
cosmetic, it's load-bearing bias baked into the world's shape.

**Why it matters for next-gen.** Whatever the shared campaign-setup spec becomes
([[0046]]'s one-spec-many-entrypoints), it should *know* the suggested order and the
checkpoint-write rhythm — entrypoints can nudge toward zooming out ("before we detail her,
what's the world she's unfair to?") without blocking character-first seeds. The
container-world risk is the *reason* for the nudge, and it's worth surfacing to the user
during workshops, not silently enforcing. Checkpoint writes pair with the disposable/
permanent primer tiers ([[0049-disposable-bootstrap-primer]]).

**Follow-ups answered (user, same day).** De-weighting a character-first start is "very
hard" — the mechanism is [[0079-relational-anchoring-antipattern]] (the LLM writes
everything as relatives of in-context material); workaround is excluding the character
from context while building world material, effortful and imperfect. And Emberfall's
6 branches aren't a correction *or* an expression of Xel-iri gravity — it's simply the
user's one fantasy setting with many characters being started in it; but "original primer
was very much keyed for xel-iris branch," so the weighting sits in the *primer*, not the
branch spread.

**Open threads.** What are the "big checkpoints" exactly — do they map to the three
primers ([[0048-canon-precedence-and-naming-is-permission]])? Does a primer "keyed for"
one branch need a de-keying pass when a setting goes multi-branch (Emberfall as the test
case)?

**Verdict.** _(unevaluated.)_
