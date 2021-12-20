class MyStack:
    def __init__(self):
        self.__arr = []

    def push(self, to_push):
        self.__arr.append(to_push)

    def pop(self):
        if self.is_empty():
            return None
        return self.__arr.pop()

    def is_empty(self):
        if len(self.__arr) == 0:
            return True
        else:
            return False

    def top(self):
        if self.is_empty():
            return None
        return self.__arr[-1]

    def __str__(self):
        to_return = ""
        index = 0

        print("Stack items: ")
        for i in range(len(self.__arr)):
            to_return += str(self.__arr[len(self.__arr) - 1 - i ]) + ", "
        return to_return
