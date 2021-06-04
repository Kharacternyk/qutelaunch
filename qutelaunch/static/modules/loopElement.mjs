class ElementLoopError extends Error {
    constructor(...params) {
        super(...params);
    }
}

export default function loopElement(element, backwards, filter = _ => true) {
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
