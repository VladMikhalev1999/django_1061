from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from app.models import Category


def index(request):
    categories = Category.objects.all()
    if request.method == "POST":
        id = request.POST.get("id")
        try:
            c = categories.get(pk=id)
            c.delete()
        except:
            return render(request, "app/index.html", {"cate": categories, "errors": {"delete": f"Категория {id} не найдена."}})
    return render(request, "app/index.html", {"cate": categories})


def about(request):
    return render(request, "app/about.html")


def category_add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name == "":
            return render(request, "app/category_create.html", {"name": name, "errors": {"name": "Поле наименование не может быть пустым."}})
        try:
            c = Category()
            c.name = name
            c.save()
            return redirect("app:index")
        except:
            return render(request, "app/category_create.html", {"name": name, "errors": {"name": "Такая категория уже существует."}})
    return render(request, "app/category_create.html")


def category_edit(request, id):
    try:
        c = Category.objects.get(pk=id)
    except:
        return redirect("app:category_add")
    if request.method == "POST":
        name = request.POST.get("name")
        if name == "":
            return render(request, "app/category_create.html",
                          {"cat": c, "name": name, "errors": {"name": "Поле наименование не может быть пустым."}})
        try:
            c.name = name
            c.save()
            return redirect("app:index")
        except:
            return render(request, "app/category_create.html",
                          {"cat": c, "name": name, "errors": {"name": "Такая категория уже существует."}})
    return render(request, "app/category_create.html", {"cat": c})
