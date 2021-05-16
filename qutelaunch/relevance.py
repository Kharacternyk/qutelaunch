from collections import Counter
from urllib.parse import urlparse


def get_relevant_urls(urls, n):
    counter = Counter()
    for url in urls:
        parsed = urlparse(url)
        if not parsed.query:
            counter[parsed] += 1
    n_most_relevant = (url for url, hits in counter.most_common(n))
    return n_most_relevant
