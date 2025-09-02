from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class AnswerCreate(BaseModel):
    text: str = Field(
        ..., 
        min_length=5, 
        max_length=2000, 
        description="Текст ответа (минимум 5, максимум 2000 символов)"
    )
    user_id: str = Field(
        ..., 
        min_length=3, 
        max_length=100, 
        description="Идентификатор пользователя (минимум 3, максимум 100 символов)"
    )


class Answer(BaseModel):
    id: int
    question_id: int
    user_id: str
    text: str
    created_at: datetime
    
    model_config = {"from_attributes": True}

