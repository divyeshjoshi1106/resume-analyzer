import os
from pdfminer.high_level import extract_text as pdfminer_extract_text
from docx import Document


def extract_text_from_pdf(file_path: str) -> str:
    text = pdfminer_extract_text(file_path)
    return text


def extract_text_from_docx(file_path: str) -> str:
    document = Document(file_path)

    fullText = []
    for para in document.paragraphs:
        fullText.append(para.text)
    return "\n".join(fullText)
    pass


def extract_text(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist")

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type")


# text = extract_text("mypdf.pdf")
# print(text)
