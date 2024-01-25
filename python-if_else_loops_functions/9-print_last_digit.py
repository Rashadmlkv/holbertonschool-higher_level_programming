#!/usr/bin/python3
def print_last_digit(number):
    """prints the last digit of a number."""
    num = int(str(number)[-1])
    print(num, end = '')
    return num
