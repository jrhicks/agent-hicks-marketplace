# Specify Guide

Create a slide-by-slide blueprint from the locked-in outline. Every slide is defined: content, type, delivery cues, verbal punctuation markers, speaker notes.

This is where slide crimes get caught. Winston's entire Tools section is a masterclass in what goes wrong with slides and how to fix it. The crimes are not arbitrary aesthetic preferences -- each one has a cognitive mechanism behind it. Understanding the mechanism makes you a better auditor.

---

## The Universal Truth

Winston was in Terminal A at Logan Airport. He'd just come back from a really miserable conference and the flight was horrible -- "one of those that feels like an unbalanced washing machine." For the only time in his life, he stopped on his way to his car and had a cup of coffee.

Someone approached him: "Are you Professor Winston?" "I think so," he said. The person was on his way to Europe to give a job talk: "Would you mind critiquing my slides?" "Not at all," Winston said. "You have too many and they have too many words." "How did you know?" the person asked, thinking Winston had seen a talk of his before. He hadn't.

"Because it's always true -- there are always too many slides, always too many words."

This is the lens for the entire Specify stage. Every decision defaults toward fewer slides, fewer words, more air. When in doubt, cut.

---

## Slides as Condiments

Winston demonstrates the crimes by committing all of them simultaneously. He stands far from the slides. He reads them aloud. The slides are dense with text. And the audience gets driven crazy.

The core metaphor: **slides should be condiments to what you're saying, not the main event.** When the slide is the main event, the speaker becomes background noise. When the speaker is the main event, slides enhance what's being said.

The mechanism is cognitive: humans have one language processor. It either reads or it listens. If your slides have a lot of text, you force the audience to read -- and they stop hearing you. A student of Winston's ran an experiment: he taught web programming concepts, putting half on slides and speaking the other half. Subjects remembered what was on the slides better than what was spoken. In the after-action report, one subject said: "I wish you hadn't talked so much, it was distracting."

That's the consequence of too many words. The speaker becomes the distraction.

---

## Progressive Fixing

Winston demonstrates how to fix a crime-ridden slide in progressive steps. Each step removes one layer of clutter and returns attention to the speaker:

**Step 1: Remove background junk.** Decorative backgrounds, gradient fills, watermarks -- always a distraction. Strip to clean white or simple dark.

**Step 2: Remove most words.** When Winston reduces the words, everything he read before he's "not licensed to say because it's not on the slide." But he still says it -- now it's spoken content, not read content. The audience listens instead of reading. This is the key transformation.

**Step 3: Remove logos.** You don't need them. Simplification.

**Step 4: Remove the title.** "I'm telling you the title, it doesn't have to be up there." The speaker announces what the section is about verbally. The slide doesn't need to repeat it.

**Step 5: Remove bullets.** Even the bullet markers themselves are clutter. The words can stand on their own.

Each step is a question: does removing this hurt comprehension? Almost always the answer is no. What it does hurt is the presenter's security blanket -- the feeling that everything important is written down somewhere visible. That security is the enemy of engagement.

---

## Spec Format

Each slide entry follows this template:

```markdown
### Slide N: [Title]

**Type:** title | content | chalkboard-1 | chalkboard-2 | prop-1 | prop-2 | story-1..N | section-break | contributions
**Content:** What appears on the slide (text, bullet points, image description)
**Speaker notes:** What the presenter says (conversational, not a script)
**Delivery cues:**
- [verbal punctuation] "There are three key ideas..."
- [question] "What do you think happens next?" (wait 7s)
- [cycle] Revisits concept from slide X
- [passion] Express genuine excitement here
- [pause] Let this land
```

Delivery cues use bracketed tags so the presenter can scan for them quickly.

---

## Slide Types

| Type | Description | When |
|------|-------------|------|
| `title` | Opening slide. Presentation title, speaker, collaborators, date. | First slide |
| `content` | Standard polished slide. Minimal text, big fonts. | Most slides |
| `chalkboard-1` | First frame of a chalkboard sequence. Green board, partial drawing. | Board moments |
| `chalkboard-2` | Second frame. Same board, complete drawing. Always follows chalkboard-1. | Immediately after chalkboard-1 |
| `prop-1` | First frame of a prop sequence. Professor presents the prop (setup). | Prop moments |
| `prop-2` | Second frame. Professor demonstrates insight (eureka). Always follows prop-1. | Immediately after prop-1 |
| `story-1`..`story-N` | Frames of a story sequence. 3-7 full-bleed editorial illustrations depicting different scenes with consistent characters. Variable length -- as many frames as the narrative has beats. | Narrative interludes |
| `section-break` | Visual separator between major sections. | Between sections |
| `contributions` | Final slide. Lists what was accomplished. Stays up during Q&A. | Last slide |

**Chalkboard sequences are always pairs.** 2 slides per drawing, never 3. They simulate drawing on a board -- the audience sees the idea appear as you advance. Complete mode switch from polished slides.

**Prop sequences are always pairs.** 2 slides per prop: frame 1 is the professor presenting the prop (calm, setup), frame 2 is the professor demonstrating the insight (animated, eureka). Editorial illustration style, NOT chalkboard aesthetic. See `guides/prop-sequences.md` for visual style and prompt templates.

**Story sequences are variable length (3-7 frames).** Each frame is a full-bleed editorial illustration depicting a different scene in a narrative -- book synopsis, case study, or extended anecdote. Zero text on frames; the speaker narrates. Character consistency is maintained via a character reference sheet generated before any scene frames. See `guides/story-sequences.md` for the character sheet workflow and prompt templates.

---

## Slide Crime Audit

Before finalizing, audit every slide against Winston's crimes. These aren't style preferences -- each one has a cognitive mechanism that degrades communication.

### Crime 1: Too Many Slides

Not just too many words per slide -- too many slides total. Each slide transition is a cognitive event. Too many transitions fragment the narrative. When Winston critiques at Terminal A, the first thing he says is "you have too many" -- before he even mentions words.

**Test:** Print the deck and lay it out on a table. If you can't take in the arc of the talk at a glance, there are too many slides.

### Crime 2: Too Many Words

The consequence of Microsoft allowing fonts that are too small. If your font is below about 40-50 point, it's probably enabling too many words.

**Test:** Make a sample slide with text at different sizes -- 20pt, 30pt, 40pt, 50pt, 60pt. Display it on the actual projector or screen at the actual distance. That's your minimum legible size. Winston and a student agreed: 40-50pt minimum. Below that, you're not just getting small text -- you're getting permission to overload the slide.

**Fix:** Apply progressive fixing. Remove background, reduce words, remove logos, remove title, remove bullets. Each step should feel scary (you're removing your security blanket) and the result should feel clearer.

### Crime 3: Reading Your Slides

If the speaker notes duplicate what's on the slide, the presenter will read. The audience will read faster. The presenter becomes redundant.

**Fix:** Speaker notes should ADD to slides, not repeat them. The slide shows the skeleton; the speaker provides the flesh. When you reduce words on the slide (progressive fixing step 2), you're forced into this pattern naturally.

### Crime 4: The Tennis Match

When the speaker is far from the slides, the audience's eyes bounce back and forth -- speaker, slide, speaker, slide. It's exhausting. Winston demonstrates this by standing at the far side of the room from his slides, forcing the audience into the tennis match.

**Fix:** Plan positioning. The speaker should be near the projected material so the audience can take in both in one visual field. If the room makes this impossible, restructure the slides to be less dependent on simultaneous viewing.

### Crime 5: The Laser Pointer

"It's a wonder more people aren't driven into epileptic fits." The laser pointer creates a recursive disaster: to point at something, you must turn away from the audience. You lose eye contact. You lose engagement. Winston sat with a student watching a talk where the speaker used a laser pointer with his back to the audience the entire time. The student said: "We could all leave and he wouldn't know."

The laser pointer also creates a lovely recursive picture -- you can point the laser at the back of your own projected head, which shows the back of your head, which shows the back of your head...

**Fix:** Put arrows, circles, or highlights directly on the slide. "Now look at that guy at the end of arrow number one." You don't need a laser pointer to direct attention.

### Crime 6: Too Heavy

Not enough air, not enough white space, not enough imagery. The presenter has exploited small fonts to pack maximum content onto every slide.

**Test:** Print the deck and lay it out on a table. Too-heavy talks are immediately visible -- walls of text, no breathing room.

**Contrast:** Winston shows one of his own talks. "It wasn't a deeply technical talk but I show it because there's air in it. It's mostly pictures of things. Three or four slides have text on them but when I come to those I give the audience time to read them, and they're there because they might have some historical significance." Air is the goal.

### Crime 7: Background Clutter

Decorative templates, corporate branding, textured backgrounds -- all distraction. The first step of progressive fixing is always to remove background junk.

### Hapax Legomenon

One intentionally complex or unreadable slide per presentation, maximum. The complexity IS the point. Winston's example: a diagram showing the complexity of governing in Afghanistan -- impossibly tangled, deliberately incomprehensible. The audience can't understand it, and that's the message.

You can have one per presentation, one per paper, one per book. Flag it explicitly in the spec so the producer doesn't try to "fix" it.

### Crimes in the Wild

Winston shows real examples to prove these aren't hypothetical:

- **Hands in pockets** -- the speaker at a real event
- **The Bartos Theater** -- You go down steps at the Media Lab, cross an open space, turn right down a corridor ("at this point whenever I go in there I wonder if there are torture implements around the corner"), and enter a dark gloomy place. It's well-named as a "Theater" -- it's where you watch a movie, not where you give a talk. A crime in time-and-place selection.
- **The Strata talk** -- Slide 80 of the presentation. Dense with words. First of 10 conclusion slides. The sponsor of the meeting is reading his email. The co-sponsor is examining the lunch menu. One audience member appears attentive in the still photo, but in video would be visibly asleep.

These aren't edge cases. They're the default outcome when crimes go unchecked.

---

## Opening and Closing

**First slide:** Title slide with collaborators listed. Not on the last slide -- putting collaborators last suggests nobody knows who did the work. Recognize them up front, then your final slide tells people who you are and what you accomplished.

**Opening delivery:** Empowerment promise. No joke. The audience is still calibrating your voice. They're putting laptops away, adjusting to your speaking parameters. They're not ready for a joke.

**Last slide:** Contributions. Not "Questions?", not "Thank You", not "The End", not "Conclusions." The contributions slide stays up during Q&A and while people file out. It tells them who you are.

**Closing delivery:** A joke (Doug Lenat: "I always finish with a joke -- that way people think they've had fun the whole time"), a benediction, or a salute to the audience. NOT "thank you."

---

## Act-Based Organization

For presentations with multiple acts, organize the spec as a directory:

```
05-spec/
├── 00-overview.md     # Act index, cross-act references
├── act1-slug.md       # Each act self-contained
├── act2-slug.md
└── ...
```

The overview file lists acts with slide ranges and cross-act references. Each act file uses the standard slide format (`### Slide N: Title`, etc.) scoped to that act's slides.

**When to use:** Presentations with 3+ acts or 15+ slides benefit from act-based organization. Short presentations (< 15 slides) can stay as a single `05-spec.md`.

**Asset references:** Each slide with a produced asset includes:
`**Asset:** 06-produce/assets/path/to/file.png`
This enables the review utility (`/presentation review`) to link images automatically.

**Overview file format:**

```markdown
# Spec: [Presentation Title]

## Acts

| # | Act | Slides | File |
|---|-----|--------|------|
| 1 | Setup | 1-8 | act1-setup.md |
| 2 | Context | 9-11 | act2-context.md |

## Cross-Act References

- Theme X (Act 1 -> Act 3): How it connects
```

---

## Verbal Punctuation Placement

Go through the outline's delivery plan and place each marker on specific slides:
- Enumeration markers at section starts
- Structure announcements at transitions
- Questions at engagement dips (typically after complex material or 10+ minutes of content; wait 7 seconds for answers)
- Cycling markers where concepts are revisited

Each marker becomes a `[delivery cue]` in the spec.
