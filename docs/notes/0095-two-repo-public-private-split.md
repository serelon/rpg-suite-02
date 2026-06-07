---
tags:
  - kind/decision
  - source/conversation
  - theme/architecture
  - theme/campaign-isolation
  - theme/packaging
  - maturity/seed
  - verdict/unevaluated
created: 2026-06-07
---

# Two-repo split — public core, private campaigns repo nested in campaigns/

**What it is.** Next-gen is a 2-repo setup (braindump 2026-06-07): **repo 1 (core)** holds
all tools, skills, workflows — built to eventually go public; **repo 2 (campaigns)** lives
*nested inside* repo 1's `campaigns/` folder and holds all private campaign data, private
forever. A third artifact exists implicitly: **this research vault**, which names live
campaigns throughout and therefore is also permanently private — never folded into core.

**The boundary rules** (so core can be published):
- No live-campaign examples in core — generic demo content only.
- No personal links/configs committed — gitignored `*.local.*` + committed `*.example`
  templates, which doubles as the "new user sets it up their way" mechanism.
- Core can never wikilink into campaign data — the real teeth behind "generic examples
  only": core must be entirely campaign-agnostic or it breaks when cloned alone *and*
  leaks by reference.

**Double duty.** Extends [[0091-one-vault-campaign-folder-entrypoints]]: the nested
`campaigns/` repo is simultaneously the campaign-isolation boundary *and* the
public/private boundary. 0091 said "isolation + info-boundaries become one guard" — this
adds public/private as the third edge of the same guard. The split is **structural, not
procedural** ([[0096-enforcement-matches-reversibility]]): nested repos are invisible to
the outer git automatically (plus `.gitignore` belt-and-braces).

**Publishing mechanics (deferred — public is wishlist, not mandatory).** When/if pursued:
private dev repo + public release mirror receiving **squashed snapshot releases** after
heavy audit — public history stays clean and anything added-then-removed between releases
never appears publicly at all. Audit becomes one release diff, not every commit.
First-line machinery for the dev repo: denylist pre-commit hook (campaign/character
names, personal paths — blocklist itself lives in the *private* repo) + CI backstop.
GitHub facts that shaped this: visibility is per-repo only (no private branches/folders);
pre-receive hooks are Enterprise-only; **public push = published** (assume scraped
instantly; filter-repo can't unpublish). The structural split is the cheap,
hard-to-retrofit commitment to lock in now; all the machinery waits.

**Precedent.** `rpg-tools` is already public — proof-of-shape: a repo that *can't* leak
campaign data because it never contains any.

**Open threads.** Demo campaign for the public core (docs + onboarding + test data in
one): deferred until it's time to test the campaign-setup tool; will be workshopped as
"the most generic campaign ever — likely absurdist comedy as a result." Where does this
research vault physically end up — alongside repo 2, or standalone? Public-mirror
contribution flow (issues/PRs on a dead-snapshot repo) — redesign only if outside
contributors actually materialize.

**Verdict.** _(unevaluated.)_
