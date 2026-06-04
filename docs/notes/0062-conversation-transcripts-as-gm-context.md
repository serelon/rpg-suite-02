---
tags:
  - kind/pattern
  - source/solorpg
  - theme/single-source-of-truth
  - theme/context-economy
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-04
---

# Conversation transcripts as GM context — verbatim dialogue keeps the story from mutating

**What it is.** In the last two lumina-city sessions, the user ended up **extracting
conversation transcripts** from play — verbatim dialogue records handed to the GM as
context. Instead of a one-line summary saying "they talked about X," the GM gets the
*details*. Purpose, in the user's words: "**keeps the story from mutating**."

**Where it comes from.** Organic practice in `solorpg/campaigns/lumina-city` (last two
sessions, ~mid-2026). Not a designed workflow — it emerged at the table, twice.

**Why it matters for next-gen.** Three things converge:
- It's the **third independent reinvention of verbatim capture** (texture bank
  [[0055-register-anchor-banks]], the lost memory-scenes intent
  [[0054-verbatim-capture-lost-intent]], now transcripts). The user keeps reaching for
  exact words; the system keeps not providing them. Strongest possible signal that
  *verbatim is a first-class capture mode* in the next-gen spec.
- It's the precise counterweight to [[0030-summary-as-compression]]: summaries evict
  texture, but **dialogue is sometimes state** — commitments, lies, exact phrasings, tells.
  Compressing "they talked about X" discards canon, not texture.
- It's drift prevention at the event level ([[0052-evolution-vs-drift]]): a transcript
  pins what was actually said, so recollection can't quietly rewrite it.

**Open threads.** Selection problem: which conversations earn transcription (all? flagged
at debrief?) — relates to tag-at-build ([[0058-flag-lifecycle-set-at-build-select-at-prep]]).
Where do they live — a new artifact type, or memories with a verbatim mode restored (0054's
fix)? Context cost: transcripts are heavy; JIT-load per scene
([[0060-jit-loading-retry]]) rather than infodump? Extraction tooling: currently manual —
debrief-stage automation candidate.

**Verdict.** _(unevaluated.)_
