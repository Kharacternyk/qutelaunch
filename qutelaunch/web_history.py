import sqlite3


class WebHistory:
    def __init__(self, history_db_path):
        self._uri = f"file:{history_db_path}?mode=ro"

    @property
    def _db(self):
        return sqlite3.connect(self._uri, uri=True).cursor()

    def get_most_visited_urls(self, n, *, glob="*", exclude_globs=(), since=0):
        query = """
            SELECT url
            FROM history
            WHERE atime > ?
            AND url GLOB ?
        """
        query += "AND url NOT GLOB ?" * len(exclude_globs)
        query += """
            GROUP BY url
            ORDER BY COUNT(url) DESC
            LIMIT ?
        """
        sql_parameters = since, glob, *exclude_globs, n
        urls = (row[0] for row in self._db.execute(query, sql_parameters))
        return urls
