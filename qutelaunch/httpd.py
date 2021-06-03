import re
from multiprocessing import Process
from time import time
from urllib.parse import urlparse

from flask import Flask
from flask import render_template

from .bookmarks import Bookmarks
from .web_history import WebHistory


def serve(
    history_path,
    bookmarks_path,
    list_length,
    color_scheme,
    exclude_patterns,
    recent_timespan,
):
    web_history = WebHistory(history_path)
    bookmarks = Bookmarks(bookmarks_path)

    exclude_regexes = (re.compile(pattern) for pattern in exclude_patterns)
    most_visited_urls = web_history.get_most_visited_urls(
        list_length, exclude_regexes=exclude_regexes
    )
    recent_urls = web_history.get_most_visited_urls(
        list_length,
        exclude_regexes=exclude_regexes,
        since=time() - recent_timespan,
    )

    app = Flask("qutelaunch")

    @app.route("/")
    def startpage():
        return render_template(
            "qutelaunch.html",
            most_visited_urls=most_visited_urls,
            recent_urls=recent_urls,
            bookmarks_urls=bookmarks.urls,
            color_scheme=color_scheme,
            urlparse=urlparse,
        )

    Process(target=(lambda: app.run())).start()
