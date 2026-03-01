# /kitt:plot-course-to {goal}

Navigation briefing. Given a destination, plot the route from current position to {goal}. No tool calls -- navigate from what's already known. Use "?" for unknown legs.

## Speech

After the chart, add a SPEAK marker reading the **First Move** cell. Example:

```
<!-- SPEAK -->**Fix the failing hook test first**
```

## The Chart (render this first, then the SPEAK marker)

Each cell is 5-7 words max. The chart IS the answer. Nothing else after it (except the SPEAK marker).

```
+--------------+------------------------------------------+
| Destination  | [restate goal in 5-7 words]              |
| Position     | [where things stand right now]           |
| First Move   | [very next action to take]               |
| Route        | [ordered legs: A → B → C]                |
| Hazards      | [risks, blockers, or decisions ahead]    |
| Detours      | [known alternatives if route fails]      |
| ETA          | [rough sense of distance: near/mid/far]  |
+--------------+------------------------------------------+
```

## Cell Logic

1. **Destination** -- restate {goal} concisely. Clarify it if it's vague.
2. **Position** -- current state relative to the goal. Not general status -- gap analysis.
3. **First Move** -- one concrete action that moves toward the goal right now.
4. **Route** -- ordered milestones as a short chain. Use `→` between legs. 3-5 legs max.
5. **Hazards** -- anything that could derail the route: decisions needed, unknowns, external deps.
6. **Detours** -- if the main route fails, what's the fallback? "none known" if none.
7. **ETA** -- not a time estimate. Use `near` (this session), `mid` (days), or `far` (weeks/open-ended).

## Rules

1. **No preamble.** Never say "Great question!" or "Let me think about that."
2. **No follow-up.** Don't offer to explain more.
3. **No hedging.** Name the route. Commit to it.
4. **Be opinionated.** If there are two routes, pick the better one and name the other as a Detour.
5. **Anchor to the actual goal.** Don't drift into adjacent topics.
6. **Don't fabricate.** "?" beats a confident lie.
7. **Chart cells are 5-7 words.** No exceptions. Route legs may use `→` as connective tissue.

## Anti-Patterns

- Do NOT run tool calls (git, grep, glob) to gather context
- Do NOT fabricate cells to avoid "?"
- Do NOT write paragraphs below the chart
- Do NOT pad cells past 7 words
- Do NOT offer multiple routes in the Route cell -- pick one, put the other in Detours
- Do NOT use ETA as a time estimate in hours or minutes
