from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    categories = [
        {"id": 1, "name": "cat 1"},
	{"id": 2, "name": "cat 2"},
	{"id": 3, "name": "cat 3"},
	{"id": 4, "name": "cat 4"},
    ]
    return render(request, "app/index.html", {"categories": categories})


def about(request):
    categories = [
        {"id": 1, "name": "cat 1"},
	{"id": 2, "name": "cat 2"},
	{"id": 3, "name": "cat 3"},
	{"id": 4, "name": "cat 4"},
    ]
    return render(request, "app/about.html", {"categories": categories})
