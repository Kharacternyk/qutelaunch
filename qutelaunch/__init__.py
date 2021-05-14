from .pathmanager import PathManager
from .renderer import Renderer
from .webhistory import WebHistory


def init(c):
    path_manager = PathManager()
    renderer = Renderer()
    web_history = WebHistory(path_manager)
    most_common_webpages = (
        webpage for webpage, hits in web_history.webpages.most_common(20)
    )
    startpage = renderer.render(
        "startpage.html", most_common_webpages=most_common_webpages
    )

    with open(path_manager.qutelaunch_startpage, "w") as f:
        print(startpage, file=f)

    c.url.default_page = path_manager.qutelaunch_startpage
    c.url.start_pages = path_manager.qutelaunch_startpage
