#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry:
    def area(self):
        try:
            print(BaseGeometry().area())
            """ Raising an exception message """

        except Exception as e:
            print("area() is not implemented")
