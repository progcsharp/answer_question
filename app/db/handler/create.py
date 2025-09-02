from sqlalchemy import select
from sqlalchemy.orm import selectinload

from db.models import Question, Answer
from shemas.questions import QuestionCreate
from shemas.answer import AnswerCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException


async def create_question(question_data: QuestionCreate, session: AsyncSession) -> Question:
    question = Question(text=question_data.text)
    try:
        session.add(question)
        await session.commit()
        await session.refresh(question)

        query = select(Question).options(selectinload(Question.answers)).where(Question.id == question.id)
        result = await session.execute(query)
        question_with_answers = result.scalar_one()

    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail="Database error")
    return question_with_answers


async def create_answer(question_id: int, answer_data: AnswerCreate, session: AsyncSession) -> Answer:
    answer = Answer(question_id=question_id, text=answer_data.text, user_id=answer_data.user_id)
    try:
        session.add(answer)
        await session.commit()
        await session.refresh(answer)
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail="Database error")
    
    return answer




