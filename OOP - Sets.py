import datetime


class Set:

    def __init__(self):
        self.__arr = []
        self.__size = 0
        self.__lastTimeAdded = ""

    def __str__(self):
        return str(self.__arr)

    def getArr(self):
        return self.__arr

    def getSize(self):
        return self.__size

    def getTime(self):
        return self.__lastTimeAdded

    def setArr(self, arr2):
        self.__arr = arr2

    def setSize(self, size2):
        self.__size = size2

    def setTime(self, time):
        self.__lastTimeAdded = time

    def addElement(self, elem):
        if not isinstance(elem, int):
            print("Please make sure you are trying to add an integer")
            return
        elif elem in self.__arr:
            print("This element is already in the set")
            return
        # at this point we can be sure that elem is an integer and is not in the current set

        self.__arr.append(elem)
        self.__lastTimeAdded = datetime.datetime.now()
        self.__size += 1

    def removeElement(self, elem):

        if not isinstance(elem, int):
            print("Please make sure you are trying to remove an integer")
            return
        elif elem not in self.__arr:
            print("This element is not in the set")
            return
        # at this point we can be sure that elem is an integer and is in the current set
        self.__arr.remove(elem)
        self.__size -= 1

