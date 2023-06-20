from django.db import models

# Create your models here.

class categoriaProducto(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="ID de categoria")
    nombreCategoria = models.CharField(max_length=50, blank=True, verbose_name="Nombre de categoria")

    def __str__(self):
        return self.nombreCategoria


class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="ID de producto")
    nombreProducto = models.CharField(max_length=50, blank=True, verbose_name="Nombre de producto")
    descripcionProducto = models.CharField(max_length=50, blank=True, verbose_name="Descripcion de producto")
    precioProducto = models.IntegerField(blank=True, verbose_name="Precio de producto")
    stockProducto = models.IntegerField(blank=True, verbose_name="Stock de producto")
    imagenProducto = models.ImageField(upload_to="imagenes",null=True,blank=True,verbose_name="Imagen de producto")
    categoriaProducto = models.ForeignKey(categoriaProducto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreProducto