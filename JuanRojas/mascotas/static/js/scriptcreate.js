$(function () {
  $("#formulario").validate({
    rules: {
      idProducto: "required",
      nombreProducto: "required",
      descripcionProducto: "required",
      precioProducto: "required",
      categoriaProducto: "required",
      imagenProducto: "required",
    },
    messages: {
      idProducto: {
        required: "Ingrese el id del producto",
      },
      nombreProducto: {
        required: "Ingrese el nombre del producto",
      },
      descripcionProducto: {
        required: "Ingrese la descripcion del producto",
      },
      precioProducto: {
        required: "Ingrese el precio del producto",
      },
      categoriaProducto: {
        required: "Ingrese la categoria del producto",
      },
      imagenProducto: {
        required: "Ingrese la imagen del producto",
      },
    },
  });
});
