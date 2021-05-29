"use strict";

const columns_container = document.getElementById("columns-container");

columns_container.children[0].children[1].focus();

class CycleError extends Error {
    constructor(...params) {
        super(...params);
    }
}

function cycleElement(element, backwards, filter = _ => true) {
    let sibling = element;
    do {
        sibling = backwards ? sibling.previousElementSibling : sibling.nextElementSibling;
    } while (sibling && !filter(sibling));
    if (!sibling) {
        const index = backwards ? element.parentElement.children.length - 1 : 0;
        sibling = element.parentElement.children[index];
    }
    while (sibling && !filter(sibling)) {
        sibling = backwards ? sibling.previousElementSibling : sibling.nextElementSibling;
    }
    if (!sibling) {
        throw new CycleError("Filter did not match any elements");
    }
    return sibling;
}

window.addEventListener("keydown", event => {
    const index = Number(document.activeElement.dataset.index) + 1;
    const is_anchor = element => element.tagName === "A";
    if (event.key === "ArrowDown") {
        event.preventDefault();
        cycleElement(document.activeElement, false, is_anchor).focus();
    } else if (event.key === "ArrowUp") {
        event.preventDefault();
        cycleElement(document.activeElement, true, is_anchor).focus();
    } else if (event.key === "ArrowRight") {
        event.preventDefault();
        cycleElement(document.activeElement.parentElement).children[index].focus();
    } else if (event.key === "ArrowLeft") {
        event.preventDefault();
        cycleElement(document.activeElement.parentElement, true).children[index].focus();
    }
});
