# Jarvis

A lightweight retrieval-augmented AI assistant that combines a browser chat interface, a Flask backend, Pinecone-based semantic retrieval, and an Ollama-powered language model into one modular system.

## Overview

Jarvis is a compact end-to-end assistant project designed to demonstrate how a conversational AI system can be built from separable, production-style components instead of a single monolithic script. It accepts a user message from the browser, retrieves relevant knowledge from a vector database, builds a grounded prompt from that context, and sends the prompt to a self-hosted language model to generate the final response.

The project exists to solve a core limitation of plain chatbot implementations: a language model can answer fluently, but without retrieval it may not have access to project-specific or domain-specific knowledge. Jarvis adds a retrieval layer so responses can be grounded in curated source material stored outside the model itself.

This repository currently contains the `mini-jarvis-ai` implementation, which keeps the architecture intentionally small while preserving the same major building blocks used in larger RAG systems: ingestion, embeddings, vector search, prompt construction, language-model generation, API routing, and a client interface.

## Key Features

- Browser-based chat interface for interactive conversations
- Flask API layer with a dedicated `/api/chat` endpoint
- Retrieval-augmented generation pipeline for context-aware answers
- Pinecone vector database integration for semantic search
- Pinecone Inference embeddings for both ingestion and query retrieval
- Ollama-compatible local language model generation
- Scripted knowledge ingestion from plain-text source material
- Environment-driven configuration for model and database settings
- Modular backend structure that separates routing, retrieval, prompting, and generation
- Lightweight frontend that can be served directly by the Flask app

## System Architecture

The assistant consists of the following components:

1. **Frontend Interface** – Accepts user messages in the browser and renders assistant replies.
2. **API Layer** – Receives chat requests through Flask and validates incoming payloads.
3. **RAG Orchestration** – Coordinates retrieval, prompt construction, and response generation.
4. **Embedding Module** – Converts user queries and knowledge chunks into vector representations.
5. **Vector Database Layer** – Stores embedded knowledge and returns the most relevant context matches.
6. **Prompt Builder** – Combines retrieved context with the user question into a grounded model prompt.
7. **LLM Client** – Sends the final prompt to an Ollama-compatible model endpoint and returns generated text.
8. **Ingestion Pipeline** – Chunks local knowledge files, embeds them, and uploads them into Pinecone.

```text
User Message
    ↓
Frontend Interface
    ↓
Flask API Layer
    ↓
RAG Service
    ↓
Query Embedding
    ↓
Pinecone Vector Search
    ↓
Retrieved Context
    ↓
Prompt Builder
    ↓
Ollama LLM
    ↓
Assistant Response
    ↓
Frontend Interface
```

Knowledge ingestion runs as a companion flow:

```text
knowledge.txt
    ↓
Chunking Script
    ↓
Embedding Module
    ↓
Pinecone Vector Database
```

## Project Modules

### `mini-jarvis-ai/frontend/`

The browser client for the assistant.

- **`index.html`** – Defines the chat page structure, title, message area, and input form.
- **`script.js`** – Sends user messages to `/api/chat`, receives responses, and updates the conversation view.
- **`style.css`** – Provides the visual styling for the interface, message bubbles, layout, and buttons.

### `mini-jarvis-ai/backend/app.py`

The Flask application entry point. It creates the app, registers the chat blueprint, serves the frontend, and starts the development server.

### `mini-jarvis-ai/backend/config.py`

The configuration module. It loads environment variables for Pinecone access, Ollama connectivity, and the embedding model used throughout the system.

### `mini-jarvis-ai/backend/routes/chat_routes.py`

The request-routing layer. It exposes the `/api/chat` endpoint, validates the incoming message, and returns either a generated response or a client error.

### `mini-jarvis-ai/backend/services/rag_service.py`

The core orchestration layer. It embeds the user query, retrieves the most relevant stored context, builds the final prompt, and delegates generation to the language model client.

### `mini-jarvis-ai/backend/embeddings/embedder.py`

The embedding module. It connects to Pinecone Inference and transforms raw text into vectors used for both document ingestion and similarity search.

### `mini-jarvis-ai/backend/vectordb/pinecone_client.py`

The Pinecone connection layer. It lazily creates and reuses the Pinecone client and index handle, supporting either host-based or index-name-based access.

### `mini-jarvis-ai/backend/vectordb/ingest.py`

The ingestion helper. It embeds text chunks, assigns UUIDs, attaches source text as metadata, and upserts the resulting vectors into the `knowledge` namespace.

### `mini-jarvis-ai/backend/utils/prompt_builder.py`

The prompt-construction utility. It merges retrieved context with the user question into the final instruction sent to the model.

### `mini-jarvis-ai/backend/llm/llama_client.py`

The language-model client. It sends prompts to the configured Ollama `/api/generate` endpoint and extracts the generated response text.

### `mini-jarvis-ai/scripts/`

Operational scripts for preparing and running the project.

- **`ingest_data.py`** – Reads `data/knowledge.txt`, splits it into chunks, and stores them in Pinecone.
- **`run_server.sh`** – Sets the backend import path and launches the Flask server.

### `mini-jarvis-ai/data/knowledge.txt`

The seed knowledge source used by the ingestion pipeline. Its contents become the retrieval corpus available to the assistant.

## Tech Stack

- Python
- Flask
- Pinecone vector database
- Pinecone Inference embeddings
- Ollama-compatible LLM serving
- HTML5
- CSS3
- JavaScript
- `requests`
- `python-dotenv`

## Getting Started

1. Move into the application directory:

```bash
cd mini-jarvis-ai
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
