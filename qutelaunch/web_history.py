import sqlite3
from collections import Counter


class WebHistory:
    def __init__(self, history_db_path):
        self._uri = f"file:{history_db_path}?mode=ro"

    @property
    def _db(self):
        return sqlite3.connect(self._uri, uri=True).cursor()

    def get_most_visited_urls(self, n, *, exclude_regexes=(), since=0, glob="*"):
        query = """
            SELECT url
            FROM history
            WHERE atime > ?
            AND url GLOB ?
        """
        urls = (row[0] for row in self._db.execute(query, (since, glob)))
        counter = Counter()
        for url in urls:
            if not any(regex.fullmatch(url) for regex in exclude_regexes):
                counter[url] += 1
        n_most_visited = (url for url, hits in counter.most_common(n))
        return n_most_visited
