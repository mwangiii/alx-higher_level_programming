#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
        first_name and last_name must be strings otherwise
        raise TypeError(first_name must be a string)
        or (last_name must be a string)
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    elif type(last_name) != str:
        raise TypeError("last_name must be a string")

    else:
        print("My name is {} {}").format(first_name, last_name)
