# /kitt:disable-speak

Disable text-to-speech for this session.

## Steps

Emit the disable marker. Your response MUST include this exact line:

```
<!-- SPEAK-DISABLE -->**Speech disabled.**
```

**Do NOT** run `rm`, `pkill`, or any cleanup commands. The hook handles all cleanup (removing session files, releasing voice lock, killing `say`) when it sees the SPEAK-DISABLE marker.

## Post-disable Behavior

**Stop including `<!-- SPEAK -->` markers in your responses.** The speak skill is no longer active. No more TTS markers until the user runs `/kitt:enable-speak` again.
