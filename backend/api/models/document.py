from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Document(BaseModel):
    doc_id: str
    file_name: str
    file_type: str
    content: str
    created_at: Optional[datetime] = None