#!/usr/bin/python3
def remove_char_at(str, n):
    """creates copy of string, removes character at the position n"""
    if (n < 0):
        return str
    else:
        leftside = str[:n]
        rightside = str[n + 1:]
        return leftside + rightside
