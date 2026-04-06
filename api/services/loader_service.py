import os
from ingestion.loaders.pdf_loader import load_pdf
from ingestion.loaders.docx_loader import load_docx
from ingestion.loaders.txt_loader import load_txt
from ingestion.loaders.csv_loader import load_csv
from ingestion.loaders.xlsx_loader import load_xlsx

class LoaderService:

    @staticmethod
    def extraxt_text(file_path: str) -> str:
        file_ext = os.path.splitext(file_path)[1].lower()

        if file_ext == ".pdf":
            return load_pdf(file_path)

        elif file_ext == ".docx":
            return load_docx(file_path)

        elif file_ext == ".txt":
            return load_txt(file_path)

        elif file_ext == ".csv":
            return load_csv(file_path)

        elif file_ext == ".xlsx":
            return load_xlsx(file_path)

        else:
            raise ValueError("Unsupported file type")
