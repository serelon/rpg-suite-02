---
name: session-postprocess
description: |
  Interactive session post-processing with discovery, validation, and modular capture.
  Extracts summaries, savefiles, memories, locations, characters, and campaign-specific
  content from session exports. Guides bundle template organization.
  Triggers: "/postprocess", "process this session", "postprocess session N"
---

# Session Post-Processing

Interactive workflow for processing session exports into structured campaign content.

## When to Use

- After a session has been played and exported
- You have a session export (JSONL) ready
- Want to extract and organize session content with review checkpoints

## What This Skill Produces

**Universal outputs:**
- Summary - narrative or tactical session overview
- Savefile - continuation state for next session (merged with previous)
- Memories - selected moments worth preserving
- Locations - new or developed places

**Campaign-specific outputs** (based on `postprocess-instructions.md`):
- Stories (oral traditions, tales)
- Timeline updates (non-linear campaigns)
- Data restoration (tactical campaigns)
- Verification checklists
- Custom outputs as defined

---

## Phase 1: Setup

Gather context and confirm what we're processing.

### Step 1.1: Identify Campaign and Session

If not provided, ask:
> "Which campaign and session number are we processing?"

**Check for existing session context:**

Look for existing session config or bundle JSON that might identify the branch:
```bash
ls campaigns/[name]/bundles/*/session*.json
ls campaigns/[name]/branches/*/session*.json
ls campaigns/[name]/branches/*/*/session*.json
```

If found, read it to extract:
- Branch context (e.g., `branches/leviathan/david/session-58.json`)
- POV character(s)
- Which template hierarchy applies

> "Found existing session config at `[path]`.
> Branch: [branch name]
> POV: [character(s)]
> Using this context for postprocessing."

### Step 1.2: Create Git Branch

Create an isolated branch for this work.

**First, check for unpushed commits on master:**
```bash
git status
git log origin/master..master --oneline 2>/dev/null
```

If there are unpushed commits on master:
> "Master has unpushed commits. Push them first to avoid including unrelated work in the PR."
> ```bash
> git push origin master
> ```

**Then check for uncommitted changes:**

If there are uncommitted changes:
> "You have uncommitted changes. Options:"
> 1. Stash them (`git stash`)
> 2. Commit them first
> 3. Proceed anyway (changes will mix with postprocess work)

**Create the branch:**
```bash
git checkout -b postprocess/[campaign]-s[N]
```

> "Created branch `postprocess/[campaign]-s[N]` for this work.
> All changes will be isolated until we verify and merge."

### Step 1.3: Load Campaign Context

Read in parallel:
- `campaigns/[name]/primer.md` - themes, structure
- `campaigns/[name]/CLAUDE.md` - campaign instructions
- `campaigns/[name]/postprocess-instructions.md` - processing additions/exceptions (if exists)

Note what the campaign needs:
- Is it non-linear? (timeline updates required)
- Does it have stories? (story extraction)
- Tactical campaign? (data restoration, checklists)
- Custom memory density? (sparse vs. standard)

### Step 1.4: Find Session Export

Look for the export file:
```bash
ls campaigns/[name]/imports/*session*[N]*.jsonl 2>/dev/null
ls campaigns/[name]/imports/*.jsonl 2>/dev/null
```

If multiple candidates, ask user to confirm which one.

**Note:** Export filenames often contain "prep" in the name (e.g., `Claude_export_Emberfall campaign session 06 prep_...jsonl`). This does not mean the file only contains prep — the session was played in the same conversation as the prep. Treat "prep" in the filename as normal and proceed; do not flag it as a concern.

### Step 1.5: Preprocess if Needed

Check for existing chunks:
```bash
ls campaigns/[name]/imports/chunks/session-[N]-manifest.txt
```

If missing, run preprocessing automatically:
```bash
python tools/preprocess_export.py campaigns/[name]/imports/<export.jsonl>
```

### Step 1.6: Load Previous Savefile

Find the most recent savefile for continuity:
```bash
ls campaigns/[name]/Savefiles/*-save-s*.md | sort -V | tail -1
```

Read it to inform the new savefile - maintain:
- Established relationships (update, don't replace)
- Open threads (resolve or carry forward)
- Character state (build on, not reset)
- Custom sections (preserve and update)
- Dormant content (threads/items not relevant this session but still tracked)

### Step 1.7: Confirm Before Discovery

Present what we're about to do:
> "Processing session [N] for [campaign].
>
> Previous savefile: [filename] (for continuity)
> Campaign expects: [summary, savefile, memories, locations, + campaign-specific]
> Chunks: [count] ready
>
> Ready to run discovery?"

---

## Phase 2: Discovery

Read all chunks and extract session content directly.

### Step 2.1: Read All Chunks

Read the manifest to get the chunk list:
```bash
cat campaigns/[name]/imports/chunks/session-[N]-manifest.txt
```

Then read ALL chunks in order using the Read tool. Read them sequentially — each chunk builds on the previous.

**Anti-recency-bias discipline:** As you read, build a running timeline. Early session content matters as much as late. Do not let the final chunks dominate your extraction just because they're freshest in context.

### Step 2.2: Extract Candidates

After reading all chunks, extract candidates for:

**UNIVERSAL:**
- **Characters:** Who appeared? New, returning, or developed?
- **Locations:** Places visited or established? New or developed?
- **Memories:** Emotional beats, turning points, sensory moments, relationship pivots
- **Summary beats:** Key events in chronological order

**CAMPAIGN-SPECIFIC:**
Follow `postprocess-instructions.md` — e.g., stories, timeline data, etc.

Structure your findings as:

**TIMELINE:**
- [Chunk 1-2] Event: ...
- [Chunk 3-4] Event: ...
- (etc., covering early/mid/late session)

**CHARACTERS:**
- New: [name] - [role/significance]
- Returning: [name] - [what happened with them]
- Developed: [name] - [how they grew/changed]

**LOCATIONS:**
- New: [name] - [type, significance]
- Developed: [name] - [what changed/was revealed]

**MEMORIES (candidates):**
- [title] ([type]) - [why significant]

**SUMMARY BEATS:**
- [Chronological key events]

[CAMPAIGN-SPECIFIC sections as needed]

### Step 2.3: Self-Check Extraction Quality

Before presenting to the user, verify your own extraction:
- Timeline covers early, middle, AND late session
- Character list seems complete
- Memory candidates span the session (not clustered at end)

If you notice gaps, re-read the relevant chunks before proceeding.

---

## Phase 3: Validation

Present findings by category for user review.

### Step 3.1: Characters

Present extracted characters:
> **Characters found in session [N]:**
>
> **New:**
> - [name] - [role/significance]
>
> **Returning:**
> - [name] - [what happened]
>
> **Developed:**
> - [name] - [how they changed]
>
> "Which characters should we capture/update profiles for?
> Any miscategorized or missing?"

User can:
- Confirm all
- Select subset ("just the new ones")
- Add missed characters
- Skip characters entirely

### Step 3.2: Locations

Present extracted locations:
> **Locations found:**
>
> **New:**
> - [name] - [type, significance]
>
> **Developed:**
> - [name] - [what changed]
>
> "Which locations should we capture? Any missing?"

User can select, skip, or add.

### Step 3.3: Memories

Present memory candidates:
> **Memory candidates ([count]):**
>
> *Vivid moments:*
> - [title] - [brief why]
>
> *Relationship:*
> - [title] - [brief why]
>
> *Sensory/atmosphere:*
> - [title] - [brief why]
>
> *Event summaries:*
> - [title] - [brief why]
>
> Campaign guidance: [e.g., "AEGIS: sparse, 3-5 tactical moments"]
>
> "Which memories should we capture? Aim for [N] based on campaign."

### Step 3.4: Campaign-Specific

Present any campaign-specific findings:

**For Eternal Witness (stories + timeline):**
> **Stories found:**
> - [title] - told by [character], about [subject]
>
> **Timeline data:**
> - Era: [extracted timeframe]
> - Follows: [relationship to other sessions]

**For AEGIS (data + checklist items):**
> **Data export found:** [yes/no, path]
>
> **Checklist items to verify:**
> - Wounds recorded: [names]
> - KIA recorded: [names]
> - Intel updates: [items]

### Step 3.5: Confirm Capture Plan

Summarize what we're capturing:
> **Capture plan for session [N]:**
>
> - Summary: yes
> - Savefile: yes (updating from [previous])
> - Characters: [count] ([names])
> - Locations: [count] ([names])
> - Memories: [count] selected
> - [Campaign-specific]: [details]
>
> "Ready to start capturing? Or adjust the plan?"

---

## Phase 4: Capture

Work through selected categories sequentially. Each: draft → review → adjust → finalize.

**Core character guardrail:** Protagonists, companions, and other core characters have carefully crafted profiles (voice, personality, psychological state) that are load-bearing. **Do not update core character profiles** unless the user explicitly requests it. New characters and supporting NPCs are fine to create freely. If session events warrant core character updates, flag them for the user rather than applying automatically. See Step 4.5d for details.

**Escape hatches available at any step:**
- "skip" - skip this category, move to next
- "later" - come back to this after other categories
- "stop" - pause capture, can resume later

### Step 4.1: Summary

Draft the session summary using extracted timeline beats.

**Length: one page maximum for the prose summary.** Aim for ~3KB total file size including all sections. Information density is the goal — every sentence should carry weight.

**What belongs in a summary:**
- State changes: new relationships, new locations, jobs taken, names changed, money spent, people met who'll matter again
- Decisions that close off or open up future paths
- Turning points in character arcs or relationships
- Threads advanced, resolved, or introduced
- The emotional shape of the session (arc, not scene-by-scene)

**What does NOT belong:**
- Flavor moments, atmosphere, scenic description (these go in memories)
- Comedic asides and small character beats (unless they shift something)
- Blow-by-blow of conversations, shopping trips, training montages
- Moment-to-moment narration — summarize the outcome, not the process

**Test: "Will this matter in 10 sessions?"** If a detail won't affect future play, continuity, or character state, it belongs in a memory or nowhere — not the summary.

**Format varies by campaign:**
- Narrative campaigns: story-focused with themes and character growth
- Tactical campaigns: mission-focused with outcomes and intel

See [Reference: Output Formats](#reference-output-formats) for templates.

Present draft:
> **Session [N] Summary draft:**
>
> [Draft content]
>
> "How does this look? Adjustments?"

After approval, write to `campaigns/[name]/Sessions/session-[N]-summary.md`

### Step 4.2: Savefile

The savefile is a **merge operation**, not a fresh write.

**Step 4.2a: Analyze previous savefile structure**

Read the previous savefile and identify:
- Standard sections (Current Situation, Active Relationships, Goals, Open Threads)
- Custom sections (campaign-specific: Roster Status, Inventory, Prophecies, etc.)
- Dormant content (threads/items not relevant this session but still tracked)

Present findings:
> **Previous savefile structure:**
>
> *Standard sections:*
> - Current Situation
> - Active Relationships
> - Open Threads
>
> *Custom sections found:*
> - [Section name] - [brief description]
> - [Section name] - [brief description]
>
> *Dormant content to preserve:*
> - [Thread/item not touched this session]
>
> "Any custom sections need special update instructions?"

**Step 4.2b: Draft updated savefile**

- **Update** sections affected by this session
- **Preserve** dormant content and unchanged custom sections
- **Add** new threads, relationships, items from this session
- **Close/archive** resolved threads (move to "Resolved" or remove based on campaign style)

Present draft with changes highlighted:
> **Savefile draft (changes from previous):**
>
> [Draft with annotations like "[UPDATED]", "[NEW]", "[PRESERVED]"]
>
> "How does this look? Anything to adjust or preserve differently?"

After approval, write to `campaigns/[name]/Savefiles/[character]-save-s[N].md`

### Step 4.3: Memories

Capture selected memories from validation phase.

**Step 4.3a: Read guides and draft memories**

**Read these files before drafting:**
- `prompts/memory-extraction-guide.md` — extraction philosophy, type descriptions, intensity guidance
- `templates/memory-template.md` — full JSON schema with all fields

Then for each selected memory, draft with full schema:
- id, title, type, era, session
- intensity, perspective, tags
- connections (characters, locations, related_memories)
- text (appropriate length for type — per the extraction guide)

**Step 4.3b: Present for review**

Show memories one at a time or in small batches:
> **Memory 1 of [N]: "[title]"**
>
> Type: [type] | Intensity: [intensity] | Perspective: [perspective]
> Tags: [tags]
> Connections: [characters], [locations]
>
> [Memory text]
>
> "How does this read? Adjustments to text, metadata, or connections?"

**Step 4.3c: Validate connections**

Before finalizing, check that referenced IDs exist:
- Characters in `characters/` folder
- Locations in `locations/` folder
- Related memories in `memories/` folder

Flag any missing references:
> "Memory references character 'kovacs' but no profile exists yet.
> Options: create stub during character capture, adjust reference, or leave as-is?"

After approval, write to `campaigns/[name]/memories/session-[N]-memories.json`

### Step 4.4: Locations

Capture new or significantly developed locations.

**Step 4.4a: Check existing locations**

Read `campaigns/[name]/locations/` to see what already exists.

For each location to capture:
- New location → create fresh profile
- Existing location → update/expand profile

**Step 4.4b: Read guide and draft location profiles**

**Read `rpg-tools/guides/location-guide.md` before drafting** — it defines the full JSON schema, hierarchy model, and connection types.

Draft each location with:
- id, name, type, parent (hierarchy)
- tags, minimal profile, full profile
- connections to other locations

Present draft:
> **Location: [name]**
>
> Type: [type] | Parent: [parent or "none"]
> Tags: [tags]
>
> *Minimal:*
> [1-2 sentence essence]
>
> *Full:*
> [Expanded description with atmosphere, purpose, notable features]
>
> *Connections:*
> [Related locations]
>
> "How does this look? Adjustments?"

**Step 4.4c: Consider hierarchy**

If multiple locations captured, consider relationships:
> "These locations have a hierarchy:
> - [Region] contains [Settlement] contains [Building]
>
> Should I set up parent relationships?"

After approval, write to `campaigns/[name]/locations/[id].json`

### Step 4.5: Characters

Capture new or significantly developed characters.

**Step 4.5a: Check existing characters**

Read `campaigns/[name]/characters/` to see what already exists.

For each character to capture:
- New character → determine profile depth needed
- Existing character → update/expand relevant sections

**Step 4.5b: Triage new characters**

Not every character needs the same depth:
> **New characters to capture:**
>
> *Full profile* (protagonist, major recurring):
> - [name] - [why full profile]
>
> *Minimal profile* (supporting, may return):
> - [name] - [role]
>
> *Note only* (one-off, background):
> - [name] - [brief note in session summary suffices]
>
> "Does this triage look right?"

**Step 4.5c: Read guide and draft character profiles**

**Read `rpg-tools/guides/character-guide.md` before drafting** — it defines profile structure, voice sample format, and section organization.

For full profiles, capture:
- Minimal block (role, essence, voice)
- Full block (background, personality, goals)
- Relevant sections (powers, relationships, etc.)
- Voice samples (if dialogue in session)

Present draft:
> **Character: [name]**
>
> *Minimal:*
> [Quick reference profile]
>
> *Full:*
> [Expanded profile]
>
> *Voice samples:*
> - "[Example dialogue from session]"
> - "[Another example]"
>
> "How does this look? Adjustments?"

**Step 4.5d: Update existing characters**

**CRITICAL: Core character protection**

Core characters (protagonists, companions, major recurring) have profiles refined across multiple sessions. Their voice samples, personality, and psychological state are carefully crafted and define how the character plays.

**Do NOT update core character profiles by default.** Instead, flag potential updates:

> **Potential updates to core character [name]:**
>
> This session's events suggest these changes:
> - [e.g., credits updated, new relationship, combat history]
>
> **These would require careful review:**
> - Voice/personality changes can break character feel
> - Existing content must be preserved (additive, not replacement)
> - Session-specific details should be generalized
>
> "Should I draft updates for review, or skip core character changes?"

If the user approves drafting, follow these rules:
- **Additive only** — new voice samples go alongside old ones, never replace
- **Never rewrite personality or voice** — these are load-bearing
- **Generalize, don't snapshot** — capabilities/descriptions should be timeless, not session-specific (e.g., "Reads people with forensic accuracy" not "noticed Jonah's bruises")
- **Preserve origin-state characterization** — early-session traits (defensiveness, testing behavior) coexist with growth, they don't get overwritten
- **Present the diff** — show exactly what changes before writing

For **non-core** returning characters (supporting NPCs, one-session contacts promoted to recurring):
> **Update to [name]:**
>
> *Current profile has:* [summary of existing]
>
> *This session adds:*
> - [New relationship]
> - [Changed goal]
> - [New voice sample]
>
> "Merge these updates? Or adjust?"

After approval, write to `campaigns/[name]/characters/[id].json`

### Step 4.6: Campaign-Specific Outputs

Handle outputs defined in `postprocess-instructions.md`.

**Stories (e.g., Eternal Witness):**

For each story identified in discovery:
> **Story: "[title]"**
>
> Collection: [told/private]
> Era: [when story is from/about]
> Source: [who tells it, where learned]
> Themes: [themes]
> Characters: [who appears in story]
>
> [Story text]
>
> "Capture this story?"

Write to `campaigns/[name]/stories/session-[N]-stories.json`

**Timeline (non-linear campaigns):**

> **Timeline entry for session [N]:**
>
> | Session | Title | Era | Duration | Follows | Notes |
> |---------|-------|-----|----------|---------|-------|
> | [N] | [title] | [era] | [duration] | [relationship] | [brief] |
>
> "Add this to timeline.md?"

**Data Restoration (e.g., AEGIS):**

> **Data export found:** `imports/session-[N]-data-export.zip`
>
> Will restore:
> - `data/roster.json`
> - `data/strategic.json`
> - `intel/enemies.json`
> - [etc.]
>
> "Run data restoration?"

Execute:
```bash
cd campaigns/[name]
unzip -o imports/session-[N]-data-export.zip "export/data/*" "export/intel/*" -d .
mv export/data/* data/ && mv export/intel/* intel/
rmdir export/data export/intel export
```

**Verification Checklists (e.g., AEGIS):**

> **Debrief verification commands:**
> ```bash
> tactical.py roster list --status wounded
> tactical.py roster get [NAME]  # for each casualty
> strategic.py overview
> ```
>
> "Run these now, or save checklist for later?"

**Custom Outputs:**

For any other campaign-specific outputs defined in instructions, follow the same pattern:
1. Present what was found
2. Draft the output
3. User reviews and adjusts
4. Write to appropriate location

---

## Phase 5: Bundle Integration

Review captured content and organize into bundle templates.

### Step 5.1: Review What Was Captured

Summarize the session's outputs:
> **Session [N] capture complete:**
>
> - Summary: `Sessions/session-[N]-summary.md`
> - Savefile: `Savefiles/[character]-save-s[N].md`
> - Memories: [count] in `memories/session-[N]-memories.json`
> - Locations: [count] new/updated in `locations/`
> - Characters: [count] new/updated in `characters/`
> - [Campaign-specific]: [details]
>
> "Ready to review bundle integration, or done for now?"

User can skip bundle integration entirely if not needed.

### Step 5.2: Analyze Current Template Structure

Read existing bundle templates:
- `campaigns/[name]/bundle-template.json` - base template
- `campaigns/[name]/templates/` - any existing nested templates

Present current structure:
> **Current bundle structure:**
>
> *Base template includes:*
> - Tools: dice.py, tarot.py, etc.
> - Characters: `characters/*.json`
> - Memories: `memories/*.json`
> - [etc.]
>
> *Nested templates found:*
> - `templates/locations/berlin.json` - Berlin-related content
> - `templates/factions/alpha-team.json` - Alpha team members
> - [or "None yet"]

### Step 5.3: Suggest Organization

Based on what was captured, suggest template organization:

**For new locations:**
> **New location "[name]" captured.**
>
> Options:
> 1. Add to base template (always included)
> 2. Create `templates/locations/[name].json` (include when relevant)
> 3. Create in `templates/archive/` (captured but not bundled by default)
>
> "How should this location be organized?"

**For new characters:**
> **New character "[name]" captured.**
>
> Detected associations:
> - Location: [if tied to specific place]
> - Faction: [if part of group]
>
> Options:
> 1. Add to base template (always included)
> 2. Add to `templates/locations/[place].json` (bundled with location)
> 3. Add to `templates/factions/[faction].json` (bundled with faction)
> 4. Create in `templates/archive/` (available but not default)
>
> "How should this character be organized?"

**For session summaries:**

Session summaries should be included in the branch bundle template so future sessions have access to prior session context.

> **Session summary captured.**
>
> Branch context: `branches/[branch]/`
> Suggest adding glob pattern to: `branches/[branch]/bundle-template.json`
>
> ```json
> {"src": "campaigns/[name]/Sessions/[branch]-session-*-summary.md", "dest": "summaries/"}
> ```
>
> This glob pattern will automatically include all session summaries for this branch.
> "Add session summaries to branch template?"

**For memories:**

**Default behavior:** If a branch context was identified in Step 1.1 (e.g., `branches/leviathan/david/`), suggest adding the memories file to that branch's bundle template. Memories belong to the POV character(s) who experienced them.

> **Session memories captured.**
>
> Branch context: `branches/[parent]/[pov]/`
> Suggest adding to: `branches/[parent]/[pov]/bundle-template.json`
>
> ```json
> {"src": "campaigns/[name]/memories/[branch]-session-*-memories.json", "dest": "memories/"}
> ```
>
> This glob pattern will automatically include all memory files for this branch.
> "Add memories to [POV]'s branch template?"

If no branch context, or memories are shared across branches:
> Memories are typically included via glob (`memories/*.json`).
>
> Any memories that should be location/faction-specific instead?
> (e.g., "The Berlin Cellar" memory only bundled with Berlin template)

### Step 5.4: Create/Update Templates

For each organizational decision, either create new template or update existing.

**Creating new nested template:**
```json
// templates/locations/[name].json
{
  "id": "[campaign]-location-[name]",
  "description": "Content related to [location]",
  "include": [
    {"src": "locations/[name].json", "dest": "locations/"},
    {"src": "characters/[associated-char].json", "dest": "characters/"}
  ]
}
```

**Updating existing template:**

Show diff preview:
> **Proposed changes to `templates/locations/berlin.json`:**
>
> ```diff
> {
>   "id": "aegis-location-berlin",
>   "include": [
>     {"src": "locations/berlin.json", "dest": "locations/"},
> +   {"src": "locations/the-bunker.json", "dest": "locations/"},
> +   {"src": "characters/kovacs.json", "dest": "characters/"}
>   ]
> }
> ```
>
> "Apply these changes?"

### Step 5.5: Archive vs Active

Clarify the distinction:
> **Template types:**
>
> *Active templates* - included in typical session bundles
> - Base template: always
> - Location/faction templates: when session involves that content
>
> *Archive templates* - captured but not bundled by default
> - `templates/archive/` - available for reference or future sessions
> - Useful for: one-off NPCs, visited-but-left locations, resolved plots
>
> "Any of this session's content should go to archive rather than active?"

### Step 5.6: Verify Bundle Still Works

After template changes, suggest verification:
> "Template changes complete. To verify the bundle still builds:"
>
> ```bash
> python tools/bundle.py campaigns/[name]/bundles/[next-session]/session.json --dry-run
> ```
>
> "Run this now?"

---

## Phase 6: Completion

Wrap up and confirm everything is in order.

### Step 6.1: Final Checklist

Present completion status:
> **Session [N] post-processing complete.**
>
> | Output | Status | Location |
> |--------|--------|----------|
> | Summary | ✓ | `Sessions/session-[N]-summary.md` |
> | Savefile | ✓ | `Savefiles/[character]-save-s[N].md` |
> | Memories | ✓ [count] | `memories/session-[N]-memories.json` |
> | Locations | ✓ [count] | `locations/` |
> | Characters | ✓ [count] | `characters/` |
> | [Campaign-specific] | ✓ | [location] |
> | Bundle templates | ✓/skipped | [changes made] |

### Step 6.2: Deferred Items

If any items were skipped or marked "later":
> **Deferred items:**
> - [Category]: [reason/notes]
>
> "Want to circle back to any of these now?"

### Step 6.3: Next Session Prep

Offer guidance for next session:
> **Ready for session [N+1]:**
>
> Savefile ready at: `Savefiles/[character]-save-s[N].md`
>
> To create next session bundle:
> 1. Create `bundles/session-[N+1]/session.json`
> 2. Run: `python tools/bundle.py <session.json>`
>
> Or use the session-bundle skill/agent.

### Step 6.4: Git Merge/PR

**Option A: Direct merge**
```bash
# Stage ONLY this session's outputs — never `git add -A`, which sweeps unrelated
# untracked files (stray transcripts, other campaigns' WIP, scratch files) into the
# commit. Stage the files you actually wrote/updated this run, e.g.:
git add campaigns/[name]/Sessions/session-[N]-summary.md \
        campaigns/[name]/Savefiles/[character]-save-s[N].md \
        campaigns/[name]/memories/session-[N]-memories.json \
        campaigns/[name]/imports/<export>.jsonl
# ...plus any characters/, locations/, notes/, transcripts/, or bundle templates
# this session touched. Then verify the index before committing:
git status   # confirm ONLY intended files are staged; nothing rode along
git commit -m "[campaign] session [N] postprocess"
git checkout master
git merge postprocess/[campaign]-s[N]
git branch -d postprocess/[campaign]-s[N]
```

**Option B: PR for review (recommended)**
```bash
# Stage ONLY this session's outputs — never `git add -A`, which sweeps unrelated
# untracked files (stray transcripts, other campaigns' WIP, scratch files) into the
# commit. Stage the files you actually wrote/updated this run, e.g.:
git add campaigns/[name]/Sessions/session-[N]-summary.md \
        campaigns/[name]/Savefiles/[character]-save-s[N].md \
        campaigns/[name]/memories/session-[N]-memories.json \
        campaigns/[name]/imports/<export>.jsonl
# ...plus any characters/, locations/, notes/, transcripts/, or bundle templates
# this session touched. Then verify the index before committing:
git status   # confirm ONLY intended files are staged; nothing rode along
git commit -m "[campaign] session [N] postprocess"
git push -u origin postprocess/[campaign]-s[N]
gh pr create --title "[campaign] session [N] postprocess" --body "$(cat <<'EOF'
## Session [N] Postprocessing

**Outputs:**
- Summary: `Sessions/session-[N]-summary.md`
- Savefile: `Savefiles/[character]-save-s[N].md`
- Memories: [count] captured
- Locations: [count] new/updated
- Characters: [count] new/updated
- [Campaign-specific outputs]

**Bundle changes:**
- [Template updates made]

---
Generated with session-postprocess skill
EOF
)"
```

> "PR created: [URL]
>
> Review the changes, then merge when ready.
> Or I can merge it now if you're satisfied."

After merge:
```bash
gh pr merge --merge
git checkout master
git pull
git branch -d postprocess/[campaign]-s[N]
```

### Step 6.5: If Abandoning

If something goes wrong and you want to start over:
```bash
git checkout master
git branch -D postprocess/[campaign]-s[N]
```

> "Abandoned postprocess branch. No changes were merged."

---

## Reference: Output Formats

### Summary Formats

**Narrative (default):**
```markdown
# Session [N]: [Title]

**Era/Timeframe:** [When]
**Setting:** [Where]

## Key Events
- [Event from early session]
- [Event from mid session]
- [Event from late session]

## Characters
**Introduced:** [Names]
**Developed:** [Names with brief notes]
**Lost/Departed:** [If any]

## Plot Threads
**Opened:** [New questions/tensions]
**Closed:** [Resolved]

---

## Extended

### Narrative Arc
[Numbered story beats]

### Themes Explored
- [Theme]: [How it manifested]

### Character Growth
- [Character]: [What changed]
```

**Tactical (AEGIS-style):**
```markdown
# AEGIS Session [N]: [Title]

**Date:** [Campaign date]
**Location:** [Mission location]

## Mission Summary
[2-3 paragraphs: objective, execution, outcome]

## Outcomes
- **Extracted:** [Items, intel, personnel]
- **KIA:** [Names]
- **WIA:** [Names with wound level]
- **Enemy:** [Casualties, observations]

## Intelligence Gained
- [Key intel]

## Open Questions
- [Mysteries]

---
*"[Thematic closing quote]"*
```

### Savefile Format

```markdown
# [Campaign] - Session [N] Save

**Era/Timeframe:** [Current state]

## Current Situation
[Where is the character? What just happened?]

## Active Relationships
- **[Name]**: [Current status]

## Immediate Goals
1. [What's next]

## Open Threads
- [Active tension/plot]

## Dormant Threads
- [Not currently active but still tracked]

## [Custom Sections]
[Preserved from previous savefile, updated as needed]

## Session Notes
[Context for continuation]
```

### Memory Schema

See `templates/memory-template.md` for full schema.

### Location Schema

See `rpg-tools/guides/location-guide.md` for full schema.

### Character Schema

See `rpg-tools/guides/character-guide.md` for full schema.

---

## Reference: Existing Guides

| Guide | Location | Use For |
|-------|----------|---------|
| Memory extraction | `prompts/memory-extraction-guide.md` | Types, intensity, connections |
| Memory format | `templates/memory-template.md` | Full JSON schema |
| Character creation | `rpg-tools/guides/character-guide.md` | Profile structure, voice samples |
| Location creation | `rpg-tools/guides/location-guide.md` | Hierarchy, connections |
| Story format | `templates/story-template.md` | Story collection schema |

---

## Integration

**Related skills:**
- `campaign-setup` - For formalizing new campaigns after session 01
- `workshop` - For creative exploration before/after sessions

**Replaces:**
- `session-postprocess` agent - This skill runs entirely in the main conversation
- `session-postprocess-v2` skill - Team-based variant (deprecated, context window now sufficient)
