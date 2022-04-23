"""
This program calculates my monthly salary
"""
# This function turns a string of HH:MM into a float that represents time in hours
# 2 ideas: 1) find the semicolon's index and slice according to it.
# 2) check the length of the sting, and slice according to it (length 4 = H:MM, length 5 = HH:MM, length 6 = HHH:MM)


def time_to_float(time):

    hours = 0
    minutes = 0

    try:
        if ":" not in time:  # Added to allow input of HH instead of HH:00
            return float(time)
        hours = float(time[:time.find(":")])  # Slicing the string up to the semicolon
        minutes = float(time[time.find(":") + 1:]) / 60  # Slicing the string from the semicolon
    except ValueError:
        return



    return hours+minutes


while True:  # Assures that the input is a number

    try:
        hourly_pay = int(input("Please enter the hourly pay\n"))
        break
    except ValueError:
        print("Must be a number!")

_100 = 0
_125 = 0
_150 = 0
_175 = 0
_200 = 0
percent_pay = 1.00
total_pay = 0

arr = [_100, _125, _150, _175, _200]
for i in arr:
    while True:
        try:
            arr[i] = input("How many {}% hours do you work?(HH:MM or HH):\n".format(int(percent_pay*100)))
            arr[i] = time_to_float(arr[i])  # Converts a string in the HH:MM or HH format in to a usable float
            total_pay += arr[i] * percent_pay * hourly_pay  #
            break
        except TypeError:
            print("Must be a valid time format!")

    percent_pay += 0.25  # Increases the payment rate by 25 percent
print("{:0.2f}".format(total_pay))  # prints the total pay with only two numbers after the decimal point
