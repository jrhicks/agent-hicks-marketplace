---
name: presentation
description: |
  Create presentations following Patrick Winston's how-to-speak methodology.
  Folder-as-presentation model with stage tracking via project-overview.md.
  Triggers: "/presentation", "presentation brain-dump", "presentation shape".
user-invocable: true
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
---

# /presentation

**A presentation is a folder.** The user creates a folder, cd's into it, and runs commands. `project-overview.md` in the current working directory tracks metadata and stage. No external board, no folder moves.

Create presentations using Patrick Winston's how-to-speak methodology. Presentations progress through stages from new through done.

**Methodology:** This process is grounded in Winston's MIT "How to Speak" lecture -- a practical framework for communication built on Knowledge + Practice + talent (talent smallest). The full reference lives in `${CLAUDE_PLUGIN_ROOT}/skills/presentation/guides/how-to-speak/`. Each stage integrates specific Winston techniques: empowerment promise and Star elements in shaping, cycling and verbal punctuation in outlining, slide crime avoidance and chalkboard sequences in authoring.

## Usage

```
/presentation:start <presentation-name> [--label inform|expose|persuade]
/presentation:brain-dump <presentation-name>
/presentation:shape <presentation-name>
/presentation:outline <presentation-name>
/presentation:author <presentation-name>
/presentation:chalkboard <sequence-name>
```

All commands operate on the current working directory. The user should cd into their presentation folder before running commands.

## project-overview.md Format

```yaml
---
title: "All-Hands Q1 Update"
label: inform
stage: new
---

**Topic:** What the presentation is about

**Audience:** Who this is for

**Type note:** Why this type was chosen
```

Stage values: `new`, `brain-dumping`, `shaping`, `outlining`, `authoring`, `done`

## Pipeline

| # | Stage | Verb | What Happens |
|---|-------|------|-------------|
| -- | Start | start | Setup -- create project-overview.md, introduce workflow |
| 02 | Brain-dumping | brain-dump | Raw content dump -- everything you know |
| 03 | Shaping | shape | Audience, core extraction, Star elements, fencing |
| 04 | Outlining | outline | Talk architecture, media plan (label-branched) |
| 05 | Authoring | author | Build slides in JS, iterate on PPTX directly |
| 06 | Done | -- | Presentation complete and delivered |

## Presentation Type Labels

- **inform** -- Teaching, lecturing. Board-primary. Knowledge transfer. Best tool: the board (speed matches absorption, graphic quality, empathetic mirroring).
- **expose** -- Job talks, conference talks. Slides-primary. Showcasing ideas/accomplishments. Structure: vision + done something + contributions.
- **persuade** -- Oral exams, pitches. Slides-primary. Establishing context and proving capability. Critical: situate your work first.

## Running Instructions (All Stages)

**Capture aha moments.** When a design conversation produces an insight -- about the topic, the audience, the medium -- append it to `discussion.md` in the presentation folder. Format:

```markdown
## YYYY-MM-DD -- <aha moment title>

<What changed in our thinking and why.>
```

Each dated entry is a snapshot. Don't rewrite old entries -- append new ones.

**Compilation files guide next steps.** Each stage produces brainstorm files (supplemental, exploratory) and a compilation file that locks in decisions (`03-shape.md`, `04-outline.md`). The next stage reads the compilation, not the brainstorms. Brainstorms stay as reference but don't drive downstream work.

## Stage Transition Pattern

Every stage command follows this pattern:

1. Read `project-overview.md` in cwd
2. Check `stage` field:
   - If correct prior stage: update stage, begin work
   - If already at this stage: resume
   - If later stage: error -- "already past this stage"
   - If no `project-overview.md`: error -- "run /presentation:start first"
3. Do the work
4. On completion: update `stage` in `project-overview.md` frontmatter
5. Report: show stage transition and next command

## Slide Slug IDs

Every slide has a slug-ID used to reference it in conversation and in the JS file. The slug is an acronym of the slide title plus a two-digit suffix.

**Rules:**
- Derived from the slide title: "One Shot Learning" -> `OSL-01`
- Every slide MUST have a title, even if the visual slide is titleless. The title grounds the slug.
- First occurrence gets `-01`. If the same acronym appears again (rare), increment: `-02`, `-03`.
- Slugs are stable -- reordering slides does not require renumbering. The suffix is an identity number, not a position.
- Use slugs when discussing specific slides: "update the speaker notes on OSL-01" is unambiguous.

## Authoring Model

The authoring stage merges what was previously "specify" and "produce" into a single step. The JavaScript file that generates the PPTX is the single source of truth -- it contains slide content, speaker notes, asset references, and layout decisions.

**Why:** Iterating on a markdown spec then translating to production is redundant. The user can open the PPTX, see exactly what it looks like, and direct changes by slug-ID. The JS file is a better spec than any markdown document because it produces the actual artifact.

**The JS file contains per slide:**
- Slug-ID (e.g., `OSL-01`)
- Title
- Content/layout
- Speaker notes
- Asset references
- Delivery cues

## Deliverable Sequence

Deliverables accumulate in the presentation folder, numbered to align with their stage:

**Start (setup):**
- `project-overview.md` -- minimal info (topic, audience, label, stage: new)
- `discussion.md` -- empty, ready for aha moments

**Brain-dump (02):**
- `02-brain-dump.md` -- TLDR of what was dumped
- `02-brain-dump/` -- raw attachments (images, links, notes)

**Shape (03):**
- `03-shape/` -- brainstorm sessions (01-grounding, 02-core, 03-packaging)
- `03-shape.md` -- locked-in shape merging all brainstorms

**Outline (04):**
- `04-outline/` -- brainstorm sessions (varies by type)
- `04-outline.md` -- locked-in outline

**Author (05):**
- `05-author/` -- the authoring workspace
  - `presentation.js` -- single source of truth (slides, speaker notes, assets, layout)
  - `assets/` -- images, chalkboard sequences, prop sequences, story sequences
  - `presentation.pptx` -- generated output (.gitignore)
  - `presentation.pdf` -- PDF export (.gitignore)

## How-to-Speak Reference

Full Winston methodology: `${CLAUDE_PLUGIN_ROOT}/skills/presentation/guides/how-to-speak/how-to-speak.md`
Raw transcripts: `${CLAUDE_PLUGIN_ROOT}/skills/presentation/guides/how-to-speak/how-to-speak-transcript/`

Stage guides weave in relevant Winston techniques at the point of use.

## Examples

```
/presentation:start all-hands-q1 --label inform
/presentation:brain-dump all-hands-q1
/presentation:shape all-hands-q1
/presentation:outline all-hands-q1
/presentation:author all-hands-q1
```
