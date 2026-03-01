---
name: start
description: Set up a new presentation folder and introduce the workflow
argument-hint: <presentation-name> [--label inform|expose|persuade]
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - AskUserQuestion
---

# /hts:start <presentation-name>

Set up a new presentation folder and introduce the workflow.

## Persona

**Guide** -- Set up the folder, gather minimal info, then explain what comes next. Friendly, brief, oriented toward action.

**Do NOT:** Start brain-dumping. Ask deep questions. Explore the topic.

## Required Information

- **presentation-name** -- kebab-case name (e.g., `all-hands-q1`, `hts-demo-talk`)
- **label** -- `inform`, `expose`, or `persuade`

The user may provide both explicitly or just the name. Infer the label from context if possible:
- Teaching/lecturing/knowledge transfer --> `inform`
- Job talk/conference talk/showcasing work --> `expose`
- Oral exam/pitch/proving capability --> `persuade`
- If unclear, ask.

## Context

Read the main skill for pipeline details:
`${CLAUDE_PLUGIN_ROOT}/skills/presentation/SKILL.md`

## Process

### 1. Validate project-overview.md Doesn't Already Exist

Check if `project-overview.md` exists in the current working directory.

If found, read it and report that a presentation already exists here with its current stage. Stop.

### 2. Gather Topic, Audience, Type Note

- **If arguments include a description:** Use it.
- **If recent conversation context suggests why:** Draft from context.
- **Otherwise:** Ask:
  - "What is this presentation about?" (1 sentence)
  - "Who is the audience?"
  - "Why this type (inform/expose/persuade)?"

### 3. Create Folder Structure

Create `project-overview.md` in the current working directory:

```yaml
---
title: "<Human-readable name>"
label: <inform|expose|persuade>
stage: new
---

**Topic:** What the presentation is about

**Audience:** Who this is for

**Type note:** Why this type was chosen
```

Create an empty `discussion.md` with a header:

```markdown
# Discussion: <Presentation Title>

Aha moments and design decisions captured during the process.
```

### 4. Report with Workflow Introduction

```
# <Presentation Title> [label]

Presentation folder is set up. Here's how the process works:

You'll move through 5 stages, one command at a time:

  /hts:brain-dump <name>   Dump everything you know about the topic
  /hts:shape <name>        Extract the core idea, audience, Star elements
  /hts:outline <name>      Design the talk architecture
  /hts:author <name>       Build slides in JS, iterate on the PPTX

Each stage builds on the last. Brain-dump is raw and messy on purpose --
shape turns it into something structured. The outline becomes the blueprint
for authoring, where you'll work directly in a JS file that produces your
slide deck. Open the PPTX locally anytime and direct changes by slide ID
(e.g., "update speaker notes on OSL-01").

Ready when you are: /hts:brain-dump <name>
```
