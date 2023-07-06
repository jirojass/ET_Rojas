class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def agregar(self, producto):
        if (
            str(producto.idProducto) not in self.carrito.keys()
            and producto.stockProducto > 0
        ):
            self.carrito[str(producto.idProducto)] = {
                "producto_id": str(producto.idProducto),
                "nombre": producto.nombreProducto,
                "precio": str(producto.precioProducto),
                "cantidad": 1,
                "total": producto.precioProducto,
            }
        else:
            for key, value in self.carrito.items():
                if (
                    key == str(producto.idProducto)
                    and producto.stockProducto > value["cantidad"]
                ):
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"] = producto.precioProducto
                    value["total"] = value["total"] + producto.precioProducto
                    break
                else:
                    pass

        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.idProducto)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        for key, value in self.carrito.items():
            if key == str(producto.idProducto) and value["cantidad"] > 0:
                value["cantidad"] = value["cantidad"] - 1
                value["total"] = int(value["total"]) - producto.precioProducto
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break
        self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
