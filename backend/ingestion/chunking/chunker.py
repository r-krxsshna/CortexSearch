import uuid
from typing import List
from api.models.chunk import Chunk

from utils.logger import get_logger

logger = get_logger(__name__)

class ChunkingService:

    @staticmethod
    def chunk_text(doc_id: str, text: str, chunk_size: int = 500, overlap: int = 100) -> List[Chunk]:
        words = text.split()
        chunks = []

        start = 0
        chunk_index = 0

        while start < len(words):
             end = start + chunk_size

             chunk_words = words[start:end]
             chunk_text = " ".join(chunk_words)

             chunk = Chunk(
                 chunk_id = f"chunk_{uuid.uuid4().hex[:8]}",
                 doc_id = doc_id,
                 content = chunk_text,
                 chunk_index = chunk_index,
             )

             chunks.append(chunk)

             logger.info(f"Created chunk {chunk_index} for doc {doc_id}")

             start += chunk_size - overlap
             chunk_index += 1

        return chunks