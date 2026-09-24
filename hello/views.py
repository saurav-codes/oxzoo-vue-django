import os

from django.http import HttpResponse

from hello.models import Heartbeat

PROJECT_NAME = "oxzoo-vue-django"


def greeting(request):
    tag = os.environ.get("GREETING_TAG", "")
    return HttpResponse(
        f"hello world {PROJECT_NAME}_{tag}",
        content_type="text/plain",
    )


def health(request):
    return HttpResponse("ok", content_type="text/plain")


def stats(request):
    # The count comes from postgres, so this line proves the database path works.
    return HttpResponse(
        f"beats={Heartbeat.objects.count()}",
        content_type="text/plain",
    )
