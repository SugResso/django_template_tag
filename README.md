<h1 align="center"> django_template_tag </h1>

<p align="center">
<--<a href="https://github.com/SugResso/task_book"> прошлый проект </a>
|
<a href="https://github.com/SugResso"> следующий проект </a> -->
</p>

---
# ТЗ: 

Задание
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:

   1) Меню реализовано через template tag
   2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
   3) Хранится в БД.
   4) Редактируется в стандартной админке Django
   5) Активный пункт меню определяется исходя из URL текущей страницы
   6) Меню на одной странице может быть несколько. Они определяются по названию.
   7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через
      named url.
   8) На отрисовку каждого меню требуется ровно 1 запрос к БД

Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.

      {% draw_menu 'main_menu' %}

При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.

# Настройки

---
Склонируйте репозиторий:

      git clone https://github.com/SugResso/django_template_tag.git
Перейдите в папку с проектом и активируйте виртуальное окружение:

      python -m pip install --upgrade pip
      python -m venv venv
      source venv/Scripts/activate
Установите необходимые зависимости проекта:

      pip install -r requirements.txt
Перейдите в папку и выполните миграции:

      cd src
      python manage.py makemigrations
      python manage.py migrate
Создайте супер пользователя:

      python manage.py createsuperuser
Заполните таблицу:

      python manage.py loaddata Menu_dump.json
      python manage.py loaddata Item_dump.json
Можно запускать:

      python manage.py runserver