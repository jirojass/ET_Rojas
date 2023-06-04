from django import forms
from .models import Producto


class productoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            "idProducto",
            "nombreProducto",
            "descripcionProducto",
            "precioProducto",
            "imagenProducto",
            "categoriaProducto",
        ]
        labels = {
            "idProducto": "ID de producto",
            "nombreProducto": "Nombre de producto",
            "descripcionProducto": "Descripcion de producto",
            "precioProducto": "Precio de producto",
            "imagenProducto": "Imagen de producto",
            "categoriaProducto": "Categoria de producto",
        }
        widgets = {
            "idProducto": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese ID de producto..",
                    "id": "idProducto",
                    "class": "form-control",
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
            "precioProducto": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese precio de producto..",
                    "id": "precioProducto",
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
