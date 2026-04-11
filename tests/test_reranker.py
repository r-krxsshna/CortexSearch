from retrieval.hybrid_search import HybridSearch
from ranking.reranker import Reranker

query = "How many sick leaves are allowed?"

search_engine = HybridSearch()

initial_results = search_engine.search(
    query,
    top_k=10
)

reranker = Reranker()

final_results = reranker.rerank(
    query,
    initial_results,
    top_k=3
)

for r in final_results:
    print(r["content"])