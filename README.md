# august_sender_crm
CRM

* Python 3.10.12
* Django 4.2.4
* PostgreSQL 14.9

### инструкция по запуску бэк сервера

* скачиваем Python
```
https://www.python.org/downloads/
```
* клонируем репозиторий
```
git clone git@github.com:rublock/august_sender_crm.git
```
* менеджер пакетов python
```
sudo -H pip3 install --upgrade pip
```
* виртуальное окружение
```
sudo pip install virtualenv && virtualenv venv && . venv/bin/activate
```
* тут надо выбрать интерпретатор проекта в IDE

* устанавливаем зависимости
```
pip install -r requirements.txt
```
* запускаем бэк сервер
```
python manage.py runserver 127.0.0.1:8000
```
* заходим
```
http://127.0.0.1:8000/
```
* должна быть нарисована ракета 
```
The install worked successfully! Congratulations!
You are seeing this page because DEBUG=True is in your settings file and you have not configured any URLs.
```
* подключаем БД Postgres
```
sudo apt update && sudo apt install postgresql postgresql-contrib
```
* драйвер для подключения postgres к Django
```
pip install psycopg2-binary
```
* заходим в консоль Postgres
```
sudo -u postgres psql
```
* создаем БД
```
CREATE DATABASE august_sender;
```
* выходим
```
ctrl+z
```
* изменяем настройки в config/settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'august_sender',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
* запускаем миграции для Django
```
python manage.py makemigrations
```
```
python manage.py migrate
```
* теперь надо в корне проекта создать папку frontend и развернуть там Реакт
```
mkdir frontend
```