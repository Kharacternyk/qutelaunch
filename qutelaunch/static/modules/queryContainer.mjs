export default class QueryContainer {
    constructor(elementId, callback) {
        this.element = document.getElementById(elementId);
        this.query = this.element.textContent = "";
        this.callback = callback;
    }
    //logically 
    sync(queryLogicallyChanged=true) {
        this.element.textContent = this.query
    }
    appendAsterisk() {
        if (this.query.length > 0 && this.query.slice(-1) !== "*") {
            this.query += "*";
            this.sync();
        }
    }
    appendCharacter(key) {
        if (key === "*") {
            this.appendAsterix();
        } else {
            this.query += key;
            this.sync();
            this.callback();
        }
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
