8. Бот для подбора рецепта - Вечернина Вероника
   - роль пользователя одна:
     - можно посмотреть свои созданные рецепты \/
   - меню бота:
     - создать новый рецепт \/
     - получить рецепт по продуктам \/
     - подобрать самый популярный рецепт \/
   - создать новый рецепт
     - записать в бд сам рецепт и ингредиенты \/
     - ингредиенты в формате название + граммы (пусть все в граммах будет) *
   - получить рецепт
     - запрашиваются имеющиеся продукты \/
     - после описание всех продуктов можно нажать "подобрать рецепт" \/
     - должна быть пагинация рецептов \/
     - предложенные рецепты можно лайкнуть и дизлайкнуть (пусть просто счетчик лайков у рецепта) \/
   - получить самый популярный рецепт по лайкам \/


Требования к проекту:

- Упаковка проекта в докер-компоуз и запуск через docker compose up без дополнительной настройки \/
- Два формата запуска - через polling и через webhook \/
- Стейт отдельный под каждого пользователя \/
- Без доступа к бд \/
- Метрики:
  - TODO
  - Время выполнения всех интеграционных методов (запросы на бекенд и телеграм) *
- Настройки в env \/
- poetry как сборщик пакетов \/
- Обработка ошибок и соответствующие ответы от бота \/
- Обработка флуда (tg blocks when you send too many requests) *
- Сквозное логирование \/
- прохождение flake8 + mypy в соответствии с конфигурациями проекта
- В README.md ожидается увидеть как что работает, чтобы можно было ознакомиться проще с проектом
