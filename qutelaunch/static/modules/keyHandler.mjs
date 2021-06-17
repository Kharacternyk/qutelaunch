export default class KeyHandler {
    constructor() {
        this.handlers = [];
        this.defaultHandler = event => event;
    }
    addHandler(callback, key, shift=false, control=false) {
        this.handlers.append({
            callback: callback,
            key: key,
            shift: shift,
            control: control,
        });
    }
    handle(event) {
        for (handler of this.handlers) {
            if (handler.key && handler.key !== event.key) {
                continue;
            }
            if (handler.test && !handler.test(event.key) 
        
