#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_reverse = my_list.reverse()
    for x in list_reverse:
        print("{:d}".format(x))
