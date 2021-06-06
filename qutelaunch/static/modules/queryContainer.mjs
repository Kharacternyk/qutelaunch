export default class QueryContainer {
    constructor(elementId) {
        this.element = document.getElementById(elementId);
        this.query = this.element.textContent = "";
    }

    sync() {
        this.element.textContent = this.query
    }

    appendAsterisk() {
        if (this.query.length > 0 && this.query.slice(-1) !== "*") {
            this.query += "*";
            this.sync();
        }
        return false;
    }

    appendKey(key) {
        if (key === "*") {
            return this.appendAsterix();
        }
        this.query += key;
        this.sync();
        return true;
    }

    backspace() {
        if (this.query.length > 0) {
            const result = this.query.slice(-1) !== "*";
            this.query = this.query.slice(0, -1);
            this.sync();
            return result;
        }
        return false;
    }

    handleKey(key) {
        if (key === "Backspace") {
            return this.backspace();
        }
        if (key === " ") {
            return this.appendAsterisk();
        }
        if (key.length === 1) {
            return this.appendKey(key);
        }
        return false;
    }
}
