import os
from pathlib import Path

from dotenv import load_dotenv

from ._installed_apps import INSTALLED_APPS
from ._middleware import MIDDLEWARE
from ._templates import TEMPLATES
from ._auth_password_validators import AUTH_PASSWORD_VALIDATORS

load_dotenv()

DEBUG = os.environ.get("DEBUG")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ENVIRONMENT_SHOW_TO_UNAUTHENTICATED = True
ROOT_URLCONF = "config.urls"

INSTALLED_APPS = INSTALLED_APPS
MIDDLEWARE = MIDDLEWARE
TEMPLATES = TEMPLATES
WSGI_APPLICATION = "config.wsgi.application"
AUTH_PASSWORD_VALIDATORS = AUTH_PASSWORD_VALIDATORS
INTERNAL_IPS = os.environ.get("INTERNAL_IPS").split(",")

LANGUAGE_CODE = "de-de"
TIME_ZONE= "Europe/Berlin"
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DJANGORESIZED_DEFAULT_SIZE = [1280, 720]
DJANGORESIZED_DEFAULT_QUALITY = 75
DJANGORESIZED_DEFAULT_KEEP_META = True
DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'JPEG'
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'JPEG': ".jpg"}
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True
