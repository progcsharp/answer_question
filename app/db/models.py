from datetime import datetime, timezone

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, \
    MetaData, Text, DateTime
# Pay attentions if you use another DB like Oracle, MySQL etc.
# This types implement for specific dialect

from .utils import conventions


meta = MetaData(naming_convention=conventions)
Base = declarative_base(metadata=meta)


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text, nullable=False, comment="текст вопроса")
    created_at = Column(DateTime, default=lambda: datetime.now(), nullable=False)

    answers = relationship('Answer', back_populates='question', cascade="all, delete-orphan")


class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey('questions.id'), nullable=False)
    text = Column(Text, nullable=False, comment="текст ответа")
    created_at = Column(DateTime, default=lambda: datetime.now(), nullable=False)
    user_id = Column(Text, nullable=False) #Имитация связи с юзером должно быть uuid (упростил)
    question = relationship('Question', back_populates='answers')


