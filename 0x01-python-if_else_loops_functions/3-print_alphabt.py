# Print all the letters except q(113) and e (101)
# You can only use one print function with string format
# You can only use one loop in your code
# You are not allowed to store characters in a variable
# You are not allowed to import any module

#!/usr/bin/python3
for i in range(97, 123):
    if i == 101 | i == 113:
        continue
    else:
        print("{:c}".format(i), end="")