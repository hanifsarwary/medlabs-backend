release: python manage.py migrate
web: gunicorn ambProject.wsgi
worker: celery -A ambProject worker -l info
