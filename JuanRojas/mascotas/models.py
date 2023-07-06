from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class categoriaProducto(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="ID de categoria")
    nombreCategoria = models.CharField(
        max_length=50, blank=True, verbose_name="Nombre de categoria"
    )

    def __str__(self):
        return self.nombreCategoria


class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="ID de producto")
    nombreProducto = models.CharField(
        max_length=50, blank=True, verbose_name="Nombre de producto"
    )
    descripcionProducto = models.CharField(
        max_length=50, blank=True, verbose_name="Descripcion de producto"
    )
    precioProducto = models.IntegerField(blank=True, verbose_name="Precio de producto")
    stockProducto = models.IntegerField(blank=True, verbose_name="Stock de producto")
    imagenProducto = models.ImageField(
        upload_to="imagenes", null=True, blank=True, verbose_name="Imagen de producto"
    )
    categoriaProducto = models.ForeignKey(categoriaProducto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreProducto


class Boleta(models.Model):
    idBoleta = models.AutoField(primary_key=True, verbose_name="ID de boleta")
    fechaBoleta = models.DateTimeField(
        blank=False, null=False, verbose_name="Fecha de boleta", default=datetime.now
    )
    totalBoleta = models.BigIntegerField(verbose_name="Total de boleta")
    idCliente = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, verbose_name="ID de cliente"
    )

    ESTADO_CHOICES = [
        ("procesando", "Procesando Pedido"),
        ("enviado", "Pedido Enviado"),
        ("entregado", "Pedido Entregado"),
    ]
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default="procesando",
        verbose_name="Estado de pedido",
    )

    def __str__(self):
        return str(self.idBoleta)


class DetalleBoleta(models.Model):
    idBoleta = models.ForeignKey(
        Boleta, on_delete=models.CASCADE, blank=True, verbose_name="ID de boleta"
    )
    idDetalleBoleta = models.AutoField(
        primary_key=True, verbose_name="ID de detalle de boleta"
    )
    idProducto = models.ForeignKey(
        Producto, on_delete=models.CASCADE, blank=True, verbose_name="ID de producto"
    )
    cantidad = models.IntegerField(verbose_name="Cantidad de producto")
    subtotal = models.BigIntegerField(verbose_name="Subtotal de producto")

    def __str__(self):
        return str(self.idDetalleBoleta)
