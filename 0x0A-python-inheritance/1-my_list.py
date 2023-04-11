#!/usr/bin/python3
"""New Class"""

class MyList(list):
    """Defining class MyList"""
    def print_sorted(self):
        """public class method to sort the list"""
        print(sorted(self))
