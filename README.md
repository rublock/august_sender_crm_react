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
* подключаем БД Postgres
```
sudo apt update && sudo apt install postgresql postgresql-contrib
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
* запускаем миграции для Django
```
python manage.py makemigrations
```
```
python manage.py migrate
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
* теперь надо в корне проекта создать папку frontend и развернуть там Реакт
```
mkdir frontend
```
### Подключаем Doker
*
```
https://docs.docker.com/engine/install/ubuntu/
```
*
```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```
```
cd frontend
```
```
docker build . -t react
```
```
docker run -p 3000:3000 --rm --name react-container -d react
```
```
http://127.0.0.1:3000/
```
* остановить сервер
```
docker stop react-container
```
*
```

```