export function nthOrLastChild(element, n) {
    const length = element.children.length;
    const child = n < length ? element.children[n] : element.children[length - 1];
    return child;
}
