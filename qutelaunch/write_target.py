import re
from time import time
from urllib.parse import urlparse

from .bookmarks import Bookmarks
from .renderer import Renderer
from .web_history import WebHistory


def write_target(
    target,
    history_path,
    bookmarks_path,
    list_length,
    color_scheme,
    exclude_patterns,
    recent_timespan,
):
    renderer = Renderer()
    web_history = WebHistory(history_path)
    bookmarks = Bookmarks(bookmarks_path)

    exclude_regexes = re.compile(re.escape("file://" + str(target))), *(
        re.compile(pattern) for pattern in exclude_patterns
    )
    most_visited_urls = web_history.get_most_visited_urls(
        list_length, exclude_regexes=exclude_regexes
    )
    recent_urls = web_history.get_most_visited_urls(
        list_length,
        exclude_regexes=exclude_regexes,
        since=time() - recent_timespan,
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
