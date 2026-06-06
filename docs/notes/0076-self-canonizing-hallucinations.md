---
tags:
  - kind/pattern
  - source/claude-desktop
  - theme/context-economy
  - maturity/proven
  - verdict/adopt
created: 2026-06-06
---

# Self-canonizing hallucinations — fact-check rounds launder invented details into canon

**What it is.** Observed failure mode in error-correction workflows (user, 2026-06-06):

> round 1: ai writes stuff, hallucinates detail A
> round 2: told to fact check, sees detail A...and stamps that as canon with the
> motivation "was written in, so must be canon!"

The fact-check round *launders* the hallucination: once an invented detail is in the
corpus, "exists in the data" and "is true" become indistinguishable to a checker reading
that same corpus. Verification against a self-contaminated source can only confirm, never
catch. (User's own caveat: "likely a prompting/method failure, but still" — the prompt
presumably didn't distinguish *verify against canon* from *verify internal consistency*.)

**Context: this happened in-play, as a drift-stopping attempt.** Mid-session, the GM was
asked to fact-check — and treated its *own recent session prose* as the canon source. The
anti-drift measure became the drift vector: in-session text is precisely the least
authoritative layer (it's what the primers/savefiles exist to anchor), but it's also the
nearest and freshest in context, so it wins by recency. An in-play checker must be pointed
*down* the precedence stack ([[0048-canon-precedence-and-naming-is-permission]]), away
from the session transcript it just wrote.

**Why it matters for next-gen.** Direct threat to the librarian/custodian model
([[0075-postprocessing-as-vault-librarian]]): a custodian that "resolves
canon-contradictions" by majority-of-what's-written will systematically side with
well-laundered hallucinations. What defeats it, structurally:

- **Provenance.** A claim needs a *source pointer* (which session, which workshop, which
  primer) before it counts as canon — unsourced details are exactly what the checker
  should treat as suspect, not confirm. Fits the build-manifest thinking of
  [[0057-compiled-context-needs-audit-tooling]] and makes
  [[0048-canon-precedence-and-naming-is-permission]]'s precedence checkable.
- **Check against the layer below, not the same layer.** Summaries get checked against
  transcripts ([[0062-conversation-transcripts-as-gm-context]] — verbatim is evidence),
  vault pages against session sources — never a document against itself or its siblings.
- The custodian's human gate ("always talk to the human before doing changes") is the
  last line, but only works if the proposal *shows provenance* so the human can spot the
  sourceless claim.

Cousin of [[0052-evolution-vs-drift]] (this is a mechanism by which drift survives the
defenses) and of [[0017-recap-as-verification]]'s limits.

**Open threads.** How heavy does provenance need to be — per-claim citations would be
unbearable to author; per-section source pointers maybe enough? Does the
two-trunk/page-vs-design-doc split ([[0068-multi-lens-data]]) give natural "layer below"
check targets for free? Is there a cheap prompting fix (explicit "newer text is suspect,
older canon is truth" ordering) worth testing before structural fixes?

**Verdict.** **Adopt** (appraised 2026-06-06) — both defenses: provenance ("receipts")
and check-against-the-layer-below. Known open issue, flagged by the user at appraisal:
**tuning the granularity** of provenance — per-claim is unbearable, per-file too coarse to
catch a single laundered detail; section-level is the starting guess, to be tuned in
practice.
