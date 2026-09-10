from pydantic import BaseModel

class Chunk(BaseModel):
    chunk_id: str
    doc_id: str
    content: str
    chunk_index: int