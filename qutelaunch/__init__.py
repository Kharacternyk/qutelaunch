import re
from time import time
from urllib.parse import urlparse

from .bookmarks import Bookmarks
from .color_scheme import ColorScheme
from .renderer import Renderer
from .web_history import WebHistory

__all__ = ["init"]


def init(config, c, *, list_length=20, color_scheme=ColorScheme(), exclude_patterns=()):
    renderer = Renderer()
    web_history = WebHistory(config.datadir / "history.sqlite")
    bookmarks = Bookmarks(config.configdir / "bookmarks" / "urls")

    seconds_in_day = 60 * 60 * 24
    seconds_in_week = seconds_in_day * 7
    now = time()
    day_ago = now - seconds_in_day
    week_ago = now - seconds_in_week

    target = config.datadir / "qutelaunch.html"
    c.url.start_pages = str(target)
    c.url.default_page = str(target)

    if not target.exists() or target.stat().st_mtime < day_ago:
        exclude_regexes = re.compile(re.escape("file://" + str(target))), *(
            re.compile(pattern) for pattern in exclude_patterns
        )
        most_visited_urls = web_history.get_most_visited_urls(
            list_length, exclude_regexes=exclude_regexes
        )
        weekly_highlights_urls = web_history.get_most_visited_urls(
            list_length, exclude_regexes=exclude_regexes, newer_than=week_ago
        )

        startpage = renderer.render(
            "qutelaunch.html",
            most_visited_urls=most_visited_urls,
            weekly_highlights_urls=weekly_highlights_urls,
            bookmarks_urls=bookmarks.urls,
            color_scheme=color_scheme,
            urlparse=urlparse,
        )

        with open(target, "w") as f:
            print(startpage, file=f)
