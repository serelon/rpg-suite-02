---
tags:
  - kind/pattern
  - source/aegis-tools
  - theme/architecture
  - theme/single-source-of-truth
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-05
---

# The threads tracker — quest tracking that actually worked

**What it is.** `aegis-tools/threads.py` (+ `modules/threads/module.py`), the quest/plot
tracker the user singles out: "the intel and quest tracker we made for it... turned out to
work really well" — despite the campaign itself being short-lived. Design choices that
earned it:

- **Semantic slugs for persistent things, numeric IDs for ephemera.** Threads are
  `grunfeld-survivors`, `signal-analysis` — memorable, grep-able, self-documenting in
  session notes. Rumors/contacts are `r1`, `c2` — short-lived, fine to forget. ID scheme
  matched to lifecycle.
- **Bidirectional auto-reverse connections.** `threads connect A B` writes the edge on
  *both* records atomically — half-links are structurally impossible. Real campaign data:
  zero dangling references.
- **Max-one-level nesting, enforced at write time.** Children allowed, grandchildren
  rejected with an error; remove-with-children blocked. No tree sprawl, and the real data
  has zero violations.
- **Real state machine.** `active / cold / resolved / abandoned`; resolved and abandoned
  are terminal. Plus advisory `deadline` / `blocked_until` dates — metadata for GM
  judgment, not auto-triggers.
- **Structured facts and free prose side by side, never merged.** Timestamped `notes[]`
  (prose, no schema, searchable) next to dumb `tasks[]` checkboxes. A resolved thread with
  unfinished tasks reads correctly: "research done, downstream applications still open."
- **Timestamps from campaign time, not wall-clock** — `created`/`updated` come from the
  shared `currentDate`, so "what did we learn this session" is queryable.

**Where it comes from.** Explore sweep of aegis-tools (2026-06-05); live data at
`solorpg/campaigns/aegis/data/threads.json`.

**Why it matters for next-gen.** Most of these are **vault-layer lessons**
([[0067-campaign-data-as-linked-vault]]): auto-reverse edges are exactly what the KB's
link layer needs; semantic-slug-for-persistent is a page-naming rule; prose-next-to-facts
is the entity-page shape. And it's a counterpoint to [[0061-continuity-artifacts-under-suspicion]]:
*this* continuity artifact earned trust. Worth asking why threads worked where savefiles
are doubted — possibly because threads are append-and-transition, never rewritten.

**Open threads.** Does the thread tracker generalize beyond tactical campaigns to
narrative solo play (plot threads, NPC arcs, mysteries)? aegis's enforced-rules philosophy
([[rules-as-code]] — no note yet; aegis's system-as-code stance) made the state machine cheap — what carries over to the
convention-not-code side of the house?

**Verdict.** _(unevaluated.)_
