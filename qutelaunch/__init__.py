from .renderer import Renderer
from .webhistory import WebHistory

__all__ = ["init"]


def init(config, c):
    renderer = Renderer()
    web_history = WebHistory(config.datadir / "history.sqlite")
    most_common_webpages = (
        webpage for webpage, hits in web_history.webpages.most_common(20)
    )
    startpage = renderer.render(
        "qutelaunch.html", most_common_webpages=most_common_webpages
    )

    with open(config.datadir / "qutelaunch.html", "w") as f:
        print(startpage, file=f)

    c.url.start_pages = str(config.datadir / "qutelaunch.html")
    c.url.default_page = c.url.start_pages
