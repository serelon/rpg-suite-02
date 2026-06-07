---
tags:
  - kind/idea
  - source/conversation
  - theme/workflow
  - theme/single-source-of-truth
  - maturity/experimental
  - verdict/unevaluated
created: 2026-06-07
---

# Novelization — render a played session/campaign as one seamless story file

**What it is.** An output format: take played sessions, remove the seams (OOC notes,
redos, mechanics) and produce one continuous novel-style story file. Audience: the user
re-reading their own campaigns. Wanted as an **option, not a core feature**.

**Where it comes from.** Sonnet 3.5-era experiment (braindump 2026-06-07): one heroic
prompt — "write the entire story into an artifact, remove seams, do no mistakes" — which
went *better than you'd guess* but still misplaced large slices and rewrote lots. Untested
since; late-Opus-4.x models would likely pull it off, and both user and model instincts
now say pipeline it (chapter-by-chapter with continuity checks) rather than one-shot it.

**Why it matters for next-gen.** Two reasons. (1) It's the workload that *forced* the
weaving doctrine ([[0092-weave-player-input-doctrine]]) — woven sessions novelize
almost for free; echo-then-append sessions can't. The doctrine outlived the workflow.
(2) It's another presentation layer over the same canonical record
([[0069-one-knowledge-base-many-presentation-layers]]) — like summaries and savefiles,
a render, not a source of truth. Fits the postprocessing-agent family
([[0075-postprocessing-as-vault-librarian]]) as an on-demand, low-priority member.

**Open threads.** Pipeline shape: per-session chapters → stitch, or per-arc? What's the
input — raw transcripts ([[0062-conversation-transcripts-as-gm-context]]) or
preprocessed exports ([[0032-preprocessing-token-hygiene]])? Relation to the far-future
full-rewrite ambition ([[0094-save-everything-deferred-compute]]) — novelization is the
near-term, single-campaign version of that. Worth a one-off modern-model retest before
designing anything.

**Verdict.** _(unevaluated.)_
