const columnNames = ["recent", "most-visited", "bookmarks"];

export default function fetchColumns(query) {
    if (query === undefined || query === "") {
        query = "*";
    } else {
        query = "*" + query + "*";
    }
    let promises = [];
    for (const columnName of columnNames) {
        const target = document.getElementById(columnName);
        promises.push(fetch(columnName + ".html?query=" + query)
            .then(response => response.text())
            .then(text => {
                target.innerHTML = text;
                resetFocus();
            })
        );
    }
    Promise.all(promises).then(_ => resetFocus());
}

function resetFocus() {
    for (const columnName of columnNames) {
        const column = document.getElementById(columnName);
        if (column.children.length > 1) {
            column.children[1].focus();
            break;
        }
    }
}
