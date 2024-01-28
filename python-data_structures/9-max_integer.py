#!/usr/bin/python3

def max_integer(my_list=[]):
    maximus = my_list[0]

    if (len(my_list) == 0):
        return

    for i in my_list:
        if (i > maximus):
            maximus = i

    return maximus
