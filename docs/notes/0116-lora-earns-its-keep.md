---
tags:
  - kind/principle
  - source/conversation
  - theme/local-finetuning
  - maturity/seed
  - verdict/adopt
created: 2026-06-13
---

# A fine-tune earns its keep only where prompting can't reach — mostly: small models

**What it is.** The skeptic's gate, to stop the shiny idea from over-adopting. For *pure
flavor*, a good userstyle plus a few-shot anchor is already ~85% of the way there on a
capable model. A fine-tune (LoRA) earns its keep when you want a **small/local model to
hold a register it cannot manage zero-shot** — i.e. the real payoff is making a tiny model
(E4B-class) punch above its weight for fast, local, offline play, **not** re-tuning a model
that already takes direction well. What you get is "the strong model performing my style,"
compressed into an adapter the small model can wear.

**Where it comes from.** Inbox conversation [[Claude-export-custom-lora]] (2026-06-13),
the gut-check the other assistant raised twice: distilling Opus's voice into Gemma gets
you cadence/flavor (the surface layer that distills cleanly) but **not** Opus's reasoning.

**Why it matters for next-gen.** It sets the **adoption boundary** for any local-model
work in the stack: a fine-tune is justified by a *capability gap a prompt can't close on
the target model*, and the canonical such gap is "I want this to run small and local."
This keeps fine-tuning in its lane and protects the more proven levers — exemplars
([[0005-exemplars-over-instructions]]), the sample-book grid
([[0006-sample-book-grid]]), counter-default authoring
([[0013-counter-training-name-the-default]]) — which already do the job on capable models.
It also feeds the [[0081-writer-planner-split]] sketch (local fine-tune writes prose, a
strong model plans/judges): the fine-tune's job is narrowly *in-voice continuation*, the
thing [[0012-intelligence-in-scaffolding]] wants pushed down into a small model.

**Open threads.** Per-campaign hot-swappable adapters over one base (an instance of
campaign isolation, [[0091-one-vault-campaign-folder-entrypoints]]) are attractive — one
adapter per campaign register — but only pay off once the local-writer path
([[0081-writer-planner-split]]) is real; today it may be a solution ahead of its problem
(cf. [[0031-beware-transient-constraint-architecture]] / [[0112-design-now-build-into-frame]]).
Is there a *non-small-model* case (privacy, cost, latency at scale) that also clears the
bar?

**Verdict.** _(2026-06-13.)_ **adopt** — the scoping decision, in the user's own words:
the default workflow (prep in Claude Code, **play in Claude Desktop on Opus**) isn't
changing, and you can't fine-tune Opus — so a LoRA is explicitly a **sidequest**, worth it
only for trying sessions on small/local models. Adopting this is what keeps a future
session from over-investing in fine-tuning infra. Corollary the user drew: expose session
data so a dataset is *easy to assemble later*, but **scope that exposure to the sample-book
/ texture-bank needs that pay for themselves now** — the LoRA-dataset usefulness is a free
rider, never the driver (guards the [[0031-beware-transient-constraint-architecture]] trap).
