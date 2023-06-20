$(function () {
  $("#formulario").validate({
    rules: {
      idProducto: { "required": true, "number": true },
      nombreProducto: "required",
      descripcionProducto: "required",
      precioProducto: {"required": true, "number": true, "min": 0},
      stockProducto: {"required": true, "number": true, "min": 0},
      categoriaProducto: "required",
    },
    messages: {
      idProducto: {
        required: "Ingrese el id del producto",
        number: "Formato incorrecto",
      },
      nombreProducto: {
        required: "Ingrese el nombre del producto",
      },
      descripcionProducto: {
        required: "Ingrese la descripcion del producto",
      },
      precioProducto: {
        required: "Ingrese el precio del producto",
        number: "Formato incorrecto",
      },
      stockProducto: {
        required: "Ingrese el stock del producto",
        number: "Formato incorrecto",
      },
      categoriaProducto: {
        required: "Ingrese la categoria del producto",
      },
    },
  });
});
