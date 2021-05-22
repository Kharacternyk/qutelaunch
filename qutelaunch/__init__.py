import re
from time import time
from urllib.parse import urlparse

from .bookmarks import Bookmarks
from .color_scheme import ColorScheme
from .renderer import Renderer
from .web_history import WebHistory

__all__ = ["init"]


def init(
    config,
    c,
    *,
    list_length=20,
    color_scheme=ColorScheme(),
    exclude_patterns=(),
    update_timeout=(60 * 60 * 24),
    recent_timespan=(60 * 60 * 24 * 7)
):
    renderer = Renderer()
    web_history = WebHistory(config.datadir / "history.sqlite")
    bookmarks = Bookmarks(config.configdir / "bookmarks" / "urls")

    target = config.datadir / "qutelaunch.html"
    c.url.start_pages = str(target)
    c.url.default_page = str(target)

    if not target.exists() or target.stat().st_mtime < time() - update_timeout:
        exclude_regexes = re.compile(re.escape("file://" + str(target))), *(
            re.compile(pattern) for pattern in exclude_patterns
        )
        most_visited_urls = web_history.get_most_visited_urls(
            list_length, exclude_regexes=exclude_regexes
        )
        recent_urls = web_history.get_most_visited_urls(
            list_length,
            exclude_regexes=exclude_regexes,
            newer_than=time() - recent_timespan,
        )

        startpage = renderer.render(
            "qutelaunch.html",
            most_visited_urls=most_visited_urls,
            recent_urls=recent_urls,
            bookmarks_urls=bookmarks.urls,
            color_scheme=color_scheme,
            urlparse=urlparse,
        )

        with open(target, "w") as f:
            print(startpage, file=f)
