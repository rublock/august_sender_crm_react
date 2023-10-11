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
* контейнер с Django
```
docker build . -t django:4.2.4
```
```
docker run -p 8000:8000 --rm --name django-container -d django:4.2.4
```


* контейнер с Postgres
```
docker pull postgres:14.9
```
```
docker run --name postgres-container -e POSTGRES_PASSWORD=postgres -d -p 5432:5432 postgres:14.9
```
```
docker exec -it postgres-container bash
```
```
psql -U postgres
```
```
CREATE DATABASE august_sender;
```



* контейнер с React
```
cd frontend
```
```
docker build . -t react
```
```
docker run -p 3000:3000 --rm --name react-container -d react
```
*
```

```
