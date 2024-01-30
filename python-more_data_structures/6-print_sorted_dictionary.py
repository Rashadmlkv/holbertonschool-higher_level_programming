#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    newlist = [i for i in a_dictionary]
    newlist.sort()

    for i in newlist:
        print("{}: {}".format(i, a_dictionary[i]))
