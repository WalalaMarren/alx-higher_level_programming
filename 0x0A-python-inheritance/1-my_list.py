#!/usr/bin/python3
"""This is a subclass Mylist Instantiation"""


class MyList(list):
    """
    Child class Mylist that inherits from list
    Method that prints the list in sorted order, ascending
    """

    def print_sorted(self):
        """
        Fucntion that prints a sorted list
        return: None
        """
        print(self.sort(reverse = True))
