document.addEventListener("DOMContentLoaded", function () {
  var menuToggle = document.querySelector(".menu-toggle");
  var mainNavigation = document.querySelector(".main-navigation");

  menuToggle.addEventListener("click", function () {
    mainNavigation.classList.toggle("toggled");
  });

  var menuLinks = document.querySelectorAll(".header-menu ul li a");
  menuLinks.forEach(function (link) {
    link.addEventListener("click", function () {
      mainNavigation.classList.remove("toggled");
    });
  });
});

function showAll() {
  var dishes = document.querySelectorAll('.dish-box-wp');
  dishes.forEach(function(dish) {
      dish.style.display = 'block';
  });
}

function showByClass(className) {
  var dishes = document.querySelectorAll('.dish-box-wp');
  dishes.forEach(function(dish) {
      if (dish.classList.contains(className)) {
          dish.style.display = 'block';
      } else {
          dish.style.display = 'none';
      }
  });
}

document.addEventListener("DOMContentLoaded", function () {
  const slider = document.querySelector(".slider");
  const cards = document.querySelectorAll(".card");
  const cardWidth = cards[0].offsetWidth;
  let currentIndex = 0;

  function slide() {
    if (currentIndex === cards.length - 1) {
      currentIndex = 0;
    } else {
      currentIndex++;
    }
    slider.style.transform = `translateX(-${currentIndex * cardWidth}px)`;
  }

  setInterval(slide, 3000); // Cambia el slide cada 3 segundos (3000 milisegundos)
});

/*esta es la configuracion para preseleccionar platillos*/
function mostrarPrecioSeleccionado(input) {
  var contenedor = input.closest(".dish-box-wp"); // Busca el contenedor más cercano con la clase "dish-box-wp"
  var precioSeleccionado = contenedor.querySelector(".precio-seleccionado");

  if (precioSeleccionado) {
    precioSeleccionado.innerText = "Precio: " + input.value + " bs.";
  }
}

function calcularTotalOrden() {
  var total = 0;
  var productos = document.querySelectorAll(".detalle");
  productos.forEach(function (producto) {
    var precio = parseFloat(producto.getAttribute("data-precio"));
    total += precio;
  });
  document.getElementById("totalInput").value = total.toFixed(2);
}

function agregarAlCarrito(nombreProducto, idProducto) {
  var precioSeleccionado = parseFloat(
    document.querySelector('input[name="precio_' + idProducto + '"]:checked').value
  );

  var productoHTML =
    '<li class="detalle producto-' +
    idProducto +
    '" data-precio="' +
    precioSeleccionado +
    '">' +
    " 🍽️: " +
    nombreProducto +
    " || Precio: " +
    precioSeleccionado +
    ' bs <button class="btn btn-danger rounded-circle eliminar-btn" onclick="eliminarProducto(this)"><i class="fas fa-times">X</i></button></li>';

  // Agregar el producto seleccionado a la lista visual
  document
    .getElementById("lista-productos-seleccionados")
    .insertAdjacentHTML("beforeend", productoHTML);

  // Actualizar el valor del campo oculto con los productos seleccionados
  var listaProductosSeleccionados = document.getElementById("productos_seleccionados");
  listaProductosSeleccionados.value +=
    nombreProducto + " - Precio: " + precioSeleccionado + " bs\n";

  // Calcular el total de la orden
  calcularTotalOrden();
}

function eliminarProducto(botonEliminar) {
  var productoHTML = botonEliminar.closest(".detalle");
  var nombreProducto = productoHTML.textContent
    .split(" 🍽️: ")[1]
    .split(" ||")[0];

  // Eliminar el producto de la lista visual
  productoHTML.parentNode.removeChild(productoHTML);

  // Actualizar el valor del campo oculto eliminando el producto de la lista
  var listaProductosSeleccionados = document.getElementById("productos_seleccionados");
  var productosSeleccionados = listaProductosSeleccionados.value;
  var regex = new RegExp(nombreProducto + " - Precio: [0-9.]+ bs\\n");
  listaProductosSeleccionados.value = productosSeleccionados.replace(regex, "");

  // Calcular el total de la orden
  calcularTotalOrden();
}
/*fin*/
