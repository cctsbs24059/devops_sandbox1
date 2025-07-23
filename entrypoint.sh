#!/bin/bash

# Wait for the DB if needed (example: Postgres/MySQL)

echo "Waiting for PostgreSQL..."

while ! nc -z "$DATABASE_HOST" 5432; do
  sleep 0.5
done

echo "PostgreSQL is up — applying migrations"
python manage.py migrate

echo "Starting Django app"
exec "$@"

# python manage.py runserver 0.0.0.0:8000