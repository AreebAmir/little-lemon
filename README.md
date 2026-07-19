# Little Lemon

A backend API for a fictional restaurant, built with Django and Django REST Framework. It exposes endpoints for managing the menu and table bookings, with token-based authentication via Djoser.

## Tech stack

- **Backend:** Django 4.2, Django REST Framework
- **Auth:** Djoser (token authentication)
- **Database:** MySQL
- **Rendering:** JSON and XML API responses (`djangorestframework-xml`)

## Features

- Menu items: list, create, retrieve, update, delete (`Menu` model)
- Table bookings: list, create, retrieve, update, delete (`Booking` model)
- Token-based user authentication (registration, login, tokens) via Djoser
- A protected example endpoint (`/restaurant/menu/message/`) requiring authentication
- A basic landing page (`templates/index.html`)

## Getting started

### Requirements

- Python 3.9+
- MySQL (or MariaDB) server running locally
- `mysqlclient` needs MySQL's dev headers to build — on Ubuntu/Debian: `sudo apt install default-libmysqlclient-dev build-essential pkg-config`

### Setup

1. **Clone the repo:**
   ```bash
   git clone https://github.com/<your-username>/little-lemon.git
   cd little-lemon
   ```

2. **Create a virtual environment and install dependencies.** There was no `requirements.txt` bundled with the original project, so one has been added here based on the packages the code actually imports:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Create the database:**
   ```sql
   CREATE DATABASE littlelemoncapstone;
   ```

4. **Set your database credentials.** `littlelemon/settings.py` currently has a placeholder password:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'littlelemoncapstone',
           'USER': 'root',
           'PASSWORD': 'xxxxxxxxxx',
           'HOST': '127.0.0.1',
           'PORT': '3306',
           ...
       }
   }
   ```
   Update `USER`/`PASSWORD` to match your local MySQL setup before running the app. (See [Notes](#notes) below — this is worth moving to an environment variable.)

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create an admin user** (needed to log into `/admin/` and to obtain an auth token for the protected endpoints):
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the dev server:**
   ```bash
   python manage.py runserver
   ```

8. **Visit the app:**
   - `http://127.0.0.1:8000/` — landing page
   - `http://127.0.0.1:8000/admin/` — Django admin
   - `http://127.0.0.1:8000/restaurant/menu/items/` — menu API (browsable DRF UI)
   - `http://127.0.0.1:8000/restaurant/booking/tables/` — booking API
   - `http://127.0.0.1:8000/auth/token/login/` — obtain an auth token (Djoser)

### Running tests

```bash
python manage.py test
```

## Project structure

```
├── littlelemon/            # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py / asgi.py
├── restaurant/              # main app
│   ├── models.py            # Menu, Booking
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── tests/
│   └── static/               # images, css
├── templates/index.html     # landing page
├── manage.py
├── requirements.txt          # added for setup
└── .gitignore                 # added: keeps venv/pycache/db files out of git
```

## Notes

This is an early project I'm showcasing as-is, so a couple of things are worth flagging honestly:

- **Fixed:** `test_views.py`'s `test_getall` called a nonexistent `self.loginAsTestUser()`, and the actual `login()` helper used credentials that didn't match the user created in `setUp`. It now logs in with the right user and passes.
- **Fixed:** `test_models.py`'s `test_get_all` compared against a `QuerySet` repr that was missing a closing `>`, so it always failed. Corrected the expected string.
- **Not yet fixed:** `settings.py` still hardcodes `SECRET_KEY` and a placeholder DB password, and runs with `DEBUG = True`. Fine for a local dev capstone, but the first things to move to environment variables before this went anywhere near production.

Running `python manage.py test` now passes all 3 tests cleanly.
