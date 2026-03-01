---
name: brain-dump
description: Dump raw content for the presentation
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - AskUserQuestion
---

# /hts:brain-dump

Assist the user in completing the brain-dump stage.

## Entry

1. Read `${CLAUDE_PLUGIN_ROOT}/skills/presentation/SKILL.md` for the full methodology.
2. Read `project-overview.md` in the current working directory.
3. Gate:
   - Stage `new`: update to `brain-dumping`, begin.
   - Stage `brain-dumping`: resume -- check which deliverables exist.
   - No `project-overview.md`: "Run `/hts:start` first."
   - Past `brain-dumping`: "Already in <stage>. Cannot move backward."
4. Assist the user in completing the brain-dump stage per the skill.
5. On completion: set `stage: shaping`, report next command `/hts:shape`.
