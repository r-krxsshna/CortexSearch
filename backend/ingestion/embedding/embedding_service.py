import ollama
import numpy as np
from typing import List
from api.models.chunk import Chunk
from utils.logger import get_logger

logger = get_logger(__name__)


class EmbeddingService:

    MODEL_NAME = "nomic-embed-text"

    @staticmethod
    def generate_embedding(text: str) -> List[float]:
        try:
            response = ollama.embeddings(
                model=EmbeddingService.MODEL_NAME,
                prompt=text
            )

            embedding = response["embedding"]

            return embedding

        except Exception as e:
            logger.error(f"Embedding failed: {str(e)}")
            raise

    @staticmethod
    def embed_chunks(chunks: List[Chunk]):
        embeddings = []

        for chunk in chunks:
            vector = EmbeddingService.generate_embedding(
                chunk.content
            )

            embeddings.append({
                "chunk_id": chunk.chunk_id,
                "doc_id": chunk.doc_id,
                "embedding": vector,
                "content": chunk.content
            })

            logger.info(
                f"Generated embedding for chunk {chunk.chunk_index}"
            )

        return embeddings