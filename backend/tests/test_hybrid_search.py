from retrieval.hybrid_search import HybridSearch

search_engine = HybridSearch()

query = "How many sick leaves are allowed?"

results = search_engine.search(
    query,
    top_k=3
)

for r in results:
    print(r["content"])