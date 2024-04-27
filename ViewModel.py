from User import UserSettings
from Model import Model
from JsonReader import JsonReader
from Athlete import Athlete
from TxtReader import TxtReader
from Result import Result
from PySide6.QtGui import QStandardItem

class ViewModel():
    def __init__(self, model: Model):
        self.userSetting = UserSettings()
        self.__model = model
        self.json_Reader = JsonReader()
        self.txt_Reader = TxtReader()
        self.sorted_list_Of_Athletes : list[Athlete] = []

    def save_File_Of_Athletes(self, file_Path):
        self.dict_For_Save = {}
        for id, athlete in self.__model.athlethes.items():
            self.dict_For_Save[athlete.place] = {
                    "Нагрудный номер": athlete.id,
                    "Имя": athlete.name,
                    "Фамилия": athlete.surname,
                    "Результат": self.slice_Miliseconds(athlete.result.final_time)
                    }

        self.json_Reader.save_Json(self.dict_For_Save, file_Path)


    def change_Selected_File_Of_Athletes(self, file):
        self.__model.userSettings.selected_File_Of_Athletes = file

    def change_Selected_File_Of_Results(self, file):
        self.__model.userSettings.selected_File_Of_Results = file

    def change_Dict_Of_Athlethes(self):
        data = self.json_Reader.read_Json(self.__model.userSettings.selected_File_Of_Athletes)

        for item in data:
            self.__model.athlethes[item] = Athlete(id = item, name = data[item]["Surname"], surname = data[item]["Name"])

    def change_Dict_Of_Results(self):
        for line in self.txt_Reader.read_txt_by_lines(self.__model.userSettings.selected_File_Of_Results):

            #If id exist in results dict
            if line.split()[0] in self.__model.results:
                if line.split()[1] == "start": self.__model.results[line.split()[0]].start_Time = line.split()[2]
                if line.split()[1] == "finish": self.__model.results[line.split()[0]].finish_Time = line.split()[2]
            else:
                if line.split()[1] == "start": self.__model.results[line.split()[0]] = Result(start_Time = line.split()[2])
                if line.split()[1] == "finish": self.__model.results[line.split()[0]] = Result(finish_Time = line.split()[2])

    def calculate_Tooked_Places_By_Athletes(self):
        self.__model.athlethes = dict(sorted(self.__model.athlethes.items(), key=lambda x: (x[1].result.final_time == "", x[1].result.final_time)))

        for place, (_, athlete) in enumerate(self.__model.athlethes.items()):
            athlete.place = str(place+1)

    def slice_Miliseconds(self, time: str):
        if time:
            milliseconds = time.split(".")[1]
            milliseconds = milliseconds[:2]
            print("")
            print(time)
            print(milliseconds)
            print("")
            time = f"{time.split('.')[0]}.{milliseconds}"

            return time
        else:
            return time

    def create_Athletes(self):
        self.change_Dict_Of_Athlethes()
        self.change_Dict_Of_Results()

        for athlete_id, athlete in self.__model.athlethes.items():
            if athlete_id in self.__model.results:
                flag_Start_And_Finish_Exist = True

                #if Start time exist
                if self.__model.results[athlete_id].start_Time:
                    athlete.result.start_Time = self.__model.results[athlete_id].start_Time
                else:
                    flag_Start_And_Finish_Exist = False

                #if Finish time exist
                if self.__model.results[athlete_id].finish_Time:
                    athlete.result.finish_Time = self.__model.results[athlete_id].finish_Time
                else:
                    flag_Start_And_Finish_Exist = False

                #if Start and Finish time exist
                if flag_Start_And_Finish_Exist:
                    athlete.result.calculate_final_time()

                #print(f"ID: {athlete.id}, Имя {athlete.name}, Фамилия, {athlete.surname}, Старт {athlete.result.start_Time}, Финиш {athlete.result.finish_Time}, Результат {athlete.result.final_time}")

    def make_Sorted_Athletes_Model(self):
        for _, athlete in self.__model.athlethes.items():
            yield [QStandardItem(athlete.place),
                   QStandardItem(athlete.id),
                   QStandardItem(athlete.name),
                   QStandardItem(athlete.surname),
                   QStandardItem(self.slice_Miliseconds(athlete.result.final_time))]
