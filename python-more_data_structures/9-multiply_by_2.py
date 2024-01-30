#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    newdiction = a_dictionary.copy()

    for key in newdiction:
        newdiction[key] = newdiction[key]*2

    return newdiction
