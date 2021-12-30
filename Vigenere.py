import math
"""

This program is used to decrypt and encrypt Vigenere cipher.

Vigenere works like "Caesar Cipher" but with more steps.
In a Caesar Cipher we choose a "key" (number) and than we "move" every letter
by that number on the ABC i.e. plaintext = "crypto", key = 2. The cipher will be
"etarvq".

Vigenere works by making the "key" a word instead of a number.
It "smears" the key word over the plaintext or the cipher before encrypting, attaching every letter a letter
from the key i.e. plaintext = "Hello World", key = "WELCOME". The "smeared" cipher will be
"WELCOMEWEL" (We ignore the spaces)

After this, every letter in the plaintext is "moved" just like in "Caesar Cipher" according to the place in
the ABC of the letter in the key in the "smeared" string i.e. "H" will move 23 places since "W" is the 23rd letter
in the ABC and become "E" (due to rollover)

Parameters:
    string - The plaintext or the cipher
    key - The key used to encrypt or decrypt
    option - 1=encrypt 2=decrypt


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
print(vig("CYBER PRO IS A FUN COURSE", "enigma", 2))

