from datetime import datetime
import os
import sys

os.system("")

class Logger:
    def __init__(self):
        self.colors = {
            "WHITE" : '\033[37m',
            "RED" : "\033[31m",
            "YELLOW" : '\033[33m',
            "GREEN" : '\033[32m',
            "END" : "\033[0m"
        }

    def log(self, message, tags="WHITE"):
        time_stamp = datetime.now().strftime("[%H:%M:%S]")
        tags = tags.split()
        color_code = "".join([self.colors[t.upper()] for t in tags])
        print(time_stamp + " - " + color_code + message + self.colors["END"])