import faiss
import numpy as np
from pathlib import Path
from retrieval.index_builder import METADATA_PATH
from utils.logger import get_logger

logger = get_logger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent

INDEX_PATH = BASE_DIR / "data" / "embeddings" / "faiss.index"
METADATA_PATH = BASE_DIR / "data" / "embeddings" / "metadata.npy"

class VectorSearch:

    def __init__(self):
        logger.info("Loading FAISS index...")

        self.index = faiss.read_index(str(INDEX_PATH))
        self.metadata = np.load(
            str(METADATA_PATH),
            allow_pickle=True,
        )

        logger.info(
            f"Loaded index with {self.index.ntotal} vectors"
        )

    def search(self, query_embedding, top_k=5):

        query_vector = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(
            query_vector,
            top_k
        )

        results = []

        for idx in indices[0]:
            if idx < len(self.metadata):
                results.append(
                    self.metadata[idx]
                )

        logger.info(
            f"Retrieved {len(results)} results"
        )

        return results