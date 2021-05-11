import sqlite3
from collections import Counter
from os import getenv
from urllib.parse import urlparse

import jinja2


class WebHistory:
    def __init__(self, history_db_path: str = None):
        if not history_db_path:
            data_dir = getenv("XDG_DATA_HOME", getenv("HOME") + "/.local/share")
            history_db_path = data_dir + "/qutebrowser/history.sqlite"
        uri = f"file:{history_db_path}?mode=ro"
        self._db = sqlite3.connect(uri, uri=True).cursor()

    @property
    def most_common_domains(self):
        query = "SELECT url FROM history"
        urls = (row[0] for row in self._db.execute(query))
        domains = (urlparse(url).netloc for url in urls)
        domains_counter = Counter(domains)
        return domains_counter


class Renderer:
    def __init__(self, templates_dir_path: str = "."):
        self._jinja = jinja2.Environment(
            loader=jinja2.FileSystemLoader(templates_dir_path)
        )

    def render(self, template_file_name, **kwargs):
        template = self._jinja.get_template(template_file_name)
        result = template.render(**kwargs)
        return result
