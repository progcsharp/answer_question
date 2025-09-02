import functools

import logging
from datetime import datetime
from typing import Callable

logger = logging.getLogger()

def log_route(route_name: str = None):
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            logger = logging.getLogger()
            route = route_name or f"{func.__module__}.{func.__name__}"
            
            # Извлекаем информацию о запросе
            request_info = ""
            if args and hasattr(args[0], 'request'):
                request = args[0].request
                request_info = f" | {request.method} {request.url.path}"
            
            logger.info(f"📥 Запрос: {route}{request_info}")
            
            start_time = datetime.now()
            
            try:
                result = await func(*args, **kwargs)
                
                execution_time = (datetime.now() - start_time).total_seconds()
                logger.info(f"�� Ответ: {route} | {execution_time:.3f}с | Успех")
                
                return result
                
            except Exception as e:
                execution_time = (datetime.now() - start_time).total_seconds()
                logger.error(f"💥 Ошибка: {route} | {execution_time:.3f}с | {str(e)}")
                raise
        
        return wrapper
    return decorator