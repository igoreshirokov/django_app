#!/bin/bash

# Устанавливаем зависимости
pip install -r requirements.txt
# tail -f /dev/null

python manage.py makemigrations
echo "Созданы миграции"

python manage.py migrate
echo "Миграции применены"

python manage.py createdemodata
echo "Установлены демо данные"


export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_EMAIL=admin@example.com
export DJANGO_SUPERUSER_PASSWORD=admin123

python manage.py createsuperuser --noinput
echo "Суперпользователь создан admin & admin123"

python manage.py runserver 0.0.0.0:8000

