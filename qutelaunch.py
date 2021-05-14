#!/usr/bin/env python
import sqlite3
from collections import Counter
from dataclasses import dataclass
from os import getenv
from urllib.parse import urlparse
from urllib.parse import urlunparse

import jinja2


@dataclass(frozen=True)
class WebPage:
    scheme: str
    netloc: str
    path: str

    @property
    def url(self):
        blocks = (self.scheme, self.netloc, self.path, "", "", "")
        return urlunparse(blocks)


class WebHistory:
    def __init__(self, history_db_path: str = None):
        if not history_db_path:
            data_dir = getenv("XDG_DATA_HOME", getenv("HOME") + "/.local/share")
            history_db_path = data_dir + "/qutebrowser/history.sqlite"
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


class Renderer:
    def __init__(self, templates_dir_path: str = "."):
        self._jinja = jinja2.Environment(
            loader=jinja2.FileSystemLoader(templates_dir_path)
        )

    def render(self, template_file_name, **kwargs):
        template = self._jinja.get_template(template_file_name)
        result = template.render(**kwargs)
        return result


def main():
    web_history = WebHistory()
    renderer = Renderer()
    most_common_webpages = (
        webpage for webpage, hits in web_history.webpages.most_common(20)
    )
    qutelaunch_html = renderer.render(
        "qutelaunch.html", most_common_webpages=most_common_webpages
    )
    print(qutelaunch_html)


if __name__ == "__main__":
    main()
