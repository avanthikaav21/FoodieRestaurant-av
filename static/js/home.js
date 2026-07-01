/* =====================================================
   FOODIE RESTAURANT - HOME PAGE JS
===================================================== */

"use strict";

/* =========================
   GSAP HERO ANIMATION
========================= */

document.addEventListener("DOMContentLoaded", function () {

    if (typeof gsap !== "undefined") {

        gsap.from(".hero-title", {

            y: 80,

            opacity: 0,

            duration: 1,

            ease: "power3.out"

        });

        gsap.from(".hero-subtitle", {

            y: 40,

            opacity: 0,

            delay: 0.3,

            duration: 1

        });

        gsap.from(".hero-buttons", {

            y: 30,

            opacity: 0,

            delay: 0.5,

            duration: 1

        });

        gsap.from(".hero-img", {

            scale: 0.8,

            opacity: 0,

            delay: 0.4,

            duration: 1

        });

    }

});

/* =========================
   SCROLL ANIMATIONS
========================= */

window.addEventListener("scroll", function () {

    let cards = document.querySelectorAll(".card");

    cards.forEach((card) => {

        let position = card.getBoundingClientRect().top;

        let screenHeight = window.innerHeight;

        if (position < screenHeight - 100) {

            card.classList.add("fade-up");

        }

    });

});

/* =========================
   BUTTON HOVER EFFECTS
========================= */

const buttons = document.querySelectorAll(".btn");

buttons.forEach(btn => {

    btn.addEventListener("mouseenter", () => {

        btn.style.transform = "translateY(-3px) scale(1.03)";

    });

    btn.addEventListener("mouseleave", () => {

        btn.style.transform = "translateY(0) scale(1)";

    });

});

/* =========================
   SIMPLE COUNTER (Optional use later)
========================= */

function animateCounter(el, target) {

    let count = 0;

    let speed = target / 100;

    let interval = setInterval(() => {

        count += speed;

        if (count >= target) {

            el.innerText = target;

            clearInterval(interval);

        } else {

            el.innerText = Math.floor(count);

        }

    }, 20);

}

/* Example usage (future stats section)
let counter = document.getElementById("ordersCount");
if(counter){
    animateCounter(counter, 5000);
}
*/

/* =========================
   END
========================= */