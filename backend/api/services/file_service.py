import os
import uuid

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_EXTENSIONS = {".pdf", ".docx", ".xlsx", ".txt", ".csv"}

class FileService:

    @staticmethod
    def save_file(filename: str, content: bytes) -> str:

        file_ext = os.path.splitext(filename)[1].lower()

        if file_ext not in ALLOWED_EXTENSIONS:
            raise ValueError(f"Unsupported file type: {file_ext}")

        unique_name = f"{uuid.uuid4().hex}{file_ext}"
        file_path = os.path.join(UPLOAD_DIR, unique_name)

        with open(file_path, "wb") as f:
            f.write(content)

        return file_path