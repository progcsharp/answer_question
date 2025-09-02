import pytest
from app import app

def test_app_structure():
    """Тест структуры приложения"""
    assert app is not None
    
    # Проверяем, что роутеры зарегистрированы
    routes = []
    for route in app.routes:
        if hasattr(route, 'path'):
            routes.append(route.path)
        elif hasattr(route, 'routes'):
            for subroute in route.routes:
                if hasattr(subroute, 'path'):
                    routes.append(subroute.path)
    
    print(f"Available routes: {routes}")
    
    # Проверяем основные эндпоинты
    assert "/questions" in routes or any("/questions" in route for route in routes)
    assert "/answers" in routes or any("/answers" in route for route in routes)

def test_health_endpoint_exists():
    """Тест что health endpoint существует в приложении"""
    # Проверяем, что health endpoint зарегистрирован
    health_routes = []
    for route in app.routes:
        if hasattr(route, 'path') and route.path == "/health":
            health_routes.append(route)
    
    assert len(health_routes) > 0, "Health endpoint не найден"
    print(f"Health endpoint найден: {health_routes[0].path}")

def test_cors_middleware():
    """Тест что CORS middleware добавлен"""
    # Проверяем middleware в правильном месте
    middleware_classes = []
    for middleware in app.user_middleware:
        if hasattr(middleware, 'cls'):
            middleware_classes.append(middleware.cls)
        else:
            middleware_classes.append(type(middleware))
    
    from fastapi.middleware.cors import CORSMiddleware
    assert CORSMiddleware in middleware_classes, f"CORS middleware не найден. Найденные: {middleware_classes}"
    print("CORS middleware найден")
