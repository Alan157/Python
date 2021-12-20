def upper_or_lower(string, num):
    nums = 0
    uppers = 0
    lowers = 0
    symbols = 0
    returned_string = ""
# --------------------------------------------------------------------------------------
    # Checks if this is a string

    if type(string) is not str:
        print("You didnt provide a string in the first parameter.")
        return

# --------------------------------------------------------------------------------------
    # Checks if the provided number (second parameter) is valid

    if(num != 1 and num != 2):
        print("You didnt provide a correct number in the second parameter (only 1 or 2).")
        return

# --------------------------------------------------------------------------------------
    # Sums up the different types of chars in the provided string

    for i in string:
        if((31 < ord(i) < 48) or (57 < ord(i) < 65) or (90 < ord(i) < 97) or (122 < ord(i) < 127)):  # Case for symbols
            symbols += 1
        elif(47 < ord(i) < 58):  # Case for numbers
            nums += 1
        elif(96 < ord(i) < 123):  # Case for lowercase letters
            lowers += 1
        elif(64 < ord(i) < 91):  # Case for uppercase letters
            uppers += 1
# --------------------------------------------------------------------------------------
    # Changes the string according to the provided parameter - 1 for lowercase and 2 for uppercase
    if(num == 1):
        for i in string:
            if(64 < ord(i) < 91):  # Checks if the char is uppercase
                returned_string += chr(ord(i) + 32)  # This will change every uppercase letter into a lowercase one (26 letters + 6 symbols = 32)
            else:
                returned_string += i  # This will concatenate the rest of the letters, the numbers and the symbols
    elif(num == 2):
        for i in string:
            if(96 < ord(i) < 123):  # Checks if the char is lowercase

                returned_string += chr(ord(i) - 32)  # This will change every lowercase letter into a uppercase one (26 letters + 6 symbols = 32)
            else:
                returned_string += i  # This will concatenate the rest of the letters, the numbers and the symbols
#  --------------------------------------------------------------------------------------

    print("Small:", lowers, "\nBig:", uppers, "\nNum:", nums, "\nSymbols:", symbols)
    return returned_string

#  --------------------------------------------------------------------------------------
upper_or_lower("ViTaLi24@!", 2)  # Testing