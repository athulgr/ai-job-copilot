import fitz  # PyMuPDF
from docx import Document
import io


def extract_text(file) -> str:
    """
    Extract text from uploaded resume.
    Supports: PDF, DOCX, TXT
    Always returns a string (never crashes).
    """

    file.seek(0)
    raw = file.read()
    name = getattr(file, "name", "").lower()

    try:
        if name.endswith(".pdf"):
            return _extract_pdf(raw)

        elif name.endswith(".docx"):
            return _extract_docx(raw)

        else:
            return raw.decode("utf-8", errors="ignore")

    except Exception:
        return ""


def _extract_pdf(raw: bytes) -> str:
    text_parts = []

    with fitz.open(stream=raw, filetype="pdf") as doc:
        for page in doc:
            text_parts.append(page.get_text())

    return "\n".join(text_parts)


def _extract_docx(raw: bytes) -> str:
    doc = Document(io.BytesIO(raw))

    return "\n".join(
        para.text for para in doc.paragraphs if para.text.strip()
    )