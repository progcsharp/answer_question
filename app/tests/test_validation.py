import pytest
from pydantic import ValidationError
from shemas.questions import QuestionCreate, QuestionUpdate
from shemas.answer import AnswerCreate, AnswerUpdate


class TestQuestionValidation:
    """Тесты валидации вопросов"""

    def test_valid_question_create(self):
        """Тест создания валидного вопроса"""
        question_data = {"text": "Это валидный вопрос с достаточным количеством символов для прохождения валидации?"}
        question = QuestionCreate(**question_data)
        assert question.text == question_data["text"]

    def test_empty_text_question_create(self):
        """Тест что пустой текст вопроса не проходит валидацию"""
        with pytest.raises(ValidationError) as exc_info:
            QuestionCreate(text="")
        assert "String should have at least 10 characters" in str(exc_info.value)

    def test_short_text_question_create(self):
        """Тест что короткий текст вопроса не проходит валидацию"""
        with pytest.raises(ValidationError) as exc_info:
            QuestionCreate(text="Короткий")
        assert "String should have at least 10 characters" in str(exc_info.value)

    def test_long_text_question_create(self):
        """Тест что слишком длинный текст вопроса не проходит валидацию"""
        long_text = "Очень длинный текст вопроса " * 50  # Более 1000 символов
        with pytest.raises(ValidationError) as exc_info:
            QuestionCreate(text=long_text)
        assert "String should have at most 1000 characters" in str(exc_info.value)

    def test_valid_question_update(self):
        """Тест валидного обновления вопроса"""
        question_data = {"text": "Обновленный вопрос с достаточным количеством символов"}
        question = QuestionUpdate(**question_data)
        assert question.text == question_data["text"]

    def test_none_text_question_update(self):
        """Тест что None текст в обновлении проходит валидацию"""
        question = QuestionUpdate(text=None)
        assert question.text is None


class TestAnswerValidation:
    """Тесты валидации ответов"""

    def test_valid_answer_create(self):
        """Тест создания валидного ответа"""
        answer_data = {
            "text": "Это валидный ответ с достаточным количеством символов",
            "user_id": "user123"
        }
        answer = AnswerCreate(**answer_data)
        assert answer.text == answer_data["text"]
        assert answer.user_id == answer_data["user_id"]

    def test_empty_text_answer_create(self):
        """Тест что пустой текст ответа не проходит валидацию"""
        with pytest.raises(ValidationError) as exc_info:
            AnswerCreate(text="", user_id="user123")
        assert "String should have at least 5 characters" in str(exc_info.value)

    def test_short_text_answer_create(self):
        """Тест что короткий текст ответа не проходит валидацию"""
        with pytest.raises(ValidationError) as exc_info:
            AnswerCreate(text="К", user_id="user123")  # 1 символ, минимум 5
        assert "String should have at least 5 characters" in str(exc_info.value)

    def test_long_text_answer_create(self):
        """Тест что слишком длинный текст ответа не проходит валидацию"""
        long_text = "Очень длинный ответ " * 200  # Более 2000 символов
        with pytest.raises(ValidationError) as exc_info:
            AnswerCreate(text=long_text, user_id="user123")
        assert "String should have at most 2000 characters" in str(exc_info.value)

    def test_empty_user_id_answer_create(self):
        """Тест что пустой user_id не проходит валидацию"""
        with pytest.raises(ValidationError) as exc_info:
            AnswerCreate(text="Валидный ответ", user_id="")
        assert "String should have at least 3 characters" in str(exc_info.value)

    def test_short_user_id_answer_create(self):
        """Тест что короткий user_id не проходит валидацию"""
        with pytest.raises(ValidationError) as exc_info:
            AnswerCreate(text="Валидный ответ", user_id="ab")
        assert "String should have at least 3 characters" in str(exc_info.value)

    def test_long_user_id_answer_create(self):
        """Тест что слишком длинный user_id не проходит валидацию"""
        long_user_id = "a" * 101  # Более 100 символов
        with pytest.raises(ValidationError) as exc_info:
            AnswerCreate(text="Валидный ответ", user_id=long_user_id)
        assert "String should have at most 100 characters" in str(exc_info.value)

    def test_valid_answer_update(self):
        """Тест валидного обновления ответа"""
        answer_data = {"text": "Обновленный ответ с достаточным количеством символов"}
        answer = AnswerUpdate(**answer_data)
        assert answer.text == answer_data["text"]

    def test_none_text_answer_update(self):
        """Тест что None текст в обновлении ответа проходит валидацию"""
        answer = AnswerUpdate(text=None)
        assert answer.text is None


class TestEdgeCases:
    """Тесты граничных случаев"""

    def test_minimum_valid_question_length(self):
        """Тест минимально допустимой длины вопроса"""
        question_data = {"text": "1234567890"}  # Ровно 10 символов
        question = QuestionCreate(**question_data)
        assert question.text == "1234567890"

    def test_minimum_valid_answer_length(self):
        """Тест минимально допустимой длины ответа"""
        answer_data = {
            "text": "12345",  # Ровно 5 символов
            "user_id": "abc"   # Ровно 3 символа
        }
        answer = AnswerCreate(**answer_data)
        assert answer.text == "12345"
        assert answer.user_id == "abc"

    def test_maximum_valid_question_length(self):
        """Тест максимально допустимой длины вопроса"""
        question_data = {"text": "а" * 1000}  # Ровно 1000 символов
        question = QuestionCreate(**question_data)
        assert len(question.text) == 1000

    def test_maximum_valid_answer_length(self):
        """Тест максимально допустимой длины ответа"""
        answer_data = {
            "text": "а" * 2000,  # Ровно 2000 символов
            "user_id": "a" * 100   # Ровно 100 символов
        }
        answer = AnswerCreate(**answer_data)
        assert len(answer.text) == 2000
        assert answer.user_id == "a" * 100
