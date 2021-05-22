Qutelaunch is a local startpage for [Qutebrowser](https://www.qutebrowser.org/).
It displays columns of recently visited URLs, most visited URLs, and bookmarks.
Since Qutebrowser is frequently used with tiling window managers, Qutelaunch
tries it best at shrinking the URLs keeping them recognizable in a window of any
possible dimensions.

## Installation

*TODO*: PyPI and zip?

## Usage

Add these lines to your `config.py`:

```python
import qutelaunch

qutelaunch.init(config, c)
```

The `qutelaunch.init` functions accepts some keyword arguments that modify the
appearance or behaviour of Qutelaunch.

*  `list_length`: The length of the "Recent" and "Most Visited" lists.
*  `color_scheme`:
       The color scheme represented as an instance of the ColorScheme dataclass.
*  `exclude_patterns`:
       The RegEx patterns that describe the URLs to exclude from the "Recent" and
       "Most Visited" lists.
*  `update_timeout`: The timeout in seconds that triggers a regeneration of the file.
*  `recent_timespan`:
       The timespan in seconds that defines which URLs can show up in the "Recent"
       list.
