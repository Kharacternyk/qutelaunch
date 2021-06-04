from .color_scheme import ColorScheme
from .httpd import serve

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
    history_path = config.datadir / "history.sqlite"
    bookmarks_path = config.configdir / "bookmarks" / "urls"

    c.url.start_pages = "http://127.0.0.1:5000/index.html"
    c.url.default_page = "http://127.0.0.1:5000/index.html"

    serve(
        history_path,
        bookmarks_path,
        list_length,
        color_scheme,
        exclude_patterns,
        recent_timespan,
    )
