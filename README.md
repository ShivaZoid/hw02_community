# Спринт 3 - Сообщества

 Создано и зарегистрировано приложение Posts. Подключена база данных. Десять последних записей выводятся на главную страницу. В админ-зоне доступно управление объектами модели Post: можно публиковать новые записи или редактировать/удалять существующие.

Пользователь может перейти на страницу любого сообщества, где отображаются десять последних публикаций из этой группы.

## Установка

Для запуска приложения в dev-режиме проделайте следующие шаги:
1) Склонируйте репозиторий.

2) Перейдите в папку с кодом и создайте виртуальное окружение:
~~~
python -m venv venv
~~~

3) Активируйте виртуальное окружение:
~~~
source venv/Scripts/activate
~~~

4) Установите зависимости:
~~~
python -m pip install -r requirements.txt
~~~

5) Выполните миграции:
~~~
python manage.py makemigrations

python manage.py migrate
~~~

6) Создайте суперпользователя:
~~~
python manage.py createsuperuser
~~~

7) Запустите сервер:
~~~
python manage.py runserver
~~~
