#!/usr/bin/python3
""" BaseGeometry Module """


class BaseGeometry:
    """ BaseGeometry Class """

    def area(self):
        """ Raises exception """
        raise Exception("area() is not implemented")

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def integer_validator(self, name, value):
        if value != int:
            """if value in not an int raise TypeError"""
            raise TypeError(name + "must be an integer")

        if value <= 0:
            """if value is less than o and not equal raise Valueerror"""
            raise ValueError(name + "must be greater than o")
