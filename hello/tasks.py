import os

from celery import shared_task

APP_NAME = "oxzoo-vue-django"


def greeting_line() -> str:
    # Read at task time: GREETING_TAG is runtime env, same as the web view.
    return f"hello world {APP_NAME}_{os.environ.get('GREETING_TAG', 'unknown')}"


@shared_task
def heartbeat():
    # One row per beat tick in postgres; print() lands in the worker journal.
    from .models import Heartbeat

    row = Heartbeat.objects.create(line=greeting_line())
    print(f"heartbeat {row.id}: {row.line}")
    return {"id": row.id, "line": row.line}
