from django.urls import path
from .views import *

app_name = "app"


urlpatterns = [
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('category/add/', category_add, name='category_add'),
    path('category/<int:id>/', category_edit, name='category_edit')
]
