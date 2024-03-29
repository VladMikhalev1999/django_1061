from django.urls import path
from .views import *

app_name = "app"


urlpatterns = [
    path('index/', index, name='index'),
    path('about/', about, name='about')
]