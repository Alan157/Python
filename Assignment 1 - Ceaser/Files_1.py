
string = input("please enter name of the desired text file to duplicate")
read_file = open(string, "r")

string = string[0:len(string)-4]  # This is used to slice the ".txt" form the new file name.q

new_file = open("{0} (2).txt".format(string), "w")  # This opens the new file with original name plus a "(2)" at the end of it.
new_file.write(read_file.read())  # This writes all of the data in the original file into the new one.

read_file.close()
new_file.close()

