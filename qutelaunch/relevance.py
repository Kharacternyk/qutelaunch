from collections import Counter
from urllib.parse import urlparse


def get_relevant_urls(url_strings, n):
    counter = Counter()
    for url_string in url_strings:
        url = urlparse(url_string)
        if not url.query:
            counter[url] += 1
    n_most_relevant = (url for url, hits in counter.most_common(n))
    return n_most_relevant
