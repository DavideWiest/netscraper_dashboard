from pathlib import Path
import json
import psutil
from datetime import datetime

class LogReader():
    def __init__(self, logdir):
        self.logdir_path = Path(logdir)

        self.json_path = logdir / "log.json"
        self.settings_path = logdir / "settings.json"

    def openlog(self, logpath):
        with open(str(logpath), "r", encoding="utf-8") as f:
            file = json.load(f)
        return file

    def get_whole_jsonlog(self):
        jsonlog = self.openlog(self.json_path)

        jsonlog = jsonlog["Documents"][:100]
        for i, site in enumerate(jsonlog):
            dt = site["DateTime"].replace("T", " ").split(".")[0]
            jsonlog[i]["DateTime"] = dt
            dt_obj = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
            jsonlog[i]["dt_obj"] = dt_obj

            if i != 0:
                dt_dif = (dt_obj - jsonlog[i-1]["dt_obj"]).total_seconds()
                dt_dif = float(f"{dt_dif:.3f}")
            else:
                dt_dif = 0.0

            jsonlog[i]["dt_dif"] = dt_dif

        for i in range(len(jsonlog)):
            del jsonlog[i]["dt_obj"]

        return jsonlog

    def get_complete_stats(self):
        jsonlog = self.openlog(self.json_path)
        settings = self.openlog(self.settings_path)
        cstats = {
            "cpu": psutil.cpu_percent(),
            "ram": psutil.virtual_memory().percent
        }

        settings["StartedScraping"] = settings["StartedScraping"].replace("T", " ").split(".")[0]
        dt = datetime.strptime(settings["StartedScraping"], "%Y-%m-%d %H:%M:%S")
        settings["scraper_running_since"] = f"{(datetime.now() - dt).total_seconds() / 3600:2f}"

        jsonlog = jsonlog["Documents"][:100]
        for i, site in enumerate(jsonlog):
            dt = site["DateTime"].replace("T", " ").split(".")[0]
            jsonlog[i]["DateTime"] = dt
            dt_obj = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
            jsonlog[i]["dt_obj"] = dt_obj

            if i != 0:
                dt_dif = (dt_obj - jsonlog[i-1]["dt_obj"]).total_seconds()
                dt_dif = round(dt_dif*1000)
            else:
                dt_dif = 0.0

            jsonlog[i]["dt_dif"] = dt_dif

        for i in range(len(jsonlog)):
            del jsonlog[i]["dt_obj"]

        cstats["average_ttc"] = sum(jsonlog[i]["dt_dif"] for i in range(len(jsonlog))) / len(jsonlog)

        return {
            "log": jsonlog,
            "settings": settings,
            "comp": cstats
        }