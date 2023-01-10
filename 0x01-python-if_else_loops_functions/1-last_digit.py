#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# The string Last digit of, followed by
string = "Last digit of {} is {} and {}"
# the number, followed by
# the string is, followed by the last digit of number, followed by
lastdigit = number % 10
# if the last digit is greater than 5: the string and is greater than 5
if lastdigit > 5:
    print(string.format(number, lastdigit, "is greater than 5"))
# if the last digit < 6 and not 0: the string and < 6 and not 0
elif lastdigit < 6 and lastdigit != 0:
    print(string.format(number, lastdigit, "is less than 6 and not 0"))
# if the last digit is 0: the string and is 0
else:
    print(string.format(number, lastdigit, "is 0"))
# followed by a new line
