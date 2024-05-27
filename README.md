# Simple Django weblog

![Static Badge](https://img.shields.io/badge/DJANGO-4.2-%23092E20?style=flat&logo=django&labelColor=%23092E20&color=white)
![Static Badge](https://img.shields.io/badge/BOOTSTRAP-5-%237952B3?style=flat&logo=bootstrap&logoColor=white&labelColor=%237952B3&color=white)
![Static Badge](https://img.shields.io/badge/HTMX-%233366CC?style=flat&logo=htmx&logoColor=white&color=%233366CC)
![Static Badge](https://img.shields.io/badge/MARKDOWN-%23000000?style=flat&logo=markdown&labelColor=%23000000&color=white)

A simple blog powered by Python/Django with some features and templates to get you started quickly.

## Prerequisites

Make sure, that `python3` and `git` are installed on your machine.

## Features

- For Django 4.2
- Works with Python 3.12
- Makes use of Twitter Bootstrap v5 and Bootstrap icons
- Responsive
- Format your blog posts easily with Markdown
- Landing page with HTMX for infinite scrolling 
- Lightweight SQLite3 database
- Settings for development and production environment
- Each blog post has a image, tags, sources
- Faker factory to get a quick impression


## Optional Integrations

- PostgreSQL Database

## Installation

The following instructions will get you started.

**Clone this repository to your local working directory:**
```
$ git clone git@github.com:bjkawecki/simple-django-blog.git
```
**Create a virtual environment for local development:**
```
$ python -m venv .venv
```
**Activate the virtual environment:**
```
$ source .venv/bin/activate
```
**Install the project's dependencies:**
```
$ pip install -r requirements.txt
```
**Write the app's models to a migration file:**
```
$ python manage.py makemigrations
```
**Map the migrations to the database (creates a sqlite3 database by default):**
```
$ python manage.py migrate
```
**Create a superuser with a one-liner:**
```
$ python manage.py createsuperuser2 --username YOUR_USERNAME --password YOUR_PASSWORD --noinput --email 'YOUR_EMAIL'
```
**Start the development server at localhost:8000:**
```
$ python manage.py runserver
```


## Usage of the Faker factory

Removes all blog posts from the database and creates new fake blog posts with a tag and one source, after you confirmed. The number attribute is optional.
```
$ python manage.py fakeposts --number 5
```

Removes all blog posts from the database, after you confirmed.
```
$ python manage.py clearblog
```