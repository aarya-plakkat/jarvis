from pinecone import Pinecone
from config import EMBEDDING_MODEL, PINECONE_API_KEY

_pc = None


def get_client():
    global _pc
    if _pc is None:
        _pc = Pinecone(api_key=PINECONE_API_KEY)
    return _pc


def embed(texts):
    pc = get_client()
    result = pc.inference.embed(
        model=EMBEDDING_MODEL,
        inputs=texts,
        parameters={"input_type": "passage"},
    )
    return [item.values for item in result.data]
