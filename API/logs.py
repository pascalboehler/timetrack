from datetime import date, datetime, time
import os
from os.path import exists as file_exists

class Log:

    def __init__(self, class_logging):
        self._class_logging = class_logging
        self.appendLine(f"{date.today()} - {self._class_logging} - INFO - Logging started\n")

    def debug(self, message):
        self.appendLine(f"{date.today()} - {self._class_logging} - DEBUG - {message}\n")

    def info(self, message):
        self.appendLine(f"{date.today()} - {self._class_logging} - INFO - {message}\n")

    def warning(self, message):
        self.appendLine(f"{date.today()} - {self._class_logging} - WARNING - {message}\n")

    def error(self, message):
        self.appendLine(f"{date.today()} - {self._class_logging} - ERROR - {message}\n")

    def critical(self, message):
        self.appendLine(f"{date.today()} - {self._class_logging} - CRITICAL - {message}\n")

    def appendLine(self,line):
        if file_exists(f"./logs/{date.today().year}/{date.today().month}/{date.today()}.log"):
            file = open(f"./logs/{date.today().year}/{date.today().month}/{date.today()}.log", 'a')
            file.write(line)
            file.close() # IMPORTANT: Close file after writing, to prevent issues with different instances of this class!
        else:
            if not file_exists(f"./logs/{date.today().year}/{date.today().month}"):
                os.makedirs(f"./logs/{date.today().year}/{date.today().month}")
            file = open(f"./logs/{date.today().year}/{date.today().month}/{date.today()}.log", 'w')
            file.write(line)
            file.close() # IMPORTANT: Close file after writing, to prevent issues with different instances of this class!
