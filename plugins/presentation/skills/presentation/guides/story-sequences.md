# Story Sequence Guide

Story sequences are multi-frame editorial illustration sequences that accompany verbal storytelling. Unlike prop sequences (2 frames, one prop) or chalkboard sequences (2 frames, one diagram), story sequences depict 3-7 completely different scenes with consistent characters -- walking the audience through a narrative interlude.

## When to Use

- **Book or paper synopses** -- condensing a story into visual scenes (e.g., "The Goal" by Goldratt)
- **Case studies** -- showing progression through a real situation
- **Multi-scene anecdotes** -- narrative interludes that span settings and time
- **Thought experiments** -- stepping through hypothetical scenarios

The key signal: the narrative has **multiple distinct settings** with **recurring characters**. If it's one setting with one object, that's a prop sequence. If it's an abstract diagram, that's a chalkboard sequence. If characters move through different worlds, that's a story sequence.

## Visual Style

- **Full-bleed editorial illustration** -- cinematic, atmospheric, warm color palette
- **New Yorker / Vanity Fair magazine quality** -- slightly stylized, recognizable likenesses
- **Zero text on frames** -- no captions, labels, or speech bubbles. The speaker narrates.
- **Cinematic composition** -- each frame is a scene, not a portrait. Environment tells the story alongside the characters.
- **Consistent palette across all frames** -- warm tones, natural lighting, same illustration style

## Frame Structure

**3-7 scene frames**, each depicting a different setting. Every frame shows one moment in the narrative.

Unlike prop sequences (always exactly 2 frames) or chalkboard sequences (always exactly 2 frames), story sequences have variable length. The number of frames matches the number of narrative beats -- no padding, no compression.

Each frame should be self-explanatory at a glance: you should be able to look at it and understand the setting, the characters' emotional state, and the dramatic moment without reading anything.

---

## Scene Planning (Outline Stage)

Before any visual production, design each frame in the outline. The point you're making drives the scene you illustrate -- not the other way around.

For each frame, define:

| # | Point | Characters | Scene | Disposition |
|---|-------|------------|-------|-------------|
| 1 | What you are literally saying while this slide is up | Who is present in this frame | Setting/environment | Emotional state of each character |

- **Point** -- the narrative beat. What does the audience learn or feel from this frame? This is the speaker's script driver.
- **Characters** -- only the characters needed for this beat. Not every character appears in every frame.
- **Scene** -- the physical setting. Different from the previous frame.
- **Disposition** -- how each character feels. This drives the image generation prompt.

The scene plan lives in the delivery brainstorm (`02-delivery.md` or `05-delivery.md`) under the Props section. Produce reads it and generates images to match.

### Example: "The Goal" Scene Plan

| # | Point | Characters | Scene | Disposition |
|---|-------|------------|-------|-------------|
| 1 | Alex's plant is failing -- machines down, orders late, jobs at risk | Alex, background workers | Factory floor, idle machines, red lights | Alex: anxious, hand in hair. Workers: uncertain |
| 2 | Leadership's answer is automation -- throw technology at it | Alex, executives | Corporate boardroom, decline charts | Executives: demanding. Alex: defensive, arms crossed |
| 3 | A chance encounter with a physics professor who sees the real problem | Alex, Jonah | Restaurant booth, warm amber light | Jonah: calm, knowing smile, sketching. Alex: skepticism turning to curiosity |
| 4a | The bottleneck is obvious once you see it -- one slow kid holds everyone back | Alex, boy scouts, Herbie | Forest trail, strung out line | Alex: troubled realization. Herbie: exhausted under heavy pack |
| 4b | Move the constraint to the front, redistribute the load -- the line moves together | Alex, boy scouts, Herbie | Forest trail, tight group | Herbie: beaming, leading. Others: neutral, trudging. Alex: satisfied |
| 5 | Back at the plant, the same principle works -- focus on the bottleneck, not efficiency everywhere | Alex | Factory floor, running smoothly | Alex: brightening, realization hitting |
| 6 | Alex now teaches what he learned -- calm certainty replaces the opening anxiety | Alex, colleagues | Meeting room, whiteboard | Alex: confident. Colleagues: attentive |

Notice how the Point column is what the speaker says. The visual follows from that.

---

## Character Reference Sheet

This is the core consistency mechanism. The challenge with multi-frame narrative sequences is **character consistency** -- the same characters must be recognizable across 3-7 completely different settings. Solved with a pattern borrowed from concept art and animation: define all characters first, generate them together in one neutral image, then use that sheet as the transform input for every scene.

### Step 1: Define Characters

For each character in the narrative, specify:
- **Name** and **role** in the story
- **Distinguishing visual features** -- hair, build, age, expression tendency
- **Clothing** -- specific enough to be recognizable across scenes
- **Emotional range** -- what states this character needs to convey across the sequence

Example (from "The Goal"):

| Character | Role | Features | Clothing |
|-----------|------|----------|----------|
| Alex | Plant manager, protagonist | Mid-30s, dark hair, worried expression baseline | White dress shirt, loosened tie, sleeves often rolled |
| Jonah | Physics professor, mentor | Older, silver hair, calm knowing smile | Rumpled tweed jacket, no tie, professorial |
| Bill Peach | Division VP, pressure source | Imposing, broad shoulders, stern | Dark suit, power tie |

### Step 2: Generate Character Reference Sheet

Generate ALL characters together in one neutral-background image. This is the single source of truth for character appearance. The prompt should be detailed -- describe every character fully.

```
All characters standing together against a plain warm gray background.
Editorial illustration style, warm color palette, slightly stylized.

Left: [Character 1 full description].
Center: [Character 2 full description].
Right: [Character 3 full description].

Full body, neutral poses, facing viewer. Clean background, no setting details.
Same warm editorial illustration style for all characters.
```

Output: `05-author/assets/story-sequences/<story-name>/character-sheet.png`

### Step 3: Generate Each Scene Frame

Transform FROM the character reference sheet for every scene. The character sheet is always the input image -- never chain frame-to-frame (that causes style drift and character mutation).

Scene prompts are SHORT -- just the setting and action. The character sheet already has the visual identity baked in.

```
Transform this group into a scene: [setting]. [Character name] is [action/pose].
[Other character] is [action/pose]. [Atmosphere/lighting]. Cinematic composition,
same editorial illustration style. --aspect 16:9
```

**Always transform from the character sheet.** Never from a previous frame. This is how animators work -- character sheets before storyboards. It decouples character identity from any specific setting.

---

## Prompt Engineering

### Character Sheet Prompt: Be Detailed

The character sheet prompt is the most important prompt in the sequence. Describe every character thoroughly -- clothing, build, hair, expression, distinguishing features. This is your one chance to establish visual identity. Be redundant. Be specific.

### Scene Prompts: Be Brief

Scene prompts should be 2-3 sentences. The character sheet already provides the visual identity. The scene prompt only needs:
1. **Setting** -- where are we? (factory floor, boardroom, restaurant)
2. **Action** -- what are characters doing? (arguing, teaching, realizing)
3. **Atmosphere** -- what's the emotional tone? (tense, warm, revelatory)

### Negative Constraints

- "NO text, NO captions, NO speech bubbles, NO labels"
- "NO other people unless specified"
- "Same editorial illustration style as the reference"

---

## Production Commands

```bash
# Step 1: Generate character reference sheet
python3 .claude/skills/nano-banana/scripts/generate_image.py generate \
  "<character-sheet-prompt>" \
  05-author/assets/story-sequences/<story-name>/character-sheet.png

# Step 2: Generate each scene frame (transform from character sheet)
python3 .claude/skills/nano-banana/scripts/generate_image.py transform \
  05-author/assets/story-sequences/<story-name>/character-sheet.png \
  "<scene-prompt>" \
  05-author/assets/story-sequences/<story-name>/frame-1.png \
  --aspect 16:9

python3 .claude/skills/nano-banana/scripts/generate_image.py transform \
  05-author/assets/story-sequences/<story-name>/character-sheet.png \
  "<scene-prompt>" \
  05-author/assets/story-sequences/<story-name>/frame-2.png \
  --aspect 16:9

# Repeat for frame-3 through frame-N
```

---

## Example: "The Goal" Synopsis

Five scenes walking the audience through Goldratt's manufacturing fable.

### Characters

| Character | Role | Features | Clothing |
|-----------|------|----------|----------|
| Alex | Plant manager, protagonist | Mid-30s, dark hair, worried expression baseline | White dress shirt, loosened tie, sleeves often rolled |
| Jonah | Physics professor, mentor | Older, silver hair, calm knowing smile | Rumpled tweed jacket, no tie, professorial |
| Executives | Division leadership | Imposing, suited | Dark suits, power ties |

### Character Sheet Prompt

```
Three characters standing together against a plain warm gray background.
Editorial illustration style, warm color palette, slightly stylized.

Left: Alex, mid-30s plant manager. Dark hair, slightly disheveled. Worried,
tired expression. White dress shirt with loosened tie, sleeves rolled up.

Center: Jonah, older physics professor and mentor. Silver-gray hair, warm calm
smile, knowing eyes. Rumpled brown tweed jacket over blue shirt, no tie.
Professorial but approachable.

Right: A stern executive in a dark navy suit with red power tie. Broad shoulders,
imposing posture, frowning.

Full body, neutral poses, facing viewer. Clean background, no setting details.
Same warm editorial illustration style for all characters.
```

### Scene Plan (from Outline)

| # | Point (what you say) | Characters | Scene | Disposition |
|---|----------------------|------------|-------|-------------|
| 1 | Alex's plant is failing -- machines down, orders late, jobs at risk | Alex, background workers | Factory floor, idle machines, red lights | Alex: anxious, hand in hair. Workers: uncertain |
| 2 | Leadership's answer is automation -- throw technology at it | Alex, executives | Corporate boardroom, decline charts | Executives: demanding. Alex: defensive, arms crossed |
| 3 | A chance encounter with a physics professor who sees the real problem | Alex, Jonah | Restaurant booth, warm amber light | Jonah: calm, knowing smile, sketching. Alex: skepticism to curiosity |
| 4a | The bottleneck is obvious once you see it -- one slow kid holds everyone back | Alex, boy scouts, Herbie | Forest trail, strung out line | Alex: troubled realization. Herbie: exhausted under heavy pack |
| 4b | Move the constraint to the front, redistribute the load -- the line moves together | Alex, boy scouts, Herbie | Forest trail, tight group | Herbie: beaming, leading. Others: neutral, trudging. Alex: satisfied |
| 5 | Back at the plant, the same principle works -- focus on the bottleneck | Alex | Factory floor, running smoothly | Alex: brightening, realization hitting |
| 6 | Alex now teaches what he learned -- calm certainty replaces the opening anxiety | Alex, colleagues | Meeting room, whiteboard | Alex: confident. Colleagues: attentive |

The Point column is what the speaker says. The visual follows from that. Produce reads this table and generates images to match -- characters, scene, and disposition become the image prompt.

---

## Asset Directory Structure

```
05-author/assets/story-sequences/
└── <story-name>/
    ├── character-sheet.png          # All characters, neutral background
    ├── frame-1.png                  # Scene 1 (16:9)
    ├── frame-2.png                  # Scene 2 (16:9)
    ├── frame-3.png                  # Scene 3 (16:9)
    ├── ...                          # As many as needed (3-7)
    └── frame-N.png                  # Final scene (16:9)
```
