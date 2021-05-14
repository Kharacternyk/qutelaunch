from .renderer import Renderer
from .webhistory import WebHistory


def init(c):
    # FIXME
    # c.url.default_page = "/tmp/qutelaunch.py"
    # c.url.start_pages = "/tmp/qutelaunch.py"

    web_history = WebHistory()
    renderer = Renderer()
    most_common_webpages = (
        webpage for webpage, hits in web_history.webpages.most_common(20)
    )
    qutelaunch_html = renderer.render(
        "qutelaunch.html", most_common_webpages=most_common_webpages
    )

    with open("/tmp/qutelaunch.html", "w") as f:
        print(qutelaunch_html, file=f)
