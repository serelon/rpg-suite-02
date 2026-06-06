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

**Selection problem, dissolved (user, 2026-06-04).** The need was realized **mid-session**,
and extraction was retroactive: "go read all chunks of session X, gimme a transcript of
scene Y." This works because the **raw session chunks persist** in imports/ — so verbatim
doesn't need prediction at capture time at all. Keep the raw substrate; extract on demand.
The imports archive is not an inbox, it's the permanent harvest substrate
([[0007-harvest-vs-workshop]]). The real design requirement is *cheap, addressable
re-extraction* (find scene Y in session X fast), not foresight.

**The artifacts examined (sweep 2026-06-06).** Two files in
`lumina-city/transcripts/` (`nyx-session-0{2,3}-ling-vidal-transcript.md`, ~8KB each).
The emergent format is remarkably well-formed for an undesigned type:
- **Header block:** Campaign / Branch / Session / Timeframe / Location / Speakers (with
  role notes) / **Source** / Type — where *Source cites the exact chunk files and line
  ranges* (`imports/chunks/session-02-chunk-02.md lines ~710–889`). That's
  [[0076-self-canonizing-hallucinations]]'s **provenance receipts, invented independently
  in the wild** — the strongest possible validation that receipts are a natural shape,
  not imposed ceremony.
- **Type declaration in-file:** "Verbatim dialogue extract — spoken lines only; narration,
  interiority, and player-input lines omitted. `…` marks elided narration." A treatment
  flag ([[0085-knowledge-entries-vs-tool-data]]) written as prose.
- **Scene-context blockquote:** 1–2 sentences of what the conversation *accomplishes*
  (purpose zoom), then `**SPEAKER:**` lines with `…` elisions.
- So the transcript is already a knowledge entry with the standard anatomy: metadata,
  purpose line, body, provenance — it just doesn't know it yet.

**And the system is blind to it:** transcripts appear in *no* documented structure —
not lumina-city's CLAUDE.md, not postprocess-instructions' 7 memory types, not the
summaries. A live specimen of the custodian's exception-hunting job
([[0075-postprocessing-as-vault-librarian]]): a treasure-exception the tooling would
never have surfaced ([[0026-exceptions-are-features]]).

**Open threads.** Does on-demand extraction scale, or do hot conversations earn promotion
to a cached artifact after first extraction (extract-once, keep-thereafter — these two
*are* that promotion, manually)? Where do they live — new artifact type, or knowledge
entry with a verbatim treatment flag (0085's answer: the latter)? Context cost: heavy;
JIT-load per scene ([[0060-jit-loading-retry]])? Extraction tooling: currently manual —
debrief-stage automation candidate.

**Verdict.** _(unevaluated.)_
