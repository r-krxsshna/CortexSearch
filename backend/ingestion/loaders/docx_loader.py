from docx import Document as DocxDocument

@staticmethod
def load_docx(file_path: str) -> str:
    doc = DocxDocument(file_path)
    return "\n".join([para.text for para in doc.paragraphs])