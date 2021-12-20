class Student:

    def __init__(self):
        self.__firstName = ""
        self.__lastName = ""
        self.__age = 0
        self.__grade = 0

    def get_firstName(self):
        return self.__firstName

    def get_lastName(self):
        return self.__lastName

    def get_age(self):
        return self.__age

    def get_grade(self):
        return self.__grade

    def set_firstName(self, name):
        self.__firstName = name

    def set_lastName(self, name):
        self.__lastName = name

    def set_age(self, age):
        self.__age = age

    def set_grade(self, grade):
        self.__grade = grade

    def update_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("The grade must be between 0-100")
            return

    def update_firstName(self, name):
        if len(name) > 10:
            print("The first name cannot contain more than 10 characters")
            return
        else:
            self.__firstName = name

    def update_lastName(self, name):
        if len(name) > 20:
            print("The last name cannot contain more than 20 characters")
            return
        else:
            self.__lastName = name

    def __str__(self):
        return "Fisrt name : {}\nLast name : {}\nAge : {}" \
               "\nGrade : {}".format(self.__firstName, self.__lastName, self.__age, self.__grade)





