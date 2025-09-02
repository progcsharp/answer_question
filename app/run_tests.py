#!/usr/bin/env python3
"""
Скрипт для запуска тестов Question-Answer API
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Запускает команду и выводит результат"""
    print(f"\n{'='*50}")
    print(f"🚀 {description}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("✅ Успешно выполнено")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка выполнения команды: {e}")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        return False

def main():
    """Основная функция"""
    print("🧪 Запуск тестов для Question-Answer API")
    
    # Проверяем, что мы в правильной директории
    if not os.path.exists("tests"):
        print("❌ Директория tests не найдена. Убедитесь, что вы находитесь в корне проекта.")
        sys.exit(1)
    
    # Запускаем простые тесты
    if run_command("python -m pytest tests/test_simple.py -v", "Запуск простых тестов"):
        print("\n✅ Простые тесты прошли успешно!")
    else:
        print("\n❌ Простые тесты завершились с ошибками")
    
    # Запускаем все тесты
    if run_command("python -m pytest tests/ -v", "Запуск всех тестов"):
        print("\n✅ Все тесты прошли успешно!")
    else:
        print("\n❌ Некоторые тесты завершились с ошибками")
        print("\n💡 Рекомендации:")
        print("1. Проверьте, что все зависимости установлены: pip install -r requirements.txt")
        print("2. Убедитесь, что pytest-asyncio установлен: pip install pytest-asyncio")
        print("3. Для детальной диагностики используйте: python -m pytest tests/ -v -s")

if __name__ == "__main__":
    main()
