#!/usr/bin/python3


"""funftion that returns true
    if obj is instance of a class inherited from
"""


def inherits_from(obj, a_class):
    """ Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class  """

    return issubclass(type(obj), a_class) and type(obj) != a_class
