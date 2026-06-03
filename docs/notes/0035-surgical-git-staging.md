---
tags:
  - kind/pattern
  - source/solorpg
  - theme/workflow
  - theme/human-in-the-loop
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# Surgical git staging — branch-per-run, never `git add -A`

**What it is.** Each postprocess runs on its **own branch** (`postprocess/[campaign]-s[N]`),
and the skill is emphatic (twice): **never `git add -A`** — it sweeps unrelated untracked
files (stray transcripts, other campaigns' WIP, scratch files) into the commit. Instead,
**stage only the files this run actually wrote**, then `git status` to confirm *only* intended
files are staged before committing. Work is isolated on the branch and merged/PR'd
deliberately; an abandon path (`git branch -D`) discards cleanly.

**Where it comes from.** [[session-postprocess]] v1, Steps 1.2 and 6.4 (the repeated
`git add -A` warning is clearly a scar from being burned).

**Why it matters for next-gen.** A concrete safety rule for **any agent that writes into a
shared, multi-tenant repo** (which this vault and the campaign repos both are). It's the
version-control face of the same instinct as [[0028-checkpointed-human-gates]] (review before
commit) and the campaign-isolation thread ([[0029-information-boundary-enforcement]]): don't
let one operation's output bleed into another's. Worth encoding as a default for framework
agents, not rediscovering per-skill.

**Open threads.** Can the "stage only what this run wrote" set be tracked automatically (the
agent knows the files it Wrote) rather than hand-listed? Per-run worktrees as a stronger
isolation than branches?
