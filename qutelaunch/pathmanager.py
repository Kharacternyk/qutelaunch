from os import getenv
from os import makedirs


class PathManager:
    def __init__(self):
        # TODO Make read-only via properties or in another way
        self.data_home = getenv("XDG_DATA_HOME", getenv("HOME") + "/.local/share")
        self.qutebrowser_data_home = self.data_home + "/qutebrowser"
        self.qutebrowser_history_db = self.qutebrowser_data_home + "/history.sqlite"
        self.qutelaunch_data_home = self.data_home + "/qutelaunch"
        self.qutelaunch_startpage = self.qutelaunch_data_home + "/startpage.html"

        makedirs(self.qutelaunch_data_home, exist_ok=True)
