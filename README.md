# Hakaton-MVP 🤖

**OpenSense** — платформа для доступного цифрового пространства.

## О проекте
Инструменты на основе AI для людей с ограниченными возможностями:
голосовой ввод, анализ текста, accessibility-функции.

## Структура
- `backend/` — FastAPI сервер (Python)
- `frontend/` — веб-интерфейс (HTML/CSS/JS)

## Запуск бэкенда
```bash
cd backend
pip install fastapi uvicorn
uvicorn main:app --reload
```

## API эндпоинты
- `GET /` — проверка работы
- `GET /health` — статус сервера  
- `POST /analyze` — анализ текста

## Команда
- Backend: EgorFurry
- Frontend: Бекболат
