#!/usr/bin/env python3
# tts-daemon.py - Persistent Kokoro TTS daemon using a named pipe
#
# Loads the Kokoro model once at startup, then reads lines from a FIFO
# and speaks them immediately. Each line format: voice|speed|text
#
# Usage:
#   python3 tts-daemon.py <fifo_path>
#
# Clients write: "af_heart|1.0|Hello world\n" to the FIFO and return immediately.

import sys
import os
import signal

FIFO_PATH = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/.claude-speak-plugin/tts.pipe")
MODEL = "prince-canuma/Kokoro-82M"

def main():
    # Create FIFO if not present
    if not os.path.exists(FIFO_PATH):
        os.makedirs(os.path.dirname(FIFO_PATH), exist_ok=True)
        os.mkfifo(FIFO_PATH)

    # Load model once
    from mlx_audio.tts.generate import generate_audio

    # Warm up: pre-load model weights by generating silence-length text
    generate_audio("Ready.", model=MODEL, voice="af_heart", speed=1.0,
                   output_path="/tmp", file_prefix="kitt-warmup",
                   play=True, verbose=False)

    # Write PID file so speak.sh can check if daemon is alive
    pid_path = FIFO_PATH + ".pid"
    with open(pid_path, "w") as f:
        f.write(str(os.getpid()))

    # Clean up PID on exit
    def cleanup(signum=None, frame=None):
        try:
            os.unlink(pid_path)
        except FileNotFoundError:
            pass
        sys.exit(0)

    signal.signal(signal.SIGTERM, cleanup)
    signal.signal(signal.SIGINT, cleanup)

    # Main loop: open FIFO for reading (blocks until a writer connects)
    while True:
        try:
            with open(FIFO_PATH, "r") as fifo:
                for line in fifo:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split("|", 2)
                    if len(parts) != 3:
                        continue
                    voice, speed_str, text = parts
                    try:
                        speed = float(speed_str)
                    except ValueError:
                        speed = 1.0
                    try:
                        generate_audio(text, model=MODEL, voice=voice, speed=speed,
                                       output_path="/tmp", file_prefix="kitt-speak",
                                       play=True, verbose=False)
                    except Exception as e:
                        sys.stderr.write(f"TTS error: {e}\n")
        except Exception as e:
            sys.stderr.write(f"FIFO error: {e}\n")

if __name__ == "__main__":
    main()
