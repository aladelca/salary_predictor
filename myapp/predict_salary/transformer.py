import docx
import pandas as pd
import re
import PyPDF2


def get_pdf(path):
    with open(path, 'rb') as file:
        lector = PyPDF2.PdfReader(file)
        final_text = []
        for page_num in range(len(lector.pages)):
            page = lector.pages[page_num]
            text = page.extract_text()
            final_text.append(text)
        return " ".join(final_text)


def get_text_from_document(path):
    doc = docx.Document(path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)

    return " ".join(full_text)