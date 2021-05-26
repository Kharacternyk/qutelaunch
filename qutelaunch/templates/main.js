"use strict";

window.addEventListener("keydown", event => {
    if (event.key === "ArrowDown") {
        event.preventDefault();
        /* FIXME */
        document
            .activeElement
            .parentElement
            .parentElement
            .nextElementSibling
            .children[0]
            .children[0]
            .focus();
    } else if (event.key === "ArrowUp") {
        event.preventDefault();
        /* FIXME */
        document
            .activeElement
            .parentElement
            .parentElement
            .previousElementSibling
            .children[0]
            .children[0]
            .focus();
    }
});
