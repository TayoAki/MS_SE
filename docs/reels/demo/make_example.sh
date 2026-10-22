#!/usr/bin/env bash
# make_example.sh spec.json OUT — a voiced, faceless example cut in the house style (build_parker.py):
# the AI stand-in voice, the composition timed to it, the renderer's checks, a draft render, the voice muxed in.
# Assets the spec names (assets/...) must already be in OUT. Result: OUT/<name>.mp4
set -euo pipefail
SPEC=$1; OUT=$2
HERE=$(cd "$(dirname "$0")" && pwd)
PY=~/.cache/persa-shorts/py/bin/python
NAME=$(python3 -I -c "import json,sys;print(json.load(open(sys.argv[1]))['name'])" "$SPEC")
mkdir -p "$OUT"
if [ ! -f ~/.cache/hyperframes/tts/models/kokoro-v1.0.onnx ]; then   # first run: the renderer downloads the voice model
  HYPERFRAMES_PYTHON="$PY" npx --yes hyperframes tts "ready" -o "$OUT/.voice-check.wav" >/dev/null && rm -f "$OUT/.voice-check.wav"
fi
"$PY" -I "$HERE/voice.py" "$SPEC" --out "$OUT" | tail -1
python3 -I "$HERE/build_parker.py" "$SPEC" --out "$OUT"
cd "$OUT"
npx --yes hyperframes check . 2>&1 | grep -E "error\(s\)|✗" | head -5
npx --yes hyperframes render . -o silent.mp4 -q draft 2>&1 | grep -E "rendered in" || true
ffmpeg -loglevel error -y -i silent.mp4 -i voice.wav -c:v copy -c:a aac -b:a 160k -shortest "$NAME.mp4"
echo "$OUT/$NAME.mp4"
