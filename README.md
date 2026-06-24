# AI Candidate Screening System

## Overview
AI-powered candidate screening platform that:

- Uploads and parses resumes
- Extracts candidate skills
- Uses RAG (Retrieval Augmented Generation) with ML knowledge base
- Generates interview questions
- Evaluates candidate answers

## Tech Stack

- FastAPI
- Python
- ChromaDB
- LangChain
- HuggingFace Embeddings
- Gemini API
- SQLite

## Project Structure

backend/
│
├── app.py
├── database.py
├── models.py
├── schemas.py
├── resume_parser.py
├── rag.py
├── ingest.py
├── interview.py
├── evaluation.py
├── chroma_db/
├── Knowledge_base/
├── uploads/
└── requirements.txt

## Features

### Resume Upload
- Upload PDF resume
- Extract skills automatically

### Knowledge Base
- ML Book PDF ingestion
- ChromaDB vector storage

### Question Generation
- Context-aware interview questions
- RAG-powered retrieval

### Answer Evaluation
- Score candidate answers
- Generate feedback

## API Endpoints

### GET /

Returns system status.

### GET /health

Health check endpoint.

### POST /upload_resume

Upload resume PDF and extract skills.

### POST /generate_question

Generate interview question based on skills and knowledge base.

### POST /evaluate_answer

Evaluate candidate answer and return score.

## Run Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Start server:

```bash
python -m uvicorn app:app --reload --port 9000
```

Open Swagger:

```text
http://localhost:9000/docs
```

## Architecture

Resume Upload
↓
Skill Extraction
↓
Knowledge Base Retrieval (RAG)
↓
Question Generation
↓
Answer Evaluation