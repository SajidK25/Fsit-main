#!/bin/bash
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate

# gunicorn backend.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
exec "$@"
