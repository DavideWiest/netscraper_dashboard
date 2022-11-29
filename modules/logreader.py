from pathlib import Path

class LogReader():
    def __init__(self, logdir):
        self.logdir_path = Path(logdir)

        self.csvlog_path = logdir / "log.csv"
        self.jsonlog_path = logdir / "log.json"
        self.controllog_path = logdir / "control.json"

    def openlog(self, logpath):
        with open(logpath, "r", encoding="utf-8") as f:
            file = f.read()
        return file