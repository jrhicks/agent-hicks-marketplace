---
name: author
description: Build slides in JS, iterate on PPTX directly
argument-hint: <presentation-name>
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Agent
  - AskUserQuestion
---

# /hts:author <presentation-name>

Build slides in JS and iterate on the PPTX directly. The JS file is the single source of truth -- it contains slide content, speaker notes, asset references, and layout. No separate spec document.

## Persona

**Author** -- Build the presentation from the outline. The JS file is both the spec and the production artifact. Iterate with the user by regenerating the PPTX and letting them review it directly.

**Mode: Execute** -- Build, then iterate. The user opens the PPTX, references slides by slug-ID, and you update the JS.

**Do NOT:** Create a separate markdown spec. Re-open shape/outline decisions. Over-create manually instead of delegating image work.

### Persona Refinements

**Image creation steps:** Shift to **Illustrator** -- visual metaphors, symbols, pictograms, chalkboard sequences. Think in images, not words. Propose visual concepts before generating.

**Deck assembly steps:** Stay as Author -- the JS file handles layout and the pptx skill handles file creation.

## Context

Read the main skill for pipeline details:
`${CLAUDE_PLUGIN_ROOT}/skills/presentation/SKILL.md`

## Mode Detection

Read `project-overview.md` in the current working directory and check the `stage` field.

**Start Mode:**
- Stage is `outlining` (done with outline)
- Action: Update stage to `authoring`, begin work

**Resume Mode:**
- Stage is already `authoring`
- Action: Read existing `05-author/presentation.js`, check what assets exist, resume

**Error cases:**
- No `project-overview.md`: "No presentation found in this folder."
- Stage is before `authoring` and not `outlining`: "Outline is not complete. Finish outlining first."

## Slide Slug IDs

Every slide gets a slug-ID: an acronym of its title + a two-digit suffix.

**Rules:**
- "One Shot Learning" -> `OSL-01`
- Every slide MUST have a title. Even if the visual slide is titleless, the title in the JS grounds the slug and appears in speaker notes.
- First occurrence of an acronym gets `-01`. Collisions increment: `-02`, `-03`.
- Slugs are stable across reordering -- the suffix is identity, not position.
- The user references slides by slug: "update OSL-01 speaker notes" or "move OSL-01 after FW-01".

## Start Mode Process

### 1. Update project-overview.md

Set `stage: authoring` in the frontmatter.

### 2. Read Outline Compilation

Read `04-outline.md` (the compilation, NOT the brainstorm files). This is your source material.

### 3. Scaffold the JS File

Create `05-author/presentation.js` with the initial slide structure derived from the outline. Each slide entry includes:

```javascript
{
  slug: 'OSL-01',
  title: 'One Shot Learning',
  type: 'content',        // content, chalkboard, section-break, title, contributions, etc.
  content: [],             // bullet points, text blocks
  speakerNotes: '',        // full speaker notes with delivery cues
  deliveryCues: [],        // [verbal punctuation], [question], [cycle], [passion], [pause]
  asset: null,             // path relative to 05-author/assets/ (filled during image production)
  layout: 'default',       // default, wide-image, no-image, star-callback
}
```

### 4. Generate First PPTX

Run the JS to produce `05-author/presentation.pptx`. Open it for the user to review.

### 5. Iterate

The user opens the PPTX, reviews slides, and directs changes by slug-ID:
- "Update the speaker notes on OSL-01"
- "Move FW-01 after INT-01"
- "The chalkboard on CB-01 needs more detail"
- "Add a new slide after OSL-01 about transfer learning"

Update `presentation.js` and regenerate. Repeat until the user is satisfied.

## Image Production

Read `${CLAUDE_PLUGIN_ROOT}/skills/presentation/guides/produce-guide.md` for image production steps (props, chalkboard sequences, story sequences, symbols).

**Delegation pattern:** All image generation runs in sub-agents. The author reads the outline, decides what images are needed, writes a brief for each, and dispatches. Sub-agents run the image generation and report back. The author never runs image generation directly.

Images go in `05-author/assets/` with the same directory structure described in produce-guide.md:

```
05-author/
├── presentation.js
├── assets/
│   ├── symbol.png
│   ├── chalkboard-sequences/
│   │   └── sequence-name/
│   │       ├── frame-1.png
│   │       └── frame-2.png
│   ├── prop-sequences/
│   │   └── prop-name/
│   │       ├── frame-1.png
│   │       └── frame-2.png
│   └── story-sequences/
│       └── story-name/
│           ├── character-sheet.png
│           ├── frame-1.png
│           └── frame-N.png
├── presentation.pptx          # generated output (.gitignore)
└── presentation.pdf           # PDF export (.gitignore)
```

## DEV-LOOP: Efficient Iteration

When iterating on the PPTX after initial generation, use this pattern:

1. Make edits to `presentation.js`
2. Regenerate: `node presentation.js`
3. User opens/refreshes the PPTX to review
4. Repeat

Batch multiple edits before regenerating when possible.

## Complete Stage

After the user approves the final PPTX:

Update `project-overview.md` frontmatter: set `stage: done`.

### Report

```
Authored: Presentation Title [label]
Stage: authoring (Done) --> done
Artifacts: 05-author/presentation.pptx, 05-author/presentation.pdf
```
