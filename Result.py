from datetime import (datetime, time)

class Result():
    def __init__(self, start_Time = "", finish_Time = ""):
        self.start_Time = start_Time
        self.finish_Time = finish_Time
        self.final_time = ""

    def calculate_final_time(self):
        start_time = datetime.strptime(self.start_Time, "%H:%M:%S,%f")
        finish_time = datetime.strptime(self.finish_Time, "%H:%M:%S,%f")
        self.final_time = str(finish_time - start_time).replace("0:", "", 1)
