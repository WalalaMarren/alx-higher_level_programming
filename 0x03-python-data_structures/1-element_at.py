#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 0 or idx not in range(len(my_list))):
        return None
    print("Element at index {:d} is {}".format(idx, my_list[idx]))
