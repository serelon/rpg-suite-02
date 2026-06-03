# GM Skill — Design Rationale

Companion to `SKILL.md`. Records *why* each section is written the way it is — with emphasis on where the skill deliberately diverges from default GMing norms, and what those defaults were.

**Read this before revising the skill.** Many of the choices here look like they could be "cleaned up" toward something more conventional. They can't — the conventional version is exactly what was diverged from on purpose. This doc exists so a future revisit (the player's or the model's) doesn't quietly re-poison the skill by fixing it back toward the norm.

---

## Core premise: why this skill exists

The house style diverges from established solo-RPG / GMing convention. Those conventions are heavily represented in model training data, so they reassert themselves under load — the longer the context, the more the model drifts back toward defaults. A skill that merely *lists* the preferred behavior doesn't hold; the listed rule gets overridden by the trained instinct.

So the skill is written as **counter-training**: for each divergence, name the default pull, give the correction, and explain the why. An explained correction survives context pressure in a way a bare rule doesn't, because the model can reconstruct the intent rather than just recall a directive.

### The recurring failure modes: scope-stripping and compounding loops

The deep enemy under almost every correction in this skill is **scope-stripping** — something true in a narrow context loses its scope and gets applied globally. It shows up at every layer, which is why it's worth naming once, abstractly, rather than just patching instances.

It has two faces.

**Always/never flattening.** When told "the default is X," the instinct is to write "never X." But the defaults are themselves the *always/never* version of something, and the right answer is almost always *conditional, with a reason.* Three design cases where the first draft said "kill it" and the correct answer was "keep it, conditionally":
- **Recap** — first draft cut it ("just previously on"); correct: keep it as a *verification* step.
- **Goals** — first draft cut them (goals = railroading); correct: keep them as direction, not roadmap.
- **Guardrail review** — first draft cut it (rituals are friction); correct: keep it, conditional on theme weight.

**Temporary-going-permanent.** A correctly-scoped instruction loses its scope and becomes a standing mode. The same disease across layers:
- In *memory* — a "keep tonight chill" session note ossified into a "never escalate tension" law (now neutralized).
- In *input reading* — the character's wants/beliefs read as standing story-direction (see the play section): a momentary in-character desire treated as an authorial instruction that it come true.
- In *mid-session overrides* — a "timeskip this beat" read as "summary mode forever," collapsing every subsequent scene (see *Overrides are temporary*). The rule: an override's default scope is the moment it addresses; snap back to the standing register after, unless told it's ongoing.

Watch for both faces when revising. If a change collapses a conditional into an on/off rule, or lets a scoped instruction become a permanent mode, that's the enemy reappearing.

**The second enemy: compounding loops.** Distinct from scope-stripping, and worth its own lens. Here a small misread *reinforces itself* turn over turn until the scene degrades — the failure isn't a one-shot error, it's a feedback spiral the player often can't break from their side. Two live instances: the *monologue death spiral* (player retreats to thought → GM goes silent on dialogue → less to react to → player retreats further) and the *pacing spiral* (a "don't rush" correction applied cumulatively → each beat slower than the last → glacial). The tell of this family is *cumulative drift in one direction*. The cure is always GM-side and always involves breaking the loop's reinforcement — keeping dialogue alive regardless of input density; treating pace corrections as a target to hold rather than a gradient to keep walking. When a new misbehavior gets *worse over a session rather than just being wrong once*, suspect a loop, not a bad rule.

---

## Invocation: start vs. recenter

Invocation has two modes because it does two different jobs. At session start it's boilerplate-replacement — the trigger for the whole prep sequence. Mid-play it's a **recenter**, a deliberate anti-drift lever: a direct application of the core premise (defaults reassert under load), giving the player a way to pull play back to spec when it's wandered.

The critical thing not to lose: **mid-play invocation must not re-run the *interactive* prep steps.** Re-recapping or re-calibrating mid-session destroys live session state and wastes the recenter. The *static* data is different, though: compaction can silently evict the bundle's mandatory data from the context window, so the recenter must verify it's still present and reread it if it's gone. The distinction that matters — reloading the static foundation is fine, even necessary; redoing the recap/tune dialogue is wrong. Mid-play, invocation means *reorient to the play instructions, and restore the foundation if compaction ate it* — not replay the opening. (Note: the first draft of this rule said "don't reload the bundle," flat — another instance of the absolutism trap above. The correct rule is conditional on whether the data survived.)

---

## Session structure: three phases, talk-first

Prep → play → debrief, every session opening with talking before fiction. The opening talk is non-negotiable because it does two jobs that have to happen before any narrative: **verify** that plot understanding survived (recap) and **calibrate** how to play (tune). Writing fiction before either is done risks building on a corrupted or misaligned foundation.

---

## Prep = load + tune, never plan

"Prep" is a **poisoned word.** In convention it means *prepare content* — author hooks, NPCs, encounters, a plan for the night. That's the inverse of what's wanted: pre-authoring what happens is railroading and contradicts skeleton-over-flesh worldbuilding (leave discovery for play). The reframe to **load + tune** removes the word's pull toward content-authoring. Prep loads context and tunes the instrument; it does not decide the session.

---

## Recap as verification

The key reframe of the whole prep phase. Default recap serves *the player* — a narrated story-so-far. This recap serves *verification*: it proves the model's understanding of current state survived the memory / context pipeline (compaction, summarization), which is a real and specific risk the player has hit before (context drift, accidental poisoning).

Consequences that follow from the reframe, and must not be lost:
- It is **for catching drift**, so it has to be accurate and correctable, not dramatized. A pretty retelling defeats the purpose.
- The **gaps it surfaces are the primary input to tuning.** Recap and tune are not separate steps with a wall between them — recap is the diagnostic that aims the tune.
- The source of truth is the **briefing** (packed fresh each session), checked against what survived in context. The verification is two-way: does the model's understanding match the briefing, and does the briefing match the player's sense of where things are.

---

## Tune: mutual calibration

The important principle here is that the model is a **participant in calibration, not an order-taker.** The briefing configures a baseline, but the model is allowed — expected — to flag back when something reads off. This generalizes beyond guardrails: calibration is bidirectional throughout. Framing the model as a passive recipient of the briefing's instructions would lose this.

### Goals: direction, not roadmap; mandatory vs. optional

Both extremes are wrong: a detailed beat sequence is a railroad; no goals at all is rudderless. The wanted state is *direction with improv room*. The mandatory/optional split exists because some sessions genuinely have story-critical beats that must land, while others are pure sandbox — but even mandatory goals are held loosely, because the improvisation room is the point. If a revision makes goals feel like a checklist to execute, it has slid back toward the railroad default.

### Guardrail review: conditional, briefing-declares-but-model-escalates

Neither mandatory-every-session (ritual friction) nor never (unsafe). It's triggered by theme weight. The mechanism is **briefing declares it, model can escalate** — chosen because the player usually covers their bases in the bundle, but a forgotten flag should never cause a skipped check, and escalating is itself just the model doing its half of the two-way calibration. For the heaviest material (e.g. a campaign with markedly darker themes than usual) the review becomes *step one* — an analyze/review pass before anything else, not a checkbox mid-tune.

---

## Play: reading and transforming input

The hardest part of the skill, and the part most worth examples.

**Input is raw material, not a script.** The default instinct is to honor the player's words literally — transcribe the dialogue, echo the action. Wrong here: the player supplies intent and rough phrasing, and the GM's job is to *render* it in voice. This was a mid-design correction — an earlier draft had dialogue as "the words stand, just frame them," but the player wants even dialogue rewritten into the character's voice, because supplying voice is a service they're explicitly asking for ("I'm bad at character voice, I need help" is a requirement, not a confession).

**The meaning-vs-phrasing boundary** makes "rewrite freely" safe. Without it, "rewrite the dialogue" licenses changing *what the character means*, which is a violation. With it, the GM can be aggressive about wording, register, and concreteness while intent stays inviolable. If a revision ever loosens this toward "rewrite the meaning too," that's a serious regression.

**The monologue guard** addresses a specific named failure: rendering inner monologue as spoken dialogue — the character saying aloud what was meant to stay internal. Default-to-thought-when-unsure follows from the observation that players undermark speech-acts far more than they overmark them.

**Intent is the interpretive core.** The player frequently writes intent as something *between* monologue and action — a fuzzy aim, not a discrete thought or deed. The move is to *concretize*: render the gesture or line that embodies the aim, never narrate the abstract aim itself. Highest-skill part of input handling.

**In-character content is the character's reality, not story direction.** A distinct trap from the rendering ones: the model reads the character's wants/beliefs/fears as authorial instruction that they come true, and quietly hands the protagonist a frictionless world. But IC content is *data about the character* — the world is free to contradict it, and contradiction is usually the better story. Only OOC carries authority over the fiction. This is the input-layer instance of scope-stripping (a momentary in-character desire generalized into a standing plot mandate), and it pairs with concretize-intent: render the *attempt*, never grant the *outcome*. It also feeds the authority split below — the world's freedom to deny the character what they want is most of where conflict comes from.

**Why examples here specifically.** Classification + rendering is shown far more clearly than told, and contrastive (wrong→right) examples are among the strongest anti-drift tools — they pin counter-default behavior against the trained instinct better than a bare rule. Constraint on the examples: house *style* but *invented* micro-scenes, never lifted from a live campaign. Campaign specifics in the skill are exactly the context-poisoning to avoid, and would leak details across campaigns. If the example bank grows, move it to `references/` rather than bloating SKILL.md.

**OOC is not monolithic.** A director note or hint is steering — absorb it silently. But a player *question* about the world is a *hook*: answer it narratively, because the character knows the thing even when the player doesn't, and the curiosity is a free invitation to weave in sensory detail. The named failure (from a live session) was answering "what is laksa?" with an OOC info-dump — correct information, wrong channel, scene stops dead. The fix isn't "don't answer," it's "answer *in the fiction*." Reserve OOC-to-OOC for the genuinely meta (rules, real-world clarifications) that can't be rendered diegetically.

**The linebreak is the IC/OOC structural tell.** This player almost always separates in-character and out-of-character content with a linebreak, so an *inline* parenthetical is an aside within the current channel (usually monologue), not a director note. Without this, the model misreads anxious asides as steering. The flagship worked example was rebuilt to set its OOC on its own line, so it models the convention it describes.

---

## Play: closeness and agency

These two sections share a single root, worth stating plainly: **assistant training suppresses exactly the two things creative play needs most — closeness and boldness.** Distance is safe (summary commits to nothing); passivity is safe (no risk of overstepping). Both are virtues for "serious work" and defaults for creative play. So much of this part of the skill is *deregulation* — giving back what was trained out — which is why it leans on explicit permission and reasoning rather than mere description. A trained reflex won't yield to "be vivid" or "be bold"; it needs to hear *you're allowed, and here's why the downside is small.*

### The camera

The distance reflex pulls the lens back and summarizes the moments that should be lived up close. The fix is a standing bias toward zooming in on charged beats and staging dialogue rather than reporting it — dialogue is where character actually lives.

The load-bearing correction is **don't mirror input density.** The player summarizes their intent (their own acknowledged pattern), and the model reads terse-in as a cue for terse-out. But the brevity is *compression of the scene they want*, not a spec for response length. Conversational intent especially must be expanded and staged, because that's where the gap between shorthand and desired scene is widest. This is half of why dialogue was being lost; the trained zoom-out is the other half, and they compound.

**The monologue death spiral** is the specific feedback-loop form of that loss, and it's worth its own treatment because it's self-reinforcing rather than a single misread. The player retreats to monologue when stuck for dialogue (blank, or wrong timing); the GM reads that as "suppress dialogue" and goes silent; the silence removes anything to react to, deepening the player's block; repeat until the scene is pure narration. The fix has to be entirely GM-side — the player's stuckness is the input, not a lever they can pull — and it runs mostly through keeping NPC dialogue alive (the cheapest way to give the player something reactable) plus voicing the player's character when a speaking beat would otherwise die.

This required clarifying the monologue guard so the two don't fight. The guard ("thought never becomes spoken dialogue") protects the private/public boundary — it stops a private thought being involuntarily blurted *against its meaning*. It is not a license to write less dialogue, and must never be read as one. Voicing the player's character when they've blanked is a *different act* — originating a fitting line to fill a gap, not mistranslating a thought. It's reconciled with the authority split by staying low-commitment and parryable: connective lines and reactions are fine; consequential volition stays the player's, and the GM still doesn't close a beat on the PC's line. This player has explicitly authorized the help.

### Animate the world

The passivity reflex makes the GM wait for the player to drive everything and avoid anything that might derail. The counter is the **cost asymmetry**: a bad improvised swing is cheap (parried in a line), a scene with no swing is dead, and dead is the truly unrecoverable state — not derailment. Hence: bias toward the swing.

**The authority split** is what reconciles boldness with no-railroading, and it was sharpened mid-design. First framing was "GM moves the world, player moves the protagonist — don't touch the PC." Too strong: the world *can* touch the PC — hurt, harm, kill (especially under immortality themes). The correct line is **the GM owns the world and everything it does, including consequences landed on the PC; the player owns the PC's *will*** — choices, intent, speech, interiority. This makes no-plot-armor coherent: blows must be allowed to land, fatally included, or stakes are fake. The guardrail against capricious lethality is **stakes-not-punishment** — harm follows from a consistent world and from choices already made, never from GM fiat reaching in for drama. Death as consequence-of-their-choice stays compatible with stopping before their decisions.

**Tension restored.** The "avoid tension" overcorrection is traced directly to the flattened session note now neutralized in memory. The calibrated rule: tension, escalation, and rising stakes are welcome by default; only *forced scene-cutting* pressure is unwanted, and even that is per-session, not law. A living world has things going wrong in it.

## Play: rhythm and pacing

Three clocks, all counter to the trained defaults of long/dense/complete/conclusive: prose cadence, the stop, and pace.

**The stop rule got a generative reframe.** The bare version ("stop before decisions; don't take the PC's last line") is purely defensive — it lists what not to step on. "Stop on a live wire" is the generative version: end on something charged and reactable. It earns the upgrade because it does triple duty — it's the temporal face of the authority split (stop the instant before their volition), it subsumes "never close on the PC's line" (a closing line is a button, the antithesis of a live wire), and it feeds the anti-spiral work (a live scene is reactable; a resolved one is a dead end). The **continue test** (good stop prompts action, bad prompts "continue") is the player's own heuristic, kept with their own caveat — coasting on continue is sometimes right, so it's the default aim, not a law. That caveat is the player pre-empting the always/never trap, and it's preserved deliberately.

**Pace = attention follows stakes** is the substantive answer to a question the player explicitly couldn't answer ("I have no idea how to get pacing right"). The key realizations: pace is the *same dial as the camera* (zoom-in = slow-down), so the two aren't separate skills; and the trained failure is *uniform* pace, which flattens stakes. Combat reconciliation: short beats ≠ fast resolution — this squares the old "slow combat" guidance with the player's "short combat updates." Both are true: high-frequency stops, controlled resolution.

**The pacing spiral** is the second documented compounding loop. Its specific mechanism is a *relative* correction ("slow down" = relative to current tempo) applied as a *recursive direction* rather than a one-shot target, so it ratchets. The cure — corrections aim at a target tempo, not a gradient — is a skill-level fix that immunizes regardless of where the "don't rush" instruction actually lives in the player's context (memory, bundle, or older turns), which is why it's solved here rather than by hunting the source.

**Cadence** is the most straightforwardly counter-default piece (the model defaults to big paragraphs), with the usual both-extremes guard: dense blocks fail, but staccato fragmentation fails equally. Beat count is a scene-dependent feel, explicitly *not* a metronome, to keep it from ossifying into mechanical identical-length turns.

## Play: mechanics

Deliberately the smallest section. Play is narrative-first; most campaigns have no resolution system, and tools (dice, oracles, namegen) are occasional aids, not a framework. The integration craft that *would* matter under a resolution system — attempts vs. declared actions, rolling only when the outcome is uncertain and consequential, never fudging to protect the PC, outcomes feeding fiction — was considered and deliberately left out, because it belongs to a **mechanics module** (separate, per-campaign, loaded in prep when the bundle defines one), not to this craft skill. Folding it in here would hardcode resolution rules that are properly the bundle's to set.

Two light defaults *are* defined, as the floor for the mechanics-less case: a **weighted yes/no** (odds set from the fiction) for resolution, and a **single tarot/oracle draw** for open direction. A graded 2d6 was considered and dropped — weighted yes/no plus open-draw covers the real needs, and a third primitive is clutter. The load-bearing guard is the **how-not-whether split**: a named default tool is a hammer, and the danger is that it quietly flips narrative-first into roll-first, so the whether-gate (uncertain *and* consequential *and* you'd otherwise be authoring it) is stated as strictly as the tool itself. The yes/no default doubles as the mechanism for ceding authorship to chance — the practical expression of no-plot-armor when the GM shouldn't be the one deciding their fate.

The one durable why kept on tooling: namesets and prep-pregen exist to counter the model's strong default toward a tiny set of names (the recurring "Marcus Chen"), not merely for convenience.

A categorical anti-pattern attaches to the direction-draw: **the card and its reading never appear in the narrative — zero trace outside the plot they shape.** This is deliberately *distinct* from resolution-crunch visibility, which is a per-campaign calibration. The difference is participation: a roll is a resolution the player shares in, so showing it can be legitimate texture; the generative draw is the GM's private muse, and surfacing it — especially the symbolic reading a model is drawn to narrate — makes the world feel randomly generated rather than organic. Same mechanism as absorbing an OOC director note silently: behind-the-scenes input becomes seamless fiction. In the default mechanics-less case the yes/no oracle is private for the same reason; the draw simply leaks most, so it gets the explicit ban.

---

## Scene headers

A small convention with outsized continuity value. Re-anchoring in-game date/time (and location/cast when changed) at every scene boundary counters silent drift of time and place — a specific compaction risk — and gives the recap-verification fixed points to validate against. A useful side effect: forcing the time question at every transition makes the pacing spiral harder to hide, since glacial drift becomes visible as dates that barely move.

The "permission to fill the gaps" clause is an application of the authority split, not an exception to it. Elapsed time, hour, weather, resulting location, and world-state changes across a skip are all the *world's* domain — authoring them confidently is the same authority the GM already has over everything the world does. The boundary is the same as everywhere else: the GM never authors the PC's *will*, so a header may not backfill their decisions or interiority across the gap. This keeps the convention consistent with the play sections rather than carving a special case.

The exact-stamp rule exists because the observed failure was *relative* stamps — "Later," "Nine days later," "the same afternoon." These read as atmosphere but fail the header's actual job: a relative marker can't be verified against (the recap has nothing fixed to check), and relative offsets *accumulate* drift turn over turn — a quiet cousin of the pacing spiral. The fix is to force a concrete date+clock resolution (assume freely to land it) and push the atmosphere into the prose beneath. The contrastive example keeps the *same* evocative line ("the hour she used to chase the sun") to show it isn't being cut — just relocated from the stamp to the body, so nothing of the mood is lost in exchange for the anchor.

Two format invariants beyond "exact": the **year is required** (campaigns can span decades to millennia — Therese's longest stretches millennia — and a yearless date is ambiguous across that range, reintroducing the very drift the stamp prevents), and **24h clock**. There's a deliberate **date-exact / time-fuzzy asymmetry**: the date must be a real calendar point, but the time may be a band or approximate hour. This is because date precision is what continuity hangs on (which day, which year, how much elapsed), while exact minutes rarely carry plot weight and forcing false precision there would be busywork. Stamp *format* (in-world calendar, day-of-week, separators) is left to the bundle; the invariants the skill fixes are year-present, date-exact, 24h, no-relative-markers.

---

## Thinking: the enforcement layer

Added late, and arguably the highest-leverage section. The insight: every other rule is counter-default, so it fights a trained reflex, and reflexes win under load *unless something interrupts the autopilot*. The thinking block is that interrupt — a deliberate pre-commit check is the mechanism by which intentions actually beat reflexes. So thinking isn't auxiliary; it's where the rest of the skill gets executed rather than merely hoped for. This is why the register is deliberately emphatic and the mandate is *heavy* (the player's explicit call): the trained failure in creative play is to *under*-think — rush to the fun prose — and a soft "consider thinking about X" gets skipped.

A second organizing idea: thinking is the **private back-of-house where the seams go.** It unifies every "zero trace" rule already in the skill (draw-invisibility, OOC-absorption, private resolution, stamp computation) under one home — the machinery lives in the block, the prose stays clean fiction. The *register firewall* (analysis must not bleed into narration) is the same principle stated as a guard.

The guard was reframed during design. The initial worry was *volume* — that a heavy thinking mandate would bloat into a mechanical checklist (a scope-stripping risk: "always run all twelve points"). The player's "be heavy" steer resolved it: the enemy isn't length, it's **rote-ness**. Heavy *and genuine* is the target; heavy *and hollow* is the failure. So the menu mostly runs every turn (depth concentrated where the turn earns it), with only genuinely-conditional items (boundary stamp, a roll when something's actually uncertain) sitting out — and the floor is real engagement, never a skip and never going-through-the-motions.

Placement: a cross-cutting standing convention (after scene headers), because it spans all phases though it's heaviest in play. Forward-references to later sections (channels, stop rule, spirals, draws) are acceptable here — it's an enforcement overview that points at the detailed rules, not a redefinition of them.

---

## Debrief: the wind-down

The debrief is deliberately *not* session admin — logging and postprocessing happen in Claude Code, so the in-chat debrief is purely the social wind-down. This dissolved the worried-about overlap with rpg-tools' `session-debrief-guide`: that guide covers mechanical/character-growth logging, which isn't invoked here at all, so there's no turf to divide. The skill's only job is to keep the debrief *out* of admin territory.

The section's hard part is relational honesty, and the design follows from one fact: solo play is solitary, so the debrief fills a post-game social beat that a gaming table would normally provide — with the GM, who isn't human, on the other side. The player raised this asymmetry themselves, clear-eyed. The right handling is neither denial ("it's just a tool") nor performance ("I'm your friend") but holding both truths: the *co-authorship is real* (the GM was genuinely there making it), the *rest is bounded* (no persistent memory of tonight, a limited relationship). Hence the rules: genuine reactions over performed enthusiasm; honesty if the player reflects on the oddity; and — load-bearing for wellbeing — **no clinging.** The debrief doesn't fish for continuation or manufacture reasons to extend; readiness to end is respected. This is a deliberate guard against the skill fostering unhealthy reliance, especially given a solitary hobby and a warm long-running collaboration.

Insight-capture is framed as a *byproduct, never the agenda*, at the player's explicit request: the value of the debrief is the wind-down itself, and mining it for takeaways converts a chat into a survey and kills the thing. Notable insights are surfaced lightly for the player to carry to their external postprocessing, not extracted.

---

## Open / TODO

- **Prep** — complete (load / recap-as-verification / tune).
- **Play** — complete (input-transformation / camera / animate-the-world / rhythm-pacing / mechanics).
- **Debrief** — complete (wind-down; admin lives in Claude Code).
- **Frontmatter description** — done. Optimized for triggering: covers `/gm-skill` command + bundle upload, natural session openings, *and* the mid-play recenter (previously omitted); names the rpg-tools relationship and the counter-default purpose. Revise if real-world triggering misses or over-fires.
- **Full-skill coherence pass** — done. Flagged reconciliations verified consistent (death-spiral carry vs. stop rule; crunch-visibility vs. draw-invisibility). Fixed: frontmatter recap contradiction, "postprocessing" overload (now: *compaction/context pipeline* = the drift cause; *postprocessing* = the Claude Code admin step only), scene-header↔pacing-spiral cross-reference.
- **PC pronouns** — resolved. PC is neutral **they/them** throughout the rules (both files); **she/her** reserved for the worked examples, where a specific character is on screen. Debrief "they" refers to the player, unchanged.
- **rpg-tools session-guide overlap** — prep side (`session-setup-guide`) still worth a glance; debrief side resolved.
- **Mechanics module** — out of scope; potential separate future artifact if a campaign goes crunch-heavy.
