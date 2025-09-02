from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import logging

from routers.answer import router as answer_router
from routers.questions import router as questions_router

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

app = FastAPI(debug=False)

# Добавляем CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check эндпоинт
@app.get("/health")
async def health_check():
    """Health check эндпоинт"""
    return {"status": "healthy", "service": "question-answer-api"}

app.include_router(router=answer_router)
app.include_router(router=questions_router)

