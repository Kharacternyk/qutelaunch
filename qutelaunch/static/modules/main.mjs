import fetchColumns from "./fetchColumns.mjs";
import loopElement from "./loopElement.mjs";
import QueryContainer from "./queryContainer.mjs";
import { nthOrLastChild } from "./utils.mjs";

fetchColumns();

const queryContainer = new QueryContainer("query-container");

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
    } else if (queryContainer.handleKey(event.key)){
        event.preventDefault();
        fetchColumns(queryContainer.query);
    }
});
