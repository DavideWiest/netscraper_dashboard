from pathlib import Path
import json
import psutil

class LogReader():
    def __init__(self, logdir):
        self.logdir_path = Path(logdir)

        self.json_path = logdir / "log.json"
        self.settings_path = logdir / "settings.json"

    def openlog(self, logpath):
        with open(str(logpath), "r", encoding="utf-8") as f:
            file = json.load(f)
        return file


    def get_stats(self):
        jsonlog = self.openlog(self.json_path)
        settings = self.openlog(self.settings_path)
        cstats = {
            "cpu": f"{psutil.cpu_percent()}%",
            "ram": f"{psutil.virtual_memory().percent}%"
        }

        return {
            "log": jsonlog,
            "settings": settings,
            "pc": cstats
        }