from pathlib import Path
import environ
import os
from datetime import timedelta

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env.read_env(os.path.join(BASE_DIR, "user_auth/.env"))

SECRET_KEY = env("SECRET_KEY", cast=str)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG", cast=str)

ALLOWED_HOSTS = env("ALLOWED_HOSTS", cast=lambda v: [s.strip() for s in v.split(",")])

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user.apps.UserConfig',
    'authentication.apps.AuthenticationConfig',
    'db.apps.DbConfig',
    'rest_framework',
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'conf.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': env.db()
}

# DATABASE_URL=postgres://user1:198616Gm@localhost:5432/db_user
# на сервере
# DATABASE_URL=postgres://user1:198616Gm@db:5432/db_user


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

STATIC_URL = env("STATIC_URL", cast=str)
STATIC_ROOT = os.path.join(BASE_DIR, env("STATIC_ROOT", cast=str, default="static/"))

MEDIA_ROOT = os.path.join(BASE_DIR, "uploads/")
MEDIA_URL = env("MEDIA_URL", cast=str)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'db.User'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


SIMPLE_JWT = {
    # Время жизни токена доступа (в данном случае 15 минут)
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),

    # Время жизни токена обновления (в данном случае 1 день)
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),

    # Указывает, нужно ли обновлять токены обновления при каждом запросе
    "ROTATE_REFRESH_TOKENS": False,

    # Указывает, нужно ли добавлять токен в черный список после его обновления
    "BLACKLIST_AFTER_ROTATION": False,

    # Указывает, нужно ли обновлять время последнего входа пользователя
    "UPDATE_LAST_LOGIN": False,

    # Алгоритм, используемый для подписи токенов (в данном случае HMAC SHA-256)
    "ALGORITHM": "HS256",

    # Ключ для подписи токенов, обычно это SECRET_KEY вашего Django проекта
    "SIGNING_KEY": SECRET_KEY,

    # Ключ для проверки подписи токенов (обычно оставляется пустым)
    "VERIFYING_KEY": "",

    # Аудитория токенов (можно использовать для ограничения использования токена)
    "AUDIENCE": None,

    # Издатель токенов (можно использовать для идентификации источника токена)
    "ISSUER": None,

    # Пользовательский JSON-кодер (можно использовать для изменения способа сериализации)
    "JSON_ENCODER": None,

    # URL для получения JWK (JSON Web Key) для проверки подписи токена (обычно не используется)
    "JWK_URL": None,

    # Допуск по времени для проверки срока действия токена (0 означает отсутствие допуска)
    "LEEWAY": 0,

    # Типы заголовков аутентификации, используемые для передачи токена (в данном случае Bearer)
    "AUTH_HEADER_TYPES": ("Bearer",),

    # Имя заголовка, в котором будет передаваться токен (обычно HTTP_AUTHORIZATION)
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",

    # Поле, представляющее идентификатор пользователя (по умолчанию 'id')
    "USER_ID_FIELD": "id",

    # Поле, в котором будет храниться идентификатор пользователя в токене
    "USER_ID_CLAIM": "user_id",

    # Правило аутентификации пользователя (по умолчанию используется стандартное правило)
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    # Классы токенов аутентификации, которые будут использоваться (в данном случае только AccessToken)
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),

    # Имя поля для указания типа токена (обычно 'token_type')
    "TOKEN_TYPE_CLAIM": "token_type",

    # Класс пользователя токена (по умолчанию TokenUser )
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser ",

    # Уникальный идентификатор токена (JTI - JWT ID)
    "JTI_CLAIM": "jti",

    # Имя поля для указания времени истечения для скользящего токена обновления
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",

    # Время жизни скользящего токена (в данном случае 5 минут)
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),

    # Время жизни скользящего токена обновления (в данном случае 1 день)
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    # Сериализатор для получения токенов (по умолчанию TokenObtainPairSerializer)
    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",

    # Сериализатор для обновления токенов (по умолчанию TokenRefreshSerializer)
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",

    # Сериализатор для проверки токенов (по умолчанию TokenVerifySerializer)
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",

    # Сериализатор для черного списка токенов (по умолчанию TokenBlacklistSerializer)
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",

    # Сериализатор для получения скользящих токенов (по умолчанию TokenObtainSlidingSerializer)
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",

    # Сериализатор для обновления скользящих токенов (по умолчанию TokenRefreshSlidingSerializer)
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}
