from ingest import chunker
from ingest.embedder import Embedder
from store.store import vector_store
embedder = Embedder()

def ingest_text(text: str, chunk_size: int = 500, overlap: int = 50):
    chunks = chunker.chunk_text(text, chunk_size, overlap)

    embeddings = embedder.embed_batch(chunks)

    for chunk, embedding in zip(chunks, embeddings):
        vector_store.add(
            chunk,
            embedding
        )

