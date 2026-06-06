---
tags:
  - kind/idea
  - source/conversation
  - theme/architecture
  - maturity/speculative
  - verdict/unevaluated
created: 2026-06-06
---

# Writer/planner split — multilayer storywriting for Unicorn

**What it is.** A [[0074-project-unicorn]] idea (user, 2026-06-06): **multilayer
storywriting — one agent writes, another plans.** Concretely: a local Gemma RP finetune
writes the story prose, "with opus doing the heavy thinking."

**Why it matters for next-gen.** Several existing threads converge on it:
- It's the **tier-by-judgment principle** ([[0064-unharvested-archive]]'s
  stages-bound-to-judgment-levels) applied to *live play* instead of batch processing:
  prose generation is high-volume/style-bound; planning, canon-guarding, and consequence
  judgment are low-volume/high-stakes.
- It could structurally absorb jobs currently crammed into one context: the planner holds
  the mandatory checks ([[0066-mandatory-presence-not-length]]) and canon precedence
  ([[0048-canon-precedence-and-naming-is-permission]], [[0076-self-canonizing-hallucinations]]'s
  checker pointed down-stack) without competing for the writer's attention — attention
  starvation (0066) gets solved by *having two attentions*.
- Cost: the expensive model runs occasionally (beats, scene plans, retcon checks); the
  cheap local model runs every turn. Same economics as [[0077-context-injection-vs-cache-economics]]
  pursues by other means.
- An RP-finetuned local writer may also hold *register/voice* better than a generalist —
  ties into the verbatim-anchors/voice cluster (0053–0055).

**Open threads.** Interface between them: does the planner hand the writer a beat sheet, a
constraint list, or live interventions (and is that interface the same *seed* contract as
[[0080-engineer-and-gardener]] — planner as in-session engineer, writer as pure gardener)?
Latency: two-model turnaround per turn vs planner-every-N-turns. Failure mode: writer
drifts between planner check-ins — who catches it, how fast? Is the planner also the
in-play fact-checker (0076), and does that overload *it* in turn?

**Verdict.** _(unevaluated.)_
