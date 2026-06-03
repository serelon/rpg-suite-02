---
tags:
  - kind/pattern
  - source/solorpg
  - source/new
  - theme/architecture
  - theme/context-economy
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# Beware architecting around transient model constraints

**What it is.** Model capabilities move — fast. Architecture built to *work around* a current
limit becomes dead weight the moment the limit lifts. **Worked example:** `solorpg`'s session
postprocess went v1 (single subagent reads chunks, returns a lossy report) → v2 (a Lead +
persistent **Lorekeeper** team, [[0025-lead-plus-persistent-lorekeeper]]) — an elaborate
multi-agent split whose *entire reason for existing* was fitting session data into a **165k**
context window. When the window became **1M**, fitting everything in one context turned
trivial and **the whole apparatus was obsoleted twice over.** Significant design effort,
zeroed by a capability bump.

**Where it comes from.** User correction during mining: "postprocess v2 is obsolete… we made
that when you still had a 165k window; once that got upped to 1M, fitting all the data in one
context became trivial."

**Why it matters for next-gen.** A **load-bearing design discipline**, especially now (we're
choosing the architecture). Separate two kinds of decision:
- **Capability workarounds** — exist because *today's* model can't do X (small context, weak
  instruction-following, no thinking channel). Keep these **cheap to delete**; isolate them;
  expect to.
- **Genuine architecture** — true regardless of model size (separation of concerns,
  data-by-volatility, frontend-agnosticism). Build on these.

It hands the appraisal a sharp **verdict-time test**: *"Is this pattern solving a salience /
correctness / structure problem, or just a capacity limit that will evaporate?"* Note the
[[sample-book]] insight already passes it ("crispness is a **salience** problem, not a
capacity one" → [[0009-jit-context-and-eviction]] survives bigger windows). Multi-agent
*splitting-to-fit* does not. Tension to hold: don't *under*-build for today either — but when
you do, quarantine it.

**Open threads.** What in our own emerging design is secretly a 2026-capability workaround?
(Chunking? Bundling? Any "split across agents" move?) Audit each against the test. Does
1M-context obsolete other source patterns — preprocessing/chunking pipelines especially?
