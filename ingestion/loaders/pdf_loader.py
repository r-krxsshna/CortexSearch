import fitz

@staticmethod
def load_pdf(file_path: str) -> str:
    lines = []
    try:
        with fitz.open(file_path) as doc:
            for page in doc:
                lines.append(page.getText())
                return "".join(lines)
    except Exception as e:
        raise ValueError(f"Could not read PDF: {e}")
