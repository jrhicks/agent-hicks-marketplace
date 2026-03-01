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

# /hts:author

Assist the user in completing the authoring stage.

## Entry

1. Read `${CLAUDE_PLUGIN_ROOT}/skills/presentation/SKILL.md` and `${CLAUDE_PLUGIN_ROOT}/skills/presentation/guides/produce-guide.md` for the full methodology.
2. Read `project-overview.md` in the current working directory.
3. Gate:
   - Stage `outlining`: update to `authoring`, begin.
   - Stage `authoring`: resume -- read existing `05-author/presentation.js`, check what assets exist.
   - No `project-overview.md`: "Run `/hts:start` first."
   - Before `authoring` and not `outlining`: "Outline is not complete. Run `/hts:outline` first."
4. Assist the user in completing the authoring stage per the skill and guide.
5. On completion: set `stage: done`, report final artifacts.
