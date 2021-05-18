from time import time

from .bookmarks import Bookmarks
from .renderer import Renderer
from .web_history import WebHistory

__all__ = ["init"]


def init(config, c, list_length=20):
    renderer = Renderer()
    web_history = WebHistory(config.datadir / "history.sqlite")
    bookmarks = Bookmarks(config.configdir / "bookmarks" / "urls")

    seconds_in_week = 60 * 60 * 24 * 7
    week_ago = time() - seconds_in_week
    most_visited_urls = web_history.get_most_visited_urls(list_length)
    weekly_highlights_urls = web_history.get_most_visited_urls(
        list_length, newer_than=week_ago
    )

    startpage = renderer.render(
        "qutelaunch.html",
        most_visited_urls=most_visited_urls,
        weekly_highlights_urls=weekly_highlights_urls,
        bookmarks_urls=bookmarks.urls,
    )

    with open(config.datadir / "qutelaunch.html", "w") as f:
        print(startpage, file=f)

    c.url.start_pages = str(config.datadir / "qutelaunch.html")
    c.url.default_page = c.url.start_pages
