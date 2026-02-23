---
name: speak
description: Internal skill loaded by /kitt:enable-speak. Not user-invocable. Provides marker format rules, voice selection, and speech content guidelines for embedding SPEAK markers in Claude Code responses.
version: 3.1.0
---

# kitt:speak -- SPEAK Marker Reference

How to embed speech markers in Claude Code responses. Loaded by `/kitt:enable-speak`, not invoked directly.

## Marker Format

```
<!-- SPEAK -->**brief summary here**                              (defaults: session voice, 180 wpm)
<!-- SPEAK(voice:Samantha) -->**with custom voice**               (custom voice)
<!-- SPEAK(rate:250) -->**with custom speed**                     (custom speed)
<!-- SPEAK(voice:Samantha rate:250) -->**both**                   (both)
```

Defaults: your session voice (set at enable time), rate `180` wpm.

## Control Markers

These are emitted ONLY by `/kitt:enable-speak` and `/kitt:disable-speak`, never in regular responses:

```
<!-- SPEAK-ENABLE(voice:Karen) -->**Speech enabled.**             (enable session speech)
<!-- SPEAK-DISABLE -->**Speech disabled.**                        (disable session speech)
```

The hook uses these to create/remove per-session enabled files and voice locks.

## When to Include Markers

**DO include** a `<!-- SPEAK -->` marker for:
- Task completions ("Done, tests pass.")
- Errors or failures ("Build failed.")
- Questions to the user ("Which approach?")
- Key findings or status updates ("Found the bug.")

**DO NOT include** markers for:
- Code blocks, file listings, verbose output
- Intermediate tool-call-only responses
- Long explanations (pick a one-line headline instead)
- Flattery or low-value acknowledgment ("good call", "will do", "got it", "sounds good", "absolutely")

## Speech Content Rules

Speech must be **informative, not agreeable**. Describe WHAT you're doing, not THAT you agree.

| Bad (blocked by hook)            | Good                          |
|----------------------------------|-------------------------------|
| "Good call, doing that."         | "Adding flattery filter."     |
| "Sure, will do."                 | "Updating the hook script."   |
| "Got it, on it."                 | "Refactoring the parser."     |
| "Absolutely, great idea."        | "Building the new endpoint."  |

Speech must be **plain English words only**. No hashes, hex codes, line numbers, or alphanumeric noise. Humans cannot follow spoken gibberish like commit SHAs or UUIDs.

| Bad                              | Good                          |
|----------------------------------|-------------------------------|
| "Pushed d651e91."                | "Pushed to main."             |
| "Fixed line 133."               | "Fixed the shell config."     |
| "Error 0x8BADF00D."             | "Memory error found."         |
| "Version 3.1.4-rc2."            | "New version pushed."         |

Short version labels like "v3" are OK.

## Rules

- Keep spoken text under 5 words -- a tiny headline
- Plain English words only -- no hashes, hex, line numbers, or codes
- One marker per response is usually enough
- The marker is invisible to the user (HTML comment) but the bold text renders nicely
- Multiple markers in one response play sequentially

## Available Voices

Voice is chosen at enable time. First unclaimed voice from the pool:

| Voice | Style |
|-------|-------|
| Daniel | British English |
| Samantha | American English |
| Karen | Australian English |
| Moira | Irish English |
| Rishi | Indian English |

Override per-marker with `<!-- SPEAK(voice:Name) -->`. Run `say -v '?'` to see all installed voices.
