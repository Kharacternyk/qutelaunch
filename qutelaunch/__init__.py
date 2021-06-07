import logging

from .bookmarks import Bookmarks
from .color_scheme import ColorScheme
from .httpd import serve
from .web_history import WebHistory

__all__ = ["init", "ColorScheme"]


def init(
    config,
    c,
    *,
    port=42512,
    list_length=20,
    color_scheme=ColorScheme(),
    exclude_globs=(),
    recent_timespan=(60 * 60 * 24 * 7),
    **kwargs,
):
    web_history = WebHistory(config.datadir / "history.sqlite")
    bookmarks = Bookmarks(config.configdir / "bookmarks" / "urls")

    logging.getLogger("werkzeug").disabled = True

    c.url.start_pages = f"http://127.0.0.1:{port}/index.html"
    c.url.default_page = c.url.start_pages

    serve(
        port,
        web_history,
        bookmarks,
        list_length,
        color_scheme,
        exclude_globs,
        recent_timespan,
    )
