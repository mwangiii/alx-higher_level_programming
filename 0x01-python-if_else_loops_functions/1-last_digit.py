#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# The string Last digit of, followed by
# the number, followed by
# the string is, followed by the last digit of number, followed by
# if the last digit is greater than 5: the last digit of the number,is_,and is greater than 5
last_digit = number % 10
if last_digit > 5:
    print('Last digit of {:d} is {:d} is greater than 5'.format(number)(last_digit))
# if the last digit is 0: the last digit of the number,is_ and is 0
elif last_digit == 0:
    print('Last digit of {:d} is {:d} is 0'.format(number)(last_digit))
# if the last digit is less than 6 and not 0: the last digit of the number,is_,and is less than 6 and not 0
else:
    print('Last digit of {:d} is {:d} is less than 6 and not 0'.format(number)(last_digit))
