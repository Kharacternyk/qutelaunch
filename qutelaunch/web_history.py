import sqlite3
from collections import Counter


class WebHistory:
    def __init__(self, history_db_path):
        uri = f"file:{history_db_path}?mode=ro"
        self._db = sqlite3.connect(uri, uri=True).cursor()

    def get_most_visited_urls(self, n, *, exclude_regexes=(), since=0):
        query = "SELECT url FROM history WHERE atime > ?"
        urls = (row[0] for row in self._db.execute(query, (since,)))
        counter = Counter()
        for url in urls:
            if not any(regex.fullmatch(url) for regex in exclude_regexes):
                counter[url] += 1
        n_most_visited = (url for url, hits in counter.most_common(n))
        return n_most_visited
