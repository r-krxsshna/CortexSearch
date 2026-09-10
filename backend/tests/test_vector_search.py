from ingestion.embedding.embedding_service import EmbeddingService
from retrieval.vector_search import VectorSearch

query = "How many sick leaves are allowed?"

query_embedding = EmbeddingService.generate_embedding(
    query
)

search_engine = VectorSearch()

results = search_engine.search(
    query_embedding,
    top_k=3
)

for r in results:
    print(r["content"])

