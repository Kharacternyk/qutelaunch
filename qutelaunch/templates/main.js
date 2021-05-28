"use strict";

const columns_container = document.getElementById("columns-container");

columns_container.children[0].children[0].focus();

function cycleElement(element, backwards) {
    let sibling = backwards ? element.previousElementSibling : element.nextElementSibling;
    if (!sibling) {
        const index = backwards ? element.parentElement.children.length - 1 : 0;
        sibling = element.parentElement.children[index];
    }
    return sibling;
}

window.addEventListener("keydown", event => {
    if (event.key === "ArrowDown") {
        event.preventDefault();
        cycleElement(document.activeElement).focus();
    } else if (event.key === "ArrowUp") {
        event.preventDefault();
        cycleElement(document.activeElement, true).focus();
    } else if (event.key === "ArrowRight") {
        event.preventDefault();
        const index = Number(document.activeElement.dataset.index);
        cycleElement(document.activeElement.parentElement).children[index].focus();
    } else if (event.key == "ArrowLeft") {
        event.preventDefault();
        const index = Number(document.activeElement.dataset.index);
        cycleElement(document.activeElement.parentElement, true).children[index].focus();
    }
});
