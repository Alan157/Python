import math
"""



"""
def vig(string, key, option):

    key_ext = ""
    i = 0
    encoded_decoded = ""
    count = 0
    string = string.upper()
    key = key.upper()
    while i < (math.ceil(float(len(string)) / float(len(key)))):
        key_ext += key
        i += 1
        
    if len(string) < len(key_ext):
        # j = len(key_ext) % len(string)
        # length = len(key_ext) - j
        key_ext = key_ext[:len(string)]
    # return key_ext
    # key_ext = key_ext.replace(" ", "")

    if option == 1:
        for i in string:
            if 96 < ord(i) < 123:  # Case for lower case letters

                if ord(i) - (ord(key_ext[count]) - 97) < 97:  # Case for an decode that results in a letter that is out of bounds
                    encoded_decoded += chr(ord(i) - (ord(key_ext[count]) - 97) + 26)  # In case the letter is out of bounds (after 'z') we want to cycle the letters that we encode by subtracting 26
                else:
                    encoded_decoded += chr(ord(i) - (ord(key_ext[count]) - 97))  # We normalize the key to be between 0-25
                count += 1

            elif 64 < ord(i) < 91:  # Case for upper case letters / Might be useless

                if ord(i) - (ord(key_ext[count]) - 65) < 65:  # Case for an encode that results in a letter that is out of bounds
                    encoded_decoded += chr(ord(i) - (ord(key_ext[count]) - 65) + 26)  # In case the letter is out of bounds (after 'Z') we want to cycle the letters that we encode by subtracting 26
                else:
                    encoded_decoded += chr(ord(i) - (ord(key_ext[count]) - 65))  # We normalize the key to be between 0-25
                count += 1

    if option == 2:
        for i in string:
            if 96 < ord(i) < 123:  # Case for lower case letters

                if ord(i) + (ord(key_ext[count]) - 97) > 122:  # Case for an encode that results in a letter that is out of bounds
                    encoded_decoded += chr(ord(i) + (ord(key_ext[count]) - 97) - 26)  # In case the letter is out of bounds (before 'a') we want to cycle the letters that we decode by adding 26
                else:
                    encoded_decoded += chr(ord(i) + (ord(key_ext[count]) - 97))  # We normalize the key to be between 0-25
                count += 1

            elif 64 < ord(i) < 91:  # Case for upper case letters

                if ord(i) + (ord(key_ext[count]) - 65) > 90:  # Case for an encode that results in a letter that is out of bounds
                    encoded_decoded += chr(ord(i) + ord(key_ext[count]) - 65 - 26)  # In case the letter is out of bounds (before 'A') we want to cycle the letters that we decode by adding 26
                else:
                    encoded_decoded += chr(ord(i) + ord(key_ext[count]) - 65)  # We normalize the key to be between 0-25
                count += 1

    return encoded_decoded



print(vig("GLJKDPVBQYMFYAKUGRWR", "enigma", 1))
print(vig("nlazeiibljji", "luck", 1))

