export default function fetchColumns() {
    const columnNames = ["recent", "most-visited", "bookmarks"];
    for (const columnName of columnNames) {
        const target = document.getElementById(columnName);
        fetch(columnName + ".html")
            .then(response => response.text())
            .then(text => {
                target.innerHTML = text;
                if (columnName == "recent") {
                    target.children[1].focus();
                }
            });
    }
}
