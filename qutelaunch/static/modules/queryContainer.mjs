export default class QueryContainer {
    constructor(elementId) {
        this.element = document.getElementById(elementId);
        this.query = this.element.textContent = "";
    }
    sync() {
        this.element.textContent = this.query
    }
    handleKey(key) {
        if (key === "Backspace") {
            this.query = this.query.slice(0, -1);
            this.sync();
            return true;
        }
        if (key === " ") {
            this.query += "*";
            this.sync();
            return true;
        }
        if (key.length === 1) {
            this.query += key;
            this.sync();
            return true;
        }
        return false;
    }
}
