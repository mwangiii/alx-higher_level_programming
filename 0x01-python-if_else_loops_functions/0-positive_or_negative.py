#!/usr/bin/python3
import random
number = random.randint(-10, 10)
#if the number is greater than 0: is positive
if number > 0:
	print('is positive\n')
#if the number is 0: is zero
elif number == 0:
	print('is zero\n')
#if the number is less than 0: is negative
else:
	print('is negative\n')
#followed by a new line
