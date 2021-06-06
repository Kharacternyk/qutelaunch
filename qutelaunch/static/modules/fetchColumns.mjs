export default function fetchColumns(query) {
    const columnNames = ["recent", "most-visited", "bookmarks"];
    if (query === undefined || query === "") {
        query = "*";
    } else {
        query = "*" + query + "*";
    }
    for (const columnName of columnNames) {
        const target = document.getElementById(columnName);
        fetch(columnName + ".html?query=" + query)
            .then(response => response.text())
            .then(text => {
                target.innerHTML = text;
                if (columnName == "recent") {
                    target.children[1].focus();
                }
            });
    }
}
