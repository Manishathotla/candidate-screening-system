from fastapi import FastAPI, UploadFile, File
import shutil
import os

from database import engine
from models import Base

from resume_parser import extract_text_from_pdf, extract_skills
from interview import generate_question
from evaluation import evaluate_answer
from schemas import AnswerRequest


app = FastAPI(
    title="AI Candidate Screening System"
)

Base.metadata.create_all(bind=engine)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def root():
    return {
        "message": "AI Candidate Screening System Running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    
    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    text = extract_text_from_pdf(file_path)
    skills = extract_skills(text)

    return {
        "filename": file.filename,
        "skills": skills
    }


@app.post("/generate_question")
def create_question(data: dict):

    role = data.get("role")
    skills = data.get("skills", [])

    question = generate_question(
        role,
        skills
    )

    return {
        "question": question
    }

@app.post("/evaluate_answer")
def evaluate(data: dict):

    question = data.get("question")
    answer = data.get("answer")

    result = evaluate_answer(question, answer)

    print("RESULT =", result)

    return result