import os
import datetime as date

class Log:
    # logging uses greenwhich main time!

    timezone: date.tzinfo
    class_logging: str

    def __init__(self, class_logging):
        print("Logging started")
        self.timezone = date.tzinfo.utcoffset(+1) # Timezone BERLIN, AMSTERDAM
        self.class_logging = class_logging

    def debug(self, message):
        print(f"{date.today(self.timezone)} - {self.class_logging} - DEBUG - {message}")

    def info(self, message):
        print(f"{date.today(self.timezone)} - {self.class_logging} - INFO - {message}")

    def warning(self, message):
        print(f"{date.today(self.timezone)} - {self.class_logging} - WARNING - {message}")

    def error(self, message):
        print(f"{date.today(self.timezone)} - {self.class_logging} - ERROR - {message}")

    def critical(self, message):
        print(f"{date.today(self.timezone)} - {self.class_logging} - CRITICAL - {message}")