#!/bin/bash
# speak.sh - Claude Code Stop hook for TTS (v3.0.0)
#
# Session-specific speech: each session independently enables/disables via
# control markers. Non-speech sessions exit in ~100ms (fast path).
#
# Control markers (emitted by enable/disable commands only):
#   <!-- SPEAK-ENABLE(voice:Karen) -->**Speech enabled.**
#   <!-- SPEAK-DISABLE -->**Speech disabled.**
#
# Speech markers (emitted by Claude in responses):
#   <!-- SPEAK -->**text here**                              (defaults: session voice, 180 wpm)
#   <!-- SPEAK(voice:Samantha) -->**text here**               (custom voice)
#   <!-- SPEAK(rate:250) -->**text here**                     (custom speed)
#   <!-- SPEAK(voice:Samantha rate:250) -->**text here**      (both)
#
# Per-session files in ~/.claude-speak-plugin/:
#   enabled-{SESSION_ID}       voice name; presence = enabled
#   voices/{voice_name}        SESSION_ID; cross-session dedup
#   state-{SESSION_ID}         last-spoken UUID; dedup
#   remind-{SESSION_ID}        reminder cooldown
#
DEFAULT_RATE="180"
SPEAK_DIR="$HOME/.claude-speak-plugin"
mkdir -p "$SPEAK_DIR"
VOICE_LOCK_DIR="$SPEAK_DIR/voices"

# -- Helper: set terminal tab title --
# Always sets title. CLAUDE_CODE_DISABLE_TERMINAL_TITLE=1 means Claude Code
# won't compete, so the speak hook can safely own the tab title.
set_tab_title() {
  printf '\033]0;%s\007' "$1" > /dev/tty 2>/dev/null
}

# -- Guard: python3 required --
command -v python3 >/dev/null || exit 0

# -- Read hook input --
INPUT=$(cat)
TRANSCRIPT_PATH=$(echo "$INPUT" | python3 -c "import sys,json; print(json.loads(sys.stdin.read()).get('transcript_path',''))" 2>/dev/null)
STOP_HOOK_ACTIVE=$(echo "$INPUT" | python3 -c "import sys,json; print(json.loads(sys.stdin.read()).get('stop_hook_active',''))" 2>/dev/null)

# Prevent infinite loops
if [ "$STOP_HOOK_ACTIVE" = "true" ] || [ "$STOP_HOOK_ACTIVE" = "True" ]; then
  exit 0
fi

# Bail if no transcript
if [ -z "$TRANSCRIPT_PATH" ] || [ ! -f "$TRANSCRIPT_PATH" ]; then
  exit 0
fi

# -- Derive session ID from transcript filename --
SESSION_ID=$(basename "$TRANSCRIPT_PATH" .jsonl)
ENABLED_FILE="$SPEAK_DIR/enabled-${SESSION_ID}"

# -- Session-specific enabled check --
if [ -f "$ENABLED_FILE" ]; then
  # Session already enabled -- read stored voice
  DEFAULT_VOICE=$(cat "$ENABLED_FILE")
  set_tab_title "$DEFAULT_VOICE"

  # Check for re-enable with different voice (SPEAK-ENABLE while already enabled)
  if tail -c 4096 "$TRANSCRIPT_PATH" | grep -q 'SPEAK-ENABLE'; then
    RE_VOICE=$(tail -c 4096 "$TRANSCRIPT_PATH" | sed -n 's/.*SPEAK-ENABLE(voice:\([^)]*\)).*/\1/p' | tail -1)
    if [ -n "$RE_VOICE" ] && [ "$RE_VOICE" != "$DEFAULT_VOICE" ]; then
      # Release old voice lock
      old_safe=$(echo "$DEFAULT_VOICE" | tr ' ()' '_--')
      rm -f "$VOICE_LOCK_DIR/$old_safe"
      # Claim new voice lock
      new_safe=$(echo "$RE_VOICE" | tr ' ()' '_--')
      mkdir -p "$VOICE_LOCK_DIR"
      echo "$SESSION_ID" > "$VOICE_LOCK_DIR/$new_safe"
      # Update enabled file
      echo "$RE_VOICE" > "$ENABLED_FILE"
      DEFAULT_VOICE="$RE_VOICE"
      set_tab_title "$DEFAULT_VOICE"
    fi
  fi
else
  # Not enabled -- check if this response contains a SPEAK-ENABLE marker
  sleep 0.1
  if ! tail -c 4096 "$TRANSCRIPT_PATH" | grep -q 'SPEAK-ENABLE'; then
    exit 0  # fast path: not enabled, no enable marker
  fi

  # SPEAK-ENABLE found -- extract voice from marker
  ENABLE_VOICE=$(tail -c 4096 "$TRANSCRIPT_PATH" | sed -n 's/.*SPEAK-ENABLE(voice:\([^)]*\)).*/\1/p' | tail -1)
  [ -z "$ENABLE_VOICE" ] && ENABLE_VOICE="Daniel"

  # Clean stale voice locks (sessions inactive for 10+ minutes)
  mkdir -p "$VOICE_LOCK_DIR"
  for lock in "$VOICE_LOCK_DIR"/*; do
    [ -f "$lock" ] || continue
    lock_session=$(cat "$lock")
    lock_transcript=$(dirname "$TRANSCRIPT_PATH")/${lock_session}.jsonl
    if [ ! -f "$lock_transcript" ] || [ "$(find "$lock_transcript" -mmin +10 2>/dev/null)" ]; then
      rm -f "$lock"
    fi
  done

  # Claim voice lock
  safe_name=$(echo "$ENABLE_VOICE" | tr ' ()' '_--')
  echo "$SESSION_ID" > "$VOICE_LOCK_DIR/$safe_name"

  # Create enabled file with voice
  echo "$ENABLE_VOICE" > "$ENABLED_FILE"
  DEFAULT_VOICE="$ENABLE_VOICE"
  set_tab_title "$DEFAULT_VOICE"
fi

# -- Wait for transcript flush (only enabled sessions pay this cost) --
sleep 0.3

# -- Find last assistant text block --
PARSED=$(grep '"type":"assistant"' "$TRANSCRIPT_PATH" | python3 -c "
import sys, json

uuid = ''
text = ''

for line in sys.stdin:
    try:
        data = json.loads(line.strip())
    except:
        continue
    if data.get('type') != 'assistant':
        continue
    content = data.get('message', {}).get('content', [])
    texts = [c['text'] for c in content if c.get('type') == 'text']
    if texts:
        joined = '\n'.join(texts)
        if joined.strip():
            uuid = data.get('uuid', '')
            text = joined

print(uuid)
print(text)
" 2>/dev/null)

MSG_UUID=$(echo "$PARSED" | head -1)
LAST_MSG=$(echo "$PARSED" | tail -n +2)

if [ -z "$MSG_UUID" ]; then
  exit 0
fi

# -- UUID deduplication --
STATE_FILE="$SPEAK_DIR/state-${SESSION_ID}"
STORED_UUID=""
[ -f "$STATE_FILE" ] && STORED_UUID=$(cat "$STATE_FILE")

if [ "$MSG_UUID" = "$STORED_UUID" ]; then
  exit 0
fi

echo "$MSG_UUID" > "$STATE_FILE"

if [ -z "$LAST_MSG" ]; then
  exit 0
fi

# -- SPEAK-DISABLE detection --
if echo "$LAST_MSG" | grep -q 'SPEAK-DISABLE'; then
  safe_name=$(echo "$DEFAULT_VOICE" | tr ' ()' '_--')
  rm -f "$VOICE_LOCK_DIR/$safe_name"
  rm -f "$ENABLED_FILE"
  pkill -f "say -v" 2>/dev/null || true
  say -v "$DEFAULT_VOICE" -r "$DEFAULT_RATE" "Speech disabled" &
  exit 0
fi

# -- Count SPEAK markers --
MARKER_COUNT=$(echo "$LAST_MSG" | grep -c '<!-- SPEAK' || true)

# -- Guard: reject low-value speech --
if [ "$MARKER_COUNT" -gt 0 ]; then
  LOW_VALUE=$(echo "$LAST_MSG" | grep '<!-- SPEAK' | while IFS= read -r ml; do
    t=$(echo "$ml" | sed -n 's/.*-->\*\*\(.*\)\*\*.*/\1/p')
    if echo "$t" | grep -iqE '(good call|great call|nice call|sounds good|will do that|got it|understood|makes sense|good idea|great idea|you.re right|of course|sure thing|absolutely|definitely|on it)'; then
      echo "LOW"
    fi
  done)
  if [ -n "$LOW_VALUE" ]; then
    cat <<'LOWVAL'
{
  "decision": "block",
  "reason": "Low-value speech detected. Don't spend speech on flattery or acknowledgment ('good call', 'will do', 'got it'). Describe WHAT you're doing instead: 'Updating the hook script' beats 'Sure, good call'. Rewrite your <!-- SPEAK -->**text** to be informative about the action."
}
LOWVAL
    exit 0
  fi
fi

# -- Speak markers sequentially in background subshell --
if [ "$MARKER_COUNT" -gt 0 ]; then
  (echo "$LAST_MSG" | grep '<!-- SPEAK' | while IFS= read -r marker_line; do
    # Extract params block if present: <!-- SPEAK(voice:X rate:N) -->
    params=$(echo "$marker_line" | sed -n 's/.*<!-- SPEAK(\([^)]*\)) -->.*/\1/p')

    # Extract the bold text after the marker: **text here**
    text=$(echo "$marker_line" | sed -n 's/.*-->\*\*\(.*\)\*\*.*/\1/p')

    if [ -z "$text" ]; then
      continue
    fi

    # Extract optional voice parameter -- if specified, update session voice and lock
    voice=$(echo "$params" | sed -n 's/.*voice:\([^ )]*\).*/\1/p')
    if [ -n "$voice" ]; then
      old_safe=$(echo "$DEFAULT_VOICE" | tr ' ()' '_--')
      rm -f "$VOICE_LOCK_DIR/$old_safe"
      new_safe=$(echo "$voice" | tr ' ()' '_--')
      echo "$SESSION_ID" > "$VOICE_LOCK_DIR/$new_safe"
      echo "$voice" > "$ENABLED_FILE"
      DEFAULT_VOICE="$voice"
      set_tab_title "$voice"
    else
      voice="$DEFAULT_VOICE"
    fi

    # Extract optional rate parameter
    rate=$(echo "$params" | sed -n 's/.*rate:\([0-9]*\).*/\1/p')
    rate="${rate:-$DEFAULT_RATE}"

    set_tab_title "$voice: $text"
    say -v "$voice" -r "$rate" "$text"
    # Touch lock file so mtime reflects last speech activity (enables LRU fallback)
    touch "$VOICE_LOCK_DIR/$(echo "$voice" | tr ' ()' '_--')" 2>/dev/null
  done) &
fi

# -- Reminder if markers missing from substantive response --
if [ "$MARKER_COUNT" -eq 0 ] && [ ${#LAST_MSG} -gt 50 ]; then
  REMIND_COOLDOWN="$SPEAK_DIR/remind-${SESSION_ID}"
  NOW=$(date +%s)
  if [ -f "$REMIND_COOLDOWN" ]; then
    LAST_REMIND=$(cat "$REMIND_COOLDOWN")
    if [ $((NOW - LAST_REMIND)) -lt 300 ]; then
      exit 0
    fi
  fi
  echo "$NOW" > "$REMIND_COOLDOWN"

  cat <<'REMINDER'
{
  "decision": "block",
  "reason": "Speech is enabled but your last response had no <!-- SPEAK -->**summary** marker. Please add one. Format: <!-- SPEAK -->**brief summary** (under 5 words). You can also use <!-- SPEAK(voice:Name rate:N) -->**text**."
}
REMINDER
fi

exit 0
