import sqlite3
from collections import Counter
from urllib.parse import urlparse

from qutelaunch.webpage import WebPage


class WebHistory:
    def __init__(self, history_db_path):
        uri = f"file:{history_db_path}?mode=ro"
        self._db = sqlite3.connect(uri, uri=True).cursor()

    @property
    def webpages(self):
        query = "SELECT url FROM history"
        urls = (row[0] for row in self._db.execute(query))
        webpages = Counter()
        for url in urls:
            scheme, netloc, path, params, query, fragment = urlparse(url)
            if not query:
                webpages[WebPage(scheme, netloc, path)] += 1
        return webpages
