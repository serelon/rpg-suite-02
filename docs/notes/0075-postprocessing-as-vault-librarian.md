---
tags:
  - kind/idea
  - source/conversation
  - theme/architecture
  - theme/single-source-of-truth
  - maturity/speculative
  - verdict/adopt
created: 2026-06-06
---

# Post-processing is the vault librarian — and maybe needs a colleague

**What it is.** Settles 0067's parked question (user, 2026-06-06): in the canonical-vault
world ([[0067-campaign-data-as-linked-vault]]), **post-processing becomes the librarian**
— instead of writing character JSONs and savefiles, it updates entity pages, adds session
pages, links new entities in. Its output artifacts become vault mutations
([[0073-structured-mutation-beats-rewrite]]: append/patch operations, not regenerated
files).

**Two open design questions raised with it:**

1. **Is one librarian enough — do we need a second?** Candidate split: the
   *ingest librarian* (post-process: turns play into vault updates) vs a *custodian*
   (periodic gardening: link integrity, schema validation ([[0072-schema-drift-tools-vs-hand-edited-json]]'s
   validate-loudly), drift audits ([[0052-evolution-vs-drift]]'s fresh-context detection),
   index freshness). Different cadence, different context needs — ingest wants the
   session fresh in mind; custodial wants *no* session context, the cold eye.

2. **Batch vs streamed.** Today post-processing runs after a full session. Could it run
   **as-we-go, scene-by-scene** (SillyTavern-pattern; natural fit for
   [[0074-project-unicorn]])? Condensing per scene instead of per session. Pulls toward:
   smaller, safer mutations (0073), scene boundaries as the natural chunk unit (the
   retroactive chunk-extraction in [[0062-conversation-transcripts-as-gm-context]]
   already treats scenes as the unit), and the live-context-delta machinery
   ([[0051-live-context-delta]]) doing double duty — the same scene-condensate could
   patch the *running* session's context AND queue as a vault mutation.

**Custodian's job list (user, 2026-06-06 — research material, not committed design):**
housekeeping; audit links / graph health; archive obsolete data; resolve
canon-contradictions; flag out-of-date formats needing updates; and the tricky one —
**look for *exceptions*** — user's lean: mostly *treasure* ("new patterns we need to
cover", cf. [[0026-exceptions-are-features]]) but it "can also be rot"; the custodian
surfaces both and the human sorts which is which. Two hard constraints named:
the whole thing is being set up to be **self-evolving** ([[0041-self-evolving-versioned-spec]]),
and — guardrail — **"always talk to the human before doing changes, or we risk going off
the rails"**: the custodian proposes, never commits; same human-gate as the
postprocessing PRs in [[0052-evolution-vs-drift]].

**Why it matters for next-gen.** Defines post-processing's role in the one-KB architecture
([[0069-one-knowledge-base-many-presentation-layers]]): consumers read the KB, the
librarian is the *write path*. If writes are streamed, the KB stays near-live; if batch,
it lags a session behind — which consumers (especially RAG) would feel.

**Open threads.** Scene-boundary detection — who calls "that was a scene"? (GM model
mid-play? a watcher? explicit user beat?) **Genuinely unsolved** (user, 2026-06-06):
"sometimes we have very clear barriers, sometimes they blur, and i dont really have a
clear answer." Likely needs a hybrid: take the cheap wins when barriers are clear (hard
cuts, location changes, time skips), and let blurry stretches fall back to end-of-session
batch — streaming as opportunistic, not mandatory. Does streamed condensation degrade prose quality
vs end-of-session hindsight (early scenes look different once the session's end is known)?
Review gate: solorpg post-processing earned PRs — what's the review step for a stream of
small mutations ([[0052-evolution-vs-drift]] gates)?

**Verdict.** **Adopt the core** (appraised 2026-06-06): post-processing is the vault's
write path, mutations not regenerations, propose-never-commit human gate. Explicitly
*open*, not decided: the custodian split (job list captured, shape undecided) and
streamed-vs-batch (scene-boundary detection unsolved; [[0082-live-hook-pipeline]] is the
leading mechanism candidate).
