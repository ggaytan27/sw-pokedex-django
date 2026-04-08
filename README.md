# sw-pokedex-django
Simple Pokedex app, using Django Framework


# Commands Section
--Creating project
django-admin startproject mysite

--Execute pending mitrations to DB
python manage.py migrate

--Run Development Server
py manage.py runserver

--Create an app
py manage.py startapp pokedex

--Creating and applying migrations
py manage.py makemigrations pokedex

--Inspect SQL outpput of a migration file
py manage.py sqlmigrsate pokedex 0001

--Sync DB with the new model
py manage.py migrate

--Creating an superuser
py manage.py createsuperuser
    - master
    - master@mail.com
    - 123456