import sqlite3
from collections import Counter
from urllib.parse import urlparse


class WebHistory:
    def __init__(self, history_db_path):
        uri = f"file:{history_db_path}?mode=ro"
        self._db = sqlite3.connect(uri, uri=True).cursor()

    def get_most_visited_urls(self, n, *, newer_than=0):
        query = "SELECT url FROM history WHERE atime > ?"
        url_strings = (row[0] for row in self._db.execute(query, (newer_than,)))
        counter = Counter()
        for url_string in url_strings:
            url = urlparse(url_string)
            counter[url] += 1
        n_most_visited = (url for url, hits in counter.most_common(n))
        return n_most_visited
