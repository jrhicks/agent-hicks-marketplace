# /kitt:enable-speak

Enable text-to-speech for this session.

## Prerequisites & Voice Selection

Run the find-voice script (description: "Checking dependencies and finding voice"):

```bash
${CLAUDE_PLUGIN_ROOT}/skills/speak/scripts/find-voice.sh
```

Output is a single line:
- `OK:<voice>` -- prerequisites pass, use the voice after the colon
- `ERROR:<message>` -- tell the user the message and stop

## Enable

1. Load the **kitt:speak** skill to learn marker format and rules.

2. Emit the enable marker with the chosen voice. Your response MUST include this exact line (substituting VOICE with the chosen voice name, e.g. `Daniel`, `Samantha`, `Karen`, `Moira`, `Rishi`):

```
<!-- SPEAK-ENABLE(voice:VOICE) -->**Speech enabled.**
```

Example: `<!-- SPEAK-ENABLE(voice:Karen) -->**Speech enabled.**`

**Do NOT** create any files (`touch`, `echo >`, etc.). The hook handles all file creation when it sees the SPEAK-ENABLE marker.

## Post-enable Behavior

**From now on, include `<!-- SPEAK -->**brief spoken summary**` markers in every substantive response.**

The speak skill (loaded in step 1) defines the full rules. Key points:
- Task completions, errors, questions, key findings -- always mark
- Keep spoken text under 5 words
- Be informative, not agreeable ("Updating the parser" not "Sure, will do")
- Your session voice is set at enable time; override per-marker with `voice:Name` if needed
