Проект "Программа самообучения"
==============================
Краткое описание
----------------
LMS-система, в которой каждый желающий может размещать свои полезные материалы или курсы. Создан с использованием Python и DRF. Авторизация настроена с помощью JWT, настроен вывод документации через Swagger и Redoc, реализовано асинхронное выполнение задач с помощью Celery и Schedule. В качестве брокера используется Redis, в качестве базы данных PostgreSQL. Также в проекте имеется интеграция с сервисом платежей Stripe.

# Инструкция по запуску DockerFile

1.Первой инструкцией всегда идёт FROM с указанием родительского образа. Например, FROM python:3.11.

2.Инструкция WORKDIR устанавливает рабочий каталог контейнера. Например, WORKDIR /code. Последующие команды RUN, CMD наследуют привязку WORKDIR.

3.Завершающей инструкцией всегда идёт CMD. Например, CMD ["python", "main.py"]. CMD наследует привязку к WORKDIR, поэтому web_interface.py будет запущен из папки /code.


Чтобы собрать Docker-образ, сохраним данный Dockerfile в директории с вашим проектом и выполним команду в терминале:
docker build -t my-python-app .
Здесь -t my-python-app задает имя образа, а . указывает на текущую директорию с Dockerfile.
После успешной сборки образа вы можете запустить контейнер с помощью команды:
docker run my-python-app
Таким образом вы запустите ваше Python-приложение в контейнере.


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
