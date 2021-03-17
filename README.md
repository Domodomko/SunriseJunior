# SunRise Junior Task
## Made by Sergei Shinn

A Django app with product catalog and authorization, made as a test task for a Junior Backend-developer vacancy.


## About Developing

- The task was written in 2 days, most of the time was spent learning jQuery and Ajax
- I write API and native Django application together for the first time. It was an interesting experience
- I chose confirmation by mail for authorization,, but I'm also familiar with FireBase


## Link Structure

Here's some kind of documentation for this app:  
  
**The Main Page has products categories and subcategories on it**

- **/user** - User Profile Update
- **/signin** - Sign In
- **/signout** - Sign Out
- **/signup** - Sign Up
- **/products** - Products List
- **/products/(pk)** - Product Page
- **/api** - API part of the App
    - **/signup** - Sign Up
    - **/signin** - Sign In
    - **/user** - User Profile Update
- **/admin** - Admin panel
- **/swagger** - Swagger API Page
- **/redoc** - Redoc API Page


## Installation
##### *This instruction is written for Linux users*
After pushing this repository and creating your DB on Postgre, you'll need to create new python venv for it and install requirements:

```sh
python3 -m venv /venv
pip install -r requirements.txt
```
Create settings .env file with these variables inside:
- DEBUG
- SECRET_KEY
- DATABASE_URL
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT
- EMAIL_HOST
- EMAIL_PORT
- EMAIL_HOST_USER
- EMAIL_HOST_PASSWORD
- EMAIL_BACKEND


After that you'll need to migrate the data, create a superuser and run the application:

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
