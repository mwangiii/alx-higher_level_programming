#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for i in range(x):

        try:
            print("{:d}".format(x))
            print(my_list[0:0])

        except IndexError:
            print("{:d}".format(x))
            print("{:d}".format(my_list=[]))
