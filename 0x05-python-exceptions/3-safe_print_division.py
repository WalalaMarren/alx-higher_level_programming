#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        a / b
    except ZeroDivisionError:
        print("Division by zero is error !!")
    finally:
        print("Inside result: {:d}".format(a / b))
