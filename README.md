# august_sender_crm
CRM

* Python 3.10.12
* Django 4.2.4
* PostgreSQL 14.9
* Docker 24.0.6

### инструкция по запуску через Docker

```
https://www.docker.com/get-started/
```
* контейнер с Postgres
```
docker-compose up -d postgres
```

* контейнер с Django
```
docker-compose up -d mainapp
```
* если нужно зайти в контейнер
```
docker exec -it django-container /bin/bash
```

* контейнер с React