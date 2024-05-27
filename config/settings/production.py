import os
from .base import *

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS")

SECRET_KEY = os.environ.get("SECRET_KEY")

DATABASE_ENGINE = os.environ.get("DATABASE_ENGINE")

if DATABASE_ENGINE == "POSTGRESQL":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "HOST": os.environ.get("POSTGRESQL_HOST"),
            "NAME": os.environ.get("POSTGRESQL_NAME"),
            "USER": os.environ.get("POSTGRESQL_USER"),
            "PASSWORD": os.environ.get("POSTGRESQL_PASSWORD"),
            "PORT": os.environ.get("POSTGRESQL_PORT"),

        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3")
        }
    }


SECURE_HSTS_SECONDS = 2592000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

ENVIRONMENT_NAME = "Production server"
ENVIRONMENT_COLOR = "#FF2222"


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
