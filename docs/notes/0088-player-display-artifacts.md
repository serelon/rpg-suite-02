---
tags:
  - kind/pattern
  - source/solorpg
  - theme/architecture
  - theme/context-economy
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-06
---

# Player-display artifacts — the third audience (cheatsheets as oversized widgets)

**What it is.** A data class the type system ([[0085-knowledge-entries-vs-tool-data]])
hadn't named, exemplified by the skill-generated HTML cheatsheets (interview 2026-06-06):
artifacts "built for the sole purpose of people readable for the player, and player
alone. it's a glorified oversized widget."

Defining properties:
- **The GM is strictly instructed *not* to read it.** It's **redundant by construction**
  — every fact on a cheatsheet already lives elsewhere in canon — so reading it is "just
  a waste of tokens." Negative load rule, enforced by instruction.
- **Write-only from the system's perspective**: rendered out, never read back. Pure
  [[0056-files-as-build-products]]; zero canon weight; regenerable at will.
- Format freedom because no model pays for it — "some actually include code :)
  (threadlight one!)". Same economics as tool data's complexity license (0085): cost
  invisible to the context window.
- It's [[0082-live-hook-pipeline]]'s widget lane, **pre-invented in the static era**: a
  cheatsheet is a widget that updates per-session instead of per-turn.

**Currently the class has one member** ("think it's just cheatsheets...for now") — and
the user names why: "we've worked with claude desktop as the endpoint pretty much..that
has limits on how to use enriched data." The class is *endpoint-constrained, not
idea-constrained* — [[0074-project-unicorn]]'s own UI (widget panes, sidecards, live
state displays) is where it grows.

**Why it matters for next-gen.** Completes the audience axis of the type system. Readers
are now: **model-context** (knowledge entries, zoom-tiered), **human-as-author/auditor**
(design trunk, state files, manifests), **player-display** (rendered, redundant,
never-loaded). Each has opposite optimization pressures (token-lean vs legible vs pretty),
which is exactly why one artifact must never serve two masters — the cheatsheet's
never-read rule is [[0068-multi-lens-data]]'s lens separation enforced at the audience
level. The "redundant by construction + never loaded" pattern is also the only fully
drift-safe artifact class in the whole system: it can't contaminate anything
([[0076-self-canonizing-hallucinations]] has no path in).

**Open threads.** Does the never-read rule need *structural* enforcement in next-gen
(player-display trunk excluded from all consumer manifests) rather than instruction?
What grows in this class under Unicorn — live character sheets, relationship maps, the
economy render ([[0087-spreadsheet-semantics-tool-data]])? Is there a *player-authored*
variant (notes the player writes that the GM must not see — fog-of-war in reverse,
[[0071-fog-of-war-as-data-structure]])?

**Verdict.** _(unevaluated.)_
