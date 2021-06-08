const card = document.querySelector(".card");
const container = document.querySelector(".container");

const title = document.querySelector(".title");
const sneaker = document.querySelector(".sneaker img");
const purchase = document.querySelector(".purchase");
const description = document.querySelector(".info h3");
const sizes = document.querySelector(".sizes");

container.addEventListener("mousemove", (e) => {
  let xAxis = (window.innerWidth / 2 - e.pageX) / 25;
  let yAxis = (window.innerHeight / 2 - e.pageY) / 25;
  card.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
});

//Animate In
container.addEventListener("mouseenter", (e) => {
  card.style.transition = "none";
  //Popout se mueve el titulo hacia la derecha 150px cuando entramos con el mouse a card
  title.style.transform = "translateZ(150px)";
  //sneaker contenedor de imagen + circulo
  sneaker.style.transform = "translateZ(200px) rotateZ(-45deg)";
  //description
  description.style.transform = "translateZ(125px)";
  //sizes
  sizes.style.transform = "translateZ(100px)";
  //purchase Button
  purchase.style.transform = "translateZ(75px)";
});

//Animate Out
//cuando el mouse se retira ocurre lo siguiente:
container.addEventListener("mouseleave", (e) => {
  card.style.transition = "all 0.5s ease";
  card.style.transform = `rotateY(0deg) rotateX(0deg)`;
  // Popback - cuando sale del card el titulo vuelve a cero
  title.style.transform = "translateZ(0px)";
  //sneaker contenedor de imagen + circulo
  sneaker.style.transform = "translateZ(0px) rotateZ(0deg)";
  //description
  description.style.transform = "translateZ(0px)";
  //sizes
  sizes.style.transform = "translateZ(0px)";
  //purchase Button
  purchase.style.transform = "translateZ(0px)";
});

function addToField(c) {
  document.getElementById('input1').value += c;
};
