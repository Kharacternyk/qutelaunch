import re
from time import time
from urllib.parse import urlparse

from .bookmarks import Bookmarks
from .color_scheme import ColorScheme
from .renderer import Renderer
from .web_history import WebHistory

__all__ = ["init", "ColorScheme"]


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
    """Set qutelaunch.html as the startpage and regenerate the file if needed.

    Args:
        config: The config object provided by Qutebrowser for use in config.py.
        c: The shorthand object provided by Qutebrowser for use in config.py.

    Keyword Args:
        list_length: The length of the "Recent" and "Most Visited" lists.
        color_scheme:
            The color scheme represented as an instance of the ColorScheme dataclass.
        exclude_patterns:
            The RegEx patterns that describe the URLs to exclude from the "Recent" and
            "Most Visited" lists.
        update_timeout: The timeout in seconds that triggers a regeneration of the file.
        recent_timespan:
            The timespan in seconds that defines which URLs can show up in the "Recent"
            list.
    """
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
