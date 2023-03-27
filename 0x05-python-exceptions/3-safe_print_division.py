#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        x = a / b
    except ZeroDivisionError:
        print("Division by zero is error !!")
    finally:
        if (a / b):
            print("Inside result:{:d}".format(a / b))
        else:
            return(None)
