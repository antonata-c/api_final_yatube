# Описание проекта:
Данный проект является API для социальной сети Yatube, выполняет задачи связанные с добавлением постов, групп, комментариев и всего что относится к социальным сетям.

Предоставлен полноценный доступ ко всем функциям социальной сети с помощью отправки запросов на сервер.

### Стек используемых технологий:
- `Python 3.8`
- `Django`
- `Django REST Framework`
- `SQLite3`
***
# Как запустить проект:
##### Для Windows используем:
```python
python
```
##### Для Linux и MacOS используем:
```python
python3
```
### Клонировать репозиторий и перейти в него в командной строке:
```python
git clone https://github.com/antonata-c/api_final_yatube.git
cd api_final_yatube
```
### Cоздать и активировать виртуальное окружение:
```python
python3 -m venv venv
source venv/bin/activate
```
### Обновить пакетный менеджер pip:
```python
python3 -m pip install --upgrade pip
```
### Установить зависимости из файла requirements.txt
```python
pip install -r requirements.txt
```
### Выполнить миграции:
```python
cd yatube_api
python3 manage.py migrate
```
### Запустить проект:
```python
python3 manage.py runserver
```


### Пример запросов к API
* Получение всех постов
```python
URL: api/v1/posts/
Method: GET
Response: {
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
* Добавление нового комментария
```python
URL: api/v1/posts/{post_id}/comments/
Method: POST
Params: {
    "text": "string"
}

Response: {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
}
```
#### Полная документация доступна по адресу:
```python
http://127.0.0.1:8000/redoc/
```
***
### Автор работы:
**[Антон Земцов](https://github.com/antonata-c)**
