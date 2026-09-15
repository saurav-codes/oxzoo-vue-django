from django.http import HttpResponse
from django.urls import path

from hello import views

urlpatterns = [
    path("api/greeting", views.greeting),
    path("health", views.health),
]
