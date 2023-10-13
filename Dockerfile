FROM python:3.11-slim

WORKDIR /app

COPY . /app/
RUN apt-get update && apt-get install -y curl && apt-get clean
RUN pip install -r requirements.txt

CMD python manage.py migrate \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='adin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin')" \
    && python manage.py runserver 0.0.0.0:8000