/* =====================================================
   Foodie Restaurant
   Global JavaScript
===================================================== */

"use strict";

/* ==========================================
   DOM Ready
========================================== */

document.addEventListener("DOMContentLoaded", function () {

    initializeNavbar();

    initializeScrollButton();

    initializeAnimations();

    initializeTooltips();

});


/* ==========================================
   Navbar Effect
========================================== */

function initializeNavbar() {

    const navbar = document.querySelector(".custom-navbar");

    if (!navbar) return;

    window.addEventListener("scroll", function () {

        if (window.scrollY > 50) {

            navbar.style.background =
                "rgba(15,23,42,.95)";

            navbar.style.boxShadow =
                "0 8px 30px rgba(0,0,0,.25)";

        } else {

            navbar.style.background =
                "rgba(15,23,42,.75)";

            navbar.style.boxShadow = "none";

        }

    });

}


/* ==========================================
   Scroll To Top
========================================== */

function initializeScrollButton() {

    const button = document.getElementById("scrollTopBtn");

    if (!button) return;

    window.addEventListener("scroll", function () {

        if (window.scrollY > 300) {

            button.style.display = "flex";

        } else {

            button.style.display = "none";

        }

    });

    button.addEventListener("click", function () {

        window.scrollTo({

            top: 0,

            behavior: "smooth"

        });

    });

}


/* ==========================================
   GSAP Animation
========================================== */

function initializeAnimations() {

    if (typeof gsap === "undefined") {

        return;

    }

    gsap.from(".navbar", {

        y: -80,

        opacity: 0,

        duration: 1

    });

    gsap.from(".section-title", {

        y: 40,

        opacity: 0,

        duration: 1,

        stagger: 0.2

    });

    gsap.from(".card", {

        y: 50,

        opacity: 0,

        duration: 0.8,

        stagger: 0.15

    });

}


/* ==========================================
   Bootstrap Tooltips
========================================== */

function initializeTooltips() {

    if (typeof bootstrap === "undefined") {

        return;

    }

    const tooltipTriggerList = [].slice.call(

        document.querySelectorAll(

            '[data-bs-toggle="tooltip"]'

        )

    );

    tooltipTriggerList.map(function (element) {

        return new bootstrap.Tooltip(element);

    });

}


/* ==========================================
   Utility Function
========================================== */

function showToast(message) {

    console.log(message);

}


/* ==========================================
   End
========================================== */