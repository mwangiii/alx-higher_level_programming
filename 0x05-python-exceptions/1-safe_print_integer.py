#!/usr/bin/python3
def safe_print_integer(value):
    value = int
    while True:
        try:
            print("{:d}".format(value))

        except ValueError:
            return False
