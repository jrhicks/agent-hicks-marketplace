#!/usr/bin/env bash
# Plays intro audio instantly when user submits /kitt:speak-enable

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Read stdin JSON and check if prompt matches /kitt:speak-enable
INPUT=$(cat)
PROMPT=$(echo "$INPUT" | grep -o '"prompt"[[:space:]]*:[[:space:]]*"[^"]*"' | head -1 | sed 's/.*"prompt"[[:space:]]*:[[:space:]]*"//;s/"$//')

if echo "$PROMPT" | grep -q '/kitt:speak-enable'; then
  afplay "$SCRIPT_DIR/kitt-intro.mp3" &
  afplay "$SCRIPT_DIR/kitt-turbo-boost.mp3" &
fi

exit 0
