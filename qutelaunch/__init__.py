from .bookmarks import Bookmarks
from .color_scheme import ColorScheme
from .httpd import serve
from .web_history import WebHistory

__all__ = ["init", "ColorScheme"]


def init(
    config,
    c,
    *,
    list_length=20,
    color_scheme=ColorScheme(),
    exclude_patterns=(),
    recent_timespan=(60 * 60 * 24 * 7),
    **kwargs,
):
    web_history = WebHistory(config.datadir / "history.sqlite")
    bookmarks = Bookmarks(config.configdir / "bookmarks" / "urls")

    c.url.start_pages = "http://127.0.0.1:5000/index.html"
    c.url.default_page = "http://127.0.0.1:5000/index.html"

    serve(
        web_history,
        bookmarks,
        list_length,
        color_scheme,
        exclude_patterns,
        recent_timespan,
    )
