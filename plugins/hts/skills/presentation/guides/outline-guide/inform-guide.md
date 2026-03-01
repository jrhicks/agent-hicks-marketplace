# Inform Outline Guide

**Persona refinement: Instructional Designer** -- Think in learning objectives, knowledge scaffolding, building understanding step by step. The goal is knowledge transfer, not showcasing.

---

## The Nature of Inform Talks

An inform talk exists to change how people think. Not to display what you know, not to cover material, not to impress -- to build understanding in someone else's head that wasn't there before.

Winston surveyed his department about inspiration. He talked to incoming freshmen, senior faculty, and everyone in between. What he found reveals the architecture of a great inform talk:

**Freshmen** were inspired by a high school teacher who told them they could do it. The "you can do it" message is the emotional foundation of informing. Your audience needs to believe the material is within their reach.

**Senior faculty** were inspired by someone who helped them see a problem in a new way. This is the intellectual payoff of informing. You aren't just adding facts to a pile -- you're reorganizing how someone perceives the problem space.

**Everyone** was inspired when someone exhibited passion about what they were doing. Not performative excitement. Genuine fascination that naturally communicates itself. Winston puts it simply: "I do artificial intelligence. How can you not be interested in artificial intelligence? If you're not interested in artificial intelligence you're probably not interested in interesting things." When he lectures in his AI class, it's natural for him to talk about what he thinks is cool and how exciting some new idea is. That kind of expression of passion makes a difference while informing.

This gives you three design layers for an inform talk:
1. **Emotional foundation** -- "you can do it" (audience believes the material is accessible)
2. **Intellectual transformation** -- "see it a new way" (audience's mental model shifts)
3. **Passion current** -- your genuine fascination flowing through the delivery

---

## Promise, Then Inspire

Every inform talk starts with a promise -- the empowerment promise carried forward from the Shape. But for inform talks, the promise has a second movement: inspiration. You promise what they'll know, then you inspire them to want to know it.

### Express How Cool Stuff Is

One of Winston's most powerful techniques for the opening of an inform talk is to show, concretely, why the subject matter is astonishing. Not by asserting it's interesting but by demonstrating the gap between naive and informed.

His example: teaching resource allocation (the kind of ideas you'd need to allocate aircraft to a flight schedule or schedule a factory). He frames it as coloring states on a US map so no bordering states share a color. He shows the naive algorithm running. Then he asks: "Should we wait till it finishes?" No -- because the sun will have exploded and consumed the Earth before it finishes. But with a slight adjustment -- which his students will understand in the next 50 minutes -- it completes in seconds.

"Isn't that cool? You got to be amazed by stuff that takes a computation from longer than the lifetime of the solar system into a few seconds."

The structure: show the problem. Show the naive attempt failing spectacularly. Promise the insight that makes it trivial. Give a timeline ("you will understand this in the next 50 minutes"). The audience is now hooked because they've seen the gap between ignorance and understanding, and they've been promised they'll cross it.

Plan this for your opening: what before-and-after can you demonstrate that makes the audience feel the gap?

---

## Teaching People How to Think

Winston asked MIT faculty what their most important purpose was. They all said "teach people how to think." He asked the natural follow-up: "How do you teach people how to think?" Blank stare. Nobody could answer.

Winston's answer is that we are storytelling animals. We start developing story understanding and manipulation skills with fairy tales in childhood and continue through professional schools -- law, business, medicine, engineering -- and throughout life. Thinking is story work.

If that's what thinking is about, then teaching people how to think means providing them with:

- **The stories they need to know** -- the canonical examples, the case studies, the narratives that carry the field's knowledge. Not abstract principles first, stories first.
- **The questions they need to ask about those stories** -- the analytical lenses that separate surface from substance. What should they be looking for?
- **Mechanisms for analyzing those stories** -- the formal tools, frameworks, or mental models that let them take stories apart and understand why they work.
- **Ways of putting stories together** -- the compositional skill of building new understanding by combining existing stories. Synthesis, not just analysis.
- **Ways of evaluating how reliable the story is** -- the critical judgment to know when a story is solid versus when it's just plausible. Epistemological hygiene.

This framework is your design tool. For each section of your inform talk, ask: which of these five am I providing? A section that introduces a canonical example is providing a story. A section that shows a framework is providing a mechanism for analysis. A section that compares two approaches is teaching evaluation.

If your talk only provides stories without questions or mechanisms, the audience will remember anecdotes but not be able to think independently. If it's all mechanisms with no stories, the audience will have tools they don't know how to use. The five elements should be present across the talk as a whole, though any individual section will emphasize one or two.

---

## Boards Are the Inform Medium

Winston is unambiguous: the board is the right tool for informing. Slides are for exposing. When you're teaching, you use a board. Three virtues:

**Graphic quality.** You can draw, diagram, visualize naturally. The board invites spatial thinking. You can sketch a relationship, circle a key term, draw an arrow connecting two ideas. This is how understanding gets built -- spatially, incrementally, visually.

**Speed.** The speed at which you write on the board is approximately the speed at which people absorb ideas. This is a profound insight. Slides flip too fast. When you present pre-made slides, you're asking the audience to absorb at your clicking speed, not their thinking speed. The board forces you to pace yourself to human cognition. The bottleneck of your handwriting speed is actually a feature, not a bug.

**Target.** The board gives you something to do with your hands and creates a physical focal point. Many novice speakers become suddenly aware of their hands as if they were private parts that shouldn't be exposed in public. Hands go into pockets or behind the back. Winston tells a story about visiting a convent in Serbia where a nun immediately pulled his hands from behind his back because the gesture was extraordinarily insulting in that culture -- associated with concealing a weapon. The board solves this: you have something to point at, write on, gesture toward. Your hands have a job.

Underlying all three virtues is empathetic mirroring. When the audience watches you write on the board, mirror neurons in their brains activate. They feel themselves writing. They feel the movement of drawing a diagram, the deliberation of choosing where to place a concept. You can't get this from a slide. You can't get it from a picture. You need to see it happening in the physical world. This is why students always say "more chalk, less PowerPoint."

Winston watched Seymour Papert give a lecture. He thought it was terrific, so he went a second time -- first to absorb the content, second to note the style. What he discovered: Papert was constantly pointing at the board. And then Winston noticed that none of the stuff Papert was pointing to had anything to do with what he was saying. Nevertheless, it was effective. The board creates a gravitational field of attention. Even imprecise pointing works because the physical gesture of engagement -- the body turning, the arm extending, the hand indicating -- activates empathetic mirroring in the audience.

**Virtual adaptation:** In virtual presentations, "board" means chalkboard sequence slides -- 2 back-to-back slides that progressively reveal a drawing on a green chalkboard background. These are a deliberate mode switch from polished slides. The point is to simulate the incremental, hand-drawn quality of board work. See the **pptx** skill's chalk-board guide for the workflow.

Default most sections to `[board]`. Use slides only for data, complex diagrams you can't draw live, or photographic evidence. Mark each section: `[board]`, `[slides]`, or `[board+slides]`.

---

## Brainstorm 1: Sections

**Deliverable:** `04-outline/01-sections.md`

Draft the section outline from the shape compilation. For inform talks, design each section through the storytelling-animals lens:

- **What story does this section tell?** (canonical example, case study, narrative)
- **What question does it teach the audience to ask?** (analytical lens)
- **What mechanism does it provide?** (framework, mental model, tool)
- **How does it connect to other sections?** (composition, synthesis)
- **How does it build confidence?** (the "you can do it" layer)

Each section should:
- Build on what came before (knowledge scaffolding)
- Have a clear learning objective (what will the audience understand after this section?)
- Be labeled with medium: `[board]`, `[slides]`, or `[board+slides]`
- Note the "how cool stuff is" moment, if any (the before/after that makes the insight visceral)

Structure proposal:

```markdown
# Sections

## 1. [Opening] [board]
Empowerment promise. Express how cool stuff is (before/after demo).
Situating.

## 2. [Section Name] [board]
What this covers. Learning objective: ...
Story: ... / Mechanism: ... / Question: ...

## 3. [Section Name] [board]
What this covers. Learning objective: ...
Story: ... / Mechanism: ... / Question: ...

...

## N. [Closing] [slides]
Contributions slide. Final words.
```

**Cycling plan:** Note which concepts need revisiting in later sections. Mark with `(cycles: section N)`. Remember: at any given moment about 20% of your audience is fogged out. Cycling isn't repetition for slow learners -- it's probability management for human attention.

Present the draft for user reaction. Revise until approved.

---

## Brainstorm 2: Delivery

**Deliverable:** `04-outline/02-delivery.md`

Walk through the section outline and plan delivery specifics:

- **Verbal punctuation placements** -- where to enumerate, announce structure, create seams
- **Question placements** -- 2-4 questions with location and purpose (7 seconds of silence is the standard wait time, even though it feels like eternity)
- **Cycling plan** -- which concepts get revisited and where
- **Opening** -- the empowerment promise + the "how cool stuff is" demo that hooks them
- **Passion beats** -- mark moments where genuine fascination naturally surfaces. Don't script passion, but identify the material that makes you lean forward. That's where passion will flow.
- **Closing** -- contributions list + final words (joke, benediction, or salute)

```markdown
# Delivery Plan

## Opening
[Empowerment promise. "How cool stuff is" demo if applicable. First sentences.]

## Verbal Punctuation Points
- Before section 2: "There are three key ideas..."
- After section 3: "So we've now seen X and Y. The third idea is..."

## Questions
- After section 2: "[question]" (purpose: check understanding)
- During section 4: "[question]" (purpose: re-engage, create surprise)

## Cycling
- Concept A: introduced in section 2, revisited in section 4 from [angle]
- Concept B: ...

## Passion Beats
- Section 3: [this is where the "isn't that cool" moment lives]
- Section 5: [this is where the "you can do it" moment lives]

## Props
Physical:
- [prop name]: [what it demonstrates] -- [how to source/build]

Narrative sequences (story synopsis, case study, multi-scene anecdote):
- [story name]: [what narrative it walks through]
  - Cast: [character name] ([description, role]) / [character name] ([description, role])
  - Scene plan (point drives the visual):

    | # | Point (what you say) | Characters | Scene | Disposition |
    |---|----------------------|------------|-------|-------------|
    | 1 | ... | ... | ... | ... |
    | 2 | ... | ... | ... | ... |

Illustration sequences (2-frame prop adaptation):
- [prop name]: Frame 1 [setup] / Frame 2 [insight]

## Closing
Final slide: Contributions
- [contribution 1]
- [contribution 2]
- [contribution 3]

Final words: [joke / benediction / salute]
```

---

## Lock-In

Synthesize sections + delivery into `04-outline.md`. This is the compilation the Specify stage reads.
