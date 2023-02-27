#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
        first_name and last_name must be strings otherwise
    """

    if not isinstance(first_name, str):
        TypeError ("first_name must be a string ")

    if not isinstance(last_name):
        TypeError("last_name must be a string ")

    print("My name is {} {}".format(first_name, last_name))