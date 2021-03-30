#app에만 대한 url을 관리하는 것
#이걸 나중에 또 myapi의 urls에 연결해줘야 한다

from django.urls import path, include
from .views import helloAPI, printBPM

urlpatterns = [
    path("hello/", helloAPI),
    path("bpm/", printBPM),
]