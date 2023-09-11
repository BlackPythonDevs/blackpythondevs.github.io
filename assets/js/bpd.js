/**
 * Main JS file for BPDev behaviours
 */

// Menu on small screens
let menuToggle = document.querySelectorAll('.menu-toggle');
if (menuToggle) {
    for (let i = 0; i < menuToggle.length; i++) {
        menuToggle[i].addEventListener('click', function (e) {
            document.body.classList.toggle('menu--opened');
            e.preventDefault();
        }, false);
    }
}
;