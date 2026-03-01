---
name: outline
description: Design the talk architecture and media plan
argument-hint: <presentation-name>
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - AskUserQuestion
---

# /hts:outline

Assist the user in completing the outline stage.

## Entry

1. Read `${CLAUDE_PLUGIN_ROOT}/skills/presentation/SKILL.md` and the outline guides:
   - `${CLAUDE_PLUGIN_ROOT}/skills/presentation/guides/outline-guide/guide.md`
   - `${CLAUDE_PLUGIN_ROOT}/skills/presentation/guides/outline-guide/inform-guide.md`
   - `${CLAUDE_PLUGIN_ROOT}/skills/presentation/guides/outline-guide/expose-persuade-guide.md`
2. Read `project-overview.md` in the current working directory.
3. Gate:
   - Stage `shaping`: update to `outlining`, begin.
   - Stage `outlining`: resume -- check which brainstorm files exist.
   - No `project-overview.md`: "Run `/hts:start` first."
   - Before `outlining` and not `shaping`: "Shape is not complete. Run `/hts:shape` first."
   - Past `outlining`: "Already in <stage>. Cannot move backward."
4. Assist the user in completing the outline stage per the skill and guides.
5. On completion: set `stage: authoring`, report next command `/hts:author`.
