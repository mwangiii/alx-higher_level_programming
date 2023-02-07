#!/usr/bin/python3
class Myclass1(object):
    pass


def lookup(obj):
    obj = 3

    return[Myclass1() for i in range(obj)]


class MyClass2(object):
    my_attr1 = 3

    def my_meth(self):
        pass
