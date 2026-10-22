#!/bin/bash
# Cloud sessions start in a fresh container: link the content machine back into place and
# get the Persa Shorts editor's free tools ready. Safe to run more than once.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

P="$CLAUDE_PROJECT_DIR"
EDITOR="$P/.claude/skills/nextphase-persa-shorts"

# The skills and the workspace live in this repo; their docs use ~/.claude/skills/... and ~/content-machine.
# Link only where nothing real is in the way.
link() { if [ -L "$2" ] || [ ! -e "$2" ]; then ln -sfn "$1" "$2"; fi; }
mkdir -p "$HOME/.claude/skills"
link "$P/.claude/skills/content-machine" "$HOME/.claude/skills/content-machine"
link "$EDITOR" "$HOME/.claude/skills/nextphase-persa-shorts"
link "$P/content-machine" "$HOME/content-machine"
chmod +x "$EDITOR/scripts/"*

# The editor's private Python env (pillow, numpy, playwright for page shots). Playwright is pinned to the
# version of the Chromium already in the image so nothing has to download a browser.
PRIV="$HOME/.cache/persa-shorts/py"
if ! "$PRIV/bin/python" -c 'import PIL, numpy, playwright' 2>/dev/null; then
  PW="$(node -p "require('$(npm root -g)/playwright/package.json').version" 2>/dev/null || true)"
  python3 -m venv "$PRIV"
  "$PRIV/bin/python" -m pip install -q --disable-pip-version-check pillow numpy ${PW:+"playwright~=${PW%.*}.0"}
fi

# yt-dlp for the niche-scripts skill's YouTube research, in its own env, put on PATH for the session.
NS="$HOME/.cache/niche-scripts/venv"
if [ ! -x "$NS/bin/yt-dlp" ]; then
  python3 -m venv "$NS" && "$NS/bin/python" -m pip install -q --disable-pip-version-check yt-dlp || true
fi
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo "export PATH=\"$NS/bin:\$PATH\"" >> "$CLAUDE_ENV_FILE"
fi

# The free local AI stand-in voice for example cuts (docs/reels/demo/voice.py): Kokoro in the private env; the
# renderer's own `hyperframes tts` downloads the model on first use and finds the packages through HYPERFRAMES_PYTHON.
if ! "$PRIV/bin/python" -c 'import kokoro_onnx, soundfile' 2>/dev/null; then
  "$PRIV/bin/python" -m pip install -q --disable-pip-version-check kokoro-onnx soundfile || true
fi
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo "export HYPERFRAMES_PYTHON=\"$PRIV/bin/python\"" >> "$CLAUDE_ENV_FILE"
fi

# The renderer (HyperFrames via npx) and its headless Chrome, the sound palette; prints "All set" when ready.
if bash "$EDITOR/scripts/doctor.sh" --fix >/dev/null 2>&1; then
  echo "content-machine: skills linked, workspace at ~/content-machine, editor tools All set"
else
  echo "content-machine: skills linked, workspace at ~/content-machine; editor tools NOT ready — run: bash ~/.claude/skills/nextphase-persa-shorts/scripts/doctor.sh --fix"
fi
