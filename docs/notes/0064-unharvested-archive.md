---
tags:
  - kind/question
  - source/solorpg
  - source/claude-desktop
  - theme/single-source-of-truth
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-04
---

# The unharvested archive — most raw sessions never came home

**What it is.** The away-play loop (export chat → `campaigns/*/imports/` → post-process)
only exists *since the current system*. Before it, sessions stayed in Claude Desktop. The
user has pondered a **full Claude Desktop data dump**: 1000+ threads, "at most half" RP
sessions — call it ~500. The imports folders today hold **~58 exports across 19 campaigns**
(counted 2026-06-04), five campaigns at zero — including lineage-rich ones
(the-great-awakening, threads-of-berlin, where-mists-gather). The raw-substrate coverage is
maybe a tenth of the actual play corpus.

**Where it comes from.** User disclosure during light workshop (2026-06-04); counts
verified against `solorpg/campaigns/*/imports/`.

**Why it matters for next-gen.** Directly weakens [[0062-conversation-transcripts-as-gm-context]]'s
"extract retroactively on demand" — on-demand extraction only reaches what was harvested.
For everything pre-system, verbatim is *currently unrecoverable from the repo* (texture
banks, transcripts, voice samples for old campaigns can't be built). A dump-and-sort is
the only way to make the substrate complete — and at ~1000 threads it's an **agent-scale
triage job** (classify RP/not-RP, attribute to campaign, route to imports/) — precisely
the shape of the old E:\rpg 5-agent pipeline, reborn ([[0040-vector-db-as-lore-search-module]]
would also want this corpus). Tarot Tales-era lineage ([[0053-anchor-hierarchy-voice-keystone]])
lives in there too.

**Composition (user, 2026-06-04):** the archive holds *both* unharvested sessions of
existing campaigns *and* whole lost campaigns that never got folders — **plus a lot of
oneshots**. Oneshots are notable: the campaign-folder model has no home for them at all
(no folder, no savefile chain, no postprocess target), yet they're a large share of actual
play. Next-gen data model question: is a oneshot a degenerate campaign, or its own artifact
type? (Cf. [[0026-exceptions-are-features]] — a structural class the current system
doesn't even *try* to absorb.)

**Upgraded from pondering to plan (user, 2026-06-06).** "i'll prolly do a full claude
desktop/web/mobile datadump sometimes. and..toss that into our process-framework. we'll
need to build a workflow for handling that, because that'll be ridiculous amounts of data,
and i suspect at most half will be relevant." So this is now a **named next-gen workflow
requirement**: a bulk-ingest/triage module, not a one-off chore. Implied stages: classify
(RP / not-RP — expect ≥50% discard), attribute (existing campaign / lost campaign /
oneshot), route (imports, new homes, [[0065-oneshots-as-spawning-pool]]'s cheap home for
oneshots), then feed the librarian ([[0075-postprocessing-as-vault-librarian]]) at archive
scale. Also the future test corpus for trigger-keyword validation
([[0069-one-knowledge-base-many-presentation-layers]]) and cache-policy simulation
([[0077-context-injection-vs-cache-economics]]) — the dump pays for itself thrice.

**Resource note (user, 2026-06-06):** local LLMs are available (Gemma 4) and could carry
much of the bulk — "at least postprocess/categorize." Suggests a **cost-tiered pipeline**:
local models do the high-volume/low-judgment passes (RP-or-not classification, campaign
attribution, chunking), frontier models reserved for the low-volume/high-judgment passes
(verbatim extraction, voice/texture harvesting, canon-sensitive summarization). Tier
boundary = where errors become expensive. Middle tier candidate: DeepSeek — postprocessing
has traditionally been Opus in Claude Code ("the best and smartest option… also the most
expensive"), and a mid-tier model may cover much of it. The roster is explicitly
era-variable ("at least until mythos drops...") — so per-[[0031-beware-transient-constraint-architecture]],
the pipeline should bind *stages to judgment levels*, not to named models; which model
fills which tier is config, not architecture.

**Open threads.** Is a Desktop data dump even exportable in bulk today, and in what format?
Triage criteria: route by campaign how — title matching, content classification? Storage:
1000 threads of JSONL is heavy — does it live in the campaign repo or a separate
archive store (data/tools split, per E:\rpg's design)?

**Verdict.** _(unevaluated.)_
