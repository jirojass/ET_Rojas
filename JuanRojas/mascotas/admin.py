from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Producto)
admin.site.register(models.categoriaProducto)
admin.site.register(models.Boleta)
admin.site.register(models.DetalleBoleta)