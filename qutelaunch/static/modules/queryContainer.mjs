export default class QueryContainer {
    constructor(elementId) {
        this.element = document.getElementById(elementId);
        this.query = this.element.textContent = "";
    }
    sync() {
        this.element.textContent = this.query
    }
    handleKey(key) {
        if (key == "Backspace") {
            this.query = this.query.slice(0, -1);
            this.sync();
            return true;
        }
        if (/^[-a-zA-Z.:\/0-9]$/.test(key)) {
            this.query += key;
            this.sync();
            return true;
        }
        return false;
    }
}
