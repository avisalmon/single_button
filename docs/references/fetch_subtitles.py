"""
Fetch auto-generated subtitles for every video in the single_button playlist.
Saves each as docs/references/NN title.en.vtt
Skips already-downloaded files.
Run from project root: python docs/references/fetch_subtitles.py
"""
import subprocess, time, os, re

PROXY = "http://proxy-mu.intel.com:912"
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
DONE_FILE = os.path.join(OUT_DIR, ".done.txt")

VIDEOS = [
    ("01", "Jap-4eeCaNw", "בניית מיקרו ארקייד פלאפי"),
    ("02", "zH8_QF0gqBY",  "001 intro to course"),
    ("03", "-p3vHewAgE8",  "002 setup"),
    ("04", "VOU1evNbYDQ",  "010 lines"),
    ("05", "D2WSFFeNTw4",  "020 intro"),
    ("06", "s_1dilEqFfM",  "021 move the line"),
    ("07", "RELDbdn2RzU",  "022 performance"),
    ("08", "Z9-u8Ub67hw",  "030 more than lines"),
    ("09", "AwkKSgIKmt0",  "040 text"),
    ("10", "lveNiPN7LF0",  "050 read a button"),
    ("11", "tVNSqr0vF4g",  "070 move around"),
    ("12", "zeDq5jQDPiw",  "090 pong 1"),
    ("13", "eEXuKzupk_w",  "100 pong part 2"),
    ("14", "29LO7Znncrg",  "110 functions"),
    ("15", "B8l2I_6iC90",  "111 pong collision"),
]

def already_done(idx):
    pattern = os.path.join(OUT_DIR, f"{idx} *.vtt")
    import glob
    return bool(glob.glob(pattern))

def fetch_one(idx, vid_id, title, retries=4, delay=30):
    url = f"https://www.youtube.com/watch?v={vid_id}"
    out_template = os.path.join(OUT_DIR, f"{idx} {title}.%(ext)s")
    cmd = [
        "yt-dlp",
        "--write-auto-sub", "--write-sub",
        "--sub-lang", "en",
        "--sub-format", "vtt",
        "--skip-download",
        "--no-warnings",
        "--proxy", PROXY,
        "-o", out_template,
        url,
    ]
    for attempt in range(1, retries + 1):
        print(f"  [{idx}] {title} — attempt {attempt}/{retries}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout + result.stderr
        if "429" in output:
            print(f"  429 rate limit. Waiting {delay}s...")
            time.sleep(delay)
            delay = min(delay * 2, 120)
        elif "no subtitles" in output.lower() or "There are no subtitles" in output:
            print(f"  No subtitles available for this video.")
            return "NO_SUBS"
        else:
            # Check if file was written
            import glob
            files = glob.glob(os.path.join(OUT_DIR, f"{idx} *.vtt"))
            if files:
                print(f"  OK: {os.path.basename(files[0])}")
                return "OK"
            else:
                print(f"  Done but no file found (may already exist or no subs).")
                return "OK"
    return "FAILED"

def main():
    print(f"Output dir: {OUT_DIR}")
    os.makedirs(OUT_DIR, exist_ok=True)
    
    for idx, vid_id, title in VIDEOS:
        if already_done(idx):
            print(f"  [{idx}] SKIP (already downloaded)")
            continue
        status = fetch_one(idx, vid_id, title)
        if status == "OK":
            # Wait between successful downloads to avoid rate limiting
            time.sleep(8)
        elif status == "FAILED":
            print(f"  [{idx}] FAILED after all retries")
            time.sleep(15)

    print("\nDone. Files in:", OUT_DIR)
    import glob
    for f in sorted(glob.glob(os.path.join(OUT_DIR, "*.vtt"))):
        print(" ", os.path.basename(f))

if __name__ == "__main__":
    main()
