from rank_bm25 import BM25Okapi
from utils.logger import get_logger
import numpy as np

logger = get_logger(__name__)

class KeywordSearch:

    def __init__(self, metadata):
        """
                metadata: list of dicts
                [
                    {
                        chunk_id,
                        doc_id,
                        content
                    }
                ]
                """

        logger.info("Initializing BM25...")

        self.metadata = metadata

        self.corpus = [
            item["content"].lower().split()
            for item in metadata
        ]

        self.bm25 = BM25Okapi(self.corpus)

        logger.info("BM25 initialized")

    def search(self, query: str, top_k=5):

        logger.info("Running BM25 search...")

        query_tokens = query.lower().split()

        scores = self.bm25.get_scores(query_tokens)

        top_indices = np.argsort(scores)[::-1][:top_k]

        results = []

        for idx in top_indices:
            results.append(self.metadata[idx])

        logger.info(f"Retrieved {len(results)} keyword results")

        return results