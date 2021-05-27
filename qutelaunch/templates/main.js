"use strict";

document.getElementById("recent-column").children[1].focus();

window.addEventListener("keydown", event => {
    if (event.key === "ArrowDown") {
        event.preventDefault();
        document.activeElement.nextElementSibling.focus();
    } else if (event.key === "ArrowUp") {
        event.preventDefault();
        document.activeElement.previousElementSibling.focus();
    }
});
