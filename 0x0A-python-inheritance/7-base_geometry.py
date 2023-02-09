#!/usr/bin/python3
""" BaseGeometry Module """


class BaseGeometry:
    """ BaseGeometry Class """

    def area(self):
        """ Raises exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if type(value) is not int:
            """if value in not an int raise TypeError"""
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            """if value is less than o and not equal raise Valueerror"""
            raise ValueError("{} must be greater than 0".format(name))
