from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class productoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            "idProducto",
            "nombreProducto",
            "descripcionProducto",
            "precioProducto",
            "stockProducto",
            "imagenProducto",
            "categoriaProducto",
        ]
        labels = {
            "idProducto": "ID de producto",
            "nombreProducto": "Nombre de producto",
            "descripcionProducto": "Descripcion de producto",
            "precioProducto": "Precio de producto",
            "stockProducto": "Stock de producto",
            "imagenProducto": "Imagen de producto",
            "categoriaProducto": "Categoria de producto",
        }
        widgets = {
            "idProducto": forms.NumberInput(
                attrs={
                    "placeholder": "Ingrese ID de producto..",
                    "id": "idProducto",
                    "class": "form-control",
                    "data-msg-number": "Formato incorrecto",
                }
            ),
            "nombreProducto": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese nombre de producto..",
                    "id": "nombreProducto",
                    "class": "form-control",
                }
            ),
            "descripcionProducto": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese descripción de producto..",
                    "id": "descripcionProducto",
                    "class": "form-control",
                }
            ),
            "precioProducto": forms.NumberInput(
                attrs={
                    "placeholder": "Ingrese precio de producto..",
                    "id": "precioProducto",
                    "class": "form-control",
                }
            ),
            "stockProducto": forms.NumberInput(
                attrs={
                    "placeholder": "Ingrese stock de producto..",
                    "id": "stockProducto",
                    "class": "form-control",
                }
            ),
            "imagenProducto": forms.FileInput(
                attrs={"id": "imagenProducto", "class": "form-control"}
            ),
            "categoriaProducto": forms.Select(
                attrs={"id": "categoriaProducto", "class": "form-control"}
            ),
        }
