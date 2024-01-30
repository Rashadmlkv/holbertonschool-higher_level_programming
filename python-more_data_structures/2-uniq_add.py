#!/usr/bin/python3

def uniq_add(my_list=[]):

    if (len(my_list) != 0):
        newlist = set()
        newlist = set(my_list)
        num = list(newlist)[0]

        for i in list(newlist)[1:]:
            num += i
        return num
