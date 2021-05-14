from dataclasses import dataclass
from urllib.parse import urlunparse


@dataclass(frozen=True)
class WebPage:
    scheme: str
    netloc: str
    path: str

    @property
    def url(self):
        blocks = (self.scheme, self.netloc, self.path, "", "", "")
        return urlunparse(blocks)
