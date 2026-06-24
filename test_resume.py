from resume_parser import extract_text_from_pdf
from resume_parser import extract_skills

pdf_path = "uploads/resume.pdf"

text = extract_text_from_pdf(pdf_path)

skills = extract_skills(text)

print(skills)