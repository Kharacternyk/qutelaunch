class Bookmarks:
    def __init__(self, bookmarks_list_path):
        self._path = bookmarks_list_path

    @property
    def urls(self):
        # TODO do not read the file if mtime hasn't changed
        with open(self._path, "r") as f:
            for url_and_title in f.read().splitlines():
                yield url_and_title.split()[0]
