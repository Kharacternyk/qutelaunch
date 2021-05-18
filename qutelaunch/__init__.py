from .renderer import Renderer
from .web_history import WebHistory

__all__ = ["init"]


def init(config, c, list_length=20):
    renderer = Renderer()
    web_history = WebHistory(config.datadir / "history.sqlite")
    most_visited_urls = web_history.get_most_visited_urls(list_length)
    startpage = renderer.render("qutelaunch.html", most_visited_urls=most_visited_urls)

    with open(config.datadir / "qutelaunch.html", "w") as f:
        print(startpage, file=f)

    c.url.start_pages = str(config.datadir / "qutelaunch.html")
    c.url.default_page = c.url.start_pages
