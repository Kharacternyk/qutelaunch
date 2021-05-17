import sqlite3


class WebHistory:
    def __init__(self, history_db_path):
        uri = f"file:{history_db_path}?mode=ro"
        self._db = sqlite3.connect(uri, uri=True).cursor()

    @property
    def urls(self):
        query = "SELECT url FROM history"
        urls = (row[0] for row in self._db.execute(query))
        return urls
