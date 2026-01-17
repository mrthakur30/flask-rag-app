
from ingest.embedder import Embedder
from store.store import vector_store

embedder = Embedder()


def retrieve_context(query: str, top_k: int = 3) -> list[str]:
     embeddings = embedder.embed(query)
     relevent_text_chunks = vector_store.search(embeddings,top_k)
     return relevent_text_chunks


