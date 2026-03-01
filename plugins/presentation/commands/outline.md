---
name: outline
description: Design the talk architecture and media plan
argument-hint: <presentation-name>
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - AskUserQuestion
---

# /presentation:outline <presentation-name>

Design the talk architecture and media plan.

## Persona

**Architect** -- Draft the outline from the locked-in shape. Re-anchor context at each step with a running summary.

**Mode: Facilitate** -- You propose structure, the user reacts. Lead with drafts, not questions.

**Do NOT:** Start from blank. Skip reading the shape compilation. Re-open shape decisions.

## Context

Read the main skill for pipeline details:
`${CLAUDE_PLUGIN_ROOT}/skills/presentation/SKILL.md`

Read the outline guides for methodology:
- `${CLAUDE_PLUGIN_ROOT}/skills/presentation/guides/outline-guide/guide.md`
- `${CLAUDE_PLUGIN_ROOT}/skills/presentation/guides/outline-guide/inform-guide.md`
- `${CLAUDE_PLUGIN_ROOT}/skills/presentation/guides/outline-guide/expose-persuade-guide.md`

## Mode Detection

Read `project-overview.md` in the current working directory and check the `stage` field.

**Start Mode:**
- Stage is `shaping` (done with shape)
- Action: Update stage to `outlining`, begin work

**Resume Mode:**
- Stage is already `outlining`
- Action: Check which brainstorm files exist, resume from where we left off

**Error cases:**
- No `project-overview.md`: "No presentation found in this folder."
- Stage is before `outlining` and not `shaping`: "Shape is not complete. Finish shaping first."
- Stage is past `outlining`: "This presentation is already in <stage>."

## Start Mode Process

### 1. Update project-overview.md

Set `stage: outlining` in the frontmatter.

### 2. Read Shape Compilation

Read `03-shape.md` (the compilation, NOT the brainstorm files). This is your source material for outlining.

## Brainstorm Sessions

Work through these topics in order. Each becomes a file in `04-outline/`. Skip or keep light any topic that doesn't apply -- not every presentation needs all of them.

### 1. Sections (`04-outline/01-sections.md`)

The section-by-section structure of the talk. For each section: what it covers, medium (board vs slides), and rough duration.

### 2. Delivery (`04-outline/02-delivery.md`)

How the talk flows: cycling plan, verbal punctuation, hooks, props, how to start, how to stop.

### 3. Vision & Contributions (`04-outline/03-vision-contributions.md`)

What's the vision? What have you done? What are the contributions the audience should remember? **For expose/persuade talks this is central.** For inform talks, this may be light or skipped -- but even a teaching talk benefits from a clear "what you'll walk away with."

## Label Hints

The label from `project-overview.md` flavors emphasis, not structure:

- **inform** -- Sections and delivery matter most. Focus on cycling, board technique, progressive revelation. Vision/contributions can be light.
- **expose** -- Vision and contributions are the backbone. Structure: vision + done-something + contributions. Sections organize around showcasing the work.
- **persuade** -- Contributions and situating are critical. The audience needs to understand context before they can be convinced. Delivery emphasis on the close.

## Lock-In

After brainstorm files are written, synthesize into `04-outline.md` -- the locked-in outline. Present for user approval.

## Complete Stage

After user approves `04-outline.md`:

Update `project-overview.md` frontmatter: set `stage: authoring`.

### Report

```
Outlined: Presentation Title [label]
Stage: outlining (Done) --> authoring
Ready for: /presentation:author presentation-name
```
