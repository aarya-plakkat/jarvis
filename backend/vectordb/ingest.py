import uuid
from embeddings.embedder import embed
from vectordb.pinecone_client import get_index


def ingest_texts(texts, namespace="knowledge"):
    vectors = embed(texts)
    index = get_index()
    items = []
    for text, vec in zip(texts, vectors):
        items.append({"id": str(uuid.uuid4()), "values": vec, "metadata": {"text": text}})
    index.upsert(vectors=items, namespace=namespace)
    return len(items)
