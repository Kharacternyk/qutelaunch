class Bookmarks:
    def __init__(self, bookmarks_list_path):
        with open(bookmarks_list_path, "r") as f:
            self._urls = [
                url_and_title.split()[0] for url_and_title in f.read().splitlines()
            ]

    @property
    def urls(self):
        return iter(self._urls)
