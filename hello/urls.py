from django.urls import path

from hello import views

urlpatterns = [
    path("api/greeting", views.greeting),
    path("api/stats", views.stats),
    path("health", views.health),
]
