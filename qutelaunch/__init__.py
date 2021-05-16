from .relevance import get_relevant_urls
from .renderer import Renderer
from .webhistory import WebHistory

__all__ = ["init"]


def init(config, c):
    renderer = Renderer()
    web_history = WebHistory(config.datadir / "history.sqlite")
    relevant_urls = get_relevant_urls(web_history.urls, 20)
    startpage = renderer.render("qutelaunch.html", relevant_urls=relevant_urls)

    with open(config.datadir / "qutelaunch.html", "w") as f:
        print(startpage, file=f)

    c.url.start_pages = str(config.datadir / "qutelaunch.html")
    c.url.default_page = c.url.start_pages
