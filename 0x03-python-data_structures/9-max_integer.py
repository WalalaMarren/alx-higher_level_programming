#!/usr/bin/python3
def max_integer(my_list=[]):
    max_number = my_list[0]
    for x in my_list:
        if x > max_number:
            return x
