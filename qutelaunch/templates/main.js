"use strict";

const columns_container = document.getElementById("columns-container");

columns_container.children[0].children[1].focus();

class ElementLoopError extends Error {
    constructor(...params) {
        super(...params);
    }
}

function loopElement(element, backwards, filter = _ => true) {
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
        throw new ElementLoopError("Filter did not match any elements");
    }
    return sibling;
}

function nthOrLastChild(element, n) {
    const length = element.children.length;
    const child = n < length ? element.children[n] : element.children[length - 1];
    return child;
}

window.addEventListener("keydown", event => {
    const index = Number(document.activeElement.dataset.index) + 1;
    const is_anchor = element => element.tagName === "A";
    const handler = {
        ArrowDown: () => loopElement(document.activeElement, false, is_anchor).focus(),
        ArrowUp: () => loopElement(document.activeElement, true, is_anchor).focus(),
        ArrowRight: () => {
            const column = loopElement(document.activeElement.parentElement)
            nthOrLastChild(column, index).focus();
        },
        ArrowLeft: () => {
            const column = loopElement(document.activeElement.parentElement, true)
            nthOrLastChild(column, index).focus();
        },
    }[event.key];
    if (handler) {
        event.preventDefault();
        handler();
    }
});
