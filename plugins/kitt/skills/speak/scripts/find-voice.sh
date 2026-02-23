#!/bin/bash
# find-voice.sh - Check prerequisites and find an available voice
#
# Output (single line):
#   OK:<voice>        prerequisites pass, use this voice
#   ERROR:<message>   prerequisites failed
#
# Exit codes: 0 always (output encodes success/failure)

SPEAK_DIR="$HOME/.claude-speak-plugin"
mkdir -p "$SPEAK_DIR"
VOICE_LOCK_DIR="$SPEAK_DIR/voices"
VOICES=("Daniel" "Samantha" "Karen" "Moira" "Rishi")

# -- Prerequisites --
if ! command -v say >/dev/null 2>&1; then
  echo "ERROR:Speech requires macOS with the say command. Not available on this system."
  exit 0
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR:Speech requires python3 on PATH."
  exit 0
fi

# -- Find unclaimed voice --
mkdir -p "$VOICE_LOCK_DIR"

for v in "${VOICES[@]}"; do
  safe_name=$(echo "$v" | tr ' ()' '_--')
  if [ ! -f "$VOICE_LOCK_DIR/$safe_name" ]; then
    echo "OK:$v"
    exit 0
  fi
done

# -- All claimed: steal least recently used (oldest mtime) --
lru=$(ls -tr "$VOICE_LOCK_DIR" | head -1)
if [ -n "$lru" ]; then
  # Map safe filename back to voice name
  for v in "${VOICES[@]}"; do
    safe_name=$(echo "$v" | tr ' ()' '_--')
    if [ "$safe_name" = "$lru" ]; then
      echo "OK:$v"
      exit 0
    fi
  done
  # Lock file doesn't match any known voice (stale from old pool), use first voice
  echo "OK:${VOICES[0]}"
else
  echo "OK:${VOICES[0]}"
fi
