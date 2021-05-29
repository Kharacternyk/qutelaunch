from os import getenv
from time import time

from .color_scheme import ColorScheme
from .write_target import write_target

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
    target = config.datadir / "qutelaunch.html"
    history_path = config.datadir / "history.sqlite"
    bookmarks_path = config.configdir / "bookmarks" / "urls"

    c.url.start_pages = str(target)
    c.url.default_page = str(target)

    if getenv("QUTELAUNCH_DEBUG"):
        update_timeout = 0

    if not target.exists() or target.stat().st_mtime < time() - update_timeout:
        write_target(
            target,
            history_path,
            bookmarks_path,
            list_length,
            color_scheme,
            exclude_patterns,
            recent_timespan,
        )
