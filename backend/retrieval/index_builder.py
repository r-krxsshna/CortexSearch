import faiss
import numpy as np
import os
from pathlib import Path
from utils.logger import get_logger

logger = get_logger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent

INDEX_PATH = BASE_DIR / "data" / "embeddings" / "faiss.index"
METADATA_PATH = BASE_DIR/ "data" / "embeddings" / "metadata.npy"

class IndexBuilder:

    @staticmethod
    def build_index(embeddings):
        """
        embeddings: list of dicts
        {
            chunk_id,
            doc_id,
            embedding,
            content
        }
        """

        logger.info("Building FAISS index....")

        vectors = []
        metadata = []

        for item in embeddings:
            vectors.append(item["embedding"])

            metadata.append({
                "chunk_id": item["chunk_id"],
                "doc_id": item["doc_id"],
                "content": item["content"]
            })

        vectors_np = np.array(vectors).astype("float32")

        dimension = vectors_np.shape[1]

        index = faiss.IndexFlatL2(dimension)

        index.add(vectors_np)

        logger.info(f"Total vectors indexed : {index.ntotal}")

        os.makedirs("data/embeddings", exist_ok=True)

        faiss.write_index(index,str(INDEX_PATH))

        np.save(str(METADATA_PATH), metadata)

        logger.info(f"FAISS index saved successfully")

        return index
