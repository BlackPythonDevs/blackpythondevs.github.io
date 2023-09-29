/**
 * Main JS file for BPDev behaviours
 */

// Menu on small screens
let menuToggle = document.querySelectorAll(".menu-toggle");
if (menuToggle) {
  for (let i = 0; i < menuToggle.length; i++) {
    menuToggle[i].addEventListener(
      "click",
      function (e) {
        document.body.classList.toggle("menu--opened");
        e.preventDefault();
      },
      false,
    );
  }
}

function loadLanguage(lang) {
  base_pathname = window.location.pathname.replace(/\/[a-z]+([_-][a-z]+)?\//, "/");
  if (lang === "en") {
    url = base_pathname;
  } else {
    url = "/" + lang + base_pathname;
  }
  window.location.assign(url);
}

$(document).ready(function () {
  $("#language").change(function () {
    loadLanguage($("#language option:selected").val());
  });
});
