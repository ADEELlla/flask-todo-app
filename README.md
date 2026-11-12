[前往中文文档](README_zh.md)

# flask-todo-app

> Simple web todo application based on flask.

![flask-todo](http://i.imgur.com/aXIeP9K.png)

## Dependencies

- alembic
- Babel
- Flask
- Jinja2
- Flask-Babel
- Flask-SQLAlchemy
- Flask-Script
- Flask-Migrate

## Installation

```
$ git clone https://github.com/aixiamomo/flask-todo-app
$ cd flask-todo-app
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

## How to run

```
$ cd flask-todo-app
$ python manage.py db upgrade
$ python manage.py runserver
 * Running on http://127.0.0.1:7345/ (Press CTRL+C to quit)
```

Then open url http://127.0.0.1:7345 in Chrome.

On Windows PowerShell, activate the environment with:

```
.\.venv\Scripts\Activate.ps1
```

## Continuous integration

The GitHub Actions workflow in `.github/workflows/ci-native.yml` runs on every
push and pull request to `master`. It installs dependencies, validates the
Python code, creates the SQLite database from the Alembic migration, and starts
the Flask server to verify that the home page responds through `curl`.



