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





## Getting Started

1. Move into the application directory:

```bash
cd jarvis
```

2. Create a `.env` file with the required configuration:

```env
PINECONE_API_KEY=
PINECONE_ENV=
PINECONE_INDEX=
PINECONE_HOST=
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3
EMBEDDING_MODEL=llama-text-embed-v2
```

3. Install backend dependencies:

```bash
pip install -r backend/requirements.txt
```

4. Ingest the knowledge base:

```bash
python scripts/ingest_data.py
```

5. Start the server:

```bash
./scripts/run_server.sh
```

6. Open the app in your browser:

```text
http://localhost:5000
```

## Repository Layout

```text
jarvis/
├── README.md
└── mini-jarvis-ai/
    ├── backend/
    │   ├── app.py
    │   ├── config.py
    │   ├── embeddings/
    │   ├── llm/
    │   ├── routes/
    │   ├── services/
    │   ├── utils/
    │   └── vectordb/
    ├── data/
    │   └── knowledge.txt
    ├── frontend/
    │   ├── index.html
    │   ├── script.js
    │   └── style.css
    └── scripts/
        ├── ingest_data.py
        └── run_server.sh
```
