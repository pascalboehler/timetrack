import datetime as date

class Log:
    # logging uses greenwhich main time!

    timezone: date.tzinfo
    class_logging: str

    def __init__(self, class_logging):
        self.appendLine("Logging started")
        self.timezone = date.tzinfo.utcoffset(+1) # Timezone BERLIN, AMSTERDAM
        self.class_logging = class_logging

    def debug(self, message):
        self.appendLine(f"{date.today(self.timezone)} - {self.class_logging} - DEBUG - {message}")

    def info(self, message):
        self.appendLine(f"{date.today(self.timezone)} - {self.class_logging} - INFO - {message}")

    def warning(self, message):
        self.appendLine(f"{date.today(self.timezone)} - {self.class_logging} - WARNING - {message}")

    def error(self, message):
        self.appendLine(f"{date.today(self.timezone)} - {self.class_logging} - ERROR - {message}")

    def critical(self, message):
        self.appendLine(f"{date.today(self.timezone)} - {self.class_logging} - CRITICAL - {message}")

    def appendLine(self,line):
        file = open(f"./logs/{date.today(self.timezone).year}/{date.today(self.timezone).month}/{date.today(self.timezone)}.log")
        file.write(line)
        file.close() # IMPORTANT: Close file after writing, to prevent issues with different instances of this class!
