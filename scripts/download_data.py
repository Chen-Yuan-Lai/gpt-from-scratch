"""Download tinyshakespeare into data/input.txt (works on Windows / Linux)."""
from pathlib import Path
from urllib.request import urlretrieve

URL = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
OUT = Path(__file__).resolve().parent.parent / "data" / "input.txt"

if __name__ == "__main__":
    OUT.parent.mkdir(exist_ok=True)
    urlretrieve(URL, OUT)
    print(f"saved {OUT} ({OUT.stat().st_size:,} bytes)")
