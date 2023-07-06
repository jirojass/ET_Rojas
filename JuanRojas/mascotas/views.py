from django.shortcuts import render, redirect
from .models import Producto, Boleta, DetalleBoleta
from .forms import productoForm, RegistroUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from mascotas.compras import Carrito
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def gallery(request):
    return render(request, "gallery.html")


def contact(request):
    return render(request, "contact.html")


@staff_member_required(login_url="/accounts/login/")
def list(request):
    productos = Producto.objects.all()
    datos = {"productos": productos}
    return render(request, "list.html", datos)


@staff_member_required(login_url="/accounts/login/")
def create(request):
    if request.method == "POST":
        productoform = productoForm(request.POST, request.FILES)
        if productoform.is_valid():
            productoform.save()
            return redirect("create")
    else:
        productoform = productoForm()
    return render(request, "create.html", {"producto_form": productoform})


@staff_member_required(login_url="/accounts/login/")
def modify(request, id):
    producto = Producto.objects.get(idProducto=id)
    datos = {"form": productoForm(instance=producto)}
    if request.method == "POST":
        formulario = productoForm(
            data=request.POST, instance=producto, files=request.FILES
        )
        if formulario.is_valid:
            formulario.save()
            return redirect("list")
    return render(request, "modify.html", datos)


@staff_member_required(login_url="/accounts/login/")
def delete(request, id):
    productoEliminado = Producto.objects.get(idProducto=id)
    productoEliminado.delete()
    return redirect("create")


def registrar(request):
    data = {"form": RegistroUserForm()}
    if request.method == "POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data["username"],
                password=formulario.cleaned_data["password1"],
            )
            login(request, user)
            return redirect("index")
        data["form"] = formulario
    return render(request, "registration/registrar.html", data)


def products(request):
    productos = Producto.objects.all()
    datos = {"productos": productos}
    return render(request, "products.html", datos)


def agregar_producto(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito.agregar(producto=producto)
    return redirect("products")


def eliminar_producto(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito.eliminar(producto=producto)
    return redirect("products")


def restar_producto(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito.restar(producto=producto)
    return redirect("products")


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("products")


@login_required
def generarBoleta(request):
    precio_total = 0
    detalles = {}
    iva = 0.19
    envio = 3000
    for key, value in request.session["carrito"].items():
        precio_total += int(value["precio"]) * int(value["cantidad"])
        producto = Producto.objects.get(idProducto=value["producto_id"])
        cant = value["cantidad"]
        subtotal = cant * int(value["precio"])
        detalle = DetalleBoleta(idProducto=producto, cantidad=cant, subtotal=subtotal)
        detalles[producto.idProducto] = detalle
        producto.stockProducto -= cant
        producto.save()

    precio_iva = precio_total * iva
    boleta = Boleta(
        totalBoleta=int(precio_total + (precio_total * iva) + envio),
        idCliente=User.objects.get(id=request.user.id),
        estado="procesando",
    )
    boleta.save()
    productos = []
    for key, value in detalles.items():
        value.idBoleta = boleta
        value.save()
        productos.append(value)
    datos = {
        "productos": productos,
        "fecha": boleta.fechaBoleta,
        "total": boleta.totalBoleta,
        "estado": boleta.get_estado_display(),
        "iva": int(precio_iva),
        "envio": envio,
    }
    request.session["boleta"] = boleta.idBoleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, "detallecarrito.html", datos)


def paginacion(request):
    productos = Producto.objects.all()
    paginator = Paginator(productos, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "products.html", {"page_obj": page_obj})
