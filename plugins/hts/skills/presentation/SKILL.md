---
name: hts
description: |
  Create presentations following Patrick Winston's how-to-speak methodology.
  Folder-as-presentation model with stage tracking via project-overview.md.
  Triggers: "/hts", "hts brain-dump", "hts shape".
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

# /hts

**A presentation is a folder.** The user creates a folder, cd's into it, and runs commands. `project-overview.md` in the current working directory tracks metadata and stage. No external board, no folder moves.

Create presentations using Patrick Winston's how-to-speak methodology. Presentations progress through stages from new through done.

**Methodology:** This process is grounded in Winston's MIT "How to Speak" lecture -- a practical framework for communication built on Knowledge + Practice + talent (talent smallest). The full reference lives in `${CLAUDE_PLUGIN_ROOT}/skills/presentation/guides/how-to-speak/`. Each stage integrates specific Winston techniques: empowerment promise and Star elements in shaping, cycling and verbal punctuation in outlining, slide crime avoidance and chalkboard sequences in authoring.

## Usage

```
/hts:start [--label inform|expose|persuade]
/hts:brain-dump
/hts:shape
/hts:outline
/hts:author
/hts:chalkboard <sequence-name>
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
   - If no `project-overview.md`: error -- "run /hts:start first"
3. Do the work
4. On completion: update `stage` in `project-overview.md` frontmatter
5. Report: show stage transition and next command

---

## Brain-dump Stage

**Persona: Listener** -- Draw out raw content without organizing. Catch and record verbatim. Ask follow-up questions to draw out more, never to structure. If the dump is thin, initiate a guided brainstorm.

**Do NOT:** Over-structure too early. Edit while dumping. Reorganize content. Suggest structure.

**How it works:**
- The user shares everything they know about the topic
- Ask follow-up questions: "What else?", "Any examples?", "What about X?"
- Offer to pull in external material: "Want me to research anything via web search?"
- If the user sends files, images, or links, save them to `02-brain-dump/`

**If the dump is thin**, switch to guided brainstorm:
- "Who is someone in the audience? What do they already know?"
- "What's the one thing you most want them to walk away with?"
- "Is there a story or example that captures this?"
- "What would surprise them?"

**Deliverables:**
- `02-brain-dump.md` -- TLDR summarizing what was dumped (brief overview, not the content itself)
- `02-brain-dump/` -- folder with attachments or `notes.md` with raw dump content

---

## Shape Stage

**Persona: Shaper** -- Work through 3 brainstorm sessions then lock in. Lead with proposals drawn from the brain-dump. Present drafts for the user to react to -- don't ask open questions that leave them alone with the work.

**Do NOT:** Answer for the user. Skip brainstorms. Start from blank instead of proposing from brain-dump.

**Guide:** Read `${CLAUDE_PLUGIN_ROOT}/skills/presentation/guides/shape-guide.md` for detailed session instructions.

**Brainstorm sessions (in order):**
1. **Grounding** (audience, situating, fencing) --> `03-shape/01-grounding.md`
2. **Core** (salient idea, story, surprise) --> `03-shape/02-core.md`
3. **Packaging** (symbol, slogan, empowerment promise) --> `03-shape/03-packaging.md`

After each session, write the brainstorm file. Re-anchor context before starting the next.

**Lock-in:** Synthesize all 3 brainstorms into `03-shape.md` -- the compilation downstream stages read. Present for user approval. Should include: audience, situating, fencing, salient idea, story, surprise, symbol, slogan, empowerment promise.

---

## Outline Stage

**Persona: Architect** -- Draft the outline from the locked-in shape. Lead with drafts, not questions.

**Do NOT:** Start from blank. Skip reading the shape compilation. Re-open shape decisions.

**Guides:**
- `${CLAUDE_PLUGIN_ROOT}/skills/presentation/guides/outline-guide/guide.md`
- `${CLAUDE_PLUGIN_ROOT}/skills/presentation/guides/outline-guide/inform-guide.md`
- `${CLAUDE_PLUGIN_ROOT}/skills/presentation/guides/outline-guide/expose-persuade-guide.md`

**Brainstorm topics (in order).** Skip or keep light any that don't apply:

1. **Sections** (`04-outline/01-sections.md`) -- section-by-section structure, medium per section (board vs slides), rough duration
2. **Delivery** (`04-outline/02-delivery.md`) -- cycling plan, verbal punctuation, hooks, props, how to start, how to stop
3. **Vision & Contributions** (`04-outline/03-vision-contributions.md`) -- vision, what you've done, contributions the audience should remember. Central for expose/persuade. Can be light for inform.

**Label hints** (flavor emphasis, not structure):
- **inform** -- Sections and delivery matter most. Vision/contributions can be light.
- **expose** -- Vision and contributions are the backbone.
- **persuade** -- Contributions and situating are critical.

**Lock-in:** Synthesize into `04-outline.md`. Present for user approval.

---

## Authoring Stage

**Persona: Author** -- Build the presentation from the outline. The JS file is both the spec and the production artifact. Iterate with the user by regenerating the PPTX and letting them review it directly.

**Do NOT:** Create a separate markdown spec. Re-open shape/outline decisions.

**Image creation steps:** Shift to **Illustrator** persona. Read `${CLAUDE_PLUGIN_ROOT}/skills/presentation/guides/produce-guide.md` for image production (props, chalkboard sequences, story sequences, symbols). Delegate all image generation to sub-agents.

**Process:**
1. Read `04-outline.md` (the compilation)
2. Scaffold `05-author/presentation.js` with slide structure from the outline
3. Generate first PPTX, open for user to review
4. Iterate: user directs changes by slug-ID, update JS, regenerate

**DEV-LOOP:** Edit `presentation.js`, run `node presentation.js`, user reviews PPTX. Batch edits before regenerating.

**Deliverables:**
- `05-author/presentation.js` -- single source of truth
- `05-author/assets/` -- images, sequences
- `05-author/presentation.pptx` -- generated output (.gitignore)
- `05-author/presentation.pdf` -- PDF export (.gitignore)

---

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

```javascript
{
  slug: 'OSL-01',
  title: 'One Shot Learning',
  type: 'content',        // content, chalkboard, section-break, title, contributions, etc.
  content: [],             // bullet points, text blocks
  speakerNotes: '',        // full speaker notes with delivery cues
  deliveryCues: [],        // [verbal punctuation], [question], [cycle], [passion], [pause]
  asset: null,             // path relative to 05-author/assets/
  layout: 'default',       // default, wide-image, no-image, star-callback
}
```

## How-to-Speak Reference

Full Winston methodology: `${CLAUDE_PLUGIN_ROOT}/skills/presentation/guides/how-to-speak/how-to-speak.md`
Raw transcripts: `${CLAUDE_PLUGIN_ROOT}/skills/presentation/guides/how-to-speak/how-to-speak-transcript/`

Stage guides weave in relevant Winston techniques at the point of use.

## Examples

```
cd ~/talks/all-hands-q1
/hts:start --label inform
/hts:brain-dump
/hts:shape
/hts:outline
/hts:author
```
