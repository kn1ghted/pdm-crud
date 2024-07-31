# Introduction

Simple CRUD system developed using Python - Django and MySQL

Template is written with django 5.07 and python 3 in mind.

### Main features

* Bootstrap CDN included

# Development stages

This project has been developed with the reference of this youtube video by Develoteca
https://youtu.be/ezIj71CX944?si=WSPATU_IblIy_43q

Language and model has been replaced for own learning purposes

    - Django install from the console 
    $ pip install django
    
    - Start the new project:
    $ django-admin startproject <project_name>     
      
    - Create Django application
    $ python3 manage.py startapp <app_name>

    - Add application URLs and VIEWS
    urls.py and views.py under the new folder with the application name

    - Configure and connect MySQL database
    Database name must match instance schema
    Simple USERS table created
    Install pymysql package in _init_.py
    pymysql.install_as_MySQLdb()

    - Make migrations. In case of changes in the models rerun the shell commands
    $ python3 manage.py makemigrations
    $ python3 manage.py migrate

    - Create manager admin user
    $ python3 manage.py createsuperuser
    u: admin
    p: admin

You can now run the development server:

    $ python manage.py runserver