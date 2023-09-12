"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path
# from users.tasks import user_activity_check, task1
# from lms.tasks import shared_task

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z^)*&u(s0co&!2886kq#c%jev#h60ka2ajnn*(9)ozx9czfhrp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

STANDARD_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

USER_APPS = [
    'django_crontab',  # crontab
    'django_celery_beat',  # celery-beat
    'drf_yasg',  # yasg
    'rest_framework',  # rest_framework
    'django_filters',  # django_filters
    'rest_framework_simplejwt',  # JWT
    'users.apps.UsersConfig',
    'lms.apps.LmsConfig',
]

INSTALLED_APPS = STANDARD_APPS + USER_APPS

STRIPE_API_KEY = "sk_test_51NaO5cAG5LQisvlaNNahDCacDrXRR7qNuI34osLGqdwVLi53iWtDcNXNXAAfRRKp4v0GP7XNkqI2xZMMP0dh8tdH00pJkDoYtj"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'work21',
#         'USER': 'postgres',
#         'PASSWORD': '1973',
#     }
# }

# для докера
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': work21-docker,
        'USER': postgres,
        'PASSWORD': mysecretpassword,
        'HOST': db,
    }
}


# Password validation

# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'django-test-alex77bel@yandex.ru'
EMAIL_HOST_PASSWORD = 'nqlxykqluoiwvzwd'
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER

REST_FRAMEWORK = {

    # настройка для rest_framework
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),

    # настройка для JWT
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),

    # эта настройка добавляет авторизацию на все контроллеры
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',)
    # по умолчанию доступ ко всему открыт
    # 'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',)
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=10),
}

CELERY_BEAT_SCHEDULE = {

    'user_activity_check': {
        'task': 'users.tasks.user_activity_check',
        'schedule': timedelta(minutes=1)
    },
}
# 1. Обязательно должно присутствовать 'task', иначе не найдет
# 2. команды запуска периодических задач (надо почему-то в разных терминалах):
# celery -A config worker -l INFO
# celery -A config beat -l info -S django


# Настройки для Celery
# URL-адрес брокера сообщений
CELERY_BROKER_URL = 'redis://localhost:6379'  # Например, Redis, который по умолчанию работает на порту 6379
# URL-адрес брокера результатов, также Redis
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# Часовой пояс для работы Celery
CELERY_TIMEZONE = "Europe/Moscow"
# Флаг отслеживания выполнения задач
CELERY_TASK_TRACK_STARTED = True
# Максимальное время на выполнение задачи
CELERY_TASK_TIME_LIMIT = 30 * 60

# CRONJOBS = [
#     ('* * * * *', 'lms.cron.my_scheduled_job'щз),
# ]
