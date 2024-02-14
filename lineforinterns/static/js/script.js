let navbar = document.querySelector(".header .flex .navbar");

document.querySelector("#menu-btn").onclick = () => {
  navbar.classList.toggle("active");
};

window.onscroll = () => {
  navbar.classList.remove("active");
};

document.querySelectorAll('input[type="number"]').forEach((inputNumber) => {
  inputNumber.oninput = () => {
    if (inputNumber.value.length > inputNumber.maxLength)
      inputNumber.value = inputNumber.value.slice(0, inputNumber.maxLength);
  };
});

// Open the pop-up
function openPopup() {
  document.getElementById("popup").style.display = "block";
}

// Close the pop-up when the close button is clicked
function closePopup() {
  document.getElementById("popup").style.display = "none";
}

// Close the pop-up when clicking outside of it
window.onclick = function (event) {
  var popup = document.getElementById("popup");
  if (event.target == popup) {
    popup.style.display = "none";
  }
};
