Проект "Программа самообучения"
==============================
Краткое описание
----------------
LMS-система, в которой каждый желающий может размещать свои полезные материалы или курсы. Создан с использованием Python и DRF. Авторизация настроена с помощью JWT, настроен вывод документации через Swagger и Redoc, реализовано асинхронное выполнение задач с помощью Celery и Schedule. В качестве брокера используется Redis, в качестве базы данных PostgreSQL. Также в проекте имеется интеграция с сервисом платежей Stripe.

# Запуск приложения в docker-compose:

- Создай файл .env и заполни его по образцу .env_еxample 
- Для создания и запуска docker-контейнера выполни команду в терминале в папке проекта:

        docker-compose up -d --build

**Технологии в проекте:**

- Python, Celery, Redis, Django, DRF, PostgreSQL, JWT, Stripe, Unittest,

**Сущности в проекте:**

- Course (Курс)
- Lesson (Урок)
- User (Пользователь)
- Payment (Платеж)
- Subscription (Подписка)