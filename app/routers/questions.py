from typing import List

from fastapi import APIRouter, Path, status, Depends, Body
from datetime import datetime

from shemas.questions import Question, QuestionCreate
from shemas.answer import AnswerCreate, Answer
from db.engine import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from db.handler.get import get_question_by_id, get_all_questions
from db.handler.delete import delete_question
from db.handler.create import create_question, create_answer
from utils.logging import log_route

router = APIRouter(prefix="/questions", tags=["questions"])


@router.get("/", response_model=List[Question])
@log_route("Получить все вопросы")
async def get_all_questions_route(db: AsyncSession = Depends(get_db)):
    """Получить все вопросы"""
    questions = await get_all_questions(db)
    return questions


@router.get("/{id}", response_model=Question)
@log_route("Получить вопрос по ID")
async def get_question_route(id: int = Path(..., gt=0, description="ID вопроса"), db: AsyncSession = Depends(get_db)):
    """Получить вопрос по ID"""
    question = await get_question_by_id(id, db)
    return question


@router.post("/", response_model=Question, status_code=status.HTTP_201_CREATED)
@log_route("Создать новый вопрос")
async def create_question_route(question: QuestionCreate, db: AsyncSession = Depends(get_db)):
    """Создать новый вопрос"""
    question = await create_question(question, db)
    return question


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
@log_route("Удалить вопрос")
async def delete_question_route(id: int = Path(..., gt=0, description="ID вопроса"), db: AsyncSession = Depends(get_db)):
    """Удалить вопрос"""
    await delete_question(id, db)
    return


@router.post("/{id}/answers/", response_model=Answer, status_code=status.HTTP_201_CREATED)
@log_route("Добавить ответ к вопросу")
async def add_answer_route(id: int = Path(..., gt=0, description="ID вопроса"), db: AsyncSession = Depends(get_db), answer: AnswerCreate = Body(...)):

    await get_question_by_id(id, db)
    
    answer = await create_answer(id, answer, db)
    return answer
