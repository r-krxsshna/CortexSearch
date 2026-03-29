from datetime import datetime
from fastapi import APIRouter, UploadFile, File, HTTPException
from utils.logger import get_logger
from api.models.upload_response import UploadResponse
from api.services.file_service import FileService
from api.services.loader_service import LoaderService

import os
import uuid

logger = get_logger(__name__)
router = APIRouter(prefix="/v1", tags=["upload"])

@router.post("/upload", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)):

    try:

        if not file:
            raise HTTPException(status_code=400, detail="No file provided")

        logger.info(f"Recieved file: {file.filename}")

        content = await file.read()

        file_path = FileService.save_file(file.filename, content)

        doc_id = f"doc_{uuid.uuid4().hex[:8]}"

        text = LoaderService.extraxt_text(file_path)

        if not text.strip():
            raise HTTPException(status_code=400, detail="Empty document")

        logger.info(f"Text extracted for doc_id: {doc_id}")

        return UploadResponse(
            file_name=file.filename,
            file_type=os.path.splitext(file.filename)[1],
            file_size=len(content),
            message="File uploaded & processed successfully",
            doc_id=doc_id,
            uploaded_at=datetime.now()
        )

    except ValueError as e:
        logger.error(str(e))
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        logger.error(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

