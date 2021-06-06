from fnmatch import fnmatch


class Bookmarks:
    def __init__(self, bookmarks_list_path):
        self._path = bookmarks_list_path

    def get_urls(self, n, *, glob="*"):
        # TODO do not read the file if mtime hasn't changed
        with open(self._path, "r") as f:
            for url_and_title in f:
                if n <= 0:
                    break
                url = url_and_title.split()[0]
                if fnmatch(url, glob):
                    n -= 1
                    yield url
