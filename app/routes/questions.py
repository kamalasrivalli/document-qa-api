from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()


class Question(BaseModel):
    question: str = Field(min_length=3)


@router.post("/ask")
def ask(request: Question):
    return {"answer": f"You asked: {request.question}"}