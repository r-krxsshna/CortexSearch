from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UploadResponse(BaseModel):
    file_name: str
    file_type: str
    file_size: int
    message: str
    doc_id: Optional[str] = None
    uploaded_at: Optional[datetime] = None