from fastapi import FastAPI

import uvicorn

from typing import Optional

# Создание объекта приложения.
app = FastAPI()
# app = FastAPI(docs_url=None, redoc_url=None) 

# @app.get('/')
# def read_root():
#     return {'Hello': 'FastAPI'}

@app.get('/me')
def hello_author():
    return {'Hello': 'author'}

@app.get('/{name}')
def greetings(
        name: str,
        surname: str,
        age: Optional[int] = None,
        is_staff: bool = False
) -> dict[str, str]:
    result = ' '.join([name, surname])
    result = result.title()
    if age is not None:
        result += ', ' + str(age)
    if is_staff:
        result += ', сотрудник'
    return {'Hello': result} 


if __name__ == '__main__':
    # Команда на запуск uvicorn.
    # Здесь же можно указать хост и/или порт при необходимости,
    # а также другие параметры.
    uvicorn.run('main:app', reload=True) 