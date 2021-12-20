class element():

    def __init__(self):
        self.__row = 0
        self.__col = 0
        self.__letter = ""

    def get_row(self):
        return self.__row

    def get_col(self):
        return self.__col

    def get_letter(self):
        return self.__letter

    def set_row(self, row):
        self.__row = row

    def set_col(self, col):
        self.__col = col

    def set_letter(self, letter):
        self.__letter = letter

    def move_row(self, new_row):  # Changes the row to a given row ("new_row"). might check in the main func for abs
        if new_row >= 5:
            print("There are only 5 rows (0-4)")
            return
        else:
            self.__row = new_row