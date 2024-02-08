# Пример бекэнда на базе Django REST framework

## Запуск

```
python -m venv venv
venv\scripts\activate.bat
pip install -r requirements.txt
python manage.py runserver
```

## Семантика RESTful API

Действия с данными в базе данных (CRUD)
- INSERT - Create - POST (для списков - создает новый объект)
- SELECT - Read   - GET (получает список объектов)
- UPDATE - Update - PUT (PATCH)
- DELETE - Delete - DELETE
