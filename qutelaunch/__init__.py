from .relevance import get_relevant_urls
from .renderer import Renderer
from .web_history import WebHistory

__all__ = ["init"]


def init(config, c, list_length=20):
    renderer = Renderer()
    web_history = WebHistory(config.datadir / "history.sqlite")
    relevant_urls = get_relevant_urls(web_history.url_strings, list_length)
    startpage = renderer.render("qutelaunch.html", relevant_urls=relevant_urls)

    with open(config.datadir / "qutelaunch.html", "w") as f:
        print(startpage, file=f)

    c.url.start_pages = str(config.datadir / "qutelaunch.html")
    c.url.default_page = c.url.start_pages
