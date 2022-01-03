
"""
This program can encrypt and decrypt text via the "playfair" cipher.

The method takes a string that contains either plaintext or cipher, a key and an option to encode or decode.

We use the key and, without repeating letters, we write it as a 5x5 matrix and complete the rest of the spaces
with the rest of the ABC, excluding "J" (if "J" is a part of the key we replace it with "I"). I.e. key = Repeater
the matrix will look like this:
(R E P A T)
(B C D F G)
(H I K L M)
(N O Q S U)
(V W X Y Z)

Now we pair the letters in the plaintext or cipher with one another, each one with the one next to it,
If we have two of the same letter that will end up in a pair, we put an "X" in between them to avoid them pairing.
if there an odd number of letters we add an "X" to the end to pair with the last letter.

Now we can start encoding or decoding.

Encoding works like this:
We take each pair and check their place in relation to one another.
1)If they are in the same column, we replace each letter in the pair with the one below it in the matrix (in a cyclic manner)
2)If they are in the same row, we replace each letter in the pair with the one right to it in the matrix (in a cyclic manner)
3) if they are in a different row and column, we create a square between them as such that they will be at opposite ends
of the square: i.e. pair = QG so the square will look like this: (D F G) then, we swap the letters with their opposites
in the same row, I.e. G for D and Q for U.                       (K L M)
                                                                 (Q S U)
Decoding the just the reverse process.

Parameters:
    string - plaintext or cipher
    key - the "password" to build the matrix with
    option - 1=encode 2=decode
"""
def playfair(string, key, option):
    key_normal = ""
    charset = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    row_1 = 0
    row_2 = 0
    k = 0
    a = 0
    b = 0
    returned_string = ""
    odd_flag = False
    c = 0

    string = string.replace(" ", "")

    # Adding an X after the first letter in a pair of the same letter
    while c < len(string)-1:
        if string[c] == string[c+1]:
            string = string[:c+1] + "X" + string[c+1:]
        c += 2

    print(string)  # for testing

    if len(string) % 2 != 0:  # if the string has an odd number of letters we add an X to make it an even number
        string += "X"
        odd_flag = True

    print(string)  # for testing

    for i in key:  # Removes all duplicate letters from the key
        if i not in key_normal:
            key_normal += i
    key_normal = key_normal.replace("J", "I")  # In case we have a "J" we need to replace it with an "I"

    m = [[],
         [],
         [],
         [],
         []]  # Matrix to fill with letters

    key_normal = key_normal[::-1]  # reversing the string for concatenating
    for i in key_normal:
        charset = charset.replace(i, "")  # Removes the letters of key from the charset
        charset = i + charset  # concatenates the first letter of the key to the beginning of the charset

    while a < 5:  # fills the matrix with the letters
        while b < 5:
            m[a].append(charset[k])
            k += 1
            b += 1
        a += 1
        b = 0

    """
        Same row -> Same list
        Same column -> Different list but same index
    """
    # Encrypting
    if option == 1:

        a = 0
        while a < len(string):  # a is index
            for i in range(5):  # Case for same row
                if string[a] in m[i] and string[a + 1] in m[i]:

                    if m[i].index(string[a])+1 > 4:  # Cyclic motion
                        returned_string += m[i][0]  # Concatenates the first letter in the row
                    else:
                        returned_string += m[i][m[i].index(string[a])+1]  # Concatenates one letter to the right

                    if m[i].index(string[a+1])+1 > 4:  # Cyclic motion
                        returned_string += m[i][0]
                        a += 2  # The iterator is incremented by 2 since we check in pairs
                        continue  # No need to check for other cases
                    else:
                        returned_string += m[i][m[i].index(string[a+1]) + 1]
                        a += 2
                        continue

            # Case for same Column
            # Also used for the final case (different row and column) so no condition here
            for i in range(5):  # Finds the row of string[a]
                if string[a] in m[i]:
                    row_1 = i
                    break

            for i in range(5):  # Finds the row of string[a+1]
                if string[a+1] in m[i]:
                    row_2 = i
                    break

            if m[row_1].index(string[a]) == m[row_2].index(string[a+1]):  # Check for same column

                if row_1+1 > 4:  # Cyclic motion
                    returned_string += m[0][m[row_1].index(string[a])]  # Concatenates same index(column) but in the first row
                else:
                    returned_string += m[row_1+1][m[row_1].index(string[a])]  # Concatenates 1 row down, same index(column)

                if row_2+1 > 4:
                    returned_string += m[0][m[row_2].index(string[a+1])]
                    a += 2  # The iterator is incremented by 2 since we check in pairs
                    continue  # No need to check for other cases
                else:
                    returned_string += m[row_2+1][m[row_2].index(string[a+1])]
                    a += 2
                    continue

            # If we got here then string[a] and string[a+1] are in different rows and different columns

            returned_string += m[row_1][m[row_2].index(string[a+1])]  # Concatenates same row but a+1 index(column)
            returned_string += m[row_2][m[row_1].index(string[a])]  # Concatenates same row but a index(column)
            a += 2

        return returned_string

    if option == 2:

        a = 0
        while a < len(string):  # a is index
            for i in range(5):  # Case for same row
                if string[a] in m[i] and string[a + 1] in m[i]:

                    if m[i].index(string[a]) - 1 < 0:  # Cyclic motion
                        returned_string += m[i][4]  # Concatenates the first letter in the row
                    else:
                        returned_string += m[i][m[i].index(string[a]) - 1]  # Concatenates one letter to the left

                    if m[i].index(string[a + 1]) - 1 < 0:  # Cyclic motion
                        returned_string += m[i][4]
                        a += 2  # The iterator is incremented by 2 since we check in pairs
                        continue  # No need to check for other cases
                    else:
                        returned_string += m[i][m[i].index(string[a + 1]) - 1]
                        a += 2
                        continue

            # Case for same Column
            # Also used for the final case (different row and column) so no condition here
            for i in range(5):  # Finds the row of string[a]
                if string[a] in m[i]:
                    row_1 = i
                    break

            for i in range(5):  # Finds the row of string[a+1]
                if string[a + 1] in m[i]:
                    row_2 = i
                    break

            if m[row_1].index(string[a]) == m[row_2].index(string[a + 1]):  # Check for same column

                if row_1 - 1 < 0:  # Cyclic motion
                    returned_string += m[4][m[row_1].index(string[a])]  # Concatenates same index(column) but in the last row
                else:
                    returned_string += m[row_1 - 1][m[row_1].index(string[a])]  # Concatenates 1 row up, same index(column)

                if row_2 - 1 < 0:
                    returned_string += m[4][m[row_2].index(string[a + 1])]
                    a += 2  # The iterator is incremented by 2 since we check in pairs
                    continue  # No need to check for other cases
                else:
                    returned_string += m[row_2 - 1][m[row_2].index(string[a + 1])]
                    a += 2
                    continue

            # If we got here then string[a] and string[a+1] are in different rows and different columns

            returned_string += m[row_1][m[row_2].index(string[a + 1])]  # Concatenates same row but a+1 index(column)
            returned_string += m[row_2][m[row_1].index(string[a])]  # Concatenates same row but a index(column)
            a += 2

        return returned_string


print(playfair("THISCOURSEISABOUTCONFIDENTIALITY","DETERIORATION",1))
