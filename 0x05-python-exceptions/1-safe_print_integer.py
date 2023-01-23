#!/usr/bin/python3
def safe_print_integer(value):
    x = int
    while True:
        try:
            print("{:d}".format(x))

        except ValueError:
            return False
