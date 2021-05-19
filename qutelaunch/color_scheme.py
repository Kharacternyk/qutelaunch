from dataclasses import dataclass


@dataclass(frozen=True)
class ColorScheme:
    background: str = "#282828"
    foreground: str = "#fbf1c7"
