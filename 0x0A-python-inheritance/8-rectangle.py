#!/usr/bin/python3
""" Contains the BaseGeometry Class and Rectangle Sub Class """


class BaseGeometry:
    """ BaseGeometry Class """

    def area(self):
        """ Raises exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method that validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    pass
    """inherits from the previous class"""


def __init__(self, width, height):
    BaseGeometry.integer_validator(self, "width", width)
    self.__widht = width

    BaseGeometry.integer_validator(self, "height", height)
    self.__height = height
