from .base import *
import os


ALLOWED_HOSTS = ["*"]

SECRET_KEY = "ovi%w*1dr7o+_tol293y^(e@_1q63lso3pci$av@wj_b8we@(g"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3")
    }
}


ENVIRONMENT_NAME = "Developement server"
ENVIRONMENT_COLOR = "#54D71F"

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


INSTALLED_APPS += ["debug_toolbar",]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware",]