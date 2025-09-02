from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from db.models import Question, Answer
from exception.database import NotFoundedError


async def get_all_questions(session):
    query = select(Question).options(joinedload(Question.answers))
    result = await session.execute(query)
    questions = result.unique().scalars().all()
    return questions


async def get_question_by_id(id: int, session: AsyncSession) -> Question:
    query = select(Question).options(selectinload(Question.answers)).where(Question.id == id)
    result = await session.execute(query)
    question = result.scalar_one_or_none()
    if not question:
        raise NotFoundedError
    return question


async def get_answer_by_id(id: int, session: AsyncSession) -> Answer:
    query = select(Answer).where(Answer.id == id)
    result = await session.execute(query)
    answer = result.scalar_one_or_none()
    if not answer:
        raise NotFoundedError
    return answer

