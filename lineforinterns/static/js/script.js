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

document.addEventListener('DOMContentLoaded', function() {
  // เลือกปุ่มปิด
  var closeBtn = document.getElementById('closeBtn');
  // เลือก popup
  var popup = document.getElementById('popup');

  // เมื่อคลิกปุ่มปิด
  closeBtn.addEventListener('click', function() {
    popup.style.display = 'none';
  });

  // แสดง popup และปิดอัตโนมัติภายใน 5 วินาที
  popup.style.display = 'block';
  setTimeout(function() {
    popup.style.display = 'none';
  }, 5000); // 5000 มีความหมายว่าปิดหลังจาก 5 วินาที
});