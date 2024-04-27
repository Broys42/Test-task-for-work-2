from User import UserSettings
from Athlete import Athlete
from Result import Result

class Model():
    def __init__(self):
        self.userSettings = UserSettings()
        self.athlethes : dict[int, Athlete] = {}
        self.results : dict[int, Result] = {}
