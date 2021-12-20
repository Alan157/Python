num = int(input("Please enter a number"))
file = open("new.txt", "w")

for i in range(num):
    file.write("{0}, {1}\n".format(i, num))
    i += 1
    num -= 1
file.close()
