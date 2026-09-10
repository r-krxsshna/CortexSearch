from sentence_transformers import CrossEncoder
from utils.logger import get_logger

logger = get_logger(__name__)


class CrossEncoderModel:

    def __init__(self):

        logger.info(
            "Loading Cross Encoder model..."
        )

        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

        logger.info(
            "Cross Encoder loaded"
        )

    def score(self, query, documents):

        """
        query: string
        documents: list[str]
        """

        pairs = [
            (query, doc)
            for doc in documents
        ]

        scores = self.model.predict(pairs)

        return scores