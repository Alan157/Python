from MyStack import MyStack


def bracket_check(string):

    s = MyStack()
    table_open = ["{", "[", "("]
    table_close = ["}", "]", ")"]

    for i in string:
        if i in table_open:
            s.push(i)
        elif i in table_close:  # This checks if the opening and closing brackets match
            if s.is_empty():
                return False
            elif ord(s.top()) == ord("{"):  # case for "{}"
                if ord(i) != ord("}"):
                    return False
                else:
                    s.pop()
            elif ord(s.top()) == ord("["):  # case for "[]"
                if ord(i) != ord("]"):
                    return False
                else:
                    s.pop()
            elif ord(s.top()) == ord("("):  # case for "()"
                if ord(i) != ord(")"):
                    return False
                else:
                    s.pop()

    if s.is_empty():  # At the end, if everything is correct the stack should be empty.
        return True
    else:
        return False
