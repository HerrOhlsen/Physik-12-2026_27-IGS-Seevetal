"""Generate one mp3 per audio script with Gemini TTS, trim silence, normalize, then transcribe back for checking.
Usage: python tts.py <ModulId> [s1 s2 ...]    reads audio-src/<ModulId>/sN.txt, writes src/<ModulId>/sN.mp3
Needs GEMINI_API_KEY, ffmpeg on PATH, requests in the venv."""
import os, sys, subprocess, pathlib, time
import requests, base64

ROOT = pathlib.Path(__file__).resolve().parent.parent
mod = sys.argv[1]; names = sys.argv[2:] or sorted(p.stem for p in (ROOT / "audio-src" / mod).glob("s*.txt"))
KEY = os.environ["GEMINI_API_KEY"].strip().strip('"\'').strip()  # the env var may carry a stray quote/newline
VOICE = "Charon"
MODELS = ["gemini-3.8-flash-tts", "gemini-2.5-flash-preview-tts"]
URL = "https://generativelanguage.googleapis.com/v1beta/models/{}:generateContent"

def tts(text):
    last = None
    for model in MODELS:
        for attempt in range(3):
            r = requests.post(URL.format(model), headers={"x-goog-api-key": KEY}, timeout=180, json={
                "contents": [{"parts": [{"text": text}]}],
                "generationConfig": {"responseModalities": ["AUDIO"], "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": VOICE}}}}})
            if r.status_code == 200:
                part = r.json()["candidates"][0]["content"]["parts"][0]["inlineData"]
                return model, part["mimeType"], base64.b64decode(part["data"])
            last = RuntimeError(f"{model} {r.status_code} {r.text[:150]}"); print("  retry", last); time.sleep(4)
    raise last

def transcribe(mp3_bytes):
    r = requests.post(URL.format("gemini-3.8-flash"), headers={"x-goog-api-key": KEY}, timeout=180, json={
        "contents": [{"parts": [{"inlineData": {"mimeType": "audio/mpeg", "data": base64.b64encode(mp3_bytes).decode()}},
                                {"text": "Transkribiere das Audio wortgetreu auf Deutsch. Nur der Text."}]}]})
    r.raise_for_status(); return r.json()["candidates"][0]["content"]["parts"][0]["text"]

for n in names:
    text = (ROOT / "audio-src" / mod / f"{n}.txt").read_text(encoding="utf-8")
    model, mime, data = tts(text)
    tmp = ROOT / "audio-src" / mod / f"{n}.raw"
    tmp.write_bytes(data)
    out = ROOT / "src" / mod / f"{n}.mp3"
    if "wav" in mime or data[:4] == b"RIFF":
        inp = ["-i", str(tmp)]
    else:  # raw PCM 24 kHz mono 16 bit
        inp = ["-f", "s16le", "-ar", "24000", "-ac", "1", "-i", str(tmp)]
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inp,
                    "-af", "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.2,areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.3,areverse,loudnorm=I=-19:TP=-2",
                    "-ac", "1", "-ar", "24000", "-b:a", "48k", str(out)], check=True)
    tmp.unlink() if out.exists() and out.stat().st_size > 0 else None
    dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(out)], capture_output=True, text=True).stdout.strip()
    # transcribe back for a check
    try:
        (ROOT / "audio-src" / mod / f"{n}.transkript.txt").write_text(transcribe(out.read_bytes()), encoding="utf-8")
    except Exception as e:
        print("  transkript fehlgeschlagen", str(e)[:100])
    print(n, model, mime, f"{float(dur):.0f}s", out.stat().st_size // 1024, "KB")
