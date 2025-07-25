import re
from PyPDF2 import PdfReader
import docx

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    return ' '.join([page.extract_text() for page in reader.pages if page.extract_text()])

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return ' '.join([para.text for para in doc.paragraphs])
def clean_text(text):
    return re.sub(r'[^\w\s]', '', text.lower())
def calculate_score(resume_text, job_keywords):
    resume_text = clean_text(resume_text)
    words = resume_text.split()
    score = 0
    matched_keywords = []

    for keyword in job_keywords:
        if keyword.lower() in words:
            score += 1
            matched_keywords.append(keyword)

    return {
        "score": score,
        "matched": matched_keywords,
        "total": len(job_keywords),
        "percentage": round((score / len(job_keywords)) * 100, 2) if job_keywords else 0
    }
