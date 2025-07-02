from fastapi import FastAPI, Path, Query

import uvicorn

from typing import Optional

from enum import Enum

# Создание объекта приложения.
app = FastAPI()
# app = FastAPI(docs_url=None, redoc_url=None) 



class EducationLevel(str, Enum):
    # Укажем значения с большой буквы, чтобы они хорошо смотрелись 
    # в документации Swagger.
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'


@app.get('/me', tags=['special methods'], summary='Приветствие автора')
def hello_author():
    return {'Hello': 'author'}

@app.get(
        '/{name}',
        tags=['common methods'],
        summary='Общее приветствие',
        response_description='Полная строка приветствия'
)
def greetings(
        *,
        name: str = Path(..., min_length=2, max_length=20),
        age: Optional[int] = None,
        is_staff: bool = False,
        education_level: Optional[EducationLevel] = None,
        surname: str = Query(..., min_length=2, max_length=50),
) -> dict[str, str]:
    """
    Приветствие пользователя:

    - **name**: имя
    - **surname**: фамилия
    - **age**: возраст (опционально)
    - **is_staff**: является ли пользователь сотрудником
    - **education_level**: уровень образования (опционально)
    """
    result = ' '.join([name, surname])

    result = result.title()

    if age is not None:
        result += ', ' + str(age)

    if education_level is not None:
        # Чтобы текст смотрелся грамотно, 
        # переведём строку education_level в нижний регистр.
        result += ', ' + education_level.lower()

    if is_staff:
        result += ', сотрудник'

    return {'Hello': result} 


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True) 