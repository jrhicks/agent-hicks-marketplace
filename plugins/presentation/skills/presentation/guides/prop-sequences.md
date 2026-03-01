# Prop Sequence Guide

Prop sequences are paired illustration slides that adapt physical props for virtual/slide-based presentations. They follow the same 2-frame pattern as chalkboard sequences but use a different visual style.

## Reference Images

In `generated-images/hts/`:
- `prop-reference-base.png` -- Clean base: professor at chalkboard, no prop. **Use as input for all prop transforms.**
- `prop-bicycle-wheel-1.png` -- Example Frame 1: Professor presenting the bicycle wheel
- `prop-bicycle-wheel-2.png` -- Example Frame 2: Professor pointing at the duct tape insight

## Visual Style

**Editorial illustration** -- warm, slightly stylized, recognizable likeness. Think New Yorker magazine illustration. NOT a cartoon, NOT photorealistic, NOT chalkboard aesthetic.

- Brown tweed jacket with leather elbow patches, light blue collared shirt
- Warm color palette, natural lighting
- Clean green chalkboard fills the wall behind the professor

## Frame Structure

**Frame 1 (setup):** Professor presents the prop. Calm, confident expression. The prop is prominent and clearly visible. The audience should understand what they're looking at.

**Frame 2 (insight):** Professor demonstrates the key moment. Animated, enthusiastic expression -- the eureka moment. The prop has changed state (duct tape added, something revealed, something in motion). The energy shift between frames tells the story.

## How It Works

The base reference image (`prop-reference-base.png`) already has the correct style, outfit, hair, setting, and composition baked in. To create a prop sequence, transform the base image -- don't start from the raw selfie each time. This gives consistent style across all props.

**Aspect ratio:** The `--aspect 16:9` flag uses Gemini's native `ImageConfig` to generate at 16:9 directly. No cropping or padding needed.

## Prompt Engineering Tactics

These lessons were learned iterating on the bicycle wheel sequence.

### Camera Perspective: Front-Row Student POV

The base image already establishes this. When writing prop prompts, maintain the same perspective -- the professor is close, at or slightly above eye level, chalkboard behind.

### Negative Prompts

Gemini doesn't use negative prompts like Stable Diffusion, but explicit exclusions help:
- "There are NO desks, seats, or audience members visible"
- "NO other people in the scene"

### Consistency Between Frames

Both frames should share:
- Same outfit (tweed jacket, blue shirt)
- Same chalkboard background
- Same camera angle and distance
- Same illustration style and color palette

What changes between frames:
- Expression (calm --> animated)
- Pose (presenting --> pointing/demonstrating)
- Prop state (intact --> modified / in motion)

## Working Prompts

Since the base image already has the style, setting, and outfit, prompts are short -- just describe the prop and pose.

### Frame 1 (setup)

```
Add a [PROP] to this illustration. The professor is holding the
[PROP] by [HOW], presenting it directly to the viewer. Eye contact.
Calm, confident expression. The [PROP] is prominent and clearly
visible. Keep the same editorial illustration style, outfit, and
chalkboard background. NO other people, NO audience members visible.
```

### Frame 2 (insight)

```
Add a [PROP IN CHANGED STATE] to this illustration. The professor
is holding [PROP IN CHANGED STATE] in one hand, and [ACTION -- e.g.,
pointing excitedly at the key detail] with the other. Their expression
is animated, enthusiastic, eyes wide -- the eureka moment. Keep the
same editorial illustration style, outfit, and chalkboard background.
NO other people, NO audience members visible.
```

Replace `[BRACKETED]` sections with prop-specific details.

## Production Command

```bash
# Frame 1
python3 .claude/skills/nano-banana/scripts/generate_image.py transform \
  generated-images/hts/prop-reference-base.png \
  "<frame-1-prompt>" \
  05-author/assets/prop-sequences/<prop-name>/frame-1.png \
  --aspect 16:9

# Frame 2
python3 .claude/skills/nano-banana/scripts/generate_image.py transform \
  generated-images/hts/prop-reference-base.png \
  "<frame-2-prompt>" \
  05-author/assets/prop-sequences/<prop-name>/frame-2.png \
  --aspect 16:9
```

## Creating a New Base Reference

If the presenter changes, generate a new base from their selfie:

```bash
python3 .claude/skills/nano-banana/scripts/generate_image.py transform \
  <presenter-selfie.png> \
  "Transform this person into a warm editorial illustration. Make their hair noticeably more gray and white -- distinguished silver-gray hair. Classic brown tweed jacket with leather elbow patches over a light blue collared shirt. Standing in front of a large CLEAN green chalkboard. Hands lightly clasped, calm confident expression, eye contact. NO props, NO objects in hands. NO other people. Warm editorial illustration style like the New Yorker. Warm color palette." \
  generated-images/hts/prop-reference-base.png \
  --aspect 16:9
```
