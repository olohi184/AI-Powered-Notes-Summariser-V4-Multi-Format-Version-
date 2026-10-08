"""Extract readable text from supported document formats."""
from pathlib import Path


def extract_text(path: str | Path) -> str:
    path = Path(path)
    suffix = path.suffix.lower()
    if suffix == ".txt":
        text = path.read_text(encoding="utf-8")
    elif suffix == ".pdf":
        import pdfplumber
        with pdfplumber.open(path) as pdf:
            text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    elif suffix == ".docx":
        from docx import Document
        document = Document(path)
        text = "\n".join(p.text for p in document.paragraphs)
    else:
        raise ValueError("Supported formats: .txt, .pdf, .docx")
    text = text.strip()
    if not text:
        raise ValueError("No readable text found. Scanned PDFs may require OCR.")
    return text
