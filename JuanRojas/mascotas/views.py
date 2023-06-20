from django.shortcuts import render, redirect
from .models import Producto
from .forms import productoForm, RegistroUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def gallery(request):
    return render(request, "gallery.html")


def contact(request):
    return render(request, "contact.html")

@login_required
def list(request):
    productos = Producto.objects.all()
    datos = {'productos': productos}
    return render(request, 'list.html', datos)

@login_required
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
@login_required
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
@login_required
def delete(request, id):
    productoEliminado = Producto.objects.get(idProducto=id)
    productoEliminado.delete()
    return redirect ('create')

def registrar(request):
    data={
        'form':RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], 
                    password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect ('index')
        data["form"] = formulario
    return render(request, 'registration/registrar.html',data)

def products(request):
    productos = Producto.objects.all()
    datos={
        'productos': productos
    }
    return render(request,'products.html',datos)