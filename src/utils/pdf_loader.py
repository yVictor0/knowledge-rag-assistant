import pdfplumber
import os
from pathlib import Path


def extract_text_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {pdf_path}")

    pages = []

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()

                if text and text.strip():
                    pages.append({
                        "page": i + 1,
                        "text": text.strip()
                    })

    except Exception as e:
        raise RuntimeError(f"Erro ao ler o PDF: {e}")

    return pages


def chunk_text(pages, chunk_size=500, overlap=50):
    if overlap >= chunk_size:
        raise ValueError("overlap deve ser menor que chunk_size")

    chunks = []

    for page in pages:
        text = page["text"]
        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]

            if chunk.strip():  # evita chunk vazio
                chunks.append({
                    "id": f"p{page['page']}_c{start}",
                    "text": chunk,
                    "page": page["page"]
                })

            start += chunk_size - overlap

    return chunks
