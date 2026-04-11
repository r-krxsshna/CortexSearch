from ranking.cross_encoder import CrossEncoderModel
from utils.logger import get_logger

logger = get_logger(__name__)


class Reranker:

    def __init__(self):

        self.cross_encoder = CrossEncoderModel()

    def rerank(
        self,
        query,
        results,
        top_k=5
    ):

        logger.info("Running reranking...")

        documents = [
            item["content"]
            for item in results
        ]

        scores = self.cross_encoder.score(
            query,
            documents
        )

        # Attach scores
        scored_results = []

        for item, score in zip(
            results,
            scores
        ):

            item["score"] = float(score)

            scored_results.append(item)

        # Sort by score
        scored_results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        logger.info(
            f"Top {top_k} results selected"
        )

        return scored_results[:top_k]