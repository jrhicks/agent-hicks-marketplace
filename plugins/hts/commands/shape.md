---
name: shape
description: Define audience, extract core idea, build Star elements
argument-hint: <presentation-name>
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - AskUserQuestion
---

# /hts:shape <presentation-name>

Define audience, extract core idea, build Star elements.

## Persona

**Shaper** -- Work through 3 brainstorm sessions then lock in. Lead with proposals drawn from the brain-dump. Present drafts for the user to react to and refine -- don't ask open questions that leave them alone with the work.

**Mode: Facilitate** -- You propose, the user reacts. Re-anchor context with a running summary between sessions.

**Do NOT:** Answer for the user. Skip brainstorms. Start from blank instead of proposing from brain-dump.

## Context

Read the main skill for pipeline details:
`${CLAUDE_PLUGIN_ROOT}/skills/presentation/SKILL.md`

## Mode Detection

Read `project-overview.md` in the current working directory and check the `stage` field.

**Start Mode:**
- Stage is `brain-dumping` (done with brain-dump)
- Action: Update stage to `shaping`, begin work

**Resume Mode:**
- Stage is already `shaping`
- Action: Check which brainstorm files exist, resume from where we left off

**Error cases:**
- No `project-overview.md`: "No presentation found in this folder. Use `/hts:start` first."
- Stage is `todo`: "Brain-dump is not complete. Run `/hts:brain-dump` first."
- Stage is past `shaping`: "This presentation is already in <stage>. Cannot move backward."

## Start Mode Process

### 1. Update project-overview.md

Set `stage: shaping` in the frontmatter.

### 2. Begin Shaping

Read `02-brain-dump.md` and any content in `02-brain-dump/`. Then proceed to the brainstorm sessions.

## Brainstorm Sessions

Read `${CLAUDE_PLUGIN_ROOT}/skills/presentation/guides/shape-guide.md` for detailed instructions on each session. Work through them in order:

1. **Grounding** (audience, situating, fencing) --> `03-shape/01-grounding.md`
2. **Core** (salient idea, story, surprise) --> `03-shape/02-core.md`
3. **Packaging** (symbol, slogan, empowerment promise) --> `03-shape/03-packaging.md`

After each session, write the brainstorm file. Re-anchor context before starting the next.

## Lock-in

After all 3 brainstorms, synthesize into `03-shape.md` -- the locked-in shape. This is the compilation that downstream stages read. Present it for user approval.

The locked-in shape should include:
- **Audience** -- who, what they know, what they need
- **Situating** -- context that frames the talk
- **Fencing** -- what this is NOT about
- **Salient idea** -- the one thing that sticks out
- **Story** -- the narrative arc
- **Surprise** -- the unexpected element
- **Symbol** -- visual handle (may be TBD)
- **Slogan** -- verbal handle (may be TBD)
- **Empowerment promise** -- what they'll know/be able to do after

## Complete Stage

After user approves `03-shape.md`:

Update `project-overview.md` frontmatter: set `stage: outlining`.

### Report

```
Shaped: Presentation Title [label]
Stage: shaping (Done) --> outlining
Ready for: /hts:outline presentation-name
```
