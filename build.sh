#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py makemigrations accounts
python manage.py makemigrations core
python manage.py makemigrations madameParfum
python manage.py makemigrations
python manage.py migrate accounts
python manage.py migrate core
python manage.py migrate madameParfum
python manage.py migrate