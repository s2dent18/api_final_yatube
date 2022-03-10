[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)

# API сервис Yatube

```sh
git clone https://github.com/s2dent18/api_final_yatube.git
```

## Описание сервиса:

Основная задумка проекта: перенос функционала сервиса Yatube в формат API приложения, которое позволит пользоваться сервисом вне сайта.

## Функционал:

* система подписок на пользователей   
* просмотр, создание и редактирование постов    
* просмотр и создание групп  
* просмотр, создание и редактирование комментариев  
* фильтрация по заданным параметрам   

Документация доступна по адресу http://localhost:8000/redoc/

## Локальный запуск проекта:

* Создайте файл с переменными виртуального окружения:  
```sh
python -m venv venv
```    
* Выполните установку зависимостей из файла requirements.txt:   
```sh
pip install -r requirements.txt
```    
* Выполните миграции командой:  
```sh
python manage.py migrate
```  
* Запустите сервер:  
```sh
python manage.py runserver
```  
