import logging
import re
from multiprocessing import Process
from time import time
from urllib.parse import urlparse

from flask import Flask
from flask import render_template
from flask import Response

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
    exclude_regexes = (re.compile(pattern) for pattern in exclude_patterns)
    web_history = WebHistory(history_path)
    bookmarks = Bookmarks(bookmarks_path)
    app = Flask("qutelaunch", static_url_path="")
    logging.getLogger("werkzeug").disabled = True

    @app.route("/styles.css")
    def serve_styles():
        return Response(
            render_template("styles.css", color_scheme=color_scheme),
            mimetype="text/css",
        )

    @app.route("/recent.html")
    def serve_recent():
        recent_urls = web_history.get_most_visited_urls(
            list_length,
            exclude_regexes=exclude_regexes,
            since=time() - recent_timespan,
        )
        return render_template(
            "column.html",
            header="Recent",
            urls=recent_urls,
            urlparse=urlparse,
        )

    @app.route("/most-visited.html")
    def serve_most_visited():
        most_visited_urls = web_history.get_most_visited_urls(
            list_length, exclude_regexes=exclude_regexes
        )
        return render_template(
            "column.html",
            header="Most Visited",
            urls=most_visited_urls,
            urlparse=urlparse,
        )

    @app.route("/bookmarks.html")
    def serve_bookmarks():
        return render_template(
            "column.html",
            header="Bookmarks",
            urls=bookmarks.urls,
            urlparse=urlparse,
        )

    Process(target=(lambda: app.run()), daemon=True).start()
