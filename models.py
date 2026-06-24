from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class InterviewSession(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    candidate_name = Column(String)
    role = Column(String)

    questions = relationship("Question", back_populates="session")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(
        Integer,
        ForeignKey("sessions.id")
    )

    question_text = Column(Text)

    session = relationship(
        "InterviewSession",
        back_populates="questions"
    )

    answers = relationship(
        "Answer",
        back_populates="question"
    )


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)

    question_id = Column(
        Integer,
        ForeignKey("questions.id")
    )

    answer_text = Column(Text)

    question = relationship(
        "Question",
        back_populates="answers"
    )