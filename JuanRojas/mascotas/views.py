from django.shortcuts import render, redirect
from .models import Producto
from .forms import productoForm

# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def gallery(request):
    return render(request, "gallery.html")


def contact(request):
    return render(request, "contact.html")


def create(request):
    if request.method == "POST":
        productoform = productoForm(
            request.POST, request.FILES
        )
        if productoform.is_valid():
            productoform.save()
            return redirect("create")
    else:
        productoform = productoForm()
    return render(request, "crear.html", {"producto_form": productoform})
