$(function () {
  $("#contacto").validate({
    rules: {
      nom: {
        required: true,
        minlength: 2,
        maxlength: 20,
      },
      edad: {
        required: true,
        number: true,
        min: 18,
        max: 120,
      },
      gen: {
        required: true,
      },
      email: {
        required: true,
        email: true,
      },
      tel: {
        required: true,
        number: true,
        minlength: 8,
        maxlength: 11,
      },
      men: {
        required: true,
        minlength: 10,
        maxlength: 1000,
      },
    },

    messages: {
      nom: {
        required: "Ingrese su nombre",
        minlength: "Caracteres insuficientes (2)",
        maxlength: "Caracteres excedidos (20)",
      },
      edad: {
        required: "Ingrese su edad",
        number: "Formato incorrecto",
        min: "Edad minima 18",
        max: "Edad maxima 120",
      },
      gen: {
        required: "Ingrese su genero",
      },
      email: {
        required: "Ingrese un correo valido",
        email: "Formato incorrecto",
      },
      tel: {
        required: "Ingrese un numero de telefono",
        number: "Formato incorrecto",
        minlength: "Caracteres insuficientes (8)",
        maxlength: "Caracteres excedidos (11)",
      },
      men: {
        required: "Debe ingresar un mensaje",
        minlength: "Caracteres insuficientes (10)",
        maxlength: "Caracteres excedidos (1000)",
      },
    },
  });
});

function Enviar() {
  if ($("#contacto").valid()) {
    alert("Mensaje enviado. Le responderemos a la brevedad");
  } else {
    alert("Mensaje no enviado. Revise los campos");
  }
}

function Limpiar() {
  alert("Formulario limpiado");
}

var button1 = document.querySelector(".btn-primary");
var button2 = document.querySelector(".btn-secondary");

button1.addEventListener("mouseenter", function () {
  button1.style.width = "110px";
  button1.style.height = "50px";
  button1.style.backgroundColor = "#9a92ce";
  button1.style.borderColor = "#9a92ce";

});

button1.addEventListener("mouseleave", function () {
  button1.style.width = "100px";
  button1.style.height = "40px";
  button1.style.backgroundColor = "#aba2e5";
  button1.style.borderColor = "#aba2e5";
});

button2.addEventListener("mouseenter", function () {
  button2.style.width = "110px";
  button2.style.height = "50px";
  button2.style.backgroundColor = "#ce9295";
  button2.style.borderColor = "#ce9295";
});

button2.addEventListener("mouseleave", function () {
  button2.style.width = "100px";
  button2.style.height = "40px";
  button2.style.backgroundColor = "#e5a2a6";
  button2.style.borderColor = "#e5a2a6";
});
