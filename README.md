# Бот для подбора рецепта
   - роль пользователя одна:
     - можно посмотреть свои созданные рецепты
   - меню бота:
     - создать новый рецепт
     - получить рецепт по продуктам
     - подобрать самый популярный рецепт
   - создать новый рецепт
     - записать в бд сам рецепт и ингредиенты
     - ингредиенты в формате название
   - получить рецепт
     - запрашиваются имеющиеся продукты
     - после описание всех продуктов можно нажать "подобрать рецепт"
     - должна быть пагинация рецептов
     - предложенные рецепты можно лайкнуть
   - получить самый популярный рецепт по лайкам

### Запуск:

1. Запустить бекенд проекта на FastAPI
2. Создать .env файл (пример в .env.example)
3. `docker compose up --build`
4. В телеграме найти "SUON recipes" (@suon_recipes_bot)

Чтобы запустить бота через webhook, нужно раскомментировать соответствующую строку в .env

### Требования к проекту:

- Упаковка проекта в докер-компоуз и запуск через docker compose up без дополнительной настройки
- Два формата запуска - через polling и через webhook
- Стейт отдельный под каждого пользователя
- Без доступа к бд
- Метрики:
  - Время выполнения всех интеграционных методов (запросы на бекенд и телеграм)
- Настройки в env
- poetry как сборщик пакетов
- Обработка ошибок и соответствующие ответы от бота
- Обработка флуда
- Сквозное логирование
- прохождение flake8 + mypy в соответствии с конфигурациями проекта
