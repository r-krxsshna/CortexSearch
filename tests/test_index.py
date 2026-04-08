from ingestion.chunking.chunker import ChunkingService
from ingestion.embedding.embedding_service import EmbeddingService
from retrieval.index_builder import IndexBuilder

text = """
Employees are entitled to 10 sick leaves annually.
Unused leaves will not carry forward.
"""

doc_id = "doc_test"

chunks = ChunkingService.chunk_text(
    doc_id,
    text
)

embeddings = EmbeddingService.embed_chunks(
    chunks
)

index = IndexBuilder.build_index(
    embeddings
)

print("Index built successfully")