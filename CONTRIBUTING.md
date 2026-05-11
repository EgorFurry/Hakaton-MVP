# Как работать с репозиторием

## Первый раз
1. Установи Git: https://git-scm.com/download/win
2. Склонируй репо:
   git clone https://github.com/EgorFurry/Hakaton-MVP.git
3. Настрой себя:
   git config --global user.name "ТвоёИмя"
   git config --global user.email "твоя@почта.com"

## Каждый день
1. Переключись на свою ветку:
   git checkout frontend
2. Подтяни свежие изменения:
   git pull origin frontend
3. Поработал — сохрани:
   git add .
   git commit -m "Что именно сделал"
   git push origin frontend

## Правила
- Никогда не пушь напрямую в main
- Всегда работай в своей ветке (frontend или backend)
- Пиши понятные сообщения коммитов
- Если что-то сломалось — пиши мне или в группу 

                                         Удачи, Егор 