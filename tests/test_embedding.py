from ollama import embeddings

from ingestion.chunking.chunker import ChunkingService
from ingestion.embedding.embedding_service import EmbeddingService

text = """
Employees are entitled to 10 sick leaves annually.
Unused leaves will not carry forward.
"""

doc_id = "doc_test"

chunks = ChunkingService.chunk_text(
    doc_id=doc_id,
    text=text,
)

embeddings = EmbeddingService.embed_chunks(chunks)

print(len(embeddings))
print(len(embeddings[0]["embedding"]))