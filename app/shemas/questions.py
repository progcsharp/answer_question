from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

from shemas.answer import Answer


class Question(BaseModel):
    id: int
    text: str
    answers: List[Answer] = []
    created_at: datetime

    model_config = {"from_attributes": True}


class QuestionCreate(BaseModel):
    text: str = Field(
        ..., 
        min_length=10, 
        max_length=1000, 
        description="Текст вопроса (минимум 10, максимум 1000 символов)"
    )
    