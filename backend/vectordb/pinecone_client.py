from pinecone import Pinecone
from config import PINECONE_API_KEY, PINECONE_INDEX, PINECONE_HOST

_pc = None
_index = None


def get_index():
    global _pc, _index
    if _pc is None:
        _pc = Pinecone(api_key=PINECONE_API_KEY)
    if _index is None:
        if PINECONE_HOST:
            _index = _pc.Index(PINECONE_INDEX, host=PINECONE_HOST)
        else:
            _index = _pc.Index(PINECONE_INDEX)
    return _index
