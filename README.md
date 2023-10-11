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
docker build . -t django
```
```
docker run -p 8000:8000 django
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
