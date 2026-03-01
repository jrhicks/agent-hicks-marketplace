---
name: shape
description: Define audience, extract core idea, build Star elements
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - AskUserQuestion
---

# /hts:shape

Assist the user in completing the shape stage.

## Entry

1. Read `${CLAUDE_PLUGIN_ROOT}/skills/presentation/SKILL.md` and `${CLAUDE_PLUGIN_ROOT}/skills/presentation/guides/shape-guide.md` for the full methodology.
2. Read `project-overview.md` in the current working directory.
3. Gate:
   - Stage `brain-dumping`: update to `shaping`, begin.
   - Stage `shaping`: resume -- check which brainstorm files exist.
   - No `project-overview.md`: "Run `/hts:start` first."
   - Before `shaping` and not `brain-dumping`: "Brain-dump is not complete. Run `/hts:brain-dump` first."
   - Past `shaping`: "Already in <stage>. Cannot move backward."
4. Assist the user in completing the shape stage per the skill and guide.
5. On completion: set `stage: outlining`, report next command `/hts:outline`.
