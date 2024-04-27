class TxtReader():
    def __init__(self):
        pass

    def read_txt_by_lines(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                yield line.strip()
