#!/usr/bin/env python3
def no_c(my_string):
    for i in range(len(my_string)):
        if my_string[i] in "cC":
            del my_string[i]
    return my_string
