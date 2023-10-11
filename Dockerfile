FROM python:3.10.12

RUN mkdir app
WORKDIR app

ADD . /app/

RUN pip install -r requirements.txt

CMD gunicorn mainapp.wsgi:application -b 0.0.0.0:8000