
def encode_decode(num):

    """"
        This function is used to encode and decode depending on which parameter is passed:
        1 for encode and 2 for decode.
    """
    """
        SHOULD CHANGE THE ENCODE AND DECODE CHECKS TO BE ONLY ONCE WITH 2 DIFFERENT LOOPS!!!
        SHOULD PASS THE KEY AND FILENAME TO THIS FUNC
    """
    key = 0  # might be useless
    given_file_name = ""  # might be useless
    encoded_decoded = ""

    key = int(input("Please choose the key(an integer): "))
    if key > 25:
        key = int(key % 26)  # We want to normalize the key by removing all of the '26s' in it via modulo

    given_file_name = input("Please enter the name of the file you wish to Encode: \n")
    given_file = open(given_file_name, "r")
    string_encode_decode = given_file.read()  # We read the string form the file

    for i in string_encode_decode:
        if 96 < ord(i) < 123:  # Case for lower case letters
            if num == 1:  # Case for encode
                if ord(i) + key > 122:  # Case for an encode that results in a letter that is out of bounds
                    encoded_decoded += chr(ord(i) + key - 26)  # In case the letter is out of bounds (after 'z') we want to cycle the letters that we encode by subtracting 26
                else:
                    encoded_decoded += chr(ord(i) + key)
            elif num == 2:  # Case for decode
                if ord(i) - key < 97:  # Case for an encode that results in a letter that is out of bounds
                    encoded_decoded += chr(ord(i) - key + 26)  # In case the letter is out of bounds (before 'a') we want to cycle the letters that we decode by adding 26
                else:
                    encoded_decoded += chr(ord(i) - key)
        elif 64 < ord(i) < 91:  # Case for lower case letters
            if num == 1:  # Case for encode
                if ord(i) + key > 90:  # Case for an encode that results in a letter that is out of bounds
                    encoded_decoded += chr(ord(i) + key - 26)  # In case the letter is out of bounds (after 'Z') we want to cycle the letters that we encode by subtracting 26
                else:
                    encoded_decoded += chr(ord(i) + key)
            elif num == 2:  # Case for decode
                if ord(i) - key < 65:  # Case for an encode that results in a letter that is out of bounds
                    encoded_decoded += chr(ord(i) - key + 26)  # In case the letter is out of bounds (before 'A') we want to cycle the letters that we decode by adding 26
                else:
                    encoded_decoded += chr(ord(i) - key)
        else:
            encoded_decoded += i  # We dont encode/decode non-letters so we can concatenate as is
    given_file.close()
    given_file_name = given_file_name[0:len(given_file_name)-4]  # This is to remove the ".txt" from the name of the new file
    if num == 1:
        new_file = open("{0} Encode.txt".format(given_file_name), "w")
    elif num == 2:
        new_file = open("{0} Decode.txt".format(given_file_name), "w")
    new_file.write(encoded_decoded)
    new_file.close()
#  -----------------------------------------------------------------------------------------------------------------------------------

option = 0

while option != 3:
    print("Please choose one of the following:\n1) Encode a file\n2) Decode a file\n3) Exit\n")
    option = int(input("Option number: "))

    if option == 1:
        encode_decode(option)
        print("File encoded!")
    elif option == 2:
        encode_decode(option)
        print("File decoded!")
    else:
        print("Please choose a valid option!\n")

print("Exiting.")

