from llm.llama_client import generate_response
from embeddings.embedder import embed
from vectordb.pinecone_client import get_index
from utils.prompt_builder import build_prompt


def retrieve_context(query, top_k=3, namespace="knowledge"):
    index = get_index()
    query_vec = embed([query])[0]
    res = index.query(vector=query_vec, top_k=top_k, include_metadata=True, namespace=namespace)
    matches = res.get("matches", [])
    contexts = [m.get("metadata", {}).get("text", "") for m in matches]
    return [c for c in contexts if c]


def answer(query):
    contexts = retrieve_context(query)
    prompt = build_prompt(query, contexts)
    return generate_response(prompt)
