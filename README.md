## Create the project directory
> mkdir Your_Directory

> cd Your_Directory

## Create a virtual environment to isolate our package dependencies locally
> python3 -m venv env

> source env/bin/activate  # On Windows use `env\Scripts\activate`

## Install Django and Django REST framework into the virtual environment
> pip install -r requirements.txt

## Set up a new project with a single application
> django-admin startproject books_api

> cd books

> django-admin startapp books

## Migrate Models to DB
> python manage.py makemigrations books

> python manage.py migrate books

## Use DB
> sqlite3  db.sqlite3
 
> .tables
OR
> python manage.py dbshell 

## Run Server
> python manage.py runserver 8080