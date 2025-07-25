# utils/pdf_utils.py

import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Extract full text from a PDF file using PyMuPDF.
    Returns text page by page, separated by double newlines.
    """
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text() + "\n\n"
    except Exception as e:
        print(f"❌ Error reading {pdf_path}: {e}")
    return text