from pydantic import BaseModel


class StartInterviewRequest(BaseModel):
    candidate_name: str
    role: str


class AnswerRequest(BaseModel):
    session_id: int
    question_id: int
    answer: str


class InterviewResponse(BaseModel):
    session_id: int
    question: str

class AnswerRequest(BaseModel):
    question: str
    answer: str