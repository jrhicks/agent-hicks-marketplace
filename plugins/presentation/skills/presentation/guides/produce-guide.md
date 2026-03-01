# Produce Guide

Build artifacts from the spec. This is where the presentation becomes physical -- slides, images, props, speaker notes. Every production decision is guided by one principle: the speaker is the main event, everything else is a condiment.

**Context management:** Image generation is context-expensive -- prompt templates, API calls, visual review, iteration. Delegate ALL image work to sub-agents. The producer orchestrates (decides what images to create, reviews results) but never runs nano-banana commands directly. This keeps the main conversation lean for the text-heavy steps (speaker notes, contributions, ending).

---

## DEV-LOOP: Efficient Iteration During Refinement

When refining a presentation during the produce phase (especially after initial PPTX generation), use the DEV-LOOP pattern to iterate without waiting for regeneration cycles.

**Setup (one-time):**
```bash
# Start a background watcher in the 05-author/ folder
# (where presentation.js lives)
while true; do
  sleep 2
  if [ -f .regenerate_trigger ]; then
    rm .regenerate_trigger
    node presentation.js
  fi
done
```

**Iteration workflow:**
1. Make edits to `presentation.js` (update contributor names, fix speaker notes, adjust slide content, etc.)
2. Create the trigger file: `touch .regenerate_trigger`
3. Continue discussing the next changes while the background task regenerates
4. By the time you review PowerPoint, the new PPTX is ready
5. Repeat for each refinement

**Benefits:**
- No context switches or waiting for generation
- Batch multiple edits before reviewing
- Continuous conversation flow while artifacts build

**Example:**
```
You: Remove Wayne & Preston from contributors
Me: Updated presentation.js, triggered regeneration
You: Also remove the Android Review slides
Me: Updated (trigger), continue talking...
You: Open PowerPoint when ready
(PPTX is ready)
```

This pattern is essential when iterating on slide details, speaker notes, or order adjustments based on feedback.

---

## Step 1: Props

Props come first because they're the most memorable part of any talk and the hardest to source last-minute.

Winston's evidence is overwhelming. Jim Glass saw Winston break a wooden pointer in a talk 20 years earlier. What does Glass remember? "Oh yeah, that's the one where you broke the pointer." Not the content. Not the slides. The prop. Henrik Ibsen understood this -- the pot-bellied stove in *Hedda Gabler* is what Winston remembers about the play many decades later. Alan Lazarus's pendulum in 26-100 is what students remember about conservation of energy. Seymour Papert's bicycle wheel is what people remember about thinking about problems the right way.

Props create empathetic mirroring more powerfully than any other medium. When the audience watches you manipulate a physical object, mirror neurons fire. They feel themselves doing it. You can't get that from a slide or a picture. You need to see it in the physical world.

**Production checklist for props:**
- What physical objects were planned in the outline?
- For in-person: can they be sourced, built, or borrowed? Do they need a practice run?
- For virtual/slides: each prop becomes a **prop sequence** -- paired illustration slides

### Prop Sequences (Virtual Adaptation)

Physical props can't be handed to a slide audience. Instead, produce a 2-frame illustration sequence showing the professor presenting and demonstrating the prop. These are editorial-style illustrations (warm, New Yorker magazine style) -- NOT chalkboard aesthetic.

- **Frame 1 (setup):** Professor calmly presents the prop. Eye contact with audience.
- **Frame 2 (insight):** Professor animatedly demonstrates the key moment. Expression shifts to excited/eureka.

**Requires a reference photo of the presenter.** Use `transform` mode with nano-banana to preserve likeness.

**Delegate each prop to a sub-agent:**

```
Task (subagent_type: general-purpose):
  "Generate prop sequence: <prop-name>"

  Read guides/prop-sequences.md for prompt templates and camera angle notes.
  Reference photo: <path-to-presenter-photo>

  Prop: <prop-name>
  Frame 1 (setup): <description of professor presenting prop>
  Frame 2 (insight): <description of eureka moment with prop>

  Generate both frames using nano-banana transform with --aspect 16:9.
  Output to 05-author/assets/prop-sequences/<prop-name>/frame-1.png and frame-2.png.
  Review the output images and report quality assessment.
```

Run prop agents in parallel when multiple props are needed. Review results after all complete.

### Story Sequences (Narrative Props)

Story sequences are multi-frame editorial illustrations that accompany verbal storytelling -- book synopses, case studies, extended anecdotes. Unlike prop sequences (2 frames, one prop), story sequences depict 3-7 completely different scenes with consistent characters.

The consistency challenge is solved with a **two-phase generation pattern**: first generate a character reference sheet (all characters together on a neutral background), then transform from that sheet for every scene frame. Never chain frame-to-frame.

**Phase 1: Character reference sheet**

```
Task (subagent_type: general-purpose):
  "Generate character reference sheet: <story-name>"

  Read guides/story-sequences.md for the character sheet workflow.

  Characters:
  - <name>: <role, features, clothing>
  - <name>: <role, features, clothing>

  Generate a single image with all characters on a neutral background
  using nano-banana generate (not transform -- no input image needed).
  Output to 05-author/assets/story-sequences/<story-name>/character-sheet.png.
  Review output and report quality.
```

**Phase 2: Scene frames (all transform from character sheet)**

```
Task (subagent_type: general-purpose):
  "Generate story sequence scenes: <story-name>"

  Read guides/story-sequences.md for scene prompt patterns.
  Character sheet: 05-author/assets/story-sequences/<story-name>/character-sheet.png

  Scenes:
  - Frame 1: <setting, action, atmosphere>
  - Frame 2: <setting, action, atmosphere>
  - Frame 3: <setting, action, atmosphere>
  ...

  Generate each frame using nano-banana transform from the character sheet
  with --aspect 16:9. ALWAYS transform from the character sheet, never from
  a previous frame.
  Output to 05-author/assets/story-sequences/<story-name>/frame-1.png through frame-N.png.
  Review output and report quality + character consistency across frames.
```

Phase 1 must complete before Phase 2 starts (the character sheet is the input). Multiple story sequences can run their Phase 1s in parallel, but each story's Phase 2 depends on its own Phase 1.

Props are producible artifacts. Don't leave them to the day of.

---

## Step 2: Generate Images

Switch to **Illustrator** persona for this step.

Scan the spec for slides that need images:
- **Symbol images** -- the visual handle from Shape (Winston's Star: the arch was his symbol)
- **Chalkboard sequences** -- pairs of progressive-reveal drawings on green board
- **Prop sequences** -- pairs of editorial illustrations showing professor with prop (produced in Step 1)
- **Story sequences** -- multi-frame narrative illustrations with consistent characters (produced in Step 1)
- **Diagrams or illustrations** -- any visual content specified

### Delegation Pattern

**All image generation runs in sub-agents.** The producer reads the spec, decides what images are needed, writes a brief for each, and dispatches. Sub-agents read the relevant guide, run nano-banana, and report back. The producer never touches nano-banana directly.

Run independent image agents in parallel (prop sequences, story sequences, chalkboard sequences, symbols can all generate concurrently). Note: story sequence Phase 2 (scene frames) depends on Phase 1 (character sheet) completing first.

### Symbol and Illustration Images

Keep images clean. Winston's "air" principle applies to images too -- an illustration crammed with detail is the visual equivalent of a slide crammed with words.

```
Task (subagent_type: general-purpose):
  "Generate symbol image: <name>"

  Use the nano-banana skill to generate an image.
  Concept: <what it represents>
  Style: <minimal, clean, specific to presentation theme>
  Aspect: <16:9 for full-bleed, 1:1 for inline>
  Output: 05-author/assets/<name>.png
  Review output and report quality.
```

### Chalkboard Sequences

Chalkboard sequences simulate drawing on a board. Always 2 slides per drawing.

**Generate each frame separately** (don't transform from full image -- Gemini over-erases small elements).

```
Task (subagent_type: general-purpose):
  "Generate chalkboard sequence: <sequence-name>"

  Read the pptx skill's chalk-board guide for chalkboard workflow and style details.

  Frame 1 (partial): <description of foundation element only>
  Frame 2 (complete): <description of full concept>

  Generate each frame with nano-banana. Green chalkboard background,
  white and pale yellow chalk, hand-drawn feel, educational sketch style.
  Output to 05-author/assets/chalkboard-sequences/<name>/frame-1.png and frame-2.png.
  Aspect: 16:9.
  Review output and report quality.
```

### Image Quality Review

After all image agents complete, spawn an **Art Director** review:

```
Task (subagent_type: general-purpose, model: haiku):
  "Art Director review of generated images"

  Review all images in 05-author/assets/.
  For each: Does it match the spec? Is style consistent?
  Chalkboard sequences: green + chalk aesthetic maintained?
  Prop sequences: editorial illustration style, not cartoon?
  Story sequences: character consistency across all scene frames?
    Same characters recognizable in different settings?
  Report images needing regeneration with specific feedback.
```

Dispatch regeneration agents for any failures.

---

## Step 3: Extract Speaker Notes

Speaker notes live in `presentation.js` as the `speakerNotes` property on each slide. Review them for quality during authoring.

Speaker notes must ADD to slides, not repeat them. This is the language-processor constraint in action: the audience can either read the slide or listen to the speaker, not both. If the speaker notes duplicate the slide content, the presenter will read aloud what the audience is already reading silently -- and the audience will finish first, then wait.

Winston's progressive fixing makes this automatic: when you strip words from slides, the removed content migrates to speaker notes. The slide shows the skeleton; the speaker provides the flesh.

**Quality check for speaker notes:**
- Does any note merely restate what's on the slide? (Crime: reading your slides)
- Are delivery cues preserved? (`[verbal punctuation]`, `[question]`, `[cycle]`, `[passion]`, `[pause]`)
- Is the tone conversational, not scripted? (Notes guide the speaker, they're not a teleprompter)
- Are the passion beats marked? (These are moments where genuine fascination surfaces -- don't script the enthusiasm, just mark where the material naturally generates it)

Format:

```markdown
# Speaker Notes: [Presentation Title]

## Slide 1: [Title]
[speaker notes with delivery cues preserved]

## Slide 2: [Title]
[speaker notes]

...
```

This is a standalone document the presenter can print or reference independently.

---

## Step 4: Craft the Contributions Slide

The contributions slide deserves its own production step because it's the most important slide in the deck. It's the one that's up there while people are asking questions and filing out. It tells them who you are.

Winston is emphatic about what doesn't belong here:
- **"Questions?"** -- Can be up for 20 minutes. Squanders real estate. Squanders an opportunity to tell people who you are.
- **"Thank You"** -- Never seen anybody write it down. Wastes opportunity.
- **"The End"** -- Even worse. Does nothing for you.
- **"Conclusions"** -- Seems legitimate but people don't care about conclusions. They care about what you have done.

**"Contributions" is the correct label.** It mirrors the done-something enumeration from the opening (the sandwich structure). Winston's example from his own stump speech: "Here are the things I typically demonstrate. And this is what we get out of it." He waits for people to read it.

**Production criteria for contributions text:**
- Concrete accomplishment language, not vague claims
- Readable at a glance -- the audience will scan this while asking questions
- 3-5 items maximum
- Each item stands alone (someone walking in during Q&A should understand each point without context)
- If using Winston's Star: the Salient Idea and Slogan should be visible or echoed here

---

## Step 5: Assemble PPTX

The `presentation.js` file IS the assembly step. It contains all slide data, speaker notes, and asset references. Run it to produce the PPTX. Delegate to the **pptx** skill for any specialized layout needs.

The pptx skill handles:
- Slide creation with proper layouts
- Image placement (full-bleed for chalkboard sequences)
- Speaker notes embedding
- Font sizing (minimum ~40pt for content text per Winston's rule -- below that you're enabling too many words)

**Air check:** After assembly, scroll through the deck. Does it have air? Winston showed one of his own talks: "It wasn't a deeply technical talk but I show it because there's air in it. It's mostly pictures of things. Three or four slides have text on them but when I come to those I give the audience time to read them." If the deck feels heavy -- walls of text, no breathing room -- go back and apply progressive fixing.

**Print test:** Print the deck and lay it out on a table. Winston uses this test to catch too-heavy talks. At a glance, you should see the arc of the talk. Too many slides, too-dense slides, and structural problems all become visible in the physical layout.

Output: `05-author/presentation.pptx`

---

## Step 6: Plan the Ending

The final words need as much production attention as the final slide. Three options, each with a different effect:

**A joke.** Doug Lenat told Winston his secret in a bar in Austin: "I always finish with a joke. And that way people think they've had fun the whole time." A joke is fine at the end -- by this point the audience has calibrated to your voice (unlike the opening, where jokes fall flat because people are still adjusting).

**A benediction.** Governor Christie: "And together, everybody together, we will stand up once again for American greatness, for our children and grandchildren. God bless you and God bless America." Bill Clinton (watch for the lip-pursing where he almost says "thank you" but forces himself not to): "If that is what you want, if that is what you believe, you must vote and you must reelect President Barack Obama. God bless you and God bless America." Then the little salute.

**A salute to the audience.** "It's been great fun being here. It's been fascinating to see what you folks are doing here. I've been stimulated and provoked by the kinds of questions you've been asking. It's been really great. And I look forward to coming back on many occasions in the future."

**NOT "thank you."** You will not go to hell if you conclude by saying thank you, but it's a weak move. "Thank you for listening" suggests everybody stayed out of politeness and had a profound desire to be somewhere else. Once wild applause has started you can mouth a thank you. But the last thing you do should not be saying thank you.

Write the planned ending into the speaker notes for the contributions slide.

---

## Step 7: Export PDF

Export the PPTX to PDF for sharing:

Output: `05-author/presentation.pdf`

Both `.pptx` and `.pdf` should be in `.gitignore` (binary files).

---

## Step 8: Upload to Google Slides

Final step. Upload the presentation to Google Slides for delivery.

Report the Google Slides URL to the user.

---

## Asset Directory Structure

```
05-author/
├── assets/
│   ├── symbol.png                        # Visual handle
│   ├── [other-images].png                # Inline illustrations
│   ├── chalkboard-sequences/
│   │   ├── sequence-name/
│   │   │   ├── frame-1.png               # Partial drawing
│   │   │   └── frame-2.png               # Complete drawing
│   │   └── another-sequence/
│   │       ├── frame-1.png
│   │       └── frame-2.png
│   ├── prop-sequences/
│   │   └── prop-name/
│   │       ├── frame-1.png               # Setup (calm, presenting)
│   │       └── frame-2.png               # Insight (animated, eureka)
│   └── story-sequences/
│       └── story-name/
│           ├── character-sheet.png        # All characters, neutral bg
│           ├── frame-1.png               # Scene 1 (16:9)
│           ├── frame-2.png               # Scene 2 (16:9)
│           └── frame-N.png               # As many as needed (3-7)
├── presentation.js                    # Single source of truth (slides, notes, assets)
├── presentation.pptx                     # Generated deck (.gitignore)
└── presentation.pdf                      # PDF export (.gitignore)
```
