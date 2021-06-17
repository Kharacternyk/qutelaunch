import fetchColumns from "./fetchColumns.mjs";
import QueryContainer from "./queryContainer.mjs";
import keyHandler from "./keyHandler.mjs"; 

fetchColumns();

const queryContainer = new QueryContainer("query-container");
const keyHandler = new KeyHandler(queryContainer);

window.addEventListener("keydown", keyHandler.handle);
