# Hakaton-MVP 🤖

**OpenSense** — AI-платформа для доступного цифрового пространства.

## О проекте
Инструменты на основе AI для людей с ограниченными возможностями:
голосовой ввод, анализ текста, OCR, accessibility-функции.

## Структура
- `backend/` — FastAPI сервер (Python)
- `docs/` — веб-интерфейс (HTML/CSS/JS)

## Запуск бэкенда

### 1. Клонируй репо
git clone https://github.com/EgorFurry/Hakaton-MVP.git
cd Hakaton-MVP/backend

### 2. Установи зависимости
pip install -r requirements.txt

### 3. Запусти сервер
uvicorn main:app --reload

## API эндпоинты
- `GET /` — проверка работы
- `GET /health` — статус сервера
- `POST /analyze` — анализ текста

## Сайт
https://egorfurry.github.io/Hakaton-MVP/

## Команда
- Backend: EgorFurry
- Frontend: Бекболат
