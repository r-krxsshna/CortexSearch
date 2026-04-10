from retrieval.keyword_search import KeywordSearch
from retrieval.vector_search import VectorSearch
from ingestion.embedding.embedding_service import EmbeddingService
from pathlib import Path
import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent

METADATA_PATH = BASE_DIR / "data" / "embeddings" / "metadata.npy"

from utils.logger import get_logger

logger = get_logger(__name__)

class HybridSearch:

    def __init__(self):
        logger.info(f"Initializing Hybrid Search...")

        self.vector_search = VectorSearch()

        metadata = np.load(
            METADATA_PATH,
            allow_pickle=True
        )

        self.keyword_search = KeywordSearch(metadata)

        logger.info(f"Running Hybrid Search...")

    def search(self, query: str, top_k=5):

        logger.info(f"Running Hybrid Search...")

        query_embedding = (
            EmbeddingService.generate_embedding(query)
        )

        vector_results = self.vector_search.search(
            query_embedding,
            top_k=top_k
        )

        keyword_results = self.keyword_search.search(
            query,
            top_k=top_k
        )

        combined_results = self._combined_results(
            vector_results,
            keyword_results
        )

        return combined_results[:top_k]

    def _combined_results(self, vector_results, keyword_results):

        combined = {}

        for item in vector_results:
            combined[item["chunk_id"]] = item

        for item in keyword_results:
            combined[item["chunk_id"]] = item

        return list(combined.values())