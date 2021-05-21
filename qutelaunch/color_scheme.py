from dataclasses import dataclass


@dataclass(frozen=True)
class ColorScheme:
    background: str = "#282828"
    foreground: str = "#fbf1c7"
    section_header: str = "#928374"
    url_background_odd: str = "#3c3836"
    url_background_even: str = "#504945"
