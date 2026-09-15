import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Real deployments set DJANGO_SECRET_KEY in the ox env editor; the default keeps local runs working.
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "insecure-example-key")

DEBUG = False

ALLOWED_HOSTS = ["vue-django.oxzoo.sorv.dev", "127.0.0.1", "localhost"]

INSTALLED_APPS = []

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
]

ROOT_URLCONF = "hello.urls"

WSGI_APPLICATION = "hello.wsgi.application"

# This example has no models, so no database is configured and no migrate hook is
# needed (a sqlite file would also be unwritable at runtime under the sandbox).
DATABASES = {}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True
