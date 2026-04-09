import numpy as np
from retrieval.keyword_search import KeywordSearch
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

METADATA_PATH = BASE_DIR/ "data" / "embeddings" / "metadata.npy"

metadata = np.load(
    METADATA_PATH,
    allow_pickle=True
)

search_engine = KeywordSearch(metadata)

query = "sick leaves policy"

results = search_engine.search(query, top_k=3)

for r in results:
    print(r["content"])