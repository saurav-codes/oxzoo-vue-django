import os

from django.http import HttpResponse

PROJECT_NAME = "oxzoo-vue-django"


def greeting(request):
    tag = os.environ.get("GREETING_TAG", "")
    return HttpResponse(
        f"hello world {PROJECT_NAME}_{tag}",
        content_type="text/plain",
    )


def health(request):
    return HttpResponse("ok", content_type="text/plain")
