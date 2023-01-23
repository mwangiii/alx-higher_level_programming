#!/usr/bin/python3
def safe_print_integer(value):
    x = int(input("Enter a number"))
    print("{:d}".format())
    try:
        return True

    except ValueError:
        return False
