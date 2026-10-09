import os
from pathlib import Path

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# Deployments set DJANGO_SECRET_KEY as an ox variable (Generate on the review screen);
# the default keeps local runs working.
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "insecure-example-key")

DEBUG = False

# ox provides PUBLIC_HOST, the address the project serves. ALLOWED_HOSTS
# (comma-separated) overrides it, for example to add a second domain.
ALLOWED_HOSTS = [
    host.strip()
    for host in (
        os.environ.get("ALLOWED_HOSTS")
        or ",".join(filter(None, [os.environ.get("PUBLIC_HOST"), "127.0.0.1", "localhost"]))
    ).split(",")
    if host.strip()
]

INSTALLED_APPS = [
    "hello",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
]

ROOT_URLCONF = "hello.urls"

WSGI_APPLICATION = "hello.wsgi.application"

# DATABASE_URL comes from the postgres service in ox.toml. The sqlite
# fallback is local-dev convenience only: it exists just when DATABASE_URL
# is unset, and ox always sets it.
if os.environ.get("DATABASE_URL"):
    DATABASES = {"default": dj_database_url.parse(os.environ["DATABASE_URL"])}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Broker and result backend ride the project's redis from ox.toml
# (REDIS_URL). CELERY_BROKER_URL overrides for custom setups; the 127.0.0.1
# default covers running a worker on a dev machine without env.
_broker_url = (
    os.environ.get("CELERY_BROKER_URL")
    or os.environ.get("REDIS_URL")
    or "redis://127.0.0.1:6379/0"
)
CELERY_BROKER_URL = _broker_url
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", _broker_url)

# One timer to prove beat runs: the worker repeats this line every 60s and
# /api/stats counts the rows it writes.
CELERY_BEAT_SCHEDULE = {
    "heartbeat-every-60s": {
        "task": "hello.tasks.heartbeat",
        "schedule": 60.0,
    },
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True
