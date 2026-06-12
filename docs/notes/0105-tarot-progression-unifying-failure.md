---
tags:
  - kind/pattern
  - source/tarot-tales
  - theme/progression
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-12
---

# Tarot Tales progression: under-specified markers with no semantic layer decay into flavor

**What it is.** Tarot Tales (v1.9) had four progression gears — **Core Aspects**
(5 aspects, ⭐–⭐⭐⭐⭐⭐), **Narrative Traits** (3 descriptive), the **Discovery System**
(Recognition → Understanding → Integration, typed Knowledge/Personal/World, pick 1 of 2–3
effects), and the **Between-Adventures** advancement gate ("one character advancement per
team") — plus an optional **Powers** rule (Latent○→Mastered⭐⭐⭐⭐⭐, vertical/horizontal/
new-manifestation growth). All four shared **one fatal flaw: they were under-specified
symbolic markers the GM had to interpret with no anchored mechanics behind them.** So they
decayed into the only thing an unenforced marker can become — narrative flavor — and in the
freeform era the user dropped them, because the marker had become redundant with prose.
**The marker dissolved into prose because it was never structurally distinct from prose.**

**The user's own diagnosis (interview 2026-06-12):**
- **Stars** broke for two reasons: (a) *no mechanics* told the GM how to interpret ⭐⭐ vs
  ⭐⭐⭐⭐ — the missing **semantic layer**; and (b) **token cost** — a star is ≥1 token, and
  one long campaign had 10+ character sheets, most past the starter 5 aspects, all with
  multiple powers = a wall of 1-token stars.
- **Updating sheets** was "rewrite-while-copying," no surgical edits → a direct instance of
  [[0073-structured-mutation-beats-rewrite]]. The pain wasn't the *progression*; it was that
  the state lived in a format only updatable by full re-emission.
- **Discoveries** were hit-and-miss-with-extra-misses: **too loosely defined**, weird for
  the GM to interpret — the semantic-layer gap again.
- **Narrative Traits** also dissolved into prose in the freeform era.
- Built with Sonnet 3.5 while new to LLMs; the unenforced ratings *looked* like "advanced
  stuff happening" but were hallucinated narrative assistance at best.

Also a **cap problem**: the system was built for short campaigns, then hit long ones and
maxed out the finite option space ("got weird").

**Where it comes from.** `G:\My Drive\Projects\Tarot Tales\older files\Rulebook - Tarot
Tales RPG System.md` (v1.9) + `Optional Rule - Powers.md`; user interview 2026-06-12.

**Why it matters for next-gen.** This is the negative space that defines the next-gen
character record. The fixes are already proven in **Aegis** (CRUD data-layer, defined
stats with a rules-as-interpretation-contract, auto-xp). Generalize the *fix pattern*
([[0106-three-layer-character-record]]), not Aegis's specific rules. Two near-free wins fall
out: an encoding that isn't ⭐-strings (a number/enum) + surgical edits kills the token and
rewrite cost independent of any design question.

**Open threads.** Pull Aegis's character-sheet/xp design into a source note as the
proof-of-fix. Was the Discovery *loop* (story-bound, no XP counter) salvageable if given a
semantic layer, or fundamentally too loose? Relation to the cap problem — do defined stats
also cap, and does that matter in long campaigns?

**Verdict.** _(unevaluated.)_
