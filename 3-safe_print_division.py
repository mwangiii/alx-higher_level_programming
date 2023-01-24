#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        ans = (a/b)

    except ZeroDivisionError:
        print("{} {}".format("Inside result:", "None"))

    finally:
        print("{} {}".format("Inside result:", ans))
