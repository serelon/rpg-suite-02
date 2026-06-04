# GM-Skill Tuning Note — Thinking-Block Enforcement

**Context:** Lumina City (Nyx), Session 04. Diagnosing a recurring instruction-following drift and the fix to the thinking instructions.

## Symptom

The **transform / weave-the-input** rule — rewrite the player's lines into choreographed narrative voice; never transcribe — degraded mid-session. It's the campaign's most common drift, and normally a single gentle nudge restores it. This time it took 1–2 escalating corrections before it held.

## What it wasn't

**Not data loss.** No autocompact/summarization occurred. The full prep load (primer, setting + branch docs, all three summaries, the savefile, all 29 memories in full, profiles, name pools) stayed raw in context the whole session. The rule was never evicted — it stopped *firing*.

## Root cause

**Craft drift via attention starvation.** "Transform the input" is a *counter-default* rule: left unattended it loses to the trained reflex (mirror the input → transcribe short lines, pour the effort into NPC/scenery instead). Counter-default rules only fire while something *actively holds them* — and per the skill, that something is the thinking block ("the thinking block is where this skill is enforced").

**The trigger:** a mid-session instruction to stop overthinking. Reasonable — the blocks were genuinely bloated — but it thinned the *enforcement layer* along with the fat. Length came down and the load-bearing checks came down with it. The misses got stickier immediately afterward; the timeline fits.

**Possible secondary contributor (unverifiable from inside):** attention conscription from injected guidance around the session's heavy themes. Can't be confirmed by introspection — injected text isn't auditable as discrete labeled items from in here — but it's mechanism-consistent: it competes for the *same* attentional budget the craft rules draw on. Whatever the source, the dial we can actually turn is the thinking instruction.

**The unifying mechanism:** attention is the scarce resource. Anything that *reduces* it (thin thinking) or *competes for* it (injected guidance, dense recent narrative) starves the counter-default craft rules first, because they're the ones that exist only by being held.

## The lesson (your phrasing, refined)

Correct: make the thinking a **checklist of mandatory boxes**, not loose open-ended reflection.

Refinement: **length is not the lever — mandatory-presence is.** The target is *"brief, but these always run,"* not *"brief."* A bare *be concise* instruction reads as *shed load*, and the first thing shed is the counter-default craft.

Guard both failure modes:
- **Too loose** → sprawls back into the overthinking we were trying to kill.
- **Rote** → the skill's own warning: a checklist run as hollow box-ticking does no real work. Each box must be a genuine check, not a ritual.

So the spec is: **short, fixed, genuine.**

## Candidate mandatory checks (fire every turn, regardless of length)

- **Transform** — re-voice and choreograph the player's input into prose; never transcribe the quoted lines. *(The one that broke this session — make it box #1.)*
- **Live wire** — decide the stop point in advance; end on something reactable.
- **Don't mirror density** — terse input is compression of a scene to render, not a spec for a terse reply.

Plus the standing per-turn guards already in the skill, kept on the same list so they don't get crowded out:
- **Authority split** — move the world, never author the PC's will; stop before their decisions.
- **Scene-header stamp** — at every boundary (exact date + 24h time).
- **"What have I forgotten?"** — the open threads / who's where sweep.

## Note on content (so it isn't mis-attributed)

The drift was an **enforcement/attention** problem, not a **content-appropriateness** one. The session's guardrails held cleanly — the burn kept in shape, never shown, the weight carried in the negative space. Don't read the drift as a signal the material was a problem; it wasn't.

## One-line takeaway

Don't make the thinking *shorter* — make the **load-bearing checks non-negotiable** and let everything else be as lean as it wants. Short block, real checks.
