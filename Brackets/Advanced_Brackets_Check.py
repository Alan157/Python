from MyStack import MyStack
from Brackets_Check import bracket_check

def bracket_check_single(string):
    # Checks if the brackets in the string are closed correctly and if they adhere to the rules of nested
    # parentheses : "{[()]}"

    # The idea is to build a second string comprised only of the brackets in their order of appearance
    # and then check if they are in the correct mathematical order.

    # There are some basic statements we can use inorder to check:
    # 1) First bracket - If it is a "{" then a "[" MUST follow it, otherwise there is no use for the "{".
    #    If it is a "[" then a "(" MUST follow it
    # 2) Last bracket - If it is a "}" then a "]" MUST come before it, otherwise there is no use for the "}".
    #    If it is a "]" then a ")" MUST come before it

    j = 0
    if not bracket_check(string):
        return False

    # Case for the first bracket
    if string[j] == "{":
        if not string[j + 1] == "[":
            return False
    elif string[j] == "[":
        if not string[j+1] == "(":
            return False
    elif string[j] == "(":  # might be useless
        if not string[j + 1] == ")":
            return False

    # j += 1
    for j in range(1, len(string)-2):  # might be -2 if splitting the case for the last bracket
        if string[j] == "{":
            if not string[j+1] == "[" or not string[j-1] == ")":  # Should be an "and" not an "or" (?)
                return False
        if string[j] == "[":
            if not string[j+1] == "(" or not string[j-1] == "{":  # Should be an "and" not an "or" (?)
                return False
        if string[j] == "(":
            if not string[j+1] == ")" or not string[j-1] == "[":  # Should be an "and" not an "or" (?)
                return False

    j = len(string)-1  # might be useless
    # Case for the last bracket
    #if string[j] in ["{", "[", "("]:
       # return False
    if string[j] == "}":
        if not string[j - 1] == "]":
            return False
    elif string[j] == "]":
        if not string[j - 1] == ")":
            return False
    elif string[j] == ")":  # might be useless
        if not string[j - 1] == "(":
            return False

    return True


# A recursive function that uses "bracket_check_single" to check if the string is correct.
# It should be able to handle a string with multiple groups (a group is between 1 and 3 pairs of brackets)
# of brackets by outsourcing the check of a single group  to the function "bracket_check_single".

# Its going to check what size group it is by the first bracket: "{" = 3 pairs, "[" = 2 pairs and "(" = 1 pair.

# The idea is to slice the string after every outsourcing by the number of pairs * 2 (between 2 and 6 characters)
# and checking the result of the outsourcing, if True, calls itself again with the sliced string, else, return false.

def bracket_check_multiple(string):
    if len(string) % 2 != 0:  # an odd number of elements cannot be correct (brackets should come in pairs)
        return False
    if len(string) == 0:
        return True
    if string[0] == '(':
        if bracket_check_single(string[:2]):
            return bracket_check_multiple(string[2:])
        else:
            return False
    if string[0] == '[':
        if bracket_check_single(string[:4]):
            return bracket_check_multiple(string[4:])
        else:
            return False
    if string[0] == '{':
        if bracket_check_single(string[:6]):
            return bracket_check_multiple(string[6:])
        else:
            return False
    return False  # Should be unreachable since the above cases should cover all of the the options:
                  # 1. The string is empty 2. it contains only brackets.


def bracket_check_main(string):  # This will create the string that "bracket_check_multiple" will use (only brackets)
    
    table = ["{", "[", "(", ")", "]", "}"]
    bracket_string = ""
    
    for i in string:  # Creates a string comprised only of brackets
        if i in table:
            bracket_string += i

    return bracket_check_multiple(bracket_string)

