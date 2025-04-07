FROM python:3.10-slim


SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию
WORKDIR /user_auth

# Устанавливаем pipenv
RUN pip install --no-cache-dir pipenv

# Копируем Pipfile и Pipfile.lock в контейнер
COPY Pipfile Pipfile.lock ./

# Устанавливаем зависимости с помощью pipenv
RUN pipenv install --deploy --ignore-pipfile

# Копируем все файлы приложения и .env файл в контейнер
COPY . .


# Указываем переменную окружения для Django
ENV DJANGO_SETTINGS_MODULE=conf.settings

# Открываем порт, на котором будет работать приложение
EXPOSE 8000
