from pypdf import PdfReader
import re


def extract_text_from_pdf(pdf_path):
    text = ""

    reader = PdfReader(pdf_path)

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_skills(text):
    skills_db = [
        "Python",
        "Java",
        "C++",
        "Machine Learning",
        "Deep Learning",
        "NLP",
        "SQL",
        "FastAPI",
        "Flask",
        "React",
        "TensorFlow",
        "PyTorch",
        "Data Science",
        "AWS",
        "Docker",
        "Git"
    ]

    found_skills = []

    for skill in skills_db:
        if re.search(skill, text, re.IGNORECASE):
            found_skills.append(skill)

    return found_skills