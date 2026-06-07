---
tags:
  - kind/principle
  - source/conversation
  - theme/single-source-of-truth
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-07
---

# Save everything as deferred compute — raw data outlives today's models

**What it is.** A standing rationale behind the save-everything stance: one reason the
user preserves all raw session data is "to be able to rewrite all my stories in the far
future when the technology can actually handle that." Raw captures are **deferred
compute** — keep the lossless record now, re-render it when models are good enough.
User's own caveat, verbatim: "'future rewrite' is still high up on the 'vanity project'
list tho :)" — it's motivation and insurance, not a requirement to design against.

**Where it comes from.** Braindump 2026-06-07, explaining why novelization
([[0093-novelization-as-output]]) was attempted too early and shelved rather than the
data being discarded. It also explains the affect behind solorpg's "data is *very*
important" and the pain of [[0064-unharvested-archive]] (~500 Desktop sessions not in
the repo — exactly the raw material this principle says must survive).

**Why it matters for next-gen.** It sharpens what "canonical record" must mean:
derived artifacts (summaries, savefiles, novelizations) are disposable renders, but the
**raw transcript layer is the permanent asset** and should be hoarded losslessly —
supporting [[0062-conversation-transcripts-as-gm-context]] and the build-products view
([[0056-files-as-build-products]]): sources forever, renders regenerable. Capture
formats should favor *losslessness over convenience*, since future consumers are
unknown and likely more capable.

**Open threads.** Does "lossless" include the OOC/redo/mechanics layer that novelization
strips — i.e. keep the seams *and* their markers? (Probably yes: future rewrites need to
know what was a redo.) Tension with [[0032-preprocessing-token-hygiene]]: preprocessing
must be a fork, never a replacement, of the raw export.

**Verdict.** _(unevaluated.)_
