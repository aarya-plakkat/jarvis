import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
BACKEND_DIR = ROOT_DIR / "backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from vectordb.ingest import ingest_texts

DATA_PATH = ROOT_DIR / "data" / "knowledge.txt"


def chunk_text(text, max_chars=800):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        chunks.append(text[start:end].strip())
        start = end
    return [c for c in chunks if c]


def main():
    text = DATA_PATH.read_text(encoding="utf-8")
    chunks = chunk_text(text)
    count = ingest_texts(chunks)
    print(f"Ingested {count} chunks")


if __name__ == "__main__":
    main()
