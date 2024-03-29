from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import Category


def index(request):
    categories = Category.objects.all()
    """
        select * from app_category where id > 1
    """
    return render(request, "app/index.html", {"cate": categories})


def about(request):
    return render(request, "app/about.html")
