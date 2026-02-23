# /kitt:whats-going-on

Situation report. Render a status table from current context. No tool calls -- just answer from what's already known. Use "?" for unknown cells.

## Speech

After the table, add a SPEAK marker that reads out the **Currently** cell. Allowed to be slightly longer than normal -- up to 10 words. Example:

```
<!-- SPEAK -->**Halfway through the hook refactor, two files left**
```

## The Table (render this first, then the SPEAK marker)

Each cell is 5-7 words max. The table IS the answer. Nothing else after it (except the SPEAK marker).

```
+-----------+-----------------------------------------+
| While     | [verb-ing] [thing] for [user/goal]      |
| Noticed   | [specific problem or motive]            |
| Currently | [where things stand right now]          |
| Next      | [very next task to pick up]             |
| Blocked   | [waiting on user/external]              |
| Parked    | [set aside, not forgotten]              |
| Pending   | [uncommitted/unsaved work]              |
+-----------+-----------------------------------------+
```

## Line Rules

- **While** -- zoom out to the user story. What are you doing and for whom? e.g. "adding TTS for developer feedback".
- **Noticed** -- WHY this work is happening. The specific problem or motive.
- **Currently** -- status snapshot. What's actually built, tested, or blocked right now.
- **Next** -- the very next task to pick up.
- **Blocked** -- anything waiting on user, external dependency, or decision. "none" if clear.
- **Parked** -- tasks discussed but intentionally set aside.
- **Pending** -- uncommitted files, unsaved state, things that need persisting.

## Rules

1. **No preamble.** Never say "Great question!" or "Let me think about that."
2. **No follow-up.** Don't offer to explain more.
3. **No hedging.** Don't say "it depends" without saying what it depends on.
4. **Be opinionated.** "Should we X?" gets a yes or no.
5. **Anchor the invoker.** Name projects/features/decisions explicitly.
6. **Don't fabricate.** "I don't know" beats a guess.
7. **Table cells are 5-7 words.** No exceptions.

## Anti-Patterns

- Do NOT run tool calls (git, grep, glob) to gather context
- Do NOT fabricate cells to avoid "?"
- Do NOT dump paragraphs
- Do NOT pad table cells past 7 words
- Do NOT add menus, drill-downs, or AskUserQuestion after the table
