from urllib.parse import urlparse


class Bookmarks:
    def __init__(self, bookmarks_list_path):
        with open(bookmarks_list_path, "r") as f:
            self._url_strings = [
                url_title.split()[0] for url_title in f.read().splitlines()
            ]

    @property
    def urls(self):
        urls = (urlparse(url_string) for url_string in self._url_strings)
        return urls
