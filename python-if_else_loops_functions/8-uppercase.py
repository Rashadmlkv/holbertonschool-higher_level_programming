#!/usr/bin/python3
def uppercase(str):
    """prints a string in uppercase followed by a new line."""
    for i in range(len(str)):
        if (str[i] >= 'a' and str[i] <= 'z'):
            upper = chr(ord(str[i]) - 32)
        else:
            upper = str[i]
        if (i != len(str) - 1):
            print(f"{upper}", end='')
        else:
            print(f"{upper}")
