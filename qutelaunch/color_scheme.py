from dataclasses import dataclass


@dataclass(frozen=True)
class ColorScheme:
    page_bg: str = "#282828"
    header_fg: str = "#928374"
    url_odd_bg: str = "#3c3836"
    url_odd_fg: str = "#fbf1c7"
    url_even_bg: str = "#504945"
    url_even_fg: str = "#fbf1c7"
    url_focused_bg: str = "#fbf1c7"
    url_focused_fg: str = "#282828"
