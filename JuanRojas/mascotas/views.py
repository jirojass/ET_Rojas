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

def list(request):
    productos = Producto.objects.all()
    datos = {'productos': productos}
    return render(request, 'list.html', datos)


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
    return render(request, "create.html", {"producto_form": productoform})

def modify(request, id):
    producto = Producto.objects.get(idProducto=id)
    datos = {
        'form': productoForm(instance=producto)
    }
    if request.method=='POST':
        formulario = productoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            return redirect('list')
    return render(request, 'modify.html', datos)

def delete(request, id):
    productoEliminado = Producto.objects.get(idProducto=id)
    productoEliminado.delete()
    return redirect ('create')