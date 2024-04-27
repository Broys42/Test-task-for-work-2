import json

class JsonReader():
    def __init__(self):
        pass

    def read_Json(self, file_Path):
        with open(file_Path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        return data

    def save_Json(self, data, file_Path: str):
        with open(file_Path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
