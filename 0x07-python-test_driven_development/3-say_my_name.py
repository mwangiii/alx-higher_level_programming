#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
        first_name and last_name must be strings otherwise
        raise TypeError(first_name must be a string)
        or (last_name must be a string)
    """

    if first_name != type(str):
        TypeError("first_name must be a string")

    if last_name != type(str):
        TypeError("last_name must be a string")

    print("My name is {} {}").format(first_name, last_name)
