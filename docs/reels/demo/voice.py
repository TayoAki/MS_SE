#!/usr/bin/env python3
"""voice.py — a stand-in voice for an example cut: every spoken line through a free local AI voice (Kokoro-82M).

    ~/.cache/persa-shorts/py/bin/python -I docs/reels/demo/voice.py spec.json --out DIR [--voice af_heart] [--speed 1.05]

Writes DIR/voice/NN.wav per line, DIR/voice.wav (the lines joined with the builder's 0.25 s breath) and
DIR/voice.json (each line's length), which build_parker.py times the beats and captions from. A line can carry
"tts": "how to say it" when the spelling reads badly aloud ("three one one" for 311). The model is the one
`npx hyperframes tts` downloads (~/.cache/hyperframes/tts); the voice is a stand-in until the creator records.
"""
import argparse, json, os, pathlib, sys

GAP = 0.25
CACHE = pathlib.Path.home() / ".cache/hyperframes/tts"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec"); ap.add_argument("--out", required=True)
    ap.add_argument("--voice", default="af_heart"); ap.add_argument("--speed", type=float, default=1.05)
    a = ap.parse_args()
    import numpy as np, soundfile as sf
    from kokoro_onnx import Kokoro
    model, voices = CACHE / "models/kokoro-v1.0.onnx", CACHE / "voices/voices-v1.0.bin"
    if not model.exists():
        sys.exit("voice.py: run `npx --yes hyperframes tts \"hello\" -o /tmp/x.wav` once to download the voice model")
    k = Kokoro(str(model), str(voices))
    spec = json.loads(pathlib.Path(a.spec).read_text())
    out = pathlib.Path(os.path.expanduser(a.out)); (out / "voice").mkdir(parents=True, exist_ok=True)
    rows, parts, sr = [], [], 24000
    for i, ln in enumerate(spec["lines"]):
        text = ln.get("tts", ln["say"])
        samples, sr = k.create(text, voice=spec.get("voice", a.voice), speed=spec.get("speed", a.speed), lang="en-us")
        samples = np.asarray(samples, dtype=np.float32)
        nz = np.nonzero(np.abs(samples) > 0.003)[0]              # trim the model's leading/trailing silence
        if len(nz):
            samples = samples[max(0, nz[0] - int(0.03 * sr)): nz[-1] + int(0.08 * sr)]
        sf.write(out / "voice" / f"{i:02d}.wav", samples, sr)
        rows.append(round(len(samples) / sr, 3))
        parts += [samples, np.zeros(int(GAP * sr), dtype=np.float32)]
        print(f"{i + 1:2d} {rows[-1]:5.2f}s  {text[:70]}")
    sf.write(out / "voice.wav", np.concatenate(parts[:-1]), sr)
    (out / "voice.json").write_text(json.dumps({"durations": rows, "gap": GAP, "voice": spec.get("voice", a.voice)}, indent=1))
    print(f"total {sum(rows) + GAP * (len(rows) - 1):.1f}s -> {out}/voice.wav")


if __name__ == "__main__":
    main()
