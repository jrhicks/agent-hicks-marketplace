---
name: chalkboard
description: Create a chalkboard sequence -- progressive-reveal drawings
argument-hint: <sequence-name>
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

Create a chalkboard sequence -- a series of progressive-reveal drawings on a green chalkboard background. Each frame adds to the previous one, building a concept visually as you advance slides.

## Persona

**Illustrator** -- Think in shapes and spatial relationships, not words. Chalkboard sequences are drawings, not slides. Collaborate with the user and generate images using the bundled script to create each frame.

**Do NOT:** Generate polished graphics. Use photorealistic style. Make slides that happen to have a green background.

## This is Drawing, Not Slides

The point of a chalkboard is to draw -- shapes, arrows, relationships, diagrams. Very few words, mostly drawing.

- Draw a star and put a word next to each point
- Draw a box, label the edges, add arrows showing flow
- Sketch a shape in the center and build outward

If it could work as a normal slide with a different background, it's not a chalkboard sequence. Bullet points on a green background is not a chalkboard.

## Context

This command can be run standalone or during the authoring stage. It produces image assets that go in the presentation's `05-author/assets/chalkboard-sequences/` directory.

## Frames

A sequence is typically ~5 frames that progressively reveal a drawing:

1. A shape appears
2. A label on one edge
3. Another element added
4. Connections drawn
5. The complete picture

Each frame builds on the last. The audience watches you "draw" as you advance. More or fewer frames is fine -- use as many as the concept needs. Too few frames forces too much speaker notes per slide -- spread the talking across more visual steps.

## Visual Style

- **Background:** Dark green chalkboard
- **Drawing:** White and pale yellow chalk, hand-drawn feel
- **Style:** Educational sketch -- like a professor actually drew it
- **Aspect:** 16:9 (full-bleed slide)
- **Air:** Keep it sparse. A chalkboard crammed with detail defeats the purpose.

## Process

### 1. Gather the Concept

Ask the user:
- "What concept is this chalkboard explaining?"
- "What's the visual -- a shape, a diagram, a flow?"
- "What order should it build in?"

### 2. Propose the Frame Sequence

Describe all frames in words before generating. The user should confirm the visual plan:

```
Chalkboard: <sequence-name>

Frame 1: <what appears first -- a shape, a starting element>
Frame 2: <what gets added>
Frame 3: <what gets added>
Frame 4: <what gets added>
Frame 5: <the complete drawing>
```

### 3. Determine Output Location

- If `project-overview.md` exists in cwd (inside a presentation): output to `05-author/assets/chalkboard-sequences/<sequence-name>/`
- If no presentation context: output to `./chalkboard-sequences/<sequence-name>/`

### 4. Generate Frames

**Image generation script:** `${CLAUDE_PLUGIN_ROOT}/skills/presentation/scripts/generate_image.py`

```bash
python ${CLAUDE_PLUGIN_ROOT}/skills/presentation/scripts/generate_image.py generate \
  "Green chalkboard with chalk drawing of [CONCEPT]. White and pale yellow chalk, hand-drawn, educational sketch." \
  <output-path>/frame-1.png --aspect 16:9
```

Requires `GOOGLE_API_KEY` env var and `pip install google-genai Pillow`.

**Generate each frame separately.** Do not transform one frame from another -- image models tend to over-erase small elements when transforming.

Work with the user iteratively. Generate a frame, review it together, adjust the prompt, regenerate if needed, then move to the next frame.

Each frame prompt should specify:
- Green chalkboard background
- White and pale yellow chalk, hand-drawn feel
- Educational sketch style, no photorealism
- Same spatial layout as previous frames (new elements added, existing ones stay)
- 16:9 aspect ratio

### 5. Review

Read the generated images and assess:
- Does each frame clearly build on the previous one?
- Is the spatial layout consistent across frames?
- Is the chalk aesthetic consistent? (Green board, hand-drawn, sparse)
- Are there very few words and mostly drawing?

If issues, regenerate the problematic frame.

### 6. Report

```
Chalkboard: <sequence-name>
Frames: <output-path>/frame-1.png through frame-N.png

Use in presentation.js:
  { slug: 'XX-01', type: 'chalkboard', asset: 'assets/chalkboard-sequences/<sequence-name>/frame-1.png' }
  { slug: 'XX-02', type: 'chalkboard', asset: 'assets/chalkboard-sequences/<sequence-name>/frame-2.png' }
  ...
```
