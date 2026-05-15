# Mini-Jarvis

Mini-Jarvis demonstrates how enterprise-grade AI assistants can be built using self-hosted LLMs combined with vector databases for contextual intelligence.

## Setup

1. Create a `.env` file with:
   - `PINECONE_API_KEY`
   - `PINECONE_ENV`
   - `PINECONE_INDEX`
   - `PINECONE_HOST` (serverless host URL)
   - `OLLAMA_BASE_URL`
   - `OLLAMA_MODEL`
   - `EMBEDDING_MODEL` (default: `llama-text-embed-v2`)

2. Install dependencies:

```bash
pip install -r backend/requirements.txt
```

3. Ingest knowledge:

```bash
python scripts/ingest_data.py
```

4. Run the server:

```bash
./scripts/run_server.sh
```

Frontend files are in `frontend/`. Serve them with any static file server or place behind a reverse proxy to the Flask backend.
