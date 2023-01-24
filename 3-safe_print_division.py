#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        ans = (a/b)
        print("{} {}".format("Inside result", ans))

    except ZeroDivisionError:
        print("{} {}".format("Inside result:", "None"))

    finally:
        return ans
