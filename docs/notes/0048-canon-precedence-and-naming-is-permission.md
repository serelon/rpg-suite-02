---
tags:
  - kind/pattern
  - source/solorpg
  - theme/context-economy
  - maturity/proven
  - verdict/unevaluated
created: 2026-06-03
---

# Workshop's context protocol — naming is permission; primers are design intent, not canon

**What it is.** Two portable rules from the workshop skill's context-loading protocol:
1. **Naming is permission.** When the user names a campaign, load its context immediately
   (root CLAUDE.md → campaign CLAUDE.md → branch/subsetting CLAUDE.md) — no asking. Cheap
   reads announce-and-go; only bulk dispatches ask first.
2. **Canon precedence.** For pre-session branches, the primer is the source. After play,
   **primers are design intent, not canon** — character JSON + most recent savefile outrank
   the primer. (User: "things evolve from the seeds after session 01.")

**Where it comes from.** `solorpg/.claude/skills/workshop/SKILL.md`. Part of why workshop is
the user's "best multipurpose skill" — frictionless entry plus sophistication about which
source is truth at which lifecycle moment.

**Why it matters for next-gen.** Canon precedence should be a **spec-level rule**, not a
quirk of one skill — every consumer (compiler, briefing, post-processing) needs the same
answer to "what is true now?". Naming-is-permission is a UX principle for any entrypoint.

**Open threads.** Does precedence generalize to a full ordering (savefile > character JSON >
memories > summaries > primer)? Related: [[0030-summary-as-compression]],
[[0017-recap-as-verification]], [[0046-campaign-lifecycle-geological-strata]].

**Verdict.** _(unevaluated — appraisal owed, parked 2026-06-03 at user's request.)_
