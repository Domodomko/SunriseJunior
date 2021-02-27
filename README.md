# SunRise Junior Task
## Made by Sergei Shinn

A Django app with product catalog and authorization, made as a test task for a Junior Backend-developer vacancy.


## About Developing

- The task was written in 2 days, most of the time was spent learning jQuery and Ajax
- I write API and native Django application together for the first time. It was an interesting experience


## Link Structure

Here's some kind of documentation for this app:

- /admin - Admin panel
- /api - API part of the App
    - /signup - Sign Up
    - /signin - Sign In
    - /user - User Profile Update
- /user - User Profile Update
- /signin - Sign In
- /signout - Sign Out
- /signup - Sign Up
- /products - Products part of the App
    - /products - Products List
    - /categories - Categories List
    - /products/<pk> - Product Page


## Installation
##### *This instruction is written for Linux users*

After pushing this repository, you'll need to create new python venv for it and install requirements:

```sh
python3 -m venv /venv
pip install -r requirements.txt
```

After that you'll need to migrate the data, create a superuser and run the application:

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
