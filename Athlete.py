from Result import Result

class Athlete():
    def __init__(self, id = 0, name = "", surname = ""):
        self.id = id
        self.name = name
        self.surname = surname
        self.result = Result()
        self.place = 0
