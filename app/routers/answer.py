from fastapi import APIRouter, HTTPException, Path, status, Depends, Body
from typing import List

from shemas.answer import Answer
from db.engine import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from db.handler.get import get_answer_by_id
from db.handler.delete import delete_answer
from utils.logging import log_route

router = APIRouter(prefix="/answers", tags=["answers"])

@router.get("/{id}", response_model=Answer)
@log_route("Получить ответ по ID")
async def get_answer(id: int = Path(...), db: AsyncSession = Depends(get_db)):
    answer = await get_answer_by_id(id, db)
    return answer

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
@log_route("Удалить ответ")
async def delete_answer_route(id: int = Path(...), db: AsyncSession = Depends(get_db)):
    await delete_answer(id, db)
    return

