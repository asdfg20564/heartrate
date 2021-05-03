from django.urls import path, include
from .views import printLOG, printCUR

urlpatterns = [
    path("log/", printLOG),
    path("cur/", printCUR),
]