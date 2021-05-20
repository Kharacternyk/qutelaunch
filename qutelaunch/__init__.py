import re
from time import time

from .bookmarks import Bookmarks
from .color_scheme import ColorScheme
from .renderer import Renderer
from .web_history import WebHistory

__all__ = ["init"]


def init(config, c, *, list_length=20, color_scheme=ColorScheme(), exclude_patterns=()):
    renderer = Renderer()
    web_history = WebHistory(config.datadir / "history.sqlite")
    bookmarks = Bookmarks(config.configdir / "bookmarks" / "urls")

    seconds_in_week = 60 * 60 * 24 * 7
    week_ago = time() - seconds_in_week

    target = str(config.datadir / "qutelaunch.html")
    exclude_regexes = re.compile(re.escape("file://" + target)), *(
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
    )

    with open(config.datadir / "qutelaunch.html", "w") as f:
        print(startpage, file=f)

    c.url.start_pages = target
    c.url.default_page = target
