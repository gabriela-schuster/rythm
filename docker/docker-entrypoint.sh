#!/bin/bash

# Wait for database service
./docker/wait-for-it.sh db:3306

# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate

# Create admin super user with admin/admin credentials
echo "Creating admin user if not exists"
python manage.py shell < docker/create_user.py

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
