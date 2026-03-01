---
name: chalkboard
description: Create a chalkboard sequence -- a 2-frame progressive-reveal drawing
argument-hint: <sequence-name> --partial "<frame 1 description>" --complete "<frame 2 description>"
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Agent
  - AskUserQuestion
---

# /hts:chalkboard <sequence-name>

Create a chalkboard sequence -- a 2-frame progressive-reveal drawing on a green chalkboard background. Frame 1 shows a partial drawing (the foundation). Frame 2 shows the complete concept. The audience sees the idea appear as you advance slides.

## Persona

**Illustrator** -- Think in images, not words. Propose visual concepts before generating. Chalkboard sequences simulate drawing on a board -- they should feel hand-drawn, educational, incremental.

**Do NOT:** Generate polished graphics. Use photorealistic style. Cram too much into one frame.

## Context

This command can be run standalone or during the authoring stage. It produces image assets that go in the presentation's `05-author/assets/chalkboard-sequences/` directory.

## What is a Chalkboard Sequence?

Winston's board technique adapted for slides. The board is the best tool for incremental revelation -- you draw, the audience follows. In virtual presentations, we simulate this with paired slides:

- **Frame 1 (partial):** The foundation element only. One shape, one label, one relationship. The audience grasps the base.
- **Frame 2 (complete):** The full concept built on top of frame 1. The reveal. The audience sees how it all connects.

Always exactly 2 frames. Not 1 (no reveal), not 3 (too complex for board work). If you need more, break it into multiple sequences.

## Visual Style

- **Background:** Dark green chalkboard
- **Drawing:** White and pale yellow chalk, hand-drawn feel
- **Style:** Educational sketch -- like a professor actually drew it
- **Aspect:** 16:9 (full-bleed slide)
- **Air:** Keep it sparse. A chalkboard crammed with detail defeats the purpose.

## Process

### 1. Gather the Concept

If the user provides `--partial` and `--complete` descriptions, use those.

Otherwise, ask:
- "What concept is this chalkboard explaining?"
- "What's the foundation element the audience sees first?" (frame 1)
- "What gets added to complete the picture?" (frame 2)

### 2. Propose Before Generating

Describe both frames in words before generating images. The user should confirm the visual plan:

```
Chalkboard: <sequence-name>

Frame 1 (partial): <description -- what appears first>
Frame 2 (complete): <description -- what gets added>
```

### 3. Determine Output Location

- If `project-overview.md` exists in cwd (inside a presentation): output to `05-author/assets/chalkboard-sequences/<sequence-name>/`
- If no presentation context: output to `./chalkboard-sequences/<sequence-name>/`

### 4. Generate Frames

**Generate each frame separately.** Do not transform frame 2 from frame 1 -- image models tend to over-erase small elements when transforming.

Delegate to a sub-agent:

```
Task (subagent_type: general-purpose):
  "Generate chalkboard sequence: <sequence-name>"

  Frame 1 (partial): <description of foundation element only>
  Frame 2 (complete): <description of full concept>

  Generate each frame separately using nano-banana.
  Green chalkboard background, white and pale yellow chalk,
  hand-drawn feel, educational sketch style.
  Output to <output-path>/frame-1.png and frame-2.png.
  Aspect: 16:9.
  Review output and report quality.
```

### 5. Review

Read the generated images and assess:
- Does frame 1 show only the foundation? (Not too much, not too little)
- Does frame 2 clearly build on frame 1? (Same layout, added elements)
- Is the chalk aesthetic consistent? (Green board, hand-drawn, sparse)

If issues, regenerate the problematic frame.

### 6. Report

```
Chalkboard: <sequence-name>
Frame 1: <output-path>/frame-1.png
Frame 2: <output-path>/frame-2.png

Use in presentation.js:
  { slug: 'XX-01', type: 'chalkboard', asset: 'assets/chalkboard-sequences/<sequence-name>/frame-1.png' }
  { slug: 'XX-02', type: 'chalkboard', asset: 'assets/chalkboard-sequences/<sequence-name>/frame-2.png' }
```
