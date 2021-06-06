from multiprocessing import Process
from time import time
from urllib.parse import urlparse

from flask import Flask
from flask import render_template
from flask import request
from flask import Response


def serve(
    web_history,
    bookmarks,
    list_length,
    color_scheme,
    exclude_regexes,
    recent_timespan,
):
    app = Flask("qutelaunch", static_url_path="")

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
            glob=request.args["query"],
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
            list_length,
            exclude_regexes=exclude_regexes,
            glob=request.args["query"],
        )
        return render_template(
            "column.html",
            header="Most Visited",
            urls=most_visited_urls,
            urlparse=urlparse,
        )

    @app.route("/bookmarks.html")
    def serve_bookmarks():
        bookmarks_urls = bookmarks.get_urls(list_length, glob=request.args["query"])
        return render_template(
            "column.html",
            header="Bookmarks",
            urls=bookmarks_urls,
            urlparse=urlparse,
        )

    Process(target=(lambda: app.run()), daemon=True).start()
