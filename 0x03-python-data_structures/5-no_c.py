#!/usr/bin/env python3
def no_c(my_string):
<<<<<<< HEAD
    print(my_string.translate({ord(i): None for i in 'Cc'}))
=======
    for i in range(len(my_string)):
        if my_string[i] in "cC":
            del my_string[i]
    return my_string
>>>>>>> 3d21bbe326d60270e06075f8a6a208a391dbcfe0
